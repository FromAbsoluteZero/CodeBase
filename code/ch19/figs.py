import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
exec(open('_lib.py').read())
NAVY,RED,GREEN,ORANGE,SLATE="#1F3A5F","#8C2F39","#2F6B54","#C1662F","#5A6673"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10.5,"axes.edgecolor":SLATE,
 "text.color":"#222","xtick.color":SLATE,"ytick.color":SLATE,
 "axes.spines.top":False,"axes.spines.right":False,"figure.dpi":150})

# Fig 19.1 impurity curves
p=np.linspace(1e-9,1-1e-9,400)
H=-(p*np.log2(p)+(1-p)*np.log2(1-p)); G=1-(p**2+(1-p)**2)
fig,ax=plt.subplots(figsize=(6.4,3.2))
ax.plot(p,H,color=NAVY,lw=2,label="entropy (bits)")
ax.plot(p,G,color=ORANGE,lw=2,label="gini impurity")
ax.axvline(0.1215,color=SLATE,ls=':',lw=1.2)
ax.annotate("this dataset\np = 0.1215",xy=(0.1215,0.53),xytext=(0.20,0.82),
            fontsize=9.2,color=SLATE,arrowprops=dict(arrowstyle="->",color=SLATE,lw=.9))
ax.set_xlabel("proportion of the minority class in a group")
ax.set_ylabel("impurity"); ax.legend(frameon=False)
ax.set_title("Both measures peak at a balanced group and vanish at a pure one",
             color=NAVY,fontsize=11.3,loc="left")
fig.tight_layout(); fig.savefig("fig19_1.png",bbox_inches="tight")

# Fig 19.2 leaf risk
t=DecisionTreeClassifier(max_depth=3,random_state=0).fit(Xtr,ytr)
leaf=t.apply(Xtr)
rows=sorted(((ytr[leaf==lf].mean(),(leaf==lf).sum(),lf) for lf in np.unique(leaf)),reverse=True)
p_=[r[0] for r in rows]; n_=[r[1] for r in rows]
fig,ax=plt.subplots(figsize=(6.8,3.3))
ypos=np.arange(len(rows))[::-1]
cols=[RED if v>ytr.mean() else NAVY for v in p_]
ax.barh(ypos,[v*100 for v in p_],color=cols,height=.62)
ax.axvline(ytr.mean()*100,color=SLATE,ls='--',lw=1)
ax.text(ytr.mean()*100+1,ypos[-1]-0.6,"base rate 12.2%",fontsize=9,color=SLATE)
ax.set_yticks(ypos); ax.set_yticklabels([f"{n} people" for n in n_],fontsize=9)
ax.set_xlabel("attrition rate within the leaf  (%)")
ax.set_title("Eight leaves, sorted by risk: the tree is a segmentation",
             color=NAVY,fontsize=11.3,loc="left")
fig.tight_layout(); fig.savefig("fig19_2.png",bbox_inches="tight")
print("ok")
