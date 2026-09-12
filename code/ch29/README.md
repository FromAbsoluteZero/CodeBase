# Chapter 29 — Interpretability

Companion code for Chapter 29 of *From Absolute Zero*.

## What is here

| File | What it is |
|---|---|
| `_lib.py` | shared setup: puts the data file in place (the blocks carry their own imports) |
| `c1.py` | `import numpy as np, pandas as pd` |
| `c2.py` | `imp = pd.Series(rf.feature_importances_,` |
| `c3.py` | `from sklearn.inspection import permutation_importance` |
| `c4.py` | `from sklearn.inspection import partial_dependence` |
| `c5.py` | `import shap` |
| `c6.py` | `import shap` |
| `figs.py` | regenerates `fig29_1.png`, `fig29_2.png` |

**6 printed blocks** (`c1.py` … `c6.py`), in the order the book prints them.

## Running it

The blocks are fragments of **one continuing session**, exactly as the book presents them: later
blocks use variables defined by earlier ones, so they are not standalone scripts. `_lib.py` only
puts the data file in place. Run them in order, from this directory:

```bash
python -c "for f in ['_lib.py', 'c1.py', 'c2.py', 'c3.py', 'c4.py', 'c5.py', 'c6.py']: exec(open(f, encoding='utf-8').read())"
```

To stop after a particular block, shorten the list. Each block's output appears in the order the
book prints it.

## Data

`hr.csv` is created by Chapter 14 (`code/ch14/gen_hr.py`). The blocks read it from the working
directory, as the book does. `_lib.py` uses the local file if you have generated one, otherwise
the byte-identical copy shipped in `data/generated/hr.csv`. Full provenance: `DATA_MANIFEST.csv`.

## Figures

```bash
python figs.py
```

Writes `fig29_1.png`, `fig29_2.png` into this directory (the shipped versions are in `figures/`).

## Requirements

This chapter needs `shap`, which is in `requirements-optional.txt`.

## Reproducibility

Every block is explicitly seeded. At the versions pinned in `requirements.txt` the output
should match the book digit for digit.
See `docs/REPRODUCIBILITY.md` if a number does not match.
