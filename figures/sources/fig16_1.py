"""Figure 16.1 - the three-way split at 400 DPI.

Everything else -- the 70/30 split, the labels, "opened once, at the end" -- is the diagram's.
"""
from _style import *

TRAIN_PCT, TEST_PCT, K = 70, 30, 5
assert TRAIN_PCT + TEST_PCT == 100

fig, ax = blank((7.10, 2.80), 100, 50)

label(ax, 1.5, 47.5, "ALL AVAILABLE DATA", fs=9.5, bold=True, color=SLATE, ha="left")
rbox(ax, 1.5, 39.0, 68.0, 7.0, edge=NAVY, face=TINT, lw=1.8, r=1.0)
label(ax, 35.5, 42.5, f"TRAINING  ({TRAIN_PCT}%)", fs=11, bold=True, color=NAVY)
rbox(ax, 72.5, 39.0, 26.0, 7.0, edge=RED, face="#F7EAEA", lw=1.8, r=1.0)
label(ax, 85.5, 42.5, f"TEST  ({TEST_PCT}%)", fs=11, bold=True, color=RED)
ax.plot([35.5, 35.5], [37.4, 38.9], color=SLATE, lw=1.0)

label(ax, 1.5, 34.0, "CROSS-VALIDATION INSIDE THE TRAINING PORTION",
      fs=9.5, bold=True, color=SLATE, ha="left")

CW, CG, CH, RG, X0, TOP = 12.6, 1.2, 4.6, 1.0, 1.5, 30.0
for r in range(K):
    y = TOP - (r + 1) * (CH + RG)
    for c in range(K):
        x = X0 + c * (CW + CG)
        val = (c == r)
        rbox(ax, x, y, CW, CH, edge=GREEN if val else NAVY,
             face="#DCEBE1" if val else TINT, lw=1.4, r=0.7)
        label(ax, x + CW / 2, y + CH / 2, "validate" if val else "train",
              fs=8.2, bold=True, color=GREEN if val else NAVY)

label(ax, 73.0, 21.0, f"{K} scores\nmean +/- sd", fs=9.5, color=GREEN, ha="left", va="center")
arrow(ax, 82.0, 3.0, 88.5, 38.5, color=RED, lw=1.5, scale=13, style="->",
      conn="arc3,rad=0.30")
label(ax, 73.0, 1.5, "opened once, at the end", fs=9.5, color=RED, ha="left", va="center")
save(fig, "fig16_1.png")
