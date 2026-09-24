# Q204 · Share within group with transform

Chapter 4 · intermediate · data: `data/generated/retail.csv`

Write `line_share(df)` returning a Series, aligned to `df`'s index, giving each line's revenue
(`Quantity × UnitPrice`) as a fraction of its invoice's total revenue. The shares of every invoice must add
up to 1. No invoice in this file has a zero total.

```bash
python practice/exercises/pandas/q204-share-within-group-with-transform/check.py
```
