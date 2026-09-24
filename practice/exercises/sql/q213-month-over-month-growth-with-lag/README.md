# Q213 · Month-over-month growth with LAG

Chapter 5 · intermediate · data: `data/generated/retail.csv` as table `orders`

The check loads `retail.csv` into an in-memory SQLite database exactly as Chapter 5 does: one table,
`orders`, with the file's columns plus `Revenue = Quantity × UnitPrice`. `InvoiceNo` is text (cancellations
begin with `C`), `InvoiceDate` is an ISO string such as `2024-01-17`, and `CustomerID` is NULL where the
file has no value.

Write your query in `starter.sql` (replace `SELECT NULL;`). Column names and their order must match the
table below; row order matters only where the task says so.


Return one row per month with its revenue, the previous month's revenue and the growth between them.

| column | meaning |
|---|---|
| `Month` | `YYYY-MM` |
| `Revenue` | that month's `SUM(Revenue)` |
| `PrevRevenue` | the previous month's revenue; NULL for the first month |
| `GrowthPct` | `(Revenue - PrevRevenue) / PrevRevenue * 100`; NULL for the first month |

Order by `Month`.


```bash
python practice/exercises/sql/q213-month-over-month-growth-with-lag/check.py
```
