#!/bin/bash

# ===========================================
# Script: complete_split_pipeline.sh
# Description:
#   1. Generate instance ID split files (train/dev/test)
#   2. Filter final instruction-style data using those splits
# ===========================================

# ---------- Dataset → Preprocessing Split Path ----------
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

# ---------- Use wnd_id splitting? ----------
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

# ---------- Config ----------
datasets=("ace05-en" "casie" "richere-en" "fewevent" "geneva" "genia2011" "genia2013" "m2e2" "maven" "mee" "mlee" "muc4" "phee" "rams" "speed" "wikievents")
guideline_variants=("No_guideline" "guideline_H" "guideline_P" "guideline_PN" "guideline_PS" "guideline_PN_INT" "guideline_PS_INT")
split_folders=("split1" "split2" "split3" "split4" "split5")

BASE_DATA_DIR="../../data"
GEN_ID_SCRIPT="generate_split_ids.py"
SPLIT_FILTER_SCRIPT="split_final.py"

# ===========================================
# 🧩 Stage 1: Generate ID Split Files
# ===========================================
echo -e "\n🧩 Stage 1: Generating Instance Split IDs"
echo "==========================================="

for dataset in "${datasets[@]}"; do
    echo "Dataset: $dataset"

    preprocessing_base="${BASE_DATA_DIR}/processed_data/${preprocessing_bases[$dataset]}"
    wnd_id_setting="${split_by_wnd_id[$dataset]}"

    for guideline in "${guideline_variants[@]}"; do
        echo "  Guideline: $guideline"

        master_preprocessed_filepath="${BASE_DATA_DIR}/code_converted_data/${guideline}/${dataset}/split1/preproc_script/Mapper_data_${dataset}.json"
        splits_directory="${BASE_DATA_DIR}/code_converted_data/${guideline}/${dataset}/splits_ids"

        if [ ! -f "$master_preprocessed_filepath" ]; then
            echo "  ⚠️ Skipping $dataset | $guideline — Missing: $master_preprocessed_filepath"
            continue
        fi

        for split_folder in "${split_folders[@]}"; do
            echo "    ➤ Generating ID split: $split_folder"
            python "$GEN_ID_SCRIPT" \
                "$master_preprocessed_filepath" \
                "$splits_directory" \
                "$preprocessing_base" \
                "$split_folder" \
                "$wnd_id_setting"
        done

        echo "✅ Done ID generation for: $dataset | $guideline"
        echo "-------------------------------------------"
    done

    echo "Completed all variants for $dataset"
    echo "=================================================="
done

# ===========================================
# 🧩 Stage 2: Generate Final Data Splits
# ===========================================
echo -e "\n📦 Stage 2: Filtering Final Input-Output Files by Split IDs"
echo "==========================================="

for dataset in "${datasets[@]}"; do
    for guideline in "${guideline_variants[@]}"; do
        for split_folder in "${split_folders[@]}"; do

            root_directory="${BASE_DATA_DIR}/code_converted_data/${guideline}/${dataset}/splits_ids/${split_folder}"
            modified_master_file="${BASE_DATA_DIR}/code_converted_data/${guideline}/${dataset}/split1/Final_input_output_data_${dataset}.json"
            output_directory="${BASE_DATA_DIR}/code_converted_data/${guideline}/${dataset}/final_data_split/${split_folder}"

            if [ -f "$modified_master_file" ] && [ -d "$root_directory" ]; then
                echo "✅ Splitting: $dataset | $guideline | $split_folder"
                python "$SPLIT_FILTER_SCRIPT" "$root_directory" "$modified_master_file" "$output_directory"
            else
                echo "⚠️ Skipping: $dataset | $guideline | $split_folder — Missing input files or directories"
            fi
        done
    done
done

echo -e "\n🎯 Completed both ID generation and final data split filtering!"
