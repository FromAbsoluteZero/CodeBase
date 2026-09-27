"""Figure 1.2 - the analytics workflow as a loop, with the share of effort.

The six stages, their ring order, the "decision / then a sharper question" centre, the six
percentages (15, 10, 30, 20, 10, 15) and the caveat under the bars are all the diagram's.
The percentages sum to 100 and the assertion below keeps that true if the figure is edited.
"""
from _style import *
import numpy as np

STAGES = ["frame the\nquestion", "collect", "clean", "explore", "model\n(optional)", "communicate"]
EFFORT = [("framing", 15, NAVY), ("collecting", 10, SLATE), ("cleaning", 30, "#B0521F"),
          ("exploring", 20, "#8C97A8"), ("modeling", 10, GREEN), ("communicating", 15, "#C8A05A")]
assert sum(e for _, e, _ in EFFORT) == 100

fig = plt.figure(figsize=(9.44, 3.707))
ax = fig.add_axes([0.00, 0.02, 0.50, 0.96]); ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")

CX, CY, R = 50, 52, 33
ang = np.linspace(90, 90 - 360, 400)
ax.plot(CX + R * np.cos(np.radians(ang)), CY + R * np.sin(np.radians(ang)),
        color="#B0521F", lw=1.8, zorder=0)
for i, txt in enumerate(STAGES):
    a = np.radians(90 - i * 60)
    x, y = CX + R * np.cos(a), CY + R * np.sin(a)
    w, h = 27, 17
    face = "#FBF3E6" if i == 0 else (TINT if i == 4 else "white")
    rbox(ax, x - w / 2, y - h / 2, w, h, edge=NAVY, face=face, lw=1.7, r=2.0, z=2)
    label(ax, x, y, txt, fs=9.5, bold=(i == 0), color=NAVY, z=3)
label(ax, CX, CY + 4, "decision", fs=11.5, bold=True, color="#B0521F")
label(ax, CX, CY - 3, "then a sharper question", fs=9.5, italic=True, color=SLATE)

bx = fig.add_axes([0.615, 0.13, 0.30, 0.76])
names = [n for n, _, _ in EFFORT]; vals = [v for _, v, _ in EFFORT]; cols = [c for _, _, c in EFFORT]
ypos = np.arange(len(names))[::-1]
bx.barh(ypos, vals, color=cols, height=0.62)
for y, v, c in zip(ypos, vals, cols):
    bx.text(v + 1.0, y, f"{v}%", va="center", ha="left", fontsize=10, fontweight="bold", color=c)
bx.set_yticks(ypos); bx.set_yticklabels(names, fontsize=10, color="#222")
bx.set_xticks([]); bx.set_xlim(0, 38)
bx.spines["bottom"].set_visible(False); bx.spines["left"].set_color(RULE)
bx.set_title("Typical share of effort", fontsize=10.5, color="#222", loc="left")
bx.tick_params(length=0)
bx.text(0, -0.95, "Indicative proportions, not measured values —\nthe point is the ordering, "
                  "not the exact numbers", fontsize=9, style="italic", color=SLATE, va="top")
plt.close("all") if False else None
fig.savefig("fig01_2.png", bbox_inches="tight"); plt.close(fig); print("wrote fig01_2.png")
