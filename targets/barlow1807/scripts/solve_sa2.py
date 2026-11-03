import sys,re,math,random,collections
sys.path.insert(0,'scripts'); from parse import words
corp=open('corpus/federalist.txt',encoding='utf8').read().lower()
corp=re.sub(r'[^a-z]+',' ',corp)
import os
TR=os.environ.get('TR','')
if TR=='novowel': corp=' '.join(re.sub('[aeiou]','',w) or w for w in corp.split())
if TR=='noninit': corp=' '.join(w[0]+re.sub('[aeiou]','',w[1:]) for w in corp.split())
if TR=='noe': corp=' '.join(w[0]+w[1:].replace('e','') for w in corp.split())
N=4; cnt=collections.Counter(corp[i:i+N] for i in range(len(corp)-N))
tot=sum(cnt.values()); floor=math.log(0.5/tot)
LP={k:math.log(v/tot) for k,v in cnt.items()}
vocab=collections.Counter(corp.split())
VOC={w for w,c in vocab.items() if c>=2}
lf=collections.Counter(c for c in corp if c!=' '); lt=sum(lf.values())
EXP={c:lf[c]/lt for c in 'abcdefghijklmnopqrstuvwxyz'}
pages=sys.argv[1].split(','); seed=int(sys.argv[2]); WB=float(sys.argv[3]) if len(sys.argv)>3 else 3.0
cw=[]
for p in pages:
    for k,v in words(open(f'trans_raw/p{p}_A.txt',encoding='utf8').read()):
        if k=='C':
            v=[t for t in v if t and len(t)<=2]
            if v: cw.append(v)
syms=sorted({t for w in cw for t in w}); n=sum(len(w) for w in cw)
random.seed(seed); L='abcdefghijklmnopqrstuvwxyz'
key={s:random.choices(L,weights=[EXP[c] for c in L])[0] for s in syms}
def score(key):
    s=0; lc=collections.Counter()
    for w in cw:
        d=''.join(key[x] for x in w); lc.update(d)
        t=' '+d+' '
        for i in range(len(t)-N+1): s+=LP.get(t[i:i+N],floor)
        if d in VOC: s+=WB*len(d)
    kl=sum(v*math.log((v/n)/EXP[c]) for c,v in lc.items())
    return s-2*kl
if os.environ.get('INIT'):
    for kv in open(os.environ['INIT']).read().split():
        a,b=kv.split('=')
        if a in key: key[a]=b
cur=score(key); best=(cur,dict(key)); T=float(os.environ.get('T0','20'))
for it in range(int(sys.argv[4]) if len(sys.argv)>4 else 80000):
    old=dict(key); s1=random.choice(syms)
    if random.random()<0.5: key[s1]=random.choice(L)
    else:
        s2=random.choice(syms); key[s1],key[s2]=key[s2],key[s1]
    new=score(key)
    if new>cur or random.random()<math.exp((new-cur)/T): cur=new
    else: key=old
    T=max(0.3,T*0.99994)
    if cur>best[0]: best=(cur,dict(key))
key=best[1]
print(round(best[0]))
print(' '.join(''.join(key[x] for x in w) for w in cw[:150]))
print(' '.join(f'{s}={key[s]}' for s in syms))
