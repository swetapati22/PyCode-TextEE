from datasets import Dataset
import os
import json
import random
from tqdm import tqdm
from datasets import load_dataset
from sklearn.model_selection import train_test_split


def get_shot_data(key, shot_count, shot_data):
    shots = [data for idx, data in enumerate(shot_data)]
    shots_data = random.sample(shots, shot_count)
    return shots_data

def manage_dataset(dataset, key, shots = None, shot_data = None):
    conversations = []
    for idx, d in tqdm(enumerate(dataset), total=len(dataset), desc=f"Preparing: {key}"):
        # print(d)
        question, answer, task_type = d["instruction"] + "\n\n" + d["input"], d["output"], d["task_type"]
        # answer = answer.replace("####", "Therefore, the answer is ####") + " ####"
        # Structure the conversation as a list of dictionaries
        conversation = [
            {"role": "user", "content": question, "gt":"", "key": key, "task_type": task_type},
            {"role": "assistant", "content": answer if key == "train" else "", "gt":answer, "key": key, "task_type":task_type}
        ]
        conversations.append(conversation)
    
    # Convert the structured list into a Dataset object
    dataset_dict = {"conversations": conversations}
    with open(f"/scratch/spati/tmp/LLaMA/datasets/richere_test100_guidelinePN_Adv_w_NS_iter2_{key}_sole_data.json", "w") as f:
        json.dump(dataset_dict, f, indent = 4)
    # Convert to Dataset format
    return Dataset.from_dict(dataset_dict) 

def richere_test100_guidelinePN_Adv_w_NS_iter2(shot_data = False):
    # ds = load_dataset("openai/gsm8k", "main")
    # train_dataset = manage_dataset(ds["train"], "train")
    k = 8
    # full_train_dataset = [x for x in ds["train"]]
    # train_data, valid_data = train_test_split(
    #     full_train_dataset, test_size=.15, random_state=1337
    # )
    train_data, valid_data = json.load(open("/scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments_richere/richere_15random_adv_guidelines/final_data_split/PA_iter2_100_train_w_neg.json")), json.load(open("/scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments_richere/richere_15random_adv_guidelines/final_data_split/test_final.json"))
    test_data = json.load(open("/scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments_richere/richere_15random_adv_guidelines/final_data_split/test_final.json"))
    train_dataset = manage_dataset(train_data, "train", None, None)
    valid_dataset = manage_dataset(valid_data, "valid", None, None)
    test_dataset = manage_dataset(test_data, "test", None, None)
    
    print(f"Train dataset size: {len(train_dataset)}")
    print(f"Validation dataset size: {len(valid_dataset)}")
    print(f"Test dataset size: {len(test_dataset)}")
    # print(train_dataset[0])
    # print(valid_dataset[0])
    # print(test_dataset[0])
    return {"train_dataset": train_dataset, "valid_dataset": valid_dataset, "test_dataset": test_dataset}
    # return {"train_dataset": train_dataset, "valid_dataset": valid_dataset}




if __name__ == "__main__":
    load_ACE()