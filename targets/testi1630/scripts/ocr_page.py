# ocr_page.py : language-free first read of every cipher line. Shape features only; trained on the eye-read c. 23r and c. 13r signs.
import sys,json,numpy as np,cv2,re
from PIL import Image
from scipy.ndimage import uniform_filter,label,find_objects
KEY={'T':'e','2':'i','N':'o','A':'a','9':'r','V':'n','3':'t','x':'s','4':'l','D':'c','+':'u','#':'p','o':'m','c':'d','g':'g','v':'h','r':'f','7':'z','/':'b','t':'q'}
def load(blk):
    a=np.asarray(Image.open(blk).convert('L')).astype(np.float32); bg=uniform_filter(a,151); return ((bg-a)>28).astype(np.uint8)
def vec(ink,b):
    x0,y0,x1,y1=b; c=ink[y0:y1,x0:x1]*255; H,W=c.shape; M=max(H,W); P=np.zeros((M,M),np.uint8)
    P[(M-H)//2:(M-H)//2+H,(M-W)//2:(M-W)//2+W]=c
    v=cv2.GaussianBlur(cv2.resize(P,(40,40),interpolation=cv2.INTER_AREA).astype(np.float32),(5,5),0); v=(v-v.mean())/(v.std()+1e-6); return (v.ravel()/40)
def line_boxes(ink,y,half=118,xmin=380,xmax=None,sw=98):
    y0,y1=max(0,y-half),min(ink.shape[0],y+half); sub=ink[y0:y1]; lab,n=label(sub,structure=np.ones((3,3))); out=[]
    for i,s in enumerate(find_objects(lab),1):
        h=s[0].stop-s[0].start; w=s[1].stop-s[1].start; ar=(lab[s]==i).sum()
        if ar<150 and h<35: continue
        # drop strays poking in from neighbour lines
        cy=(s[0].start+s[0].stop)/2
        if abs(cy-half)>half*0.72 and h<70: continue
        out.append([s[1].start,s[0].start+y0,s[1].stop,s[0].stop+y0,int(ar)])
    out.sort(); M=[]
    for b in out:
        if M:
            m=M[-1]; ov=min(m[2],b[2])-max(m[0],b[0])
            if ov>0.5*min(m[2]-m[0],b[2]-b[0]): M[-1]=[min(m[0],b[0]),min(m[1],b[1]),max(m[2],b[2]),max(m[3],b[3]),m[4]+b[4]]; continue
        M.append(b)
    R=[]
    for b in M:
        w=b[2]-b[0]
        if b[0]<xmin or (xmax and b[2]>xmax): continue
        if w>sw*1.55:
            k=max(2,int(round(w/sw))); prof=ink[b[1]:b[3],b[0]:b[2]].sum(0).astype(float); prof=cv2.GaussianBlur(prof.reshape(1,-1),(0,0),6).ravel(); cuts=[0]
            for j in range(1,k):
                c=int(j*w/k); r=int(w/k*0.3); c=c-r+int(np.argmin(prof[c-r:c+r])); cuts.append(c)
            cuts.append(w)
            for p,q in zip(cuts,cuts[1:]): R.append([b[0]+p,b[1],b[0]+q,b[3],'s'])
        else: R.append(b[:4]+['w'])
    return R
def classify(X,Y,v):
    sc=X@v; top=np.argsort(-sc)[:7]; votes={}
    for t in top: votes[Y[t]]=votes.get(Y[t],0)+sc[t]
    return max(votes,key=votes.get)
def nw(a,b):
    n,m=len(a),len(b); D=np.zeros((n+1,m+1)); D[:,0]=np.arange(n+1)*0.6; D[0,:]=np.arange(m+1)*0.6
    for i in range(1,n+1):
        for j in range(1,m+1):
            D[i,j]=min(D[i-1,j-1]+(a[i-1]!=b[j-1])*1.0,D[i-1,j]+0.6,D[i,j-1]+0.6)
    i,j=n,m; P=[]
    while i>0 and j>0:
        if D[i,j]==D[i-1,j-1]+(a[i-1]!=b[j-1])*1.0: P.append((i-1,j-1)); i-=1;j-=1
        elif D[i,j]==D[i-1,j]+0.6: i-=1
        else: j-=1
    return P[::-1]
SETS=[('scans/work/c23_block.jpg',[124,410,694,972,1261,1540,1822,2105,2391],'scans/work/c23_passA.txt'),('scans/work/c13r_block.jpg',[183,440,668,912,1133,1371,1601,1835],'scans/work/c13_passA.txt'),('scans/work/c7r_block.jpg',None,'scans/work/c7r_passA.txt')]
def train():
    T=json.load(open('scans/work/c23_tpl.json')); ink0=load('scans/work/c23_block.jpg'); X=[];Y=[]
    for l,bs in T.items():
        for b in bs: X.append(vec(ink0,b)); Y.append(l)
    X=np.array(X);Y=np.array(Y)
    data=[]
    for blk,ys,pf in SETS:
        ink=load(blk)
        if ys is None:
            ys=json.load(open(blk.replace('_block.jpg','_lines.json')))[2:17]
        P=[l.split() for l in open(pf,encoding='utf8') if l.strip()]
        for y,seq in zip(ys,P):
            B=[b for b in line_boxes(ink,y) if b[4]=='w']; V=[vec(ink,b[:4]) for b in B]; data.append((seq,V))
    for rnd in range(3):
        XX=[];YY=[]; tot=ok=0
        for seq,V in data:
            lab=[classify(X,Y,v) for v in V]
            A=nw(seq,lab); S=set(A)
            for k,(i,j) in enumerate(A):
                tot+=1; ok+=seq[i]==lab[j]
                # keep a substitution only if flanked on both sides by agreement
                if seq[i]==lab[j] or ((i-1,j-1) in S and (i+1,j+1) in S and seq[i-1]==lab[j-1] and i+1<len(seq) and j+1<len(lab) and seq[i+1]==lab[j+1]):
                    XX.append(V[j]);YY.append(seq[i])
        print('round',rnd,'aligned',tot,'agree',round(ok/max(tot,1),3),'train',len(YY),file=sys.stderr)
        X=np.array(XX);Y=np.array(YY)
    return X,Y
if __name__=='__main__':
    X,Y=train(); print('train',len(Y),{k:int((Y==k).sum()) for k in KEY},file=sys.stderr)
    for page in sys.argv[1:]:
        ink=load(f'scans/work/{page}_block.jpg'); ys=json.load(open(f'scans/work/{page}_lines.json')); res=[]
        for li,y in enumerate(ys,1):
            B=line_boxes(ink,y); s=''; lab=[]
            for b in B:
                l=classify(X,Y,vec(ink,b[:4])); lab.append(l)
                s+=KEY.get(l,'?')
            res.append(dict(line=li,boxes=[b[:4] for b in B],labels=lab)); print(page,li,s)
        json.dump(res,open(f'scans/work/{page}_ocr.json','w'))
