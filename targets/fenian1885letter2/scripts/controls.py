import gzip,json,random,hashlib,sys
lexp='/home/claude/keyless/_cs/lang/lexicons/en.json.gz'
raw=gzip.open(lexp).read(); print('lexicon sha256',hashlib.sha256(raw).hexdigest())
lex=json.loads(raw); lex=set(w.upper() for w in (lex if isinstance(lex,list) else lex.keys()))
print('lexicon words',len(lex))
words=[[85,68,85,69,84],[73,65,68,62,80],[73,65,62,82,81],[70,65,64,81],[65,71,68]]  # test units fixed before running
codes=list(range(60,86)); A=[chr(65+i) for i in range(26)]
real={60+((i+16)%26):chr(64+i) for i in range(1,27)}
def score(k,ws=words): return sum(''.join(k[c] for c in w) in lex for w in ws)
print('real key:',score(real),'of',len(words),[''.join(real[c] for c in w) for w in words])
sh=[]
for s in range(26):
    k={c:A[(i+s)%26] for i,c in enumerate(codes)}; sh.append(score(k))
print('26 shifts scores:',sh,'max other than real:',sorted(sh)[-2])
for seed in (20261112,7):
    r=random.Random(seed); dist=[]
    for _ in range(5000):
        p=A[:]; r.shuffle(p); dist.append(score(dict(zip(codes,p))))
    print('seed',seed,'random keys >= real:',sum(d>=score(real) for d in dist),'/5000; >=3:',sum(d>=3 for d in dist),'; max',max(dist))
    flat=[c for w in words for c in w]; ge=0; best=0
    for _ in range(5000):
        f=flat[:]; r.shuffle(f); it=iter(f); ws=[[next(it) for _ in w] for w in words]; sc=score(real,ws); best=max(best,sc); ge+= sc>=score(real)
    print('seed',seed,'shuffled ciphertext, real key, score>=real:',ge,'/5000; max',best)
