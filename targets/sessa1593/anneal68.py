"""Ciphertext-only check and rebuild of the Feria-Mansfeld syllable table on no. 68 (ct68.txt).
Seed = keyM.tsv. Score = es-golden-age 5-gram, no spaces, per character, over the decode with code words removed.
Control: the same score for 200 keys in which the seed's syllable values are shuffled among the numbers.
Then hill-climb: for every number, try every CV syllable; keep a change only if the score rises."""
import sys,os,random,json
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..'))
from lang import lm
from dec68 import K as SEED, lines
M=lm.load('es-golden-age',spaces=False)
def sc(s): return M.per_char(lm.norm(s,'modern',False))
toks=[t for _,ts in lines() for t in ts]
nums=sorted({t for t in toks if t.isdigit() and len(t)==2})
segs=[]
def text(K):
    out=[];cur=''
    for t in toks:
        v=K.get(t)
        if v is None or v=='·': 
            if cur: out.append(cur); cur=''
        else: cur+=v
    if cur: out.append(cur)
    return out
def score(K):
    ss=text(K); n=sum(len(s) for s in ss)
    return sum(sc(s)*len(s) for s in ss if len(s)>2)/max(1,n)
base=score(SEED)
random.seed(1)
vals=[SEED[n] for n in nums if n in SEED]; keys=[n for n in nums if n in SEED]
ctl=[]
for i in range(200):
    v=vals[:]; random.shuffle(v); K=dict(SEED); K.update(zip(keys,v)); ctl.append(score(K))
ctl.sort()
print(f'seed keyM score {base:.4f}; shuffled control max {ctl[-1]:.4f} mean {sum(ctl)/len(ctl):.4f}')
CV=[c+v for c in 'bcdfghjlmnpqrstvxyz' for v in 'aeiou']+['que','qui','qua','a','e','i','o','u']
K=dict(SEED); cur=score(K); changes=[]
for rnd in range(3):
    for n in nums:
        best=(cur,K.get(n))
        for v in CV:
            K[n]=v; s=score(K)
            if s>best[0]+0.002: best=(s,v)
        old=SEED.get(n); K[n]=best[1]
        if best[0]>cur: changes.append((n,old,best[1],round(best[0]-cur,4))); cur=best[0]
print(f'after hill-climb {cur:.4f}')
for c in changes: print('  ',c)
json.dump({n:K[n] for n in nums if K.get(n)!=SEED.get(n)},open('anneal68_changes.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
