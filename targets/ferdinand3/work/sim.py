import sys, os, numpy as np, multiprocessing as mp
sys.path.insert(0,'.')
IT=int(os.environ.get('IT','4000000')); W=float(os.environ.get('W','1')); T0=float(os.environ.get('T0','20'))
def make():
    import hsolve
    from lang import lm
    txt=open(r'C:\Users\dbour\cypher\lang\corpora\la-gutenberg.txt',encoding='latin-1').read()
    t=lm.norm(txt[4000000:4004000],'latin',spaces=False)[:786]
    rng=np.random.default_rng(1)
    # 107 symbols allocated proportional to freq
    f=np.array([t.count(a) for a in hsolve.ALPHA],float)
    nh=np.maximum(1,np.round(f/f.sum()*107)).astype(int)
    sym=[];start=0;homs={}
    for a,n in zip(hsolve.ALPHA,nh):
        homs[a]=list(range(start,start+n)); start+=n
    seq=np.array([rng.choice(homs[c]) for c in t],np.int64)
    truth=np.zeros(start,np.int64)
    for a,h in homs.items():
        for s in h: truth[s]=hsolve.ALPHA.index(a)
    return t,seq,start,truth
def job(seed):
    import hsolve
    t,seq,n,truth=make()
    fx=-np.ones(n,np.int64)
    b,k=hsolve.anneal(seq,n,hsolve.LP,hsolve.A,hsolve.ORDER,IT,T0,0.0,0.0,fx,fx.copy(),seed,hsolve.FREQ,W)
    d=hsolve.decode(seq,k)
    return b, sum(x==y for x,y in zip(d,t))/len(t), d[:100]
if __name__=='__main__':
    t,seq,n,truth=make(); print(n, t[:100])
    with mp.Pool(16) as p: r=p.map(job,range(16))
    r.sort(key=lambda x:-x[0])
    for x in r[:6]: print(round(x[0],1), round(x[1],3), x[2])
