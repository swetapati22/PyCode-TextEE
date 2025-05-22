# Instruction Data Preprocessing Pipeline

This is the **master guide** for the end-to-end data preprocessing pipeline.

This pipeline converts **TextEE-style natural language event data** into **Structured Python code prompts** with optional annotation guidelines, in **instruction-style input-output pairs** ready for LLM training or evaluation.

Each stage of the pipeline builds upon the previous one, ensuring consistency, structure, and schema-awareness across datasets and guideline variants.

---

# 🧩 End-to-End Workflow Overview

The recommended way to run the entire preprocessing pipeline is via the **data_processing_pipeline script** provided in scripts folder. 

## 🔄 Pipeline Stages

The complete pipeline is divided into **6 sequential modules**, each in its dedicated folder. You can run them end-to-end or invoke them individually by refering the section specific README files within each directory.

### 1️⃣ `1_ontology_preprocessing`
- Extracts event types, roles, and schemas from raw datasets.
- Converts to Python-style dataclasses.
- Merges schemas into a master definition.
- 📄 Details: `scripts/1_ontology_preprocessing/README.md`

### 2️⃣ `2_instruction_formating`
- Converts schema and examples into instruction-formatted inputs and outputs.
- Supports various guideline settings and no-guideline formats.
- 📄 Details: `scripts/2_instruction_formating/README.md`

### 3️⃣ `3_splitting`
- Splits instruction-formatted data into 5 folds (`split1` to `split5`) as given by TextEE.
- Ensures consistency across guideline variants.
- 📄 Details: `scripts/3_splitting/README.md`

### 4️⃣ `4_sampling`
- Samples N examples for `train`, `dev`, and `test` with broad event-type coverage.
- Maintains null-event proportion.
- Maintains same sample IDs across to all variants.
- 📄 Details: `scripts/4_sampling/README.md`

### 5️⃣ `5_train_negative_sampling`
- Augments `train` split with negative samples (no-event examples).
- Event-type aware random sampling.
- 📄 Details: `scripts/5_train_negative_sampling/README.md`

### 6️⃣ `6_test_dev_enumeration`
- Adds event-type enumeration instances to `test` and `dev`.
- Ensures full coverage of event types for each datasets in `test` and `dev`.
- 📄 Details: `scripts/6_test_dev_enumeration/README.md`

---

## Requirements

Before running any script, ensure:
- Your datasets are formatted in standard **TextEE-style** JSON
- All paths are correctly set in your `*.sh` scripts
- Python dependencies are installed (`tqdm`, `argparse`, etc.)

---

## How to Use

We recommend executing each stage in order:

```bash
# Step-by-step (modify script if needed)
bash 1_ontology_preprocessing/ontology_unified.sh
bash 2_instruction_formating/format_instructions.sh
bash 3_splitting/split_across_guidelines.sh
bash 4_sampling/sample_n_data.sh
bash 5_train_negative_sampling/train_negative_sampling.sh
bash 6_test_dev_enumeration/enumerate_test_dev.sh
```

Alternatively, we the master script if full automation is desired.


---

## 📦 Output Folders

Each script operates inside the `data/` directory and writes to corresponding folders:

```
data/
├── processed_data/                 # Original splits
├── extracted_ontology/            # Ontology JSONs & class definitions
├── code_converted_data/           # Instruction-format data
├── synthesized_guidelines/        # Generated guideline texts (if used)
```

---


## Notes

- All consolidated `.sh` files are customizable — modify dataset names or paths inside each as needed
- Each stage is modular and can be run independently if needed
- If any dataset fails in a batch run, it will print a warning but continue with others

---

## 📬 Contact

For issues, contributions, or questions, please contact the authors.
