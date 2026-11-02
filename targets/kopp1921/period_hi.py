"""Period search on the first pair only: per column choose the hi-key (digitwise) maximising LL under the plain code's first-pair distribution."""
import json,sys,collections,math,random,re
import numpy as np
sys.stdout.reconfigure(encoding='utf-8')
P=[g for f in ('lutowinoff417_ct.txt','kopp0876_ct.txt','kopp0877_ct.txt') for g in open(f).read().split() if '?' not in g]
c=collections.Counter(g[:2] for g in P);n=len(P)
L=np.log(np.array([(c[f'{i:02d}']+.3)/(n+30) for i in range(100)]))
S=np.zeros((100,100),dtype=int)
for k in range(100):
    for v in range(100):
        S[k,v]=((v//10-k//10)%10)*10+(v%10-k%10)%10
def score(h,p):
    tot=0
    for col in range(p):
        x=np.array(h[col::p])
        tot+=L[S[:,x]].sum(1).max()
    return tot/len(h)
M=[json.loads(l) for l in open('messages_ocr.jsonl',encoding='utf-8')]
seen=set()
for m in M:
    g=[x for x in m['groups'] if len(x)==4 and x.isdigit()]
    if m['len']!=4 or len(g)<70 or tuple(g[:10]) in seen or re.search('AUSSENAMT|OESTER|RADIO|GAMOT',m['head']): continue
    seen.add(tuple(g[:10]))
    h=[int(x[:2]) for x in g]
    ps=range(1,41)
    r=[score(h,p) for p in ps]
    # null by shuffling, per p
    random.seed(1);nul=np.zeros((12,len(r)))
    for t in range(12):
        e=h[:];random.shuffle(e)
        nul[t]=[score(e,p) for p in ps]
    z=(np.array(r)-nul.mean(0))/nul.std(0).clip(1e-3)
    top=np.argsort(-z)[:5]
    print(m['file'][5:-4],len(g),' '.join(re.findall(r'[A-Za-z]{3,}',m['head'])[-2:]),[(int(ps[i]),round(float(z[i]),1)) for i in top],flush=True)
