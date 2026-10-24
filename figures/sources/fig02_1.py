"""Figure 2.1 - assignment read as an instruction at 400 DPI.

The heading, both boxes, the "store" and "evaluated FIRST" labels and the three numbered
steps are the diagram's wording.
"""
from _style import *

fig, ax = blank((7.60, 2.927), 100, 40)

label(ax, 19, 37, "count = count + 1", fs=11.5, bold=True, color=NAVY)
label(ax, 61, 37, "read as an instruction, not as algebra", fs=11.5, bold=True, color=NAVY)

rbox(ax, 6, 22.5, 25, 8.0, edge=NAVY, face=TINT, lw=1.8, r=1.3)
label(ax, 18.5, 26.5, "count", fs=12.5, bold=True, color=NAVY)
label(ax, 18.5, 20.3, "the NAME on the left", fs=9.5, color=SLATE, va="top")

rbox(ax, 42, 22.5, 24, 8.0, edge=NAVY, face="white", lw=1.8, r=1.3)
label(ax, 54, 26.5, "count + 1", fs=12.5, color=NAVY)
label(ax, 54, 20.3, "the EXPRESSION on the right", fs=9.5, color=SLATE, va="top")

arrow(ax, 41.5, 26.5, 31.5, 26.5, color="#B0521F", lw=2.6, scale=20)
label(ax, 36.5, 29.3, "=", fs=13, bold=True, color="#B0521F")
label(ax, 36.5, 22.6, "store", fs=9.5, italic=True, color="#B0521F")

arrow(ax, 78, 26.5, 66.5, 26.5, color="#B0521F", lw=2.6, scale=20)
label(ax, 80, 28.6, "evaluated", fs=10, bold=True, color="#B0521F", ha="left")
label(ax, 80, 24.6, "FIRST", fs=10, bold=True, color="#B0521F", ha="left")

rule(ax, 4, 96, 16.0, color="#D6DCE5", lw=1.4)

STEPS = ["Python evaluates the right-hand side",
         "That produces a value, say 7",
         "The name on the left is attached to it"]
for i, s in enumerate(STEPS):
    y = 11.0 - i * 4.6
    rbox(ax, 6, y, 6.2, 3.4, edge="#B0521F", face="#B0521F", lw=0.5, r=0.7)
    label(ax, 9.1, y + 1.7, str(i + 1), fs=10, bold=True, color="white")
    label(ax, 16, y + 1.7, s, fs=10.5, color="#222", ha="left")
save(fig, "fig02_1.png")
