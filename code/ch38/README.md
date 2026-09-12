# Chapter 38 — Retrieval (RAG)

Companion code for Chapter 38 of *From Absolute Zero*.

## What is here

| File | What it is |
|---|---|
| `gen_docs.py` | the printed block that creates `policy.md` |
| `_lib.py` | shared setup: the imports and objects the printed blocks assume, which the book shows once at the start of the session |
| `c1.py` | `import re` |
| `c2.py` | `# Ten questions, with the index of the chunk that answers each.` |
| `c3.py` | `from sklearn.feature_extraction.text import TfidfVectorizer` |
| `gen_tickets.py` | the printed block that creates `tickets.txt` |
| `c4.py` | `from collections import Counter` |
| `c5.py` | `import re` |
| `c6.py` | `# A retriever always returns its top k, even when the answer is absent.` |
| `figs.py` | regenerates `fig38_1.png` |

**6 printed blocks** (`c1.py` … `c6.py`), in the order the book prints them.

## Running it

The blocks are fragments of **one continuing session**, exactly as the book presents them: later
blocks use variables defined by earlier ones, and the imports and shared objects live in
`_lib.py`. They are not standalone scripts — `python c1.py` on its own stops with a `NameError`.
Run them in order, from this directory:

```bash
python -c "for f in ['gen_docs.py', '_lib.py', 'c1.py', 'c2.py', 'c3.py', 'gen_tickets.py', 'c4.py', 'c5.py', 'c6.py']: exec(open(f, encoding='utf-8').read())"
```

To stop after a particular block, shorten the list. Each block's output appears in the order the
book prints it.

## Data

`policy.md` and `tickets.txt` are written by the chapter's own blocks (`gen_docs.py`, Step 1, and
`gen_tickets.py`, Step 5), which the command above runs in their printed places. If you skip one,
`_lib.py` writes the missing file so the later blocks still run (Step 5's file quietly, so its
`wrote tickets.txt` line appears only where the book prints it).

## Figures

```bash
python figs.py
```

Writes `fig38_1.png` into this directory (the shipped versions are in `figures/`).

## Reproducibility

Every block is explicitly seeded. At the versions pinned in `requirements.txt` the output
should match the book digit for digit.
See `docs/REPRODUCIBILITY.md` if a number does not match.
