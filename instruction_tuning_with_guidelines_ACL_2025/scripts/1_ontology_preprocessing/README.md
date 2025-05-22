# Ontology Preprocessing

We extract event schemas from datasets and convert them into standardized Python-style class hierarchies. These definitions are used later for instruction tuning and evaluation.

---

## Unified Ontology Preprocessing Pipeline

For a seamless experience, run all ontology preprocessing and consolidation steps with:

```bash
sh complete_ontology_pipeline.sh
```

This unified script:
- Iterates over all datasets (defined within the script)
- Generates per-dataset ontology files (event types, argument roles, class definitions)
- Merges all class definitions into a master Python dataclass file

---

## Pipeline Structure

The unified script internally performs two stages:

### Stage 1: Dataset-wise Ontology Preprocessing
For each dataset, this step:
- Extracts schemas and argument role definitions from splits (`train.json`, `dev.json`, `test.json`)
- Converts the schema into Python-style @dataclass structures
- Generates:

| File Name                                     | Description                                                                 |
|----------------------------------------------|-----------------------------------------------------------------------------|
| `Master_event_types_<dataset>.json`          | List of all canonical event types for the dataset                          |
| `Master_event_dataclasses_<dataset>.json`    | Attributes (argument roles) for each event, with placeholder descriptions  |
| `Dataclass_<dataset>.py`                     | Python-style @dataclass definitions for each event                         |
| `Dataclass_events_<dataset>.json`            | Structural hierarchy in JSON format (equivalent to the Python version)     |
| `Event_mapper_<dataset>.json`                | Maps raw event names to code-friendly class names                          |

---

### 🔧 Stage 2: Consolidating All Dataclasses

Once individual dataset schemas are extracted, we merge all event definitions into:

| File Name                        | Description                                                            |
|----------------------------------|------------------------------------------------------------------------|
| `Master_dataclass.py`           | Unified Python file containing all event class definitions across datasets |
  
This file is essential for:
- Creating class-based input/output structures
- Enabling evaluation using `eval(result == predicted_result)` style logic

---

## ⚙️ Alternatively: Run Steps Manually

If you'd like more granular control:

### Step 1: Extract ontology for each dataset
```bash
sh ontology_preprocessing.sh
```

### Step 2: Merge dataclass definitions into one master file
```bash
sh consolidate_dataclasses.sh
```

---

## Supported Datasets

The code is compatible with any dataset following the **TextEE format**, where each instance includes `event_mentions`.

You can modify the dataset list in the scripts to extend or limit what is processed.

---

## 📂 Output Directory Structure

```
data/extracted_ontology/<dataset>/
├── Master_event_types_<dataset>.json          # List of standardized event types
├── Master_event_dataclasses_<dataset>.json    # Attribute definitions with roles
├── Dataclass_<dataset>.py                     # Python @dataclass structure per event type
├── Dataclass_events_<dataset>.json            # JSON format of the dataclass hierarchy
├── Event_mapper_<dataset>.json                # Maps original event names to Pythonic class names
```

Final merged output:
```
data/extracted_ontology/Master_dataclass.py    # Unified Python file combining all dataclass definitions
```

---

## Use in Evaluation

The `Master_dataclass.py` file is used to:
- Parse structured model predictions
- Instantiate predictions using Python classes
- Evaluate predictions consistently across datasets and guidelines

---

## 📬 Contact

For help or questions, reach out to the authors.
