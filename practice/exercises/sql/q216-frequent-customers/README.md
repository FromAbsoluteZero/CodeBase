# Q216 · Frequent customers

Chapter 5 · intermediate · data: `data/generated/retail.csv` as table `orders`

The check loads `retail.csv` into an in-memory SQLite database exactly as Chapter 5 does: one table,
`orders`, with the file's columns plus `Revenue = Quantity × UnitPrice`. `InvoiceNo` is text (cancellations
begin with `C`), `InvoiceDate` is an ISO string such as `2024-01-17`, and `CustomerID` is NULL where the
file has no value.

Write your query in `starter.sql` (replace `SELECT NULL;`). Column names and their order must match the
table below; row order matters only where the task says so.


Return the customers with **five or more distinct invoices**, ignoring rows with no `CustomerID`.

| column | meaning |
|---|---|
| `CustomerID` | the customer |
| `Invoices` | number of distinct invoices |
| `Revenue` | `SUM(Revenue)` |

Order by `Revenue` descending.


```bash
python practice/exercises/sql/q216-frequent-customers/check.py
```
