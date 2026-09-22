import sys,random,math
sys.path.insert(0,'.')
from lang import lm
t=open('r7707/ct.txt').read().split()
syms=sorted(set(t)); x=[syms.index(s) for s in t]; n=len(syms)
AL='abcdefghijklmnopqrstuvwxyz'
lang=sys.argv[1]; P=int(sys.argv[2]); mode=sys.argv[4]
m=lm.load(lang,order=4,spaces=False)
def dec(perm,k):
  o=[]
  for i,v in enumerate(x):
    p=perm[v]
    if p>=26: continue
    o.append(AL[(p+k[i%P])%26] if mode=='v' else AL[(k[i%P]-p)%26])
  return ''.join(o)
def sc(perm,k):
  d=dec(perm,k); return m.score(d)-6*(len(x)-len(d))
best=-1e9
for r in range(int(sys.argv[3])):
  perm=list(range(n)); random.shuffle(perm); k=[random.randrange(26) for _ in range(P)]
  cur=sc(perm,k); T=4
  for it in range(50000):
    if random.random()<0.75:
      a,b=random.sample(range(n),2); perm[a],perm[b]=perm[b],perm[a]; s=sc(perm,k)
      if s>cur or random.random()<math.exp((s-cur)/T): cur=s
      else: perm[a],perm[b]=perm[b],perm[a]
    else:
      j=random.randrange(P); o=k[j]; k[j]=random.randrange(26); s=sc(perm,k)
      if s>cur or random.random()<math.exp((s-cur)/T): cur=s
      else: k[j]=o
    T=max(0.1,T*0.99985)
  if cur>best: best=cur; print(lang,P,mode,r,round(cur/len(x),2),dec(perm,k),flush=True)
