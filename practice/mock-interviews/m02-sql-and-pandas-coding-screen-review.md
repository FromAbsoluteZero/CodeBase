# M02 · SQL and pandas coding screen: review sheet

Read this only after you have sat the [mock interview](m02-sql-and-pandas-coding-screen.md).

## 1. Q211

Find the invoice with the second-highest total revenue, using DENSE_RANK so that ties are handled.

<sub>Chapters [5](../by-chapter/ch05.md)</sub>

Check your code: `python practice/exercises/sql/q211-second-highest-invoice-total/check.py`

**What a strong answer contains.** Aggregate to one row per invoice, rank with DENSE_RANK() OVER (ORDER BY total DESC) in a CTE, and select rank 2. DENSE_RANK rather than ROW_NUMBER, so two invoices tied for first both rank 1 and the second-highest value is still rank 2; LIMIT 1 OFFSET 1 gets that wrong under ties (Q11).

## 2. Q213

Compute each month's revenue, the previous month's revenue, and the growth between them.

<sub>Chapters [5](../by-chapter/ch05.md)</sub>

Check your code: `python practice/exercises/sql/q213-month-over-month-growth-with-lag/check.py`

**What a strong answer contains.** Aggregate to months in a CTE with substr(InvoiceDate, 1, 7), then LAG(Revenue) OVER (ORDER BY Month) gives the previous row's value; growth is (Revenue - Prev) / Prev, NULL for the first month because LAG returns NULL there (Q18). Strong solutions guard against a zero previous month and note that LAG assumes no month is missing from the data.

## 3. Q210

For each category, return its top product by revenue, using ROW_NUMBER in a CTE.

<sub>Chapters [5](../by-chapter/ch05.md)</sub>

Check your code: `python practice/exercises/sql/q210-best-selling-product-per-category/check.py`

**What a strong answer contains.** Aggregate to (Category, Description) first, then ROW_NUMBER() OVER (PARTITION BY Category ORDER BY Revenue DESC) in a CTE, and filter rn = 1 in the outer query. The filter cannot go in the same SELECT's WHERE because window functions are evaluated after WHERE (Q12). Strong solutions say what happens on ties and add a tiebreaker to the ORDER BY.

## 4. Q197

Test whether a set of columns identifies a row uniquely, drop exact duplicates, and find out what one row of retail.csv really represents.

<sub>Chapters [4](../by-chapter/ch04.md) · [11](../by-chapter/ch11.md)</sub>

Check your code: `python practice/exercises/pandas/q197-establish-the-grain/check.py`

**What a strong answer contains.** df.duplicated(subset=keys).any() answers whether the keys are a grain; drop_duplicates() removes exact copies. The trap is assuming that (InvoiceNo, StockCode) identifies a line: even after the exact duplicates are gone, some invoices list the same product on two lines with different quantities, so the grain is one row per order line and nothing in the file names it. Strong solutions say so, add a line number if the analysis needs a key, and check the grain again after every merge.

## 5. Q198

Attach each order line's invoice total to the line with a merge that asserts the many-to-one relationship.

<sub>Chapters [4](../by-chapter/ch04.md)</sub>

Check your code: `python practice/exercises/pandas/q198-merge-with-a-contract/check.py`

**What a strong answer contains.** Aggregate to one row per invoice first, then merge back with how='left' and validate='m:1', which raises if the right side's key is not unique. The row count must not change; a merge that grows the frame has multiplied rows (Q2, Q7). Strong solutions check the count before and after in code, not by eye.

[Back to the mock interview](m02-sql-and-pandas-coding-screen.md)

---

<sub>Question and answer text © 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). It is not covered by the MIT licence that applies to the code. See [LICENSING.md](../../LICENSING.md).</sub>
