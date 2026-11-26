"""solve.py seed iters [crib] [nullable] : homophonic SA on the TRAINING letters only. crib = 'engelsk' pins the pattern-word signs."""
import sys,random,math
sys.path.insert(0,'/home/claude/keyless/rosenkrantz1629/tools')
from common import *
seed=int(sys.argv[1]); iters=int(sys.argv[2]); crib=sys.argv[3] if len(sys.argv)>3 else 'none'; nullable=len(sys.argv)>4
import os
MERGE={}
ms=os.environ.get('MERGE','')
M1b=[['D8','TH','OU'],['CD','U','CU'],['PF','GM','BX'],['X4','+','4','XA','X3'],['LD','LH'],['RH','FM'],['OM','OMb'],['PI','MM'],['TB','OX']]
M1a=[['D8','TH','OU','CD','U','CU']]+M1b[2:]
M2=[['D8','TH','OU'],['CD','U','CU','OO','TB','OX'],['PF','GM','BX','AR'],['X4','+','4','XA','X3','PM'],['HB','HH','H'],['LD','LH'],['PI','MM'],['RH','FM','FO'],['OM','OMb'],['DD','DB'],['V','VR','TV']]
M4=[['D8','TH','OU'],['CD','U','CU'],['OO','TB','OX'],['PF','GM'],['X4','4','XA','X3'],['+','PM'],['HB','HH','H'],['LD','LH'],['PI','MM'],['RH','FM'],['OM','OMb'],['V','TV']]
DIG=set('1235679')
for grp in {'M1a':M1a,'M1b':M1b,'M2':M2,'M3':M2,'M4':M4,'M5':M4}.get(ms,[]):
    for g in grp: MERGE[g]=grp[0]
DROP={'RG'} if ms else set()
if ms in('M3','M5'): DROP|=DIG
rows=load(); rows=[(a,b,c,[[MERGE.get(t,t) for t in s if t not in DROP] for s in segs]) for a,b,c,segs in rows]
segs=[s for r in rows if r[0] in TRAIN for s in r[3]]
types=sorted({t for s in segs for t in s}); lm=LM()
A='abcdefghiklmnoprstuvy'+('_' if nullable else '')
pin={}
if crib=='engelsk':
    pin={'D8':'e','TH':'e','OU':'e','PF':'n','GM':'n','X4':'g','LD':'l','RH':'s','FM':'s','OM':'k','OMb':'k'}
    pin={k:v for k,v in pin.items() if MERGE.get(k,k)==k}
def dec(key): return [''.join(key[t] for t in s).replace('_','') for s in segs]
import collections
_t=open(R+'/lm/da1620.txt').read().replace(' ','');EXP={c:_t.count(c)/len(_t) for c in set(_t)}
FW=float(sys.argv[5]) if len(sys.argv)>5 else 1.0
def sc(key):
    d=dec(key); j=''.join(d); n=len(j) or 1; c=collections.Counter(j)
    chi=sum((c.get(a,0)-EXP.get(a,0)*n)**2/(EXP.get(a,0.001)*n) for a in A if a!='_')
    return sum(lm.score(x) for x in d)-FW*chi
best=None
rnd=random.Random(seed)
NR=int(os.environ.get('NR','4'))
for restart in range(NR):
    key={t:pin.get(t,rnd.choice('eadnrtsilo')) for t in types}; cur=sc(key); T=3.0
    free=[t for t in types if t not in pin]
    for i in range(iters):
        if rnd.random()<0.5:
            t=rnd.choice(free); old=key[t]; key[t]=rnd.choice(A)
            if key[t]==old: continue
            new=sc(key)
            if new>cur or rnd.random()<math.exp((new-cur)/T): cur=new
            else: key[t]=old
        else:
            t,u=rnd.sample(free,2)
            if key[t]==key[u]: continue
            key[t],key[u]=key[u],key[t]; new=sc(key)
            if new>cur or rnd.random()<math.exp((new-cur)/T): cur=new
            else: key[t],key[u]=key[u],key[t]
        T=max(0.08,T*(0.03**(1.0/iters)))
    if best is None or cur>best[0]: best=(cur,dict(key))
print('merge',ms,'seed',seed,'iters',iters,'crib',crib,'nullable',nullable,'types',len(types),'letters',sum(map(len,segs)),'score %.1f'%best[0])
print(' '.join(f'{k}={v}' for k,v in sorted(best[1].items())))
key=best[1]
for r in rows:
    if r[0] in TRAIN: print(r[0],r[1],r[2],' | '.join(''.join(key[t] for t in s) for s in r[3]))
