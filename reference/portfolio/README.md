# Building a portfolio that gets read

Appendix B of the book says why three finished projects beat any certificate, what a good project looks
like, and what to avoid. This folder holds what the appendix has no room for: a README template, the
checklist as a file you can copy, and a bank of project framings.

| File | What it is | Licence |
|---|---|---|
| [`../templates/README_TEMPLATE.md`](../templates/README_TEMPLATE.md) | the README skeleton, finding first, for a ninety-second reader | CC0: copy it into your project |
| [`../templates/PROJECT_CHECKLIST.md`](../templates/PROJECT_CHECKLIST.md) | the checklist from Appendix B plus the credential rule from Appendix A | CC0 |
| [`project-ideas.md`](project-ideas.md) | framings for the three projects Chapter 45 asks for, without dataset links | CC BY-NC-SA 4.0 |

## The three projects

Chapter 45 prescribes them, and Appendix B is written to match:

1. **An analysis.** A question someone would act on, a messy file, a defensible answer, and a one-page
   write-up. Chapters 1 to 12.
2. **A model, honestly evaluated.** A baseline, a proper split, a metric that fits the decision, a
   threshold chosen on purpose, and a statement of what the model does not know. Chapters 13 to 29.
3. **Something in production.** The model from project 2, or a simpler one, served behind an interface,
   with monitoring that would notice drift and a note on what you would do when it does. Chapters 43
   and 44.

Three shows range. Beyond three, additional projects add little; below two, a reviewer cannot tell
whether you got lucky.

## The README is the project

Most reviewers read the README and stop. Write it last, write it for someone who will spend ninety
seconds, and lead with the finding rather than the method. The template opens with two sentences that
state the finding and the decision it informs, because that is the part a reviewer is looking for.

## What to avoid

- **The datasets everyone uses.** Titanic, Iris and the Boston housing set signal a completed tutorial.
  So do this book's six datasets: every reader has them, which is the same problem. Use them to
  practise (the exercises do); build your portfolio on data from your own industry, your own
  interests, or a public source nobody else has picked.
- **The unfinished exploration.** Forty cells and no conclusion says you can operate the tools and cannot
  answer a question. Stop at a clear finding with three charts.
- **Claiming causation.** A model that predicts churn does not establish what causes it. Chapter 15
  explains what would license the stronger word.

## Before you show anyone

Run the [project checklist](../templates/PROJECT_CHECKLIST.md). The last item, that somebody who is not
you has read it and understood the conclusion, is the one most often skipped and the one that catches
the most.

---

<sub>© 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt); see [LICENSING.md](../../LICENSING.md).</sub>
