"""EM on a period-p key. The token model is relearned from the plain family plus the current strip.
Independent check: bigram repeats in the strip at lags that are not multiples of p (a wrong key cannot make these)."""
import json,sys,collections,math,random
import numpy as np
sys.stdout.reconfigure(encoding='utf-8')
P=[g for f in ('lutowinoff417_ct.txt','kopp0876_ct.txt','kopp0877_ct.txt') for g in open(f).read().split() if '?' not in g]
D=np.array([[int(c) for c in f'{v:04d}'] for v in range(10000)]);W=np.array([1000,100,10,1])
SUB=None
def table(tok,beta):
    F=collections.Counter(t[:2] for t in tok);S=collections.Counter(t[2:] for t in tok);C=collections.Counter(tok);n=len(tok)
    return np.array([math.log(C[f'{v:04d}']/n*beta+(1-beta)*(F[f'{v:04d}'[:2]]+.05)/(n+5)*(S[f'{v:04d}'[2:]]+.05)/(n+5)) for v in range(10000)])
def strip(col,keys):
    return (((D[col][None,:,:]-D[keys][:,None,:])%10)*W).sum(2)
M=[json.loads(l) for l in open('messages_ocr.jsonl',encoding='utf-8')]
f,mn,p=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]);restarts=int(sys.argv[4]) if len(sys.argv)>4 else 1
m=[m for m in M if f in m['file'] and m['n']>=mn and m['len']==4][0]
g=np.array([int(x) for x in m['groups'] if len(x)==4 and x.isdigit()])
allk=np.arange(10000)
def decode(k): return [f'{int(((D[x]-D[k[i%p]])%10)@W):04d}' for i,x in enumerate(g)]
def bigram_rep(o):
    pos=collections.defaultdict(list)
    for i in range(len(o)-1): pos[(o[i],o[i+1])].append(i)
    return sum(1 for v in pos.values() for a in range(len(v)) for b in range(a+1,len(v)) if (v[b]-v[a])%p)
best=None
for r in range(restarts):
    random.seed(r)
    LP=table(P,.5);keys=[None]*p
    for c in range(p):
        sc=LP[strip(g[c::p],allk)].sum(1);keys[c]=int(np.argmax(sc)) if r==0 else int(random.choice(np.argsort(-sc)[:5]))
    for it in range(12):
        out=decode(keys);LP=table(P+out,.6)
        for c in range(p):
            out=decode(keys);rest=[t for i,t in enumerate(out) if i%p!=c]
            LPc=table(P+rest,.6)
            sc=LPc[strip(g[c::p],allk)].sum(1);keys[c]=int(np.argmax(sc))
    out=decode(keys);LP=table(P+out,.6);ll=float(LP[[int(x) for x in out]].sum())/len(out)
    rp=bigram_rep(out)
    print(r,round(ll,3),'bigram repeats',rp,[f'{k:04d}' for k in keys],flush=True)
    if best is None or rp>best[0]: best=(rp,keys,out)
rp,keys,out=best
V=set(P)
print('in vocab',round(sum(x in V for x in out)/len(out),3),'distinct',len(set(out)))
print(' '.join(out))
print(collections.Counter(out).most_common(25))
json.dump({'file':m['file'],'p':p,'keys':keys,'out':out},open(f'em_{f}_{p}.json','w'))
