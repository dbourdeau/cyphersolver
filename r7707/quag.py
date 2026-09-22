import sys,random,math
sys.path.insert(0,'.')
from lang import lm
t=[s for s in open('r7707/ct.txt').read().split()]
syms=sorted(set(t)); x=[syms.index(s) for s in t]; n=len(syms)
AL='abcdefghijklmnopqrstuvwxyz'
lang=sys.argv[1]; P=int(sys.argv[2])
m=lm.load(lang,order=4,spaces=False)
def dec(perm,k): return ''.join(AL[(perm[v]+k[i%P])%26] for i,v in enumerate(x))
best=-1e9
for r in range(int(sys.argv[3])):
  perm=[random.randrange(26) for _ in range(n)]; k=[random.randrange(26) for _ in range(P)]
  cur=m.score(dec(perm,k)); T=4
  for it in range(40000):
    if random.random()<0.8:
      j=random.randrange(n); o=perm[j]; perm[j]=random.randrange(26); s=m.score(dec(perm,k))
      if s>cur or random.random()<math.exp((s-cur)/T): cur=s
      else: perm[j]=o
    else:
      j=random.randrange(P); o=k[j]; k[j]=random.randrange(26); s=m.score(dec(perm,k))
      if s>cur or random.random()<math.exp((s-cur)/T): cur=s
      else: k[j]=o
    T=max(0.1,T*0.9998)
  if cur>best: best=cur; print(lang,P,r,round(cur/len(x),2),dec(perm,k),flush=True)
