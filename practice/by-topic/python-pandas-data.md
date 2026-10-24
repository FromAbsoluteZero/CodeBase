# Python, pandas, and data handling

Asked in every analytics and data science loop, usually as a live exercise rather than from memory.

Track: Python and data handling · 30 questions · [All topics](README.md) · [Practice home](../README.md)

Levels: beginner 17, intermediate 13. Types: conceptual 7, coding 22, scenario 1.

Answer each question aloud before you open its note.

<a id="q1"></a>

**Q1.** Why must a function return rather than print?

<sub>Chapters [3](../by-chapter/ch03.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Printing sends text to the screen and yields None; returning hands a value back to the caller so it can be stored, tested, or composed. Strong answers note that a printing function cannot be unit tested or chained, and that the silent None is what later breaks with an unhelpful error far from its cause.

</details>

<a id="q2"></a>

**Q2.** What does validate="m:1" do on a merge, and why use it?

<sub>Chapters [4](../by-chapter/ch04.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

It asserts the join is many-to-one and raises if the right key is not unique. Strong answers frame it as a cheap contract: without it a duplicated key silently multiplies rows, inflating every sum downstream, and the fault is usually found weeks later in a total that looks slightly wrong.

</details>

<a id="q3"></a>

**Q3.** Explain .loc versus .iloc.

<sub>Chapters [4](../by-chapter/ch04.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

.loc selects by label, .iloc by integer position. Strong answers note that they coincide on a default RangeIndex, which is exactly why the confusion survives until an index is filtered or sorted and the two silently diverge.

</details>

<a id="q4"></a>

**Q4.** What is the SettingWithCopyWarning telling you?

<sub>Chapters [4](../by-chapter/ch04.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

That you are assigning into something pandas cannot guarantee is a view of the original rather than a copy, so the write may vanish. Strong answers name the fix — .copy() when you want a new object, single-step .loc assignment when you want to write through — and know that from pandas 3.0 a filter always hands back a copy, so nothing is printed and the edit simply never reaches the original.

</details>

<a id="q5"></a>

**Q5.** Why do you write & and | instead of and and or when filtering?

<sub>Chapters [4](../by-chapter/ch04.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Python's and and or evaluate truthiness of a whole object and cannot operate element by element; & and | are the vectorized operators. Strong answers add that precedence forces parentheses around each condition, which is the second half of the same mistake.

</details>

<a id="q6"></a>

**Q6.** How would you check a file before analysing it?

<sub>Chapters [4](../by-chapter/ch04.md) · [11](../by-chapter/ch11.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; scenario</sub>

<details>
<summary>What a strong answer contains</summary>

Shape, dtypes, head, null counts, duplicate count, and the range of every key numeric column. Strong answers add a grain check — what one row means — and reconcile at least one total against a known figure, because a file that parses cleanly can still be the wrong extract.

</details>

<a id="q7"></a>

**Q7.** What is the grain of a table, and why does it matter?

<sub>Chapters [4](../by-chapter/ch04.md) · [1](../by-chapter/ch01.md) · [5](../by-chapter/ch05.md) · [11](../by-chapter/ch11.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

The grain is what a single row represents — one order, one order line, one customer-month. Strong answers explain that joining tables of different grain silently fans out rows, and that every aggregate is wrong in a way no null check will catch.

</details>

<a id="q8"></a>

**Q8.** How do you turn a long table into a cross-tab, and what is the trap?

<sub>Chapters [4](../by-chapter/ch04.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

pivot_table or pivot, with an explicit aggregation function. The trap is that pivot fails on duplicate index-column pairs while pivot_table quietly averages them, so a silent mean appears where the analyst expected a single value. Strong answers name the aggfunc explicitly rather than relying on the default.

</details>

<a id="q186"></a>

**Q186.** Using only the csv module, count the rows in retail.csv and total the Quantity column.

<sub>Chapters [3](../by-chapter/ch03.md) · [4](../by-chapter/ch04.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; coding</sub>

Exercise: [python/q186-count-rows-and-sum-a-column](../exercises/python/q186-count-rows-and-sum-a-column/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

Open the file with csv.DictReader so each row is a dictionary keyed by the header, count rows as you go, and convert Quantity with int() before adding: every value read from a CSV is a string. Strong solutions read the file once and do not load it into a list first.

</details>

<a id="q187"></a>

**Q187.** Write a function that computes the revenue of one order line and another that totals an invoice, so that the results can be reused rather than printed.

<sub>Chapters [3](../by-chapter/ch03.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; coding</sub>

Exercise: [python/q187-return-instead-of-print](../exercises/python/q187-return-instead-of-print/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

A function that prints hands back None, so nothing downstream can use it; a function that returns hands back a value that can be stored, tested and composed. The line function does one multiplication and returns it; the invoice function calls it for every row and returns the sum. Strong solutions do not print anything.

</details>

<a id="q188"></a>

**Q188.** Total revenue (Quantity × UnitPrice) per Category using only the csv module and a dictionary.

<sub>Chapters [3](../by-chapter/ch03.md) · [4](../by-chapter/ch04.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; coding</sub>

Exercise: [python/q188-revenue-by-category-with-a-dictionary](../exercises/python/q188-revenue-by-category-with-a-dictionary/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

One pass over the file, a dictionary from category to running total, and dict.get(key, 0) or a defaultdict to avoid the KeyError on the first line of each category. Convert both numeric columns before multiplying. Strong solutions round only when reporting, not while accumulating.

</details>

<a id="q189"></a>

**Q189.** Count the distinct invoices in each calendar month of retail.csv using the standard library.

<sub>Chapters [3](../by-chapter/ch03.md) · [11](../by-chapter/ch11.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; coding</sub>

Exercise: [python/q189-distinct-invoices-per-month](../exercises/python/q189-distinct-invoices-per-month/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

The month is the first seven characters of the ISO date, so slicing the string is enough here; parsing with datetime is the safer habit when dates arrive in mixed formats. The trap is counting rows instead of invoices: the grain is one row per order line, so collect InvoiceNo values in a set per month and report the set sizes.

</details>

<a id="q190"></a>

**Q190.** Find the rows of retail.csv that appear more than once, and count how many extra copies the file holds.

<sub>Chapters [11](../by-chapter/ch11.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; coding</sub>

Exercise: [python/q190-find-exact-duplicate-rows](../exercises/python/q190-find-exact-duplicate-rows/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

Rows are lists of strings, which are unhashable as lists, so convert each to a tuple and count with a dictionary or collections.Counter. A row that appears three times is one duplicated row with two extra copies; report the row once and count copies beyond the first. Strong solutions distinguish exact duplicates from legitimate repeats, such as a customer ordering the same product twice on different dates.

</details>

<a id="q191"></a>

**Q191.** Count the rows of retail.csv with no CustomerID and report them as a share of all rows.

<sub>Chapters [11](../by-chapter/ch11.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; coding</sub>

Exercise: [python/q191-missing-customer-ids](../exercises/python/q191-missing-customer-ids/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

A missing value in a CSV is an empty string, not None, so test row['CustomerID'] == '' (or .strip() == ''). Return the count and the share as a fraction, and let the caller format it as a percentage. Strong solutions note what the missing IDs mean for any per-customer analysis: those rows can be counted in revenue but cannot be attributed.

</details>

<a id="q192"></a>

**Q192.** List the n best-selling products in retail.csv by total quantity, highest first.

<sub>Chapters [3](../by-chapter/ch03.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; coding</sub>

Exercise: [python/q192-top-products-by-quantity](../exercises/python/q192-top-products-by-quantity/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

Accumulate quantity per Description in a dictionary, then sort the items with sorted(..., key=lambda kv: kv[1], reverse=True) and slice the first n. Strong solutions mention that ties need a rule, and that the cancellation lines, with negative quantities, reduce a product's total as they should.

</details>

<a id="q193"></a>

**Q193.** Write a parser that turns a text field into a float without crashing on empty or malformed values, then use it to compute the mean total of the non-cancelled invoices.

<sub>Chapters [3](../by-chapter/ch03.md) · [11](../by-chapter/ch11.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; coding</sub>

Exercise: [python/q193-parse-numbers-safely](../exercises/python/q193-parse-numbers-safely/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

Wrap float() in try/except ValueError and return a default, so one bad cell does not stop a run of two thousand; the caller decides what the default means. For the mean, group lines by invoice, skip invoices whose number starts with C, and divide the sum of totals by the number of invoices, not the number of lines. Strong solutions count how many values fell back to the default and report it, because silent defaults hide data problems.

</details>

<a id="q194"></a>

**Q194.** Build a dictionary from invoice number to the number of order lines it has, and count the invoices with more than a given number of lines.

<sub>Chapters [3](../by-chapter/ch03.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; coding</sub>

Exercise: [python/q194-lines-per-invoice](../exercises/python/q194-lines-per-invoice/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

One pass to build {InvoiceNo: count} with dict.get or a Counter, then a comprehension or sum(1 for ... if ...) over its values. Strong solutions keep the two steps separate so the dictionary can be reused for other questions about invoice size.

</details>

<a id="q195"></a>

**Q195.** Aggregate daily revenue to months, then write a function that returns the month-over-month growth of any monthly series.

<sub>Chapters [3](../by-chapter/ch03.md) · [28](../by-chapter/ch28.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; coding</sub>

Exercise: [python/q195-month-over-month-growth-as-a-function](../exercises/python/q195-month-over-month-growth-as-a-function/) · data: `daily_revenue.csv`

<details>
<summary>What a strong answer contains</summary>

Two functions with one job each: monthly_revenue reads the file and sums by month; mom_growth takes a dictionary of month totals and returns each month's change as a fraction of the previous month, with None for the first month because it has no predecessor. Keeping the growth function independent of the file makes it testable on a three-item dictionary. Strong solutions sort by month before differencing rather than trusting file order.

</details>

<a id="q196"></a>

**Q196.** Write the file check you would run before any analysis: rows, columns, missing values, exact duplicates and the date range.

<sub>Chapters [4](../by-chapter/ch04.md) · [11](../by-chapter/ch11.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; coding</sub>

Exercise: [pandas/q196-check-a-file-before-analysing-it](../exercises/pandas/q196-check-a-file-before-analysing-it/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

Shape, dtypes, null counts, duplicate count and the range of the key columns, in one function that returns a dictionary rather than printing, so the same check runs in a notebook and in a test. Strong solutions add a grain check (Q7): what one row represents, and whether the columns you expect to identify a row actually do.

</details>

<a id="q197"></a>

**Q197.** Test whether a set of columns identifies a row uniquely, drop exact duplicates, and find out what one row of retail.csv really represents.

<sub>Chapters [4](../by-chapter/ch04.md) · [11](../by-chapter/ch11.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; coding</sub>

Exercise: [pandas/q197-establish-the-grain](../exercises/pandas/q197-establish-the-grain/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

df.duplicated(subset=keys).any() answers whether the keys are a grain; drop_duplicates() removes exact copies. The trap is assuming that (InvoiceNo, StockCode) identifies a line: even after the exact duplicates are gone, some invoices list the same product on two lines with different quantities, so the grain is one row per order line and nothing in the file names it. Strong solutions say so, add a line number if the analysis needs a key, and check the grain again after every merge.

</details>

<a id="q198"></a>

**Q198.** Attach each order line's invoice total to the line with a merge that asserts the many-to-one relationship.

<sub>Chapters [4](../by-chapter/ch04.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; coding</sub>

Exercise: [pandas/q198-merge-with-a-contract](../exercises/pandas/q198-merge-with-a-contract/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

Aggregate to one row per invoice first, then merge back with how='left' and validate='m:1', which raises if the right side's key is not unique. The row count must not change; a merge that grows the frame has multiplied rows (Q2, Q7). Strong solutions check the count before and after in code, not by eye.

</details>

<a id="q199"></a>

**Q199.** Build a Country × Category table of total revenue with pivot_table, with zeros where a combination has no sales.

<sub>Chapters [4](../by-chapter/ch04.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; coding</sub>

Exercise: [pandas/q199-cross-tab-with-pivot-table](../exercises/pandas/q199-cross-tab-with-pivot-table/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

pivot_table(values='Revenue', index='Country', columns='Category', aggfunc='sum', fill_value=0). Name the aggregation explicitly: the default is the mean, which silently answers a different question (Q8). Strong solutions check that the table's grand total equals the sum of the revenue column.

</details>

<a id="q200"></a>

**Q200.** Select the order lines that are either a bulk Beans purchase (ten or more units) or shipped to France.

<sub>Chapters [4](../by-chapter/ch04.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; coding</sub>

Exercise: [pandas/q200-filter-with-and](../exercises/pandas/q200-filter-with-and/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

Vectorized boolean operators, each condition in parentheses: (df.Category == 'Beans') & (df.Quantity >= 10) | (df.Country == 'France'). Python's and/or cannot combine Series (Q5), and without the parentheses the comparison binds after & and raises. Strong solutions name the mask and reuse it.

</details>

<a id="q201"></a>

**Q201.** Report revenue per category twice: gross, excluding cancellation lines, and net, including them.

<sub>Chapters [11](../by-chapter/ch11.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; coding</sub>

Exercise: [pandas/q201-cancellations-gross-and-net](../exercises/pandas/q201-cancellations-gross-and-net/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

Cancellations are the invoices whose number starts with C; their quantities are negative, so a plain sum already nets them out. Gross needs the cancellation rows excluded first. Strong solutions state which figure answers which question: gross for what was ordered, net for what was kept, and report both when the gap is material.

</details>

<a id="q202"></a>

**Q202.** Fill the missing AnnualIncome values in customers.csv with the median income of each customer's Plan, and count what you filled.

<sub>Chapters [11](../by-chapter/ch11.md) · [24](../by-chapter/ch24.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; coding</sub>

Exercise: [pandas/q202-impute-missing-income-by-plan](../exercises/pandas/q202-impute-missing-income-by-plan/) · data: `customers.csv`

<details>
<summary>What a strong answer contains</summary>

groupby('Plan')['AnnualIncome'].transform('median') gives every row its group's median, and fillna with that Series fills only the gaps. Return a new frame rather than mutating the input, and count the filled rows so the reader of your analysis knows how much is imputed. Strong solutions mention the leakage rule from Chapter 24: when a model follows, compute the medians on the training rows only.

</details>

<a id="q203"></a>

**Q203.** Parse the signup dates in customers.csv and compute the churn rate of each signup year.

<sub>Chapters [11](../by-chapter/ch11.md) · [12](../by-chapter/ch12.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; coding</sub>

Exercise: [pandas/q203-churn-by-signup-year](../exercises/pandas/q203-churn-by-signup-year/) · data: `customers.csv`

<details>
<summary>What a strong answer contains</summary>

pd.to_datetime on SignupDate, .dt.year for the cohort, then groupby(year)['Churn'].mean(): Churn is 0 or 1, so its mean is the rate. Strong solutions report the cohort sizes beside the rates, because a rate from a small cohort is noise, and note that recent cohorts have had less time to churn.

</details>

<a id="q204"></a>

**Q204.** Compute each order line's share of its invoice's revenue without collapsing the frame.

<sub>Chapters [4](../by-chapter/ch04.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; coding</sub>

Exercise: [pandas/q204-share-within-group-with-transform](../exercises/pandas/q204-share-within-group-with-transform/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

groupby('InvoiceNo')['Revenue'].transform('sum') returns a Series aligned to the original rows, so dividing gives a per-line share and the shares of an invoice sum to one. A groupby().sum() would collapse to one row per invoice and need a merge back. Strong solutions handle the invoices whose total is zero or negative explicitly rather than letting a division by zero through.

</details>

<a id="q205"></a>

**Q205.** Turn daily revenue into weekly means and find the best week.

<sub>Chapters [28](../by-chapter/ch28.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; coding</sub>

Exercise: [pandas/q205-weekly-resample](../exercises/pandas/q205-weekly-resample/) · data: `daily_revenue.csv`

<details>
<summary>What a strong answer contains</summary>

Parse Date, set it as the index, then resample('W').mean(): weekly bins ending on Sunday. idxmax gives the week with the highest mean. Strong solutions say what the label of a resampled bin means (the end of the week, by default) and that a partial first or last week can distort a mean.

</details>

<a id="q206"></a>

**Q206.** Cross-tabulate attrition rate by Department and OverTime in hr.csv and find the riskiest combination.

<sub>Chapters [12](../by-chapter/ch12.md) · [14](../by-chapter/ch14.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; coding</sub>

Exercise: [pandas/q206-attrition-by-department-and-overtime](../exercises/pandas/q206-attrition-by-department-and-overtime/) · data: `hr.csv`

<details>
<summary>What a strong answer contains</summary>

pivot_table with values='Attrition', index='Department', columns='OverTime', aggfunc='mean' turns a 0/1 outcome into a rate per cell. To find the maximum cell, stack the table and take idxmax. Strong solutions show the counts behind the rates and resist reading the table causally: overtime and attrition can share a cause.

</details>

<a id="q207"></a>

**Q207.** Compute the fraud base rate in transactions.csv and the fraud rate by hour of day, and find the riskiest hour.

<sub>Chapters [22](../by-chapter/ch22.md) · [23](../by-chapter/ch23.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; coding</sub>

Exercise: [pandas/q207-fraud-rate-by-hour](../exercises/pandas/q207-fraud-rate-by-hour/) · data: `transactions.csv`

<details>
<summary>What a strong answer contains</summary>

The base rate is the mean of the 0/1 Fraud column; the hourly rate is groupby('Hour')['Fraud'].mean(), with size() beside it because an hour with few transactions gives a noisy rate. The base rate is what makes 99.5% accuracy meaningless here (Q100). Strong solutions express the hourly rate relative to the base rate rather than as raw percentages.

</details>

---

<sub>Question and answer text © 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). It is not covered by the MIT licence that applies to the code. See [LICENSING.md](../../LICENSING.md).</sub>
