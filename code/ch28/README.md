# Chapter 28 — Time Series and Forecasting

Companion code for Chapter 28 of *From Absolute Zero*.

## What is here

| File | What it is |
|---|---|
| `gen_daily.py` | the printed block that creates `daily_revenue.csv` |
| `_lib.py` | shared setup: puts the data file in place (the blocks carry their own imports) |
| `c1.py` | `import pandas as pd` |
| `c2.py` | `by_dow = s.groupby(s.index.day_name()).mean()` |
| `c3.py` | `roll = s.rolling(7, center=True).mean()      # 7 days kills the weekly cycle` |
| `c4.py` | `import numpy as np` |
| `c5.py` | `from statsmodels.tsa.holtwinters import ExponentialSmoothing` |
| `c6.py` | `from sklearn.ensemble import RandomForestRegressor` |
| `c7.py` | `def fold(cut):` |
| `figs.py` | regenerates `fig28_1.png`, `fig28_2.png` |

**7 printed blocks** (`c1.py` … `c7.py`), in the order the book prints them.

## Running it

The blocks are fragments of **one continuing session**, exactly as the book presents them: later
blocks use variables defined by earlier ones, so they are not standalone scripts. `_lib.py` only
puts the data file in place. Run them in order, from this directory:

```bash
python -c "for f in ['gen_daily.py', '_lib.py', 'c1.py', 'c2.py', 'c3.py', 'c4.py', 'c5.py', 'c6.py', 'c7.py']: exec(open(f, encoding='utf-8').read())"
```

To stop after a particular block, shorten the list. Each block's output appears in the order the
book prints it.

## Data

`daily_revenue.csv` is created by this chapter's Step 1, `gen_daily.py`, which the command above runs first.
A byte-identical copy ships in `data/generated/daily_revenue.csv`; `_lib.py` falls back to it if the file is
not in this directory.

## Figures

```bash
python figs.py
```

Writes `fig28_1.png`, `fig28_2.png` into this directory (the shipped versions are in `figures/`).

## Requirements

This chapter needs `statsmodels`, which is in `requirements-optional.txt`.

## Reproducibility

Every block is explicitly seeded. At the versions pinned in `requirements.txt` the output
should match the book digit for digit.
See `docs/REPRODUCIBILITY.md` if a number does not match.
