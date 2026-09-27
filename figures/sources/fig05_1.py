"""Figure 5.1 - SQL's written order against its execution order.

Both six-clause lists, their glosses, the "written 1st, runs 5th" leader and the closing
sentence are the diagram's.
"""
from _style import *

WRITTEN = [("SELECT", "what you want"), ("FROM", "which table"), ("WHERE", "which rows"),
           ("GROUP BY", "what to collapse on"), ("HAVING", "which groups survive"),
           ("ORDER BY", "how to sort")]
RUNS = ["FROM", "WHERE", "GROUP BY", "HAVING", "SELECT", "ORDER BY"]
assert RUNS.index("SELECT") == 4          # written first, runs fifth

fig, ax = blank((7.60, 3.133), 100, 50)
label(ax, 24, 47.0, "WRITTEN ORDER", fs=11, bold=True, color=SLATE)
label(ax, 76, 47.0, "EXECUTION ORDER", fs=11, bold=True, color="#B0521F")

H, GAP, TOP = 5.2, 0.9, 42.0
for i, (k, g) in enumerate(WRITTEN):
    y = TOP - (i + 1) * (H + GAP)
    hot = (k == "SELECT")
    rbox(ax, 4, y, 40, H, edge="#B0521F" if hot else NAVY,
         face="#FBF3E6" if hot else TINT, lw=1.5, r=0.9)
    label(ax, 6.5, y + H / 2, k, fs=10, bold=True, color="#B0521F" if hot else NAVY, ha="left")
    label(ax, 21, y + H / 2, g, fs=9.5, color=SLATE, ha="left")

for i, k in enumerate(RUNS):
    y = TOP - (i + 1) * (H + GAP)
    hot = (k == "SELECT")
    rbox(ax, 55, y, 42, H, edge="#B0521F" if hot else NAVY,
         face="#FBF3E6" if hot else "white", lw=1.5, r=0.9)
    rbox(ax, 56.2, y + 0.6, 6.4, H - 1.2, edge="#B0521F" if hot else NAVY,
         face="#B0521F" if hot else "#1F3A5F", lw=0.5, r=0.6)
    label(ax, 59.4, y + H / 2, str(i + 1), fs=9.5, bold=True, color="white")
    label(ax, 64.5, y + H / 2, k, fs=10, bold=True, color="#B0521F" if hot else NAVY, ha="left")

# The leader label sits in the gutter ABOVE the curve rather than on it, so the dashed
# curve cannot strike through "written 1st, runs 5th".
arrow(ax, 44.5, TOP - H / 2 - 0.9, 54.6, TOP - 5 * (H + GAP) + H / 2, color="#B0521F",
      lw=1.8, scale=15, style="->", conn="arc3,rad=-0.30")
label(ax, 49.5, 45.0, "written 1st,\nruns 5th", fs=9.5, bold=True, color="#B0521F")

label(ax, 4, 1.4, "This is why a column alias created in SELECT cannot be used in WHERE "
                  "— it does not exist yet.", fs=10, italic=True, color=NAVY, ha="left")
save(fig, "fig05_1.png")
