"""4-figure system: is there a per-message digit shift? Group-level match rates under the best shift for message pairs,
and repeat-lag (period) profile inside messages."""
import json,re,collections,sys,itertools
sys.stdout.reconfigure(encoding='utf-8')
M=[json.loads(l) for l in open('targets/kopp1921/messages_ocr.jsonl',encoding='utf-8')]
F=[m for m in M if m['len']==4 and m['n']>=50 and 'AUSSENAMT' not in m['head'] and 'OESTER' not in m['head'] and 'RADIO' not in m['head']]
def gs(m): return [g for g in m['groups'] if len(g)==4]
def sub(g,k): return ''.join(str((int(a)-int(b))%10) for a,b in zip(g,k))
S=[collections.Counter(gs(m)) for m in F]
print(len(F))
# best shift between pairs
res=[]
for i,j in itertools.combinations(range(len(F)),2):
    d=collections.Counter()
    for a,va in S[i].items():
        for b,vb in S[j].items():
            d[sub(a,b)]+=va*vb
    k,v=d.most_common(1)[0]
    n=min(sum(S[i].values()),sum(S[j].values()))
    res.append((v/n,v,k,F[i]['file'][5:-4],F[j]['file'][5:-4],len(gs(F[i])),len(gs(F[j])), d.most_common(2)[1][1]))
res.sort(reverse=True)
for r in res[:30]: print(r)
# lag profile
for m in sorted(F,key=lambda m:-m['n'])[:12]:
    g=gs(m);out=[]
    for lag in range(1,31):
        eq=sum(a[0]==b[0] for a,b in zip(g,g[lag:]))/(len(g)-lag)
        out.append(round(eq*100))
    print(m['file'][5:-4],len(g),out)
