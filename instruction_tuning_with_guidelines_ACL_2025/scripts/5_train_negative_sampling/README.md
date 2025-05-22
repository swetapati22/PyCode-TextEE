# Negative Sampling with and without Guidelines

This utility enables the automated addition of **negative event-type examples** to training data across different datasets and guideline configurations, including **synthetic**, **human-authored**, and **no-guideline** settings.

---

## 📁 Directory Structure

```
IT_LLaMA/
├── data/
│   ├── code_converted_data/
│   ├── synthesized_guidelines/
│   │   ├── ace05-en/
│   │   ├── richere-en/
│   │   └── guidelines_merged_across_datasets.json  # Used for No_guideline
├── scripts/
│   └── negative_sampling/
│       ├── add_neg_samples.py     # Main Python script
│       └── add_neg_samples.sh     # Runner script
```

---

## 🚀 How It Works

### 1. `add_neg_samples.sh`

This script:
- Iterates over all guidelines and datasets.
- For each split folder (e.g., `split1`, `split2`, etc.):
  - Identifies eligible train files.
  - Calls the Python script to append negative examples.

Supports both:
- **Descriptive guidelines** (e.g., `guideline_H`, `guideline_P`)
- **No_guideline** structural format

### 2. `add_neg_samples.py`

This script:
- Loads the training instances.
- For each `wnd_id`, identifies unused event types.
- Creates a new `@dataclass` (either structural or with docstrings).
- Injects negative examples with empty output (`[]`).

Handles:
- Guidelines as **lists or strings**.
- Attributes as **lists or strings**.
- Optional `--is_random` to shuffle which descriptions to use.
- Structured-only fallback for `--no_guideline` mode.

---

## ⚙️ Command-Line Usage

You don't have to run this directly unless debugging. But for reference:

```bash
python add_neg_samples.py \
  --test_file path/to/train.json \
  --master_event_file path/to/Master_event_types.json \
  --ace_master_file path/to/guidelines.json \
  --output_file path/to/output.json \
  --num_instances 15 \
  --is_random True \
  [--no_guideline]  # Only for No_guideline setting
```

---

## 🧪 Output Format

Appends new entries to the original training data:
- Preserves original instances
- Adds `N` new instances (per `wnd_id`) with unused event types
- Each negative instance:
  - Replaces the `@dataclass` with a new class
  - Sets `output: []`
  - Adds explanation: _"No event mentions...result should be empty."_

---

## ✅ Edge Case Coverage

- [x] Multiple guideline types
- [x] No_guideline mode
- [x] Random/non-random guideline descriptions
- [x] Split folder traversal
- [x] Skips pre-processed files (`_w_neg_*.json`)
- [x] Graceful fallbacks for missing files

---

## 📌 Customization

Update the following in `add_neg_samples.sh` to control processing:

```bash
DATASETS=("ace05-en" "richere-en")
GUIDELINES=("No_guideline" "guideline_H" "guideline_P" ...)
SPLIT_FOLDERS=("split1" "split2" ...)
NUM_NEGATIVE_INSTANCES=15
```

---

## 🎉 That's It

Run the shell script and you're good to go:

```bash
sh add_neg_samples.sh
```

Your output will be saved alongside the original training files with `_w_neg_15.json` suffix.