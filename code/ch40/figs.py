import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
exec(open('_lib.py').read())
exec(open('c1.py').read().split('print(f')[0])
NAVY,RED,GREEN,ORANGE,SLATE="#1F3A5F","#8C2F39","#2F6B54","#C1662F","#5A6673"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10.5,"axes.edgecolor":SLATE,
 "text.color":"#222","xtick.color":SLATE,"ytick.color":SLATE,
 "axes.spines.top":False,"axes.spines.right":False,"figure.dpi":150})

# Fig 40.1: kappa vs rater noise
noises = [0.2, 0.6, 1.0, 1.5, 2.5]
kappas = []
for noise in noises:
    ks = []
    for pair_seed in range(20):
        a = simulate_rater(true_quality, noise, seed=1000+pair_seed)
        b = simulate_rater(true_quality, noise, seed=2000+pair_seed)
        ks.append(cohen_kappa(a, b))
    kappas.append(np.mean(ks))

fig, ax = plt.subplots(figsize=(6.4, 3.3))
ax.plot(noises, kappas, 'o-', color=NAVY, lw=2)
ax.axhline(0, color=SLATE, ls=':', lw=1)
ax.set_xlabel("rater noise (standard deviation)"); ax.set_ylabel("Cohen's kappa")
ax.set_title("Inter-rater agreement collapses as raters get noisier",
             color=NAVY, fontsize=11.3, loc="left")
fig.tight_layout(); fig.savefig("fig40_1.png", bbox_inches="tight")

# Fig 40.2: rubric RMSE vs number of criteria, with 1/sqrt(n) reference
ns = [1, 2, 3, 5, 10]
rmses = [1.0620, 0.7638, 0.5898, 0.4420, 0.3014]
theory = [1.0620 / np.sqrt(n) for n in ns]
fig, ax = plt.subplots(figsize=(6.4, 3.3))
ax.plot(ns, rmses, 'o-', color=NAVY, lw=2, label="measured")
ax.plot(ns, theory, '--', color=RED, lw=1.5, label="1/\u221an prediction")
ax.set_xlabel("number of rubric criteria averaged"); ax.set_ylabel("RMSE against true quality")
ax.set_title("Averaging independent criteria reduces error as the law\nof large numbers predicts",
             color=NAVY, fontsize=10.8, loc="left")
ax.legend(frameon=False)
fig.tight_layout(); fig.savefig("fig40_2.png", bbox_inches="tight")
print("ok")
