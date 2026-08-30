import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np, pandas as pd
exec(open('_lib.py').read())
NAVY,RED,GREEN,ORANGE,SLATE="#1F3A5F","#8C2F39","#2F6B54","#C1662F","#5A6673"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10.5,"axes.edgecolor":SLATE,
 "text.color":"#222","xtick.color":SLATE,"ytick.color":SLATE,
 "axes.spines.top":False,"axes.spines.right":False,"figure.dpi":150})

# Fig 25.1 grid vs random coverage
fig,ax=plt.subplots(1,2,figsize=(7.4,3.2))
g=np.array([[a,b] for a in np.linspace(.1,.9,5) for b in np.linspace(.1,.9,5)])
r=np.random.default_rng(3).uniform(.05,.95,(25,2))
for a_,pts,t,c in [(ax[0],g,"grid search, 25 fits",NAVY),(ax[1],r,"random search, 25 fits",ORANGE)]:
    a_.scatter(pts[:,0],pts[:,1],s=26,color=c)
    a_.set_title(t,color=NAVY,fontsize=11)
    a_.set_xlabel("parameter that matters"); a_.set_xlim(0,1); a_.set_ylim(0,1)
    a_.set_yticks([])
    for v in np.unique(pts[:,0]):
        a_.plot([v,v],[0,0.045],color=c,lw=2)
ax[0].set_ylabel("parameter that does not")
ax[0].text(.5,-.30,"5 distinct values tried",ha="center",fontsize=9,color=SLATE,transform=ax[0].transAxes)
ax[1].text(.5,-.30,"25 distinct values tried",ha="center",fontsize=9,color=SLATE,transform=ax[1].transAxes)
fig.suptitle("Same budget. Random search explores five times more of the axis that matters",
             color=NAVY,fontsize=11.5,x=.02,ha="left")
fig.tight_layout(); fig.savefig("fig25_1.png",bbox_inches="tight")

# Fig 25.2 optimism vs candidates
from sklearn.datasets import make_classification
X,yy=make_classification(n_samples=600,n_features=20,n_informative=6,flip_y=0.15,random_state=0)
space={"learning_rate":loguniform(1e-3,3e-1),"max_depth":randint(2,8),
       "max_iter":randint(60,300),"l2_regularization":loguniform(1e-3,1e1)}
outer=StratifiedKFold(4,shuffle=True,random_state=0)
ns=[3,5,10,20,40,60]; inner=[];nest=[]
for n in ns:
    s=RandomizedSearchCV(HistGradientBoostingClassifier(random_state=0),space,
                         n_iter=n,cv=3,random_state=0,n_jobs=-1).fit(X,yy)
    inner.append(s.best_score_); nest.append(cross_val_score(s,X,yy,cv=outer,n_jobs=-1).mean())
fig,ax=plt.subplots(figsize=(6.6,3.3))
ax.plot(ns,inner,'o-',color=ORANGE,lw=2,label="tuned (inner) score")
ax.plot(ns,nest,'o-',color=NAVY,lw=2,label="nested (honest) estimate")
ax.fill_between(ns,nest,inner,color=ORANGE,alpha=.10)
ax.set_xscale("log"); ax.set_xticks(ns); ax.set_xticklabels(ns)
ax.set_xlabel("candidates searched"); ax.set_ylabel("accuracy")
ax.set_title("Search harder and the reported score improves faster than the model does",
             color=NAVY,fontsize=11.3,loc="left")
ax.legend(frameon=False,fontsize=9,loc="lower left")
fig.tight_layout(); fig.savefig("fig25_2.png",bbox_inches="tight")
print("ok")
