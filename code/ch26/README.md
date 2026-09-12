# Chapter 26 — Clustering

Companion code for Chapter 26 of *From Absolute Zero*.

## What is here

| File | What it is |
|---|---|
| `gen_seg.py` | the printed block that creates `segments.csv` |
| `_lib.py` | shared setup: the imports and objects the printed blocks assume, which the book shows once at the start of the session |
| `c1.py` | `# Scaling is not optional here. k-means minimizes squared distance, so a` |
| `c2.py` | `# Choosing k. Inertia always falls, so it cannot pick k on its own.` |
| `c3.py` | `# Three algorithms, same data, same scaling.` |
| `c4.py` | `# DBSCAN has no k, but it has eps -- and it is far more sensitive to eps` |
| `c5.py` | `# k-means assumes clusters are round blobs of similar size. When they are` |
| `c6.py` | `# The deliverable is not the labels. It is the profile.` |
| `figs.py` | regenerates `fig26_1.png`, `fig26_2.png` |

**6 printed blocks** (`c1.py` … `c6.py`), in the order the book prints them.

## Running it

The blocks are fragments of **one continuing session**, exactly as the book presents them: later
blocks use variables defined by earlier ones, and the imports and shared objects live in
`_lib.py`. They are not standalone scripts — `python c1.py` on its own stops with a `NameError`.
Run them in order, from this directory:

```bash
python -c "for f in ['gen_seg.py', '_lib.py', 'c1.py', 'c2.py', 'c3.py', 'c4.py', 'c5.py', 'c6.py']: exec(open(f, encoding='utf-8').read())"
```

To stop after a particular block, shorten the list. Each block's output appears in the order the
book prints it.

## Data

`segments.csv` is created by this chapter's Step 1, `gen_seg.py`, which the command above runs first.
A byte-identical copy ships in `data/generated/segments.csv`; `_lib.py` falls back to it if the file is
not in this directory.

## Figures

```bash
python figs.py
```

Writes `fig26_1.png`, `fig26_2.png` into this directory (the shipped versions are in `figures/`).

## Reproducibility

Every block is explicitly seeded. At the versions pinned in `requirements.txt` the output
should match the book digit for digit.
See `docs/REPRODUCIBILITY.md` if a number does not match.
