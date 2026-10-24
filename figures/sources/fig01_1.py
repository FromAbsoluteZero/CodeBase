"""Figure 1.1 - the four kinds of analytics at 400 DPI.

Every box, question, worked example and the arrow legend belong to the diagram. The four
percentages sum to 100, which the assertion below holds the drawing to.
"""
from _style import *

fig, ax = blank((7.60, 3.24), 100, 50)

CARDS = [("DESCRIPTIVE", "What happened?", "revenue fell 8%\nlast quarter", GREEN, TINT),
         ("DIAGNOSTIC", "Why did it happen?", "concentrated in one\nregion after a price change", SLATE, "white"),
         ("PREDICTIVE", "What happens next?", "another 3% fall\nif trends hold", ORANGE, "white"),
         ("PRESCRIPTIVE", "What should we do?", "reverse the price change\nin that region", RED, "#FBF3E6")]

label(ax, 50, 47.5, "Naming the family tells you which tools you need before you open the data",
      fs=10.5, color=SLATE, italic=True)

W, GAP, X0, Y0, H = 23.2, 1.4, 0.6, 15.0, 27.0
for i, (head, q, ex, edge, face) in enumerate(CARDS):
    x = X0 + i * (W + GAP)
    rbox(ax, x, Y0, W, H, edge=edge, face=face, lw=1.8, r=1.4)
    label(ax, x + W / 2, Y0 + H - 4.6, head, fs=11.5, bold=True, color=edge)
    label(ax, x + W / 2, Y0 + H - 10.2, q, fs=10, italic=True, color=NAVY)
    label(ax, x + W / 2, Y0 + 7.6, ex, fs=8.8, color=SLATE)
    if i < 3:
        arrow(ax, x + W + 0.15, Y0 + H / 2, x + W + GAP - 0.15, Y0 + H / 2,
              color=RULE, lw=1.4, scale=11)

arrow(ax, 1.0, 9.0, 99.0, 9.0, color="#A8451F", lw=2.4, scale=18)
label(ax, 1.0, 4.2, "value per answered question rises  →  and so does difficulty, "
                    "and the risk of being confidently wrong",
      fs=10, bold=True, color="#A8451F", ha="left")
save(fig, "fig01_1.png")
