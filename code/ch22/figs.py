import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
exec(open('_lib.py').read())
NAVY,RED,GREEN,ORANGE,SLATE="#1F3A5F","#8C2F39","#2F6B54","#C1662F","#5A6673"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10.5,"axes.edgecolor":SLATE,
 "text.color":"#222","xtick.color":SLATE,"ytick.color":SLATE,
 "axes.spines.top":False,"axes.spines.right":False,"figure.dpi":150})
m=make_pipeline(StandardScaler(),LogisticRegression(max_iter=5000)).fit(Xtr,ytr)
p=m.predict_proba(Xte)[:,1]

# Fig 22.1 ROC vs PR side by side
fpr,tpr,_=roc_curve(yte,p); prec,rec,_=precision_recall_curve(yte,p)
fig,ax=plt.subplots(1,2,figsize=(7.6,3.3))
ax[0].plot(fpr,tpr,color=NAVY,lw=2); ax[0].plot([0,1],[0,1],ls='--',color=SLATE,lw=.9)
ax[0].set_xlabel("false positive rate"); ax[0].set_ylabel("true positive rate")
ax[0].set_title(f"ROC  \u2014  AUC {roc_auc_score(yte,p):.3f}",color=NAVY,fontsize=11)
ax[1].plot(rec,prec,color=ORANGE,lw=2)
ax[1].axhline(yte.mean(),ls='--',color=SLATE,lw=.9)
ax[1].text(0.35,yte.mean()+0.02,"base rate 0.43%",fontsize=8.6,color=SLATE)
ax[1].set_xlabel("recall"); ax[1].set_ylabel("precision")
ax[1].set_title(f"Precision-recall  \u2014  AP {average_precision_score(yte,p):.3f}",
                color=NAVY,fontsize=11)
fig.suptitle("The same model, two curves, two very different impressions",
             color=NAVY,fontsize=11.8,x=.02,ha="left")
fig.tight_layout(); fig.savefig("fig22_1.png",bbox_inches="tight")

# Fig 22.2 calibration
gb=HistGradientBoostingClassifier(random_state=0).fit(Xtr,ytr)
fig,ax=plt.subplots(figsize=(5.6,3.4))
for name,mdl,c in [("logistic",m,NAVY),("gradient boosting",gb,ORANGE)]:
    pp=mdl.predict_proba(Xte)[:,1]
    o=np.argsort(pp); xs=[];ys=[]
    for b in range(10):
        idx=o[b*len(pp)//10:(b+1)*len(pp)//10]
        xs.append(pp[idx].mean()); ys.append(yte[idx].mean())
    ax.plot(xs,ys,'o-',color=c,lw=1.8,ms=5,label=name)
lim=[3e-4,6e-2]
ax.plot(lim,lim,ls='--',color=SLATE,lw=1,label="perfect calibration")
ax.set_xscale("log"); ax.set_yscale("log"); ax.set_xlim(lim); ax.set_ylim(lim)
ax.set_xlabel("mean predicted probability"); ax.set_ylabel("observed fraud rate")
ax.set_title("Calibration by decile of predicted risk",color=NAVY,fontsize=11.3,loc="left")
ax.legend(frameon=False,fontsize=9,loc="upper left")
fig.tight_layout(); fig.savefig("fig22_2.png",bbox_inches="tight")
print("ok")
