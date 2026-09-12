# Chapter 9 — Linear Algebra Without Tears

Companion code for Chapter 9 of *From Absolute Zero*.

## What is here

| File | What it is |
|---|---|
| `_lib.py` | shared setup: puts the data file in place (the blocks carry their own imports) |
| `c1.py` | `import numpy as np, pandas as pd` |
| `c2.py` | `A = np.arange(6).reshape(2, 3)` |
| `c3.py` | `names = ["Acme Cafe", "Bean Bros", "Office Depot", "Corner Kiosk"]` |
| `c4.py` | `import numpy as np` |
| `c5.py` | `cust = clean.dropna(subset=["CustomerID"]).groupby("CustomerID").agg(` |
| `c6.py` | `w = np.array([1.0, 50.0, 30.0])` |
| `c7.py` | `contrib = X * w                # each feature's contribution` |
| `c8.py` | `Z = (X - X.mean(axis=0)) / X.std(axis=0)` |
| `c9.py` | `cust["rank_raw"] = cust["score"].rank(ascending=False)` |

**9 printed blocks** (`c1.py` … `c9.py`), in the order the book prints them.

## Running it

The blocks are fragments of **one continuing session**, exactly as the book presents them: later
blocks use variables defined by earlier ones, so they are not standalone scripts. `_lib.py` only
puts the data file in place. Run them in order, from this directory:

```bash
python -c "for f in ['_lib.py', 'c1.py', 'c2.py', 'c3.py', 'c4.py', 'c5.py', 'c6.py', 'c7.py', 'c8.py', 'c9.py']: exec(open(f, encoding='utf-8').read())"
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
