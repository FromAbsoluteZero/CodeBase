import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
exec(open('_lib.py').read())
NAVY,RED,GREEN,ORANGE,SLATE="#1F3A5F","#8C2F39","#2F6B54","#C1662F","#5A6673"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10.5,"axes.edgecolor":SLATE,
 "text.color":"#222","xtick.color":SLATE,"ytick.color":SLATE,
 "axes.spines.top":False,"axes.spines.right":False,"figure.dpi":150})
m=make_pipeline(StandardScaler(),LogisticRegression(max_iter=5000)).fit(Xtr,ytr)
pr=m.predict_proba(Xte)[:,1]; p_star=C_FP/(C_FP+C_FN)

grid=np.geomspace(0.0005,0.6,300)
def parts(th):
    pred=pr>=th
    fp=int((pred&(yte==0)).sum()); fn=int((~pred&(yte==1)).sum())
    return C_FP*fp, C_FN*fn
rev=np.array([parts(t)[0] for t in grid]); miss=np.array([parts(t)[1] for t in grid])
tot=rev+miss
fig,ax=plt.subplots(figsize=(6.8,3.5))
ax.plot(grid,rev,color=NAVY,lw=1.8,label="cost of reviews")
ax.plot(grid,miss,color=ORANGE,lw=1.8,label="cost of missed fraud")
ax.plot(grid,tot,'--',color=RED,lw=2.4,label="total")
ax.axvline(p_star,color=SLATE,ls=':',lw=1.3)
ax.annotate(f"p* = {p_star:.4f}",xy=(p_star,tot.min()*1.05),
            xytext=(p_star*0.30,tot.min()*1.9),fontsize=9.2,color=SLATE,
            arrowprops=dict(arrowstyle="->",color=SLATE,lw=.9))
ax.plot(grid[tot.argmin()],tot.min(),'o',color=RED,ms=7,zorder=5)
ax.axvline(0.5,color=SLATE,ls='--',lw=1)
ax.text(0.5*1.05,4e3,"default\n0.5",fontsize=9,color=SLATE)
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlabel("threshold (log scale)"); ax.set_ylabel("cost (log scale)")
ax.set_ylim(2e3, 1.4e5)
ax.set_title("The two costs move in opposite directions; the total has a minimum",
             color=NAVY,fontsize=11.3,loc="left")
ax.legend(frameon=False,fontsize=9,loc="upper right")
fig.tight_layout(); fig.savefig("fig23_1.png",bbox_inches="tight")
print("ok")
