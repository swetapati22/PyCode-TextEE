# #!/bin/bash

# # ===========================
# # Script: add_negative_examples.sh
# # Description:
# #     Automatically adds negative examples across all guidelines, datasets, and splits.
# # ===========================

# # Configuration
# DATA_ROOT="../../data/code_converted_data"
# GUIDELINES_DIR="../../data/synthesized_guidelines"
# FINAL_DATA_DIR="final_data_split"
# NUM_NEGATIVE_INSTANCES=15
# IS_RANDOM="True"

# # List of datasets and guidelines
# DATASETS=("ace05-en" "richere-en")
# GUIDELINES=("No_guideline" "guideline_H" "guideline_P" "guideline_PN" "guideline_PS" "guideline_PN_INT" "guideline_PS_INT")
# # SPLIT_FOLDERS=("split1" "split2" "split3" "split4" "split5")
# SPLIT_FOLDERS=("split1")

# # Path to the Python script
# PYTHON_SCRIPT="add_neg_samples.py"

# # Loop over everything
# for GUIDELINE in "${GUIDELINES[@]}"; do
#   for DATASET in "${DATASETS[@]}"; do
#     echo ""
#     echo "🔍 Processing guideline: $GUIDELINE | dataset: $DATASET"

#     MASTER_EVENT_FILE="${DATA_ROOT}/${GUIDELINE}/${DATASET}/ont_preproc/Master_event_types_${DATASET}.json"
#     ACE_MASTER_FILE="${GUIDELINES_DIR}/${DATASET}/${GUIDELINE}.json"

#     if [[ ! -f "$MASTER_EVENT_FILE" ]] || [[ ! -f "$ACE_MASTER_FILE" ]]; then
#       echo "⚠️ Skipping: missing files for $GUIDELINE | $DATASET"
#       continue
#     fi

#     for SPLIT in "${SPLIT_FOLDERS[@]}"; do
#       SPLIT_DIR="${DATA_ROOT}/${GUIDELINE}/${DATASET}/${FINAL_DATA_DIR}/${SPLIT}"

#       if [[ ! -d "$SPLIT_DIR" ]]; then
#         echo "⚠️ Skipping: $SPLIT_DIR does not exist"
#         continue
#       fi

#       for FILE in "${SPLIT_DIR}"/train*.json; do
#         [[ $FILE == *_w_neg* ]] && continue  # Skip already processed files

#         OUTPUT_FILE="${FILE%.json}_w_neg_${NUM_NEGATIVE_INSTANCES}.json"

#         echo ""
#         # echo "==============================================="
#         # echo "➡️  Adding negatives to: $FILE"
#         # echo "📥  Master event types: $MASTER_EVENT_FILE"
#         # echo "📥  ACE guideline file: $ACE_MASTER_FILE"
#         # echo "💾  Output:             $OUTPUT_FILE"
#         # echo "==============================================="

#         python "$PYTHON_SCRIPT" \
#           --test_file "$FILE" \
#           --master_event_file "$MASTER_EVENT_FILE" \
#           --ace_master_file "$ACE_MASTER_FILE" \
#           --output_file "$OUTPUT_FILE" \
#           --is_random "$IS_RANDOM" \
#           --num_instances "$NUM_NEGATIVE_INSTANCES"

#         if [[ $? -eq 0 ]]; then
#           echo "✅ Saved: $OUTPUT_FILE"
#         else
#           echo "❌ Error processing: $FILE"
#         fi
#       done
#     done
#   done
# done

# echo -e "\n🎉 All negative sampling completed."


#!/bin/bash

# ===========================
# Script: add_negative_examples.sh
# Description:
#     Automatically adds negative examples across all guidelines, datasets, and splits.
# ===========================

# Configuration
DATA_ROOT="../../data/code_converted_data"
GUIDELINES_DIR="../../data/synthesized_guidelines"
FINAL_DATA_DIR="final_data_split"
MASTER_GUIDELINE_FILE="../../data/synthesized_guidelines/guidelines_merged_across_datasets.json"
NUM_NEGATIVE_INSTANCES=15
IS_RANDOM="True"

# List of datasets and guidelines
DATASETS=("ace05-en" "richere-en")
GUIDELINES=("No_guideline" "guideline_H" "guideline_P" "guideline_PN" "guideline_PS" "guideline_PN_INT" "guideline_PS_INT")
SPLIT_FOLDERS=("split1")

PYTHON_SCRIPT="add_neg_samples.py"

for GUIDELINE in "${GUIDELINES[@]}"; do
  for DATASET in "${DATASETS[@]}"; do
    echo ""
    echo "🔍 Processing guideline: $GUIDELINE | dataset: $DATASET"

    MASTER_EVENT_FILE="${DATA_ROOT}/${GUIDELINE}/${DATASET}/ont_preproc/Master_event_types_${DATASET}.json"

    # Choose guideline source
    if [[ "$GUIDELINE" == "No_guideline" ]]; then
      ACE_MASTER_FILE="${MASTER_GUIDELINE_FILE}"
      NO_GUIDELINE_FLAG="--no_guideline"
    else
      ACE_MASTER_FILE="${GUIDELINES_DIR}/${DATASET}/${GUIDELINE}.json"
      NO_GUIDELINE_FLAG=""
    fi

    # Check required files
    if [[ ! -f "$MASTER_EVENT_FILE" ]] || [[ ! -f "$ACE_MASTER_FILE" ]]; then
      echo "⚠️ Skipping: missing files for $GUIDELINE | $DATASET"
      continue
    fi

    for SPLIT in "${SPLIT_FOLDERS[@]}"; do
      SPLIT_DIR="${DATA_ROOT}/${GUIDELINE}/${DATASET}/${FINAL_DATA_DIR}/${SPLIT}"

      if [[ ! -d "$SPLIT_DIR" ]]; then
        echo "⚠️ Skipping: $SPLIT_DIR does not exist"
        continue
      fi

      for FILE in "${SPLIT_DIR}"/train*.json; do
        [[ $FILE == *_w_neg* ]] && continue

        OUTPUT_FILE="${FILE%.json}_w_neg_${NUM_NEGATIVE_INSTANCES}.json"

        echo ""
        echo "---------------------------------------------"
        echo "➡️  Adding negatives to: $FILE"
        echo "📥  Master event types: $MASTER_EVENT_FILE"
        echo "📥  ACE guideline file: $ACE_MASTER_FILE"
        echo "💾  Output:             $OUTPUT_FILE"
        echo "---------------------------------------------"

        python "$PYTHON_SCRIPT" \
          --test_file "$FILE" \
          --master_event_file "$MASTER_EVENT_FILE" \
          --ace_master_file "$ACE_MASTER_FILE" \
          --output_file "$OUTPUT_FILE" \
          --is_random "$IS_RANDOM" \
          --num_instances "$NUM_NEGATIVE_INSTANCES" \
          $NO_GUIDELINE_FLAG

        if [[ $? -eq 0 ]]; then
          echo "✅ Saved: $OUTPUT_FILE"
        else
          echo "❌ Error processing: $FILE"
        fi
      done
    done
  done
done

echo -e "\n🎉 All negative sampling completed."
