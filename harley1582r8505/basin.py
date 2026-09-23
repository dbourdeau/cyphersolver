import sys,os,json,random,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))+'/..')
from lang import lm
import numpy as np
from solve import load_runs
M=lm.load(os.environ.get('MODEL','fr-1600-letters'),order=int(os.environ.get('ORDER','5')),spaces=False)
mp0=json.load(open(sys.argv[1])); ROUNDS=int(sys.argv[2]); IT=int(sys.argv[3])
runs=[r for r in load_runs() if len(r)>=4]
signs=sorted({s for r in runs for s in r}); si={s:i for i,s in enumerate(signs)}
seq=[np.array([si[s] for s in r]) for r in runs]
occ=[[j for j,r in enumerate(seq) if i in set(r.tolist())] for i in range(len(signs))]
LET='abcdefghilmnopqrstuxy'; alpha=[M.encode(c)[0] for c in LET]; inv={M.encode(c)[0]:c for c in LET}
FR=dict(a=8.2,b=1.0,c=3.2,d=3.8,e=16.5,f=1.1,g=1.0,h=0.8,i=7.2,l=5.6,m=3.0,n=7.0,o=5.4,p=2.8,q=1.3,r=6.5,s=8.0,t=7.0,u=6.5,x=0.4,y=0.4)
import collections
cnt=np.zeros(len(signs))
for r in seq:
    for t in r: cnt[t]+=1
NT=int(cnt.sum()); exp={M.encode(c)[0]:FR[c]/sum(FR.values())*NT for c in FR}
W=float(os.environ.get('W','1'))
def pen(k):
    obs=collections.Counter()
    for i,v in enumerate(k): obs[int(v)]+=cnt[i]
    return sum((obs.get(a,0)-e)**2/e for a,e in exp.items())
def score(k): return sum(M.score_idx(k[r]) for r in seq)-W*pen(k)
FIX=json.load(open(os.environ['FIX'])) if os.environ.get('FIX') else {}
key=np.array([M.encode(FIX.get(s, mp0.get(s,'e')))[0] for s in signs])
freeidx=[i for i,s in enumerate(signs) if s not in FIX]
best=(score(key),key.copy())
print('start',round(best[0],1),file=sys.stderr)
for rd in range(ROUNDS):
    k=best[1].copy()
    for _ in range(random.randint(3,8)): k[random.choice(freeidx)]=random.choice(alpha)
    rsc=np.array([M.score_idx(k[r]) for r in seq]); cur=rsc.sum()-W*pen(k); loc=(cur,k.copy())
    for it in range(IT):
        T=1.2*(1-it/IT)+0.01
        i=random.choice(freeidx); old=int(k[i]); nv=random.choice(alpha)
        if nv==old: continue
        k[i]=nv; js=occ[i]; ns=np.array([M.score_idx(k[seq[j]]) for j in js])
        new=rsc.sum()-rsc[js].sum()+ns.sum()-W*pen(k)
        if new>=cur or random.random()<math.exp((new-cur)/T):
            cur=new; rsc[js]=ns
            if cur>loc[0]: loc=(cur,k.copy())
        else: k[i]=old
    if loc[0]>best[0]:
        best=loc; print('round',rd,round(best[0],1),file=sys.stderr)
key=best[1]; mp={s:inv[int(key[i])] for i,s in enumerate(signs)}
print(json.dumps(mp,sort_keys=True))
txt=[''.join(mp[s] for s in r) for r in runs]
print('per-char',round(sum(M.score(t) for t in txt)/sum(len(t) for t in txt),3))
for t in txt: print(t)
