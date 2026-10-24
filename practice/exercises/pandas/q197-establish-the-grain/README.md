# Q197 · Establish the grain

Chapters 4 and 11 · intermediate · data: `data/generated/retail.csv`

The grain is what one row represents (Q7). Write:

- `is_unique_grain(df, keys)`: `True` if no two rows share the same values of the columns in `keys`.
- `dedupe(df)`: the frame with exact duplicate rows removed, keeping the first copy, index reset.
- `repeated_product_lines(df)`: after deduplication, the number of `(InvoiceNo, StockCode)` pairs that
  still occur on more than one line.

Then answer for yourself: is `["InvoiceNo", "StockCode"]` a grain of the raw file? Of the deduplicated
file? If not, what does one row represent, and what would you have to add to identify it?

```bash
python practice/exercises/pandas/q197-establish-the-grain/check.py
```
