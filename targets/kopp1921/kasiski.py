"""Kasiski on whole groups inside each message: lag histogram of exact repeats, after dropping retransmitted duplicates."""
import json,re,collections,sys,math
sys.stdout.reconfigure(encoding='utf-8')
M=[json.loads(l) for l in open('targets/kopp1921/messages_ocr.jsonl',encoding='utf-8')]
seen=set();rows=[]
for m in M:
    L=m['len'];g=[x for x in m['groups'] if len(x)==L]
    if len(g)<40 or tuple(g[:15]) in seen: continue
    seen.add(tuple(g[:15]))
    pos=collections.defaultdict(list)
    for i,x in enumerate(g): pos[x].append(i)
    lags=[]
    for x,p in pos.items():
        for a in range(len(p)):
            for b in range(a+1,len(p)): lags.append(p[b]-p[a])
    if len(lags)<3: continue
    # score best period dividing most lags
    best=sorted(((sum(1 for d in lags if d%q==0)/len(lags),q) for q in range(2,61)),reverse=True,key=lambda t:(t[0]*t[1]**.5))[:3]
    rows.append((len(lags),len(g),L,m['file'][5:-4],m['disc'],' '.join(re.findall(r'[A-Za-z]{3,}',m['head'])[-3:]),[(round(a,2),q) for a,q in best],sorted(lags)[:14]))
rows.sort(key=lambda r:-r[0])
for r in rows[:50]: print(r)
