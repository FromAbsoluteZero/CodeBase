# Q214 · Counting with NULLs

Chapter 5 · beginner · data: `data/generated/retail.csv` as table `orders`

The check loads `retail.csv` into an in-memory SQLite database exactly as Chapter 5 does: one table,
`orders`, with the file's columns plus `Revenue = Quantity × UnitPrice`. `InvoiceNo` is text (cancellations
begin with `C`), `InvoiceDate` is an ISO string such as `2024-01-17`, and `CustomerID` is NULL where the
file has no value.

Write your query in `starter.sql` (replace `SELECT NULL;`). Column names and their order must match the
table below; row order matters only where the task says so.


Return a single row with three counts.

| column | meaning |
|---|---|
| `TotalRows` | all rows |
| `WithCustomer` | rows where `CustomerID` is not NULL |
| `WithoutCustomer` | rows where `CustomerID` is NULL |


```bash
python practice/exercises/sql/q214-counting-with-nulls/check.py
```
