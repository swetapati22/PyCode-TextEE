from tqdm import tqdm
from utils import *
import argparse
import json
import os
import re


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--dataset_directory", help="Dataset Directory", default="./../../TextEE/processed_data")
parser.add_argument("-d", "--dataset_name", help="Dataset Name", default="richere-en")

def extract_parents(event_name):
    parent_name = event_name[event_name.index("(")+1: event_name.index(")")]
    return parent_name

from collections import defaultdict
import json
from tqdm import tqdm

def create_event_meta_data(dataset, dataset_name, mapper_path="mapper.json",max_examples_per_label=5):
    mapper   = json.load(open(mapper_path))               # your ontology map
    meta     = defaultdict(lambda:                         # per-event label
                 {"examples": [], "parent_name": None, "arg_list": set()})
    ontology = defaultdict(set)                            # parent ➜ {child …}

    for sent in tqdm(dataset, total=len(dataset)):
        for ev in sent["event_mentions"]:
            et           = ev["event_type"]                # e.g.  Life:Die
            parent_et    = extract_parents(mapper[dataset_name].get(et, et))
            event_label  = clean_event_name(et, dataset_name)  # e.g. Die(LifeEvent)

            meta[event_label]["parent_name"] = parent_et
            ontology[parent_et].add(event_label)

            meta[event_label]["examples"].append(ev)

            for arg in ev["arguments"]:
                meta[event_label]["arg_list"].add(arg["role"])

    # turn the sets into lists so the object is JSON-friendly
    for v in meta.values():
        v["arg_list"] = sorted(v["arg_list"])
    ontology = {k: sorted(list(v)) for k, v in ontology.items()}

    for et in meta:
        print(f"et:{et}, count{len(meta[et]['examples'])}")
    print("---X---")
    print(ontology)
    print("---X---")
    return dict(meta), ontology


MAX_SAMPLES = 10
def get_best_fit(event_dataset, event_type, meta_data):
    print(">>>", meta_data[event_type]["examples"], type(meta_data[event_type]["examples"]))
    full_argument_list = meta_data[event_type]["arg_list"]
    def extract_field_types(results):
        field_types = set()
        for result in results:
            field_types.update(result.keys())
        return field_types
    # sorted_data = sorted(event_dataset, key = lambda x: len(x["examples"]), reverse = True)
    sorted_data = sorted(meta_data[event_type], key=lambda x: len(x["examples"]), reverse=True)
    all_fields = set(full_argument_list) - set(["mention"])
    covered_fields = set()
    selected_examples = []

    while covered_fields != all_fields and len(selected_examples) < MAX_SAMPLES:
        # print(covered_fields)
        # print(all_fields)
        # print('-'*100)
        best_example = None
        best_new_fields = set()

        for example in sorted_data:
            if example in selected_examples:
                continue  # Skip examples already added
            results = example["event_mentions"][event_type]["results"]
            # print(results)
            # xx
            fields = extract_field_types(results)- set(["mention"])
            # print(fields)
            # xx
            new_fields = fields - covered_fields
            if new_fields and len(new_fields) > len(best_new_fields):
                best_example = example
                best_new_fields = new_fields

        if best_example:
            selected_examples.append(best_example)
            covered_fields.update(best_new_fields)
    
    if len(selected_examples) < MAX_SAMPLES:
        remaining_examples = [ex for ex in sorted_data if ex not in selected_examples]
        remaining_slots = MAX_SAMPLES - len(selected_examples)
        selected_examples.extend(remaining_examples[:remaining_slots])

    # formatted_examples = tabulate(selected_examples, headers="keys")
    print(f"Finished event type {event_type} with {len(selected_examples)} samples. Arguments were: {full_argument_list}. Total {len(selected_examples)} number of samples")
    print(f"All positive examples look like: {selected_examples}")
    return selected_examples#formatted_examples


        
if __name__ == "__main__":
    args = parser.parse_args()
    dataset_name = args.dataset_name
    all_schemas = json.load(open("full_schema.json"))
    mapper = json.load(open("mapper.json"))
    mapper_dict = mapper[dataset_name]
    all_ets = [clean_event_name(k, dataset_name) for k in list(mapper_dict.keys())]
    print(all_schemas[all_ets[0]])
    dataset = [json.loads(x) for x in open(f"{args.dataset_directory}/{dataset_name}/split1/train.json")]
    meta_data, ontology = create_event_meta_data(dataset, dataset_name)
    get_best_fit(dataset, all_ets[0], meta_data)
    # print(meta_data)

