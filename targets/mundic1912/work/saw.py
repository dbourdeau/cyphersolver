import re,random,math,sys,unicodedata
from collections import Counter
raw=open('work/corpus/pg2000.txt',encoding='utf-8').read()+open('work/corpus/pg15532.txt',encoding='utf-8').read()
raw=unicodedata.normalize('NFD',raw.lower()); raw=''.join(c for c in raw if not unicodedata.combining(c))
txt=re.sub('[^a-z]+',' ',raw)
q=Counter(txt[i:i+4] for i in range(len(txt)-3)); N=sum(q.values())
floor=math.log10(0.01/N); Q={k:math.log10(v/N) for k,v in q.items()}
def score(s): return sum(Q.get(s[i:i+4],floor) for i in range(len(s)-3))
ct=' '+sys.argv[1]+' '
A='abcdefghijklmnopqrstuvwxyz'
fixed=dict(p.split('=') for p in sys.argv[4].split(',')) if len(sys.argv)>4 else {}
best=[]
for restart in range(int(sys.argv[2])):
    key=list(A); random.shuffle(key)
    for c,p in fixed.items():
        j=key.index(p); i=A.index(c); key[i],key[j]=key[j],key[i]
    free=[i for i in range(26) if A[i] not in fixed]
    def dec(k): m=dict(zip(A,k)); m[' ']=' '; return ''.join(m[c] for c in ct)
    cur=score(dec(key)); T=10
    for it in range(int(sys.argv[3])):
        i,j=random.sample(free,2)
        if A[j] in fixed: continue
        key[i],key[j]=key[j],key[i]
        s=score(dec(key))
        if s>cur or random.random()<math.exp((s-cur)/T): cur=s
        else: key[i],key[j]=key[j],key[i]
        T=max(0.2,T*0.9997)
    best.append((round(cur,1),dec(key)))
for b in sorted(best)[-6:]: print(b)
