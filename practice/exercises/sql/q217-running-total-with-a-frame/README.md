# Q217 · Running total with a frame

Chapter 5 · intermediate · data: `data/generated/retail.csv` as table `orders`

The check loads `retail.csv` into an in-memory SQLite database exactly as Chapter 5 does: one table,
`orders`, with the file's columns plus `Revenue = Quantity × UnitPrice`. `InvoiceNo` is text (cancellations
begin with `C`), `InvoiceDate` is an ISO string such as `2024-01-17`, and `CustomerID` is NULL where the
file has no value.

Write your query in `starter.sql` (replace `SELECT NULL;`). Column names and their order must match the
table below; row order matters only where the task says so.


Return each month's revenue and the running total up to and including that month.

| column | meaning |
|---|---|
| `Month` | `YYYY-MM` |
| `Revenue` | that month's revenue |
| `RunningTotal` | cumulative revenue through that month |

Order by `Month`. State the window frame explicitly with `ROWS`.


```bash
python practice/exercises/sql/q217-running-total-with-a-frame/check.py
```
