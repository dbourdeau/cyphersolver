"""Monoalphabetic anneal on a token stream: part 'S' (second pair), 'F' (first pair) or 'G' (whole group). Tries Russian and German."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import sys,random,math,re,collections
import numpy as np
sys.stdout.reconfigure(encoding='utf-8')
HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,os.path.join(HERE,'..','..'))
from lang import lm
A='абвгдежзийклмнопрстуфхцчшщыьэюя'
T=re.sub('[^'+A+']','',open(os.path.join(HERE,'ru_corpus.txt'),encoding='utf-8').read().lower().replace('ё','е').replace('ъ','ь'))
part=sys.argv[1];files=sys.argv[2].split(',');s0,s1,it=int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]);ctrl=len(sys.argv)>6 and sys.argv[6]=='shuffle'
LM=lm.DenseLM.build(T,3,A)
G=[g for f in files for g in open(os.path.join(HERE,f)).read().split() if '?' not in g]
tk=[{'S':g[2:],'F':g[:2],'G':g}[part] for g in G]
if ctrl: random.seed(7);random.shuffle(tk)
sy=[k for k,_ in collections.Counter(tk).most_common()]
ix={k:i for i,k in enumerate(sy)};x0=np.array([ix[t] for t in tk])
print(len(tk),len(sy),flush=True)
N=len(A)
fr=collections.Counter(T);byf=[A.index(c) for c,_ in fr.most_common()]
def run(seed):
    random.seed(seed)
    p=(byf+byf[:12]+byf[:12])[:len(sy)]
    p=np.array(p);spare=[c for c in range(N) if c not in set(p.tolist())]
    for _ in range(40):
        a,b=random.randrange(len(p)),random.randrange(len(p));p[a],p[b]=p[b],p[a]
    cur=LM.score_idx(p[x0])/len(x0);best=(cur,p.copy())
    t0,t1=.08,.002
    for i in range(it):
        t=t0*(t1/t0)**(i/it)
        a=random.randrange(len(p))
        b=random.randrange(len(p));p[a],p[b]=p[b],p[a];undo=(a,b,None)
        c=LM.score_idx(p[x0])/len(x0)
        if c>=cur or random.random()<math.exp((c-cur)/t): cur=c
        else:
            if undo[1] is not None: p[a],p[undo[1]]=p[undo[1]],p[a]
            else: p[a]=undo[2]
        if cur>best[0]: best=(cur,p.copy())
    return best
for s in range(s0,s1):
    b=run(s);print(s,round(b[0],3),''.join(A[i] for i in b[1][x0])[:240],flush=True)
    print('  ',' '.join(f'{sy[i]}={A[b[1][i]]}' for i in range(min(len(sy),36))),flush=True)
