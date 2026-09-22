import sys, random, math
sys.path.insert(0,'..')
from lang import lm
M=lm.load('de-1500s',order=5,spaces=True)
alpha=list('abcdefghiklmnoprstuwz')
FIX={'9':'u','0':'n','1':'d','6':'e','12':'r','W':'t','4':'h','7':'i','3':'g','F':'s'}
T=[]
for l in open('cipher_tokens.txt',encoding='utf8'):
  if l.startswith('L'): T+=[t for t in l.split(':',1)[1].split() if t!='?']+['/']
merge='pair' in sys.argv
if merge:
  U=[];i=0
  while i<len(T):
    if T[i]=='1' and i+1<len(T) and T[i+1]=='2': U.append('12');i+=2
    else: U.append(T[i]);i+=1
  T=U
syms=sorted(set(T)-{'/','M'}-set(FIX))
def dec(k):
  o=[]
  for t in T:
    if t=='/': o.append(' ')
    elif t=='M': o.append(o[-1] if o else '')
    else: o.append(k[t])
  return ''.join(o)
random.seed(int(sys.argv[2]) if len(sys.argv)>2 else 1)
best=None
for run in range(int(sys.argv[1])):
  k={s:random.choice(alpha) for s in syms}; k.update(FIX); sc=M.score(dec(k)); temp=15
  for it in range(40000):
    s=random.choice(syms); old=k[s]; k[s]=random.choice(alpha)
    n=M.score(dec(k))
    if n>sc or random.random()<math.exp((n-sc)/temp): sc=n
    else: k[s]=old
    temp=max(0.2,temp*0.99985)
  if not best or sc>best[0]: best=(sc,dict(k))
  print(round(sc/len(T),3),dec(k)[:200]); sys.stdout.flush()
print(best[1]); print(dec(best[1]))
