"""Pool aligned dinomes by discriminant word: last word(s) before the groups. Is the table shared?"""
import json,re,collections,sys
sys.stdout.reconfigure(encoding='utf-8')
M=[json.loads(l) for l in open('targets/kopp1921/messages_ocr.jsonl',encoding='utf-8')]
def ic(c):
    n=sum(c.values());return sum(v*(v-1) for v in c.values())/(n*(n-1))*100 if n>1 else 0
P=collections.defaultdict(list);seen=set()
for m in M:
    L=m['len'];g=[x for x in m['groups'] if len(x)==L]
    if len(g)<12 or tuple(g[:10]) in seen: continue
    seen.add(tuple(g[:10]))
    w=re.findall(r'[A-Za-z]{3,}',m['head'])
    d=(m['disc'] or (w[-1].upper() if w else '-'))
    P[(d,L)].append(g)
rows=[]
for (d,L),ms in P.items():
    gs=[x for g in ms for x in g]
    if len(gs)<80: continue
    c=collections.Counter()
    per=[]
    for g in ms:
        s=''.join(g);ci=collections.Counter(s[i:i+2] for i in range(0,len(s)-1,2));c.update(ci);
        if len(s)>120: per.append(round(ic(ci),1))
    rows.append((round(ic(c),2),d,L,len(ms),len(gs),per[:10],' '.join(k for k,_ in c.most_common(14))))
for r in sorted(rows,reverse=True)[:60]: print(r)
