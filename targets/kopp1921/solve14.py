"""Strip a period-p key with the whole-group model: python solve14.py <frame> <minlen> <p> [digit|mod]"""
import json,sys,collections,math,random
import numpy as np
sys.stdout.reconfigure(encoding='utf-8')
P=[g for f in ('lutowinoff417_ct.txt','kopp0876_ct.txt','kopp0877_ct.txt') for g in open(f).read().split() if '?' not in g]
F=collections.Counter(g[:2] for g in P);S=collections.Counter(g[2:] for g in P);C=collections.Counter(P);n=len(P);V=set(P)
LP=np.array([math.log(C[f'{v:04d}']/n*.5+(F[f'{v:04d}'[:2]]+.05)/(n+5)*(S[f'{v:04d}'[2:]]+.05)/(n+5)*.5) for v in range(10000)])
D=np.array([[int(c) for c in f'{v:04d}'] for v in range(10000)])
W=np.array([1000,100,10,1])
def sub_all(col,mode):
    # returns matrix keys x tokens of stripped values
    if mode=='mod': return (col[None,:]-np.arange(10000)[:,None])%10000
    return (((D[col][None,:,:]-D[:,None,:])%10)*W).sum(2)
M=[json.loads(l) for l in open('messages_ocr.jsonl',encoding='utf-8')]
f,mn,p=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]);mode=sys.argv[4] if len(sys.argv)>4 else 'digit'
m=[m for m in M if f in m['file'] and m['n']>=mn and m['len']==4][0]
g=np.array([int(x) for x in m['groups'] if len(x)==4 and x.isdigit()])
print(m['file'],len(g),m['head'][-40:])
keys=[];tot=0
for c in range(p):
    col=g[c::p];sc=LP[sub_all(col,mode)].sum(1);o=np.argsort(-sc)[:3];keys.append(int(o[0]));tot+=sc[o[0]]
    print(c,len(col),[f'{int(k):04d}:{sc[k]/len(col):.2f}' for k in o])
out=[]
for i,x in enumerate(g):
    k=keys[i%p]
    v=(x-k)%10000 if mode=='mod' else int(((D[x]-D[k])%10@W))
    out.append(f'{v:04d}')
print('LL/token',round(tot/len(g),3),'in vocab',round(sum(x in V for x in out)/len(out),3))
print(' '.join(out))
print(collections.Counter(out).most_common(30))
json.dump({'keys':keys,'out':out},open(f'strip_{f}_{p}.json','w'))
