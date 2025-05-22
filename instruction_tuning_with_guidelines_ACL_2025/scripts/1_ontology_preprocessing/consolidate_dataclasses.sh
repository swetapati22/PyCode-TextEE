#!/bin/bash

# Navigate to the ontology_preprocessing folder to keep the path unchanged:

# Listing datasets in the desired order of preprocessing:
# Datasets can be from within this tested list or any others in code format:
DATASETS=("ace05-en" "casie" "richere-en" "fewevent" "geneva" "genia2011" "genia2013" "m2e2" "maven" "mee" "mlee" "muc4" "phee" "rams" "speed" "wikievents")

# Directory containing subfolders for each dataset, each having Dataclass_<dataset>.py
INPUT_DIR="../../data/extracted_ontology"

# Output file with consolidated master dataclass:
OUTPUT_FILE="../../data/extracted_ontology/Master_dataclass.py"

# Filter only existing dataclass files
VALID_DATASETS=()
SKIPPED_DATASETS=()

for DATASET in "${DATASETS[@]}"; do
  if [ -f "${INPUT_DIR}/${DATASET}/Dataclass_${DATASET}.py" ]; then
    VALID_DATASETS+=("$DATASET")
  else
    SKIPPED_DATASETS+=("$DATASET")
  fi
done

# If no valid dataclass files found, skip
if [ ${#VALID_DATASETS[@]} -eq 0 ]; then
  echo "⚠️  No valid dataclass files found. Skipping consolidation."
  exit 0
fi

# Run consolidation with valid datasets
echo "📁 Consolidating dataclass files for datasets: ${VALID_DATASETS[*]}"
python3 consolidate_dataclasses.py --datasets "${VALID_DATASETS[@]}" --input_dir "$INPUT_DIR" --output_file "$OUTPUT_FILE"

# Show skipped datasets, if any
if [ ${#SKIPPED_DATASETS[@]} -gt 0 ]; then
  echo -e "\n⚠️ Skipped datasets (no dataclass file found):"
  for ds in "${SKIPPED_DATASETS[@]}"; do
    echo "   - $ds"
  done
fi
echo ""

# Print outcome
if [ $? -eq 0 ]; then
  echo "✅ Successfully created: $OUTPUT_FILE"
else
  echo "❌ Consolidation failed."
fi


