import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
exec(open('_lib.py').read()); exec(open('_lib2.py').read())
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import normalize
NAVY,RED,GREEN,ORANGE,SLATE="#1F3A5F","#8C2F39","#2F6B54","#C1662F","#5A6673"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10.5,"axes.edgecolor":SLATE,
 "text.color":"#222","xtick.color":SLATE,"ytick.color":SLATE,
 "axes.spines.top":False,"axes.spines.right":False,"figure.dpi":150})

vec=TfidfVectorizer(stop_words="english").fit(texts)
sp=np.asarray(normalize(vec.transform(texts)).todense())
def tf_rank(q):
    qv=np.asarray(normalize(vec.transform([q])).todense()).ravel()
    s=sp@qv
    return None if s.max()==0 else list(np.argsort(-s))
def de_rank(q): return list(np.argsort(-(dense@embed(q))))

ks=range(1,6); tf=[];de=[]
for k in ks:
    tf.append(np.mean([ (r is not None and g in r[:k]) for q,g in queries for r in [tf_rank(q)] ]))
    de.append(np.mean([ g in de_rank(q)[:k] for q,g in queries ]))

fig,ax=plt.subplots(figsize=(6.6,3.3))
ax.plot(list(ks),[v*100 for v in tf],'o-',color=RED,lw=2,label="keyword (tf-idf)")
ax.plot(list(ks),[v*100 for v in de],'o-',color=NAVY,lw=2,label="dense embeddings")
ax.set_xticks(list(ks)); ax.set_ylim(0,105)
ax.set_xlabel("k  (chunks handed to the generator)"); ax.set_ylabel("recall@k  (%)")
ax.set_title("Recall bounds everything downstream",color=NAVY,fontsize=12,loc="left")
ax.legend(frameon=False,loc="lower right")
fig.tight_layout(); fig.savefig("fig38_1.png",bbox_inches="tight")
print("tfidf",[round(v,2) for v in tf]); print("dense",[round(v,2) for v in de])
