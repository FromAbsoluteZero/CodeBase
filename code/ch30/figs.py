import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
exec(open('_lib.py').read())
NAVY,RED,GREEN,ORANGE,SLATE="#1F3A5F","#8C2F39","#2F6B54","#C1662F","#5A6673"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10.5,"axes.edgecolor":SLATE,
 "text.color":"#222","xtick.color":SLATE,"ytick.color":SLATE,
 "axes.spines.top":False,"axes.spines.right":False,"figure.dpi":150})

# Fig 30.1: network architecture diagram
fig, ax = plt.subplots(figsize=(6.6, 3.2)); ax.axis("off")
ax.set_xlim(0, 10); ax.set_ylim(-0.7, 5.2)
def layer(x, n, color, label, y0=0.6, y1=4.4):
    ys = np.linspace(y0, y1, n)
    for y in ys:
        ax.add_patch(plt.Circle((x, y), 0.13, fc=color, ec="white", lw=1, zorder=3))
    ax.text(x, y0-0.5, label, ha="center", fontsize=8.6, color=SLATE)
    return ys
in_y = layer(1.2, 6, "#C8CED8", "input\n64 pixels")
h_y  = layer(4.5, 8, NAVY, "hidden\n32 neurons, ReLU")
out_y = layer(7.8, 6, ORANGE, "output\n10 digits, softmax")
for a in in_y:
    for b in h_y:
        ax.plot([1.2,4.5],[a,b], color="#D8DEE6", lw=.4, zorder=1)
for a in h_y:
    for b in out_y:
        ax.plot([4.5,7.8],[a,b], color="#D8DEE6", lw=.4, zorder=1)
ax.text(4.5, 4.92, "forward pass", fontsize=9.5, color=NAVY, ha="center")
ax.annotate("", xy=(7.6,4.75), xytext=(2.0,4.75),
            arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.3))
ax.text(4.5, -0.42, "backward pass (the gradient)", fontsize=9.5, color=RED, ha="center")
ax.annotate("", xy=(2.0,-0.15), xytext=(7.6,-0.15),
            arrowprops=dict(arrowstyle="->", color=RED, lw=1.3))
ax.set_title("Two weight matrices, one nonlinearity between them",
             color=NAVY, fontsize=11.5, loc="left")
fig.tight_layout(); fig.savefig("fig30_1.png", bbox_inches="tight")

# Fig 30.2: loss and accuracy over training -- identical seed (30) to
# c5.py, so this figure and the printed table describe the same run.
D_in, H, D_out = 64, 32, 10
r5 = np.random.default_rng(30)
W1 = r5.normal(0, np.sqrt(2/D_in), (D_in, H)); b1 = np.zeros(H)
W2 = r5.normal(0, np.sqrt(2/H), (H, D_out));    b2 = np.zeros(D_out)
Ytr = np.eye(10)[ytr]
def softmax(z):
    z = z - z.max(axis=-1, keepdims=True); e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)
losses, accs = [], []
for epoch in range(401):
    z1 = Xtr @ W1 + b1; a1 = np.maximum(0, z1)
    p = softmax(a1 @ W2 + b2)
    loss = -np.sum(Ytr*np.log(p+1e-12))/len(Xtr)
    dz2 = (p-Ytr)/len(Xtr)
    dW2, db2 = a1.T@dz2, dz2.sum(0)
    dz1 = (dz2@W2.T)*(z1>0)
    dW1, db1 = Xtr.T@dz1, dz1.sum(0)
    W1-=0.5*dW1; b1-=0.5*db1; W2-=0.5*dW2; b2-=0.5*db2
    if epoch % 5 == 0:
        zt1 = Xte@W1+b1; at1=np.maximum(0,zt1); pt=softmax(at1@W2+b2)
        losses.append(loss); accs.append((pt.argmax(1)==yte).mean())
ep = list(range(0,401,5))
fig, ax1 = plt.subplots(figsize=(6.6,3.3))
ax1.plot(ep, losses, color=RED, lw=2)
ax1.set_xlabel("epoch"); ax1.set_ylabel("training loss", color=RED)
ax1.tick_params(axis='y', colors=RED)
ax2 = ax1.twinx()
ax2.plot(ep, accs, color=NAVY, lw=2)
ax2.set_ylabel("test accuracy", color=NAVY)
ax2.tick_params(axis='y', colors=NAVY)
ax2.spines['top'].set_visible(False)
ax1.set_title("Loss falls, accuracy rises, from the same gradient",
              color=NAVY, fontsize=11.5, loc="left")
fig.tight_layout(); fig.savefig("fig30_2.png", bbox_inches="tight")
print("ok")
