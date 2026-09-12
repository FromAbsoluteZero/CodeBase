# Chapter 4 — Working with Data: NumPy and pandas

Companion code for Chapter 4 of *From Absolute Zero*.

## What is here

| File | What it is |
|---|---|
| `gen_retail.py` | the printed block that creates `retail.csv` |
| `_lib.py` | shared setup: puts the data file in place (the blocks carry their own imports) |
| `c1.py` | `import pandas as pd` |
| `c2.py` | `# one column is a Series, several are a DataFrame` |
| `c3.py` | `# label-based vs position-based` |
| `c4.py` | `# the quick form: one column, one statistic` |
| `c5.py` | `regions = pd.DataFrame({` |
| `c6.py` | `pv = m.pivot_table(index="Region", columns="Category",` |
| `c7.py` | `import numpy as np, time` |
| `c8.py` | `import pandas as pd` |
| `c9.py` | `df["Revenue"] = df["Quantity"] * df["UnitPrice"]` |
| `c10.py` | `by_country = (clean.groupby("Country")["Revenue"].sum()` |
| `c11.py` | `clean["InvoiceDate"] = pd.to_datetime(clean["InvoiceDate"])` |
| `c12.py` | `prod = clean.groupby("Description").agg(` |
| `c13.py` | `top = prod.index[0]` |

**13 printed blocks** (`c1.py` … `c13.py`), in the order the book prints them.

## Running it

The blocks are fragments of **one continuing session**, exactly as the book presents them: later
blocks use variables defined by earlier ones, so they are not standalone scripts. `_lib.py` only
puts the data file in place. Run them in order, from this directory:

```bash
python -c "for f in ['gen_retail.py', '_lib.py', 'c1.py', 'c2.py', 'c3.py', 'c4.py', 'c5.py', 'c6.py', 'c7.py', 'c8.py', 'c9.py', 'c10.py', 'c11.py', 'c12.py', 'c13.py']: exec(open(f, encoding='utf-8').read())"
```

To stop after a particular block, shorten the list. Each block's output appears in the order the
book prints it.

## Data

`retail.csv` is created by this chapter's first block, `gen_retail.py`, which the command above runs first.
A byte-identical copy ships in `data/generated/retail.csv`; `_lib.py` falls back to it if the file is
not in this directory.

## Reproducibility

Every block is explicitly seeded. At the versions pinned in `requirements.txt` the output
should match the book digit for digit.
The one exception is the `loop … ms / vectorized … ms / ratio` line in `c7.py`: it measures your machine and will differ.
See `docs/REPRODUCIBILITY.md` if a number does not match.
