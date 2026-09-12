"""Figure 12.3 - six categories over twelve months as small multiples.

Each panel is one Category from the chapter's own retail table, summed by month. The six
panels share one y scale, which is the point the caption makes: on a shared scale Supplies
is visibly small, and on free scales it would look like Beans.
"""
import numpy as np, pandas as pd
from _style import *
from _data import retail_path

df = pd.read_csv(retail_path())
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
clean = df[~df["InvoiceNo"].str.startswith("C")].copy()
clean["m"] = pd.to_datetime(clean["InvoiceDate"]).dt.month
piv = clean.pivot_table(index="m", columns="Category", values="Revenue",
                        aggfunc="sum").reindex(range(1, 13))
cats = list(piv.columns)
assert len(cats) == 6, cats

fig, axes = plt.subplots(2, 3, figsize=(9.50, 4.08), sharey=True, sharex=True)
for ax, c in zip(axes.ravel(), cats):
    y = piv[c].values
    ax.plot(piv.index, y, color=NAVY, lw=2.0)
    ax.fill_between(piv.index, 0, y, color=TINT)
    ax.set_title(c, color=NAVY, fontsize=10.5, loc="left")
    ax.set_xticks([1, 6, 12]); ax.set_xlim(1, 12)
    ax.spines["left"].set_color(RULE); ax.spines["bottom"].set_color(RULE)
    ax.set_ylim(0, piv.values.max() * 1.06); ax.set_yticks([0, 2000, 4000, 6000])
axes[0, 0].set_ylabel("revenue"); axes[1, 0].set_ylabel("")
fig.supxlabel("month", color="#222", fontsize=10.5, y=0.02)
fig.suptitle("Shared scale is what makes small multiples work", color=NAVY,
             fontsize=11, x=0.012, ha="left")
fig.tight_layout(rect=[0, 0.03, 1, 0.945])
fig.savefig("fig12_3.png", bbox_inches="tight"); plt.close(fig)
print("wrote fig12_3.png  categories:", cats)
