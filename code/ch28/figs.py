import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, pandas as pd, numpy as np, warnings
warnings.filterwarnings("ignore")
from statsmodels.tsa.holtwinters import ExponentialSmoothing

NAVY, RED, GREEN, ORANGE, SLATE = "#1F3A5F", "#8C2F39", "#2F6B54", "#C1662F", "#5A6673"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                     "axes.edgecolor": SLATE, "axes.labelcolor": "#222",
                     "text.color": "#222", "xtick.color": SLATE,
                     "ytick.color": SLATE, "axes.spines.top": False,
                     "axes.spines.right": False, "figure.dpi": 150})

s = pd.read_csv("daily_revenue.csv",
                parse_dates=["Date"]).set_index("Date")["Revenue"]
s = s.asfreq("D")

# ---- Figure 28.1 : the three things inside a series -------------------------
fig, ax = plt.subplots(3, 1, figsize=(7.6, 5.4), sharex=True)
w = s["2024-01-01":"2024-06-30"]
ax[0].plot(w.index, w.values, color=NAVY, lw=.9)
ax[0].set_title("The series as it arrives", color=NAVY, loc="left", fontsize=11.5)
ax[0].set_ylabel("revenue")

roll = s.rolling(7, center=True).mean()["2024-01-01":"2024-06-30"]
ax[1].plot(w.index, w.values, color="#C8CED8", lw=.8)
ax[1].plot(roll.index, roll.values, color=RED, lw=1.8)
ax[1].set_title("A 7-day mean removes the weekly cycle and leaves the trend",
                color=NAVY, loc="left", fontsize=11.5)
ax[1].set_ylabel("revenue")

resid = (w / roll)
ax[2].axhline(1, color=SLATE, ls="--", lw=.8)
ax[2].plot(resid.index, resid.values, color=GREEN, lw=.9)
ax[2].set_title("What is left over: the weekly pattern, repeating",
                color=NAVY, loc="left", fontsize=11.5)
ax[2].set_ylabel("ratio to trend")
fig.tight_layout()
fig.savefig("fig28_1.png", bbox_inches="tight")

# ---- Figure 28.2 : one window lies, six windows tell the truth --------------
H = 28
def fold(cut):
    tr, te = s[:cut], s[cut:cut + H]
    rep = np.array(tr.iloc[-7:].values.tolist() * 4)
    sn = np.mean(np.abs(te.values - rep))
    hw = ExponentialSmoothing(tr, trend="add", seasonal="add",
                              seasonal_periods=7).fit().forecast(H)
    return sn, np.mean(np.abs(te.values - hw.values))

cuts = [len(s) - H * k for k in range(6, 0, -1)]
res = [fold(c) for c in cuts]
labels = [s.index[c + H - 1].strftime("%d %b") for c in cuts]
x = np.arange(len(cuts))

fig, ax = plt.subplots(figsize=(7.6, 3.5))
ax.bar(x - .19, [r[0] for r in res], .38, label="seasonal naive", color=NAVY)
ax.bar(x + .19, [r[1] for r in res], .38, label="Holt-Winters", color=ORANGE)
ax.set_xticks(x); ax.set_xticklabels(labels)
ax.set_ylabel("MAE  (dollars)"); ax.set_xlabel("four-week window ending")
ax.set_title("The same two methods, six consecutive test windows",
             color=NAVY, loc="left", fontsize=12)
ax.annotate("Christmas sits in\nthis window", xy=(5, 700), xytext=(3.5, 620),
            fontsize=9.5, color=SLATE,
            arrowprops=dict(arrowstyle="->", color=SLATE, lw=.9))
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig("fig28_2.png", bbox_inches="tight")
print("figures written")
