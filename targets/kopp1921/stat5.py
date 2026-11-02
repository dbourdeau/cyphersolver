"""4-figure messages: align the first two digits to a template by a per-message digit shift."""
import json,re,collections,sys,math
sys.stdout.reconfigure(encoding='utf-8')
M=[json.loads(l) for l in open('targets/kopp1921/messages_ocr.jsonl',encoding='utf-8')]
F=[];seen=set()
for m in M:
    g=[x for x in m['groups'] if len(x)==4]
    if m['len']==4 and len(g)>=45 and tuple(g[:12]) not in seen and not re.search('AUSSENAMT|OESTER|RADIO|GAMOT',m['head']):
        seen.add(tuple(g[:12]));F.append((m,g))
print(len(F))
ref=[x for m,g in F if m['file'].endswith('042-1265.jpg') or m['file'].endswith('M316-042-1265.jpg') for x in g]
def fp(gs,a,b):
    c=collections.Counter(x[a:b] for x in gs);n=sum(c.values())
    return {k:v/n for k,v in c.items()}
R=fp(ref,0,2)
rows=[]
for m,g in F:
    best=[]
    for s1 in range(10):
        for s2 in range(10):
            sc=0
            for k,v in fp(g,0,2).items():
                t=str((int(k[0])-s1)%10)+str((int(k[1])-s2)%10)
                sc+=v*R.get(t,0)
            best.append((round(sc*100,2),s1,s2))
    best.sort(reverse=True)
    rows.append((best[0],best[1][0],len(g),m['file'][5:-4],' '.join(re.findall(r'[A-Za-z]{3,}',m['head'])[-3:]),' '.join(k+':'+str(v) for k,v in collections.Counter(x[:2] for x in g).most_common(5))))
for r in sorted(rows,key=lambda r:r[3]): print(r)
