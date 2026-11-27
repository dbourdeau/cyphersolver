"""Classify every segmented sign with the kNN trained on ff. 34r-35v (work/train2.pkl); write
work/machine.tsv: page, line index, y, cursive, median NN distance, labels (with top-3 probs in work/probs.pkl)."""
import pickle, numpy as np, sys
sys.path.insert(0,'scripts'); from feat import feat
from sklearn.neighbors import KNeighborsClassifier
tr=pickle.load(open(sys.argv[1] if len(sys.argv)>1 else 'work/train2.pkl','rb'))
X=np.array([feat(m) for m,_ in tr]); y=[t for _,t in tr]
knn=KNeighborsClassifier(5,weights='distance').fit(X,y); cls=knn.classes_
P=pickle.load(open('work/pages.pkl','rb'))
out=[];probs={};dist={}
for p,L in P.items():
    for j,l in enumerate(L):
        ss=sorted(l['signs'],key=lambda s:s['x0'])
        if not ss: continue
        F=np.array([feat(s['m']) for s in ss])
        pr=knn.predict_proba(F); d,_=knn.kneighbors(F,1)
        labs=[cls[i] for i in pr.argmax(1)]
        probs[(p,j)]=[sorted(zip(cls,r),key=lambda x:-x[1])[:4] for r in pr]
        out.append((p,j,l['y'],l['cursive'],float(np.median(d)),labs)); dist[(p,j)]=d[:,0].tolist()
pickle.dump((out,probs),open('work/machine.pkl','wb')); pickle.dump(dist,open('work/dist.pkl','wb'))
with open('work/machine.tsv','w',encoding='utf8') as f:
    for p,j,yy,c,d,labs in out: f.write(f"{p}\t{j}\t{yy}\t{c:.2f}\t{d:.2f}\t{' '.join(labs)}\n")
