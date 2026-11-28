"""Anneal with word dividers as spaces; option: drop a sign as null. usage: anneal_sp.py restarts [null_label]"""
import sys, os, random, math, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
from lang import lm
here = os.path.dirname(os.path.abspath(__file__))
lines = [l.split()[1:] for l in open(os.path.join(here,'transcription.txt'),encoding='utf8') if l.startswith(('48r','48v'))]
null = sys.argv[2] if len(sys.argv)>2 else None
toks=[]
for l in lines:
    for t in l:
        if t=='|': toks.append(' ')
        elif t!=null: toks.append(t)
    # line end: no divider assumed (words run over); keep as is
s=' '.join(''.join(['_' if t==' ' else t+',' for t in toks]).split('_'))
syms=sorted(set(t for t in toks if t!=' '))
L=lm.AR_LETTERS; m=lm.load('ar-mamluk', spaces=True)
def dec(k): return ' '.join(''.join(k[t] for t in w) for w in ' '.join(toks).replace('  ',' ').split(' ') if w) 
words=[]; cur=[]
for t in toks:
    if t==' ':
        if cur: words.append(cur); cur=[]
    else: cur.append(t)
if cur: words.append(cur)
def dec(k): return ' '.join(''.join(k[t] for t in w) for w in words)
def sc(k): return m.score_idx(m.encode(dec(k)))
best=None
for r in range(int(sys.argv[1])):
    random.seed(100+r); perm=random.sample(L,len(L)); k=dict(zip(syms,perm)); spare=perm[len(syms):]; c=sc(k); T=3.0
    for it in range(40000):
        a=random.choice(syms)
        if spare and random.random()<0.2:
            j=random.randrange(len(spare)); k[a],spare[j]=spare[j],k[a]; u=('s',a,j)
        else:
            b=random.choice(syms); k[a],k[b]=k[b],k[a]; u=('w',a,b)
        n=sc(k)
        if n>=c or random.random()<math.exp((n-c)/T): c=n
        elif u[0]=='s': k[a],spare[u[2]]=spare[u[2]],k[a]
        else: k[a],k[u[2]]=k[u[2]],k[a]
        T=max(0.05,T*0.99985)
    n=sum(len(w)+1 for w in words)
    print(r, round(c/n,3), dec(k)[:120], flush=True)
    if best is None or c>best[0]: best=(c,dict(k))
print('BEST',best[0]/n); print(json.dumps(best[1],ensure_ascii=False)); print(dec(best[1]))
