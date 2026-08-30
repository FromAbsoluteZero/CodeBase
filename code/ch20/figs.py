import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
exec(open('_lib.py').read())
NAVY,RED,GREEN,ORANGE,SLATE="#1F3A5F","#8C2F39","#2F6B54","#C1662F","#5A6673"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10.5,"axes.edgecolor":SLATE,
 "text.color":"#222","xtick.color":SLATE,"ytick.color":SLATE,
 "axes.spines.top":False,"axes.spines.right":False,"figure.dpi":150})

# Fig 20.1 variance reduction vs correlation
ks=np.array([1,2,3,5,8,12,20,35,60,100])
fig,ax=plt.subplots(figsize=(6.6,3.3))
for corr,c in [(0.0,NAVY),(0.3,GREEN),(0.6,ORANGE),(0.9,RED)]:
    v=[]
    for k in ks:
        sh=rng.normal(0,np.sqrt(corr),6000)
        ow=rng.normal(0,np.sqrt(1-corr),(6000,int(k)))
        v.append((sh[:,None]+ow).mean(1).var())
    ax.plot(ks,v,'o-',color=c,lw=2,ms=4,label=f"correlation {corr:.1f}")
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlabel("number of models averaged"); ax.set_ylabel("variance of the average")
ax.set_title("Averaging only helps to the extent the errors differ",
             color=NAVY,fontsize=11.3,loc="left")
ax.legend(frameon=False,fontsize=9)
fig.tight_layout(); fig.savefig("fig20_1.png",bbox_inches="tight")

# Fig 20.2 bagging vs boosting curves on hr
from sklearn.tree import DecisionTreeRegressor
r2=np.random.default_rng(0)
bag_p=np.zeros((200,len(Xte))); 
for i in range(200):
    idx=r2.integers(0,len(Xtr),len(Xtr))
    t=DecisionTreeClassifier(max_features=3,random_state=i).fit(Xtr.values[idx],ytr[idx])
    bag_p[i]=t.predict_proba(Xte.values)[:,1]
bag_auc=[roc_auc_score(yte,bag_p[:k].mean(0)) for k in range(1,201)]
f=np.zeros(len(Xtr)); tf=np.zeros(len(Xte)); boost_auc=[]
for _ in range(200):
    p=1/(1+np.exp(-f)); h=DecisionTreeRegressor(max_depth=3,random_state=0).fit(Xtr,ytr-p)
    f+=0.1*h.predict(Xtr); tf+=0.1*h.predict(Xte); boost_auc.append(roc_auc_score(yte,tf))
fig,ax=plt.subplots(figsize=(6.6,3.3))
ax.plot(range(1,201),bag_auc,color=NAVY,lw=2,label="bagging (parallel, averaged)")
ax.plot(range(1,201),boost_auc,color=ORANGE,lw=2,label="boosting (sequential, corrective)")
ax.axhline(0.7297,color=SLATE,ls='--',lw=1)
ax.text(105,0.734,"logistic regression, 0.7297",fontsize=9,color=SLATE)
ax.set_xlabel("number of trees"); ax.set_ylabel("test AUC")
ax.set_title("Two ways to combine trees, and the model that still beats both",
             color=NAVY,fontsize=11.3,loc="left")
ax.legend(frameon=False,fontsize=9,loc="lower right")
fig.tight_layout(); fig.savefig("fig20_2.png",bbox_inches="tight")
print("ok")
