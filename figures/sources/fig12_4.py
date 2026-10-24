"""Figure 12.4 - the worked example's final chart, drawn by Chapter 12's own Step 5 code.

Chapter 12 has no companion directory: its blocks run as printed. This script rebuilds
the two objects Step 5 uses from the earlier blocks (the de-duplicated `clean` table
with its Month column, and `m`, total revenue by month), then runs the Step 5 block
exactly as printed. The only difference is the file name it saves to.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd
from _data import retail_path

df = pd.read_csv(retail_path()).drop_duplicates()
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
clean = df[~df["InvoiceNo"].str.startswith("C")].copy()
clean["InvoiceDate"] = pd.to_datetime(clean["InvoiceDate"])
clean["Month"] = clean["InvoiceDate"].dt.month
m = clean.groupby("Month")["Revenue"].sum()

# ---- Step 5, as printed ----
uk_rows = clean[clean["Country"]=="United Kingdom"]
de_rows = clean[clean["Country"]=="Germany"]
uk = uk_rows.groupby("Month")["Revenue"].sum()
de = de_rows.groupby("Month")["Revenue"].sum()

def change(s):                       # H2 against H1, as a fraction
    return s.loc[7:12].sum() / s.loc[1:6].sum() - 1

title = (f"H2 revenue was {-change(uk):.0%} lower in the UK "
         f"and {change(de):.0%} higher in Germany")
note = (f"Total revenue {change(m):+.1%}. "
        f"Observed in one year, not a confirmed trend.")
print("chart title:", title)
print("subtitle:", note)

fig, ax = plt.subplots(figsize=(7, 3.4))
ax.axvspan(6.5, 12.5, color="#FAF0E6")      # shade the second half
for s, name, colour in [(uk, "UK", "#B0541F"),
                        (de, "Germany", "#1F3251")]:
    ax.plot(s.index, s.values, color=colour, linewidth=2)
    ax.text(12.7, s.iloc[-1], name, color=colour,       # direct label
            va="center", fontweight="bold")
    for lo, hi in [(1, 6), (7, 12)]:        # each half's monthly mean
        ax.hlines(s.loc[lo:hi].mean(), lo, hi, color=colour,
                  linestyle="--", lw=1)
top = uk.max() * 1.15
ax.text(3.5, top, "H1", ha="center", fontsize=9, color="#5A6472")
ax.text(9.5, top, "H2", ha="center", fontsize=9, color="#5A6472")
ax.set_title(title, loc="left", fontsize=11, pad=22)
ax.text(0, 1.03, note, transform=ax.transAxes, fontsize=8.5,
        color="#5A6472")
ax.set_xticks(range(1, 13))
ax.set_xlabel("month")
ax.set_ylim(0, top * 1.08)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.yaxis.set_major_formatter(
    FuncFormatter(lambda v, _: f"${v/1000:,.0f}k"))
fig.savefig("fig12_4.png", dpi=400, bbox_inches="tight")
# ----------------------------
assert title == "H2 revenue was 14% lower in the UK and 75% higher in Germany", title
print("wrote fig12_4.png")
