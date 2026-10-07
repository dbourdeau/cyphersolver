"""Retrospective alignment (list A is now also attestation, not a clean holdout): align cipher tokens (decoded with key_1601 values only) to the contemporary decipherment text.
A token counts as correct if, in the best monotone alignment, one of its key values matches the decipherment at that
point. Mismatched tokens may absorb 0-4 letters; extra decipherment letters may be skipped. Reports accuracy overall and
by key grade of the token (H/C/M; '-' = token absent from key)."""
import sys, functools, collections, re
sys.path.insert(0, __import__('os').path.dirname(__file__))
from measure import load_key, blocks, look
from frscore import norm
def mnorm(s): return norm(re.sub(r"\bM(r|\.)\s",'Monsieur ',s))
from pathlib import Path
KEY = Path(__file__).resolve().parents[1] / 'key.tsv'
K=load_key(KEY)
# Historical support grades, not repository evidence grades; preserves the original H denominator.
for line in KEY.read_text().splitlines():
    if line and not line.startswith('#'):
        cols=line.split('\t'); K[cols[0]]=(K[cols[0]][0], cols[4])
L={l.split('\t')[0]:l.split('\t')[1] for l in open(sys.argv[1]) if not l.startswith('#') and '\t' in l}
B=[b for b in blocks(sys.argv[2]) if b['id'] in L]
sys.setrecursionlimit(100000)
def align(toks,P,top):
    vals=[];grades=[]
    for t in toks:
        k=look(K,t)
        if k is None or K[k][1]=='I': vals.append([]); grades.append('-')
        else: vals.append([mnorm(v) for v in (K[k][0][:1] if top else K[k][0]) if mnorm(v)]); grades.append(K[k][1])
    n=len(toks); m=len(P)
    @functools.lru_cache(None)
    def f(i,j):
        if i==n: return (0 if j==m else -0.01*(m-j)),()
        best=(-1e9,())
        for v in vals[i]:
            if P.startswith(v,j):
                s,p=f(i+1,j+len(v)); best=max(best,(s+1,(1,)+p))
        for k in range(0,5):
            if j+k<=m:
                s,p=f(i+1,j+k); best=max(best,(s-0.001,(0,)+p))
        if j<m:
            s,p=f(i,j+1); best=max(best,(s-0.02,p))
        return best
    s,path=f(0,0); f.cache_clear()
    return list(path),grades
T=Ct=Ca=0; byg=collections.defaultdict(lambda:[0,0])
for b in B:
    P=mnorm(L[b['id']]); n=len(b['tok'])
    pt,_=align(tuple(b['tok']),P,True); pa,gr=align(tuple(b['tok']),P,False)
    a=sum(pt); c=sum(pa); T+=n; Ct+=a; Ca+=c
    for ok,g in zip(pa,gr): byg[g][0]+=ok; byg[g][1]+=1
    print(f"{b['id']:5s} tokens {n:3d} correct(top value) {a:3d} correct(any homophone) {c:3d}")
print(f"TOTAL {T} tokens: correct with top key value {Ct} ({100*Ct/T:.1f}%), with any listed homophone {Ca} ({100*Ca/T:.1f}%)")
for g in ['H','C','M','-']:
    if byg[g][1]: print(f"  legacy support {g}: {byg[g][0]}/{byg[g][1]} = {100*byg[g][0]/byg[g][1]:.1f}% correct")
