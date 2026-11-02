"""Model-free: within a message, the digitwise difference d between odd and even columns that produces most coincidences.
A key of period 2 predicts one d far above the rest. Also lag-coincidence by lag parity."""
import json,sys,collections,re,random
sys.stdout.reconfigure(encoding='utf-8')
M=[json.loads(l) for l in open('messages_ocr.jsonl',encoding='utf-8')]
def sub(a,b): return ''.join(str((int(x)-int(y))%10) for x,y in zip(a,b))
seen=set()
for m in M:
    g=[x for x in m['groups'] if len(x)==4 and x.isdigit()]
    if g and g[0]=='1921': g=g[1:]
    if m['len']!=4 or len(g)<90 or tuple(g[:10]) in seen or re.search('AUSSENAMT|OESTER|RADIO|GAMOT',m['head']): continue
    seen.add(tuple(g[:10]))
    a=collections.Counter(g[0::2]);b=collections.Counter(g[1::2]);d=collections.Counter()
    for x,u in a.items():
        for y,v in b.items(): d[sub(x,y)]+=u*v
    top=d.most_common(3)
    # same-column vs cross-column exact coincidence rate
    same=sum(v*(v-1)//2 for v in a.values())+sum(v*(v-1)//2 for v in b.values());cross=sum(a[x]*b[x] for x in a)
    ns=len(g[0::2])*(len(g[0::2])-1)//2+len(g[1::2])*(len(g[1::2])-1)//2;nc=len(g[0::2])*len(g[1::2])
    print(m['file'][5:-4],len(g),'same %.4f cross %.4f'%(same/ns,cross/nc),top,' '.join(re.findall(r'[A-Za-z]{3,}',m['head'])[-2:]))
