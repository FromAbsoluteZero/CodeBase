# Q189 · Distinct invoices per month

Chapters 3 and 11 · intermediate · data: `data/generated/retail.csv`

Write `invoices_per_month(path)` returning a dictionary that maps each month, written `YYYY-MM`, to the
number of **distinct** invoices in that month. The file has one row per order line, so an invoice with six
lines must be counted once.

Dates are ISO strings such as `2024-01-17`.

```bash
python practice/exercises/python/q189-distinct-invoices-per-month/check.py
```
