# Chapter 13 — Linear Regression, Thoroughly

Companion code for Chapter 13 of *From Absolute Zero*.

## What is here

| File | What it is |
|---|---|
| `_lib.py` | shared setup: puts the data file in place (the blocks carry their own imports) |
| `c1.py` | `import pandas as pd, numpy as np` |
| `c2.py` | `y = o["rev"].values` |
| `c3.py` | `fitted = X @ beta` |
| `c4.py` | `D = pd.get_dummies(o["country"], prefix="c",` |
| `c5.py` | `def vif(X, j):` |
| `c6.py` | `import numpy as np` |
| `c7.py` | `r = stats.linregress(o["units"], o["rev"])` |
| `c8.py` | `y = o["rev"].values` |
| `c9.py` | `D = pd.get_dummies(o["country"], prefix="", prefix_sep="",` |
| `c10.py` | `fit = Xc @ bc` |
| `c11.py` | `print(f"1. Each additional unit is associated with "` |

**11 printed blocks** (`c1.py` … `c11.py`), in the order the book prints them.

## Running it

The blocks are fragments of **one continuing session**, exactly as the book presents them: later
blocks use variables defined by earlier ones, so they are not standalone scripts. `_lib.py` only
puts the data file in place. Run them in order, from this directory:

```bash
python -c "for f in ['_lib.py', 'c1.py', 'c2.py', 'c3.py', 'c4.py', 'c5.py', 'c6.py', 'c7.py', 'c8.py', 'c9.py', 'c10.py', 'c11.py']: exec(open(f, encoding='utf-8').read())"
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
