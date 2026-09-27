# [Project title: a finding, not a topic]

<!-- README template for a portfolio project (Appendix B of From Absolute Zero). CC0: copy it into
     your project, delete these comments, and keep the order. A reviewer will spend ninety seconds
     and read from the top. -->

**[Finding, in one sentence, with the number.]** **[What it means for the decision, in one sentence.]**

<!-- Example: "Customers who signed up through the app churn at 29%, against 18% for the web,
     and the gap is entirely in the first ninety days. Retention effort should move to app onboarding." -->

## The question

- **Decision:** [what will be done differently depending on the answer]
- **Who decides:** [the role, not a name]
- **Metric:** [the number that settles it, and the threshold that changes the decision]

## The data

- **Source:** [where it came from, and when]
- **Grain:** one row is [one order line / one customer-month / ...]
- **Size:** [rows × columns, date range]
- **Cleaning decisions:** [each one, with the count it affected, e.g. "removed 18 cancellation lines (negative quantities)"]
- **What the data cannot answer:** [the limits you found]

## The method

[Two or three sentences. Name the baseline and what beat it. Link the notebook or script for detail;
do not paste the code here.]

## The result

| Measure | Baseline | This work |
|---|---|---|
| [metric] | [value] | [value] |

[One chart that makes the finding visible. Title it with the finding.]

## Limitations

- [What you do not know]
- [What would change the conclusion if it were true]
- [Associated with, not causes: say which claims are causal and why the design supports them, or that none are]

## Reproduce it

```bash
git clone [url]
cd [folder]
pip install -r requirements.txt
python run.py        # or: open analysis.ipynb and run all cells
```

Every number above is produced by that command. Library versions are pinned in `requirements.txt`.
No data files or credentials are in this repository; `[how to obtain the data]`.
