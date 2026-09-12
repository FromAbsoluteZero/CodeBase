# Chapter 21 — Distance and Margin: kNN and SVMs

Companion code for Chapter 21 of *From Absolute Zero*.

## What is here

| File | What it is |
|---|---|
| `_lib.py` | shared setup: the imports and objects the printed blocks assume, which the book shows once at the start of the session |
| `c1.py` | `# kNN has no training step. It memorizes, then measures distance at` |
| `c2.py` | `# k trades bias against variance, exactly as Chapter 17 described.` |
| `c3.py` | `# Distances stop discriminating as dimensions grow. This is the reason` |
| `c4.py` | `# An SVM maximizes the margin: the gap between the boundary and the` |
| `c5.py` | `# C and gamma both control complexity, and they interact. C sets how much` |
| `c6.py` | `# What all this costs. kNN has no training time and expensive prediction;` |
| `figs.py` | regenerates `fig21_1.png`, `fig21_2.png` |

**6 printed blocks** (`c1.py` … `c6.py`), in the order the book prints them.

## Running it

The blocks are fragments of **one continuing session**, exactly as the book presents them: later
blocks use variables defined by earlier ones, and the imports and shared objects live in
`_lib.py`. They are not standalone scripts — `python c1.py` on its own stops with a `NameError`.
Run them in order, from this directory:

```bash
python -c "for f in ['_lib.py', 'c1.py', 'c2.py', 'c3.py', 'c4.py', 'c5.py', 'c6.py']: exec(open(f, encoding='utf-8').read())"
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

Writes `fig21_1.png`, `fig21_2.png` into this directory (the shipped versions are in `figures/`).

## Reproducibility

Every block is explicitly seeded. At the versions pinned in `requirements.txt` the output
should match the book digit for digit.
The one exception is the millisecond columns of the timing table in `c6.py`: it measures your machine and will differ.
See `docs/REPRODUCIBILITY.md` if a number does not match.
