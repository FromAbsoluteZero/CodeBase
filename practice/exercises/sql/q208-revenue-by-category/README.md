# Q208 · Revenue by category

Chapter 5 · beginner · data: `data/generated/retail.csv` as table `orders`

The check loads `retail.csv` into an in-memory SQLite database exactly as Chapter 5 does: one table,
`orders`, with the file's columns plus `Revenue = Quantity × UnitPrice`. `InvoiceNo` is text (cancellations
begin with `C`), `InvoiceDate` is an ISO string such as `2024-01-17`, and `CustomerID` is NULL where the
file has no value.

Write your query in `starter.sql` (replace `SELECT NULL;`). Column names and their order must match the
table below; row order matters only where the task says so.


Return one row per `Category` with its total revenue, largest first.

| column | meaning |
|---|---|
| `Category` | the category |
| `Revenue` | `SUM(Revenue)` for that category |


```bash
python practice/exercises/sql/q208-revenue-by-category/check.py
```
