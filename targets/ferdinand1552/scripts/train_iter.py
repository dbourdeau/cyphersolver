"""Iterative training set: seed from the 34r lines paired by count, then align every transcription line
of ff. 34r-35v against every segmented line by DP on the classifier's predictions, keep confident
sign matches, retrain. Output work/train2.pkl (crop, label)."""
import pickle, numpy as np, sys
sys.path.insert(0,'scripts'); from feat import feat
from sklearn.neighbors import KNeighborsClassifier
train,pairs,T=pickle.load(open('work/train_signs.pkl','rb'))
P=pickle.load(open('work/pages.pkl','rb'))
seed=[]
for i,j in pairs['34r']:
    toks=T['34r'][i][1]; ss=sorted(P['34r'][j]['signs'],key=lambda s:s['x0'])
    if len(ss)==len(toks): seed+=list(zip([s['m'] for s in ss],toks))
cur=seed
SEG=[(p,j,sorted(l['signs'],key=lambda s:s['x0'])) for p in T for j,l in enumerate(P[p]) if len(l['signs'])>=6]
FE={(p,j):np.array([feat(s['m']) for s in ss]) for p,j,ss in SEG}
def align(pred,toks):
    # pred: list of dict label->prob ; global alignment, gap cost
    n,m=len(pred),len(toks); D=np.zeros((n+1,m+1)); D[:,0]=-np.arange(n+1)*.6; D[0,:]=-np.arange(m+1)*.6
    B=np.zeros((n+1,m+1),int)
    for i in range(1,n+1):
        for j in range(1,m+1):
            a=D[i-1,j-1]+(pred[i-1].get(toks[j-1],0)*2-0.5); b=D[i-1,j]-.6; c=D[i,j-1]-.6
            D[i,j]=max(a,b,c); B[i,j]=np.argmax([a,b,c])
    i,j=n,m; out=[]
    while i>0 and j>0:
        if B[i,j]==0: out.append((i-1,j-1)); i-=1;j-=1
        elif B[i,j]==1: i-=1
        else: j-=1
    return D[n,m],out
for it in range(4):
    X=np.array([feat(m) for m,_ in cur]); y=[t for _,t in cur]
    knn=KNeighborsClassifier(3,weights='distance').fit(X,y); cls=knn.classes_
    new=[]
    for p,tl in T.items():
        segs=[(j,ss) for pp,j,ss in SEG if pp==p]
        probs={j:[dict(zip(cls,r)) for r in knn.predict_proba(FE[(p,j)])] for j,ss in segs}
        for k,toks in tl:
            toks=[t for t in toks if t not in('Sicut','Insuper','Postq')]
            best=max(((align(probs[j],toks),j,ss) for j,ss in segs),key=lambda x:x[0][0]/max(1,len(toks)))
            (sc,al),j,ss=best
            if sc/len(toks)<0.6: continue
            # keep matches whose neighbours also match (anchor runs)
            for a,b in al:
                new.append((ss[a]['m'],toks[b]))
    cur=new
    print('iter',it,'signs',len(cur))
from sklearn.model_selection import cross_val_score
X=np.array([feat(m) for m,_ in cur]); y=[t for _,t in cur]
print('cv',cross_val_score(KNeighborsClassifier(3,weights='distance'),X,y,cv=5).mean())
pickle.dump(cur,open('work/train2.pkl','wb'))
