# Test/Dev Event Type Enumeration

This module performs **event type enumeration** for `test` and `dev` splits across datasets and guideline variants by **inserting missing event types as negative samples** (empty results).

---

## Overview

The goal is to ensure that every instance (grouped by `wnd_id`) **includes all event types** from the dataset's ontology. This is done by:

- Identifying missing event types for each `wnd_id`
- Inserting structurally valid but empty examples for these types
- Using optional **guideline-based class descriptions**, or structural-only for `No_guideline`

---

## Folder Structure

```
code_converted_data/
└── <guideline>/
    └── <dataset>/
        ├── final_data_split/
        │   └── split*/ 
        │       ├── test.json
        │       ├── dev.json
        │       ├── test_enumerated.json
        │       └── dev_enumerated.json
        └── ont_preproc/
            └── Master_event_types_<dataset>.json
    No_guideline/
        └── guidelines_merged_across_datasets.json  # Used for class info in enumeration or you can pass the guideline file path from any one guideline setting.
```

---

## How to Run

Run the enumeration pipeline using:

```bash
bash test_enumeration.sh
```

This script will:
1. Process all `test`/`dev` files across splits
2. Enumerate missing event types as new (empty) examples
3. Save results into `_enumerated.json` files

---

## ⚙️ Configuration

All options are configured in `test_enumeration.sh`:

| Variable              | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| `DATA_ROOT`           | Root path to processed data                                                 |
| `DATASETS`            | Datasets to enumerate (e.g., `ace05-en`, `richere-en`)                      |
| `GUIDELINE_MODELS`    | All guideline variants including `No_guideline`                             |
| `SPLITS`              | List of split folders (`split1`, `split2`, ...)                             |
| `IS_RANDOM`           | Whether to randomly pick descriptions when multiple are provided            |
| `PYTHON_SCRIPT`       | Python script for actual enumeration logic (`test_enumeration.py`)          |

---

## Enumeration Logic

- For each file:
  - Group instances by `wnd_id`
  - Identify event types **already present** for that group
  - Insert one synthetic example per **missing event type**
  - Use:
    - Guideline descriptions (if available and not `No_guideline`)
    - Structural-only definitions (for `No_guideline` mode)

- Output JSONs are extended versions of original files with added negative samples

---

## Requirements

Ensure the following files are present before running:

| File | Path |
|------|------|
| Master event types | `ont_preproc/Master_event_types_<dataset>.json` |
| Guideline JSONs | `data/synthesized_guidelines/<dataset>/<guideline>.json` |
| No_guideline fallback | `code_converted_data/No_guideline/guidelines_merged_across_datasets.json` or you can pass the guideline file path from any one guideline setting. |

---

## Output Example

If you run on `split1` for `ace05-en`, you'll get:

- Original:  
  ```
  final_data_split/split1/test.json
  final_data_split/split1/dev.json
  ```

- Enumerated Output:
  ```
  final_data_split/split1/test_enumerated.json
  final_data_split/split1/dev_enumerated.json
  ```

Each file contains:
- All original examples
- One new example for each missing event type per `wnd_id`, with `output: []`

---

## Notes

- Safely skips files not containing `test` or `dev` in filename
- Reuses max `instance_id` to extend new examples
- Gracefully skips processing if any input file is missing
- Supports full control over guidelines, datasets, and splits

---

## 📬 Contact

For feedback or contributions, feel free to reach out to the authors.