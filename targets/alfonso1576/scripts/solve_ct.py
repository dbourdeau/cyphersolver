# ciphertext-only hill-climb over many-to-one tables (Italian, 20 letters), no crib.
import re,glob,random,math,sys,json,collections
import numpy as np
A='abcdefghilmnopqrstuz'; idx={c:i for i,c in enumerate(A)}
def norm(s):
    s=s.lower()
    for a,b in (('à','a'),('è','e'),('é','e'),('ì','i'),('ò','o'),('ù','u'),('v','u'),('j','i'),('y','i'),('k','c'),('w','u'),('x','s')):
        s=s.replace(a,b)
    return re.sub(r'[^abcdefghilmnopqrstuz]','',s)
txt=''
d=open('scans/corpus/ariosto.txt',encoding='utf8').read()
# the letters: drop Gutenberg frame
s=d.find('LETTERA'); e=d.rfind('*** END'); txt+=d[s:e]
for f in glob.glob('../1567/decryption_*.txt')+glob.glob('../1567/reading_*.md'):
    txt+=open(f,encoding='utf8').read()
c=norm(txt); print('corpus',len(c))
N=20
Q=np.ones((N,N,N,N),dtype=np.float32)*0.05
for i in range(len(c)-3):
    Q[idx[c[i]],idx[c[i+1]],idx[c[i+2]],idx[c[i+3]]]+=1
Q=np.log(Q/Q.sum())
np.save('scans/corpus/q4.npy',Q)
ct=open(sys.argv[1]).read().strip() if len(sys.argv)>1 else open('work/all.txt').read().strip()
ct=ct.replace('3','B')
signs=sorted(set(ct)); si={s:i for i,s in enumerate(signs)}
C=np.array([si[x] for x in ct])
print(len(signs),signs)
freq=collections.Counter(c)
ord_letters=[x for x,_ in freq.most_common()]
def score(key):
    P=key[C]; return Q[P[:-3],P[1:-2],P[2:-1],P[3:]].sum()
best=None
rng=random.Random(1566)
for rs in range(int(sys.argv[2]) if len(sys.argv)>2 else 30):
    # start: frequency order + noise
    order=[s for s,_ in collections.Counter(ct).most_common()]
    key=np.zeros(len(signs),dtype=int)
    letters=ord_letters[:]; rng.shuffle(letters)
    for i,s in enumerate(order): key[si[s]]=idx[letters[i%N]]
    cur=score(key); T=30.0
    for it in range(60000):
        k=rng.randrange(len(signs)); old=key[k]
        if rng.random()<0.5:
            k2=rng.randrange(len(signs)); key[k],key[k2]=key[k2],key[k]
            ns=score(key)
            if ns>cur or rng.random()<math.exp((ns-cur)/T): cur=ns
            else: key[k],key[k2]=key[k2],key[k]
        else:
            key[k]=rng.randrange(N); ns=score(key)
            if ns>cur or rng.random()<math.exp((ns-cur)/T): cur=ns
            else: key[k]=old
        T=max(0.3,T*0.99985)
    pt=''.join(A[key[x]] for x in C)
    print(rs,round(cur),pt[:110],flush=True)
    if best is None or cur>best[0]: best=(cur,key.copy(),pt)
print(best[0]); print({signs[i]:A[best[1][i]] for i in range(len(signs))})
print(best[2])
json.dump({signs[i]:A[best[1][i]] for i in range(len(signs))},open('work/key_auto.json','w'))
