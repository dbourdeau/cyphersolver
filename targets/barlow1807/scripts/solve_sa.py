import sys,re,math,random,collections,glob
sys.path.insert(0,'scripts'); from parse import words
corp=open('corpus/federalist.txt',encoding='utf8').read().lower()
corp=re.sub(r'[^a-z]+',' ',corp)
N=4; cnt=collections.Counter(corp[i:i+N] for i in range(len(corp)-N))
tot=sum(cnt.values()); floor=math.log(0.01/tot)
LP={k:math.log(v/tot) for k,v in cnt.items()}
pages=sys.argv[1].split(','); seed=int(sys.argv[2]) if len(sys.argv)>2 else 1
cw=[]
for p in pages:
    for k,v in words(open(f'trans_raw/p{p}_A.txt',encoding='utf8').read()):
        if k=='C':
            v=[t for t in v if t and len(t)<=3]
            if v: cw.append(v)
syms=sorted({t for w in cw for t in w})
random.seed(seed)
L='abcdefghijklmnopqrstuvwxyz'
freq='eeeeeeettttttaaaaaoooooiiiiinnnnnsssssrrrrhhhhlllddducccmmwwffggyyppbbvvkjxqz'
key={s:random.choice(freq) for s in syms}
def score(key):
    s=0
    for w in cw:
        t=' '+''.join(key[x] for x in w)+' '
        for i in range(len(t)-N+1): s+=LP.get(t[i:i+N],floor)
    return s
cur=score(key); best=(cur,dict(key)); T=10.0
for it in range(60000):
    s=random.choice(syms); old=key[s]; key[s]=random.choice(L)
    new=score(key)
    if new>cur or random.random()<math.exp((new-cur)/T): cur=new
    else: key[s]=old
    T=max(0.2,T*0.99993)
    if cur>best[0]: best=(cur,dict(key))
key=best[1]
print(best[0])
print(' '.join(''.join(key[x] for x in w) for w in cw[:120]))
print(' '.join(f'{s}={key[s]}' for s in syms))
