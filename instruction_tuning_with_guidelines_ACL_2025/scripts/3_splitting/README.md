# Data Splitting Pipeline

This stage of the pipeline takes the **instruction-formatted dataset** and prepares it into standard **train/dev/test splits** based on the splits described by TextEE, enabling effective training and evaluation of LLMs on event extraction.

---

## ✅ Pipeline Overview

The splitting process involves two major stages:

1. **Generate instance-level split files** using `doc_id` or `wnd_id` references.
2. **Filter the full dataset** to construct final train/dev/test datasets using those IDs.

---

## 🚀 Running the Full Pipeline

To run the entire split generation process end-to-end:

```bash
bash run_all_split_generation.sh
```

This executes:
- `generate_split_ids.sh` → Creates ID-based split files.
- `split_final.sh` → Filters the master file into final `train.json`, `dev.json`, and `test.json`.

---

## Supported Datasets

All datasets that follow the TextEE-style structure with fields like `doc_id`, `wnd_id`, and `instance_id` are supported.

| Dataset        | Split by `wnd_id` |
|----------------|-------------------|
| ace05-en       | No                |
| richere-en     | No                |
| geneva         | ✅ Yes            |
| Others         | No                |

---

## 📜 Guideline Variants

The splitting pipeline works for **all guideline formats** used in earlier preprocessing steps:

| Guideline Variant | Description                                   |
|--------------------|-----------------------------------------------|
| `No_guideline`     | No guideline attached (baseline)              |
| `guideline_H`      | Human-written guidelines                      |
| `guideline_P`      | Positive LLM-generated examples               |
| `guideline_PN`     | Positive + Negative examples                  |
| `guideline_PS`     | Positive + Sibling-type examples              |
| `guideline_PN_INT` | Integrated version from PN variants           |
| `guideline_PS_INT` | Integrated version from PS variants           |

---

## 📂 Step-by-Step Outputs

### 1️⃣ Generate Split IDs  
Run: `generate_split_ids.sh`

This script produces instance ID files per split based on `train.txt`, `dev.txt`, and `test.txt` from the original preprocessing.

📁 **Example Output:**
```
data/code_converted_data/guideline_P/ace05-en/splits_ids/split1/train.json
```

Each file contains:
```json
["ace05-en_0", "ace05-en_1", "ace05-en_2", ...]
```

---

### 2️⃣ Filter Final Input-Output Data  
Run: `split_final.sh`

This filters the `Final_input_output_data_<dataset>.json` file using the split IDs created above.

📁 **Example Output:**
```
data/code_converted_data/guideline_P/ace05-en/final_data_split/split1/train.json
```

Each split file contains **full examples** in instruction format:
```json
{
  "doc_id": "...",
  "instruction": "...",
  "input": "...",
  "output": [...]
}
```

---

## Running Step-by-Step

You can also run scripts independently:

### Step 1: Generate Split IDs
```bash
bash generate_split_ids.sh
```

### Step 2: Create Final Split Files
```bash
bash split_final.sh
```

---

## 📂 Directory Structure

Each dataset and guideline variant will have the following layout:

```
data/code_converted_data/<guideline>/<dataset>/
Final_input_output_data_<dataset>.json
    splits_ids/
    └️ split1/
        ├️ train.json     # instance_ids
        ├️ dev.json
        └️ test.json
    final_data_split/
    └️ split1/
        ├️ train.json
        ├️ dev.json
        └️ test.json
```

---

## Script Summary

| Script                  | Description                                          |
|-------------------------|------------------------------------------------------|
| `generate_split_ids.sh` | Creates instance ID lists for train/dev/test splits  |
| `split_final.sh`        | Filters final instruction-formatted dataset          |
| `run_all_split_generation.sh` | Combines both steps into one end-to-end process |

---

## Notes

- `split_by_wnd_id` is used for datasets like `geneva`.
- If files are missing (e.g., guideline not present), the scripts gracefully skip.
- Supports multiple `split folders`: `split1`, `split2`, ..., `split5`.

---

## 📬 Contact

For help or questions, reach out to the authors.