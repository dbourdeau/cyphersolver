import sys,os,random,math,collections,json
sys.path.insert(0,'..')
from lang import lm
from decode import KEY,load
M=lm.load('fr-1530-despatches')
VALS=list('abcdefghilmnopqrstuxyz')
def segs(L):
    S=[];cur=[]
    for _,l in L:
        for t in l:
            if t=='...':
                if cur: S.append(cur); cur=[]
            else: cur.append(t)
    if cur: S.append(cur)
    return S
def text(S,k):
    return ['' .join(k[t] for t in s) for s in S]
def score(S,k):
    return sum(M.score_idx(M.encode(lm.norm(x,'early'))) for x in text(S,k) if len(x)>3)
def anneal(S,k,free,iters=20000,T0=3.0,seed=0):
    rnd=random.Random(seed); cur=score(S,k); best=(cur,dict(k))
    for i in range(iters):
        T=T0*(1-i/iters)+0.05
        s=rnd.choice(free); old=k[s]; k[s]=rnd.choice(VALS)
        new=score(S,k)
        if new>=cur or rnd.random()<math.exp((new-cur)/T): cur=new
        else: k[s]=old
        if cur>best[0]: best=(cur,dict(k))
    return best
if __name__=='__main__':
    files=sys.argv[1].split(','); mode=sys.argv[2] if len(sys.argv)>2 else 'unk'
    L=load(files); S=segs(L)
    syms=sorted({t for s in S for t in s})
    k={s:KEY.get(s,'') for s in syms}
    k={s:v.strip('[]') for s,v in k.items()}
    free=[s for s in syms if s not in KEY] if mode=='unk' else [s for s in syms if s not in ('1','n')]
    for s in free:
        if k[s]=='': k[s]='e'
    print('free',free, 'base',score(S,k))
    res=[anneal(S,dict(k),free,iters=int(sys.argv[3]) if len(sys.argv)>3 else 6000,seed=r) for r in range(3)]
    res.sort(key=lambda r:-r[0])
    for sc,kk in res: print(round(sc),{s:kk[s] for s in free})
    kk=res[0][1]
    for (name,l) in L: print(name,''.join('…' if t=='...' else kk[t] for t in l))
    json.dump(kk,open('fit_'+mode+'.json','w'),ensure_ascii=False)
