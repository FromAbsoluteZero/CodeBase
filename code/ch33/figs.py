import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
exec(open('../_greyscale_safe.py').read())   # dash + hatch per colour, for black-and-white printing
exec(open('_lib.py').read())
exec(open('c3.py').read().split('def loss_fn')[0])
NAVY,RED,GREEN,ORANGE,SLATE="#1F3A5F","#8C2F39","#2F6B54","#C1662F","#5A6673"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10.5,"axes.edgecolor":SLATE,
 "text.color":"#222","xtick.color":SLATE,"ytick.color":SLATE,
 "axes.spines.top":False,"axes.spines.right":False,"figure.dpi":150,"savefig.dpi":400})

# Fig 33.1: vanishing gradient through time, log scale
def tanh_grad(h): return 1 - h**2
r2 = np.random.default_rng(33)
D_hid = 16
Wh_decay = r2.normal(0, 0.3, (D_hid, D_hid))
def run_and_track_grad(n_steps, Wh_):
    h = np.zeros(D_hid); hs = [h]
    x = r2.normal(size=(n_steps, D_hid))
    for t in range(n_steps):
        h = np.tanh(x[t] + h @ Wh_); hs.append(h)
    grad = np.eye(D_hid)
    for t in range(1, n_steps+1):
        grad = grad @ (Wh_ @ np.diag(tanh_grad(hs[t])))   # forward order, as in c2.py
    return np.linalg.norm(grad)
lengths = list(range(2, 81, 2))
grads = [run_and_track_grad(n, Wh_decay) for n in lengths]
fig, ax = plt.subplots(figsize=(6.4, 3.3))
ax.plot(lengths, grads, color=RED, lw=2)
ax.set_yscale("log")
ax.set_xlabel("sequence length"); ax.set_ylabel("gradient norm, last step to first")   # the axis is log-scaled; a longer label was clipped
ax.set_title("The gradient reaching the first step vanishes as sequences grow",
             color=NAVY, fontsize=11.2, loc="left")
fig.tight_layout(); fig.savefig("fig33_1.png", bbox_inches="tight")

# Fig 33.2: recall accuracy, plain RNN vs attention, across sequence length
# the accuracies Step 5 and Step 6 print (c5.py, c6.py), copied from the book's own table.
# They are typed rather than recomputed on purpose: the length-40 plain-RNN run is
# numerically unstable and its value depends on the NumPy build's BLAS library (0.3250 in
# the book and in the pinned environment; 0.3050 and 0.3350 seen elsewhere; see
# docs/REPRODUCIBILITY.md), and the figure must agree with the printed table.
lens = [2, 5, 10, 20, 40]
plain = [1.0, 1.0, 0.66, 0.305, 0.325]
attn = [1.0, 1.0, 1.0, 1.0, 0.995]
fig, ax = plt.subplots(figsize=(6.4, 3.3))
ax.plot(lens, plain, 'o-', color=RED, lw=2, label="plain RNN (last hidden state only)")
ax.plot(lens, attn, 'o-', color=NAVY, lw=2, label="RNN with attention")
ax.axhline(1/3, color=SLATE, ls='--', lw=1)
ax.text(30, 0.36, "chance (3 classes)", fontsize=9, color=SLATE)
ax.set_xlabel("sequence length"); ax.set_ylabel("recall accuracy")
ax.set_title("Recalling the first element: attention finds what training could not",
             color=NAVY, fontsize=11.2, loc="left")
ax.legend(frameon=False, loc="center right")
fig.tight_layout(); fig.savefig("fig33_2.png", bbox_inches="tight")
print("ok")
