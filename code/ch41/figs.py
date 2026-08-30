import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
exec(open('_lib.py').read())
exec(open('c1.py').read().split('print(f')[0])
NAVY,RED,GREEN,ORANGE,SLATE="#1F3A5F","#8C2F39","#2F6B54","#C1662F","#5A6673"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10.5,"axes.edgecolor":SLATE,
 "text.color":"#222","xtick.color":SLATE,"ytick.color":SLATE,
 "axes.spines.top":False,"axes.spines.right":False,"figure.dpi":150})

# Fig 41.1: task success rate vs steps, for several per-step accuracies
steps_range = list(range(1, 41))
fig, ax = plt.subplots(figsize=(6.6, 3.4))
for p, color in [(0.99, GREEN), (0.95, NAVY), (0.90, ORANGE), (0.80, RED)]:
    rates = [p**n for n in steps_range]
    ax.plot(steps_range, rates, lw=2, color=color, label=f"p = {p}")
ax.set_xlabel("number of steps in the task"); ax.set_ylabel("task success rate")
ax.set_title("A small per-step error rate compounds into a large one",
             color=NAVY, fontsize=11.3, loc="left")
ax.legend(frameon=False, title="per-step accuracy")
fig.tight_layout(); fig.savefig("fig41_1.png", bbox_inches="tight")

# Fig 41.2: stopping threshold tradeoff
thresholds = [0.5, 0.7, 0.85, 0.95, 0.99]
premature = [1.0000, 0.9832, 0.6785, 0.2976, 0.1847]
wasted = [0.000, 0.000, 0.043, 0.366, 0.701]
fig, ax1 = plt.subplots(figsize=(6.6, 3.3))
ax1.plot(thresholds, premature, 'o-', color=RED, lw=2)
ax1.set_xlabel("stopping-confidence threshold"); ax1.set_ylabel("premature-stop rate", color=RED)
ax1.tick_params(axis='y', colors=RED)
ax2 = ax1.twinx()
ax2.plot(thresholds, wasted, 'o-', color=NAVY, lw=2)
ax2.set_ylabel("average wasted steps", color=NAVY)
ax2.tick_params(axis='y', colors=NAVY)
ax2.spines['top'].set_visible(False)
ax1.set_title("Two costs move in opposite directions as the threshold rises",
             color=NAVY, fontsize=11.1, loc="left")
fig.tight_layout(); fig.savefig("fig41_2.png", bbox_inches="tight")
print("ok")
