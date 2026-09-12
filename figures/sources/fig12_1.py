"""Figure 12.1 - five questions, five chart types.

The five cards and the zero-baseline rule beneath them keep the diagram's wording.
"""
from _style import *

CARDS = [("DISTRIBUTION", "how is it spread?", "histogram\nboxplot"),
         ("COMPARISON", "which is biggest?", "sorted bar\n(start at zero)"),
         ("CHANGE", "is it growing?", "line\n(zero optional)"),
         ("RELATIONSHIP", "do they move together?", "scatterplot"),
         ("COMPOSITION", "what are the parts?", "stacked bar\n(not a pie)")]

fig, ax = blank((7.60, 2.927), 100, 50)
W, GAP, X0, Y0, H = 18.4, 1.0, 2.0, 26.0, 21.0
for i, (head, q, rec) in enumerate(CARDS):
    x = X0 + i * (W + GAP)
    rbox(ax, x, Y0, W, H, edge="#C8CED8", face="white", lw=1.4, r=1.2)
    label(ax, x + W / 2, Y0 + H - 4.0, head, fs=9.8, bold=True, color=NAVY)
    label(ax, x + W / 2, Y0 + H - 8.2, q, fs=8.1, italic=True, color=SLATE)
    rbox(ax, x + 1.4, Y0 + 2.2, W - 2.8, 8.4, edge="#B0521F", face="#FBF3E6", lw=1.5, r=1.0)
    label(ax, x + W / 2, Y0 + 6.4, rec, fs=9.2, bold=True, color="#B0521F", mono=True)

rule(ax, 2, 98, 22.0, color="#D6DCE5", lw=1.4)
label(ax, 2, 18.0, "THE ZERO-BASELINE RULE", fs=10.5, bold=True, color=NAVY, ha="left")

rbox(ax, 2, 1.5, 45, 13.0, edge=GREEN, face="#E9F1EC", lw=1.6, r=1.1)
label(ax, 24.5, 8.0, "BARS must start at zero\nlength encodes the value, so a cut\n"
                     "baseline multiplies the difference", fs=9.8, color=GREEN)
rbox(ax, 52, 1.5, 46, 13.0, edge=NAVY, face=TINT, lw=1.6, r=1.1)
label(ax, 75, 8.0, "LINES need not\nslope encodes change, so forcing zero\n"
                   "can flatten a real movement to nothing", fs=9.8, color=NAVY)
save(fig, "fig12_1.png")
