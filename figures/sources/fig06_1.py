"""Figure 6.1 - the order-value distribution at 400 DPI.

Built from the chapter's own order table (data/generated/retail.csv, aggregated exactly as
code/ch06 does), so the 897 orders, the mean, the median rule, the $655 upper fence and the
count of orders beyond it are computed here rather than copied off the old picture.
"""
import numpy as np
from _style import *
from _data import orders

o = orders()
rev = o["rev"].values
n = len(rev)
mean, med = rev.mean(), np.median(rev)
q1, q3 = np.percentile(rev, [25, 75])
fence = q3 + 1.5 * (q3 - q1)
beyond = int((rev > fence).sum())

fig = plt.figure(figsize=(8.08, 4.18))
ax = fig.add_axes([0.085, 0.375, 0.895, 0.505])
bx = fig.add_axes([0.085, 0.105, 0.895, 0.205], sharex=ax)

# 34 equal-width bins over the data range
ax.hist(rev, bins=34, color=TINT, edgecolor=SLATE, linewidth=0.7)
ax.axvline(med, color=NAVY, lw=2.4)
ax.axvline(mean, color="#B0521F", lw=2.6, ls=(0, (4, 2.5)))
ax.set_ylabel("number of orders")
ax.set_title(f"{n} orders: right-skewed, so the mean describes no typical customer",
             color=NAVY, fontsize=11, loc="left", pad=26)
ax.spines["left"].set_color(RULE)
ax.set_xlim(-10, max(900, rev.max() * 1.02))

# the label lives ABOVE the axes, in the pad reserved for it, and its leader drops to the rule
ax.annotate(f"mean ${mean:,.0f}", xy=(mean, 1.0), xycoords=("data", "axes fraction"),
            xytext=(mean + 95, 1.115), textcoords=("data", "axes fraction"),
            color="#B0521F", fontsize=10.5, fontweight="bold", ha="left", va="center",
            annotation_clip=False,
            arrowprops=dict(arrowstyle="->", color="#B0521F", lw=1.6, shrinkA=2, shrinkB=0))
ax.text(0.985, 0.72, "the right tail is what\npulls the mean above\nthe median",
        transform=ax.transAxes, ha="right", va="top", color=SLATE, fontsize=9.5)

bp = bx.boxplot(rev, vert=False, widths=0.55, whis=1.5, showfliers=True,
                patch_artist=True, medianprops=dict(color=NAVY, lw=2.0),
                boxprops=dict(facecolor=TINT, edgecolor=NAVY, lw=1.6),
                whiskerprops=dict(color=SLATE, lw=1.3), capprops=dict(color=SLATE, lw=1.3),
                flierprops=dict(marker="o", markersize=3.2, markerfacecolor="#B0521F",
                                markeredgecolor="none", alpha=0.85))
bx.set_yticks([]); bx.spines["left"].set_visible(False); bx.spines["bottom"].set_color(RULE)
bx.set_xlabel("order value ($)")
bx.text(fence, 1.42, f"fence ${fence:,.0f}", color=SLATE, fontsize=9.5, ha="center", va="bottom")
# clear of the flier row: the outliers sit at y = 1, so the note goes well below them
bx.text(fence + 45, 0.48, f"{beyond} large orders —\nreal, not errors",
        color="#B0521F", fontsize=9.5, ha="left", va="center")
bx.set_ylim(0.22, 1.62)
plt.setp(ax.get_xticklabels(), visible=False)
fig.savefig("fig06_1.png", bbox_inches="tight"); plt.close(fig)
print(f"wrote fig06_1.png   n={n} mean={mean:.2f} median={med:.2f} fence={fence:.2f} beyond={beyond}")
