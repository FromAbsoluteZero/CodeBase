import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
exec(open('_lib.py').read())
NAVY,RED,GREEN,ORANGE,SLATE="#1F3A5F","#8C2F39","#2F6B54","#C1662F","#5A6673"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10.5,"axes.edgecolor":SLATE,
 "text.color":"#222","xtick.color":SLATE,"ytick.color":SLATE,
 "axes.spines.top":False,"axes.spines.right":False,"figure.dpi":150})

names=["drop City","one-hot all\n(189 cols)","ordinal code","target encode\n(cross-fitted)"]
def build(step, cols):
    num=Pipeline([("imp",SimpleImputer(strategy="median")),("sc",StandardScaler())])
    return Pipeline([("pre",ColumnTransformer([("n",num,NUM),("c",step,cols)])),
                     ("clf",LogisticRegression(max_iter=2000))])
opts=[(OneHotEncoder(handle_unknown="ignore"),LOWCARD),
      (OneHotEncoder(handle_unknown="ignore"),LOWCARD+["City"]),
      (OrdinalEncoder(handle_unknown="use_encoded_value",unknown_value=-1),LOWCARD+["City"]),
      (TargetEncoder(random_state=0),LOWCARD+["City"])]
means=[];sds=[]
for step,cols in opts:
    s=cross_val_score(build(step,cols),df,y,cv=cv,scoring="roc_auc")
    means.append(s.mean()); sds.append(s.std())
fig,ax=plt.subplots(figsize=(6.8,3.4))
x=np.arange(4)
cols=[GREEN,RED,NAVY,NAVY]
ax.bar(x,means,yerr=sds,capsize=5,color=cols,width=.6)
ax.set_xticks(x); ax.set_xticklabels(names,fontsize=9.2)
ax.set_ylim(0.60,0.70); ax.set_ylabel("cross-validated AUC")
ax.axhline(means[0],color=SLATE,ls=':',lw=1)
ax.set_title("Four ways to handle a 180-level column that carries no signal",
             color=NAVY,fontsize=11.3,loc="left")
fig.tight_layout(); fig.savefig("fig24_1.png",bbox_inches="tight")
print("ok")
