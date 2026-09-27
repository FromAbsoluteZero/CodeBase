"""Figure 8.1 - a hypothesis test as a comparison against what chance produces.

The curve is the null distribution of the difference in conversion rate. The observed
difference is +0.70 pp and the chapter reports p = 0.18, which fixes the standard error at
0.70 / 1.34 = 0.5224 pp, so the +-1.96 SE rules land at +-1.024 pp.
"""
import numpy as np
from scipy import stats
from _style import *

SE, OBS = 0.5224, 0.70
crit = 1.96 * SE
x = np.linspace(-2.6, 3.4, 1200)
pdf = stats.norm.pdf(x, 0, SE)

fig, ax = plt.subplots(figsize=(7.60, 3.45))
ax.plot(x, pdf, color=NAVY, lw=2.4)
ax.fill_between(x, pdf, where=(np.abs(x) <= crit), color=TINT)
ax.fill_between(x, pdf, where=(x <= -crit), color=ORANGE, alpha=0.25)
ax.fill_between(x, pdf, where=(x >= crit), color=ORANGE, alpha=0.25)
for s in (-1, 1):
    ax.axvline(s * crit, color=SLATE, ls="--", lw=1.2)
    ax.annotate(f"{'+' if s > 0 else '-'}1.96 SE", xy=(s * crit, 0),
                xytext=(s * crit + s * 0.07, stats.norm.pdf(0, 0, SE) * 0.14),
                color=SLATE, fontsize=9.5,
                ha="left" if s > 0 else "right", va="bottom")
ax.axvline(OBS, color=ORANGE, lw=2.6)
ax.annotate(f"observed  +{OBS:.2f} pp", xy=(OBS, stats.norm.pdf(OBS, 0, SE) * 0.86),
            xytext=(1.35, 0.60), color=ORANGE, fontsize=10.5, fontweight="bold",
            arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.2))
ax.text(-0.02, 0.20, "what chance alone\nproduces if the pages\nconvert identically",
        color=SLATE, fontsize=10, ha="center", va="center")
ax.text(1.42, 0.28, "p = 0.18\nthe observed gap sits\ninside the ordinary range",
        color=ORANGE, fontsize=10.5, fontweight="bold", ha="left", va="center")
ax.set_xlabel("difference in conversion rate (percentage points)")
ax.set_yticks([]); ax.spines["left"].set_visible(False)
ax.set_ylim(0, stats.norm.pdf(0, 0, SE) * 1.10)
ax.set_title("A hypothesis test asks whether the data is surprising under the null",
             color=NAVY, fontsize=11.5, loc="left")
fig.tight_layout()
save(fig, "fig08_1.png")
