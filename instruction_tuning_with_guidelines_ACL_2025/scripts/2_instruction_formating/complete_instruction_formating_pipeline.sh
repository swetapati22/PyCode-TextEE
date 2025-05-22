#!/bin/bash

# ===========================================
# Script: data_to_model_conversion.sh
# Description:
#     - Converts raw TextEE-style JSONs into dataclass-style prompts
#     - Attaches multiple guideline variants if available
#     - Converts dataclass-style prompts into instruction-style inputs
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

# Optional separators
declare -A custom_separators=(
    ["mee"]="_"
)

# Split folders to loop over
split_folders=("split1" "split2" "split3" "split4" "split5")

# List of all guideline variants
ALL_GUIDELINE_VARIANTS=("guideline_H" "guideline_P" "guideline_PN" "guideline_PS" "guideline_PN_INT" "guideline_PS_INT")

# Python script names
PREPROCESS_SCRIPT="data_preprocessing.py"
FORMAT_SCRIPT="model_input_output_format.py"
BASE_DATA_DIR="../../data"

# ===========================================
# 1️⃣ Baseline Run (No Guidelines)
# ===========================================

GUIDELINE_FILE_NAME="No_guideline"
MERGED_GUIDELINES_FILE="${BASE_DATA_DIR}/synthesized_guidelines/guidelines_merged_across_datasets.json"

for DATASET in "${!datasets_task_types[@]}"; do
    TASK_TYPE=${datasets_task_types[$DATASET]}
    CUSTOM_SEPARATOR=${custom_separators[$DATASET]:-"None"}

    for SPLIT in "${split_folders[@]}"; do
        ROOT_DIR="${BASE_DATA_DIR}/processed_data/${DATASET}/${SPLIT}"
        [ -d "$ROOT_DIR" ] || { echo "⏭️ Skipping $DATASET - $SPLIT (not found)"; continue; }

        echo "⚙️ Preprocessing $DATASET - $SPLIT [No Guidelines]..."

        # Output paths
        OUTPUT_BASE="${BASE_DATA_DIR}/code_converted_data/${GUIDELINE_FILE_NAME}/${DATASET}/${SPLIT}"
        MASTER_DATA="${OUTPUT_BASE}/preproc_script/Master_data_${DATASET}.json"
        MAPPER_DATA="${OUTPUT_BASE}/preproc_script/Mapper_data_${DATASET}.json"
        MASTER_EVENT_TYPES="${OUTPUT_BASE}/ont_preproc/Master_event_types_${DATASET}.json"
        MASTER_EVENT_ATTRIBUTES="${OUTPUT_BASE}/ont_preproc/Master_event_dataclasses_${DATASET}.json"
        EVENT_MAPPER_OUTPUT="${OUTPUT_BASE}/ont_preproc/Event_mapper_${DATASET}.json"
        FINAL_OUTPUT="${OUTPUT_BASE}/Master_data_with_Guidelines_${DATASET}.json"

        python3 "$PREPROCESS_SCRIPT" \
            --task "$TASK_TYPE" \
            --root_dir "$ROOT_DIR" \
            --master_data "$MASTER_DATA" \
            --mapper_data "$MAPPER_DATA" \
            --master_event_types "$MASTER_EVENT_TYPES" \
            --master_event_attributes "$MASTER_EVENT_ATTRIBUTES" \
            --mapper_event_filepath "$EVENT_MAPPER_OUTPUT" \
            --custom_sep "$CUSTOM_SEPARATOR" \
            --dataset "$DATASET" \
            --guidelines_filepath "${BASE_DATA_DIR}/synthesized_guidelines/${DATASET}/${GUIDELINE_FILE_NAME}.json" \
            --final_output_filepath "$FINAL_OUTPUT" \
            --generate_unique_event_types 1 \
            --generate_event_attributes 1 \
            --generate_final_output 0 \
            --is_random 0

        echo "✅ Preprocessed $DATASET - $SPLIT [No Guidelines]"

        echo "📤 Converting to model input-output format..."

        python3 "$FORMAT_SCRIPT" \
            --input_filepath "$MASTER_DATA" \
            --output_filepath="${OUTPUT_BASE}/Final_input_output_data_${DATASET}.json" \
            --guidelines_file "$MERGED_GUIDELINES_FILE" \
            --task "$TASK_TYPE" \
            --dataset "$DATASET"

        echo "✅ Done: $DATASET - $SPLIT [No Guidelines]"
        echo "------------------------------------------"
    done
done

# ===========================================
# 2️⃣ Guideline-Based Runs
# ===========================================

for DATASET in "${!datasets_task_types[@]}"; do
    TASK_TYPE=${datasets_task_types[$DATASET]}
    CUSTOM_SEPARATOR=${custom_separators[$DATASET]:-"None"}

    for GUIDELINE_FILE_NAME in "${ALL_GUIDELINE_VARIANTS[@]}"; do
        GUIDELINE_FILE="${BASE_DATA_DIR}/synthesized_guidelines/${DATASET}/${GUIDELINE_FILE_NAME}.json"
        [ -f "$GUIDELINE_FILE" ] || { echo "❌ Skipping: $GUIDELINE_FILE_NAME not found for $DATASET"; continue; }

        for SPLIT in "${split_folders[@]}"; do
            ROOT_DIR="${BASE_DATA_DIR}/processed_data/${DATASET}/${SPLIT}"
            [ -d "$ROOT_DIR" ] || { echo "⏭️ Skipping $DATASET - $SPLIT (not found)"; continue; }

            echo "⚙️ Preprocessing $DATASET | Guideline = $GUIDELINE_FILE_NAME | Split = $SPLIT"

            OUTPUT_BASE="${BASE_DATA_DIR}/code_converted_data/${GUIDELINE_FILE_NAME}/${DATASET}/${SPLIT}"
            MASTER_DATA="${OUTPUT_BASE}/preproc_script/Master_data_${DATASET}.json"
            MAPPER_DATA="${OUTPUT_BASE}/preproc_script/Mapper_data_${DATASET}.json"
            MASTER_EVENT_TYPES="${OUTPUT_BASE}/ont_preproc/Master_event_types_${DATASET}.json"
            MASTER_EVENT_ATTRIBUTES="${OUTPUT_BASE}/ont_preproc/Master_event_dataclasses_${DATASET}.json"
            EVENT_MAPPER_OUTPUT="${OUTPUT_BASE}/ont_preproc/Event_mapper_${DATASET}.json"
            FINAL_OUTPUT="${OUTPUT_BASE}/Master_data_with_Guidelines_${DATASET}.json"

            python3 "$PREPROCESS_SCRIPT" \
                --task "$TASK_TYPE" \
                --root_dir "$ROOT_DIR" \
                --master_data "$MASTER_DATA" \
                --mapper_data "$MAPPER_DATA" \
                --master_event_types "$MASTER_EVENT_TYPES" \
                --master_event_attributes "$MASTER_EVENT_ATTRIBUTES" \
                --mapper_event_filepath "$EVENT_MAPPER_OUTPUT" \
                --custom_sep "$CUSTOM_SEPARATOR" \
                --dataset "$DATASET" \
                --guidelines_filepath "$GUIDELINE_FILE" \
                --final_output_filepath "$FINAL_OUTPUT" \
                --generate_unique_event_types 1 \
                --generate_event_attributes 1 \
                --generate_final_output 1 \
                --is_random 1

            echo "✅ Preprocessed $DATASET - $SPLIT with $GUIDELINE_FILE_NAME"

            echo "📤 Converting to model input-output format..."

            python3 "$FORMAT_SCRIPT" \
                --input_filepath "$FINAL_OUTPUT" \
                --output_filepath="${OUTPUT_BASE}/Final_input_output_data_${DATASET}.json" \
                --guidelines_file "$GUIDELINE_FILE" \
                --task "$TASK_TYPE" \
                --dataset "$DATASET"

            echo "✅ Done: $DATASET - $SPLIT with $GUIDELINE_FILE_NAME"
            echo "═════════════════════════════════════════════════════════════"
        done
    done
done

echo "🎉 All data → prompt → instruction conversions complete!"
