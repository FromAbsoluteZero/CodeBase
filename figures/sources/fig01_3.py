"""Figure 1.3 - the framing brief. Five labelled rows and the closing band,
with the diagram's wording preserved exactly.
"""
from _style import *

ROWS = [("THE DECISION",   "reverse the June price rise, or leave it — by the 21st"),
        ("THE METRIC",     "category revenue, retail orders only, March to September"),
        ("THE COMPARISON", "affected category vs. categories with no price change"),
        ("THE THRESHOLD",  "a gap of more than a few points changes the decision"),
        ("THE RIVALS",     "competitor promotion; supply shortage — both must be ruled out")]

fig, ax = blank((7.60, 3.133), 100, 50)
label(ax, 50, 47.5, 'Half a page that turns "revenue is down, can you look into it" into a project',
      fs=10.5, italic=True, color=SLATE)

LW, RX, RW, H, GAP = 26.0, 29.5, 69.0, 6.0, 1.0
top = 44.0
for i, (k, v) in enumerate(ROWS):
    y = top - (i + 1) * (H + GAP)
    rbox(ax, 1.0, y, LW, H, edge=NAVY, face=TINT, lw=1.7, r=1.1)
    label(ax, 1.0 + LW / 2, y + H / 2, k, fs=10, bold=True, color=NAVY)
    rbox(ax, RX, y, RW, H, edge="#C8CED8", face="white", lw=1.3, r=1.1)
    label(ax, RX + RW / 2, y + H / 2, v, fs=10, color=SLATE)
y = top - 6 * (H + GAP)
rbox(ax, 1.0, y, RX + RW - 1.0, H, edge="#B0521F", face="#FBF3E6", lw=1.7, r=1.1)
label(ax, (1.0 + RX + RW) / 2, y + H / 2, "agreed with the requester BEFORE any data is pulled",
      fs=10.5, bold=True, color="#B0521F")
save(fig, "fig01_3.png")
