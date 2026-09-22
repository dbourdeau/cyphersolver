"""Homophonic letter annealer for R4350: every code -> one letter; clear words kept as fixed letters.
usage: python hanneal.py seed iters [model] [order]"""
import os,sys,re,random,math,json
import numpy as np
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
sys.stdout.reconfigure(encoding='utf-8')
from lang import lm
HERE=os.path.dirname(os.path.abspath(__file__))
seed=int(sys.argv[1]); iters=int(sys.argv[2]); model=sys.argv[3] if len(sys.argv)>3 else 'de-modern'; order=int(sys.argv[4]) if len(sys.argv)>4 else 5
M=lm.load(model,order=order,spaces=False); alpha=M.alpha; L=len(alpha)
runs=[l.split() for l in open(os.path.join(HERE,os.environ.get('RUNS','runs.txt')),encoding='utf8') if l.strip()]
codes=sorted({x for r in runs for x in r if x.isdigit()},key=int); ci={c:i for i,c in enumerate(codes)}; n=len(codes)
# flat template: code index or -(letter+1)
tpl=[]; 
for r in runs:
    for x in r:
        if x.isdigit(): tpl.append(ci[x])
        else: tpl+= [-(alpha.index(ch)+1) for ch in lm.norm(x,'modern',spaces=False)]
tpl=np.array(tpl); isc=tpl>=0; fixed=np.where(isc,0,-tpl-1)
FIX=json.load(open(os.path.join(HERE,os.environ['FIX']),encoding='utf8')) if os.environ.get('FIX') else {}
def dec(key): return np.where(isc,key[np.clip(tpl,0,None)],fixed)
EXP=np.array([{'e':.165,'n':.098,'i':.076,'s':.07,'r':.07,'a':.063,'t':.061,'d':.051,'h':.047,'u':.042,'l':.034,'c':.03,'g':.03,'m':.025,'o':.025,'b':.019,'w':.019,'f':.017,'k':.012,'z':.011,'p':.008,'v':.008}.get(c,.002) for c in alpha])
W=float(os.environ.get('UW','1.0'))
def fscore(d):
    cnt=np.bincount(d,minlength=L)+0.5; N=cnt.sum()
    p=cnt/N; return M.score_idx(d)-W*N*np.sum(p*np.log(p/EXP))

rnd=random.Random(seed)
uni='eeeeeeeeennnnnnnnniiiiiiisssssssrrrrrrraaaaaatttttdddddhhhhhuuuulllcccggmmoobbwwffkzp'
key=np.array([alpha.index(rnd.choice(uni)) for _ in codes])
for c,v in FIX.items():
    if c in ci: key[ci[c]]=alpha.index(v)
free=[i for i,c in enumerate(codes) if c not in FIX]
cur=fscore(dec(key)); best=(cur,key.copy())
T0=float(os.environ.get('T0','15'))
for it in range(iters):
    T=T0*(0.2/T0)**(it/iters)
    i=rnd.choice(free); old=key[i]; j=None
    if rnd.random()<0.8: key[i]=rnd.randrange(L)
    else:
        j=rnd.choice(free); key[i],key[j]=key[j],key[i]
    s=fscore(dec(key))
    if s>=cur or rnd.random()<math.exp((s-cur)/T):
        cur=s
        if cur>best[0]: best=(cur,key.copy())
    else:
        if j is None: key[i]=old
        else: key[i],key[j]=key[j],key[i]
key=best[1]
d=dec(key); N=len(d)
print('seed',seed,'per_char',round(best[0]/N,3))
txt=''.join(alpha[k] for k in d)
out=[];p=0
for r in runs:
    s=''
    for x in r:
        if x.isdigit(): s+=txt[p]; p+=1
        else:
            w=lm.norm(x,'modern',spaces=False); s+=w.upper(); p+=len(w)
    out.append(s)
print('\n'.join(out))
json.dump({c:alpha[key[ci[c]]] for c in codes},open(os.path.join(HERE,f'hkey_{seed}.json'),'w'))
