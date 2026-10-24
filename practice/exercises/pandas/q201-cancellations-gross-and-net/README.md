# Q201 · Cancellations, gross and net

Chapter 11 · intermediate · data: `data/generated/retail.csv`

An `InvoiceNo` beginning with `C` is a cancellation, and its `Quantity` is negative. Write
`gross_and_net(df)` returning a DataFrame indexed by `Category`, sorted alphabetically, with two columns:

- `Gross`: revenue from the non-cancelled lines only;
- `Net`: revenue from all lines, cancellations included.

```bash
python practice/exercises/pandas/q201-cancellations-gross-and-net/check.py
```
