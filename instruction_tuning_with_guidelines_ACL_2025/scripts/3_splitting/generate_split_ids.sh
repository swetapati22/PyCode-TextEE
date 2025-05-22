#!/bin/bash

# ===========================================
# Script: run_generate_split_ids.sh
# Description:
#     Generates split ID files (train.json, dev.json, test.json)
#     for each dataset, guideline variant, and split folder.
#     Based on whether the split is by doc_id or wnd_id.
# ===========================================

# Dataset → Preprocessing split folder path
declare -A preprocessing_bases=(
    ["ace05-en"]="ace05-en/split-en"
    ["casie"]="casie/split-en"
    ["richere-en"]="richere-en/split-en"
    ["fewevent"]="fewevent/split-en"
    ["geneva"]="geneva/split-en"
    ["genia2011"]="genia2011/split-en"
    ["genia2013"]="genia2013/split-en"
    ["m2e2"]="m2e2/split-en"
    ["maven"]="maven/split-en"
    ["mee"]="mee/split-en"
    ["mlee"]="mlee/split-en"
    ["muc4"]="muc4/split-en"
    ["phee"]="phee/split-en"
    ["rams"]="rams/split-en"
    ["speed"]="speed/split-en"
    ["wikievents"]="wikievents/split-en"
)

# Dataset → Use wnd_id for splitting or not
declare -A split_by_wnd_id=(
    ["ace05-en"]=False
    ["casie"]=False
    ["richere-en"]=False
    ["fewevent"]=False
    ["geneva"]=True
    ["genia2011"]=False
    ["genia2013"]=False
    ["m2e2"]=False
    ["maven"]=False
    ["mee"]=False
    ["mlee"]=False
    ["muc4"]=False
    ["phee"]=False
    ["rams"]=False
    ["speed"]=False
    ["wikievents"]=False
)

# List of datasets to run
datasets=("ace05-en" "richere-en")

# List of guideline variants to run across
guideline_variants=("No_guideline" "guideline_H" "guideline_P" "guideline_PN" "guideline_PS" "guideline_PN_INT" "guideline_PS_INT")

# List of split folders
split_folders=("split1" "split2" "split3" "split4" "split5")

# Python script that handles the ID splitting
PYTHON_SCRIPT="generate_split_ids.py"

# Base path to your data
BASE_DATA_DIR="../../data"

# ===========================================
# 🧩 Loop over everything
# ===========================================
for dataset in "${datasets[@]}"; do
    echo " Dataset: $dataset"

    preprocessing_base="${BASE_DATA_DIR}/processed_data/${preprocessing_bases[$dataset]}"
    wnd_id_setting="${split_by_wnd_id[$dataset]}"

    for guideline in "${guideline_variants[@]}"; do
        echo "   Guideline: $guideline"

        master_preprocessed_filepath="${BASE_DATA_DIR}/code_converted_data/${guideline}/${dataset}/preproc_script/Mapper_data_${dataset}.json"
        splits_directory="${BASE_DATA_DIR}/code_converted_data/${guideline}/${dataset}/splits_ids"

        if [ ! -f "$master_preprocessed_filepath" ]; then
            echo "   ⚠️ Skipping $dataset | $guideline — Missing: $master_preprocessed_filepath"
            continue
        fi

        for split_folder in "${split_folders[@]}"; do
            echo "      ➤ Split: $split_folder"

            python "$PYTHON_SCRIPT" \
                "$master_preprocessed_filepath" \
                "$splits_directory" \
                "$preprocessing_base" \
                "$split_folder" \
                "$wnd_id_setting"
        done

        echo "   Done: $dataset | $guideline"
        echo "------------------------------------------"
    done

    echo "Completed all variants for $dataset"
    echo "=================================================="
done

echo "🏁 All datasets processed across all guideline variants and splits."
