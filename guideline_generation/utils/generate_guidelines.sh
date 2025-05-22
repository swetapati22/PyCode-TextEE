#!/bin/bash

# Usage:
# ./run_guideline_pipeline.sh <dataset_name> <guideline_type> <output_file>

# Get input arguments
DATASET_NAME=$1
GUIDELINE_TYPE=$2
OUTPUT_FILE=$3

# Run the first Python script
python create_guideline_gen_dataset.py \
  --dataset_name "$DATASET_NAME" \
  --guideline_type "$GUIDELINE_TYPE" 

# Run the second Python script using the same output file
python prompt_llms.py \
  --output_file "$OUTPUT_FILE"
