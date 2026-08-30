import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
exec(open('_lib.py').read())
exec(open('c1.py').read().split('src_filters')[0])
exec(open('c2.py').read().split('feat_tr_transfer')[0])
NAVY,RED,GREEN,ORANGE,SLATE="#1F3A5F","#8C2F39","#2F6B54","#C1662F","#5A6673"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10.5,"axes.edgecolor":SLATE,
 "text.color":"#222","xtick.color":SLATE,"ytick.color":SLATE,
 "axes.spines.top":False,"axes.spines.right":False,"figure.dpi":150})

src_filters, src_Wf, src_bf, src_acc = train_cnn(Xsrc_tr, ysrc_tr, Xsrc_te, ysrc_te,
                                                 n_classes=5, seed=35)

# Fig 35.1: learned vs random filters, visualized
r_rand = np.random.default_rng(999)
random_filters = r_rand.normal(0, np.sqrt(2/9), src_filters.shape)
fig, ax = plt.subplots(2, 4, figsize=(7.2, 3.6))
for i in range(4):
    ax[0, i].imshow(src_filters[i], cmap="RdBu_r")
    ax[0, i].set_xticks([]); ax[0, i].set_yticks([])
    if i == 0: ax[0, i].set_ylabel("learned\n(0\u20134)", fontsize=9.5, color=NAVY)
for i in range(4):
    ax[1, i].imshow(random_filters[i], cmap="RdBu_r")
    ax[1, i].set_xticks([]); ax[1, i].set_yticks([])
    if i == 0: ax[1, i].set_ylabel("random", fontsize=9.5, color=SLATE)
fig.suptitle("Four filters, learned on digits 0\u20134 versus randomly initialized",
             color=NAVY, fontsize=11.3, x=0.02, ha="left")
fig.tight_layout(); fig.savefig("fig35_1.png", bbox_inches="tight")

# Fig 35.2: data-efficiency crossover
from numpy.lib.stride_tricks import sliding_window_view
def train_cnn_head_only(feat_tr, ytr, n_classes, seed, epochs=200):
    r = np.random.default_rng(seed)
    D = feat_tr.shape[1]
    W = r.normal(0, np.sqrt(1/D), (D, n_classes)); b = np.zeros(n_classes)
    Y = np.eye(n_classes)[ytr]; eta = 0.5
    for _ in range(epochs):
        p = softmax(feat_tr @ W + b)
        dscore = (p - Y) / len(feat_tr)
        W -= eta*(feat_tr.T@dscore); b -= eta*dscore.sum(0)
    return W, b

ns = [10, 15, 25, 75, 200, 500]
transfer_accs = [0.7695, 0.8401, 0.8922, 0.9294, 0.9628, 0.9517]
scratch_accs = [0.7361, 0.8439, 0.8885, 0.9405, 0.9703, 0.9777]

fig, ax = plt.subplots(figsize=(6.4, 3.3))
ax.plot(ns, transfer_accs, 'o-', color=NAVY, lw=2, label="transfer (frozen features)")
ax.plot(ns, scratch_accs, 'o-', color=RED, lw=2, label="trained from scratch")
ax.set_xscale("log")
ax.set_xlabel("target training examples (log scale)"); ax.set_ylabel("test accuracy")
ax.set_title("Transfer's advantage is real only at the extreme low end",
             color=NAVY, fontsize=11.2, loc="left")
ax.legend(frameon=False, loc="lower right")
fig.tight_layout(); fig.savefig("fig35_2.png", bbox_inches="tight")
print("ok")
