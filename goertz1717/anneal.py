import os,sys,re,random,math,json
import numpy as np
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
from lang import lm
M=lm.load(sys.argv[1] if len(sys.argv)>1 else 'de-modern',order=4,spaces=False)
AL=M.alpha if hasattr(M,'alpha') else None
t=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'transcription.txt'),encoding='utf8').read()
segs=[[]]
for l in t.splitlines():
    if l.startswith('#'): continue
    for w in l.split():
        if re.fullmatch(r'\d+',w): segs[-1].append(('c',w))
        elif w.startswith('['): 
            for ch in lm.norm(w.strip('[]'),'modern',spaces=False): segs[-1].append(('p',ch))
        else: segs.append([])   # ? or | breaks
segs=[s for s in segs if s]
codes=sorted({x for s in segs for k,x in s if k=='c'},key=int)
ci={c:i for i,c in enumerate(codes)}
alpha=M.alpha
L=len(alpha); print('alpha',alpha)
def build(key):
    out=[]
    for s in segs:
        out.append(np.array([key[ci[x]] if k=='c' else alpha.index(x) for k,x in s],dtype=np.int64))
    return out
def score(key): return sum(M.score_idx(a) for a in build(key))
# unigram prior for init
freq='eeeeeeennnnnnniiiiissssrrrrraaaaatttttddddhhhhuuullllcccgggmmoobbwwffkzp'
best=None
seed=int(sys.argv[2]) if len(sys.argv)>2 else 0
random.seed(seed)
for restart in range(int(sys.argv[3]) if len(sys.argv)>3 else 6):
    key=[alpha.index(random.choice(freq)) for _ in codes]
    cur=score(key); T=20.0
    for it in range(60000):
        i=random.randrange(len(codes)); old=key[i]; key[i]=random.randrange(L)
        s=score(key)
        if s>=cur or random.random()<math.exp((s-cur)/T): cur=s
        else: key[i]=old
        T=max(0.3,T*0.99993)
    n=sum(len(s) for s in segs)
    print(restart,round(cur/n,3),flush=True)
    if best is None or cur>best[0]: best=(cur,key[:])
key=best[1]
txt=[]
for s in segs: txt.append(''.join(alpha[key[ci[x]]] if k=='c' else x.upper() for k,x in s))
print('\n'.join(txt))
json.dump({c:alpha[key[ci[c]]] for c in codes},open(os.path.join(os.path.dirname(os.path.abspath(__file__)),f'key_{seed}.json'),'w'))
