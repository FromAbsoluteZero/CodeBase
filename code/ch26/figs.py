import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
exec(open('_lib.py').read())
from sklearn.datasets import make_moons
NAVY,RED,GREEN,ORANGE,SLATE="#1F3A5F","#8C2F39","#2F6B54","#C1662F","#5A6673"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10.5,"axes.edgecolor":SLATE,
 "text.color":"#222","xtick.color":SLATE,"ytick.color":SLATE,
 "axes.spines.top":False,"axes.spines.right":False,"figure.dpi":150})

# Fig 26.1 choosing k: inertia vs silhouette vs ARI
ks=range(2,9); inertia=[];sil=[];ari=[]
for k in ks:
    km=KMeans(k,n_init=10,random_state=0).fit(X)
    inertia.append(km.inertia_); sil.append(silhouette_score(X,km.labels_))
    ari.append(adjusted_rand_score(truth,km.labels_))
fig,ax=plt.subplots(1,2,figsize=(7.6,3.2))
ax[0].plot(list(ks),inertia,'o-',color=NAVY,lw=2)
ax[0].set_xlabel("k"); ax[0].set_ylabel("inertia")
ax[0].set_title("Inertia always falls",color=NAVY,fontsize=11)
ax[1].plot(list(ks),sil,'o-',color=ORANGE,lw=2,label="silhouette (no labels)")
ax[1].plot(list(ks),ari,'o-',color=GREEN,lw=2,label="ARI (knows the truth)")
ax[1].axvline(4,color=SLATE,ls=':',lw=1.2)
ax[1].text(4.1,0.31,"true k = 4",fontsize=9,color=SLATE)
ax[1].set_xlabel("k"); ax[1].set_ylabel("score")
ax[1].set_title("...and silhouette picks the wrong k",color=NAVY,fontsize=11)
ax[1].legend(frameon=False,fontsize=8.6,loc="lower left")
fig.tight_layout(); fig.savefig("fig26_1.png",bbox_inches="tight")

# Fig 26.2 shape defeats k-means
Xm,ym=make_moons(n_samples=1200,noise=0.06,random_state=0)
Xm=StandardScaler().fit_transform(Xm)
labs=[("true shape",ym),
      ("k-means (k=2)",KMeans(2,n_init=10,random_state=0).fit_predict(Xm)),
      ("DBSCAN",DBSCAN(eps=0.30,min_samples=8).fit_predict(Xm))]
fig,ax=plt.subplots(1,3,figsize=(7.8,2.8))
for a_,(t,l) in zip(ax,labs):
    for v,c in zip(sorted(set(l)),[NAVY,ORANGE,SLATE]):
        m=l==v
        a_.scatter(Xm[m,0],Xm[m,1],s=5,color="#C8CED8" if v==-1 else c)
    a_.set_title(t,color=NAVY,fontsize=10.5); a_.set_xticks([]); a_.set_yticks([])
fig.suptitle("Same points, same k. Only the shape assumption differs",
             color=NAVY,fontsize=11.5,x=.02,ha="left")
fig.tight_layout(); fig.savefig("fig26_2.png",bbox_inches="tight")
print("ok")
