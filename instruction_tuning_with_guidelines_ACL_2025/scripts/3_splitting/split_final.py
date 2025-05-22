"""
====================================================================
Script: split_final.py
Description:
    This script creates final train, dev, and test splits by filtering a master instruction-formatted dataset (converted to LLM-style input-output format) using instance IDs provided in split files.
    It is the final step of the preprocessing pipeline where:
    - The master data file (e.g., Final_input_output_<dataset>.json) contains all event extraction examples.

Inputs:
    - root_directory: Path to directory with train.json / dev.json / test.json (instance IDs)
    - modified_master_file: Path to the master dataset in LLM input-output format
    - output_directory: Where to save the split JSON files

Outputs:
    - train.json
    - dev.json
    - test.json

Usage:
    python split_final.py <split_ids_folder> <master_input_file> <output_folder>

    Example:
    python split_final.py \
        data/splits_ids/split1 \
        data/Final_input_output_ace05-en.json \
        data/final_data_split/
====================================================================
"""

import json
import os
import sys

# Function to load instance IDs for train, dev, and test
def load_instance_ids(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to filter instances by ID
def filter_instances_by_ids(instance_ids, dataset):
    return [instance for instance in dataset if instance['instance_id'] in instance_ids]

# Main function to process train, dev, and test
def process_splits(root_directory, modified_master_file, output_directory):
    # Ensure output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)  # Create the directory if it doesn't exist

    # Load the modified_final_master.json dataset
    with open(modified_master_file, 'r') as file:
        modified_master = json.load(file)

    # Process each of the splits (train, dev, test) one at a time
    for filename in ['train.json', 'dev.json', 'test.json']:
        input_filepath = os.path.join(root_directory, filename)
        
        # Check if the file exists
        if os.path.exists(input_filepath):
            print(f"Processing {filename}...")

            # Load the instance IDs
            instance_ids = load_instance_ids(input_filepath)

            # Filter the instances from modified_master
            filtered_instances = filter_instances_by_ids(instance_ids, modified_master)

            # Define the output file name
            output_filepath = os.path.join(output_directory, filename)

            # Save the filtered instances to the output directory
            with open(output_filepath, 'w') as output_file:
                json.dump(filtered_instances, output_file, indent=4)
            
            print(f"{filename} processing complete. Output saved to {output_filepath}")
        else:
            print(f"File {input_filepath} not found, skipping.")

# Retrieving paths from command line arguments
if len(sys.argv) != 4:
    print("Usage: python process_splits.py <root_directory> <modified_master_file> <output_directory>")
    sys.exit(1)

root_directory = sys.argv[1]
modified_master_file = sys.argv[2]
output_directory = sys.argv[3]

# Call the function to process the splits
process_splits(root_directory, modified_master_file, output_directory)