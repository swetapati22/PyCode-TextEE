#!/bin/bash

# ===========================
# Script: data_processing_pipeline.sh
# Description:
#   Full IT-LLAMA Data Pipeline (All 6 Stages)
#   Run from: /scratch/spati/tmp/LLaMA/IT_LLaMA/scripts
# ===========================

echo "=========================================="
echo "🚀 Starting Full IT-LLAMA Data Pipeline"
echo "=========================================="

BASE_DIR=$(pwd)  # Save current directory (/scripts)

# ----------------------------------------
# Stage 1: Ontology Preprocessing
# ----------------------------------------
echo -e "\n🔧 Stage 1: Ontology Preprocessing"
cd 1_ontology_preprocessing && bash complete_ontology_pipeline.sh || echo "⚠️ Stage 1 failed, continuing..."
cd "$BASE_DIR"
echo -e "⭐️ Completed Stage 1\n=========================================="

# ----------------------------------------
# Stage 2: Prompt + Instruction Format Conversion
# ----------------------------------------
echo -e "\n🧠 Stage 2: Prompt + Instruction Formatting"
cd 2_instruction_formating && bash complete_instruction_formating_pipeline.sh || echo "⚠️ Stage 2 failed, continuing..."
cd "$BASE_DIR"
echo -e "⭐️ Completed Stage 2\n=========================================="

# ----------------------------------------
# Stage 3: Train/Dev/Test Split Generation
# ----------------------------------------
echo -e "\n📦 Stage 3: Generating Data Splits"
cd 3_splitting && bash complete_split_files.sh || echo "⚠️ Stage 3 failed, continuing..."
cd "$BASE_DIR"
echo -e "⭐️ Completed Stage 3\n=========================================="

# ----------------------------------------
# Stage 4: Random Sampling from Final Splits (Optional)
# ----------------------------------------
echo -e "\n🎲 Stage 4: Sampling from Final Splits"
cd 4_sampling && bash sample_n_data.sh || echo "⚠️ Stage 4 (sampling) failed, continuing..."
cd "$BASE_DIR"
echo -e "⭐️ Completed Stage 4\n=========================================="

# ----------------------------------------
# Stage 5: Add Negative Samples to Training Set
# ----------------------------------------
echo -e "\n➕ Stage 5: Adding Negative Samples"
cd 5_train_negative_sampling && bash add_neg_samples.sh || echo "⚠️ Stage 5 (negative sampling) failed, continuing..."
cd "$BASE_DIR"
echo -e "⭐️ Completed Stage 5\n=========================================="

# ----------------------------------------
# Stage 6: Dev/Test Enumeration for Evaluation
# ----------------------------------------
echo -e "\n🧪 Stage 6: Dev/Test Sample Enumeration"
cd 6_test_dev_enumeration && bash test_enumeration.sh || echo "⚠️ Stage 6 (enumeration) failed, continuing..."
cd "$BASE_DIR"
echo -e "⭐️ Completed Stage 6\n=========================================="

echo -e "\n🏁 ✅ Pipeline Finished: All Stages Executed (Check logs above for any errors)"
