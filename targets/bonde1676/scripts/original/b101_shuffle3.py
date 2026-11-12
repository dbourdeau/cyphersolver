import sys,re,math,random,collections,unicodedata,glob
# shuffle.py key heldout seed : char 4-gram French model; only tier A/B/F/P values (all frozen v3 letter values) scored and shuffled; other tokens and clear words are breaks
def norm(t):
    t=unicodedata.normalize('NFD',t.lower()); t=''.join(c for c in t if unicodedata.category(c)!='Mn')
    return re.sub(r'[^a-z]+',' ',t)
txt=''
for f in sorted(glob.glob('/home/claude/en/trackB/b94_scan/dl/gut/pg*.txt')):
    raw=open(f,encoding='utf-8',errors='replace').read()
    assert re.search(r'^Language: French',raw,re.M), f
    a=raw.find('*** START'); b=raw.find('*** END'); txt+=norm(raw[a:b]).replace(' ','')+' '
N=4; cnt=collections.Counter(); ctx=collections.Counter()
for w in txt.split():
    for i in range(len(w)-N+1): cnt[w[i:i+N]]+=1; ctx[w[i:i+N-1]]+=1
def score(s):
    if len(s)<N: return 0.0,0
    t=0
    for i in range(len(s)-N+1): t+=math.log((cnt[s[i:i+N]]+0.01)/(ctx[s[i:i+N-1]]+0.26))
    return t,len(s)-N+1
key={}
for l in open(sys.argv[1],encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    g,s,t=l.rstrip('\n').split('\t')
    if t in 'ABFP': key[g]=norm(s).strip()
runs=[]
for l in open(sys.argv[2],encoding='utf-8'):
    m=re.match(r'R\d+:\s*(.*)',l)
    if not m: continue
    cur=[]
    for part in re.findall(r'"[^"]*"|\S+',m.group(1)):
        g=re.sub(r'[^0-9]','',part)
        if part.startswith('"') or part.endswith('~') or g not in key:
            if cur: runs.append(cur)
            cur=[]
        else: cur.append(g)
    if cur: runs.append(cur)
def total(k):
    t=0;n=0
    for r in runs:
        a,b=score(''.join(k[g] for g in r)); t+=a;n+=b
    return t/n
types=sorted({g for r in runs for g in r}); vals=[key[g] for g in types]
true=total(key); rnd=random.Random(int(sys.argv[3])); ge=0; res=[]
for i in range(5000):
    v=vals[:]; rnd.shuffle(v); s=total(dict(zip(types,v))); res.append(s); ge+=(s>=true)
res.sort()
print('runs',len(runs),'tokens',sum(len(r) for r in runs),'types',len(types),'true %.4f'%true,'shuffles>=true',ge,'of 5000','best %.4f'%res[-1],'median %.4f'%res[2500],'seed',sys.argv[3])
