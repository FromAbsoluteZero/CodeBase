# Chapter 10 — Calculus for Optimization

Companion code for Chapter 10 of *From Absolute Zero*.

## What is here

| File | What it is |
|---|---|
| `_lib.py` | shared setup: puts the data file in place (the blocks carry their own imports) |
| `c1.py` | `import numpy as np, pandas as pd` |
| `c2.py` | `def run(eta, steps):` |
| `c3.py` | `import numpy as np` |
| `c4.py` | `b0, b1 = 0.0, 0.0` |
| `c5.py` | `g0 = 2 * err.mean()` |
| `c6.py` | `b0, b1 = 0.0, 0.0` |
| `c7.py` | `slope = b1 / x.std()` |
| `c8.py` | `X = np.column_stack([np.ones(len(x)), x])` |

**8 printed blocks** (`c1.py` … `c8.py`), in the order the book prints them.

## Running it

The blocks are fragments of **one continuing session**, exactly as the book presents them: later
blocks use variables defined by earlier ones, so they are not standalone scripts. `_lib.py` only
puts the data file in place. Run them in order, from this directory:

```bash
python -c "for f in ['_lib.py', 'c1.py', 'c2.py', 'c3.py', 'c4.py', 'c5.py', 'c6.py', 'c7.py', 'c8.py']: exec(open(f, encoding='utf-8').read())"
```

To stop after a particular block, shorten the list. Each block's output appears in the order the
book prints it.

## Data

`retail.csv` is created by Chapter 4 (`code/ch04/gen_retail.py`). The blocks read it from the working
directory, as the book does. `_lib.py` uses the local file if you have generated one, otherwise
the byte-identical copy shipped in `data/generated/retail.csv`. Full provenance: `DATA_MANIFEST.csv`.

## Reproducibility

Every block is explicitly seeded. At the versions pinned in `requirements.txt` the output
should match the book digit for digit.
See `docs/REPRODUCIBILITY.md` if a number does not match.
