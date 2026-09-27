# Q198 · Merge with a contract

Chapter 4 · intermediate · data: `data/generated/retail.csv`

Write:

- `invoice_totals(df)`: a frame with one row per `InvoiceNo` and a column `InvoiceTotal`, the sum of
  `Quantity × UnitPrice` for that invoice.
- `add_invoice_total(df)`: the original lines with an `InvoiceTotal` column attached by a left merge that
  uses `validate="m:1"`. The number of rows must not change.

The check also hands `add_invoice_total` a frame whose invoice totals are duplicated and expects the
merge to raise, which is what `validate` is for.

```bash
python practice/exercises/pandas/q198-merge-with-a-contract/check.py
```
