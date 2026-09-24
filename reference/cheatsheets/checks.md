# The checks worth running every time

Also printed in the book's Quick Reference (Appendix D). Copy them into a notebook's first cell.

- [ ] What does one row represent? (the grain, Chapter 4)
- [ ] Shape, head, dtypes, missing values, extremes (Chapter 11)
- [ ] Row count before and after every join (Chapter 4)
- [ ] Does the total match a figure somebody else already has? (Chapter 1)
- [ ] Is the median far from the mean, and if so which am I reporting? (Chapter 6)
- [ ] Was anything fitted before the train-test split? (Chapter 16)
- [ ] Is there a baseline, and does the result beat it? (Chapter 16)
- [ ] Would this result change the decision, and by how much? (Chapter 1)

The pandas exercise [Q196](../../practice/by-topic/python-pandas-data.md#q196) turns the first three into
a function you can keep.

---

<sub>© 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt); see [LICENSING.md](../../LICENSING.md). Corrections: [docs/ERRATA.md](../../docs/ERRATA.md). Every snippet was checked against the versions pinned in `requirements.txt` (pandas 3.0.2, scikit-learn 1.8.0).</sub>
