"""Figure 11.1 - where leakage enters.

Both rows, their box labels, the two right-hand verdicts and the closing Pipeline note are
the diagram's wording.
"""
from _style import *

fig, ax = blank((7.60, 3.24), 100, 50)

label(ax, 3, 47.0, "WRONG  —  the statistic is computed before the split",
      fs=11, bold=True, color=RED, ha="left")
rbox(ax, 3, 35.5, 26, 7.6, edge=NAVY, face=TINT, lw=1.8, r=1.1)
label(ax, 16, 39.3, "all the data", fs=10.5, bold=True, color=NAVY)
arrow(ax, 29.5, 39.3, 33.5, 39.3, color=RED, lw=1.8, scale=14)
rbox(ax, 34, 35.5, 30, 7.6, edge=RED, face="#F7EAEA", lw=1.8, r=1.1)
label(ax, 49, 39.3, "compute mean / scale /\ncategory average", fs=9.5, color="#222")
arrow(ax, 64.5, 39.3, 68.5, 41.6, color=RED, lw=1.6, scale=12)
arrow(ax, 64.5, 39.3, 68.5, 36.8, color=RED, lw=1.6, scale=12)
rbox(ax, 69, 40.0, 16, 4.4, edge="#C8CED8", face="white", lw=1.2, r=0.8)
label(ax, 77, 42.2, "train", fs=9.5, color="#222")
rbox(ax, 69, 34.6, 16, 4.4, edge=RED, face="white", lw=1.4, r=0.8)
label(ax, 77, 36.8, "test", fs=9.5, color="#222")
label(ax, 86.5, 39.3, "the test rows\nhelped compute it", fs=9.5, bold=True, color=RED, ha="left")

rule(ax, 3, 97, 31.0, color="#D6DCE5", lw=1.4)

label(ax, 3, 27.5, "RIGHT  —  split first, fit the transformation on training only",
      fs=11, bold=True, color=GREEN, ha="left")
rbox(ax, 3, 15.5, 26, 7.6, edge=NAVY, face=TINT, lw=1.8, r=1.1)
label(ax, 16, 19.3, "all the data", fs=10.5, bold=True, color=NAVY)
arrow(ax, 29.5, 19.8, 33.5, 22.4, color=GREEN, lw=1.6, scale=13)
arrow(ax, 29.5, 18.8, 33.5, 16.2, color=SLATE, lw=1.6, scale=13)
rbox(ax, 34, 20.4, 22, 4.6, edge=GREEN, face="white", lw=1.5, r=0.8)
label(ax, 45, 22.7, "train", fs=9.5, color="#222")
rbox(ax, 34, 13.6, 22, 4.6, edge="#C8CED8", face="white", lw=1.2, r=0.8)
label(ax, 45, 15.9, "test", fs=9.5, color=SLATE)
arrow(ax, 56.5, 22.7, 61.5, 22.7, color=GREEN, lw=1.6, scale=13)
rbox(ax, 62, 20.4, 28, 4.6, edge=GREEN, face="#E9F1EC", lw=1.5, r=0.8)
label(ax, 76, 22.7, "fit statistic HERE only", fs=9.5, color="#222")
rbox(ax, 62, 13.6, 28, 4.6, edge="#C8CED8", face="white", lw=1.2, r=0.8)
label(ax, 76, 15.9, "apply it, unchanged", fs=9.5, color=SLATE)
arrow(ax, 76, 20.2, 76, 18.3, color=GREEN, lw=1.3, scale=11, conn="arc3,rad=0.45")
label(ax, 91, 19.3, "the test rows\nnever contributed", fs=9.5, bold=True, color=GREEN, ha="left")

rbox(ax, 3, 1.0, 94, 8.4, edge="#B0521F", face="#FBF3E6", lw=1.7, r=1.2)
label(ax, 50, 6.9, "A Pipeline does this by construction: fit() sees only the training fold,",
      fs=10.5, bold=True, color="#B0521F")
label(ax, 50, 3.4, "so cross-validation refits every transformation inside every fold automatically.",
      fs=10.5, bold=True, color="#B0521F")
save(fig, "fig11_1.png")
