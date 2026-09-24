# Q193 · Parse numbers safely

Chapters 3 and 11 · intermediate · data: `data/generated/retail.csv`

Write:

- `to_float(text, default=None)`: convert `text` to a float; if it is empty or not a number, return
  `default` instead of raising.
- `mean_invoice_total(path)`: the mean revenue per invoice across the invoices that are **not**
  cancellations (an `InvoiceNo` beginning with `C` is a cancellation). Revenue per line is
  `Quantity × UnitPrice`, parsed with `to_float`.

```bash
python practice/exercises/python/q193-parse-numbers-safely/check.py
```
