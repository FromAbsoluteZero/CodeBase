# Contributing

This is a companion repository to a book, not an evolving software project. The most valuable
contribution is telling me where the book is wrong.

## Most useful: report a number that does not match

The book's central claim is that every printed number came from executing the code. If you run a
chapter at the pinned versions in `requirements.txt` and get a different number, that is a defect
and I want to know.

Please include:

- chapter and code block (e.g. `code/ch30/c4.py`)
- the number printed in the book
- the number you got
- output of `pip freeze` (or at least numpy, pandas, scikit-learn versions)
- your Python version and OS

Before reporting, check `docs/REPRODUCIBILITY.md` — some chapters are expected to reproduce
approximately rather than exactly.

## Also useful

- **Errors in the text** — technical, mathematical or otherwise
- **Broken instructions** — a command in the docs that does not work as written
- **Ambiguity** — a passage a careful reader could reasonably misread

## Less useful

- Restyling code that already runs and matches the book
- Modernising APIs — the pinned versions exist to reproduce the printed output, not to be current
- Replacing the pure-NumPy implementations with a framework — that is the pedagogical point

## Pull requests

Small, focused changes with a clear description of what was wrong. If a change would alter a number
printed in the book, say so explicitly in the PR — that has consequences beyond the repository.
