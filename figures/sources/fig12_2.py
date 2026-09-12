"""Figure 12.2 - the same twelve months drawn twice at 400 DPI.

The twelve monthly revenues are summed from the chapter's own retail table, so both panels
plot identical numbers and the figure's claim is true by construction rather than by drawing.
"""
import numpy as np, pandas as pd
from _style import *
from _data import retail_path

# Chapter 12's own listing opens with .drop_duplicates(); without it the shortest bar
# comes out at $14,034 and the page opposite says $13,754.
df = pd.read_csv(retail_path()).drop_duplicates()
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
clean = df[~df["InvoiceNo"].str.startswith("C")]
monthly = (clean.assign(m=pd.to_datetime(clean["InvoiceDate"]).dt.month)
                .groupby("m")["Revenue"].sum().reindex(range(1, 13)))
rev = monthly.values
CUT = 13000
# the three numbers the facing page states about this figure
assert round(rev.min()) == 13754, round(rev.min())
assert round(rev.max()) == 20649, round(rev.max())
assert round((rev.max() - CUT) / (rev.min() - CUT)) == 10          # "ten times the shortest"

fig, (axL, axR) = plt.subplots(1, 2, figsize=(9.433, 3.44))
for ax, colour, base in ((axL, GREEN, 0), (axR, RED, CUT)):
    ax.bar(monthly.index, rev - base, bottom=base, color=TINT, edgecolor=colour,
           linewidth=1.6, width=0.62)
    ax.set_xticks(range(1, 13)); ax.set_xlabel("month")
    ax.set_ylim(base, max(rev) * 1.045)
    ax.spines["left"].set_color(RULE); ax.spines["bottom"].set_color(RULE)
axL.set_ylabel("revenue")
axL.set_title("honest: axis starts at zero", color=GREEN, fontsize=11, loc="left")
axR.set_title(f"misleading: axis starts at ${CUT:,}", color=RED, fontsize=11, loc="left")
axR.set_yticks(np.arange(14000, int(max(rev)) + 1, 2000))
fig.suptitle("same twelve numbers in both panels", color=SLATE, fontsize=10,
             style="italic", x=0.5, y=0.995)
fig.tight_layout(rect=[0, 0, 1, 0.945])
fig.savefig("fig12_2.png", bbox_inches="tight"); plt.close(fig)
print(f"wrote fig12_2.png  monthly ${rev.min():,.0f} to ${rev.max():,.0f}, "
      f"truncated ratio {(rev.max()-CUT)/(rev.min()-CUT):.1f}x")
