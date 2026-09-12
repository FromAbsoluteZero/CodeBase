# Chapter 23 — Imbalance, Thresholds, Cost-Sensitive Decisions

Companion code for Chapter 23 of *From Absolute Zero*.

## What is here

| File | What it is |
|---|---|
| `_lib.py` | shared setup: the imports and objects the printed blocks assume, which the book shows once at the start of the session |
| `c1.py` | `# The break-even threshold falls straight out of the two costs.` |
| `c2.py` | `p_star = C_FP / (C_FP + C_FN)` |
| `c3.py` | `from imblearn.over_sampling import SMOTE` |
| `c4.py` | `# Does the theoretical p* actually minimize cost on held-out data?` |
| `c5.py` | `# Cost is not the only constraint. Capacity usually binds first.` |
| `figs.py` | regenerates `fig23_1.png` |

**5 printed blocks** (`c1.py` … `c5.py`), in the order the book prints them.

## Running it

The blocks are fragments of **one continuing session**, exactly as the book presents them: later
blocks use variables defined by earlier ones, and the imports and shared objects live in
`_lib.py`. They are not standalone scripts — `python c1.py` on its own stops with a `NameError`.
Run them in order, from this directory:

```bash
python -c "for f in ['_lib.py', 'c1.py', 'c2.py', 'c3.py', 'c4.py', 'c5.py']: exec(open(f, encoding='utf-8').read())"
```

To stop after a particular block, shorten the list. Each block's output appears in the order the
book prints it.

## Data

`transactions.csv` is created by Chapter 22 (`code/ch22/gen_tx.py`). The blocks read it from the working
directory, as the book does. `_lib.py` uses the local file if you have generated one, otherwise
the byte-identical copy shipped in `data/generated/transactions.csv`. Full provenance: `DATA_MANIFEST.csv`.

## Figures

```bash
python figs.py
```

Writes `fig23_1.png` into this directory (the shipped versions are in `figures/`).

## Requirements

This chapter needs `imbalanced-learn`, which is in `requirements-optional.txt`.

## Reproducibility

Every block is explicitly seeded. At the versions pinned in `requirements.txt` the output
should match the book digit for digit.
See `docs/REPRODUCIBILITY.md` if a number does not match.
