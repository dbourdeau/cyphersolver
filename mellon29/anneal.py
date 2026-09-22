import sys,os,random,math
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..'))
from lang import lm
model=sys.argv[1] if len(sys.argv)>1 else 'it-cinquecento'
M=lm.load(model,order=4,spaces=True)
alpha=[c for c in M.alpha if c!=' ']
lines=[l for l in open(os.path.join(os.path.dirname(__file__),'ct_v1.txt'),encoding='utf8') if not l.startswith('#') and l.strip()]
words=[]
for l in lines:
    t=l.split()
    if t[0][0].isupper() and len(t)>1 and t[0] in('Ariete','Taurus','Gemini','Cancer','Leo','Virgo','Libra','Scorpio','Sagitarius','Capricorno','Aquario','Pissis'): t=t[1:]
    for w in t:
        w=w.replace('.','').replace('~','').replace('^','').replace('∫','s').lower()
        if w in('in','cioe'): continue
        if w: words.append(w)
ct=' '.join(words); syms=sorted(set(ct)-{' '})
print(ct); print(len(ct.replace(' ','')),'syms',len(syms),''.join(syms))
def dec(k): return ''.join(k.get(c,c) for c in ct)
def sc(k): return M.score(dec(k))
best=None
for r in range(int(sys.argv[2]) if len(sys.argv)>2 else 20):
    pool=alpha[:]; random.shuffle(pool); pool=pool+['#']*(len(syms)-len(pool)) if len(syms)>len(pool) else pool
    k={c:pool[i] for i,c in enumerate(syms)}; spare=pool[len(syms):]; s=sc(k); T=3.0
    for it in range(40000):
        a=random.choice(syms)
        if spare and random.random()<0.3:
            j=random.randrange(len(spare)); o=k[a]; k[a],spare[j]=spare[j],o; n=sc(k)
            if n>s or random.random()<math.exp((n-s)/T): s=n
            else: spare[j]=k[a]; k[a]=o
        else:
            b=random.choice(syms); k[a],k[b]=k[b],k[a]; n=sc(k)
            if n>s or random.random()<math.exp((n-s)/T): s=n
            else: k[a],k[b]=k[b],k[a]
        T=max(0.05,T*0.9997)
    if best is None or s>best[0]: best=(s,dict(k))
    print(round(s/len(ct),3),dec(k))
print('BEST',best[0]/len(ct),dec(best[1]))
