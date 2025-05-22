import transformers
transformers.logging.set_verbosity_info()
import os
import gc
import re
import sys
import json
import wandb
# os.environ["WANDB_DISABLED"] = "true"
import torch
import logging
import argparse
import numpy as np
import transformers
import pandas as pd
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    TrainingArguments,
    Seq2SeqTrainingArguments,
    EarlyStoppingCallback,
)
from tqdm import tqdm
from functools import partial
from trl import SFTTrainer
from transformers import BitsAndBytesConfig
# from datasets import load_dataset
from accelerate import Accelerator
from torch.utils.data import DataLoader
from transformers.trainer_utils import get_last_checkpoint, set_seed
from transformers.integrations import WandbCallback
from unsloth import FastLanguageModel, is_bfloat16_supported
from unsloth.chat_templates import get_chat_template
from transformers import TextStreamer
from load_dataset import load_dataset
from load_eval_metrics import load_dataset_metrics
# from peft import LoraConfig, get_peft_model
from LLaMATrainer import LLaMATrainer
from transformers import TrainingArguments, DataCollatorForSeq2Seq
# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
from unsloth.chat_templates import standardize_sharegpt
from copy import deepcopy


def parse_args():
    parser = argparse.ArgumentParser(description="Train LLaMA with customizable settings.")

    # Add argument to specify config file
    parser.add_argument("--config_file", type=str, help="Path to config file (JSON format)")
    # Add argument for specifying the experiment path with a default value
    parser.add_argument("--experiment_path", type=str, default="/scratch/spati/tmp/LLaMA/checkpoints/inst_guideline_PS_Adv_w_NS_rank_128_alpha_64_lr_1e-05/", help="Direct path to the experiment to resume training.")
    # PWITHNS: /scratch/spati/tmp/LLaMA/checkpoints/inst_guideline_P_w_NS_rank_128_alpha_64_lr_1e-05/
    #PNWITHNS: /scratch/spati/tmp/LLaMA/checkpoints/inst_guideline_PN_w_NS_rank_128_alpha_64_lr_1e-05/
    #PSWITHNS: /scratch/spati/tmp/LLaMA/checkpoints/inst_guideline_PS_w_NS_rank_128_alpha_64_lr_1e-05/
    #PNADVWITHNS: /scratch/spati/tmp/LLaMA/checkpoints/inst_guideline_PN_Adv_w_NS_rank_128_alpha_64_lr_1e-05/
    #PSADVWITHNS: /scratch/spati/tmp/LLaMA/checkpoints/inst_guideline_PS_Adv_w_NS_rank_128_alpha_64_lr_1e-05/

    # Basic Parameters
    parser.add_argument("-v", "--llama_version", choices=["LLaMA 2", "LLaMA 3"], default="LLaMA 2", help="Specify LLaMA version.")
    parser.add_argument("-p", "--model_parameters", default="7B", help="Model size parameters like 7B, 13B.")
    
    # Optimization
    parser.add_argument("-o", "--optimization", choices=["LoRA", "QLoRA"], default="LoRA", help="PEFT Optimization technique.")
    parser.add_argument("-m", "--max_seq_length", type=int, default=3000, help="Maximum sequence length for inputs.") #make it 3000 for everything - Kept 1500 for RQ4(event suffles not the arg suffling) for remaining args suffling changed to 3000
    parser.add_argument("-b", "--load_in_4bit", type=bool, default=True, help="Load model in 4-bit precision.")
    
    # LoRA Parameters
    parser.add_argument("-a", "--lora_alpha", type=int, default=64, help="Scaling factor for LoRA updates.")
    parser.add_argument("-r", "--lora_rank", type=int, default=128, help="Rank size for LoRA matrix.")
    parser.add_argument("-d", "--lora_dropout", type=float, default=0, help="Dropout for LoRA layers.")
    parser.add_argument("-t", "--target_modules", nargs='+', default=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"], help="Target modules for LoRA.")
    parser.add_argument("-l", "--use_rslora", type=bool, default=True, help="Use Rank-Stabilized LoRA.")
    
    # Advanced Features
    parser.add_argument("-c", "--use_gradient_checkpointing", type=bool, default=True, help="Use gradient checkpointing.")
    parser.add_argument("--early_stopping", type=bool, default=True, help="Enable early stopping based on evaluation metrics.")
    parser.add_argument("--quantization", choices=["8bit", "4bit"], help="Choose quantization type.")
    
    # Dataset and Evaluation
    parser.add_argument("--dataset_name", type=str, default="guideline_PS_Adv_w_NS", help="Dataset name for training.")
    parser.add_argument("--eval_metrics", nargs='+', default=["accuracy", "f1"], help="Custom evaluation metrics.")
    
    # Advanced training arguments for flexibility
    parser.add_argument("--fp16", type=bool, default=False, help="Enable mixed precision training with float16.")
    parser.add_argument("--learning_rate", type=float, default=1e-5, help="Learning rate.")
    parser.add_argument("--lr_scheduler_type", choices=["linear", "cosine", "polynomial"], default="cosine", help="Type of learning rate scheduler.")
    parser.add_argument("--warmup_steps", type=int, default=0, help="Number of steps for warmup.")
    parser.add_argument("--save_steps", type=int, default=1000, help="Save checkpoint every X steps.")
    parser.add_argument("--eval_steps", type=int, default=500, help="Evaluate every X steps.")
    parser.add_argument("--patience", type=int, default=3, help="Number of eval steps for early stopping patience.")
    parser.add_argument("--per_device_train_batch_size", type=int, default=32, help="Training batch size.")
    parser.add_argument("--per_device_eval_batch_size", type=int, default=50, help="Eval batch size.")

    # Arguments for train/valid
    parser.add_argument("--do_resume_train", type=bool, default=True, help="Should we train?")
    parser.add_argument("--do_eval", type=bool, default=True, help="Should we eval?")
    args = parser.parse_args()
    
    # Load args from config file if provided
    if args.config_file:
        logger.info(f"Loading config file: {args.config_file}")
        with open(args.config_file, 'r') as f:
            config_args = json.load(f)
        
        # Update the argparse args with the values from config file
        for key, value in config_args.items():
            if not hasattr(args, key):  # Skip invalid keys
                logger.warning(f"Invalid config key: {key}. Ignoring.")
            else:
                setattr(args, key, value)
    
    return args


def parse_model_info(args):
    """Return model path based on version and size."""
    model_map = {
        "LLaMA 2": f"meta-llama/Meta-Llama-2-{args.model_parameters}",
        "LLaMA 3": f"meta-llama/Meta-Llama-3-{args.model_parameters}",
    }
    model_path = model_map.get(args.llama_version)
    if not model_path:
        raise ValueError(f"Invalid LLaMA version: {args.llama_version}")
    return model_path

def map_dataset_to_template(dataset, tokenizer, key = "conversations", dataset_type = "train"):
    # print(f"Doing padding to the {tokenizer.padding_side} for {dataset_type}")
    def apply_template(examples, tokenizer, key):
        # print("examples", examples)
        messages = examples[key]
        # print("messages", messages)
        #if dataset_type == "train" else text.replace(tokenizer.eos_token)
        texts = [tokenizer.apply_chat_template(message, tokenize = False, add_generation_prompt = False) for message in messages]
        # print("*"*50)
        # print("texts")
        # print(texts)
        # xx
        return { "text" : texts, }#{"text":[t if dataset_type == "train" else (''.join(t.rsplit(tokenizer.eos_token, 1))).strip() + "\n" for t in text]}
    # Log the number of examples processed
    # logger.info(f"Original dataset size: {len(dataset)}")
    processed_dataset = dataset.map(partial(apply_template, tokenizer=tokenizer, key=key), batched=True)
    # logger.info(f"Processed dataset size: {len(processed_dataset)}")
    # Ensure tokenizer is set to left-padding for non-train tasks when required (especially for generation)
    return processed_dataset#dataset.map(partial(apply_template, tokenizer=tokenizer, key=key), batched=True)

from unsloth.chat_templates import train_on_responses_only
instruction_response_mapper = {
    "LLaMA3_1":{
    "instruction_part": "<|start_header_id|>user<|end_header_id|>\n\n",
    "response_part": "<|start_header_id|>assistant<|end_header_id|>\n\n"
    }

}

def prepare_lora_model(args, model):
    """Prepare model with LoRA or QLoRA configuration."""
    model = FastLanguageModel.get_peft_model(
    model,
    r = args.lora_rank,
    lora_alpha = args.lora_alpha,
    lora_dropout = args.lora_dropout,
    target_modules = args.target_modules, 
    use_rslora = args.use_rslora,
    use_gradient_checkpointing = "unsloth" if args.use_gradient_checkpointing else False 
    )
    config = ""
    config += f"LoRA Rank -> {args.lora_rank}\n"
    config += f"LoRA ⍺ -> {args.lora_alpha}\n"
    config += f"LoRA dropout -> {args.lora_dropout}\n"
    config += f"Target Modules -> {args.target_modules}\n"
    config += f"Use RSLoRA -> {args.use_rslora}\n"
    config += f"Use Gradient Checkpointing -> {args.use_gradient_checkpointing}\n"
    logger.info(f"LoRA/QLoRA optimization applied with config\n{'-*'*75}\n{config}{'-*'*75}")
    return model

def main(args):
    # wandb.init(project = "LLaMAEvents_Degree", name = f"LLaMA_3.1-8B_{args.dataset_name}", entity = "LLaMAEvents")
    wandb.init(project="LLaMAEvents", name=f"LLaMA_3.1-8B_{args.dataset_name}", entity="LLaMAEvents")

    # model_name_or_path = "unsloth/Meta-Llama-3.1-8B-bnb-4bit"#parse_model_info(args)

    model_name_or_path = "unsloth/llama-3-8b-Instruct-bnb-4bit"
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    logger.info(f"Using device: {device}")
    
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name = model_name_or_path, max_seq_length=args.max_seq_length, load_in_4bit=args.load_in_4bit, dtype = None, cache_dir = "./original_models")
    # tokenizer.padding_side = "left"
    # Prepare model with LoRA or QLoRA
    model = prepare_lora_model(args, model)
    
    # logger.info(f"We will train a total of {model.print_trainable_parameters()} parameters")
    
    # dataset = load_dataset(args.dataset_name, split="train[:1000]")
    # val_dataset = load_dataset(args.dataset_name, split="train[1000:1500]")

    full_dataset = load_dataset(args.dataset_name)
    train_dataset, val_dataset, test_dataset = full_dataset["train_dataset"], full_dataset["valid_dataset"], full_dataset["test_dataset"]
    train_dataset_copy, val_dataset_copy, test_dataset_copy = deepcopy(train_dataset), deepcopy(val_dataset), deepcopy(test_dataset)
    tokenizer = get_chat_template(
        tokenizer,
        chat_template = "llama-3.1",
        )
    # print("Before SIDE", tokenizer.padding_side)
    ##
    # Add any pre-processing on dataset (templates, tokenization, etc.)
    # print("Tokenizer ---> ", tokenizer.pad_token_id, " EoS --->", tokenizer.eos_token_id)
    train_dataset = map_dataset_to_template(dataset = train_dataset, tokenizer = tokenizer)
    val_dataset = map_dataset_to_template(dataset = val_dataset , tokenizer = tokenizer, dataset_type = "validation")
    test_dataset = map_dataset_to_template(dataset = test_dataset, tokenizer = tokenizer, dataset_type = "definitely not train LoL")
    print(f"Train Size: {len(train_dataset)}; Valid Size: {len(val_dataset)}; Test Size: {len(test_dataset)}")
    # print(">>>", train_dataset[5], "<<<")
    # print(">>>", val_dataset[5], "<<<")
    # print("EOS", tokenizer.eos_token_id)
    # print("PAD", tokenizer.pad_token_id)
    # # tokenizer.padding_side = "left"
    # print("After SIDE", tokenizer.padding_side)

    trainer = LLaMATrainer(
        model=model,
        tokenizer=tokenizer,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
        dataset_text_field="text",
        max_seq_length=args.max_seq_length,
        data_collator=DataCollatorForSeq2Seq(tokenizer=tokenizer),
        dataset_num_proc=1,
        packing=False,
        args=TrainingArguments(
            run_name=f"s_{args.dataset_name}_{model_name_or_path}",
            fp16_full_eval=True,
            eval_accumulation_steps=4,
            per_device_train_batch_size=args.per_device_train_batch_size,
            per_device_eval_batch_size=args.per_device_eval_batch_size,
            learning_rate=args.learning_rate,
            lr_scheduler_type=args.lr_scheduler_type,
            num_train_epochs=10,
            evaluation_strategy="epoch",
            save_strategy="epoch",
            eval_steps=1,
            save_steps=1,
            fp16=not is_bfloat16_supported(),
            bf16=is_bfloat16_supported(),
            output_dir=f"checkpoints/",
            logging_steps=4,
            optim="adamw_8bit",
            report_to=["wandb"],
            logging_dir="logs",
            weight_decay=0.01,
            warmup_steps=350,
            seed=1337,
            load_best_model_at_end=True,
            save_total_limit=10,
            include_inputs_for_metrics=True,
            metric_for_best_model="eval_arg_cls_f1",
        ),
        compute_metrics=load_dataset_metrics(args.dataset_name),
        callbacks=[
            EarlyStoppingCallback(early_stopping_patience=args.patience),
        ]
    )
    # ToDo--> hacky solution: please find a better way
    trainer.max_seq_length=args.max_seq_length
    trainer.gt_val_data = val_dataset
    trainer.gt_test_data = test_dataset
    trainer.gt_orig_val_data = val_dataset_copy
    trainer.gt_orig_test_data = test_dataset_copy
    trainer.dataset_name = args.dataset_name
    # dataset_to_pick = 
    trainer = train_on_responses_only(trainer, 
        instruction_part = instruction_response_mapper["LLaMA3_1"]["instruction_part"],
        response_part = instruction_response_mapper["LLaMA3_1"]["response_part"]
        )
    
    # For debugging purposes
    print(">>>>> Input: ", tokenizer.decode(trainer.train_dataset[3]["input_ids"]), "<<<<<")
    space = tokenizer(" ", add_special_tokens = False).input_ids[0]
    print(">>>>> Output: ", tokenizer.decode([space if x == -100 else x for x in trainer.train_dataset[3]["labels"]]), "<<<<<")
    all_lengths = [len(x["input_ids"]) for x in trainer.train_dataset]
    print("max length should be: ", max(all_lengths))
    # xxx
    # print(val_dataset_copy[0])
    # xzzxxzxzxzxzxzxzx
    # Start Training

    torch.cuda.empty_cache()
    gc.collect()  # <----- Clear Python garbage

    # Track GPU memory usage
    print(torch.cuda.memory_summary(device=device, abbreviated=True))  # <----- Log memory usage

    if args.do_resume_train:
        if args.experiment_path:
            experiment_path = args.experiment_path
            if os.path.exists(experiment_path):
                checkpoints = [ckpt for ckpt in os.listdir(experiment_path) if os.path.isdir(os.path.join(experiment_path, ckpt)) and ckpt.startswith("checkpoint-")]
                if checkpoints:
                    checkpoints.sort(key=lambda x: int(x.split("-")[1]))
                    selected_checkpoint = os.path.join(experiment_path, checkpoints[-1])
                    print(f"Resuming training from checkpoint: {selected_checkpoint}")
                    trainer.args.output_dir = experiment_path
                    trainer.train(resume_from_checkpoint=selected_checkpoint)
                else:
                    print(f"No checkpoints found for experiment at {experiment_path}. Starting training from scratch.")
            else:
                print("Experiment path does not exist. Starting training from scratch.")
        else:
            print("No experiment path provided. Starting training from scratch.")

    if(args.do_eval):
        trainer.evaluate()
    # if trainer.eval_process:
    #     trainer.eval_process.join()

    # Save Model
    model.save_pretrained(f"models/inst_{args.dataset_name}")
    logger.info("Model saved to saved_model")

    # Evaluate Model
    logger.info("Starting model evaluation on test set...")
    trainer.evaluate(test_dataset, metric_key_prefix = "test")

if __name__ == '__main__':
    # mp.set_start_method('spawn', force=True) 28462MiB # 3C    P0             378W / 500W |  28696MiB / 8
    args = parse_args()
    main(args)





# import os
# import gc
# import re
# import sys
# import json
# import wandb
# # os.environ["WANDB_DISABLED"] = "true"
# import torch
# import logging
# import argparse
# import numpy as np
# import transformers
# import pandas as pd
# from transformers import (
#     AutoModelForCausalLM,
#     AutoTokenizer,
#     TrainingArguments,
#     Seq2SeqTrainingArguments,
#     EarlyStoppingCallback,
# )
# from tqdm import tqdm
# from functools import partial
# from trl import SFTTrainer
# from transformers import BitsAndBytesConfig
# # from datasets import load_dataset
# from accelerate import Accelerator
# from torch.utils.data import DataLoader
# from transformers.trainer_utils import get_last_checkpoint, set_seed
# from transformers.integrations import WandbCallback
# from unsloth import FastLanguageModel, is_bfloat16_supported
# from unsloth.chat_templates import get_chat_template
# from transformers import TextStreamer
# from load_dataset import load_dataset
# from load_eval_metrics import load_dataset_metrics
# # from peft import LoraConfig, get_peft_model
# from LLaMATrainer import LLaMATrainer
# from transformers import TrainingArguments, DataCollatorForSeq2Seq
# # Setup logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)


# def parse_args():
#     parser = argparse.ArgumentParser(description="Train LLaMA with customizable settings.")
    
#     # Add argument to specify config file
#     parser.add_argument("--config_file", type=str, help="Path to config file (JSON format)")
    
#     # Basic Parameters
#     parser.add_argument("-v", "--llama_version", choices=["LLaMA 2", "LLaMA 3"], default="LLaMA 2", help="Specify LLaMA version.")
#     parser.add_argument("-p", "--model_parameters", default="7B", help="Model size parameters like 7B, 13B.")
    
#     # Optimization
#     parser.add_argument("-o", "--optimization", choices=["LoRA", "QLoRA"], default="LoRA", help="PEFT Optimization technique.")
#     parser.add_argument("-m", "--max_seq_length", type=int, default=3000, help="Maximum sequence length for inputs.")
#     parser.add_argument("-b", "--load_in_4bit", type=bool, default=True, help="Load model in 4-bit precision.")
    
#     # LoRA Parameters
#     parser.add_argument("-a", "--lora_alpha", type=int, default=64, help="Scaling factor for LoRA updates.")
#     parser.add_argument("-r", "--lora_rank", type=int, default=128, help="Rank size for LoRA matrix.")
#     parser.add_argument("-d", "--lora_dropout", type=float, default=0, help="Dropout for LoRA layers.")
#     parser.add_argument("-t", "--target_modules", nargs='+', default=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"], help="Target modules for LoRA.")
#     parser.add_argument("-l", "--use_rslora", type=bool, default=True, help="Use Rank-Stabilized LoRA.")
    
#     # Advanced Features
#     parser.add_argument("-c", "--use_gradient_checkpointing", type=bool, default=True, help="Use gradient checkpointing.")
#     parser.add_argument("--early_stopping", type=bool, default=True, help="Enable early stopping based on evaluation metrics.")
#     parser.add_argument("--quantization", choices=["8bit", "4bit"], help="Choose quantization type.")
    
#     # Dataset and Evaluation
#     parser.add_argument("--dataset_name", type=str, default="degree_ACE", help="Dataset name for training.")
#     parser.add_argument("--eval_metrics", nargs='+', default=["accuracy", "f1"], help="Custom evaluation metrics.")
    
#     # Advanced training arguments for flexibility
#     parser.add_argument("--fp16", type=bool, default=False, help="Enable mixed precision training with float16.")
#     parser.add_argument("--learning_rate", type=float, default=1e-5, help="Learning rate.")
#     parser.add_argument("--lr_scheduler_type", choices=["linear", "cosine", "polynomial"], default="cosine", help="Type of learning rate scheduler.")
#     parser.add_argument("--warmup_steps", type=int, default=0, help="Number of steps for warmup.")
#     parser.add_argument("--save_steps", type=int, default=1000, help="Save checkpoint every X steps.")
#     parser.add_argument("--eval_steps", type=int, default=500, help="Evaluate every X steps.")
#     parser.add_argument("--patience", type=int, default=3, help="Number of eval steps for early stopping patience.")
#     parser.add_argument("--per_device_train_batch_size", type=int, default=32, help="Training batch size.")
#     parser.add_argument("--per_device_eval_batch_size", type=int, default=50, help="Eval batch size.")

#     # Arguments for train/valid
#     parser.add_argument("--do_resume_train", type=bool, default=True, help="Should we train?")
#     parser.add_argument("--do_eval", type=bool, default=True, help="Should we eval?")
#     args = parser.parse_args()
    
#     # Load args from config file if provided
#     if args.config_file:
#         logger.info(f"Loading config file: {args.config_file}")
#         with open(args.config_file, 'r') as f:
#             config_args = json.load(f)
        
#         # Update the argparse args with the values from config file
#         for key, value in config_args.items():
#             if not hasattr(args, key):  # Skip invalid keys
#                 logger.warning(f"Invalid config key: {key}. Ignoring.")
#             else:
#                 setattr(args, key, value)
    
#     return args


# def parse_model_info(args):
#     """Return model path based on version and size."""
#     model_map = {
#         "LLaMA 2": f"meta-llama/Meta-Llama-2-{args.model_parameters}",
#         "LLaMA 3": f"meta-llama/Meta-Llama-3-{args.model_parameters}",
#     }
#     model_path = model_map.get(args.llama_version)
#     if not model_path:
#         raise ValueError(f"Invalid LLaMA version: {args.llama_version}")
#     return model_path




# def map_dataset_to_template(dataset, tokenizer, key = "conversations", dataset_type = "train"):
#     # print(f"Doing padding to the {tokenizer.padding_side} for {dataset_type}")
#     def apply_template(examples, tokenizer, key):
#         messages = examples[key]
#         #if dataset_type == "train" else text.replace(tokenizer.eos_token)
#         texts = [tokenizer.apply_chat_template(message, tokenize = False, add_generation_prompt = False) for message in messages]
#         # print(text)
#         # xx
#         return { "text" : texts, }#{"text":[t if dataset_type == "train" else (''.join(t.rsplit(tokenizer.eos_token, 1))).strip() + "\n" for t in text]}
#     # Log the number of examples processed
#     # logger.info(f"Original dataset size: {len(dataset)}")
#     processed_dataset = dataset.map(partial(apply_template, tokenizer=tokenizer, key=key), batched=True)
#     # logger.info(f"Processed dataset size: {len(processed_dataset)}")
#     # Ensure tokenizer is set to left-padding for non-train tasks when required (especially for generation)
#     return processed_dataset#dataset.map(partial(apply_template, tokenizer=tokenizer, key=key), batched=True)

# def map_dataset_to_template_adv(dataset, tokenizer, key="conversations", dataset_type="train"):
#     def apply_template(examples, tokenizer, key):
#         messages = examples[key]
#         # Process input text (e.g., user input)
#         text = [tokenizer.apply_chat_template(message, tokenize=False, add_generation_prompt=False) for message in messages]
#         text = [t if dataset_type == "train" else (''.join(t.rsplit(tokenizer.eos_token, 1))).strip() + "\n" for t in text]
#         # Process label text (assuming the second item in messages is the expected response)
#         labels = [message[1]["value"] for message in messages]  # Modify based on your actual data structure
#         # Tokenize input and labels
#         input_ids = [tokenizer.encode(t, add_special_tokens=True) for t in text]
#         label_ids = [tokenizer.encode(l, add_special_tokens=True) for l in labels] if dataset_type != "train" else None
#         # Return input_ids and label_ids (optional for training dataset)
#         result = {"input_ids": input_ids}
#         if label_ids is not None:
#             result["label_ids"] = label_ids
#         result["original_input"] = text
#         return result
#     # logger.info(f"Original dataset size: {len(dataset)}")
#     # Apply the template to the dataset
#     processed_dataset = dataset.map(partial(apply_template, tokenizer=tokenizer, key=key), batched=True)
#     # logger.info(f"Processed dataset size: {len(processed_dataset)}")
#     return processed_dataset

# from unsloth.chat_templates import train_on_responses_only
# instruction_response_mapper = {
#     "LLaMA3_1":{
#     "instruction_part": "<|start_header_id|>user<|end_header_id|>\n\n",
#     "response_part": "<|start_header_id|>assistant<|end_header_id|>\n\n"
#     }

# }

# def prepare_lora_model(args, model):
#     """Prepare model with LoRA or QLoRA configuration."""
#     model = FastLanguageModel.get_peft_model(
#     model,
#     r = args.lora_rank,
#     lora_alpha = args.lora_alpha,
#     lora_dropout = args.lora_dropout,
#     target_modules = args.target_modules, 
#     use_rslora = args.use_rslora,
#     use_gradient_checkpointing = "unsloth" if args.use_gradient_checkpointing else False 
#     )
#     config = ""
#     config += f"LoRA Rank -> {args.lora_rank}\n"
#     config += f"LoRA ⍺ -> {args.lora_alpha}\n"
#     config += f"LoRA dropout -> {args.lora_dropout}\n"
#     config += f"Target Modules -> {args.target_modules}\n"
#     config += f"Use RSLoRA -> {args.use_rslora}\n"
#     config += f"Use Gradient Checkpointing -> {args.use_gradient_checkpointing}\n"
#     logger.info(f"LoRA/QLoRA optimization applied with config\n{'-*'*75}\n{config}{'-*'*75}")
#     return model

# from unsloth.chat_templates import standardize_sharegpt
# from copy import deepcopy

