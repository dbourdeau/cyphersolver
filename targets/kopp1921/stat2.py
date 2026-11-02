"""Per-message positional ICs: which messages show plain-code shape, which look like additive noise."""
import json,re,collections,sys
sys.stdout.reconfigure(encoding='utf-8')
M=[json.loads(l) for l in open('targets/kopp1921/messages_ocr.jsonl',encoding='utf-8')]
def ic(gs,i):
    c=collections.Counter(g[i] for g in gs);n=len(gs);return sum(v*(v-1) for v in c.values())/(n*(n-1))*10
rows=[]
for m in M:
    L=m['len'];gs=[g for g in m['groups'] if len(g)==L]
    if len(gs)<50: continue
    I=[ic(gs,i) for i in range(L)]
    rows.append((L,round(sum(I)/L,2),[round(x,2) for x in I],len(gs),m['file'][5:-4],m['disc'],' '.join(re.findall(r'[A-Za-z]{3,}',m['head'])[-4:]),' '.join(c for c,_ in collections.Counter(g[0] for g in gs).most_common(4))))
rows.sort(key=lambda r:(r[0],-r[1]))
print(len(rows))
for L in (4,5):
    R=[r for r in rows if r[0]==L]
    print('L',L,len(R))
    import statistics
    print(' mean IC dist',collections.Counter(round(r[1],1) for r in R).most_common())
    for r in R[:45 if L==5 else 70]: print(r[1:])
