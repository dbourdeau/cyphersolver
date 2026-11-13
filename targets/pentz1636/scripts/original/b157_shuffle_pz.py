# shuffle_pz.py tx key keymd5 n seed : guarded German 4-gram baseline (corpus b6b9/lm/pg55171.txt, md5 + 'Language: German' + body asserted).
# Runs = maximal sequences of figures mapped by T1, split at codes/unmapped/struck groups (dividers ignored). Shuffle = permutation of decoded letters among distinct figure types.
import sys,re,math,random,hashlib,collections
tx,kf,km,N,seed=sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4]),int(sys.argv[5])
assert hashlib.md5(open(tx,'rb').read()).hexdigest()=='1e70795fd31a4ee8c1c30dce00354226'
assert hashlib.md5(open(kf,'rb').read()).hexdigest()==km
ns={}; exec(open(kf).read(),ns); T1=ns['T1']
CF='/home/claude/en/trackB/b6b9/lm/pg55171.txt'; raw=open(CF,'rb').read()
assert hashlib.md5(raw).hexdigest()=='f476bb7446c9c38f858a455d5c91602d','corpus md5'
txt=raw.decode('utf-8','replace'); assert re.search(r'^Language: German',txt,re.M),'not German'
a=txt.find('*** START'); b=txt.find('*** END'); assert a>0 and b>a+100000
def norm(s): s=s.lower().replace('ß','ss').replace('ä','a').replace('ö','o').replace('ü','u').replace('ſ','s'); return re.sub('[^a-z]','',s).replace('v','u').replace('j','i')
body=norm(txt[a:b]); Q=collections.Counter(body[i:i+4] for i in range(len(body)-3)); tot=sum(Q.values()); fl=math.log10(0.01/tot); LP={k:math.log10(v/tot) for k,v in Q.items()}
runs=[];cur=[]
for l in open(tx):
    if not l.startswith('L'): continue
    for t in l.split('|')[1].split():
        if t in '.,': continue
        if t.startswith('{'): 
            if cur: runs.append(cur); cur=[]
            continue
        n=int(t.rstrip('?'))
        if n in T1: cur.append(n)
        else:
            if cur: runs.append(cur); cur=[]
if cur: runs.append(cur)
types=sorted({x for r in runs for x in r}); base={k:T1[k] for k in types}
def score(m):
    sc=0;n=0
    for r in runs:
        s=''.join(m[x] for x in r)
        for i in range(len(s)-3): sc+=LP.get(s[i:i+4],fl); n+=1
    return sc/n
true=score(base); rnd=random.Random(seed); vals=[base[k] for k in types]; X=[]
for i in range(N):
    v=vals[:]; rnd.shuffle(v); X.append(score(dict(zip(types,v))))
X.sort()
print(f'corpus pg55171 {len(body)} letters; runs {len(runs)}; figures {sum(map(len,runs))}; types {len(types)}; seed {seed}')
print(f'true {true:.4f}; shuffles {N}; >= true {sum(x>=true for x in X)}; best {X[-1]:.4f}; median {X[N//2]:.4f}')
