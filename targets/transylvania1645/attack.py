"""Reproducible monoalphabetic probe, using the shared Hungarian model.
Extract is provisional; clear words omitted and line breaks not word divisions.
"""
import sys, pathlib, json, re, random, math, time
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent.parent))
from lang import lm
root=pathlib.Path(__file__).resolve().parent
order=int(sys.argv[2]) if len(sys.argv)>2 else 4
m=lm.load('hu-modern',order=order,spaces=False)
stem=sys.argv[1] if len(sys.argv)>1 else 'R4936-p1-extract'
raw=(root/(stem+'.txt')).read_text()
ct=''.join(re.findall('[a-z]',raw))
alphabet='abcdefghijklmnopqrstuvwxyz'
x=np.array([alphabet.index(c) for c in ct])
windows=np.lib.stride_tricks.sliding_window_view(x,order)
weights=np.array([26**i for i in range(order-1,-1,-1)])
def score(key): return float(m.lp[key[windows]@weights].sum())
random.seed(4936)
best=-1e99
for restart in range(50):
 key=np.arange(26); random.shuffle(key)
 s=score(key)
 for it in range(12000):
  a,b=random.sample(range(26),2)
  key[a],key[b]=key[b],key[a]
  ns=score(key); temp= max(.25,8*(1-(it%3000)/3000))
  if ns>s or random.random()<math.exp(max(-700,(ns-s)/temp)): s=ns
  else: key[a],key[b]=key[b],key[a]
  if s>best:
   best=s; bk=key.copy()
 if restart%1==0:
  trans={c:alphabet[bk[i]] for i,c in enumerate(alphabet)}
  result={'score':best,'key':trans,'reading':raw.translate(str.maketrans(trans)),'restart':restart}
  (root/(stem+f'-{order}gram-result.json')).write_text(json.dumps(result,indent=2))
  if restart in (0,2,9,49): print(restart,round(best,2),result['reading'][:220],flush=True)
