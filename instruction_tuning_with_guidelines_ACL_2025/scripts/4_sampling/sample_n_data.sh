#!/bin/bash

# ===========================================
# Script: sample_n_data.sh
# Description:
#     Run full sampling pipeline across datasets, guidelines, splits.
# ===========================================

DATA_ROOT="../../data/code_converted_data"
FINAL_DATA_DIR="final_data_split"
ONTOLOGY_DIR="ont_preproc"

DATASETS=("ace05-en" "richere-en")
GUIDELINES=("No_guideline" "guideline_H" "guideline_P" "guideline_PN" "guideline_PS" "guideline_PN_INT" "guideline_PS_INT")
REFERENCE_GUIDELINE="No_guideline"
SAMPLE_SIZES=(100 2000)
SPLIT_FOLDERS=("split1" "split2" "split3" "split4" "split5")
NULL_PERCENT=0.3

python sample_n_data.py \
    --data_root "$DATA_ROOT" \
    --final_data_dir "$FINAL_DATA_DIR" \
    --ontology_dir "$ONTOLOGY_DIR" \
    --datasets "${DATASETS[@]}" \
    --guidelines "${GUIDELINES[@]}" \
    --reference_guideline "$REFERENCE_GUIDELINE" \
    --sample_sizes "${SAMPLE_SIZES[@]}" \
    --split_folders "${SPLIT_FOLDERS[@]}" \
    --null_percent "$NULL_PERCENT"
