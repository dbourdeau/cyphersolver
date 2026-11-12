import re,random,math,sys,unicodedata
from collections import Counter
raw=open('work/corpus/pg2000.txt',encoding='utf-8').read()+open('work/corpus/pg15532.txt',encoding='utf-8').read()
raw=unicodedata.normalize('NFD',raw.lower()); raw=''.join(c for c in raw if not unicodedata.combining(c))
txt=re.sub('[^a-z]','',raw)
q=Counter(txt[i:i+4] for i in range(len(txt)-3)); N=sum(q.values())
floor=math.log10(0.01/N); Q={k:math.log10(v/N) for k,v in q.items()}
def score(s): return sum(Q.get(s[i:i+4],floor) for i in range(len(s)-3))
ct=sys.argv[1].replace(' ','')
A='abcdefghijklmnopqrstuvwxyz'
best_all=None
for restart in range(int(sys.argv[2]) if len(sys.argv)>2 else 20):
    key=list(A); random.shuffle(key)
    def dec(k): m=dict(zip(A,k)); return ''.join(m[c] for c in ct)
    cur=score(dec(key)); T=10
    for it in range(int(sys.argv[3]) if len(sys.argv)>3 else 20000):
        i,j=random.sample(range(26),2); key[i],key[j]=key[j],key[i]
        s=score(dec(key))
        if s>cur or random.random()<math.exp((s-cur)/T): cur=s
        else: key[i],key[j]=key[j],key[i]
        T=max(0.2,T*0.9997)
    if best_all is None or cur>best_all[0]: best_all=(cur,''.join(key),dec(key))
    print(round(cur,1),dec(key))
print('BEST',best_all)
