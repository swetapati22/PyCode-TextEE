# Sampling n Examples Subsets from Final Instruction Data

This module handles **sampling N instruction-formatted instances** from the final `train`, `dev`, and `test` files — with full event-type coverage — across all datasets and guideline variants.

---

## ✅ Overview

We perform sampling **only once** using a `reference_guideline` (e.g., `No_guideline`) and reuse the instance IDs for all other guidelines. This ensures consistency across variant comparisons.

The sampling ensures:
- **Dynamic coverage across as many event types as possible**
- Balanced inclusion of null-type (no event) examples
- **Proportional sampling**: a certain percentage of samples from null events, and the rest from various event types

---

## 🧱 Folder Structure

```
code_converted_data/
└── <guideline>/
    └── <dataset>/
        ├── final_data_split/
        │   └── split*/ 
        │       ├── train.json
        │       ├── dev.json
        │       ├── test.json
        │       ├── train_<N>_sampled.json
        │       └── ...
        └── sampled_ids/
            └── split*/
                ├── train_<N>_sampled_ids.txt
                ├── dev_<N>_sampled_ids.txt
                └── test_<N>_sampled_ids.txt
```

---

## 🛠 How to Run

Run the sampling pipeline using:

```bash
bash sample_n_data.sh 
```

This script will:
1. Sample `N` instances from each of `train`, `dev`, and `test` using the `reference_guideline`.
2. Save instance IDs to `sampled_ids/`.
3. Reuse these IDs across **all other guideline variants** to ensure consistent evaluation.

---

## ⚙️ Configuration

All options are configured in `sample_n_data.sh`:

| Variable              | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| `DATA_ROOT`           | Root directory for `code_converted_data/`                                   |
| `DATASETS`            | List of datasets to process                                                 |
| `GUIDELINES`          | All guideline folders to sample against                                     |
| `REFERENCE_GUIDELINE` | The only guideline used to generate instance IDs                            |
| `SAMPLE_SIZES`        | List of values for `N` (e.g., `100`, `2000`)                                |
| `SPLIT_FOLDERS`       | Support for multiple splits (`split1`, ..., `split5`)                       |
| `NULL_EVENT_PERCENT`  | Percentage of samples to pull from null-type (non-event) examples           |

---

## 🧪 Sampling Logic

- Extracts event types from:
  ```
  ont_preproc/Master_event_types_<dataset>.json
  ```
- Divides the total `N` samples as:
  - `<null_event_percent>` from examples without any event
  - Remainder is **evenly split** across all known event types
- Dynamically calculates how many samples to draw from each category
- If fewer valid examples are available, adjusts without crashing

---

## 📋 Requirements

Make sure the following files exist **under your `reference_guideline` folder**:

- Instruction-formatted split data:
  ```
  final_data_split/split*/train.json, dev.json, test.json
  ```
- Event type definitions:
  ```
  ont_preproc/Master_event_types_<dataset>.json
  ```

---

## 💡 Example Output

If you run sampling for `ace05-en`, `split1`, with 100 samples:

- Sampled ID files:
  ```
  code_converted_data/No_guideline/ace05-en/sampled_ids/split1/train_100_sampled_ids.txt
  code_converted_data/No_guideline/ace05-en/sampled_ids/split1/dev_100_sampled_ids.txt
  ...
  ```

- Sampled JSONs across all guidelines:
  ```
  code_converted_data/<guideline>/ace05-en/final_data_split/split1/train_100_sampled.json
  code_converted_data/<guideline>/ace05-en/final_data_split/split1/dev_100_sampled.json
  ...
  ```

---

## 🧼 Notes

- If any file is missing, the script prints a warning and skips gracefully
- Consistency is maintained by reusing IDs across all guidelines
- Supports multiple datasets, guidelines, splits, and sample sizes

---

## 📬 Contact

For any questions or improvements, please contact the authors.
