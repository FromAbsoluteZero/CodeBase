"""Figure 7.1 - the central limit theorem on real order values.

Runs Chapter 7's own sampling loop (seed 0, 5000 draws at each of n = 1, 5, 30) on the same
order revenues, so the three distributions and the sd/skew figures printed beside them are
the chapter's own numbers rather than a redrawing of its picture.
"""
import numpy as np, pandas as pd
from _style import *
from _data import orders

pop = orders()["rev"].values
rng = np.random.default_rng(0)
mu = pop.mean()

# One y scale across the three panels: the whole point of the figure is that the same
# 5,000 draws pile up higher and higher as n grows, and independent y axes hide that.
fig, axes = plt.subplots(1, 3, figsize=(9.44, 3.43), sharey=True)
for ax, k in zip(axes, (1, 5, 30)):
    means = np.array([rng.choice(pop, k).mean() for _ in range(5000)])
    # a fixed 900-wide range at 48 bins gives the n=30 panel about seven bars; the
    # original resolves it far more finely, so the bin width scales with n
    ax.hist(means, bins=int(48 * max(1, k ** 0.5)), range=(0, 900),
            color=TINT, edgecolor=SLATE, linewidth=0.5)
    ax.axvline(mu, color=ORANGE, ls="--", lw=1.6)
    ax.set_title(f"n = {k}", color="#222", fontsize=10.5, loc="left")
    ax.set_xlabel("sample mean ($)")
    ax.set_xlim(0, 900); ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    sd, sk = means.std(ddof=1), pd.Series(means).skew()
    ax.text(0.97, 0.95, f"sd {sd:.0f}\nskew {sk:.2f}", transform=ax.transAxes,
            ha="right", va="top", color=SLATE, fontsize=9.5)

# label the population rule once, on the first panel, beside the rule rather than on it
axes[0].annotate("the population\nitself: skewed", xy=(mu, 0.55), xycoords=("data", "axes fraction"),
                 xytext=(mu + 190, 0.72), textcoords=("data", "axes fraction"),
                 color=ORANGE, fontsize=9.5, ha="left", va="center",
                 arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.0))
fig.suptitle("The same skewed population, averaged in samples of 1, 5, and 30",
             color=NAVY, fontsize=11.5, x=0.012, ha="left")
fig.tight_layout(rect=[0, 0, 1, 0.94])
save(fig, "fig07_1.png")
