"""Figure 42.1 - the academic order against the pyramid.

The five academic stages, "readers stop here", the RECOMMENDATION / impact / evidence /
risks pyramid and its six detail boxes are the diagram's.
"""
from _style import *

STAGES = ["background", "method", "results", "discussion"]

fig, ax = blank((7.60, 3.24), 100, 50)

label(ax, 2.0, 47.5, "ACADEMIC  —  builds to the conclusion", fs=10.5, bold=True,
      color=RED, ha="left")
BW, BG, X0, BY, BH = 18.0, 1.2, 2.0, 38.0, 6.2
for i, s in enumerate(STAGES):
    x = X0 + i * (BW + BG)
    rbox(ax, x, BY, BW, BH, edge="#C8CED8", face="white", lw=1.4, r=1.0)
    label(ax, x + BW / 2, BY + BH / 2, s, fs=10, color=SLATE)
    arrow(ax, x + BW + 0.15, BY + BH / 2, x + BW + BG - 0.15, BY + BH / 2,
          color=RULE, lw=1.3, scale=10)
x = X0 + 4 * (BW + BG)
rbox(ax, x, BY, BW, BH, edge="#B0521F", face="#FBF3E6", lw=1.8, r=1.0)
label(ax, x + BW / 2, BY + BH / 2, "CONCLUSION", fs=10, bold=True, color="#B0521F")
arrow(ax, 27.0, 34.0, 27.0, 37.6, color=RED, lw=1.5, scale=12)
label(ax, 27.0, 32.0, "readers stop here", fs=10, bold=True, color=RED, va="top")

rule(ax, 2.0, 98.0, 27.0, color="#C8CED8", lw=1.4)

label(ax, 2.0, 24.0, "PYRAMID  —  answer first, everything below optional",
      fs=10.5, bold=True, color=GREEN, ha="left")
# the note now lives BELOW the rule instead of astride it
label(ax, 98.0, 20.5, "a reader who stops\nafter one line still\nhas the answer",
      fs=9.5, bold=True, color=GREEN, ha="right", va="center")

rbox(ax, 26.0, 15.0, 48.0, 6.4, edge="#B0521F", face="#FBF3E6", lw=1.8, r=1.1)
label(ax, 50.0, 18.2, "RECOMMENDATION", fs=11.5, bold=True, color="#B0521F")

MID = [("impact", 2.0), ("evidence", 32.0), ("risks", 62.0)]
for name, x in MID:
    rbox(ax, x, 6.6, 26.0, 5.6, edge=NAVY, face=TINT, lw=1.8, r=1.0)
    label(ax, x + 13.0, 9.4, name, fs=10, color=NAVY)
    arrow(ax, 50.0, 14.8, x + 13.0, 12.4, color=NAVY, lw=1.4, scale=12)

for i in range(6):
    x = 2.0 + i * 16.0
    rbox(ax, x, 0.8, 14.0, 4.0, edge="#D6DCE5", face="white", lw=1.1, r=0.8)
    label(ax, x + 7.0, 2.8, "detail", fs=9, color=SLATE)
save(fig, "fig42_1.png")
