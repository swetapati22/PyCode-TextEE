#!/bin/bash

# ===========================
# Script: data_processing_pipeline.sh
# Description:
#     Runs ontology preprocessing per dataset and consolidates all dataclasses.
# ===========================

# ----------------------------------------
# Stage 1: Ontology Preprocessing
# ----------------------------------------

echo -e "\n Stage 1: Ontology Preprocessing for Each Dataset"
echo "----------------------------------------"

# Supported datasets (edit as needed)
datasets=("ace05-en" "casie" "richere-en" "fewevent" "geneva" "genia2011" "genia2013" "m2e2" "maven" "mee" "mlee" "muc4" "phee" "rams" "speed" "wikievents")

total_datasets=${#datasets[@]}
success_count=0
fail_count=0
skipped_count=0
failed_datasets=()
skipped_datasets=()


BASE_ROOT="../../data/processed_data"   # default
while [[ $# -gt 0 ]]; do
  case $1 in
    --root_dir)
      BASE_ROOT="$2"
      shift 2 ;;
    *) echo "Unknown option $1"; exit 1 ;;
  esac
done


for DATASET in "${datasets[@]}"
do
  #ROOT_DIR="../../data/processed_data/${DATASET}/split1/"
  ROOT_DIR="${BASE_ROOT%/}/${DATASET}/split1/"
  # ❗ Skip if the processed_data folder does not exist
  if [ ! -d "$ROOT_DIR" ]; then
    echo "⚠️ Skipping: $DATASET (missing folder: $ROOT_DIR)"
    skipped_datasets+=("$DATASET")
    skipped_count=$((skipped_count + 1))
    continue
  fi

  if [ "$DATASET" == "mee" ]; then
    CUSTOM_SEPARATOR="_"
  else
    CUSTOM_SEPARATOR="None"
  fi

  MASTER_EVENT_TYPES="../../data/extracted_ontology/${DATASET}/Master_event_types_${DATASET}.json"
  MASTER_EVENT_ATTRIBUTES="../../data/extracted_ontology/${DATASET}/Master_event_dataclasses_${DATASET}.json"
  CLASS_HIERARCHY_PYTHON="../../data/extracted_ontology/${DATASET}/Dataclass_${DATASET}.py"
  CLASS_HIERARCHY_JSON="../../data/extracted_ontology/${DATASET}/Dataclass_events_${DATASET}.json"
  MAPPER_OUTPUT="../../data/extracted_ontology/${DATASET}/Event_mapper_${DATASET}.json"

  echo "📦 Processing dataset: $DATASET"

  python3 ontology_preprocessing.py \
    --root_dir "$ROOT_DIR" \
    --master_event_types "$MASTER_EVENT_TYPES" \
    --master_event_attributes "$MASTER_EVENT_ATTRIBUTES" \
    --python_class_hierarchy "$CLASS_HIERARCHY_PYTHON" \
    --json_class_hierarchy "$CLASS_HIERARCHY_JSON" \
    --mapper_output_filepath "$MAPPER_OUTPUT" \
    --custom_sep "$CUSTOM_SEPARATOR" \
    --dataset "$DATASET"

  if [ $? -ne 0 ]; then
    echo "❌ Error processing: $DATASET"
    failed_datasets+=("$DATASET")
    fail_count=$((fail_count + 1))
  else
    echo "✅ Successfully processed: $DATASET"
    success_count=$((success_count + 1))
  fi

  echo "----------------------------------------"
done

echo -e "\n📊 Ontology Preprocessing Summary:"
echo "📁 Total requested: $total_datasets"
echo "✅ Successful: $success_count"
echo "❌ Failed: $fail_count"
echo "⏭️ Skipped: $skipped_count"

if [ $fail_count -gt 0 ]; then
  echo "⚠️ Failed datasets: ${failed_datasets[*]}"
fi

if [ $skipped_count -gt 0 ]; then
  echo "ℹ️ Skipped datasets: ${skipped_datasets[*]}"
fi

# ----------------------------------------
# Stage 2: Dataclass Consolidation
# ----------------------------------------

echo -e "\n Stage 2: Consolidating All Dataclasses"
echo "----------------------------------------"

# Only include datasets that weren't skipped
INCLUDED_DATASETS=()
for DATASET in "${datasets[@]}"
do
  if [[ ! " ${skipped_datasets[@]} " =~ " ${DATASET} " ]]; then
    INCLUDED_DATASETS+=("$DATASET")
  fi
done

INPUT_DIR="../../data/extracted_ontology"
OUTPUT_FILE="../../data/extracted_ontology/Master_dataclass.py"

echo "📁 Input datasets: ${INCLUDED_DATASETS[*]}"
echo "📤 Output file: $OUTPUT_FILE"

python3 consolidate_dataclasses.py \
  --datasets "${INCLUDED_DATASETS[@]}" \
  --input_dir "$INPUT_DIR" \
  --output_file "$OUTPUT_FILE"

if [ $? -ne 0 ]; then
  echo "❌ Error consolidating dataclasses"
else
  echo "✅ Master Dataclass Consolidation Complete"
fi

echo -e "\n🎉 Ontology generation and merging finished!"
