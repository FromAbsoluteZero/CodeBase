import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
exec(open('_lib.py').read())
exec(open('c1.py').read().split('print(f')[0])
exec(open('c2.py').read().split('def group_rates')[1].split('tpr0, fpr0')[0].join(['def group_rates', '']))
NAVY,RED,GREEN,ORANGE,SLATE="#1F3A5F","#8C2F39","#2F6B54","#C1662F","#5A6673"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10.5,"axes.edgecolor":SLATE,
 "text.color":"#222","xtick.color":SLATE,"ytick.color":SLATE,
 "axes.spines.top":False,"axes.spines.right":False,"figure.dpi":150})

# Fig 44.1: calibration by group -- predicted score vs actual repay rate
buckets = ['0.4-0.5', '0.5-0.6', '0.6-0.7', '0.7-0.8']
r0_rates = [0.1875, 0.3548, 0.3548, 0.6250]
r1_rates = [0.5682, 0.7000, 0.8254, 0.8906]
x = np.arange(len(buckets))
fig, ax = plt.subplots(figsize=(6.4, 3.4))
w = 0.35
ax.bar(x - w/2, r0_rates, width=w, color=RED, label="group 0")
ax.bar(x + w/2, r1_rates, width=w, color=NAVY, label="group 1")
ax.plot(x, [(lo+0.05) for lo in (0.45,0.55,0.65,0.75)], 'k--', lw=1, label="score midpoint (if calibrated)")
ax.set_xticks(x); ax.set_xticklabels(buckets)
ax.set_xlabel("predicted repayment score bucket"); ax.set_ylabel("actual repayment rate")
ax.set_title("The identical predicted score means very different things by group",
             color=NAVY, fontsize=10.6, loc="left")
ax.legend(frameon=False, fontsize=8.5)
fig.tight_layout(); fig.savefig("fig44_1.png", bbox_inches="tight")

# Fig 44.2: the threshold consequence
fig, ax = plt.subplots(figsize=(6.2, 3.3))
groups = ['group 0\n(threshold moved\nto match FPR)', 'group 1\n(unchanged)']
thresholds = [0.914, 0.5]
ax.bar(groups, thresholds, color=[RED, NAVY], width=0.5)
ax.axhline(0.5, color=SLATE, ls=':', lw=1)
ax.set_ylabel("approval threshold")
ax.set_title("Equalizing false-positive rate required very different\nthresholds per group",
             color=NAVY, fontsize=10.6, loc="left")
fig.tight_layout(); fig.savefig("fig44_2.png", bbox_inches="tight")
print("ok")
