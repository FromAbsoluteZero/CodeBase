import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np, pandas as pd, warnings
warnings.filterwarnings("ignore")
exec(open('_pre.py').read())
import shap
from sklearn.inspection import permutation_importance

NAVY, RED, GREEN, ORANGE, SLATE = "#1F3A5F", "#8C2F39", "#2F6B54", "#C1662F", "#5A6673"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10.5,
    "axes.edgecolor": SLATE, "text.color": "#222", "xtick.color": SLATE,
    "ytick.color": SLATE, "axes.spines.top": False, "axes.spines.right": False,
    "figure.dpi": 150})

cols = list(X.columns)
short = {"YearsAtCompany":"Tenure","MonthlyIncome":"Income","CommuteMinutes":"Commute",
         "JobSatisfaction":"Satisfaction","YearsSincePromotion":"Since promo",
         "Department_Sales":"Dept: Sales","Department_Support":"Dept: Support",
         "OverTime_Yes":"Overtime"}

truth = pd.Series({"OverTime_Yes":1.150,"YearsAtCompany":0.638,"JobSatisfaction":0.542,
  "Department_Sales":0.450,"MonthlyIncome":0.242,"CommuteMinutes":0.208,
  "Department_Support":0.200,"YearsSincePromotion":0.187})
imp = pd.Series(rf.feature_importances_, index=cols)
r = permutation_importance(rf, Xte, yte, n_repeats=30, random_state=0, scoring="roc_auc")
perm = pd.Series(r.importances_mean, index=cols)
sv = shap.TreeExplainer(rf).shap_values(Xte, check_additivity=False)[:, :, 1]
sh = pd.Series(np.abs(sv).mean(0), index=cols)

# ---- Figure 29.1: rank agreement with the truth --------------------------
order = truth.sort_values(ascending=False).index.tolist()
series = [("True effect", truth, SLATE), ("Impurity", RED, None),
          ("Permutation", GREEN, None), ("mean |SHAP|", NAVY, None)]
data = {"Impurity": imp, "Permutation": perm, "mean |SHAP|": sh}

fig, axes = plt.subplots(1, 4, figsize=(8.0, 3.5), sharey=True)
panels = [("The truth", truth, SLATE), ("Impurity", imp, RED),
          ("Permutation", perm, GREEN), ("mean |SHAP|", sh, NAVY)]
ypos = np.arange(len(order))[::-1]
for ax, (name, s, col) in zip(axes, panels):
    v = s[order].values
    v = v / np.abs(v).max()
    ax.barh(ypos, v, color=col, height=.62)
    ax.set_title(name, color=NAVY, fontsize=11)
    ax.axvline(0, color=SLATE, lw=.7)
    ax.set_xticks([])
axes[0].set_yticks(ypos)
axes[0].set_yticklabels([short[c] for c in order], fontsize=9.5)
fig.suptitle("Ranked by the true effect. Impurity importance gets it badly wrong.",
             color=NAVY, fontsize=12, x=.02, ha="left", y=1.0)
fig.tight_layout()
fig.savefig("fig29_1.png", bbox_inches="tight")

# ---- Figure 29.2: one employee, explained --------------------------------
i = int(np.argmax(rf.predict_proba(Xte)[:, 1]))
base = shap.TreeExplainer(rf).expected_value[1]
vals = sv[i]
o = np.argsort(np.abs(vals))
labels = [short[cols[j]] for j in o]
fig, ax = plt.subplots(figsize=(6.6, 3.2))
colors = [RED if v > 0 else NAVY for v in vals[o]]
ax.barh(np.arange(len(o)), vals[o], color=colors, height=.6)
ax.set_yticks(np.arange(len(o))); ax.set_yticklabels(labels, fontsize=9.5)
ax.axvline(0, color=SLATE, lw=.8)
ax.set_xlabel("push on predicted probability")
ax.set_title(f"Employee 154: baseline {base:.3f} + pushes = {base+vals.sum():.3f}",
             color=NAVY, fontsize=11.5, loc="left")
fig.tight_layout(); fig.savefig("fig29_2.png", bbox_inches="tight")
print("figures written")
