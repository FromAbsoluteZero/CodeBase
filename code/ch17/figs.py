import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np, pandas as pd, warnings
warnings.filterwarnings("ignore")
exec(open('_lib.py').read()); exec(open('c4.py').read())
NAVY,RED,GREEN,ORANGE,SLATE="#1F3A5F","#8C2F39","#2F6B54","#C1662F","#5A6673"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10.5,"axes.edgecolor":SLATE,
 "text.color":"#222","xtick.color":SLATE,"ytick.color":SLATE,
 "axes.spines.top":False,"axes.spines.right":False,"figure.dpi":150})

# ---- Fig 17.1 the decomposition
r2 = np.random.default_rng(0)
truth = lambda x: np.sin(1.4*x)+0.3*x
xs = np.linspace(-3,3,200); runs=300
degs=[1,2,3,4,5,6,7,8,9]; B=[];V=[];T=[]
for deg in degs:
    P=np.zeros((runs,len(xs)))
    for r in range(runs):
        x=r2.uniform(-3,3,40); y=truth(x)+r2.normal(0,.45,40)
        P[r]=np.polyval(np.polyfit(x,y,deg),xs)
    b=((P.mean(0)-truth(xs))**2).mean(); v=P.var(0).mean()
    B.append(b);V.append(v);T.append(b+v+.45**2)
fig,ax=plt.subplots(figsize=(6.9,3.4))
ax.plot(degs,B,'o-',color=NAVY,lw=2,label="bias$^2$")
ax.plot(degs,V,'o-',color=ORANGE,lw=2,label="variance")
ax.plot(degs,T,'o--',color=RED,lw=2.2,label="total error")
ax.axhline(.45**2,color=SLATE,ls='--',lw=.9)
ax.text(1.05,.45**2+.03,"irreducible noise",fontsize=8.6,color=SLATE)
i=int(np.argmin(T)); ax.axvline(degs[i],color=GREEN,ls=':',lw=1.2)
ax.text(degs[i]+.12,max(T)*.62,"best total",fontsize=9,color=GREEN)
ax.set_yscale("log"); ax.set_xlabel("polynomial degree  (model complexity ->)")
ax.set_ylabel("error (log scale)")
ax.set_title("The decomposition is exact, not a metaphor",color=NAVY,fontsize=11.5,loc="left")
ax.legend(frameon=False,loc="upper left")
fig.tight_layout(); fig.savefig("fig17_1.png",bbox_inches="tight")

# ---- Fig 17.2 coefficient paths
Xo,yo = o[feats].values, o["rev"].values
alphas=np.geomspace(.01,300,40)
paths={"ridge":[], "lasso":[]}
for a in alphas:
    for name,mdl in [("ridge",Ridge(alpha=a)),("lasso",Lasso(alpha=a,max_iter=50000))]:
        m=make_pipeline(StandardScaler(),mdl).fit(Xo,yo)
        paths[name].append(m[-1].coef_)
fig,axes=plt.subplots(1,2,figsize=(7.6,3.2),sharey=True)
for ax,name in zip(axes,["ridge","lasso"]):
    P=np.array(paths[name])
    for j,f in enumerate(feats):
        keep = f in ("units","avg_price","units_copy")
        ax.plot(alphas,P[:,j],lw=2 if keep else 1,
                color={"units":NAVY,"avg_price":GREEN,"units_copy":ORANGE}.get(f,"#C8CED8"),
                label=f if keep else None)
    ax.set_xscale("log"); ax.axhline(0,color=SLATE,lw=.8)
    ax.set_xlabel("penalty strength (alpha)")
    ax.set_title(f"{name}  (L{'2' if name=='ridge' else '1'})",color=NAVY,fontsize=11)
axes[0].set_ylabel("coefficient")
axes[1].legend(frameon=False,fontsize=8.6,loc="upper right")
fig.suptitle("L2 shrinks everything smoothly; L1 sets features to exactly zero",
             color=NAVY,fontsize=11.5,x=.02,ha="left")
fig.tight_layout(); fig.savefig("fig17_2.png",bbox_inches="tight")
print("ok")
