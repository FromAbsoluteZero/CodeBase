# Q226 · Recency, frequency, monetary

Chapters 4, 11 and 26 · advanced · data: `data/generated/retail.csv`

Write `rfm(df, as_of="2024-12-31")` returning a DataFrame indexed by `CustomerID` (rows without one
excluded) with columns:

| column | meaning |
|---|---|
| `Recency` | days from the customer's last `InvoiceDate` to `as_of` |
| `Frequency` | number of distinct invoices |
| `Monetary` | net revenue (`Quantity × UnitPrice`, cancellations included) |
| `R`, `F`, `M` | quartile scores 1 to 4; `F` and `M` give 4 to the highest quartile, `R` gives 4 to the **most recent** quartile |

Score with `pd.qcut(series.rank(method="first"), 4, labels=[1, 2, 3, 4])` (reversed labels for `R`).
Also write `top_segment_count(rfm_table)`: the number of customers with `R + F + M >= 10`.

```bash
python practice/exercises/challenges/q226-recency-frequency-monetary/check.py
```
