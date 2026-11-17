import re,collections,json
c=open('../../../sforza1597/ctts/lm_qc/italian.txt',encoding='utf-8',errors='ignore').read().lower().replace('u','v')
W=set(w for w,n in collections.Counter(re.findall('[a-z]{4,12}',c)).items() if n>=3)
def mask(s):
    n=len(s);best=[0]*(n+1);bp=[None]*(n+1)
    for i in range(n):
        if best[i]>=best[i+1]: best[i+1]=best[i];bp[i+1]=(i,0)
        for L in range(4,13):
            if i+L<=n and s[i:i+L] in W and best[i]+L>best[i+L]: best[i+L]=best[i]+L;bp[i+L]=(i,1)
    m=[0]*n;j=n
    while j>0:
        i,ok=bp[j]
        for t in range(i,j): m[t]=ok
        j=i
    return m
k=json.load(open('key_h4.json')); L=[l.split() for l in open('t7.txt').read().strip().split('\n')]
U=collections.Counter();A=collections.Counter();su=collections.Counter();sa=collections.Counter()
for t in L:
    s=''.join(k.get(x,'?') for x in t); m=mask(s)
    for i,x in enumerate(t):
        sa[x]+=1; su[x]+= (m[i]==0)
    for n in (2,3,4):
        for i in range(len(t)-n+1):
            g=' '.join(t[i:i+n]);A[g]+=1
            if sum(m[i:i+n])==0: U[g]+=1
print('per-sign unread rate (>=10 uses, worst first):')
print(' '.join(f"{x}={k.get(x)}:{su[x]}/{sa[x]}" for x in sorted(sa,key=lambda x:-su[x]/sa[x]) if sa[x]>=10))
print('recurring unread n-grams:')
for g,u in sorted(U.items(),key=lambda x:-(x[1]-1)*len(x[0].split()))[:30]:
    if u>=3: print(' ',g,f'{u}/{A[g]}',''.join(k.get(x,'?') for x in g.split()))
