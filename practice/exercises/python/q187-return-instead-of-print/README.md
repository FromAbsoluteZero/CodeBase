# Q187 · Return instead of print

Chapter 3 · beginner · data: `data/generated/retail.csv`

Interview question Q1 asks why a function must return rather than print. This exercise makes you do it.

In `starter.py`:

- `line_revenue(quantity, unit_price)` returns quantity × unit price as a float.
- `invoice_total(rows)` takes a list of dictionaries with `Quantity` and `UnitPrice` keys (strings, as a
  CSV reader gives them) and returns the invoice's total revenue as a float, using `line_revenue`.

Neither function may print. The check calls them and uses what comes back.

```bash
python practice/exercises/python/q187-return-instead-of-print/check.py
```
