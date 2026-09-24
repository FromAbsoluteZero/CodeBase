# Project ideas

Framings, not datasets. Each is a question with a decision behind it, so the project starts where
Chapter 1 says every analysis starts. Take a framing to data you can get: your own workplace or
studies, a public source in a field you know, or a dataset nobody else in your cohort has picked.
No links are given on purpose. Links rot, and a portfolio built on a dataset the reviewer has already
seen a thousand times is what Appendix B warns against.

Each framing names the chapters it exercises and what a reviewer will look for.

## Project 1 · An analysis (Chapters 1 to 12)

| Framing | The decision | What a reviewer looks for |
|---|---|---|
| **Where did the drop come from?** A metric fell: revenue, sign-ups, on-time deliveries. Break it down by segment, time and product until the fall has an address. | Where to put the next two weeks of effort | The grain stated; the decomposition adds up to the total; rival explanations listed before one is chosen |
| **Is this the right number to report?** Take a headline metric your organisation quotes and rebuild it from raw rows. | Whether to keep reporting it that way | Reconciliation to the published figure, and an honest list of where they differ and why |
| **Who are we actually serving?** Profile the customers, users or cases in a file against who the organisation thinks it serves. | Whether the targeting assumption holds | Cleaning decisions documented; charts that follow Chapter 12's rules; medians beside means where the tail matters |
| **What does a week look like?** Weekly and daily patterns in an operational series: calls, orders, incidents. | Staffing or scheduling | Seasonality shown, not asserted; the partial first and last periods handled |
| **Before and after.** Something changed on a date: a price, a policy, a layout. Compare the periods without claiming causation. | Whether the change should stay | The comparison window justified; confounders named; the word "associated" used correctly |

## Project 2 · A model, honestly evaluated (Chapters 13 to 29)

| Framing | The decision | What a reviewer looks for |
|---|---|---|
| **Who will leave?** Predict churn, attrition or non-renewal from data available before the event. | Who to contact, and whether contacting them is worth the cost | A baseline the model beats; a chronological or stratified split; leakage hunted, not assumed absent; a threshold chosen from the cost of each error |
| **Which cases need a human?** Flag the transactions, claims or tickets that deserve review. | How many reviewers the queue needs | Precision and recall at the chosen threshold, with the base rate stated; calibration checked if the score is shown to people |
| **How much, and how sure?** Forecast a quantity (demand, revenue, load) with an interval. | How much to order, staff or provision | Beaten baselines: mean, last value, seasonal naive (challenge Q224); the interval's coverage checked on the holdout |
| **What drives it?** A model whose purpose is explanation, not prediction. | What to change | Feature effects with the correlated-features caveat (Q162); no causal language without a design that supports it |
| **Are these really groups?** Segment customers, products or documents, then test whether the segments mean anything. | Whether to treat the groups differently | Standardization; the number of clusters justified; silhouette reported with its limits; the segments described in words a stakeholder would recognise |

## Project 3 · Something in production (Chapters 43 and 44)

| Framing | The decision | What a reviewer looks for |
|---|---|---|
| **Serve it.** Put project 2's model behind a small interface (a command-line tool, a notebook widget, a minimal web endpoint) with its library versions pinned. | Whether the model can be used by someone who is not you | A clean clone runs it with the steps in the README; the model file and its versions saved together |
| **Would you notice?** Add drift monitoring: the input distribution and the score distribution over time, with a threshold that raises a flag. | When to retrain | Data drift and concept drift distinguished (Q154); a written runbook for what happens when the flag is raised |
| **Explain a decision.** For a model that affects people, produce the explanation a declined applicant is owed (Q161). | Whether the system can be deployed responsibly | Which fairness definition is checked and what it costs under the others (Chapter 44); the limitations stated plainly |
| **Make it reproducible.** Take an earlier project and make every number in its README reproducible from a clean clone, with tests. | Whether the work can be trusted next year | A test that fails when a number changes; pinned versions; seeds; no data files in the repository |

## Turning a framing into a project

1. Write the decision sentence first: who decides what, based on which number, at which threshold.
2. Find data that could answer it. If the data cannot answer it, change the question, not the data.
3. Run the checks in [cheatsheets/checks.md](../cheatsheets/checks.md) before any modelling.
4. Stop at a finding. Write the README with the [template](../templates/README_TEMPLATE.md), finding
   first.
5. Run the [checklist](../templates/PROJECT_CHECKLIST.md). Have someone else read it.

---

<sub>© 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt); see [LICENSING.md](../../LICENSING.md).</sub>
