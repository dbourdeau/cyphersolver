"""Coordinate check: for each sign, score every letter (and null '_') with the rest of the key fixed.
Usage: python refine.py <tokens> <keyfile> [model]  -> prints signs whose best option differs from the key."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm
toks=[t for l in open(sys.argv[1],encoding='utf-8') if l.startswith('L') for t in l.split(':',1)[1].split() if t not in ('_','?')]
key=dict(l.strip().rsplit('=',1) for l in open(sys.argv[2],encoding='utf-8') if '=' in l)
m=lm.load(sys.argv[3] if len(sys.argv)>3 else 'la', spaces=False)
C=float(os.environ.get('NULLC','-2.6'))
def sc(k):
    s=''.join(k.get(t,'') for t in toks if k.get(t,'_')!='_')
    return m.score(s)+C*(len(toks)-len(s))
base=sc(key)
from collections import Counter
c=Counter(toks)
for s in sorted(c,key=lambda x:-c[x]):
    res=[]
    for L in list(m.alpha)+['_']:
        k=dict(key); k[s]=L; res.append((sc(k)-base,L))
    res.sort(reverse=True)
    cur=key.get(s)
    flag='' if res[0][1]==cur else '  <==='
    print(f"{s:4s} n={c[s]:3d} cur={cur} ", ' '.join(f"{L}:{d:+.0f}" for d,L in res[:5]), flag)
