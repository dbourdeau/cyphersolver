"""Exploratory homophonic substitution; provisional glyph transcription."""
import sys,re,json,random,math,time
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
from lang import lm
root=Path(__file__).parent
M=lm.load('es-golden-age',order=5,spaces=False)
raw=(root/'cipher_draft.txt').read_text()
if '--split' in sys.argv:
 raw=raw.replace('bar8 n L','e D bar8 n L').replace('k l L e Yd L three','k l L e Yd J three')
 for a,b in [('dc','c d'),('lb','l b'),('B','l three')]:raw=re.sub(r'\b'+a+r'\b',b,raw)
if '--dots' in sys.argv:
 for a,b in [('Hd','H'),('rd','r'),('ad','a'),('ud','u'),('Yd','Y')]:raw=re.sub(r'\b'+a+r'\b',b,raw)
if '--crib' in sys.argv:raw=raw.replace('k l L e Yd L three','k l L e Yd J three')
parts=re.split(r'(\[[^\]]*\])',raw)
syms=sorted(set(t for p in parts if not p.startswith('[') for t in p.split()))
items=[]
for p in parts:
 if p.startswith('['):items.extend(-(M.index[c]+1) for c in lm.norm(p[1:-1],'early',spaces=False))
 else:items.extend(syms.index(t) for t in p.split())
items=np.array(items); mask=items>=0; pos=items[mask]; fixed=-items-1
def render(key):
 x=fixed.copy();x[mask]=key[pos];return x
def score(key):
 x=render(key);q=x[:-4].copy()
 for i in range(1,5):q=q*M.A+x[i:len(x)-4+i]
 counts=np.bincount(key,minlength=M.A)
 caps=np.array([3 if c in 'aeiou' else 1 for c in M.alpha])
 penalty=30*np.maximum(counts-caps,0).sum()
 return float(M.lp[q].sum())-penalty
def show(key):
 return '\n'.join(p if p.startswith('[') else ' '.join(M.alpha[key[syms.index(t)]] for t in p.split()) for p in parts)
best=-1e99
crib={'o':'p','a':'r','l':'o','k':'n','L':'s','e':'t','Yd':'i','J':'c','three':'o','r':'e'} if '--crib' in sys.argv else {}
if '--en' in sys.argv:crib={'e':'e','D':'n'}
fixedkey={syms.index(s):M.index[c] for s,c in crib.items()}
random.seed(1596)
for run in range(int(sys.argv[1]) if len(sys.argv)>1 else 40):
 key=np.array([M.index[random.choice('aeiosnrltudcmpbghqfyzx')] for _ in syms]);cur=score(key)
 for si,ci in fixedkey.items():key[si]=ci
 cur=score(key)
 for it in range(30000):
  a=random.randrange(len(syms));b=random.randrange(len(syms));old=key.copy()
  if random.random()<0.5:key[a],key[b]=key[b],key[a]
  else:key[a]=random.randrange(M.A)
  for si,ci in fixedkey.items():key[si]=ci
  s=score(key)
  temp=3.0*(0.08/3.0)**(it/30000)
  if s>=cur or random.random()<math.exp(max(-700,(s-cur)/temp)):cur=s
  else:key=old
 if cur>best:
  best=cur;out={'score':best,'key':dict(zip(syms,[M.alpha[i] for i in key])),'reading':show(key)}
  (root/('solver_'+('_'.join(sys.argv[2:]).replace('--','') or 'base')+'_best.json')).write_text(json.dumps(out,indent=2));print(run,best,show(key),flush=True)
