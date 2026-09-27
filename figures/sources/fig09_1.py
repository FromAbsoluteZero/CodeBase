"""Figure 9.1 - one prediction is a dot product.

Every number is the chapter's own worked example: an order of 18 units across 3 product
lines, each unit worth $12 and each line worth $25, on a base of $20, so
18*12 + 3*25 + 20 = 311. The lower band shows the same operation for all 897 orders at once.
"""
from _style import *
import matplotlib.patches as mp

UNITS, LINES, PPU, PPL, BASE = 18, 3, 12, 25, 20
TOTAL = UNITS * PPU + LINES * PPL + BASE
assert TOTAL == 311

fig, ax = plt.subplots(figsize=(7.60, 3.24))
ax.set_xlim(0, 100); ax.set_ylim(0, 51); ax.axis("off")

def box(x, y, w, h, txt, edge, face="white", bold=True, fs=11.5):
    ax.add_patch(mp.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.6,rounding_size=1.2",
                                   linewidth=1.6, edgecolor=edge, facecolor=face))
    ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center",
            fontsize=fs, fontweight="bold" if bold else "normal", color="#222")

ax.text(0, 46, "ONE PREDICTION", fontsize=10.5, fontweight="bold", color=NAVY)
box(2, 35, 15, 6, str(UNITS), NAVY, TINT)
ax.text(9.5, 33.4, "units", ha="center", va="top", fontsize=9.5, color=SLATE)
box(2, 24, 15, 6, str(PPU), ORANGE)
ax.text(9.5, 22.6, "$/unit", ha="center", va="top", fontsize=9.5, color=SLATE)
ax.text(19.5, 38, "x", ha="center", va="center", fontsize=12, color="#222")

box(24, 35, 15, 6, str(LINES), NAVY, TINT)
ax.text(31.5, 33.4, "lines", ha="center", va="top", fontsize=9.5, color=SLATE)
box(24, 24, 15, 6, str(PPL), ORANGE)
ax.text(31.5, 22.6, "$/line", ha="center", va="top", fontsize=9.5, color=SLATE)
ax.text(41.5, 38, "x", ha="center", va="center", fontsize=12, color="#222")

ax.text(46, 34, "=", ha="center", va="center", fontsize=13, color="#222")
for i, (v, y) in enumerate(((UNITS * PPU, 40), (LINES * PPL, 34), (BASE, 28.5))):
    ax.text(58, y, ("" if i == 0 else "+ ") + f"{v}", ha="right", va="center",
            fontsize=11.5, color="#222")
ax.plot([49, 60], [25.4, 25.4], color="#222", lw=1.2)
box(48, 17.5, 14, 6, f"${TOTAL}", ORANGE, "#FBF3E6")

# the caption sits to the RIGHT of the arithmetic, not on top of it
ax.text(66, 36.5, "x . w + b", fontsize=12, fontweight="bold", color="#222", va="center")
ax.text(66, 32.0, "features times weights,\nsummed, plus a base",
        fontsize=9.5, color=SLATE, va="center")

ax.plot([0, 100], [15.0, 15.0], color=RULE, lw=1.0)
ax.text(0, 12.0, "EVERY PREDICTION", fontsize=10.5, fontweight="bold", color=NAVY)

# The three operands are drawn as GRIDS, not as text boxes: their shapes are what the note
# beside them is about. The original drew them the same way and then printed the labels on
# top of them; here each label sits below its own grid.
def grid(x, y, cols, rows, cw, ch, edge, face, label):
    for r in range(rows):
        for c in range(cols):
            ax.add_patch(mp.Rectangle((x + c * cw, y + (rows - 1 - r) * ch), cw * 0.94, ch * 0.86,
                                      linewidth=1.2, edgecolor=edge, facecolor=face))
    ax.text(x + cols * cw / 2, y - 1.4, label, ha="center", va="top",
            fontsize=10, family="DejaVu Sans Mono", color="#222")

grid(3, 4.0, 2, 3, 5.0, 2.0, NAVY, TINT, "X  (897, 2)")
ax.text(17.5, 6.8, "@", ha="center", va="center", fontsize=13, color=ORANGE)
grid(22, 5.0, 1, 2, 8.0, 2.0, ORANGE, "white", "w  (2,)")
ax.text(35.5, 6.8, "=", ha="center", va="center", fontsize=13, color="#222")
grid(40, 4.0, 1, 3, 8.0, 2.0, NAVY, TINT, "897 predictions")
# the explanation sits clear of every grid and keeps the em dash
ax.text(58, 9.5, "one operation, no loop \u2014\nthe inner dimension 2 is\nconsumed by the summation",
        fontsize=9.5, color=SLATE, va="top")
fig.tight_layout()
save(fig, "fig09_1.png")
