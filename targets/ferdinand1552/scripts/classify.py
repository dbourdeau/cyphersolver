import pickle, numpy as np, cv2, sys, json
from sklearn.neighbors import KNeighborsClassifier
S=pickle.load(open('work/signs.pkl','rb'))
def feat(m,n=24):
    h,w=m.shape; s=max(h,w)
    c=np.zeros((s,s),np.float32); y=(s-h)//2; x=(s-w)//2
    c[y:y+h,x:x+w]=m
    f=cv2.GaussianBlur(cv2.resize(c,(n,n),interpolation=cv2.INTER_AREA),(0,0),1.0)
    return np.concatenate([f.ravel(),[h/40,w/40]])
try:
    Xtr,ytr=pickle.load(open('work/train.pkl','rb'))
except Exception:
    lab,order=pickle.load(open('work/lab.pkl','rb'))
    G={'oo':[8],'ou':[87,26,1],'B':[21],'Th':[30,82],'D':[31,100],'U':[47,34,99,19],'Ls':[32,10,95],'P':[41,23],'3':[84,4,90,81],'u':[28,48,9,62],
       'S':[3],'Hs':[16],'H3':[18],'Z#':[77,96,14],'d':[17,61],'A':[43,98,54,7,12,44,52,72,89],'~':[101,29],'I:':[5],'uo':[75],'z':[39,22,71],'K':[97],
       'H2':[80,68],'n:':[38,36],'V':[92,67,35,2,51,42,58,94],'F':[24],'+':[103],'=O':[27],'m:':[70],'g':[86,66,85],'<':[15,102,33,53,108,0],'1':[79,25,107],
       'd:':[109],'O.':[45],'+A':[20],'E:':[78],'7':[50],'Ex':[40],'X':[55],'Eo':[37],'ii':[64,57],'C':[11,46],'Hh':[65],'e':[63],'|':[69]}
    M={c:k for k,v in G.items() for c in v}
    X=np.array([feat(s['m']) for s in S])
    keep=[i for i in range(len(S)) if lab[i] in M]
    Xtr=X[keep]; ytr=[M[lab[i]] for i in keep]
    pickle.dump((Xtr,ytr),open('work/train.pkl','wb'))
knn=KNeighborsClassifier(5,weights='distance').fit(Xtr,ytr)
X=np.array([feat(s['m']) for s in S])
pr=knn.predict(X); pb=knn.predict_proba(X).max(1)
d,_=knn.kneighbors(X,1); d=d[:,0]
for s,a,b,c in zip(S,pr,pb,d): s['c']=a; s['pb']=float(b); s['dist']=float(c)
pickle.dump(S,open('work/signs_c.pkl','wb'))
from collections import Counter
cnt=Counter(pr); print(cnt.most_common())
lines={}
for s in S: lines.setdefault((s['p'],s['l']),[]).append(s)
with open('work/pass_machine.txt','w',encoding='utf8') as f:
    for k in sorted(lines,key=lambda k:(k[0],k[1])):
        L=sorted(lines[k],key=lambda s:s['x0'])
        f.write(f"{k[0]}.{k[1]+1:02d} "+' '.join(s['c']+('?' if s['pb']<0.75 else '') for s in L)+'\n')
