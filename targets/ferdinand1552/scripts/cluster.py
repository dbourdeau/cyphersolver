import pickle, numpy as np, cv2, sys
from sklearn.cluster import AgglomerativeClustering, KMeans
from PIL import Image, ImageDraw
S=pickle.load(open('work/signs.pkl','rb'))
def feat(m,n=24):
    h,w=m.shape; s=max(h,w)
    c=np.zeros((s,s),np.float32); y=(s-h)//2; x=(s-w)//2
    c[y:y+h,x:x+w]=m
    f=cv2.GaussianBlur(cv2.resize(c,(n,n),interpolation=cv2.INTER_AREA),(0,0),1.0)
    return np.concatenate([f.ravel(),[h/40,w/40]])
X=np.array([feat(s['m']) for s in S])
k=int(sys.argv[1]) if len(sys.argv)>1 else 70
km=KMeans(k,n_init=5,random_state=1).fit(X)
lab=km.labels_
order=np.argsort(-np.bincount(lab))
W=70;H=56
sheet=Image.new('RGB',(W*14+40,H*k//1),'white') 
rows=[]
d=ImageDraw.Draw(sheet)
for r,c in enumerate(order):
    idx=np.where(lab==c)[0]
    dist=((X[idx]-km.cluster_centers_[c])**2).sum(1)
    idx=idx[np.argsort(dist)]
    d.text((2,r*H+20),f'{c}:{len(idx)}',fill='red')
    for j,i in enumerate(idx[:14]):
        m=S[i]['m']*255
        s=min(1.0,min(W-4,H-4)/max(m.shape))*1.0
        t=Image.fromarray(255-m.astype(np.uint8))
        t=t.resize((max(1,int(t.width*s)),max(1,int(t.height*s))))
        sheet.paste(t.convert('RGB'),(44+j*W,r*H+2))
sheet.save('work/clusters.png')
pickle.dump((lab,order),open('work/lab.pkl','wb'))
print(sheet.size)
