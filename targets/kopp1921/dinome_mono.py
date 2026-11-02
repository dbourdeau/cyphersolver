"""Dinome-rich 5-figure runs: contact test (survives only if dinomes are NOT transposed) and a swap anneal to Russian."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import sys,json,re,random,math,collections
import numpy as np
sys.stdout.reconfigure(encoding='utf-8')
HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,os.path.join(HERE,'..','..'))
from lang import lm
A='абвгдежзийклмнопрстуфхцчшщыьэюя'
T=re.sub('[^'+A+']','',open(os.path.join(HERE,'ru_corpus.txt'),encoding='utf-8').read().lower().replace('ё','е').replace('ъ','ь'))
LM=lm.DenseLM.build(T,3,A);byf=[A.index(c) for c,_ in collections.Counter(T).most_common()]
M=[json.loads(l) for l in open(os.path.join(HERE,'messages_ocr.jsonl'),encoding='utf-8')]
def mi(p):
    n=len(p);a=collections.Counter(x for x,_ in p);b=collections.Counter(y for _,y in p);j=collections.Counter(p)
    return sum(v/n*math.log2(v*n/(a[x]*b[y])) for (x,y),v in j.items())
def ic(c):
    n=sum(c.values());return sum(v*(v-1) for v in c.values())/(n*(n-1))*100
seen=set();rows=[]
for m in M:
    L=m['len'];g=[x for x in m['groups'] if len(x)==L]
    if L!=5 or len(g)<60 or tuple(g[:10]) in seen: continue
    seen.add(tuple(g[:10]));s=''.join(g)
    for off in (0,1):
        d=[s[i:i+2] for i in range(off,len(s)-1,2)]
        c=collections.Counter(d)
        if ic(c)<2.0: continue
        r=mi(list(zip(d,d[1:])));N=[]
        for t in range(60):
            e=d[:];random.shuffle(e);N.append(mi(list(zip(e,e[1:]))))
        mu=sum(N)/60;sd=(sum((x-mu)**2 for x in N)/60)**.5
        rows.append(((r-mu)/sd,round(ic(c),2),len(d),off,m['file'][5:-4],' '.join(re.findall(r'[A-Za-z]{3,}',m['head'])[-3:]),d))
rows.sort(key=lambda r:-r[0])
for r in rows[:30]: print(round(r[0],1),r[1:6])
for r in rows[:6]:
    d=r[6];sy=[k for k,_ in collections.Counter(d).most_common()];ix={k:i for i,k in enumerate(sy)};x=np.array([ix[t] for t in d])
    bestall=(-99,None)
    for seed in range(2):
        random.seed(seed);p=np.array((byf*5)[:len(sy)]);cur=LM.score_idx(p[x])/len(x);it=25000
        for i in range(it):
            tt=.08*(.002/.08)**(i/it);a,b=random.randrange(len(p)),random.randrange(len(p));p[a],p[b]=p[b],p[a];c=LM.score_idx(p[x])/len(x)
            if c>=cur or random.random()<math.exp((c-cur)/tt): cur=c
            else: p[a],p[b]=p[b],p[a]
        if cur>bestall[0]: bestall=(cur,''.join(A[i] for i in p[x]))
    print(r[4],r[5],round(bestall[0],2),bestall[1][:150],flush=True)
