# mesure.py — mesure unique PREREG (score caractère + 200 clés mélangées, graine 1585)
import sys, random, re
def norm(s): return re.sub('[^a-z]','',s.lower()).replace('j','i').replace('v','u')
def lev(a,b):
    p=list(range(len(b)+1))
    for i,x in enumerate(a,1):
        c=[i]
        for j,y in enumerate(b,1): c.append(min(p[j]+1,c[j-1]+1,p[j-1]+(x!=y)))
        p=c
    return p[-1]
def loadkey(f):
    k={}
    for l in open(f,encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        t=l.rstrip('\n').split('\t'); k[t[0]]=t[1] if len(t)>1 else ''
    return k
def dec(k,signs): return ''.join(k.get(s,'?') if s not in ('NUL','.') else '' for s in signs)
def score(k,pairs):
    num=den=0
    for signs,gl in pairs:
        g=norm(gl); d=dec(k,signs).replace('j','i').replace('v','u')
        num+=max(0,len(g)-lev(d,g)); den+=len(g)
    return num/den if den else 0
key=loadkey(sys.argv[1])
ciph={}; 
for l in open(sys.argv[2],encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    i,s=l.rstrip('\n').split('\t'); ciph[i]=s.split()
gl={}
for l in open(sys.argv[3],encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    t=l.rstrip('\n').split('\t'); 
    if len(t)>1 and t[1].strip(): gl[t[0]]=t[1]
pairs=[(ciph[i],gl[i]) for i in ciph if i in gl]
s0=score(key,pairs)
rng=random.Random(1585)
signs=[s for s in key if key[s]]; vals=[key[s] for s in signs]
best=0
for _ in range(200):
    v=vals[:]; rng.shuffle(v); k2=dict(key); k2.update(zip(signs,v)); best=max(best,score(k2,pairs))
m=s0-best
print(f'mots={len(pairs)} lettres={sum(len(norm(g)) for _,g in pairs)} score={s0:.3f} max_nul={best:.3f} marge={m:.3f}')
print('VERDICT', 'validé' if s0>=0.85 and m>=0.30 else ('partiel' if m>=0.30 else 'échec'))
for c,g in pairs: print(' ', ' '.join(c), '->', dec(key,c), '| glose:', norm(g))
