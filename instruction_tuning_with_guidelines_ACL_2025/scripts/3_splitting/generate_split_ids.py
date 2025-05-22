"""
==========================================================
 Script: split_instance_ids_doc_wnd.py
 Description:
    Given a master preprocessed dataset with `instance_id`s, this script creates train/dev/test split files containing only the instance IDs, based on document or window IDs as per the TextEE splits.

 Input:
    1. master_preprocessed_filepath (JSONL): File containing all instances with fields like 'doc_id', 'wnd_id', and 'inst_id'.
    2. splits_directory: Output directory to save train/dev/test split ID files.
    3. preprocessing_base: Directory containing original split files (train.txt, dev.txt, test.txt).
    4. split_folder: Name of the current split folder (e.g., split1).
    5. split_by_wnd_id (True/False): Whether to group by 'wnd_id' or 'doc_id'.

 Output:
    Saves three files in `<splits_directory>/<split_folder>/`:
        - train.json
        - dev.json
        - test.json
    Each file contains a list of instance IDs associated with the respective split.

 Usage:
    python split_instance_ids_doc_wnd.py <master_preprocessed_filepath> <splits_directory> <preprocessing_base> <split_folder> <split_by_wnd_id>

 Example:
    python split_instance_ids_doc_wnd.py \
        data/processed/Mapper_data_ace05-en.json \
        data/splits_ids \
        data/splits/ace05/split-en \
        split1 \
        False
==========================================================
"""

import os
import json
import sys

# Retrieve command line arguments
master_preprocessed_filepath = sys.argv[1]
splits_directory = sys.argv[2]
preprocessing_base = sys.argv[3]
split_folder = sys.argv[4]
split_by_wnd_id = sys.argv[5].lower() == 'true'  # Converts command line string to boolean

# Ensure split folders are created
os.makedirs(os.path.join(splits_directory, split_folder), exist_ok=True)

# Load the master preprocessed file into a dictionary for quick lookup
master_data = {}
with open(master_preprocessed_filepath, 'r') as master_file:
    for line in master_file:
        instance = json.loads(line.strip())
        # Determine whether to use doc_id or wnd_id for lookup
        key_id = instance['wnd_id'] if split_by_wnd_id else instance['doc_id']
        inst_id = instance['inst_id']

        if key_id not in master_data:
            master_data[key_id] = []
        master_data[key_id].append(inst_id)

# Function to create split files
def create_split_files(split_name, split_file_paths):
    for split_type, split_file in split_file_paths.items():
        output_file_path = os.path.join(splits_directory, split_name, f'{split_type}.json')

        with open(split_file, 'r') as f, open(output_file_path, 'w') as out_f:
            instance_ids = []
            for line in f:
                doc_or_wnd_id = line.strip()

                # Check if doc_or_wnd_id has a .txt extension and remove it if present
                if doc_or_wnd_id.endswith('.txt'):
                    doc_or_wnd_id = doc_or_wnd_id.replace('.txt', '')

                if doc_or_wnd_id in master_data:
                    instance_ids.extend(master_data[doc_or_wnd_id])
                else:
                    print(f"ID {doc_or_wnd_id} not found in master data (split: {split_name}, file: {split_type})")

            json.dump(instance_ids, out_f, indent=4)

# Define split file paths based on command line argument
split_file_paths = {
    'train': os.path.join(preprocessing_base, f'{split_folder}/train.txt'),
    'dev': os.path.join(preprocessing_base, f'{split_folder}/dev.txt'),
    'test': os.path.join(preprocessing_base, f'{split_folder}/test.txt'),
}

create_split_files(split_folder, split_file_paths)
print("Split files with instance IDs have been created successfully for", split_folder)
