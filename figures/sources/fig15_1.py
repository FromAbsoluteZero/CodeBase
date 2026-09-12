"""Figure 15.1 - power against sample size.

Uses Chapter 15's own power_at(), printed in the chapter, so the curve is the chapter's
arithmetic rather than an approximation of its picture.
"""
import numpy as np
from scipy import stats
from _style import *

def power_at(p1, p2, n, alpha=0.05):
    pbar = (p1 + p2) / 2
    se0 = np.sqrt(2 * pbar * (1 - pbar) / n)
    se1 = np.sqrt(p1 * (1 - p1) / n + p2 * (1 - p2) / n)
    zc = stats.norm.ppf(1 - alpha / 2)
    return (1 - stats.norm.cdf((zc * se0 - abs(p2 - p1)) / se1)
            + stats.norm.cdf((-zc * se0 - abs(p2 - p1)) / se1))

n = np.arange(20, 2205, 5)
fig, ax = plt.subplots(figsize=(9.44, 3.71))
# Dash patterns as well as colour: two of these three lines print at nearly the same tone
# in a black-ink interior, and the legend is the only key to which curve is which.
# The baseline is the FLAGGED population's attrition, 33% (Chapter 14's precision on the
# sixty highest scorers), not the company-wide 12%: the experiment runs on flagged staff.
for p2, col, dash, lab in ((0.30, NAVY, "solid", "detect 33% -> 30%  (3 pp)"),
                           (0.29, ORANGE, (0, (6, 2.4)), "detect 33% -> 29%  (4 pp)"),
                           (0.27, GREEN, (0, (1.4, 1.8)), "detect 33% -> 27%  (6 pp)")):
    ax.plot(n, [power_at(0.33, p2, k) for k in n], color=col, lw=2.6, ls=dash, label=lab)

ax.axhline(0.8, color=SLATE, ls="--", lw=1.3)
# label above the rule, not on it
# above the rule, in the window between where green clears it and where orange arrives
ax.annotate("conventional 80% power", xy=(430, 0.8), xytext=(430, 0.816),
            color=SLATE, fontsize=9.5, ha="left", va="bottom")

p30 = power_at(0.33, 0.29, 30)
ax.plot([30], [p30], "o", color=RED, ms=7, zorder=5)
ax.annotate(f"the experiment Chapter 14\nproposed: power {p30:.3f}",
            xy=(30, p30), xytext=(215, 0.225), color=RED, fontsize=10.5,
            fontweight="bold", va="center",
            arrowprops=dict(arrowstyle="->", color=RED, lw=1.1))

ax.set_xlabel("sample size per arm"); ax.set_ylabel("power")
ax.set_ylim(0, 1.04); ax.set_xlim(0, 2200)
ax.set_title("Power against sample size: what your experiment could possibly detect",
             color=NAVY, fontsize=11.5, loc="left")
ax.legend(frameon=False, loc="lower right")
fig.tight_layout()
save(fig, "fig15_1.png")
