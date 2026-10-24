"""Figure 13.1 - residuals against fitted values at 400 DPI.

Refits Chapter 13's own two-predictor model (units and lines, code/ch13/c2.py) on the
chapter's own order table, so the funnel, the dashed spread envelope and the three
"typical error" bars are computed rather than traced. The bars reproduce the chapter's
printed $50 / $86 / $123, which the assertion below holds the drawing to.
"""
import numpy as np, pandas as pd
from _style import *
from _data import retail_path

df = pd.read_csv(retail_path()).drop_duplicates()
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
clean = df[~df["InvoiceNo"].str.startswith("C")].copy()
o = clean.groupby("InvoiceNo").agg(rev=("Revenue", "sum"), units=("Quantity", "sum"),
                                   lines=("Revenue", "size"))
y = o["rev"].values
X = np.column_stack([np.ones(len(o)), o["units"], o["lines"]])
beta = np.linalg.lstsq(X, y, rcond=None)[0]
fitted, resid = X @ beta, y - X @ beta
band = pd.qcut(fitted, 3, labels=["small", "medium", "large"])
spread = pd.Series(resid).groupby(band, observed=True).std()
assert [round(v) for v in spread.values] == [50, 86, 123], spread.values

fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.44, 3.707),
                             gridspec_kw=dict(width_ratios=[2.05, 1.0]))
ax.scatter(fitted, resid, s=13, color=NAVY, alpha=0.30, linewidths=0)
ax.axhline(0, color="#B0521F", lw=2.0)
# the envelope: the rolling spread of the residuals, which is the funnel the caption names
edges = np.linspace(fitted.min(), np.percentile(fitted, 99), 17)
mid = 0.5 * (edges[:-1] + edges[1:])
sd = np.array([resid[(fitted >= a) & (fitted < b)].std() for a, b in zip(edges[:-1], edges[1:])])
ok = ~np.isnan(sd)
ax.plot(mid[ok], 2 * sd[ok], color=RED, ls="--", lw=1.8)
ax.plot(mid[ok], -2 * sd[ok], color=RED, ls="--", lw=1.8)
ax.set_xlabel("fitted value  ($)"); ax.set_ylabel("residual  ($)")
ax.set_title("Residuals vs fitted: a funnel, not a band", color=NAVY, fontsize=11, loc="left")
# Bottom right, under the lower envelope: on the title line it collided with the title, and
# just below the title the upper +2sd envelope ran straight through it.
ax.text(0.985, 0.045, "spread grows with the prediction", transform=ax.transAxes,
        ha="right", va="bottom", color=RED, fontsize=10, fontweight="bold")
ax.spines["left"].set_color(RULE); ax.spines["bottom"].set_color(RULE)

cols = [TINT, "#D8C3B0", "#E4A06A"]
bars = bx.bar(list(spread.index), spread.values, color=cols, edgecolor=NAVY, linewidth=1.6,
              width=0.66)
for b, v in zip(bars, spread.values):
    bx.text(b.get_x() + b.get_width() / 2, v + 3, f"${v:,.0f}", ha="center", va="bottom",
            fontsize=10.5, fontweight="bold", color=NAVY)
bx.set_ylabel("typical error ($)")
bx.set_title("by predicted size", color=NAVY, fontsize=11, loc="left")
bx.set_ylim(0, spread.max() * 1.22)
bx.spines["left"].set_color(RULE); bx.spines["bottom"].set_color(RULE)
fig.tight_layout()
fig.savefig("fig13_1.png", bbox_inches="tight"); plt.close(fig)
print("wrote fig13_1.png  typical error:", spread.round(0).to_dict())
