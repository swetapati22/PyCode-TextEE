#!/bin/bash

# ===========================
# Script: enumerate_test_dev.sh
# Description:
#     Adds enumerated negative examples to test and dev files for each dataset.
# ===========================

DATASETS=("ace05-en" "richere-en")
GUIDELINE_MODELS=("No_guideline" "guideline_H" "guideline_P" "guideline_PN" "guideline_PS" "guideline_PN_INT" "guideline_PS_INT")
SPLITS=("split1" "split2" "split3" "split4" "split5")  # You can run only desired splits
# GUIDELINE_MODELS=("guideline_PN_INT")
# SPLITS=("split1")  # You can run only desired splits

DATA_ROOT="../../data/code_converted_data"
GUIDELINES_DIR="../../data/synthesized_guidelines"
NO_GUIDELINE_DEF_FILE="../../data/synthesized_guidelines/guidelines_merged_across_datasets.json"
IS_RANDOM="True"
PYTHON_SCRIPT="test_enumeration.py"

for GUIDELINE in "${GUIDELINE_MODELS[@]}"; do
  for DATASET in "${DATASETS[@]}"; do
    echo "🔍 Processing: $GUIDELINE | $DATASET"

    MASTER_EVENT_FILE="${DATA_ROOT}/${GUIDELINE}/${DATASET}/ont_preproc/Master_event_types_${DATASET}.json"

    if [[ "$GUIDELINE" == "No_guideline" ]]; then
      ACE_MASTER_FILE="$NO_GUIDELINE_DEF_FILE"
      NO_GUIDELINE_FLAG="--no_guideline"
    else
      ACE_MASTER_FILE="${GUIDELINES_DIR}/${DATASET}/${GUIDELINE}.json"
      NO_GUIDELINE_FLAG=""
    fi

    for SPLIT in "${SPLITS[@]}"; do
      SPLIT_PATH="${DATA_ROOT}/${GUIDELINE}/${DATASET}/final_data_split/${SPLIT}"
      if [[ -d "$SPLIT_PATH" ]]; then
        for FILE in "$SPLIT_PATH"/*.json; do
          if [[ "$FILE" == *test*.json || "$FILE" == *dev*.json ]]; then
            OUTPUT_FILE="${FILE%.json}_enumerated.json"
            echo ""
            # echo "---------------------------------------------"
            # echo "📂 SPLIT: $SPLIT"
            # echo "➡️  Enumerating: $FILE"
            # echo "📥  Master event types: $MASTER_EVENT_FILE"
            # echo "📥  ACE master definitions: $ACE_MASTER_FILE"
            # echo "💾  Output: $OUTPUT_FILE"
            # echo "---------------------------------------------"

            python "$PYTHON_SCRIPT" \
              --test_file "$FILE" \
              --master_event_file "$MASTER_EVENT_FILE" \
              --ace_master_file "$ACE_MASTER_FILE" \
              --output_file "$OUTPUT_FILE" \
              --is_random "$IS_RANDOM" \
              $NO_GUIDELINE_FLAG

            if [[ $? -eq 0 ]]; then
              echo "✅ Saved: $OUTPUT_FILE"
            else
              echo "❌ Error processing: $FILE"
            fi
          fi
        done
      fi
    done
  done
done

echo -e "\n🎉 Test and dev file enumeration completed."
