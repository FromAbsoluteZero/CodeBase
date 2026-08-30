import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
exec(open('_lib.py').read())
NAVY,RED,GREEN,ORANGE,SLATE="#1F3A5F","#8C2F39","#2F6B54","#C1662F","#5A6673"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10.5,"axes.edgecolor":SLATE,
 "text.color":"#222","xtick.color":SLATE,"ytick.color":SLATE,
 "axes.spines.top":False,"axes.spines.right":False,"figure.dpi":150})

depths=[1,2,3,5,8,12,16]; tr=[];te=[]
for d in depths:
    t=DecisionTreeClassifier(max_depth=d,random_state=0).fit(Xtr,ytr)
    tr.append(roc_auc_score(ytr,t.predict_proba(Xtr)[:,1]))
    te.append(roc_auc_score(yte,t.predict_proba(Xte)[:,1]))
fig,ax=plt.subplots(figsize=(6.8,3.4))
ax.plot(depths,tr,'o-',color=RED,lw=2,label="training AUC")
ax.plot(depths,te,'o-',color=NAVY,lw=2,label="test AUC")
i=int(np.argmax(te))
ax.axvline(depths[i],color=SLATE,ls=':',lw=1)
ax.annotate("best test performance",xy=(depths[i],te[i]),
            xytext=(depths[i]+2.2,te[i]-0.09),fontsize=9.5,color=SLATE,
            arrowprops=dict(arrowstyle="->",color=SLATE,lw=.9))
ax.fill_between(depths,te,tr,color=RED,alpha=.08)
ax.set_xlabel("maximum tree depth  (model complexity ->)")
ax.set_ylabel("ROC AUC"); ax.set_ylim(.5,1.02)
ax.set_title("Training performance rises forever; test performance peaks and falls",
             color=NAVY,fontsize=11.5,loc="left")
ax.legend(frameon=False,loc="center right")
fig.tight_layout(); fig.savefig("fig16_2.png",bbox_inches="tight")

# fold spread
fig,ax=plt.subplots(figsize=(6.8,3.2))
ds=[2,3,4,5,6,8,12]; means=[];sds=[]
for d in ds:
    s=cross_val_score(DecisionTreeClassifier(max_depth=d,random_state=0),
                      Xtr,ytr,cv=cv,scoring="roc_auc")
    means.append(s.mean()); sds.append(s.std())
    ax.scatter([d]*5,s,color=SLATE,s=14,zorder=3,alpha=.65)
ax.errorbar(ds,means,yerr=sds,fmt='o-',color=NAVY,lw=2,capsize=4,zorder=4,
            label="mean +/- 1 sd across folds")
ax.set_xlabel("maximum tree depth"); ax.set_ylabel("cross-validated AUC")
ax.set_title("The spread is as large as the differences you would act on",
             color=NAVY,fontsize=11.5,loc="left")
ax.legend(frameon=False)
fig.tight_layout(); fig.savefig("fig16_3.png",bbox_inches="tight")
print("figures written")
