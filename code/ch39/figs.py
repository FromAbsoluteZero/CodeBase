import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
exec(open('_lib.py').read())
exec(open('c1.py').read().split('print(f')[0])
exec(open('c2.py').read().split('print(f')[0])
exec(open('c3.py').read().split('print(f')[0])
NAVY,RED,GREEN,ORANGE,SLATE="#1F3A5F","#8C2F39","#2F6B54","#C1662F","#5A6673"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10.5,"axes.edgecolor":SLATE,
 "text.color":"#222","xtick.color":SLATE,"ytick.color":SLATE,
 "axes.spines.top":False,"axes.spines.right":False,"figure.dpi":150})

# Fig 39.1: rank vs held-out MSE, with the true rank marked
ranks = [1, 2, 4, 8, 16, 32]
mses = []
for rank in ranks:
    _, _, loss = train_lora(Xtr, Htr_target, Xte, Hte_target, W_pretrained, rank=rank, seed=39)
    mses.append(loss)

fig, ax = plt.subplots(figsize=(6.6, 3.4))
ax.plot(ranks, mses, 'o-', color=NAVY, lw=2, label="LoRA at this rank")
ax.axhline(loss_full, color=RED, ls='--', lw=1.3, label=f"full fine-tune ({full_params:,} params)")
ax.axvline(4, color=SLATE, ls=':', lw=1.2)
ax.text(4.3, 1.3, "true rank = 4", fontsize=9, color=SLATE)
ax.set_xscale("log")
ax.set_xlabel("LoRA rank (log scale)"); ax.set_ylabel("held-out MSE")
ax.set_title("Performance jumps at the true rank, then plateaus",
             color=NAVY, fontsize=11.3, loc="left")
ax.legend(frameon=False, fontsize=9)
fig.tight_layout(); fig.savefig("fig39_1.png", bbox_inches="tight")

# Fig 39.2: parameter count vs rank, log-log, with full fine-tune marked
param_counts = [D * r_ * 2 for r_ in ranks]
fig, ax = plt.subplots(figsize=(6.6, 3.3))
ax.plot(ranks, param_counts, 'o-', color=NAVY, lw=2, label="LoRA parameters")
ax.axhline(full_params, color=RED, ls='--', lw=1.3, label="full fine-tune parameters")
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlabel("LoRA rank (log scale)"); ax.set_ylabel("trainable parameters (log scale)")
ax.set_title("Even rank 32 trains 4x fewer parameters than full fine-tuning",
             color=NAVY, fontsize=11.1, loc="left")
ax.legend(frameon=False, fontsize=9)
fig.tight_layout(); fig.savefig("fig39_2.png", bbox_inches="tight")
print("ok")
