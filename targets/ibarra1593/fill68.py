"""Constrained fill: keep keyM, rank candidate syllables for each number missing from it (one at a time, then jointly).
Candidates exclude que/qui/qua and bare vowels (the unconstrained climb collapses onto them). Control: rank of the
chosen value among all candidates and its gain against the gain of a random candidate."""
import sys,os,random
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..'))
from anneal68 import score, SEED, toks
from collections import Counter
cnt=Counter(toks)
miss=[n for n in sorted(set(toks)) if n.isdigit() and n not in SEED]
CV=[c+v for c in 'bcdfghjlmnprstvxyz' for v in 'aeiou']
K=dict(SEED); base=score(K)
for n in miss:
    r=[]
    for v in CV:
        K[n]=v; r.append((score(K)-base,v))
    K.pop(n,None); r.sort(reverse=True)
    gains=[g for g,_ in r]; med=gains[len(gains)//2]
    print(n,'x',cnt[n],'top5',[(v,round(g,4)) for g,v in r[:5]],'median gain',round(med,4))
