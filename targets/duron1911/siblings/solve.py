import random, math
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..')); from lang import lm
m=lm.load('es-modern')
A='abcdefghijklmnopqrstuvwxyz'
def anneal(ct, iters=40000, seed=0):
    rnd=random.Random(seed); key=list(A); rnd.shuffle(key)
    dec=lambda k: ''.join(k[A.index(c)] if c in A else c for c in ct)
    sc=lambda k: m.per_char(dec(k))
    cur=sc(key); best=(cur,key[:])
    for i in range(iters):
        T=0.4*(1-i/iters)+0.01
        k=key[:]; x,y=rnd.sample(range(26),2); k[x],k[y]=k[y],k[x]
        s=sc(k)
        if s>cur or rnd.random()<math.exp((s-cur)/T*10): key,cur=k,s
        if cur>best[0]: best=(cur,key[:])
    return best[0], dec(best[1])
def run(ct, n=6):
    return max(anneal(ct,seed=s) for s in range(n))
if __name__=='__main__':
    import sys
    gab='hdylq gbfvl sgyln pvdhr egblht dn vdble gbgyrsl aghle pqpbl qgebyl brhth lnfyr btvrh rerbl'
    plain='urge ver al senor madero hoy mismo diga usted si llegaron las armas que pidio el general'
    r=random.Random(7); k=list(A); r.shuffle(k)
    ctl=''.join(k[A.index(c)] if c in A else c for c in plain)
    print('control', run(ctl)); print('gabriel', run(gab))
