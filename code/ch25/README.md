# Chapter 25 — Hyperparameter Tuning

Companion code for Chapter 25 of *From Absolute Zero*.

## What is here

| File | What it is |
|---|---|
| `_lib.py` | shared setup: the imports and objects the printed blocks assume, which the book shows once at the start of the session |
| `c1.py` | `# Grid search: every combination, exhaustively.` |
| `c2.py` | `# Random search covers a wider space for the same budget, and samples` |
| `c3.py` | `# The tuned score is the maximum of many noisy estimates, so it is biased` |
| `c4.py` | `# Preprocessing choices are hyperparameters too. Tune them in the same` |
| `c5.py` | `# The honest final report: tune on training, estimate honestly, then` |
| `figs.py` | regenerates `fig25_1.png`, `fig25_2.png` |

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

`customers.csv` is created by Chapter 24 (`code/ch24/gen_orders.py`). The blocks read it from the working
directory, as the book does. `_lib.py` uses the local file if you have generated one, otherwise
the byte-identical copy shipped in `data/generated/customers.csv`. Full provenance: `DATA_MANIFEST.csv`.

## Figures

```bash
python figs.py
```

Writes `fig25_1.png`, `fig25_2.png` into this directory (the shipped versions are in `figures/`).

## Reproducibility

Every block is explicitly seeded. At the versions pinned in `requirements.txt` the output
should match the book digit for digit.
See `docs/REPRODUCIBILITY.md` if a number does not match.
