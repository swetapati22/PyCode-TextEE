# Instruction-Tuning LLMs for Event Extraction with Annotation Guidelines

**Authors**: [Saurabh Srivastava](mailto:ssrivas6@gmu.edu), [Sweta Pati](mailto:spati@gmu.edu), [Ziyu Yao](mailto:ziyuyao@gmu.edu)  
**Institution**: George Mason University

---

## Introduction
📄 Our paper Instruction-Tuning LLMs for Event Extraction with Annotation Guidelines provides a framework for exploring how annotation guidelines can improve instruction-tuned large language models (LLMs) for event extraction (EE).

- Integrates annotation guidelines (both human and machine-generated) into instruction-tuning.
- Supports **datasets** preprocessed in TextEE's natural language format.
- Provides standardized scripts to convert natural language examples into structured Python code prompts.
- Formats both the **input prompt** and the **model’s expected output** as structured Python code.
- Enables automatic guideline generation via GPT-based prompt templates.
- Improves performance in low-resource and cross-schema generalization settings.

For more details, please refer to our paper:  
[Instruction-Tuning LLMs for Event Extraction with Annotation Guidelines](https://arxiv.org/abs/2502.16377).

---

## 🗂️ Repository Structure

```
.
├── data/               # ACE05 and RichERE datasets (processed format)
├── scripts/            # Preprocessing, training, evaluation, and generation
│   ├── preprocessing/
│   ├── training/
│   ├── evaluation/
│   └── generate_guidelines/
├── models/             # LLaMA checkpoints and config files
├── prompts/            # Prompt templates for generating guidelines
├── results/            # Logs, figures, evaluation outputs
├── notebooks/          # Optional: Exploratory notebooks
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Datasets

We use two widely-used event extraction datasets:

| Dataset   | Event Types | Role Types | Instances (train/dev/test) |
|-----------|-------------|-------------|-----------------------------|
| ACE05     | 33          | 22          | 16,531 / 1,870 / 2,519      |
| RichERE   | 38          | 35          | 9,105 / 973 / 1,163         |

We follow the [TextEE](https://arxiv.org/abs/2311.09562) preprocessing pipeline and provide scripts to convert these preprocessed datasets from TextEE’s natural language format into structured Python code prompts.

To convert your data:
1. Place the preprocessed TextEE-style datasets under the `data/` directory.
2. Follow the detailed steps in [`data/README.md`](data/README.md).

⚠️ Note: Access to ACE05 and RichERE requires a license from the [LDC](https://www.ldc.upenn.edu/). We do not redistribute these datasets.

- ACE05 ([Link to ACE05 Dataset](https://catalog.ldc.upenn.edu/LDC2006T06))
- RichERE ([Link to RichERE Dataset](https://catalog.ldc.upenn.edu/LDC2023T04))

---

### ⚡ Guideline Generation

To generate machine-generated annotation guidelines:

```bash
python scripts/guidelines/generate_guidelines.py --dataset ACE05
```

We support multiple prompt variants: `Guideline-P`, `Guideline-PN`, `Guideline-PS`, and their integrated forms. These guidelines are generated using GPT-4 based on positive and negative event examples.

For guideline generation, see [`scripts/guidelines/README.md`](scripts/guidelines/README.md).

---

## 💡 Models

| Model Variant          | Description                                    |
|------------------------|------------------------------------------------|
| `LLaMA-3.1-8B-Instruct` | Main model used for instruction tuning        |
| `LLaMA-3.2-1B-Instruct` | Smaller variant used for generalization study |

We use Unsloth + rsLoRA for efficient fine-tuning. Check `scripts/training` for configs.

---

## ⚙️ Environment

We recommend using Conda + pip.

```bash
conda create -n llama-events python=3.10
conda activate llama-events
pip install -r requirements.txt
```

Also run:

```bash
python -m spacy download en_core_web_lg
```

---

## 🚀 Running

### 🏋️ Training

```bash
python scripts/training/train.py --config configs/ace05.json
```

### 📊 Evaluation

```bash
python scripts/evaluation/eval.py --model_checkpoint path/to/checkpoint.pt
```


## 📈 Results

Check our full results and analysis in the [paper](https://arxiv.org/abs/2502.16377).  

---

## 🧾 Citation

If you find this work useful for your own research please cite our paper:

```bibtex
@misc{srivastava2025instruction,
  title={Instruction-Tuning LLMs for Event Extraction with Annotation Guidelines},
  author={Saurabh Srivastava and Sweta Pati and Ziyu Yao},
  year={2025},
  eprint={2502.16377},
  archivePrefix={arXiv},
  primaryClass={cs.CL}
}
```

---

## 📬 Contact

For questions or contributions:
- Email: ssrivas6@gmu.edu | spati@gmu.edu | ziyuyao@gmu.edu
- GitHub Issues: Open one!

---

## 📜 License

This project is licensed under the MIT License.
