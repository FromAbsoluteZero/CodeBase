# Q209 · Filter rows, then filter groups

Chapter 5 · beginner · data: `data/generated/retail.csv` as table `orders`

The check loads `retail.csv` into an in-memory SQLite database exactly as Chapter 5 does: one table,
`orders`, with the file's columns plus `Revenue = Quantity × UnitPrice`. `InvoiceNo` is text (cancellations
begin with `C`), `InvoiceDate` is an ISO string such as `2024-01-17`, and `CustomerID` is NULL where the
file has no value.

Write your query in `starter.sql` (replace `SELECT NULL;`). Column names and their order must match the
table below; row order matters only where the task says so.


Return the countries whose total revenue from the `Beans` category is greater than 6,000, largest first.

| column | meaning |
|---|---|
| `Country` | the country |
| `BeansRevenue` | `SUM(Revenue)` over that country's Beans lines |


```bash
python practice/exercises/sql/q209-filter-rows-then-filter-groups/check.py
```
