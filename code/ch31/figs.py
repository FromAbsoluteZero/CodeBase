import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
exec(open('_lib.py').read())
NAVY,RED,GREEN,ORANGE,SLATE="#1F3A5F","#8C2F39","#2F6B54","#C1662F","#5A6673"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10.5,"axes.edgecolor":SLATE,
 "text.color":"#222","xtick.color":SLATE,"ytick.color":SLATE,
 "axes.spines.top":False,"axes.spines.right":False,"figure.dpi":150})

sizes = [64] + [64] * 8
exec(open('c4.py').read().split('print("naive')[0])   # forward_deep, train
exec(open('c5.py').read().split('print("naive')[0])   # forward_bn, train_bn

# Fig 31.1: activation scale, naive vs He, log scale
Ws = naive_init(sizes, seed=31); Ws_he = he_init(sizes, seed=31)
a = X[:200]
naive_scale = [np.abs(a).mean()]
for W in Ws:
    a = np.maximum(0, a @ W); naive_scale.append(np.abs(a).mean())
a = X[:200]
he_scale = [np.abs(a).mean()]
for W in Ws_he:
    a = np.maximum(0, a @ W); he_scale.append(np.abs(a).mean())

fig, ax = plt.subplots(figsize=(6.6, 3.3))
ax.plot(range(9), naive_scale, 'o-', color=RED, lw=2, label="naive init, std=1")
ax.plot(range(9), he_scale, 'o-', color=NAVY, lw=2, label="He init")
ax.set_yscale("log")
ax.set_xlabel("layer"); ax.set_ylabel("mean |activation| (log scale)")
ax.set_title("Nine layers, no training: one initialization explodes, one does not",
             color=NAVY, fontsize=11.3, loc="left")
ax.legend(frameon=False)
fig.tight_layout(); fig.savefig("fig31_1.png", bbox_inches="tight")

# Fig 31.2: training curves, naive vs He vs BN-rescued naive -- identical
# seed (31) and identical deep_sizes to the worked example, so the figure
# and the printed numbers describe the same run.
h1 = train(deep_sizes, naive_init, seed=31, eta=0.05, epochs=250)
h2 = train(deep_sizes, he_init, seed=31, eta=0.05, epochs=250)
h3 = train_bn(deep_sizes, naive_init, seed=31, eta=0.05, epochs=250)

fig, ax = plt.subplots(figsize=(6.6, 3.3))
ax.plot([x[0] for x in h1], [x[2] for x in h1], 'o-', color=RED, lw=2, label="naive init")
ax.plot([x[0] for x in h2], [x[2] for x in h2], 'o-', color=NAVY, lw=2, label="He init")
ax.plot([x[0] for x in h3], [x[2] for x in h3], 'o--', color=GREEN, lw=2,
        label="naive init + batch norm")
ax.set_xlabel("epoch"); ax.set_ylabel("test accuracy")
ax.set_title("Same five-layer network, same data, same learning rate",
             color=NAVY, fontsize=11.3, loc="left")
ax.legend(frameon=False, loc="center right")
fig.tight_layout(); fig.savefig("fig31_2.png", bbox_inches="tight")
print("ok")
