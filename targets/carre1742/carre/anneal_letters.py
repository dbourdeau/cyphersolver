# Homophonic-letter hypothesis: every group = one plaintext letter. Anneal the assignment against a French
# 4-gram model (no spaces); compare with the same search on the ciphertext in shuffled order (control).
import sys,random,math,numpy as np
sys.path.insert(0,'../../..'); sys.path.insert(0,'.')
from lang import lm
from parse import L
m=lm.load('fr-modern',order=4,spaces=False); lp=m.lp; A=len(m.alpha); k=4
def run(seqs,iters=150000,seed=0):
    rnd=random.Random(seed)
    vals=sorted(set(sum(seqs,[]))); idx={v:i for i,v in enumerate(vals)}
    S=[np.array([idx[v] for v in s]) for s in seqs]
    occ={i:[] for i in range(len(vals))}
    for si,s in enumerate(S):
        for p,x in enumerate(s): occ[x].append((si,p))
    # initial: frequency-proportional letters
    freq=[.08,.01,.03,.04,.17,.01,.01,.01,.07,.005,.001,.055,.03,.07,.05,.03,.01,.065,.08,.07,.06,.015,.001,.004,.003,.002]
    key=np.array([rnd.choices(range(A),freq[:A])[0] for _ in vals])
    def seqscore(si):
        x=key[S[si]]; n=len(x)
        return sum(lp[int(((x[i]*A+x[i+1])*A+x[i+2])*A+x[i+3])] for i in range(n-k+1))
    def local(si,lo,hi):
        x=key[S[si]]; lo=max(0,lo); hi=min(len(x)-k,hi)
        return sum(lp[int(((x[i]*A+x[i+1])*A+x[i+2])*A+x[i+3])] for i in range(lo,hi+1))
    cur=sum(seqscore(i) for i in range(len(S))); T0=2.0
    for it in range(iters):
        T=T0*(1-it/iters)+0.05
        v=rnd.randrange(len(vals)); old=key[v]; new=rnd.randrange(A)
        if new==old: continue
        spans={}
        for si,p in occ[v]: spans.setdefault(si,[]).append(p)
        before=sum(local(si,p-k+1,p) for si,ps in spans.items() for p in ps)
        key[v]=new
        after=sum(local(si,p-k+1,p) for si,ps in spans.items() for p in ps)
        d=after-before
        if d>=0 or rnd.random()<math.exp(d/T): cur+=d
        else: key[v]=old
    tot=sum(seqscore(i) for i in range(len(S))); nch=sum(len(s)-k+1 for s in S)
    txt=[''.join(m.alpha[c] for c in key[s]) for s in S]
    return tot/nch,txt
seqs=[L[k2] for k2 in ('R2968','R2970','R2972')]
for seed in range(2):
    sc,t=run(seqs,seed=seed); print('real',seed,round(sc,3),t[1][:120])
rnd=random.Random(9); sh=[]
for s in seqs: s=s[:]; rnd.shuffle(s); sh.append(s)
for seed in range(2):
    sc,t=run(sh,seed=seed); print('shuffled',seed,round(sc,3),t[1][:120])
