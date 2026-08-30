import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
exec(open('_lib.py').read())
NAVY,RED,GREEN,ORANGE,SLATE="#1F3A5F","#8C2F39","#2F6B54","#C1662F","#5A6673"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10.5,"axes.edgecolor":SLATE,
 "text.color":"#222","xtick.color":SLATE,"ytick.color":SLATE,
 "axes.spines.top":False,"axes.spines.right":False,"figure.dpi":150})

# Fig 18.1 loss against step for three optimizers
X,y,_=make_problem(cond=10)
def curve(kind,eta,steps=250,beta=0.9,b1=0.9,b2=0.999):
    w=np.zeros(2); v=np.zeros(2); m=np.zeros(2); s=np.zeros(2); H=[]
    for t in range(1,steps+1):
        gr=grad(X,y,w)
        if kind=="plain": w=w-eta*gr
        elif kind=="momentum":
            v=beta*v+gr; w=w-eta*v
        else:
            m=b1*m+(1-b1)*gr; s=b2*s+(1-b2)*gr*gr
            w=w-eta*(m/(1-b1**t))/(np.sqrt(s/(1-b2**t))+1e-8)
        H.append(loss(X,y,w))
    return H
best=loss(X,y,np.linalg.lstsq(X,y,rcond=None)[0])
fig,ax=plt.subplots(figsize=(6.6,3.4))
for kind,eta,c,lab in [("plain",0.0094,NAVY,"plain descent, eta 0.0094"),
                       ("momentum",0.0035,ORANGE,"momentum, eta 0.0035"),
                       ("adam",0.10,GREEN,"Adam, eta 0.10")]:
    H=curve(kind,eta)
    ax.plot(range(1,len(H)+1),np.array(H)-best+1e-6,color=c,lw=2,label=lab)
ax.set_yscale("log"); ax.set_xlabel("step")
ax.set_ylabel("loss above the best achievable (log)")
ax.set_title("Same problem, same starting point, three update rules",
             color=NAVY,fontsize=11.5,loc="left")
ax.legend(frameon=False,fontsize=9)
fig.tight_layout(); fig.savefig("fig18_1.png",bbox_inches="tight")

# Fig 18.2 schedules
fig,ax=plt.subplots(figsize=(6.4,2.8))
T=1500; t=np.arange(1,T+1); E=0.006
ax.plot(t,np.full(T,E),color=NAVY,lw=2,label="constant")
ax.plot(t,E*(0.1**(t//(T//3))),color=ORANGE,lw=2,label="step decay")
ax.plot(t,E*0.5*(1+np.cos(np.pi*t/T)),color=GREEN,lw=2,label="cosine decay")
ax.set_xlabel("update"); ax.set_ylabel("learning rate"); ax.set_yscale("log")
ax.set_title("Three schedules over the same run",color=NAVY,fontsize=11.3,loc="left")
ax.legend(frameon=False,fontsize=9)
fig.tight_layout(); fig.savefig("fig18_2.png",bbox_inches="tight")
print("ok")
