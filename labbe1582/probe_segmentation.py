import sys,json,re,itertools,random,math,time
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from lang import lm
root=Path(__file__).parent
m=lm.load('fr-1600-letters',order=4,spaces=False)
runs=json.loads((root/'probe_input_initial.json').read_text(encoding='utf-8'))
rng=np.random.default_rng(1577)
results=[]
for mask in range(1,64):
 prefixes={str(i) for i in range(6) if mask>>i&1}
 seqs=[];bad=0
 for r in runs:
  s=re.sub(r'\D','',r['digits']); seq=[];i=0
  while i<len(s):
   if s[i] in prefixes:
    if i+1==len(s):bad+=1
    seq.append(s[i:i+2]);i+=2
   else:seq.append(s[i]);i+=1
  seqs.append(seq)
 vocab=sorted(set(sum(seqs,[])));n=len(vocab)
 if not 17<=n<=65:continue
 lookup={s:i for i,s in enumerate(vocab)}
 grams=np.array([[lookup[t] for t in s[i:i+4]] for s in seqs for i in range(len(s)-3)])
 positions=[np.where((grams==i).any(axis=1))[0] for i in range(n)]
 best=-1e9; bk=None
 for restart in range(3):
  key=rng.integers(m.A,size=n);x=key[grams];inds=((x[:,0]*m.A+x[:,1])*m.A+x[:,2])*m.A+x[:,3];vals=m.lp[inds];score=vals.sum()
  for it in range(6000):
   t=int(rng.integers(n));old=key[t];new=int(rng.integers(m.A));key[t]=new;p=positions[t];x=key[grams[p]];iv=((x[:,0]*m.A+x[:,1])*m.A+x[:,2])*m.A+x[:,3];nv=m.lp[iv];delta=float(nv.sum()-vals[p].sum());temp=2*(1-it/6000)+.15
   if delta>=0 or rng.random()<math.exp(max(-700,delta/temp)):
    vals[p]=nv;score+=delta
    if score>best:best=score;bk=key.copy()
   else:key[t]=old
 dec=[''.join(m.alpha[bk[lookup[t]]] for t in s) for s in seqs]
 res={'prefixes':''.join(sorted(prefixes)),'score':float(best/len(grams)),'bad':bad,'symbols':n,'text':dec,'key':{t:m.alpha[bk[i]] for i,t in enumerate(vocab)}};results.append(res)
 print(json.dumps({k:res[k] for k in ['prefixes','score','bad','symbols','text']}),flush=True)
 (root/'segmentation_results.json').write_text(json.dumps(sorted(results,key=lambda r:r['score'],reverse=True),indent=2))
