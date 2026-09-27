# Q219 · Three-month moving average

Chapter 5 · intermediate · data: `data/generated/retail.csv` as table `orders`

The check loads `retail.csv` into an in-memory SQLite database exactly as Chapter 5 does: one table,
`orders`, with the file's columns plus `Revenue = Quantity × UnitPrice`. `InvoiceNo` is text (cancellations
begin with `C`), `InvoiceDate` is an ISO string such as `2024-01-17`, and `CustomerID` is NULL where the
file has no value.

Write your query in `starter.sql` (replace `SELECT NULL;`). Column names and their order must match the
table below; row order matters only where the task says so.


Return each month's revenue and the average of that month and the two before it.

| column | meaning |
|---|---|
| `Month` | `YYYY-MM` |
| `Revenue` | that month's revenue |
| `MovingAvg3` | average of this and the previous two months' revenue (fewer in the first two months) |

Order by `Month`.


```bash
python practice/exercises/sql/q219-three-month-moving-average/check.py
```
