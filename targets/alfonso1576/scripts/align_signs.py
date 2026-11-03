# Forced alignment of each cipher line to the straightened image. Language plays no part:
# inputs are the sign sequence of the line and the image. Output: x of every sign, for crops.
import re,json,sys
import numpy as np
from PIL import Image
src=open('scripts/strips_f.py').read().split("sheets('f76r'")[0]
exec(src.split('def band')[0])
LINES['f77r']=LINES['f77r']+[(2975,2925),(3100,3050),(3215,3160),(3345,3285)]
XR={'f76r':(380,3170),'f76v':(330,3130),'f77r':(250,3170)}
SH=0.42  # slant
SPAN={('f76r','01'):(1100,10**6),('f77r','14'):(0,2012),('f77r','P4'):(0,2020)}
BH=36    # x-height band below the line value
def text(p):
    out=[]
    for l in open(f'work/{p}_p2.txt'):
        a,b=l.split(None,1); out.append((a,re.sub(r'\[.*?\]','',b.strip())))
    return out
data=[]
for p in LINES:
    g=np.array(Image.open(f'scans/{p}_full.jpg').convert('L')).astype(float)
    T=text(p); x0,x1=XR[p]
    for n,(lab,s) in enumerate(T):
        yl,yr=LINES[p][n]; W=x1-x0
        prof=np.zeros(W)
        for xi in range(W):
            x=x0+xi; y0=yl+(yr-yl)*(x-LX)/(RX-LX)
            # sheared column through the x-height band
            c=0
            for dy in range(4,BH,3):
                xx=int(x-SH*(dy-BH/2)); yy=int(y0+dy)
                if 0<=xx<g.shape[1] and 0<=yy<g.shape[0] and g[yy,xx]<110: c+=1
            prof[xi]=c
        # page edge and clear text: keep the cipher span only
        col=(g[int(min(yl,yr)):int(max(yl,yr))+BH, x0:x1]<40).mean(0)
        run=np.convolve((col>0.9).astype(int),np.ones(25,int),'same')
        edge=np.where(run>=25)[0]
        if len(edge): prof[int(edge[0])-20:]=0
        lo,hi=SPAN.get((p,lab),(0,10**6))
        prof[:max(0,lo-x0)]=0; prof[max(0,min(W,hi-x0)):]=0
        ink=np.where(np.convolve(prof,np.ones(9),'same')>6)[0]
        data.append(dict(p=p,lab=lab,s=s,prof=prof,a=int(ink[0]),b=int(ink[-1]),x0=x0,yl=yl,yr=yr))
mu={}
for d in data:
    for c in d['s']: mu.setdefault(c,48.0)
STEP=2
for it in range(5):
    tot={};cnt={}
    for d in data:
        s=d['s'];prof=d['prof'];n=len(s)
        A=d['a'];B=d['b'];X=np.arange(max(A-12,0),min(B+13,len(prof)),STEP);m=len(X)
        cost=np.full((n+1,m),1e12);bk=np.zeros((n+1,m),int)
        cut=prof[X]*1.2
        cost[0,:]=np.abs(X-A)*0.3
        for i in range(1,n+1):
            mw=mu[s[i-1]]
            for j in range(m):
                lo=max(0,j-int(mw*2.0/STEP));hi=max(0,j-int(mw*0.35/STEP))
                if hi<=lo: continue
                w=X[j]-X[lo:hi]
                c=cost[i-1,lo:hi]+((w-mw)/ (0.28*mw))**2+cut[j]
                k=int(np.argmin(c));cost[i,j]=c[k];bk[i,j]=lo+k
        e=cost[n]+np.abs(X-B)*0.3
        j=int(np.argmin(e));bs=[j]
        for i in range(n,0,-1):
            j=bk[i,j];bs.append(j)
        bs=X[np.array(bs[::-1])]
        d['bs']=bs.tolist()
        for i,c in enumerate(s):
            tot[c]=tot.get(c,0)+bs[i+1]-bs[i];cnt[c]=cnt.get(c,0)+1
    mu={c:(tot[c]/cnt[c]*cnt[c]+48*2)/(cnt[c]+2) for c in tot}
print({k:round(v) for k,v in sorted(mu.items())})
out=[]
for d in data:
    s=d['s'];bs=d['bs']
    y=lambda x:d['yl']+(d['yr']-d['yl'])*(x-LX)/(RX-LX)
    for i,c in enumerate(s):
        if c=='q':
            xm=d['x0']+(bs[i]+bs[i+1])/2
            out.append(dict(p=d['p'],l=d['lab'],i=i,x=round(xm),y=round(y(xm)),ctx=s[max(0,i-3):i]+'['+c+']'+s[i+1:i+4]))
json.dump(out,open('work/qpos.json','w'))
print(len(out))
