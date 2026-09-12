# Chapter 22 — Classification Metrics

Companion code for Chapter 22 of *From Absolute Zero*.

## What is here

| File | What it is |
|---|---|
| `gen_tx.py` | the printed block that creates `transactions.csv` |
| `_lib.py` | shared setup: the imports and objects the printed blocks assume, which the book shows once at the start of the session |
| `c1.py` | `m = make_pipeline(StandardScaler(),` |
| `c2.py` | `# Precision at fixed capacity: the metric an operations team actually has.` |
| `c3.py` | `# ROC and PR describe the same model and disagree about how good it is.` |
| `c4.py` | `# A score that ranks well need not be a probability you can trust.` |
| `c5.py` | `# For this linear model, class weighting barely` |
| `c6.py` | `# The threshold is a business decision. Price both errors and sweep.` |
| `figs.py` | regenerates `fig22_1.png`, `fig22_2.png` |

**6 printed blocks** (`c1.py` … `c6.py`), in the order the book prints them.

## Running it

The blocks are fragments of **one continuing session**, exactly as the book presents them: later
blocks use variables defined by earlier ones, and the imports and shared objects live in
`_lib.py`. They are not standalone scripts — `python c1.py` on its own stops with a `NameError`.
Run them in order, from this directory:

```bash
python -c "for f in ['gen_tx.py', '_lib.py', 'c1.py', 'c2.py', 'c3.py', 'c4.py', 'c5.py', 'c6.py']: exec(open(f, encoding='utf-8').read())"
```

To stop after a particular block, shorten the list. Each block's output appears in the order the
book prints it.

## Data

`transactions.csv` is created by this chapter's Step 1, `gen_tx.py`, which the command above runs first.
A byte-identical copy ships in `data/generated/transactions.csv`; `_lib.py` falls back to it if the file is
not in this directory.

## Figures

```bash
python figs.py
```

Writes `fig22_1.png`, `fig22_2.png` into this directory (the shipped versions are in `figures/`).

## Reproducibility

Every block is explicitly seeded. At the versions pinned in `requirements.txt` the output
should match the book digit for digit.
See `docs/REPRODUCIBILITY.md` if a number does not match.
