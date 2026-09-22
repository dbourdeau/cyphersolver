import os,sys,json
import numpy as np
sys.path.insert(0,'..')
from lang import lm
from solve import load_segments
from solve2 import build, LETTERS
m=lm.load('it-cinquecento',order=5,spaces=False)
key=json.load(open(sys.argv[1]))
segs=load_segments(); types,ti,wins,per,cnt=build(segs,m)
A,K=m.A,m.order; powv=A**np.arange(K-1,-1,-1); lp=m.lp.astype(float)
k=np.array([m.index[key[t]] for t in types])
def sc(k,idx): return lp[(k[wins[idx]]*powv).sum(1)].sum()
rows=[]
for t in types:
    i=ti[t]; base=sc(k,per[i]); alts=[]
    for c in LETTERS:
        k2=k.copy(); k2[i]=m.index[c]; alts.append((sc(k2,per[i])-base,c))
    alts.sort(reverse=True)
    second=[a for a in alts if a[1]!=key[t]][0]
    rows.append((second[0],t,key[t],cnt[i],alts[:4]))
rows.sort(reverse=True)
for d,t,c,n,a in rows: print('%-6s %s n=%2d margin=%6.2f  %s'%(t,c,n,-d,' '.join('%s%.1f'%(x[1],x[0]) for x in a)))
