# Chapter 17 — Bias, Variance, and Regularization

Companion code for Chapter 17 of *From Absolute Zero*.

## What is here

| File | What it is |
|---|---|
| `_lib.py` | shared setup: the imports and objects the printed blocks assume, which the book shows once at the start of the session |
| `c1.py` | `import numpy as np` |
| `c2.py` | `rng = np.random.default_rng(0)` |
| `c3.py` | `rng = np.random.default_rng(0)` |
| `c4.py` | `rng = np.random.default_rng(0)` |
| `c5.py` | `Xo, yo = o[feats].values, o["rev"].values` |
| `figs.py` | regenerates `fig17_1.png`, `fig17_2.png` |

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

`retail.csv` is created by Chapter 4 (`code/ch04/gen_retail.py`). The blocks read it from the working
directory, as the book does. `_lib.py` uses the local file if you have generated one, otherwise
the byte-identical copy shipped in `data/generated/retail.csv`. Full provenance: `DATA_MANIFEST.csv`.

## Figures

```bash
python figs.py
```

Writes `fig17_1.png`, `fig17_2.png` into this directory (the shipped versions are in `figures/`).

## Reproducibility

Every block is explicitly seeded. At the versions pinned in `requirements.txt` the output
should match the book digit for digit.

Note: the book's Step 5 output box begins by repeating the two lines Step 4 prints (`897 orders, 10
candidate features` and the correlation). `c5.py` prints only its own table.
See `docs/REPRODUCIBILITY.md` if a number does not match.
