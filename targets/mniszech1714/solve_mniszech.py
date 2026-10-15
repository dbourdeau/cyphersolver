"""Exploratory French substitution annealer; trial.txt is deliberately provisional."""
import sys,re,json,random,math,pathlib
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent.parent))
from lang import lm
p=pathlib.Path(__file__).parent
m=lm.load('pl-modern',order=5,spaces=False)
symbols=[]; lines=[]
for line in [(p/'r7524-cipher.txt').read_text().replace('\n',' ')]:
 if line.startswith('#'): continue
 row=[]
 for t in re.findall(r'\[[^]]*\]|\d+',line):
  if t.startswith('['):row.extend(-m.index[c]-1 for c in lm.norm(t,spaces=False))
  else:
   n=int(t)
   if n not in symbols:symbols.append(n)
   row.append(symbols.index(n))
 lines.append(row)
grams=np.array([r[i:i+5] for r in lines for i in range(len(r)-4)],dtype=int)
fixed=np.where(grams<0,-grams-1,0);mask=grams>=0;g=np.maximum(grams,0)
def score(k):
 q=np.where(mask,k[g],fixed)
 ix=(((q[:,0]*m.A+q[:,1])*m.A+q[:,2])*m.A+q[:,3])*m.A+q[:,4]
 return m.lp.ravel()[ix].sum()
def render(k):
 return '\n'.join(''.join(m.alpha[k[x]] if x>=0 else m.alpha[-x-1].upper() for x in r) for r in lines)
best=-1e20;rng=random.Random(18)
for run in range(200):
 k=np.array([rng.randrange(m.A) for _ in symbols]);cur=score(k)
 for it in range(50000):
  a=rng.randrange(len(k));old=k[a];k[a]=rng.randrange(m.A)
  sc=score(k);T=5*(.04/5)**(it/50000)
  if sc>cur or rng.random()<math.exp(min(0,(sc-cur)/T)):cur=sc
  else:k[a]=old
  if cur>best:
   best=cur;bk=k.copy()
 print(run,round(float(best),2),flush=True)
 (p/'r7524-result.txt').write_text(render(bk)+'\n'+json.dumps(dict(zip(map(str,symbols),[m.alpha[x] for x in bk]))),encoding='utf8')
