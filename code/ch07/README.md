# Chapter 7 — Probability

Companion code for Chapter 7 of *From Absolute Zero*.

## What is here

| File | What it is |
|---|---|
| `_lib.py` | shared setup: puts the data file in place (the blocks carry their own imports) |
| `c1.py` | `import pandas as pd` |
| `c2.py` | `uk = orders["country"] == "United Kingdom"` |
| `c3.py` | `prior = 0.04        # P(buys)` |
| `c4.py` | `cost, margin = 6.00, 140.00` |
| `c5.py` | `from math import comb` |
| `c6.py` | `import numpy as np` |
| `c7.py` | `import numpy as np` |
| `c8.py` | `prior = 0.06     # P(churn)` |
| `c9.py` | `N = 10_000` |
| `c10.py` | `persuade = 0.30    # ASSUMPTION: 30% of at-risk customers stay` |
| `c11.py` | `breakeven = spend / (tp * value)` |
| `c12.py` | `print(f"Flagging catches {tp/churners:.0%} of churners but only "` |

**12 printed blocks** (`c1.py` … `c12.py`), in the order the book prints them.

## Running it

The blocks are fragments of **one continuing session**, exactly as the book presents them: later
blocks use variables defined by earlier ones, so they are not standalone scripts. `_lib.py` only
puts the data file in place. Run them in order, from this directory:

```bash
python -c "for f in ['_lib.py', 'c1.py', 'c2.py', 'c3.py', 'c4.py', 'c5.py', 'c6.py', 'c7.py', 'c8.py', 'c9.py', 'c10.py', 'c11.py', 'c12.py']: exec(open(f, encoding='utf-8').read())"
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
