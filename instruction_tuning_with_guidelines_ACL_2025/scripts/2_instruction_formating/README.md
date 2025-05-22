# Data Preparation Pipeline

Providing a complete pipeline to preprocess, format to Python-style code prompts, and prepare datasets for instruction-tuning large language models (LLMs) for **event extraction** tasks.

---

## Pipeline Overview

This pipeline converts **TextEE-style natural language event data** into:
1. **Structured Python code prompts** with optional annotation guidelines.
2. **Final complete data in instruction-style input-output pairs** ready for LLM training or evaluation.

---

## Running the Full Pipeline

To run the entire process end-to-end:

```bash
sh complete_instruction_formating_pipeline.sh
```

This executes:
- `data_preprocessing.sh` → Converts raw data into Python code format.
- `model_input_output_format.sh` → Converts code format into LLM instruction prompts.

This gives us the complete data for a particular dataset in the LLM instruction prompts format in a single file.

---

## 🧩 Supported Datasets

The following datasets are supported and mapped to the appropriate task type:

| Dataset        | Task Type |
|----------------|-----------|
| ace05-en       | E2E       |
| richere-en     | E2E       |
| mlee           | E2E       |
| genia2011      | E2E       |
| genia2013      | E2E       |
| m2e2           | E2E       |
| casie          | E2E       |
| phee           | E2E       |
| maven          | ED        |
| fewevent       | ED        |
| speed          | ED        |
| mee            | ED        |
| wikievents     | EAE       |
| rams           | EAE       |
| muc4           | EAE       |
| geneva         | EAE       |

- Any other datasets that are pre-processed in TextEE format can use our scripts to convert **natural language event data** into **structured python code prompts**.
---

## 🧾 Guideline Settings

Guidelines help LLMs understand what to extract. This repo supports:

| Variant            | Description                                                               |
|--------------------|---------------------------------------------------------------------------|
| `No_guideline`     | No guidelines (baseline)        
| `guideline_H`      | Human-annotated guidelines from dataset authors                          |
| `guideline_P`      | LLM-generated with 10 positive examples                                  |
| `guideline_PN`     | Positive + 15 negative examples                                           |
| `guideline_PS`     | Positive + 15 sibling-type examples                                       |
| `guideline_PN_INT` | Integrated from multiple PN variants                                      |
| `guideline_PS_INT` | Integrated from multiple PS variants                                      |                                          |

Guidelines present in the `data/synthesized_guidelines` folder are used for this data preprocessing task.

---

## 📂 Step-by-Step Outputs

### 1️⃣ Raw → Code-Formatted Prompts

Run: `data_preprocessing.sh`

**Example Output File:**
```
data/code_converted_data/guideline_P/ace05-en/preproc_script/Master_data_ace05-en.json
```

Format:
```python
# The following lines describe the task definition
@dataclass
class LifeDie(Event):
    mention: str
    Victim: List
    Place: List

# This is the text to analyze
text = "At least 19 people were killed in a blast..."

result =
```

---

### 2️⃣ Code Prompts → Instruction Format

Run: `model_input_output_format.sh`

**Example Output File:**
```
data/code_converted_data/guideline_P/ace05-en/Final_input_output_data_ace05-en.json
```

Each entry looks like:

```json
{
  "doc_id": "...",
  "task_type": "E2E",
  "instruction": "# This is an event extraction task...",
  "input": "# The following lines describe the task definition...",
  "output": "[LifeDie(mention="killed", Victim=[...], Place=[...])]"
}
```

---

## Running Step-by-Step

You can run each script individually as well:

### Step 1: Preprocessing (TextEE → Code)
```bash
sh data_preprocessing.sh
```

### Step 2: Instruction Input/Output Formatting
```bash
sh model_input_output_format.sh
```

This gives us the complete data for a particular dataset in the LLM instruction prompts format in a single file.
---

## What’s Next?

Next, you can split the instruction-formatted data into:
- Train
- Validation
- Test

(Coming up next in the pipeline)

---

## 📬 Contact

For help or questions, reach out to the authors.
