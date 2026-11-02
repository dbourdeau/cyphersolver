import json,csv,re,random,difflib,glob,collections
K={int(e['code']):(e['historical_reading'] or '') for e in json.load(open('sources/raw/historical1385_review_2026-10-27/historical1385_reference.json'))['entries']}
norm=lambda s:re.sub(r'[^a-z0-9]','',(s or '').lower())
mp=lambda m:100*(15-(m-1)//100)+(m-100*((m-1)//100))
d={}
for f in sorted(glob.glob('sources/raw/morris_duplicate_collation_2026-10-23/morris_frame7[789]_P_spans_v2.csv')):
    for r in csv.DictReader(open(f)):
        tk=[int(x) for x in re.findall(r'\d+',r['tokens'])]
        if tk and all(1<=x<=1600 for x in tk) and r['tier'].strip()=='P' and not re.search(r'\d',r['plaintext']):d.setdefault((tuple(tk),norm(r['plaintext'])),[]).append(r['id'])
sp=list(d);print('distinct (tokens,plaintext)',len(sp),'distinct groups',len({x for t,_ in sp for x in t}))
def sc(fn):
    e=f=0
    for t,p in sp:
        g=''.join(norm(K.get(fn(x),'')) for x in t);e+=g==p;f+=difflib.SequenceMatcher(None,g,p).ratio()>=.75
    return e,f
print('reversed',sc(mp),'identity',sc(lambda x:x))
random.seed(11);ee=[];ff=[]
for _ in range(1000):
    pm=list(range(16));random.shuffle(pm);a,b=sc(lambda m:100*pm[(m-1)//100]+m-100*((m-1)//100));ee.append(a);ff.append(b)
print('random 1000 exact max/mean',max(ee),sum(ee)/1000,'fuzzy max/mean',max(ff),sum(ff)/1000)
# per-block, distinct, excluding function words: multi-group or long words
per=collections.defaultdict(lambda:[0,0])
for t,p in sp:
    g=''.join(norm(K.get(mp(x),'')) for x in t);ok=g==p
    for x in set(t):
        per[(x-1)//100][1]+=1;per[(x-1)//100][0]+=ok
print('distinct-span block support exact',{100*b+1:tuple(per[b]) for b in sorted(per)})
long=[(t,p) for t,p in sp if len(t)>=3 and ''.join(norm(K.get(mp(x),'')) for x in t)==p]
print('exact multi-group examples',[(list(t),p,[K[mp(x)] for x in t],d[(t,p)][0]) for t,p in long[:12]])
single=[(t[0],p,K[mp(t[0])],d[(t,p)][0]) for t,p in sp if len(t)==1 and norm(K[mp(t[0])])==p]
print('singles',[x for x in single if x[0] in (285,76,1069,126,970,670,101,476,490)])
print('misses',[(list(t),p,[K[mp(x)] for x in t]) for t,p in sp if difflib.SequenceMatcher(None,''.join(norm(K.get(mp(x),'')) for x in t),p).ratio()<.75])
