# Coding exercises and challenges

Every exercise runs on one of the book's own datasets in `data/generated/`, and every one has a check that tells you whether your answer is right. The reference solutions were run and checked before publication, under the library versions pinned in `requirements.txt`.

**How to work one.** Read the exercise's README. Write your answer in its `starter` file, then run its check from the repository root, for example:

```bash
python practice/exercises/sql/q208-revenue-by-category/check.py
```

The check runs your starter file. `--solution` runs the reference solution instead; open it only after you have a working answer of your own.

## Python

| ID | Exercise | Level | Chapters | Data |
|---|---|---|---|---|
| Q186 | [count rows and sum a column](python/q186-count-rows-and-sum-a-column/) — Using only the csv module, count the rows in retail.csv and total the Quantity column. | beginner | 3, 4 | `retail.csv` |
| Q187 | [return instead of print](python/q187-return-instead-of-print/) — Write a function that computes the revenue of one order line and another that totals an… | beginner | 3 | `retail.csv` |
| Q188 | [revenue by category with a dictionary](python/q188-revenue-by-category-with-a-dictionary/) — Total revenue (Quantity × UnitPrice) per Category using only the csv module and a… | beginner | 3, 4 | `retail.csv` |
| Q189 | [distinct invoices per month](python/q189-distinct-invoices-per-month/) — Count the distinct invoices in each calendar month of retail.csv using the standard… | intermediate | 3, 11 | `retail.csv` |
| Q190 | [find exact duplicate rows](python/q190-find-exact-duplicate-rows/) — Find the rows of retail.csv that appear more than once, and count how many extra copies… | intermediate | 11 | `retail.csv` |
| Q191 | [missing customer ids](python/q191-missing-customer-ids/) — Count the rows of retail.csv with no CustomerID and report them as a share of all rows. | beginner | 11 | `retail.csv` |
| Q192 | [top products by quantity](python/q192-top-products-by-quantity/) — List the n best-selling products in retail.csv by total quantity, highest first. | beginner | 3 | `retail.csv` |
| Q193 | [parse numbers safely](python/q193-parse-numbers-safely/) — Write a parser that turns a text field into a float without crashing on empty or… | intermediate | 3, 11 | `retail.csv` |
| Q194 | [lines per invoice](python/q194-lines-per-invoice/) — Build a dictionary from invoice number to the number of order lines it has, and count… | beginner | 3 | `retail.csv` |
| Q195 | [month over month growth as a function](python/q195-month-over-month-growth-as-a-function/) — Aggregate daily revenue to months, then write a function that returns the… | intermediate | 3, 28 | `daily_revenue.csv` |

## pandas

| ID | Exercise | Level | Chapters | Data |
|---|---|---|---|---|
| Q196 | [check a file before analysing it](pandas/q196-check-a-file-before-analysing-it/) — Write the file check you would run before any analysis: rows, columns, missing values,… | beginner | 4, 11 | `retail.csv` |
| Q197 | [establish the grain](pandas/q197-establish-the-grain/) — Test whether a set of columns identifies a row uniquely, drop exact duplicates, and find… | intermediate | 4, 11 | `retail.csv` |
| Q198 | [merge with a contract](pandas/q198-merge-with-a-contract/) — Attach each order line's invoice total to the line with a merge that asserts the… | intermediate | 4 | `retail.csv` |
| Q199 | [cross tab with pivot table](pandas/q199-cross-tab-with-pivot-table/) — Build a Country × Category table of total revenue with pivot_table, with zeros where a… | beginner | 4 | `retail.csv` |
| Q200 | [filter with and](pandas/q200-filter-with-and/) — Select the order lines that are either a bulk Beans purchase (ten or more units) or… | beginner | 4 | `retail.csv` |
| Q201 | [cancellations gross and net](pandas/q201-cancellations-gross-and-net/) — Report revenue per category twice: gross, excluding cancellation lines, and net,… | intermediate | 11 | `retail.csv` |
| Q202 | [impute missing income by plan](pandas/q202-impute-missing-income-by-plan/) — Fill the missing AnnualIncome values in customers.csv with the median income of each… | intermediate | 11, 24 | `customers.csv` |
| Q203 | [churn by signup year](pandas/q203-churn-by-signup-year/) — Parse the signup dates in customers.csv and compute the churn rate of each signup year. | intermediate | 11, 12 | `customers.csv` |
| Q204 | [share within group with transform](pandas/q204-share-within-group-with-transform/) — Compute each order line's share of its invoice's revenue without collapsing the frame. | intermediate | 4 | `retail.csv` |
| Q205 | [weekly resample](pandas/q205-weekly-resample/) — Turn daily revenue into weekly means and find the best week. | beginner | 28 | `daily_revenue.csv` |
| Q206 | [attrition by department and overtime](pandas/q206-attrition-by-department-and-overtime/) — Cross-tabulate attrition rate by Department and OverTime in hr.csv and find the riskiest… | beginner | 12, 14 | `hr.csv` |
| Q207 | [fraud rate by hour](pandas/q207-fraud-rate-by-hour/) — Compute the fraud base rate in transactions.csv and the fraud rate by hour of day, and… | beginner | 22, 23 | `transactions.csv` |

## SQL

| ID | Exercise | Level | Chapters | Data |
|---|---|---|---|---|
| Q208 | [revenue by category](sql/q208-revenue-by-category/) — Write the query that returns total revenue per category, highest first. | beginner | 5 | `retail.csv` |
| Q209 | [filter rows then filter groups](sql/q209-filter-rows-then-filter-groups/) — List the countries whose revenue from Beans exceeds 6,000, using WHERE for the rows and… | beginner | 5 | `retail.csv` |
| Q210 | [best selling product per category](sql/q210-best-selling-product-per-category/) — For each category, return its top product by revenue, using ROW_NUMBER in a CTE. | intermediate | 5 | `retail.csv` |
| Q211 | [second highest invoice total](sql/q211-second-highest-invoice-total/) — Find the invoice with the second-highest total revenue, using DENSE_RANK so that ties… | intermediate | 5 | `retail.csv` |
| Q212 | [deduplicate with row number](sql/q212-deduplicate-with-row-number/) — Count the rows that remain after exact duplicates are removed, using ROW_NUMBER over… | intermediate | 5 | `retail.csv` |
| Q213 | [month over month growth with lag](sql/q213-month-over-month-growth-with-lag/) — Compute each month's revenue, the previous month's revenue, and the growth between them. | intermediate | 5 | `retail.csv` |
| Q214 | [counting with nulls](sql/q214-counting-with-nulls/) — Count all rows, the rows with a customer, and the rows without one, in a single query. | beginner | 5 | `retail.csv` |
| Q215 | [average lines per invoice by country](sql/q215-average-lines-per-invoice-by-country/) — Compute the average number of order lines per invoice in each country, aggregating in… | intermediate | 5 | `retail.csv` |
| Q216 | [frequent customers](sql/q216-frequent-customers/) — List the customers with at least five invoices, with their invoice count and total… | intermediate | 5 | `retail.csv` |
| Q217 | [running total with a frame](sql/q217-running-total-with-a-frame/) — Compute the cumulative revenue month by month with a window frame stated explicitly. | intermediate | 5 | `retail.csv` |
| Q218 | [gross and net by month with case](sql/q218-gross-and-net-by-month-with-case/) — Report each month's gross revenue (cancellations excluded) and net revenue… | intermediate | 5 | `retail.csv` |
| Q219 | [three month moving average](sql/q219-three-month-moving-average/) — Compute a three-month moving average of monthly revenue with a bounded window frame. | intermediate | 5 | `retail.csv` |

## Multi-step challenges

| ID | Exercise | Level | Chapters | Data |
|---|---|---|---|---|
| Q220 | [a year of retail in one function](challenges/q220-a-year-of-retail-in-one-function/) — Summarize a year of retail.csv the way a first analysis brief would: net revenue, the… | intermediate | 1, 4, 11, 12 | `retail.csv` |
| Q221 | [an honest attrition baseline](challenges/q221-an-honest-attrition-baseline/) — Build a logistic-regression baseline for attrition in hr.csv with a proper split, and… | intermediate | 14, 16, 22 | `hr.csv` |
| Q222 | [choosing a fraud threshold](challenges/q222-choosing-a-fraud-threshold/) — Train a fraud classifier on transactions.csv and pick the decision threshold that… | advanced | 22, 23 | `transactions.csv` |
| Q223 | [leakage in preprocessing measured](challenges/q223-leakage-in-preprocessing-measured/) — Measure how much a leaky preprocessing step changes a cross-validated score on… | intermediate | 16, 24, 25 | `customers.csv` |
| Q224 | [forecast baselines that must be beaten](challenges/q224-forecast-baselines-that-must-be-beaten/) — Hold out the last 90 days of daily revenue and measure three baselines any forecasting… | intermediate | 28 | `daily_revenue.csv` |
| Q225 | [do the clusters mean anything](challenges/q225-do-the-clusters-mean-anything/) — Cluster segments.csv with k-means and measure the result two ways: against the true… | intermediate | 26, 27 | `segments.csv` |
| Q226 | [recency frequency monetary](challenges/q226-recency-frequency-monetary/) — Build an RFM table for the identified customers in retail.csv, score each dimension into… | advanced | 4, 11, 26 | `retail.csv` |
| Q227 | [is the overtime effect real](challenges/q227-is-the-overtime-effect-real/) — Compare attrition between employees who work overtime and those who do not, with a… | intermediate | 8, 15, 42 | `hr.csv` |

[Practice home](../README.md)

---

<sub>Exercise text © 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). The exercise code (every `starter`, `solution` and `check` file) is MIT-licensed like the rest of the code. See [LICENSING.md](../../LICENSING.md).</sub>
