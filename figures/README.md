# Figures

The book prints **75** figures and all 75 are here.

**53 are program output**, produced by `code/chNN/figs.py` for chapters 16 to 44.

**22 are diagrams** drawn for the page rather than computed from a dataset. Each has a runnable
script in `sources/`.

Every figure in this directory is rendered at **400 DPI** by the script that produces it. Nothing
is upscaled and no resolution metadata is edited, so the pixels carry real detail. The smallest
file here is 2,194 px wide.

## The 53 generated figures

Each one is produced by its own generator, and the same render is what the book places. Run a
chapter's generator to reproduce its figures:

```bash
cd code/ch30 && python figs.py
```

Eight figures — `fig17_1` `fig20_2` `fig23_1` `fig27_2` `fig28_2` `fig29_1` `fig29_2`
`fig39_1` — contain a step whose result depends on the platform's arithmetic: a t-SNE embedding
settles differently, a tree ensemble breaks a tie in a slightly different place. Re-running them
on your machine can give a marginally different picture. (`fig22_2` used to be a ninth: its decile
binning sorted tied probabilities with an unstable sort. That was fixed before publication with
`kind="stable"` and the figure regenerated, so it now reproduces.) The shape and the point of the figure are
the same. This is the same platform sensitivity `docs/REPRODUCIBILITY.md` records for Chapter 39,
Step 3.

### Printing in black ink

Print-on-demand services convert a black-ink interior to greyscale, and under Rec. 601 this palette
compresses: maroon and green land about 4% of the tonal range apart, green and slate about 5%. Two
solid curves that close together are hard to tell apart on paper.

`code/_greyscale_safe.py` gives every colour its own dash pattern and hatch, so series separate by
pattern rather than by hue. Every `figs.py` imports it, and **it does nothing unless you set
`FAZ_GREYSCALE=1`**:

```bash
python figs.py                      # the figures as the book prints them
FAZ_GREYSCALE=1 python figs.py      # dash patterns, for a black-ink printing
```

It is off by default because the switch changes 44 of the 53 generated figures, and the colour
versions are the ones the book prints. Turn it on if you are printing the figures yourself.

Figures 10.1 and 15.1 are the exception: each plots three series whose colours converge to within
about 8% in tone once printed in black ink, and in both the legend is the only key to which curve
is which. Both give every series its own dash pattern unconditionally, in their own source, and the
legend swatches carry the pattern.

## The 22 diagram sources

Chapters 1 to 16 and Chapter 42 carry diagrams that illustrate an idea rather than plot a dataset.
Each has a script in `sources/` that draws it at 400 DPI, and where a diagram carries a number, the
script computes that number from the book's own data and asserts it.

| Script | Figure | Where its numbers come from |
|---|---|---|
| `fig01_1.py` `fig01_2.py` `fig01_3.py` | 1.1 1.2 1.3 | The diagram's own wording and percentages, which sum to 100 (asserted). |
| `fig02_1.py` `fig02_2.py` | 2.1 2.2 | Chapter 2's traceback and steps. |
| `fig03_1.py` | 3.1 | Chapter 3's prices, indices and dictionary. |
| `fig04_1.py` | 4.1 | Chapter 3's three dictionaries and Chapter 4's frame. |
| `fig05_1.py` | 5.1 | The six SQL clauses; `RUNS.index("SELECT") == 4` is asserted. |
| `fig06_1.py` | 6.1 | Computed from `data/generated/retail.csv`: 897 orders, mean $239, fence $655, 14 beyond it. |
| `fig07_1.py` | 7.1 | Chapter 7's own sampling loop, seed 0, 5,000 draws at n = 1, 5, 30. |
| `fig08_1.py` | 8.1 | Chapter 8's own proportion test. |
| `fig09_1.py` | 9.1 | Chapter 9's worked example: 18×12 + 3×25 + 20 = 311, asserted. |
| `fig10_1.py` | 10.1 | Chapter 10's own `run(eta, steps)` on the standardized order data. |
| `fig11_1.py` | 11.1 | Chapter 11's wording. |
| `fig12_1.py` | 12.1 | Chapter 12's five cards and the zero-baseline rule. |
| `fig12_2.py` | 12.2 | Twelve monthly revenues summed from `retail.csv`, so both panels plot identical numbers by construction. |
| `fig12_3.py` | 12.3 | The same table pivoted by `Category`. |
| `fig13_1.py` | 13.1 | Chapter 13's own two-predictor fit; the $50 / $86 / $123 bars are asserted. |
| `fig14_1.py` | 14.1 | Chapter 14's own logistic model, same split and scaler; the 6% recall at threshold 0.5 is asserted. |
| `fig15_1.py` | 15.1 | Chapter 15's own `power_at()`. |
| `fig16_1.py` | 16.1 | A 70/30 split and a five-fold grid; `TRAIN + TEST == 100` is asserted. |
| `fig42_1.py` | 42.1 | Chapter 42's two structures. |

Run them from this directory:

```bash
cd sources && python fig06_1.py
```

`sources/_style.py` carries the palette, the type and the drawing primitives, and matches the style
the chapter generators use so a diagram sits beside a generated figure without looking different.
`sources/_data.py` builds the order table exactly as chapters 6 to 10 build it.
