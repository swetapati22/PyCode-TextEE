#!/bin/bash

# ===========================================
# Script: data_preprocessing.sh
# Description: Converts TextEE JSON data into code-style prompts
#              Attaches available guideline settings per dataset
# ===========================================

# Dataset → Task type
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

# Optional custom separators
declare -A custom_separators=(
    ["mee"]="_"
)

# List of splits to process
split_folders=("split1" "split2" "split3" "split4" "split5") 

# ===========================================
# 1️⃣ Baseline Run: No Guidelines
# ===========================================

GUIDELINE_FILE_NAME="No_guideline"

for DATASET in "${!datasets_task_types[@]}"; do
    TASK_TYPE=${datasets_task_types[$DATASET]}
    CUSTOM_SEPARATOR=${custom_separators[$DATASET]:-"None"}

    for SPLIT in "${split_folders[@]}"; do
        ROOT_DIR="../../data/processed_data/${DATASET}/${SPLIT}/"
        [ -d "$ROOT_DIR" ] || { echo "⏭️ Skipping $DATASET - $SPLIT (not found)"; continue; }

        echo "Processing $DATASET - $SPLIT without guidelines..."

        GUIDELINES_FILE="../../data/synthesized_guidelines/${DATASET}/${GUIDELINE_FILE_NAME}.json"
        OUTPUT_BASE="../../data/code_converted_data/${GUIDELINE_FILE_NAME}/${DATASET}/${SPLIT}"
        MASTER_DATA="${OUTPUT_BASE}/preproc_script/Master_data_${DATASET}.json"
        MAPPER_DATA="${OUTPUT_BASE}/preproc_script/Mapper_data_${DATASET}.json"
        MASTER_EVENT_TYPES="${OUTPUT_BASE}/ont_preproc/Master_event_types_${DATASET}.json"
        MASTER_EVENT_ATTRIBUTES="${OUTPUT_BASE}/ont_preproc/Master_event_dataclasses_${DATASET}.json"
        EVENT_MAPPER_OUTPUT="${OUTPUT_BASE}/ont_preproc/Event_mapper_${DATASET}.json"
        FINAL_OUTPUT="${OUTPUT_BASE}/Master_data_with_Guidelines_${DATASET}.json"

        GENERATE_UNIQUE_EVENT_TYPES=1
        GENERATE_EVENT_ATTRIBUTES=1
        GENERATE_FINAL_OUTPUT=0
        IS_RANDOM=0

        python3 data_preprocessing.py \
            --task "$TASK_TYPE" \
            --root_dir "$ROOT_DIR" \
            --master_data "$MASTER_DATA" \
            --mapper_data "$MAPPER_DATA" \
            --master_event_types "$MASTER_EVENT_TYPES" \
            --master_event_attributes "$MASTER_EVENT_ATTRIBUTES" \
            --mapper_event_filepath "$EVENT_MAPPER_OUTPUT" \
            --custom_sep "$CUSTOM_SEPARATOR" \
            --dataset "$DATASET" \
            --guidelines_filepath "$GUIDELINES_FILE" \
            --final_output_filepath "$FINAL_OUTPUT" \
            --generate_unique_event_types "$GENERATE_UNIQUE_EVENT_TYPES" \
            --generate_event_attributes "$GENERATE_EVENT_ATTRIBUTES" \
            --generate_final_output "$GENERATE_FINAL_OUTPUT" \
            --is_random "$IS_RANDOM"

        echo "✅ Done: $DATASET - $SPLIT [No Guideline]"
        echo "------------------------------------------"
    done
done

# ===========================================
# 2️⃣ Guideline-Based Runs
# ===========================================

ALL_GUIDELINE_VARIANTS=("guideline_H" "guideline_P" "guideline_PN" "guideline_PS" "guideline_PN_INT" "guideline_PS_INT")
GENERATE_UNIQUE_EVENT_TYPES=1
GENERATE_EVENT_ATTRIBUTES=1
GENERATE_FINAL_OUTPUT=1
IS_RANDOM=1

for DATASET in "${!datasets_task_types[@]}"; do
    TASK_TYPE=${datasets_task_types[$DATASET]}
    CUSTOM_SEPARATOR=${custom_separators[$DATASET]:-"None"}

    for GUIDELINE_FILE_NAME in "${ALL_GUIDELINE_VARIANTS[@]}"; do
        GUIDELINES_FILE="../../data/synthesized_guidelines/${DATASET}/${GUIDELINE_FILE_NAME}.json"
        [ -f "$GUIDELINES_FILE" ] || { echo "❌ Skipping: $GUIDELINE_FILE_NAME not found for $DATASET"; continue; }

        for SPLIT in "${split_folders[@]}"; do
            ROOT_DIR="../../data/processed_data/${DATASET}/${SPLIT}/"
            [ -d "$ROOT_DIR" ] || { echo "⏭️ Skipping $DATASET - $SPLIT (not found)"; continue; }

            echo "Processing: $DATASET | Guideline = $GUIDELINE_FILE_NAME | Split = $SPLIT"

            OUTPUT_BASE="../../data/code_converted_data/${GUIDELINE_FILE_NAME}/${DATASET}/${SPLIT}"
            MASTER_DATA="${OUTPUT_BASE}/preproc_script/Master_data_${DATASET}.json"
            MAPPER_DATA="${OUTPUT_BASE}/preproc_script/Mapper_data_${DATASET}.json"
            MASTER_EVENT_TYPES="${OUTPUT_BASE}/ont_preproc/Master_event_types_${DATASET}.json"
            MASTER_EVENT_ATTRIBUTES="${OUTPUT_BASE}/ont_preproc/Master_event_dataclasses_${DATASET}.json"
            EVENT_MAPPER_OUTPUT="${OUTPUT_BASE}/ont_preproc/Event_mapper_${DATASET}.json"
            FINAL_OUTPUT="${OUTPUT_BASE}/Master_data_with_Guidelines_${DATASET}.json"

            python3 data_preprocessing.py \
                --task "$TASK_TYPE" \
                --root_dir "$ROOT_DIR" \
                --master_data "$MASTER_DATA" \
                --mapper_data "$MAPPER_DATA" \
                --master_event_types "$MASTER_EVENT_TYPES" \
                --master_event_attributes "$MASTER_EVENT_ATTRIBUTES" \
                --mapper_event_filepath "$EVENT_MAPPER_OUTPUT" \
                --custom_sep "$CUSTOM_SEPARATOR" \
                --dataset "$DATASET" \
                --guidelines_filepath "$GUIDELINES_FILE" \
                --final_output_filepath "$FINAL_OUTPUT" \
                --generate_unique_event_types "$GENERATE_UNIQUE_EVENT_TYPES" \
                --generate_event_attributes "$GENERATE_EVENT_ATTRIBUTES" \
                --generate_final_output "$GENERATE_FINAL_OUTPUT" \
                --is_random "$IS_RANDOM"

            echo "✅ Done: $DATASET - $SPLIT with $GUIDELINE_FILE_NAME"
            echo "------------------------------------------"
        done
    done
done

echo "🏁 All valid guideline combinations processed."
