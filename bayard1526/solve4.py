import sys,random,math
sys.path.insert(0,'..')
from lang import lm
M=lm.load('fr-1530-despatches',order=5,spaces=False)
rows=[l.split()[1:] for l in open('ct2.txt') if l.startswith('L')]
toks=[s for r in rows for s in r]
S=sorted(set(toks)); ix={s:i for i,s in enumerate(S)}
ct=[ix[s] for s in toks]
A='abcdefghilmnopqrstuxyz'; H=set('aeiounrst')
def ok(k):
    from collections import Counter
    c=Counter(k); return all(v<=1 or l in H for l,v in c.items()) and all(v<=3 for v in c.values())
def dec(k): return ''.join(k[c] for c in ct)
def sc(k): return M.score_idx(M.encode(dec(k)))
res=[]
for run in range(int(sys.argv[1])):
    k=random.sample(A,len(A))+random.choices('aeiounrst',k=len(S)-len(A))
    while not ok(k): k=random.sample(A,len(A))+random.choices('aeiounrst',k=len(S)-len(A))
    s=sc(k);T=3.0
    for it in range(40000):
        k2=k[:]
        if random.random()<.5: i,j=random.sample(range(len(S)),2);k2[i],k2[j]=k2[j],k2[i]
        else: k2[random.randrange(len(S))]=random.choice(A)
        if not ok(k2): continue
        s2=sc(k2)
        if s2>s or random.random()<math.exp((s2-s)/T): k,s=k2,s2
        T=max(0.05,T*0.99985)
    res.append((s,dec(k)))
for s,d in sorted(res,reverse=True)[:8]: print(round(s/len(ct),3),d)
