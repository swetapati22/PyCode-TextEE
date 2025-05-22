#!/bin/bash

#Navigate to the ontology_preprocessing folder to keep the path unchanged:

#Listing datasets in the desired order:
#Datasets can be from within these tested list of datasets or any other that you want to convert to code format:
# ("ace05-en" "casie" "richere-en" "fewevent" "geneva" "genia2011" "genia2013" "m2e2" "maven" "mee" "mlee" "muc4" "phee" "rams" "speed" "wikievents")
datasets=("ace05-en" "casie" "richere-en" "fewevent" "geneva" "genia2011" "genia2013" "m2e2" "maven" "mee" "mlee" "muc4" "phee" "rams" "speed" "wikievents")

#Counters for successful and failed runs:
total_datasets=${#datasets[@]}
success_count=0
fail_count=0
skipped_count=0
failed_datasets=()
skipped_datasets=()

#Going through each dataset:
for DATASET in "${datasets[@]}"
do
  #Changing the custom separator based on the dataset:
  if [ "$DATASET" == "mee" ]; then
    CUSTOM_SEPARATOR="_"
  else
    CUSTOM_SEPARATOR="None"
  fi

  #File Paths:
  ROOT_DIR="../../data/processed_data/${DATASET}/split1/"

  # 🧩 Skip if root directory doesn't exist
  if [ ! -d "$ROOT_DIR" ]; then
    echo "⚠️ Skipping $DATASET — missing folder: $ROOT_DIR"
    skipped_datasets+=("$DATASET")
    skipped_count=$((skipped_count + 1))
    continue
  fi

  #File Paths to store event ontology in different formats:
  MASTER_EVENT_TYPES="../../data/extracted_ontology/${DATASET}/Master_event_types_${DATASET}.json"
  MASTER_EVENT_ATTRIBUTES="../../data/extracted_ontology/${DATASET}/Master_event_dataclasses_${DATASET}.json"
  CLASS_HIERARCHY_PYTHON="../../data/extracted_ontology/${DATASET}/Dataclass_${DATASET}.py"
  CLASS_HIERARCHY_JSON="../../data/extracted_ontology/${DATASET}/Dataclass_events_${DATASET}.json"
  MAPPER_OUTPUT="../../data/extracted_ontology/${DATASET}/Event_mapper_${DATASET}.json"

  #Current dataset information:
  echo "Processing dataset: $DATASET"
  
  #Running the python script:
  python3 ontology_preprocessing.py \
      --root_dir "$ROOT_DIR" \
      --master_event_types "$MASTER_EVENT_TYPES" \
      --master_event_attributes "$MASTER_EVENT_ATTRIBUTES" \
      --python_class_hierarchy "$CLASS_HIERARCHY_PYTHON" \
      --json_class_hierarchy "$CLASS_HIERARCHY_JSON" \
      --mapper_output_filepath "$MAPPER_OUTPUT" \
      --custom_sep "$CUSTOM_SEPARATOR" \
      --dataset "$DATASET"

  #Checking the progress:
  if [ $? -ne 0 ]; then
    echo "Error processing dataset: $DATASET. Marking as failed."
    failed_datasets+=("$DATASET")
    fail_count=$((fail_count + 1))
  else
    echo "Successfully processed dataset: $DATASET"
    success_count=$((success_count + 1))
  fi

  echo "----------------------------------------"

done

#Printing the stats of progress:
echo "Summary:"
echo "Total datasets: $total_datasets"
echo "Successfully processed: $success_count"
echo "Failed: $fail_count"
echo "Skipped: $skipped_count"

if [ $fail_count -gt 0 ]; then
  echo "Failed datasets: ${failed_datasets[@]}"
fi

if [ $skipped_count -gt 0 ]; then
  echo "Skipped datasets: ${skipped_datasets[@]}"
fi

echo "Processing completed."
