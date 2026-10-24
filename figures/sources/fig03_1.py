"""Figure 3.1 - a list is reached by position, a dictionary by name.

The four prices (4.80, 4.25, 5.10, 2.75), both index rows, the four dictionary keys and
their values, and every code line beside them are the diagram's.
"""
from _style import *

PRICES = ["4.80", "4.25", "5.10", "2.75"]
DRINK = [("name", "Cold Brew"), ("price", "4.80"), ("cost", "1.35"), ("units", "1240")]

fig, ax = blank((7.60, 3.24), 100, 50)

label(ax, 2.5, 47.0, "LIST — reached by position", fs=10.5, bold=True, color=NAVY, ha="left")
BW, BG, BX, BY, BH = 10.0, 1.4, 2.5, 36.0, 6.2
for i, p in enumerate(PRICES):
    x = BX + i * (BW + BG)
    rbox(ax, x, BY, BW, BH, edge=NAVY, face=TINT, lw=1.7, r=1.0)
    label(ax, x + BW / 2, BY + BH / 2, p, fs=10.5, color="#222")
    label(ax, x + BW / 2, BY - 2.2, str(i), fs=10, bold=True, color="#B0521F")
    label(ax, x + BW / 2, BY - 5.4, str(i - 4), fs=9, color=SLATE)

CODE = [("prices[1]  ->  4.25", NAVY), ("prices[-1] ->  2.75", NAVY),
        ("prices[0:2] -> [4.80, 4.25]   (end excluded)", "#B0521F")]
for i, (t, c) in enumerate(CODE):
    label(ax, 48, 41.6 - i * 3.4, t, fs=10, color=c, mono=True, ha="left")

rule(ax, 2.5, 97, 28.5, color="#D6DCE5", lw=1.4)
label(ax, 2.5, 25.5, "DICTIONARY — reached by name", fs=10.5, bold=True, color=NAVY, ha="left")
KW, VW, RH, GAP, KX = 15.5, 25.0, 4.4, 0.9, 2.5
for i, (k, v) in enumerate(DRINK):
    y = 20.0 - i * (RH + GAP)
    rbox(ax, KX, y, KW, RH, edge="#B0521F", face="#B0521F", lw=0.5, r=0.6)
    label(ax, KX + KW / 2, y + RH / 2, k, fs=10, bold=True, color="white")
    rbox(ax, KX + KW + 0.5, y, VW, RH, edge="#C8CED8", face="white", lw=1.2, r=0.6)
    label(ax, KX + KW + 0.5 + VW / 2, y + RH / 2, v, fs=10, color="#222")

label(ax, 48, 19.5, 'drink["price"]  ->  4.80', fs=10, color=NAVY, mono=True, ha="left")
label(ax, 48, 15.5, 'drink.get("size", "unknown")', fs=10, color=NAVY, mono=True, ha="left")
label(ax, 52, 12.0, "-> no KeyError if it is missing", fs=9.5, color="#B0521F", mono=True, ha="left")
rbox(ax, 47, 1.5, 50, 8.0, edge="#B0521F", face="#FBF3E6", lw=1.7, r=1.1)
label(ax, 72, 7.0, "A LIST OF DICTIONARIES IS A TABLE", fs=10.5, bold=True, color="#B0521F")
label(ax, 72, 3.7, "one dictionary per row, one key per column", fs=10.5, bold=True, color="#B0521F")
save(fig, "fig03_1.png")
