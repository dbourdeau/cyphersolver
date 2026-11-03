# EM alignment of the machine labels of ff. 9r-9v with their gloss. Usage: em.py <seed> <seconds> [noseed]
# As run for the frozen table, 14 sign values (the dict known) were fixed in every restart. Pass noseed to start every restart from
# a fully random table. The seven frozen nulls (Ex, Eo, n:, m:, d:, e, ii) were set by hand afterwards: EM gave them letters.
import numpy as np, re, random, sys, pickle
from collections import Counter, defaultdict
gloss=open('marginal_gloss_9r_9v.txt',encoding='utf8').read()
parts=re.split(r'\n\n',gloss)
txt=' '.join(p.split('\n',1)[1] for p in parts[1:4])
txt=txt.replace('[ae]','ae').replace('[a]','a').replace('[er]','er').replace('(que)','que').replace('(?)','').replace('?','')
P=''.join(c for c in txt.lower() if c.isalpha()).replace('j','i').replace('v','u').replace('y','i')
C=[];POS=[]
for l in open('pass_A_machine.txt',encoding='utf8'):
    if l.startswith('9r') or l.startswith('9v'):
        for x in l.split()[1:]:
            if x.rstrip('?')!='|': C.append(x.rstrip('?')); POS.append(l.split()[0])
print(len(C),len(P)); print(P[:150])
syms=sorted(set(C)); sid={s:i for i,s in enumerate(syms)}
letters=sorted(set(P)); lid={c:i for i,c in enumerate(letters)}
Ci=np.array([sid[c] for c in C]); Pi=np.array([lid[c] for c in P])
n,m=len(Ci),len(Pi)
GAPC=-0.4; GAPP=-1.0; MATCH=2.0; MIS=-1.0
def dp(M,trace=False):
    # M: sym->letter id (-1 null)
    prev=np.arange(m+1)*GAPP
    ptr=np.zeros((n+1,m+1),dtype=np.int8) if trace else None
    j=np.arange(m+1)
    for i in range(1,n+1):
        ml=M[Ci[i-1]]
        sc=np.where(Pi==ml,MATCH,MIS)
        diag=prev[:-1]+sc
        up=prev+GAPC
        t=up.copy(); t[1:]=np.maximum(t[1:],diag)
        cur=np.maximum.accumulate(t-j*GAPP)+j*GAPP
        if trace:
            q=np.zeros(m+1,dtype=np.int8) # 0 up
            q[1:][diag>=up[1:]]=1
            q[(cur>t+1e-9)]=2
            ptr[i]=q
        prev=cur
    if not trace: return prev[m]
    pairs=[];i,k=n,m
    while i>0 or k>0:
        if i>0 and k>0 and ptr[i,k]==1: pairs.append((i-1,k-1)); i-=1;k-=1
        elif k>0 and (i==0 or ptr[i,k]==2): k-=1
        else: i-=1
    return prev[m],pairs[::-1]
def em(M,it=12):
    best=-1e9
    for _ in range(it):
        s,pairs=dp(M,True)
        cnt=np.zeros((len(syms),len(letters)))
        for i,k in pairs: cnt[Ci[i],Pi[k]]+=1
        M2=cnt.argmax(1)
        if (M2==M).all(): break
        M=M2
    return dp(M),M
random.seed(int(sys.argv[1]) if len(sys.argv)>1 else 1)
freq=Counter(P); pool=list(P)
best=(-1e9,None)
import time;t0=time.time()
M0=np.array([lid[random.choice(pool)] for _ in syms])
known={} if 'noseed' in sys.argv else {'3':'i','oo':'s','V':'t','Ls':'r','A':'e','<':'e','U':'u','ou':'n','u':'a','Th':'o','P':'c','Hs':'r','D':'m','I:':'m'}
restarts=0
while time.time()-t0<float(sys.argv[2]) :
    M=np.array([lid[random.choice(pool)] for _ in syms])
    for k,v in known.items():
        M[sid[k]]=lid[v]
    s,M=em(M); restarts+=1
    if s>best[0]:
        best=(s,M.copy()); print(restarts,round(s,1),{syms[i]:letters[M[i]] for i in range(len(syms))},flush=True)
import os; os.makedirs('work',exist_ok=True); pickle.dump((best,syms,letters),open('work/em_best.pkl','wb'))
