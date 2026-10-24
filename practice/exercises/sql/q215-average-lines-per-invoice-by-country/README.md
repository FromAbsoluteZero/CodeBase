# Q215 · Average lines per invoice by country

Chapter 5 · intermediate · data: `data/generated/retail.csv` as table `orders`

The check loads `retail.csv` into an in-memory SQLite database exactly as Chapter 5 does: one table,
`orders`, with the file's columns plus `Revenue = Quantity × UnitPrice`. `InvoiceNo` is text (cancellations
begin with `C`), `InvoiceDate` is an ISO string such as `2024-01-17`, and `CustomerID` is NULL where the
file has no value.

Write your query in `starter.sql` (replace `SELECT NULL;`). Column names and their order must match the
table below; row order matters only where the task says so.


Return the average number of order lines per invoice, by country.

| column | meaning |
|---|---|
| `Country` | the country |
| `Invoices` | number of distinct invoices |
| `AvgLines` | average lines per invoice |

Order by `AvgLines` descending. An invoice belongs to one country.


```bash
python practice/exercises/sql/q215-average-lines-per-invoice-by-country/check.py
```
