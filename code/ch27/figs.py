import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
exec(open('_lib.py').read())
NAVY,RED,GREEN,ORANGE,SLATE="#1F3A5F","#8C2F39","#2F6B54","#C1662F","#5A6673"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10.5,"axes.edgecolor":SLATE,
 "text.color":"#222","xtick.color":SLATE,"ytick.color":SLATE,
 "axes.spines.top":False,"axes.spines.right":False,"figure.dpi":150})
Xs=StandardScaler().fit_transform(Xd)

# Fig 27.1 scree + accuracy cost
p=PCA().fit(Xs); cum=np.cumsum(p.explained_variance_ratio_)
from sklearn.pipeline import make_pipeline
cv=StratifiedKFold(5,shuffle=True,random_state=0)
ks=[5,10,20,30,40,64]
acc=[cross_val_score(make_pipeline(StandardScaler(),PCA(n_components=k,random_state=0),
     LogisticRegression(max_iter=5000)),Xd,yd,cv=cv).mean() for k in ks]
fig,ax=plt.subplots(1,2,figsize=(7.6,3.2))
ax[0].plot(range(1,65),cum,color=NAVY,lw=2)
for t,c in [(0.90,ORANGE),(0.95,RED)]:
    k=int(np.searchsorted(cum,t)+1)
    ax[0].plot([k,k],[0,t],ls=':',color=c,lw=1.2); ax[0].plot([0,k],[t,t],ls=':',color=c,lw=1.2)
    ax[0].text(k+1.5,t-0.07,f"{t:.0%} at {k}",fontsize=8.8,color=c)
ax[0].set_xlabel("components kept"); ax[0].set_ylabel("cumulative variance")
ax[0].set_title("Sixty-four pixels, far fewer directions",color=NAVY,fontsize=11)
ax[1].plot(ks,acc,'o-',color=NAVY,lw=2)
ax[1].axhline(acc[-1],ls='--',color=SLATE,lw=1)
ax[1].text(22,acc[-1]-0.017,"all 64 pixels",fontsize=8.8,color=SLATE)
ax[1].set_xlabel("components kept"); ax[1].set_ylabel("accuracy")
ax[1].set_title("...and what compressing costs",color=NAVY,fontsize=11)
fig.tight_layout(); fig.savefig("fig27_1.png",bbox_inches="tight")

# Fig 27.2 PCA vs t-SNE view
pca2=PCA(n_components=2,random_state=0).fit_transform(Xs)
ts2=TSNE(n_components=2,init="pca",perplexity=30,random_state=0).fit_transform(Xs)
fig,ax=plt.subplots(1,2,figsize=(7.6,3.5))
for a_,(t,e) in zip(ax,[("PCA \u2014 2 components",pca2),("t-SNE \u2014 2 dimensions",ts2)]):
    sc=a_.scatter(e[:,0],e[:,1],c=yd,cmap="tab10",s=5)
    a_.set_title(t,color=NAVY,fontsize=11); a_.set_xticks([]); a_.set_yticks([])
fig.suptitle("The same 1,797 digits, projected two ways",color=NAVY,fontsize=11.5,x=.02,ha="left")
fig.tight_layout(); fig.savefig("fig27_2.png",bbox_inches="tight")
print("ok")
