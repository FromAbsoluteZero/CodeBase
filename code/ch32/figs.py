import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
exec(open('_lib.py').read())
exec(open('c1.py').read().split('img = X_img')[0])
NAVY,RED,GREEN,ORANGE,SLATE="#1F3A5F","#8C2F39","#2F6B54","#C1662F","#5A6673"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10.5,"axes.edgecolor":SLATE,
 "text.color":"#222","xtick.color":SLATE,"ytick.color":SLATE,
 "axes.spines.top":False,"axes.spines.right":False,"figure.dpi":150})

# Fig 32.1: image, filter, feature map
img = X_img[3]
horizontal_edge = vertical_edge.T
feat_v = convolve2d(img, vertical_edge)
feat_h = convolve2d(img, horizontal_edge)

fig, ax = plt.subplots(1, 3, figsize=(7.6, 2.8))
for a, data, title, cmap in [
    (ax[0], img, "input digit", "Greys"),
    (ax[1], feat_v, "vertical-edge filter", "RdBu_r"),
    (ax[2], feat_h, "horizontal-edge filter", "RdBu_r"),
]:
    a.imshow(data, cmap=cmap)
    a.set_title(title, color=NAVY, fontsize=10.5)
    a.set_xticks([]); a.set_yticks([])
fig.suptitle("One image, two filters, two different feature maps",
             color=NAVY, fontsize=11.5, x=0.02, ha="left")
fig.tight_layout(); fig.savefig("fig32_1.png", bbox_inches="tight")

# Fig 32.2: shift robustness, grouped bars
labels = ["original", "shifted 1px"]
fc = [0.9667, 0.3889]
cnn = [0.9167, 0.5667]
x = np.arange(2); w = 0.32
fig, ax = plt.subplots(figsize=(6.2, 3.3))
ax.bar(x - w/2, fc, width=w, color=RED, label="fully connected (logreg)")
ax.bar(x + w/2, cnn, width=w, color=NAVY, label="CNN, 4 filters")
ax.set_xticks(x); ax.set_xticklabels(labels)
ax.set_ylabel("test accuracy")
ax.set_title("A one-pixel shift hurts both models. It hurts the CNN less",
             color=NAVY, fontsize=11.3, loc="left")
ax.legend(frameon=False)
fig.tight_layout(); fig.savefig("fig32_2.png", bbox_inches="tight")
print("ok")
