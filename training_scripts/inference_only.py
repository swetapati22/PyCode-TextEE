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


def parse_args():
    parser = argparse.ArgumentParser(description="Train LLaMA with customizable settings.")
    
    # Add argument to specify config file
    parser.add_argument("--config_file", type=str, help="Path to config file (JSON format)")
    
    # Basic Parameters
    parser.add_argument("-v", "--llama_version", choices=["LLaMA 2", "LLaMA 3"], default="LLaMA 2", help="Specify LLaMA version.")
    parser.add_argument("-p", "--model_parameters", default="7B", help="Model size parameters like 7B, 13B.")
    
    # Optimization
    parser.add_argument("-o", "--optimization", choices=["LoRA", "QLoRA"], default="LoRA", help="PEFT Optimization technique.")
    #change in future: was 1024, changed to 3000
    parser.add_argument("-m", "--max_seq_length", type=int, default=3000, help="Maximum sequence length for inputs.")
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
    
    #changed this:
    # Dataset and Evaluation
    parser.add_argument("--dataset_name", type=str, default="richere_test_without_guideline_wo_NS", help="Dataset name for training.")
    parser.add_argument("--eval_metrics", nargs='+', default=["accuracy", "f1"], help="Custom evaluation metrics.")
    
    # Advanced training arguments for flexibility
    parser.add_argument("--fp16", type=bool, default=False, help="Enable mixed precision training with float16.")
    parser.add_argument("--learning_rate", type=float, default=1e-5, help="Learning rate.")
    parser.add_argument("--lr_scheduler_type", choices=["linear", "cosine", "polynomial"], default="cosine", help="Type of learning rate scheduler.")
    parser.add_argument("--warmup_steps", type=int, default=0, help="Number of steps for warmup.")
    parser.add_argument("--save_steps", type=int, default=1000, help="Save checkpoint every X steps.")
    parser.add_argument("--eval_steps", type=int, default=500, help="Evaluate every X steps.")
    parser.add_argument("--patience", type=int, default=3, help="Number of eval steps for early stopping patience.")
    parser.add_argument("--per_device_train_batch_size", type=int, default=64, help="Training batch size.")
    #change in future: currently 128 changed to 64
    parser.add_argument("--per_device_eval_batch_size", type=int, default=64, help="Eval batch size.")

    # Arguments for train/valid
    parser.add_argument("--do_train", type=bool, default=True, help="Should we train?")
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
        messages = examples[key]
        #if dataset_type == "train" else text.replace(tokenizer.eos_token)
        texts = [tokenizer.apply_chat_template(message, tokenize = False, add_generation_prompt = False) for message in messages]
        # print(text)
        # xx
        return { "text" : texts, }#{"text":[t if dataset_type == "train" else (''.join(t.rsplit(tokenizer.eos_token, 1))).strip() + "\n" for t in text]}
    # Log the number of examples processed
    # logger.info(f"Original dataset size: {len(dataset)}")
    processed_dataset = dataset.map(partial(apply_template, tokenizer=tokenizer, key=key), batched=True)
    # logger.info(f"Processed dataset size: {len(processed_dataset)}")
    # Ensure tokenizer is set to left-padding for non-train tasks when required (especially for generation)
    return processed_dataset#dataset.map(partial(apply_template, tokenizer=tokenizer, key=key), batched=True)

def map_dataset_to_template_adv(dataset, tokenizer, key="conversations", dataset_type="train"):
    def apply_template(examples, tokenizer, key):
        messages = examples[key]
        # Process input text (e.g., user input)
        text = [tokenizer.apply_chat_template(message, tokenize=False, add_generation_prompt=False) for message in messages]
        text = [t if dataset_type == "train" else (''.join(t.rsplit(tokenizer.eos_token, 1))).strip() + "\n" for t in text]
        # Process label text (assuming the second item in messages is the expected response)
        labels = [message[1]["value"] for message in messages]  # Modify based on your actual data structure
        # Tokenize input and labels
        input_ids = [tokenizer.encode(t, add_special_tokens=True) for t in text]
        label_ids = [tokenizer.encode(l, add_special_tokens=True) for l in labels] if dataset_type != "train" else None
        # Return input_ids and label_ids (optional for training dataset)
        result = {"input_ids": input_ids}
        if label_ids is not None:
            result["label_ids"] = label_ids
        result["original_input"] = text
        return result
    # logger.info(f"Original dataset size: {len(dataset)}")
    # Apply the template to the dataset
    processed_dataset = dataset.map(partial(apply_template, tokenizer=tokenizer, key=key), batched=True)
    # logger.info(f"Processed dataset size: {len(processed_dataset)}")
    return processed_dataset

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

from unsloth.chat_templates import standardize_sharegpt
from copy import deepcopy
def main(args):
    #changed this:
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/rq3/checkpoint-5364/"
    #Used this for inference the below one from RQ3:
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/rq3_X_Y_split/checkpoint-16092/"
    # #Sweta's Checkpoint baseline:
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_load_multi_baseline_rank_128_alpha_64_lr_1e-05/checkpoint-26820/"
    #Saurabh's Checkpoint:
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/baseline_saurabh_run/checkpoint-26820/"
    # #ACE_only Checkpoint baseline:
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_baseline_ace_rank_128_alpha_64_lr_1e-05/checkpoint-2152/"
    # #Maven_only Checkpoint baseline:
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_baseline_maven_rank_128_alpha_64_lr_1e-05/checkpoint-8252/"
    # # Saurabh's RQ3_100_Checkpoint:
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/rq3/checkpoint-5364/"
    # # Saurabh's RQ3_X_Y_Checkpoint:
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/rq3_X_Y_split/checkpoint-16092/"
    # #Wikievents_only Checkpoint baseline:
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_baseline_wikievents_rank_128_alpha_64_lr_1e-05/checkpoint-820/"
    # # Baseline_wo_guidelines_ACE: /scratch/spati/tmp/LLaMA/checkpoints/inst_baseline_wo_guidelines_ace_rank_128_alpha_64_lr_1e-05/checkpoint-4842
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_baseline_wo_guidelines_ace_rank_128_alpha_64_lr_1e-05/checkpoint-4842/"
    # # Baseline_wo_guidelines_maven
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_baseline_wo_guidelines_maven_rank_128_alpha_64_lr_1e-05/checkpoint-16504/"
    # # Baseline_wo_guidelines_wikievents:
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_baseline_wo_guidelines_wikievents_rank_128_alpha_64_lr_1e-05/checkpoint-738/"
    # # Baseline_wo_guidelines_entire_dataset:
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_load_multi_baseline_wo_guidelines_new_rank_128_alpha_64_lr_1e-05/checkpoint-26820/"
    
    #inference on ACE dataset - dev with 1 event till we cover all using checkpoint from ACE_Baseline trained w/o guideline w neg samples dataset:
    # #inference_ace_dev1_ace_only_wo_guidelines_w_neg_samp
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_load_ACE_Only_wo_guid_w_negativesample_rank_128_alpha_64_lr_1e-05/checkpoint-41435/"
    #inference on ACE dataset - dev with 1 event till we cover all using checkpoint from ACE_Baseline trained w guideline w neg samples dataset:
    # #inference_ace_dev1_ace_only_w_guidelines_w_neg_samp
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_load_ACE_Only_w_guid_w_negativesample_rank_128_alpha_64_lr_1e-05/checkpoint-58009/"


    # #inference_ACE_Only_wo_guid_w_negativesample_new
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_load_ACE_Only_wo_guid_w_negativesample_new_rank_128_alpha_64_lr_1e-05/checkpoint-66296/"
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_load_ACE_Only_wo_guid_w_negativesample_new_rank_128_alpha_64_lr_1e-05/checkpoint-74583/"


    ############### Inference of richere 100 test sample from guideline experiments  ###############
    # #guideline_P_w_NS: (till 5th epoch)
    # model_name_or_path = '/scratch/spati/tmp/LLaMA/checkpoints/inst_guideline_P_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-41435'
    # #guideline_P_wo_NS (till 10th epoch)
    # model_name_or_path = '/scratch/spati/tmp/LLaMA/checkpoints/inst_guideline_P_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-538/'
    # #guideline_PN_w_NS: (till 5th epoch)
    # model_name_or_path = '/scratch/spati/tmp/LLaMA/checkpoints/inst_guideline_PN_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-33148/'
    # #guideline_PN_wo_NS: (till 10th epoch)
    # model_name_or_path = '/scratch/spati/tmp/LLaMA/checkpoints/inst_guideline_PN_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-538/'
    # #guideline_PS_w_NS: (till 7th epoch)
    # model_name_or_path = '/scratch/spati/tmp/LLaMA/checkpoints/inst_guideline_PS_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-24861/'
    # #guideline_PS_wo_NS: (till 10th epoch)
    # model_name_or_path = '/scratch/spati/tmp/LLaMA/checkpoints/inst_guideline_PS_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-1076/'
    # #guideline_PN_adv_wo_NS: (till 5th epoch)
    # model_name_or_path = '/scratch/spati/tmp/LLaMA/checkpoints/inst_guideline_PN_Adv_rank_128_alpha_64_lr_1e-05_resumed_to_10/checkpoint-1076/'



    ############### Inference of 100 best dev set checkpoint on prior dev set ###############
    ############INFERENCE_MINI_GUIDELINE EXPERIMENTS############
    # #Train100_no_guidelines:
    # # "inference_our_dev_miniguideline_train100_wo_guidelines_w_NS":
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_miniguideline_train100_wo_guidelines_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-490/"
    # #Train100_human_guidelines:
    # # "inference_our_dev_miniguideline_train100_Human_w_NS": 
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_miniguideline_train100_Human_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-392/"
    # # "inference_our_dev_miniguideline_train100_Human_wo_NS": 
    # #Train100_Generated guidelines with only Positive examples:
    # # #"inference_our_dev_miniguideline_train100_P_w_NS": 
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_miniguideline_train100_P_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-294"
    # #"inference_our_dev_miniguideline_train100_P_wo_NS": 
    # #Train100_Generated guidelines with both Positive and 15 Negative examples:
    # # "inference_our_dev_miniguideline_train100_PN_w_NS": 
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_miniguideline_train100_PN_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-490/"
    # #"inference_our_dev_miniguideline_train100_PN_wo_NS": 
    # #Train100_Generated guidelines with both Positive and 15 Sibling examples:
    # #"inference_our_dev_miniguideline_train100_PS_w_NS": 
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_miniguideline_train100_PS_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-245/"
    # "inference_our_dev_miniguideline_train100_PS_wo_NS": 


    # #ACE_wo_guideline_wo_neg_example: Baseline_wo_guidelines_ACE: /scratch/spati/tmp/LLaMA/checkpoints/inst_baseline_wo_guidelines_ace_rank_128_alpha_64_lr_1e-05/checkpoint-4842
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_baseline_wo_guidelines_ace_rank_128_alpha_64_lr_1e-05/checkpoint-4842/"


#Havn't run on these
    # #Human_wo_NS_MiniTrain
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_miniguideline_train100_Human_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-28/"
    # #P_wo_NS_MiniTrain
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_miniguideline_train100_P_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-36/"
    # #PS_wo_NS_MiniTrain
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_miniguideline_train100_PS_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-28/"
    # #PN_wo_NS_MiniTrain
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_miniguideline_train100_PN_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-28/"


    ############Inference the full GUIDELINE EXPERIMENTS on new_full_coverage_dev_set (PA_dev_100)############
    #no_guidelines:
    #"infer_wo_guidelines_wo_NS":
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_baseline_wo_guidelines_ace_rank_128_alpha_64_lr_1e-05/checkpoint-4842/"         
    #"infer_wo_guidelines_w_NS": 
    #OLD model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_load_ACE_Only_wo_guid_w_negativesample_new_rank_128_alpha_64_lr_1e-05/checkpoint-66296/"
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_load_ACE_Only_wo_guid_w_negativesample_new_rank_128_alpha_64_lr_1e-05/checkpoint-74583/" 
         
    #human_guidelines:
    #"infer_Human_w_NS":  
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_load_ACE_Only_w_guid_w_negativesample_rank_128_alpha_64_lr_1e-05/checkpoint-58009/"
         
    #"infer_Human_wo_NS": 
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_baseline_ace_rank_128_alpha_64_lr_1e-05/checkpoint-2152/" 
         
    #Generated guidelines with only Positive examples:
    #"infer_guideline_P_w_NS": (Completlt Ran)
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_guideline_P_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-41435/"
         
    #"infer_guideline_P_wo_NS":
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_guideline_P_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-538/"  
         
    #Generated guidelines with both Positive and 15 Negative examples:
    #*********************** RUN LATER **************************** 
    #(TO DO) "infer_guideline_PN_w_NS": (Ran till 4th - HAVE RESUMED NOW) 
    #OLD BEST MODEL: model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_guideline_PN_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-33148/"  
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_guideline_PN_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-41435/"
         
    #"infer_guideline_PN_wo_NS":
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_guideline_PN_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-538/"  

    #*********************** RUN to complete experiment and then run this LATER ****************************
    #Generated guidelines with both Positive and 15 Sibling examples:
    #(TO DO) "infer_guideline_PS_w_NS": (Ran till 6th - HAVE TO RESUME)
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_guideline_PS_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-24861/" 
         
    #"infer_guideline_PS_wo_NS":
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_guideline_PS_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-1076/"  
         
    #Generated guidelines consolidated:
    #"infer_guideline_PN_Adv_wo_NS":
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_guideline_PN_Adv_rank_128_alpha_64_lr_1e-05/checkpoint-1076/"  
         
    #from here below were trained on total train - checkpointed on full coverage dev set hence, infered on old dev set without full coverage.
    #*********************** get the checkpoint on completion of experiment and then run this LATER ****************************     
    #"infer_guideline_PN_Adv_w_NS" :
    #Ran on the below - since this was the best checkpoint of trainer state - but the actual best one is in the second path
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_guideline_PN_Adv_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-82870/"
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_guideline_PN_Adv_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-58009/" 
         
    #"infer_guideline_PS_Adv_wo_NS":
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_guideline_PS_Adv_rank_128_alpha_64_lr_1e-05/checkpoint-3228/"  
         
    #*********************** get the checkpoint on completion of experiment and then run this LATER ****************************     
   #"infer_guideline_PS_Adv_w_NS" :
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_guideline_PS_Adv_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-33148/" 

    ############Inference from Train 2000 on full test############
    #no_guidelines:
    #"test2000_wo_guidelines_wo_NS":
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_train2000_wo_guidelines_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-63/"         
    #"test2000_wo_guidelines_w_NS": 
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_train2000_wo_guidelines_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-9690/" 
         
    #human_guidelines:
    #"test2000_Human_w_NS":  
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_train2000_Human_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-6783/"
    #"test2000_Human_wo_NS": 
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_train2000_Human_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-315/" 
         
    #Generated guidelines with only Positive examples:
    #"test2000_P_w_NS": (Completlt Ran)
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_train2000_P_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-6783/"
    #"test2000_P_wo_NS":
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_train2000_P_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-378/"  
         
    #Generated guidelines with both Positive and 15 Negative examples:
    #"test2000_PN_w_NS":
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_train2000_PN_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-2907/"
    #"test2000_PN_wo_NS":
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_train2000_PN_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-504/"  

    #Generated guidelines with both Positive and 15 Sibling examples:
    #"test2000_PS_w_NS":
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_train2000_PS_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-9690/"  
    #"test2000_PS_wo_NS":
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_train2000_PS_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-315/"  
         
    #Generated guidelines consolidated:
    #"test2000_PN_Adv_wo_NS":
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_train2000_PN_Adv_wo_NExample_rank_128_alpha_64_lr_1e-05/checkpoint-378/"  
    #"test2000_PN_Adv_w_NS" :
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_train2000_PN_Adv_w_NExample_rank_128_alpha_64_lr_1e-05/checkpoint-5814/" 
         
    #"test2000_PS_Adv_wo_NS":
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_train2000_PS_Adv_wo_NExample_rank_128_alpha_64_lr_1e-05/checkpoint-378/"   
   #"test2000_PS_Adv_w_NS" :
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_train2000_PS_Adv_w_NExample_rank_128_alpha_64_lr_1e-05/checkpoint-9690/" 

    # ############ACE: Inference from Train 100 on full test############
    # #ITER0
    # #Metrics/Data	Checkpoint Path
    # #ACE_train100_iter0_NoGuideline_w_NS - test100_wo_guidelines_w_NS	
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_miniguideline_train100_wo_guidelines_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-490/"
    # #ACE_train100_iter0_Guideline-H_w_NS - test100_Human_w_NS	
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_miniguideline_train100_Human_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-392/"
    # #ACE_train100_iter0_Guideline-P_w_NS - test100_P_w_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_miniguideline_train100_P_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-294/"
    # #ACE_train100_iter0_Guideline-PN_w_NS	- test100_PN_w_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_miniguideline_train100_PN_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-490/"
    # #ACE_train100_iter0_Guideline-PS_w_NS	- test100_PS_w_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_miniguideline_train100_PS_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-245/"
    # #ACE_train100_iter0_Guideline-PN-Adv_w_NS	- test100_PN_Adv_w_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_miniguideline_train100_PN_Adv_w_NExample_rank_128_alpha_64_lr_1e-05/checkpoint-392/"
    # #ACE_train100_iter0_Guideline-PS-Adv_w_NS	- test100_PS_Adv_w_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_miniguideline_train100_PS_Adv_w_NExample_rank_128_alpha_64_lr_1e-05/checkpoint-245/"

    # #ITER1	
    # #Metrics/Data	Checkpoint Path
    # #ACE_train100_iter1_NoGuideline_w_NS	- test100_wo_guidelines_w_NS_iter1
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_miniguideline_train100_wo_guidelines_w_NS_iter1_rank_128_alpha_64_lr_1e-05/checkpoint-441/"
    # #ACE_train100_iter1_Guideline-H_w_NS	- test100_Human_w_NS_iter1
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_miniguideline_train100_Human_w_NS_iter1_rank_128_alpha_64_lr_1e-05/checkpoint-441/"
    # #ACE_train100_iter1_Guideline-P_w_NS	- test100_P_w_NS_iter1
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_miniguideline_train100_P_w_NS_iter1_rank_128_alpha_64_lr_1e-05/checkpoint-441/"
    # #ACE_train100_iter1_Guideline-PN_w_NS	- test100_PN_w_NS_iter1
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_miniguideline_train100_PN_w_NS_iter1_rank_128_alpha_64_lr_1e-05/checkpoint-441/"
    # #ACE_train100_iter1_Guideline-PS_w_NS	- test100_PS_w_NS_iter1
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_miniguideline_train100_PS_w_NS_iter1_rank_128_alpha_64_lr_1e-05/checkpoint-490/"
    # #ACE_train100_iter1_Guideline-PN-Adv_w_NS - test100_PN_Adv_w_NS_iter1	
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_miniguideline_train100_PN_Adv_w_NExample_iter1_rank_128_alpha_64_lr_1e-05/checkpoint-441/"
    # #ACE_train100_iter1_Guideline-PS-Adv_w_NS	- test100_PS_Adv_w_NS_iter1
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_miniguideline_train100_PS_Adv_w_NExample_iter1_rank_128_alpha_64_lr_1e-05/checkpoint-490/"

    # #ITER2
    # #Metrics/Data	Checkpoint Path
    # #ACE_train100_iter2_NoGuideline_w_NS - test100_wo_guidelines_w_NS_iter2
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_miniguideline_train100_wo_guidelines_w_NS_iter2_rank_128_alpha_64_lr_1e-05/checkpoint-450/"
    # #ACE_train100_iter2_Guideline-H_w_NS	- test100_Human_w_NS_iter2
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_miniguideline_train100_Human_w_NS_iter2_rank_128_alpha_64_lr_1e-05/checkpoint-500/"
    # #ACE_train100_iter2_Guideline-P_w_NS	- test100_P_w_NS_iter2
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/"
    # #ACE_train100_iter2_Guideline-PN_w_NS	- test100_PN_w_NS_iter2
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/"
    # #ACE_train100_iter2_Guideline-PS_w_NS	- test100_PS_w_NS_iter2
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/"
    # #ACE_train100_iter2_Guideline-PN-Adv_w_NS	- test100_PN_Adv_w_NS_iter2
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_miniguideline_train100_PN_Adv_w_NExample_iter2_rank_128_alpha_64_lr_1e-05/checkpoint-100/"
    # #ACE_train100_iter2_Guideline-PS-Adv_w_NS	- test100_PS_Adv_w_NS_iter2
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_miniguideline_train100_PS_Adv_w_NExample_iter2_rank_128_alpha_64_lr_1e-05/checkpoint-100/"


    # ############RICHERE: Inference from Train 100 on full test############
    # #Metrics/Data	Checkpoint Path
    # #RichERE_Train_100_NoGuideline_wo_NS - richere_test100_without_guideline_wo_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train100_without_guideline_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-4/"
    # #RichERE_Train_100_Guideline-P_wo_NS - richere_test100_guidelineP_wo_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train100_guidelineP_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-32/"
    # #RichERE_Train_100_Guideline-PN_wo_NS	- richere_test100_guidelinePN_wo_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train100_guidelinePN_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-28/"
    # #RichERE_Train_100_Guideline-PS_wo_NS	- richere_test100_guidelinePS_wo_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train100_guidelinePS_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-4/"
    # #RichERE_Train_100_Guideline-PN-Adv_wo_NS	- richere_test100_guidelinePN_Adv_wo_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train100_guidelinePN_Adv_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-28/"
    # #RichERE_Train_100_Guideline-PS-Adv_wo_NS	- richere_test100_guidelinePS_Adv_wo_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train100_guidelinePS_Adv_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-36/"


    # #RichERE_Train_100_NoGuideline_w_NS - richere_test100_without_guideline_w_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train100_without_guideline_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-441/"
    # #RichERE_Train_100_Guideline-P_w_NS - richere_test100_guidelineP_w_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train100_guidelineP_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-147/"
    # #RichERE_Train_100_Guideline-PN_w_NS	- richere_test100_guidelinePN_w_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train100_guidelinePN_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-441/"
    # #RichERE_Train_100_Guideline-PS_w_NS - richere_test100_guidelinePS_w_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train100_guidelinePS_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-441/"
    # #RichERE_Train_100_Guideline-PN-Adv_w_NS	- richere_test100_guidelinePN_Adv_w_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train100_guidelinePN_Adv_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-343/"
    # #RichERE_Train_100_Guideline-PS-Adv_w_NS - richere_test100_guidelinePS_Adv_w_NS	
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train100_guidelinePS_Adv_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-490/"
	
    # ############RICHERE: Inference from Train 2000 on full test############
    # #Metrics/Data	Checkpoint Path
    # #RichERE_Train_2000_NoGuideline_wo_NS	- richere_test2000_without_guideline_wo_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train2000_without_guideline_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-567/"
    # #RichERE_Train_2000_Guideline-P_wo_NS - richere_test2000_guidelineP_wo_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train2000_guidelineP_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-252/"
    # #RichERE_Train_2000_Guideline-PN_wo_NS - richere_test2000_guidelinePN_wo_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/
    # #RichERE_Train_2000_Guideline-PS_wo_NS - richere_test2000_guidelinePS_wo_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train2000_guidelinePS_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-315/"
    # #RichERE_Train_2000_Guideline-PN-Adv_wo_NS - richere_test2000_guidelinePN_Adv_wo_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train2000_guidelinePN_Adv_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-567/"
    # #RichERE_Train_2000_Guideline-PS-Adv_wo_NS - richere_test2000_guidelinePS_Adv_wo_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train2000_guidelinePS_Adv_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-630/"

    # #RichERE_Train_2000_NoGuideline_w_NS	- richere_test2000_without_guideline_w_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train2000_without_guideline_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-5664/"
    # #RichERE_Train_2000_Guideline-P_w_NS - richere_test2000_guidelineP_w_NS	
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train2000_guidelineP_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-5664/"
    # #RichERE_Train_2000_Guideline-PN_w_NS	- richere_test2000_guidelinePN_w_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train2000_guidelinePN_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-8496/"
    # #RichERE_Train_2000_Guideline-PS_w_NS	- richere_test2000_guidelinePS_w_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train2000_guidelinePS_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-8496/"
    # #RichERE_Train_2000_Guideline-PN-Adv_w_NS - richere_test2000_guidelinePN_Adv_w_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train2000_guidelinePN_Adv_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-8496/"
    # #RichERE_Train_2000_Guideline-PS-Adv_w_NS	- richere_test2000_guidelinePS_Adv_w_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train2000_guidelinePS_Adv_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-6608/"
	
    # ############RICHERE: Inference from FULL Train on full test############
    # #Metrics/Data	Checkpoint Path
    #NoGuideline_wo_NS - richere_test_without_guideline_wo_NS
    model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train_without_guideline_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-656/"
    # #Guideline-P_wo_NS - richere_test_guidelineP_wo_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train_guidelineP_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-1312/"
    # #Guideline-PN_wo_NS - richere_test_guidelinePN_wo_NS	
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train_guidelinePN_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-656/"
    # #Guideline-PS_wo_NS - richere_test_guidelinePS_wo_NS	
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train_guidelinePS_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-656/"
    # #Guideline-PN-Adv_wo_NS - richere_test_guidelinePN_Adv_wo_NS	
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train_guidelinePN_Adv_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-2296/"
    # #Guideline-PS-Adv_wo_NS - richere_test_guidelinePS_Adv_wo_NS	
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train_guidelinePS_Adv_wo_NS_rank_128_alpha_64_lr_1e-05/checkpoint-2952/"


    # #NoGuideline_w_NS	- richere_test_without_guideline_w_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train_without_guideline_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-32473/"
    # #Guideline-P_w_NS - richere_test_guidelineP_w_NS
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train_guidelineP_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-4639/"
    # #Guideline-PN_w_NS - richere_test_guidelinePN_w_NS	
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train_guidelinePN_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-32473/"
    # #Guideline-PS_w_NS - richere_test_guidelinePS_W_NS	
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/checkpoints/inst_richere_train_guidelinePS_w_NS_rank_128_alpha_64_lr_1e-05/checkpoint-18556/"
    # #Guideline-PN-Adv_w_NS - richere_test_guidelinePN_Adv_w_NS	
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/"
    # #Guideline-PS-Adv_w_NS - richere_test_guidelinePS_Adv_w_NS	
    # model_name_or_path = "/scratch/spati/tmp/LLaMA/"
    


    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    logger.info(f"Using device: {device}")
    
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name = model_name_or_path, max_seq_length=args.max_seq_length, load_in_4bit=args.load_in_4bit, dtype = None, cache_dir = "./original_models")
    # Prepare model with LoRA or QLoRA
    model = prepare_lora_model(args, model)
    
    
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
        data_collator = DataCollatorForSeq2Seq(tokenizer = tokenizer),
        dataset_num_proc=4,
        packing=False,
        args=TrainingArguments(
            run_name = f"sweta_{args.dataset_name}_{model_name_or_path}",
            fp16_full_eval=True,
            #change in future: previously 1, changed it to 4
            eval_accumulation_steps = 4, #virtual batch size (backprop after reaching certain batches)
            per_device_train_batch_size=args.per_device_train_batch_size,
            per_device_eval_batch_size=args.per_device_eval_batch_size,
            learning_rate=args.learning_rate,
            lr_scheduler_type=args.lr_scheduler_type,
            num_train_epochs=10,  # Use args or dynamic based on early stopping
            evaluation_strategy="epoch",#steps or epoch
            save_strategy = "epoch",
            eval_steps=1,
            save_steps=1,
            fp16=not is_bfloat16_supported(),
            bf16=is_bfloat16_supported(),
            output_dir=f"checkpoints/",
            logging_steps=4,
            optim="adamw_8bit",
            # report_to=["wandb"],  # Or tensorboard
            logging_dir="logs",
            weight_decay=0.01,
            warmup_steps = 350,
            seed = 1337,
            load_best_model_at_end = True,
            save_total_limit=5,
            include_inputs_for_metrics = True,
            metric_for_best_model = "eval_arg_cls_f1",
            # # For ed datasets:
            # metric_for_best_model = "eval_trigger_cls_f1"
        ),
        compute_metrics = load_dataset_metrics(args.dataset_name),#compute_metrics_wrapper(val_dataset, tokenizer),
        callbacks=[
            EarlyStoppingCallback(early_stopping_patience=args.patience),
            # WandbCallback()  # Add more callbacks if needed
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
    # print(val_dataset_copy[0])
    # xzzxxzxzxzxzxzxzx
    # Start Training

    torch.cuda.empty_cache()
    gc.collect()  # <----- Clear Python garbage

    # Track GPU memory usage
    print(torch.cuda.memory_summary(device=device, abbreviated=True))  # <----- Log memory usage


    # if(args.do_eval):
    #     trainer.evaluate(test_dataset)
    #changed this:
    trainer.evaluate(val_dataset, metric_key_prefix = "eval")

if __name__ == '__main__':
    # mp.set_start_method('spawn', force=True) 28462MiB # 3C    P0             378W / 500W |  28696MiB / 8
    args = parse_args()
    main(args)

