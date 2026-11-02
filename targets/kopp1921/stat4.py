"""Period test on the digit stream of each long message: mean column IC for period p (digits), all systems."""
import json,re,collections,sys
sys.stdout.reconfigure(encoding='utf-8')
M=[json.loads(l) for l in open('targets/kopp1921/messages_ocr.jsonl',encoding='utf-8')]
def ic(s):
    c=collections.Counter(s);n=len(s)
    return sum(v*(v-1) for v in c.values())/(n*(n-1))*10 if n>1 else 0
out=[]
seen=set()
for m in M:
    L=m['len'];g=[x for x in m['groups'] if len(x)==L]
    if len(g)<60: continue
    t=tuple(g[:20])
    if t in seen: continue
    seen.add(t)
    s=''.join(g);base=ic(s)
    prof=[]
    for p in range(L,L*41,L):  # whole-group periods only
        cols=[s[i::p] for i in range(p)]
        v=sum(ic(c)*len(c) for c in cols if len(c)>1)/len(s)
        prof.append((round(v,2),p//L))
    top=sorted(prof,reverse=True)[:4]
    # expected noise of a column IC ~ sqrt(2*9/(N/p)^2... ) crude
    out.append((L,round(base,2),top,len(g),m['file'][5:-4],m['disc'],' '.join(re.findall(r'[A-Za-z]{3,}',m['head'])[-3:])))
out.sort(key=lambda r:(r[0],-r[2][0][0]))
for r in out:
    if r[0]==4: print(r)
print('---5')
for r in [x for x in out if x[0]==5][:45]: print(r)
