# Q212 · Deduplicate with ROW_NUMBER

Chapter 5 · intermediate · data: `data/generated/retail.csv` as table `orders`

The check loads `retail.csv` into an in-memory SQLite database exactly as Chapter 5 does: one table,
`orders`, with the file's columns plus `Revenue = Quantity × UnitPrice`. `InvoiceNo` is text (cancellations
begin with `C`), `InvoiceDate` is an ISO string such as `2024-01-17`, and `CustomerID` is NULL where the
file has no value.

Write your query in `starter.sql` (replace `SELECT NULL;`). Column names and their order must match the
table below; row order matters only where the task says so.


Some rows of `orders` are exact duplicates. Return a single row with the number of rows that would remain
if each duplicated row were kept once.

| column | meaning |
|---|---|
| `RowsAfter` | rows remaining after deduplication |


```bash
python practice/exercises/sql/q212-deduplicate-with-row_number/check.py
```
