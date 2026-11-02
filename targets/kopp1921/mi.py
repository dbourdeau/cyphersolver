"""Where does the context live? Mutual information between neighbouring pairs against a shuffled baseline."""
import sys,random,math,collections
def mi(p):
    n=len(p);a=collections.Counter(x for x,_ in p);b=collections.Counter(y for _,y in p);j=collections.Counter(p)
    return sum(v/n*math.log2(v*n/(a[x]*b[y])) for (x,y),v in j.items())
for fs in (['karakhan_ct.txt'],['lutowinoff417_ct.txt','kopp0876_ct.txt','kopp0877_ct.txt']):
    G=[g for f in fs for g in open(f).read().split() if '?' not in g]
    print(fs,len(G),len(set(G)),collections.Counter(G).most_common(12))
    print(' F',len({g[:2] for g in G}),collections.Counter(g[:2] for g in G).most_common(20))
    print(' S',len({g[2:] for g in G}),collections.Counter(g[2:] for g in G).most_common(30))
    def stat(G):
        return {'FS':mi([(g[:2],g[2:]) for g in G]),'SF+':mi([(a[2:],b[:2]) for a,b in zip(G,G[1:])]),'FF+':mi([(a[:2],b[:2]) for a,b in zip(G,G[1:])]),'SS+':mi([(a[2:],b[2:]) for a,b in zip(G,G[1:])])}
    r=stat(G);R=[]
    for s in range(200):
        F=[g[:2] for g in G];S=[g[2:] for g in G];random.shuffle(F);random.shuffle(S);R.append(stat([x+y for x,y in zip(F,S)]))
    for k in r:
        m=sum(x[k] for x in R)/200;sd=(sum((x[k]-m)**2 for x in R)/200)**.5
        print(' ',k,round(r[k],3),'null',round(m,3),'z',round((r[k]-m)/sd,1))
