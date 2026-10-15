import re, itertools, sys, os
sys.path.insert(0,'.')
from lang import lm
M=lm.load('de-1500s')
kl=open('targets/r9416/r9416/_c/key.txt').read().split('\n')[1]
key=dict(kv.split('=',1) for kv in kl.split())
key.update({'#':'?'})
AMB={'f':'eoz','H':'uk'}
CODE={('f','e'):'z',('f','o'):'f',('f','z'):'j',('H','u'):'H',('H','k'):'K'}
def dec(tok): return key.get(tok,'?')
src=open('targets/r9416/r9416/p34.txt',encoding='utf8').read().split('\n')
# gather all words sequentially for context
lines=[]
for l in src:
    m=re.match(r'^(\d\d): (.*)',l)
    lines.append(m)
allw=[]
for m in lines:
    if not m: continue
    for w in m.group(2).split():
        allw.append(w)
def toks(w): return re.findall(r'io|.',w)
def plain(w): return ''.join(dec(t) for t in toks(w) if t not in '?.|=:;{}[]')
def score(s): return M.score_idx(M.encode(s))
cnt={}
res={}
for i,w in enumerate(allw):
    T=toks(w); pos=[k for k,t in enumerate(T) if t in AMB]
    if not pos: continue
    left=' '.join(plain(x) for x in allw[max(0,i-2):i]); right=' '.join(plain(x) for x in allw[i+1:i+3])
    best=None
    for combo in itertools.product(*[AMB[T[k]] for k in pos]):
        P=[dec(t) for t in T]
        for k,c in zip(pos,combo): P[k]=c
        s=score(left+' '+''.join(P)+' '+right)
        if best is None or s>best[0]: best=(s,combo)
    NT=list(T)
    for k,c in zip(pos,best[1]):
        NT[k]=CODE[(T[k],c)]; cnt[(T[k],c)]=cnt.get((T[k],c),0)+1
    res[i]=''.join(NT)
print(cnt)
# rewrite
out=[];i=0
for l,m in zip(src,lines):
    if not m: out.append(l); continue
    ws=m.group(2).split(); nw=[]
    for w in ws:
        nw.append(res.get(i,w)); i+=1
    out.append(m.group(1)+': '+' '.join(nw))
open('targets/r9416/r9416/_c/lmsplit.txt','w',encoding='utf8').write('\n'.join(out))
