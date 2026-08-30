import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
exec(open('_lib.py').read())
NAVY,RED,GREEN,ORANGE,SLATE="#1F3A5F","#8C2F39","#2F6B54","#C1662F","#5A6673"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10.5,"axes.edgecolor":SLATE,
 "text.color":"#222","xtick.color":SLATE,"ytick.color":SLATE,
 "axes.spines.top":False,"axes.spines.right":False,"figure.dpi":150})

def boundary(ax,clf,X_,y_,title):
    m=make_pipeline(StandardScaler(),clf).fit(X_,y_)
    x0,x1=X_[:,0].min()-.4,X_[:,0].max()+.4
    z0,z1=X_[:,1].min()-.4,X_[:,1].max()+.4
    xx,yy_=np.meshgrid(np.linspace(x0,x1,300),np.linspace(z0,z1,300))
    Z=m.predict(np.c_[xx.ravel(),yy_.ravel()]).reshape(xx.shape)
    ax.contourf(xx,yy_,Z,levels=[-.5,.5,1.5],colors=["#DCE4EE","#F6E3D9"])
    ax.scatter(X_[y_==0,0],X_[y_==0,1],s=5,color=NAVY)
    ax.scatter(X_[y_==1,0],X_[y_==1,1],s=5,color=ORANGE)
    ax.set_title(title,color=NAVY,fontsize=10.5); ax.set_xticks([]); ax.set_yticks([])

# Fig 21.1 kNN k
Xm,ym=make_moons(n_samples=600,noise=0.26,random_state=0)
fig,ax=plt.subplots(1,3,figsize=(7.8,2.7))
for a_,k in zip(ax,(1,15,150)):
    boundary(a_,KNeighborsClassifier(k),Xm,ym,f"kNN, k = {k}")
fig.suptitle("One neighbour memorizes; too many erase the shape",
             color=NAVY,fontsize=11.5,x=.02,ha="left")
fig.tight_layout(); fig.savefig("fig21_1.png",bbox_inches="tight")

# Fig 21.2 linear vs kernel on circles
Xc,yc=make_circles(n_samples=700,noise=0.10,factor=0.45,random_state=0)
fig,ax=plt.subplots(1,3,figsize=(7.8,2.7))
boundary(ax[0],LinearSVC(C=1.0,max_iter=20000),Xc,yc,"linear SVM")
boundary(ax[1],SVC(C=1.0,kernel="rbf",gamma=1.0),Xc,yc,"RBF kernel, gamma 1")
boundary(ax[2],SVC(C=1.0,kernel="rbf",gamma=100),Xc,yc,"RBF kernel, gamma 100")
fig.suptitle("A straight line cannot separate a ring. Too flexible a kernel memorizes it",
             color=NAVY,fontsize=11.3,x=.02,ha="left")
fig.tight_layout(); fig.savefig("fig21_2.png",bbox_inches="tight")
print("ok")
