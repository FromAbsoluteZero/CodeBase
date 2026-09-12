"""Figure 4.1 - a DataFrame is a list of dictionaries with an index attached.

The three rows are the chapter's own example values.
"""
from _style import *
import matplotlib.patches as mp

# A DataFrame built from that list of dictionaries carries a fresh RangeIndex, so the
# index column reads 0, 1, 2 -- as it does in the chapter. The
# note below the table is about what happens LATER, after a filter, and must not be
# smuggled into the table itself.
ROWS = [(0, 3, "31.00", "Netherlands"),
        (1, 4, "12.50", "Netherlands"),
        (2, 11, "24.00", "Netherlands")]

fig, ax = plt.subplots(figsize=(7.60, 3.24))
ax.set_xlim(0, 100); ax.set_ylim(0, 62); ax.axis("off")

ax.text(0, 59.5, "THE SAME TABLE, TWO WAYS", fontsize=11, fontweight="bold", color=NAVY)
ax.text(0, 55, "Chapter 3: a list of dictionaries", fontsize=10, style="italic", color=SLATE)
for i, (q, up) in enumerate((("3", "31.00"), ("4", "12.50"), ("11", "24.00"))):
    ax.text(2, 50.5 - i * 4.0, '{"Quantity": %s, "UnitPrice": %s, ...}' % (q, up),
            fontsize=10, family="DejaVu Sans Mono", color="#222")

ax.annotate("", xy=(24, 39.8), xytext=(24, 34.6),
            arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.4,
                            mutation_scale=20, shrinkA=0, shrinkB=0))
ax.text(27, 37, "same data, stored by column", fontsize=10, fontweight="bold", color=ORANGE,
        va="center")

ax.text(0, 32, "Chapter 4: a DataFrame", fontsize=10, style="italic", color=SLATE)
COLS = [("index", 2, 13), ("Quantity", 15, 20), ("UnitPrice", 35, 20), ("Country", 55, 26)]
HDR_Y, ROW_H = 24.5, 4.6
for name, x, w in COLS:
    ax.add_patch(mp.Rectangle((x, HDR_Y), w, ROW_H, facecolor=NAVY, edgecolor="white", lw=1.2))
    ax.text(x + w / 2, HDR_Y + ROW_H / 2, name, ha="center", va="center",
            fontsize=9.5, fontweight="bold", color="white")
for r, (idx, q, up, ctry) in enumerate(ROWS):
    y = HDR_Y - (r + 1) * ROW_H
    vals = [str(idx), str(q), up, ctry]
    for (name, x, w), v in zip(COLS, vals):
        ax.add_patch(mp.Rectangle((x, y), w, ROW_H, facecolor="white",
                                  edgecolor=RULE, lw=0.9))
        ax.text(x + w / 2, y + ROW_H / 2, v, ha="center", va="center", fontsize=9.5,
                color=ORANGE if name == "index" else "#222")
# the short orange accent rule beside the index column, tying it to the
# orange note below
ax.plot([1.2, 1.2], [HDR_Y - len(ROWS) * ROW_H, HDR_Y], color=ORANGE, lw=2.6,
        solid_capstyle="butt")
# the two explanations now sit BELOW the table, each under what it describes
ax.text(2, 1.0, "the INDEX labels each row and survives\n"
                "filtering, so a filtered frame may run\n0, 3, 7, 11",
        fontsize=9, color=ORANGE, va="bottom", linespacing=1.35)
ax.text(52, 1.0, "each COLUMN is a Series of one type;\n"
                 "operations run on whole columns\nat once",
        fontsize=9, color=SLATE, va="bottom", linespacing=1.35)
fig.tight_layout()
save(fig, "fig04_1.png")
