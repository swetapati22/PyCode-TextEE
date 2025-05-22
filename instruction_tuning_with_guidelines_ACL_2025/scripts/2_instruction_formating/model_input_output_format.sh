#!/bin/bash

# ===========================================
# Script: model_input_output_format.sh
# Description: Converts code-style event prompts into model-ready instruction format
#              Handles multiple datasets and guideline settings
# ===========================================

# Dataset → Task type mapping
declare -A datasets_task_types=(
    ["ace05-en"]="E2E"
    ["richere-en"]="E2E"
    ["mlee"]="E2E"
    ["genia2011"]="E2E"
    ["genia2013"]="E2E"
    ["m2e2"]="E2E"
    ["casie"]="E2E"
    ["phee"]="E2E"
    ["maven"]="ED"
    ["fewevent"]="ED"
    ["speed"]="ED"
    ["mee"]="ED"
    ["wikievents"]="EAE"
    ["rams"]="EAE"
    ["muc4"]="EAE"
    ["geneva"]="EAE"
)

# All guideline variants
ALL_GUIDELINE_VARIANTS=("guideline_H" "guideline_P" "guideline_PN" "guideline_PS" "guideline_PN_INT" "guideline_PS_INT")

# Split folders to loop over
split_folders=("split1" "split2" "split3" "split4" "split5")

# Paths
PYTHON_SCRIPT="model_input_output_format.py"
BASE_DATA_DIR="../../data"
GUIDELINE_MERGED_FILE="${BASE_DATA_DIR}/synthesized_guidelines/guidelines_merged_across_datasets.json"

# ===========================================
# 1️⃣ Baseline Run — No Guidelines
# ===========================================
for dataset in "${!datasets_task_types[@]}"; do
    task_type="${datasets_task_types[$dataset]}"

    for split in "${split_folders[@]}"; do
        INPUT_FILE="${BASE_DATA_DIR}/code_converted_data/No_guideline/${dataset}/${split}/preproc_script/Master_data_${dataset}.json"
        OUTPUT_FILE="${BASE_DATA_DIR}/code_converted_data/No_guideline/${dataset}/${split}/Final_input_output_data_${dataset}.json"

        if [ ! -f "$INPUT_FILE" ]; then
            echo "⏭️ Skipping: $dataset - $split (missing baseline input)"
            continue
        fi

        echo "[NO-GUIDELINE] Processing: $dataset - $split"

        python3 "$PYTHON_SCRIPT" \
            --input_filepath "$INPUT_FILE" \
            --output_filepath "$OUTPUT_FILE" \
            --guidelines_file "$GUIDELINE_MERGED_FILE" \
            --task "$task_type" \
            --dataset "$dataset"

        echo "✅ Done: $dataset - $split [No Guideline]"
        echo "------------------------------------------"
    done
done

# ===========================================
# 2️⃣ Guideline-based Runs
# ===========================================
for dataset in "${!datasets_task_types[@]}"; do
    task_type="${datasets_task_types[$dataset]}"

    for guideline_variant in "${ALL_GUIDELINE_VARIANTS[@]}"; do
        GUIDELINE_FILE="${BASE_DATA_DIR}/synthesized_guidelines/${dataset}/${guideline_variant}.json"
        if [ ! -f "$GUIDELINE_FILE" ]; then
            echo "❌ Skipping: $guideline_variant not found for $dataset"
            continue
        fi

        for split in "${split_folders[@]}"; do
            INPUT_FILE="${BASE_DATA_DIR}/code_converted_data/${guideline_variant}/${dataset}/${split}/Master_data_with_Guidelines_${dataset}.json"
            OUTPUT_FILE="${BASE_DATA_DIR}/code_converted_data/${guideline_variant}/${dataset}/${split}/Final_input_output_data_${dataset}.json"

            if [ ! -f "$INPUT_FILE" ]; then
                echo "⏭️ Skipping: $dataset - $split (missing guideline input: $guideline_variant)"
                continue
            fi

            echo "Processing: $dataset | Guideline = $guideline_variant | Split = $split"

            python3 "$PYTHON_SCRIPT" \
                --input_filepath "$INPUT_FILE" \
                --output_filepath "$OUTPUT_FILE" \
                --guidelines_file "$GUIDELINE_FILE" \
                --task "$task_type" \
                --dataset "$dataset"

            echo "✅ Done: $dataset - $split with $guideline_variant"
        done

        echo "═════════════════════════════════════════════════════════════════════════════"
        echo "🗂️  Completed: $dataset for Guideline = $guideline_variant (All splits)"
        echo "═════════════════════════════════════════════════════════════════════════════"
        echo ""
    done
done

echo "🏁 All datasets and guideline variants processed."
