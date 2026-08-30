import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
exec(open('_lib.py').read())
NAVY,RED,GREEN,ORANGE,SLATE="#1F3A5F","#8C2F39","#2F6B54","#C1662F","#5A6673"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10.5,
 "axes.edgecolor":SLATE,"text.color":"#222","xtick.color":SLATE,"ytick.color":SLATE,
 "axes.spines.top":False,"axes.spines.right":False,"figure.dpi":150})

flattery=np.array([0,0,0,0,0,0,1,1]); proxy=true_utility+2.2*flattery
gp=proxy[a]-proxy[b]; aw=rng.random(len(a))<1/(1+np.exp(-gp))
rb=np.zeros(8)
for _ in range(4000):
    pa=1/(1+np.exp(-(rb[a]-rb[b]))); e=aw-pa
    g=np.zeros(8); np.add.at(g,a,-e); np.add.at(g,b,e); rb-=0.05*g/len(a)
rb-=rb.mean()

def rlhf(reward,beta,steps=3000,eta=0.1):
    z=logits_ref.copy()
    for _ in range(steps):
        p=softmax(z); adv=reward-beta*(np.log(p/pi_ref)+1)
        z+=eta*p*(adv-p@adv)
    return softmax(z)

betas=np.geomspace(8,0.02,26)
kl,score,truev=[],[],[]
for b_ in betas:
    p=rlhf(rb,b_)
    kl.append((p*np.log(p/pi_ref)).sum()); score.append(p@rb); truev.append(p@true_utility)

fig,ax=plt.subplots(figsize=(7.0,3.6))
ax.plot(kl,score,color=ORANGE,lw=2,label="what the reward model reports")
ax.plot(kl,truev,color=NAVY,lw=2,label="what people actually get")
i=int(np.argmax(truev))
ax.plot(kl[i],truev[i],'o',color=RED,ms=7,zorder=5)
ax.annotate("best true outcome;\noptimizing past here makes it worse",
            xy=(kl[i],truev[i]),xytext=(kl[i]+0.45,truev[i]-1.05),fontsize=9.5,color=SLATE,
            arrowprops=dict(arrowstyle="->",color=RED,lw=1))
ax.set_xlabel("KL divergence from the pretrained model  (optimization pressure ->)")
ax.set_ylabel("utility")
ax.set_title("Goodhart's law, drawn: the proxy keeps rising after the goal starts falling",
             color=NAVY,fontsize=11.5,loc="left")
ax.legend(frameon=False,loc="lower right")
fig.tight_layout(); fig.savefig("fig37_1.png",bbox_inches="tight")
print("ok")
