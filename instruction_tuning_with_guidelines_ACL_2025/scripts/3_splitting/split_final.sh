#!/bin/bash

# ===========================================
# Script: run_generate_final_splits.sh
# Description:
#     Filters the final instruction-style dataset using instance ID split files
#     Generates: train.json, dev.json, test.json for each dataset, guideline, and split
# ===========================================

# List of datasets
datasets=("ace05-en" "richere-en")

# List of guideline variants
guideline_variants=("No_guideline" "guideline_H" "guideline_P" "guideline_PN" "guideline_PS" "guideline_PN_INT" "guideline_PS_INT")

# List of split folders (split1, split2, etc.)
split_folders=("split1" "split2" "split3" "split4" "split5")

# Path to your Python script
PYTHON_SCRIPT="split_final.py"

# Base path for I/O
BASE_DATA_DIR="../../data"

# ===========================================
# Run for each dataset, each guideline, and each split
# ===========================================
for dataset in "${datasets[@]}"; do
    echo "Processing dataset: $dataset"

    for guideline in "${guideline_variants[@]}"; do
        echo "   Guideline: $guideline"

        for split_folder in "${split_folders[@]}"; do
            echo "      ➤ Split: $split_folder"

            # Input paths
            root_directory="${BASE_DATA_DIR}/code_converted_data/${guideline}/${dataset}/splits_ids/${split_folder}"
            modified_master_file="${BASE_DATA_DIR}/code_converted_data/${guideline}/${dataset}/Final_input_output_data_${dataset}.json"
            output_directory="${BASE_DATA_DIR}/code_converted_data/${guideline}/${dataset}/final_data_split/${split_folder}"

            # Only run if files exist
            if [ -f "$modified_master_file" ] && [ -d "$root_directory" ]; then
                echo "      Splitting using IDs from: $root_directory"
                python "$PYTHON_SCRIPT" "$root_directory" "$modified_master_file" "$output_directory"
            else
                echo "      ⚠️ Skipping $dataset | $guideline | $split_folder — Missing input files or directory"
            fi

            echo "      Done: $dataset | $guideline | $split_folder"
            echo "--------------------------------------------------"
        done
    done

    echo "Completed all guideline splits for $dataset"
    echo "=================================================="
done

echo "🏁 All datasets, guideline variants, and splits processed."