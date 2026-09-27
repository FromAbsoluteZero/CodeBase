# Q218 · Gross and net by month with CASE

Chapter 5 · intermediate · data: `data/generated/retail.csv` as table `orders`

The check loads `retail.csv` into an in-memory SQLite database exactly as Chapter 5 does: one table,
`orders`, with the file's columns plus `Revenue = Quantity × UnitPrice`. `InvoiceNo` is text (cancellations
begin with `C`), `InvoiceDate` is an ISO string such as `2024-01-17`, and `CustomerID` is NULL where the
file has no value.

Write your query in `starter.sql` (replace `SELECT NULL;`). Column names and their order must match the
table below; row order matters only where the task says so.


Cancellations are the invoices whose `InvoiceNo` begins with `C`; their quantities, and so their revenue,
are negative. Return, per month:

| column | meaning |
|---|---|
| `Month` | `YYYY-MM` |
| `Gross` | revenue from non-cancelled lines |
| `Net` | revenue from all lines |

Order by `Month`.


```bash
python practice/exercises/sql/q218-gross-and-net-by-month-with-case/check.py
```
