import sys, random, json
sys.path.insert(0, __file__.rsplit('/',1)[0])
from lib import *
P_=15
def dec(c,k,rule):
    K=k[np.arange(len(c))%P_]
    return (c-K)%26 if rule=='vig' else (K-c)%26
def climb(c, rule, rng, restarts=30):
    n=len(c); pos=np.arange(n)%P_; best=(-99,None)
    for r in range(restarts):
        k=np.array([rng.randrange(26) for _ in range(P_)]); cur=qs(dec(c,k,rule))
        improved=True
        while improved:
            improved=False
            for j in range(P_):
                KK=np.tile(k,(26,1)); KK[:,j]=np.arange(26)
                Kfull=KK[:,pos]
                Pm=(c[None,:]-Kfull)%26 if rule=='vig' else (Kfull-c[None,:])%26
                s=qs(Pm); i=int(np.argmax(s))
                if s[i]>cur+1e-9: cur=float(s[i]); k=KK[i].copy(); improved=True
        if cur>best[0]: best=(cur,k.copy())
    return best
mode=sys.argv[1]
rng=random.Random(1865)
if mode=='calib':
    ok=0; tot=0
    for uid in ['T03','T05','T06','T08','T09','S1','S2']:
        true=arr(UNITS[uid][3]); rec=[]
        for r in readers(uid):
            c=arr(''.join(groups(uid,r))); s,k=climb(c,'vig',rng)
            m=max(int((k==np.roll(true,-o)).sum()) for o in range(15))
            rec.append(m); print(uid,r,len(c),round(s,3),txtof(k),'key letters recovered',m,'/15',txtof(dec(c,k,'vig'))[:60],flush=True)
        tot+=1; ok+= (min(rec)>=12)
    print('telegrams with >=12/15 on both readers:',ok,'of',tot)
else:
    res={}
    for r in readers('T11'):
        c=arr(''.join(groups('T11',r)))
        for rule in ['vig','beau']:
            s,k=climb(c,rule,rng)
            ctl=[]
            for t in range(100):
                l=list(c); rng.shuffle(l); ctl.append(climb(np.array(l),rule,rng)[0])
            res[f'{r}_{rule}']=dict(best=round(s,3),key=txtof(k),plain=txtof(dec(c,k,rule)),control_max=round(max(ctl),3),
                                    control_p95=round(float(np.percentile(ctl,95)),3),control_median=round(float(np.median(ctl)),3),passed=s>max(ctl))
            print(r,rule,json.dumps(res[f'{r}_{rule}']),flush=True)
    json.dump(res,open('results/f_results.json','w'),indent=1)
