# Errata

Corrections to the printed book, newest first. The book's copyright page and Chapter 45 say corrections
are posted here; this is that page. Each entry names the printing it applies to, the location, what the
text says, and what it should say.

If you find an error, open an issue with the chapter, the page or block, and both versions; see
[CONTRIBUTING.md](../CONTRIBUTING.md).

## Printings

| Printing | Interiors | Notes |
|---|---|---|
| First Edition, second interior (2026-09-24) | Georgia 782 pages, Typography 704 pages, with Appendix C reduced to *Interview practice*, Appendix D renamed *Quick reference*, and the question bank moved to this repository | The current printing. Question numbers Q1 to Q185 in the bank are the numbers of the first interior's Appendix C |
| First Edition, first interior (2026-09) | Georgia 818 pages, Typography 736 pages, with the 185-question bank printed as Appendix C | Superseded before sale; listed so that references to its page numbers can be resolved |

## Corrections

### First interior, corrected in the second interior

These were found while moving the back matter online and are fixed in the current printing. They are
listed for anyone holding a copy of the first interior.

| Location | Was | Now |
|---|---|---|
| Front matter, *The companion repository* | "code/ch01 for Chapter 1" | The code folders start at `code/ch04`; Chapter 1 prints no code. The example now reads `code/ch04 for Chapter 4` |
| Front matter, *The companion repository* | full-resolution figures "from Chapter 16 on" | All 75 figures are in `figures/` |
| Appendix B, *Why three, and why finished* | "one descriptive, one predictive, one comparative" | Aligned with Chapter 45's three projects: an analysis, a model honestly evaluated, and something in production |
| Appendix C, question 133 (now Q133) | Chinchilla was trained on "four times more data" than Gopher | 1.4 trillion tokens against 300 billion is nearly five times |
| Appendix C, callout | headed "the five unanswerable ones", naming none | Removed; the bank marks each question that has no single correct answer |
| Appendix D, pandas, *Filter rows* | "wrap each condition in brackets" | parentheses, as Chapter 4 says |
| Appendix D, pandas, *Avoid the copy warning* | advice written for older pandas | pandas 3, which the book pins, never warns: a filter always returns a copy; assign with `.loc` on the original |
| Appendix D, pandas, *Join* and *Long vs wide* | `merge(..., how="left")` and `pivot_table(...)` | `validate="m:1"` on the merge and an explicit `aggfunc` on the pivot, the two rules Chapter 4 makes |
| Appendix D, SQL, *Window function* | `SUM(x) OVER (PARTITION BY k ORDER BY d)` | with the `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` frame Chapter 5 requires, so ties are not summed together |
| Appendix D, SQL, *Deduplicate* | `ROW_NUMBER() OVER (...) = 1` as if it could be filtered directly | numbered in a CTE and filtered outside it, as Chapter 5 does |
| Appendix E, *Where assistants reliably fail* | official documentation "is linked at the end of every chapter in this book" | The chapters' reading lists do not link library documentation; the text now says to check the library's official documentation for the pinned version |

### Repository

| Location | Was | Now |
|---|---|---|
| `docs/CHAPTER_MAP.md` | Chapter 29 titled "Opening the Model: Interpretability"; Chapter 32 "Convolutional Networks" | The book's titles: "Opening the Model" and "Convolutional Networks and Computer Vision" |

No corrections to the chapters themselves are outstanding.
