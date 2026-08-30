import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
exec(open('_lib.py').read())
NAVY,RED,GREEN,ORANGE,SLATE="#1F3A5F","#8C2F39","#2F6B54","#C1662F","#5A6673"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10.5,"axes.edgecolor":SLATE,
 "text.color":"#222","xtick.color":SLATE,"ytick.color":SLATE,
 "axes.spines.top":False,"axes.spines.right":False,"figure.dpi":150})

# Fig 34.1: unscaled vs scaled softmax over 5 keys
raw = np.array([9.78, 17.58, 14.82, -6.37, 4.69])
d = 64
unscaled = softmax(raw)
scaled = softmax(raw / np.sqrt(d))
fig, ax = plt.subplots(1, 2, figsize=(7.2, 3.0))
labels = [f"pos {i}" for i in range(5)]
ax[0].bar(labels, unscaled, color=RED)
ax[0].set_title("unscaled: nearly one-hot", color=NAVY, fontsize=10.8)
ax[0].set_ylim(0, 1)
ax[1].bar(labels, scaled, color=NAVY)
ax[1].set_title("scaled by 1/\u221ad_k: genuinely graded", color=NAVY, fontsize=10.8)
ax[1].set_ylim(0, 1)
fig.suptitle("The same five scores, before and after scaling", color=NAVY,
             fontsize=11.5, x=0.02, ha="left")
fig.tight_layout(); fig.savefig("fig34_1.png", bbox_inches="tight")

# Fig 34.2: attention weight on position 0 vs chance, across lengths
lengths = [2, 5, 10, 20, 40]
weight_pos0 = [0.5556, 0.2079, 0.1072, 0.0502, 0.0252]
chance = [1/L for L in lengths]
transformer_acc = [1.0, 0.895, 0.735, 0.56, 0.475]
rnn_attn_acc = [1.0, 1.0, 0.99, 0.995, 0.99]

fig, ax = plt.subplots(1, 2, figsize=(7.6, 3.5))
ax[0].plot(lengths, weight_pos0, 'o-', color=RED, lw=2, label="learned weight on position 0")
ax[0].plot(lengths, chance, '--', color=SLATE, lw=1.3, label="uniform (chance) weight")
ax[0].set_xlabel("sequence length"); ax[0].set_ylabel("attention weight on position 0")
ax[0].set_title("Learned attention decays\nto chance as length grows",
               color=NAVY, fontsize=10.3, loc="left")
ax[0].legend(frameon=False, fontsize=8.2)

ax[1].plot(lengths, rnn_attn_acc, 'o-', color=NAVY, lw=2, label="Ch33 attention (free query)")
ax[1].plot(lengths, transformer_acc, 'o-', color=RED, lw=2, label="self-attention (content query)")
ax[1].set_xlabel("sequence length"); ax[1].set_ylabel("recall accuracy")
ax[1].set_title("...and recall accuracy\nfalls with it", color=NAVY, fontsize=10.3, loc="left")
ax[1].legend(frameon=False, fontsize=8.2, loc="center left")
fig.tight_layout(); fig.savefig("fig34_2.png", bbox_inches="tight")
print("ok")
