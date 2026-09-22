"""Exhaustive hill-climb + shotgun restarts for the R4350 homophonic hypothesis.
usage: RUNS=file python hclimb.py seed seconds [order]"""
import os,sys,random,time,json
import numpy as np
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
sys.stdout.reconfigure(encoding='utf-8')
from lang import lm
HERE=os.path.dirname(os.path.abspath(__file__))
seed=int(sys.argv[1]); secs=float(sys.argv[2]); order=int(sys.argv[3]) if len(sys.argv)>3 else 4
M=lm.load('de-modern',order=order,spaces=False); alpha=M.alpha; L=len(alpha)
runs=[l.split() for l in open(os.path.join(HERE,os.environ.get('RUNS','runs.txt')),encoding='utf8') if l.strip()]
codes=sorted({x for r in runs for x in r if x.isdigit()},key=int); ci={c:i for i,c in enumerate(codes)}; n=len(codes)
tpl=[]
for r in runs:
    for x in r:
        if x.isdigit(): tpl.append(ci[x])
        else: tpl+=[-(alpha.index(ch)+1) for ch in lm.norm(x,'modern',spaces=False)]
tpl=np.array(tpl); isc=tpl>=0; fixed=np.where(isc,0,-tpl-1); idx=np.clip(tpl,0,None)
def sc(key): return M.score_idx(np.where(isc,key[idx],fixed))
rnd=random.Random(seed)
uni='eeeeeeeeennnnnnnnniiiiiiisssssssrrrrrrraaaaaatttttdddddhhhhhuuuulllcccggmmoobbwwffkzp'
LET=[alpha.index(c) for c in 'abcdefghiklmnoprstuwzv']
def climb(key,cur):
    improved=True
    while improved:
        improved=False
        for i in rnd.sample(range(n),n):
            old=key[i]; bl=old; bs=cur
            for l in LET:
                if l==old: continue
                key[i]=l; s=sc(key)
                if s>bs: bs,bl=s,l
            key[i]=bl
            if bl!=old: cur=bs; improved=True
    return key,cur
t0=time.time(); best=None
key=np.array([alpha.index(rnd.choice(uni)) for _ in codes]); key,cur=climb(key,sc(key))
gb=(cur,key.copy())
while time.time()-t0<secs:
    k2=gb[1].copy()
    for _ in range(rnd.randint(3,max(4,n//6))): k2[rnd.randrange(n)]=alpha.index(rnd.choice(uni))
    if rnd.random()<0.05: k2=np.array([alpha.index(rnd.choice(uni)) for _ in codes])
    k2,c2=climb(k2,sc(k2))
    if c2>gb[0]: gb=(c2,k2.copy()); print(round(time.time()-t0),round(c2/len(tpl),3),flush=True)
key=gb[1]; d=np.where(isc,key[idx],fixed); txt=''.join(alpha[k] for k in d)
print('final',round(gb[0]/len(tpl),3)); print(txt[:400])
json.dump({c:alpha[key[ci[c]]] for c in codes},open(os.path.join(HERE,f'ckey_{os.path.basename(os.environ.get("RUNS","runs.txt"))}_{seed}.json'),'w'))
