# Q220 · A year of retail, in one function

Chapters 1, 4, 11 and 12 · intermediate · data: `data/generated/retail.csv`

Write `retail_summary(df)` returning a dictionary with these keys:

| key | value |
|---|---|
| `net_revenue` | sum of `Quantity × UnitPrice` over all lines (cancellations are negative) |
| `cancellation_share` | minus the cancelled revenue, divided by the gross revenue of non-cancelled lines |
| `best_month`, `worst_month` | `YYYY-MM` of the highest and lowest net monthly revenue |
| `top_category` | the category with the highest net revenue |
| `top_category_share` | its share of net revenue |
| `repeat_customer_share` | among rows with a `CustomerID`, the share of customers with more than one distinct invoice |

An `InvoiceNo` beginning with `C` is a cancellation.

```bash
python practice/exercises/challenges/q220-a-year-of-retail-in-one-function/check.py
```
