# Chapter 14 — Classification and Logistic Regression

Companion code for Chapter 14 of *From Absolute Zero*.

## What is here

| File | What it is |
|---|---|
| `gen_hr.py` | the printed block that creates `hr.csv` |
| `_lib.py` | shared setup: puts the data file in place (the blocks carry their own imports) |
| `c1.py` | `import numpy as np` |
| `c2.py` | `import pandas as pd` |
| `c3.py` | `from sklearn.metrics import confusion_matrix, accuracy_score` |
| `c4.py` | `print(f"{'thresh':>7}{'flagged':>9}{'TP':>5}{'FP':>5}{'FN':>5}"` |
| `c5.py` | `from sklearn.metrics import roc_auc_score, average_precision_score` |
| `c6.py` | `bal = LogisticRegression(max_iter=1000,` |
| `c7.py` | `import numpy as np` |
| `c8.py` | `hr = pd.read_csv("hr.csv")` |
| `c9.py` | `call_cost = 400` |
| `c10.py` | `rows = []` |
| `c11.py` | `budget = 60` |
| `c12.py` | `print(f"1. Calling the 60 highest-scoring employees finds "` |

**12 printed blocks** (`c1.py` … `c12.py`), in the order the book prints them.

## Running it

The blocks are fragments of **one continuing session**, exactly as the book presents them: later
blocks use variables defined by earlier ones, so they are not standalone scripts. `_lib.py` only
puts the data file in place. Run them in order, from this directory:

```bash
python -c "for f in ['gen_hr.py', '_lib.py', 'c1.py', 'c2.py', 'c3.py', 'c4.py', 'c5.py', 'c6.py', 'c7.py', 'c8.py', 'c9.py', 'c10.py', 'c11.py', 'c12.py']: exec(open(f, encoding='utf-8').read())"
```

To stop after a particular block, shorten the list. Each block's output appears in the order the
book prints it.

## Data

`hr.csv` is created by this chapter's first block, `gen_hr.py`, which the command above runs first.
A byte-identical copy ships in `data/generated/hr.csv`; `_lib.py` falls back to it if the file is
not in this directory.

## Reproducibility

Every block is explicitly seeded. At the versions pinned in `requirements.txt` the output
should match the book digit for digit.
See `docs/REPRODUCIBILITY.md` if a number does not match.
