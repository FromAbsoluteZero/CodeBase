import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
exec(open('_lib.py').read())
exec(open('c1.py').read().split('print(f')[0])
NAVY,RED,GREEN,ORANGE,SLATE="#1F3A5F","#8C2F39","#2F6B54","#C1662F","#5A6673"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10.5,"axes.edgecolor":SLATE,
 "text.color":"#222","xtick.color":SLATE,"ytick.color":SLATE,
 "axes.spines.top":False,"axes.spines.right":False,"figure.dpi":150})

# Fig 43.1: KS p-value and PSI vs week, data-drift case
weeks = list(range(13))
ks_pvals, psis = [], []
for week in weeks:
    shift = week * 0.6
    live = r.normal(50 + shift, 10, 300)
    _, p = ks_test(baseline, live)
    ks_pvals.append(p)
exec(open('c2.py').read().split('print(f')[0])
for week in weeks:
    shift = week * 0.6
    live = r.normal(50 + shift, 10, 300)
    psis.append(psi(baseline, live))

fig, ax1 = plt.subplots(figsize=(6.6, 3.4))
ax1.plot(weeks, ks_pvals, 'o-', color=RED, lw=2, label="KS test p-value")
ax1.axhline(0.01, color=RED, ls=':', lw=1)
ax1.set_xlabel("week"); ax1.set_ylabel("KS p-value", color=RED)
ax1.tick_params(axis='y', colors=RED)
ax2 = ax1.twinx()
ax2.plot(weeks, psis, 'o-', color=NAVY, lw=2, label="PSI")
ax2.axhline(0.25, color=NAVY, ls=':', lw=1)
ax2.set_ylabel("PSI", color=NAVY)
ax2.tick_params(axis='y', colors=NAVY)
ax2.spines['top'].set_visible(False)
ax1.set_title("Two drift metrics, the same gradual shift: both eventually flag it",
             color=NAVY, fontsize=10.8, loc="left")
fig.tight_layout(); fig.savefig("fig43_1.png", bbox_inches="tight")

# Fig 43.2: the concept drift trap -- accuracy collapses, KS p-value never moves
exec(open('c3.py').read().split('print(f')[0])
r3 = np.random.default_rng(430)
accs, kss = [], []
for week in weeks:
    x_live = r3.normal(50, 10, 500)
    true_boundary_now = 50 + week * 2.5
    y_live = make_labels(x_live, true_boundary_now)
    pred = (x_live > model_boundary).astype(int)
    accs.append((pred == y_live).mean())
    _, p = ks_test(x_train, x_live)
    kss.append(p)

fig, ax1 = plt.subplots(figsize=(6.6, 3.4))
ax1.plot(weeks, accs, 'o-', color=RED, lw=2)
ax1.axhline(0.5, color=SLATE, ls=':', lw=1)
ax1.set_xlabel("week"); ax1.set_ylabel("model accuracy", color=RED)
ax1.tick_params(axis='y', colors=RED)
ax2 = ax1.twinx()
ax2.plot(weeks, kss, 'o-', color=NAVY, lw=2)
ax2.set_ylabel("feature-drift KS p-value", color=NAVY)
ax2.tick_params(axis='y', colors=NAVY)
ax2.spines['top'].set_visible(False)
ax1.set_title("Concept drift: accuracy collapses while the feature test sees nothing",
             color=NAVY, fontsize=10.6, loc="left")
fig.tight_layout(); fig.savefig("fig43_2.png", bbox_inches="tight")
print("ok")
