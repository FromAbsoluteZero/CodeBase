"""Figure 14.1 - precision and recall against the threshold at 400 DPI.

Refits Chapter 14's own logistic model on its own hr.csv with the same split (test_size 0.3,
random_state 7, stratified) and scaler, then sweeps the threshold, so both curves, the
break-even line and the "catches N% of leavers" reading at 0.5 are computed here. The
assertion holds the 0.5 reading to the value Chapter 14 prints.
"""
import numpy as np, pandas as pd, os
from _style import *
from _data import retail_path
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

hr = pd.read_csv(os.path.join(os.path.dirname(retail_path()), "hr.csv"))
X = pd.get_dummies(hr.drop(columns="Attrition"), columns=["Department", "OverTime"],
                   drop_first=True).astype(float)
y = hr["Attrition"].values
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=7, stratify=y)
sc = StandardScaler().fit(Xtr)
model = LogisticRegression(max_iter=1000).fit(sc.transform(Xtr), ytr)
p = model.predict_proba(sc.transform(Xte))[:, 1]

BREAK_EVEN = 0.15
ths = np.arange(0.05, 0.6005, 0.01)
prec, rec = [], []
for t in ths:
    f = p >= t
    tp = int((f & (yte == 1)).sum()); fp = int((f & (yte == 0)).sum())
    fn = int(((~f) & (yte == 1)).sum())
    prec.append(tp / (tp + fp) if tp + fp else np.nan)
    rec.append(tp / (tp + fn))
prec, rec = np.array(prec), np.array(rec)
r50 = rec[np.argmin(abs(ths - 0.5))]
assert round(r50 * 100) == 6, r50          # Chapter 14 prints 6% of leavers at the default

fig, ax = plt.subplots(figsize=(9.44, 3.707))
ax.plot(ths, rec, color="#B0521F", lw=2.4, label="recall — share of leavers caught")
ax.plot(ths, prec, color=NAVY, lw=2.4, label="precision — share of flags that were right")
ax.axhline(BREAK_EVEN, color=GREEN, ls=":", lw=1.8)
ax.text(0.075, BREAK_EVEN - 0.035, f"break-even precision {BREAK_EVEN:.0%}",
        color=GREEN, fontsize=10, va="top")
ax.axvline(0.5, color=SLATE, ls="--", lw=1.8)
ax.annotate(f"default threshold 0.5:\ncatches {r50:.0%} of leavers",
            xy=(0.5, 0.695), xytext=(0.238, 0.755), color=SLATE, fontsize=10,
            ha="left", va="center",
            arrowprops=dict(arrowstyle="->", color=SLATE, lw=1.1))
ax.set_xlabel("threshold"); ax.set_ylabel("rate")
ax.set_xlim(0.05, 0.60); ax.set_ylim(0, 1.02)
ax.set_title("The same model at every threshold: precision and recall trade against each other",
             color=NAVY, fontsize=11, loc="left")
# the legend keeps the top of the panel; the 0.5 note sits under it, not through it
ax.legend(loc="upper center", frameon=False, fontsize=10, bbox_to_anchor=(0.44, 1.03))
ax.spines["left"].set_color(RULE); ax.spines["bottom"].set_color(RULE)
fig.tight_layout()
fig.savefig("fig14_1.png", bbox_inches="tight"); plt.close(fig)
print(f"wrote fig14_1.png  recall at 0.5 = {r50:.4f}")
