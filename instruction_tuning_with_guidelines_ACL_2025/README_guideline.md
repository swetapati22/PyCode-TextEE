# Guideline Generation

We provides scripts to automatically generate **annotation guidelines** for each event type using GPT-4.

We support the following prompt variants for guideline generation:
- `Guideline-P`: Uses positive examples only.
- `Guideline-PN`: Uses both positive and negative examples.
- `Guideline-PS`: Uses positive examples and sibling event types.
- `Guideline-PN-Int`: Consolidated integrated version of Guideline-PN.
- `Guideline-PS-Int`: Consolidated integrated version of Guideline-PS.

---

## ⚡ How to Run

To generate guidelines for a dataset:

```bash
python scripts/guidelines/generate_guidelines.py --dataset ACE05
```

---

## 📁 Input

- Preprocessed event examples from `data/` folder (in TextEE format).
- Requires access to GPT-4 via OpenAI API (ensure keys are set up).

---

## 📄 Output

- JSON files with 5 distinct guidelines per event type.
- Saved to `data/guidelines/{dataset}/`.

---

## 📚 More

These guidelines are automatically integrated into the training prompt during instruction-tuning.
