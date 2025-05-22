# ===========================
# File: sample_n_data.py
# Description:
#     Sample from instruction-style event data with full event-type coverage
#     and configurable proportion of null examples.
# ===========================

import os
import json
import argparse
import random
from collections import defaultdict

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

def load_event_types(filepath):
    types = load_json(filepath)
    return [etype.split("(")[0] for etype in types]

def sample_data_with_distribution(data, event_types, total_samples, null_percent):
    event_dict = defaultdict(list)
    for entry in data:
        output = entry.get("output", "")
        matched = False
        for etype in event_types:
            if etype in output:
                event_dict[etype].append(entry)
                matched = True
                break
        if not matched:
            event_dict["[]"].append(entry)

    sampled_data = []
    used_ids = set()

    # Sample null examples first
    num_null = int(total_samples * null_percent)
    null_pool = event_dict["[]"]
    null_sampled = random.sample(null_pool, min(len(null_pool), num_null))
    sampled_data.extend(null_sampled)
    used_ids.update(entry["instance_id"] for entry in null_sampled)

    # Sample from event types
    remaining = total_samples - len(sampled_data)
    per_type_quota = max(1, remaining // len(event_types))
    event_samples = []
    for etype in event_types:
        samples = [entry for entry in event_dict[etype] if entry["instance_id"] not in used_ids]
        if len(samples) >= per_type_quota:
            chosen = random.sample(samples, per_type_quota)
            event_samples.extend(chosen)
            used_ids.update(entry["instance_id"] for entry in chosen)
        elif samples:
            event_samples.extend(samples)
            used_ids.update(entry["instance_id"] for entry in samples)

    sampled_data.extend(event_samples)

    # Top up if under-sampled
    if len(sampled_data) < total_samples:
        all_ids = set(entry["instance_id"] for entry in data)
        unused_ids = list(all_ids - used_ids)
        id_to_entry = {entry["instance_id"]: entry for entry in data}
        topup = [id_to_entry[iid] for iid in random.sample(unused_ids, min(total_samples - len(sampled_data), len(unused_ids)))]
        sampled_data.extend(topup)

    # Trim if oversampled
    if len(sampled_data) > total_samples:
        sampled_data = random.sample(sampled_data, total_samples)

    return sampled_data

def get_instance_ids(data):
    return [entry["instance_id"] for entry in data]

def save_ids_to_txt(ids, path):
    with open(path, 'w') as f:
        for i in ids:
            f.write(i + "\n")

def load_ids_from_txt(path):
    with open(path, 'r') as f:
        return [line.strip() for line in f]

def main(args):
    for dataset in args.datasets:
        print(f"\n🧪 Processing Dataset: {dataset}")
        reference_path = os.path.join(args.data_root, args.reference_guideline, dataset)

        for split_folder in args.split_folders:
            print(f"🔀 Split Folder: {split_folder}")

            for split_name in ["train", "dev", "test"]:
                for sample_size in args.sample_sizes:
                    split_file = os.path.join(reference_path, args.final_data_dir, split_folder, f"{split_name}.json")
                    event_file = os.path.join(reference_path, args.ontology_dir, f"Master_event_types_{dataset}.json")
                    id_dir = os.path.join(reference_path, "sampled_ids", split_folder)
                    os.makedirs(id_dir, exist_ok=True)
                    output_id_path = os.path.join(id_dir, f"{split_name}_{sample_size}_sampled_ids.txt")

                    if not os.path.exists(split_file):
                        print(f"   ⚠️ Skipping sampling: {split_file} not found [{dataset} | {args.reference_guideline}]")
                        continue

                    print(f"   📝 Sampling {sample_size} from {split_name} in {split_folder} [{dataset} | {args.reference_guideline}]")
                    data = load_json(split_file)
                    event_types = load_event_types(event_file)
                    sampled_data = sample_data_with_distribution(data, event_types, sample_size, args.null_percent)
                    sampled_ids = get_instance_ids(sampled_data)
                    save_ids_to_txt(sampled_ids, output_id_path)
                    print(f"   💾 Sample IDs saved to: {output_id_path}")

            for guideline in args.guidelines:
                print(f"\n📂 Sampling for guideline: {guideline} | Dataset: {dataset}")
                base_path = os.path.join(args.data_root, guideline, dataset)
                input_split_path = os.path.join(base_path, args.final_data_dir, split_folder)

                for split_name in ["train", "dev", "test"]:
                    for sample_size in args.sample_sizes:
                        sampled_ids_path = os.path.join(reference_path, "sampled_ids", split_folder, f"{split_name}_{sample_size}_sampled_ids.txt")
                        target_input_path = os.path.join(input_split_path, f"{split_name}.json")
                        output_json_path = os.path.join(input_split_path, f"{split_name}_{sample_size}_sampled.json")

                        if not os.path.exists(sampled_ids_path):
                            print(f"   ⚠️ Missing ID file: {sampled_ids_path} [{dataset} | {guideline}]")
                            continue

                        if not os.path.exists(target_input_path):
                            print(f"   ⚠️ Missing input JSON file: {target_input_path} [{dataset} | {guideline}]")
                            continue

                        all_data = load_json(target_input_path)
                        target_ids = load_ids_from_txt(sampled_ids_path)
                        filtered_data = [entry for entry in all_data if entry["instance_id"] in target_ids]
                        save_json(output_json_path, filtered_data)
                        print(f"   💾 Saved: {output_json_path} [{dataset} | {guideline}]")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_root", type=str, required=True)
    parser.add_argument("--final_data_dir", type=str, required=True)
    parser.add_argument("--ontology_dir", type=str, required=True)
    parser.add_argument("--datasets", nargs="+", required=True)
    parser.add_argument("--guidelines", nargs="+", required=True)
    parser.add_argument("--reference_guideline", type=str, required=True)
    parser.add_argument("--sample_sizes", nargs="+", type=int, required=True)
    parser.add_argument("--split_folders", nargs="+", required=True)
    parser.add_argument("--null_percent", type=float, default=0.3, help="Fraction of null samples (default: 0.3)")
    args = parser.parse_args()
    main(args)
