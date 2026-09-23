"""Seeded from the recovered letter key, allow each sign to be a letter or a common digraph."""
import sys,os,json,math,random
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))+'/..')
os.environ.setdefault('LAM','1.0')
import word as W
from solve import load_runs
LET=list(W.LET)
DI=['es','en','on','ou','qu','le','la','de','re','se','te','ne','me','ce','er','an','in','un','ai','oi','au','eu','ur','ar','or','ss','ll','et','ie','em','ant','ent','ion','que','par','pour','les','des','ment']
VALS=LET+DI
key=json.load(open(sys.argv[1])); ROUNDS=int(sys.argv[2]); IT=int(sys.argv[3])
runs=[r for r in load_runs() if len(r)>=3]
signs=sorted({s for r in runs for s in r}); si={s:i for i,s in enumerate(signs)}
seq=[[si[s] for s in r] for r in runs]
occ=[[j for j,r in enumerate(seq) if i in r] for i in range(len(signs))]
k=[key.get(s,'e') for s in signs]
def txt(k,r): return ''.join(k[i] for i in r)
def sc(k,r):
    t=txt(k,r); return W.seg_score(t)+W.CH.score(t)
rsc=[sc(k,r) for r in seq]; cur=sum(rsc); best=(cur,list(k))
print('start',round(cur,1),file=sys.stderr)
for rd in range(ROUNDS):
    k=list(best[1])
    for _ in range(random.randint(0,2)): k[random.randrange(len(signs))]=random.choice(VALS)
    rsc=[sc(k,r) for r in seq]; cur=sum(rsc); loc=(cur,list(k))
    for it in range(IT):
        T=20.0*(1-it/IT)+0.3
        i=random.randrange(len(signs)); old=k[i]; nv=random.choice(VALS)
        if nv==old: continue
        k[i]=nv; js=occ[i]; ns=[sc(k,seq[j]) for j in js]
        new=cur-sum(rsc[j] for j in js)+sum(ns)
        if new>=cur or random.random()<math.exp((new-cur)/T):
            cur=new
            for j,v in zip(js,ns): rsc[j]=v
            if cur>loc[0]: loc=(cur,list(k))
        else: k[i]=old
    if loc[0]>best[0]: best=loc; print('round',rd,round(best[0],1),file=sys.stderr)
k=best[1]
print(json.dumps({s:k[i] for i,s in enumerate(signs)},sort_keys=True))
print('score',round(best[0],1))
