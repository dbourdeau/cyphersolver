import re,numpy as np,unicodedata
t=''
for f in ['it-renaissance','it-gutenberg']: t+=open('../lang/corpora/'+f+'.txt',encoding='utf8',errors='ignore').read()+' '
t=unicodedata.normalize('NFD',t.lower());t=''.join(c for c in t if not unicodedata.combining(c))
t=t.replace('j','i').replace('v','u')
w=re.findall('[a-z]+',t)
w=[x for x in w if not re.fullmatch('[iuxlcdm]+',x) or x in ('il','di','mi','ci','dice','lui','ui','mil')]
s=''.join(w);A='abcdefghilmnopqrstuz';ix={c:i for i,c in enumerate(A)};N=20
x=np.array([ix[c] for c in s if c in ix])
def cnt(n):
  k=np.zeros(len(x)-n+1,dtype=np.int64)
  for j in range(n): k=k*N+x[j:len(x)-n+1+j]
  return np.bincount(k,minlength=N**n).astype(float)
p=(cnt(1)+1);p/=p.sum()
for n in (2,3,4):
  c=cnt(n).reshape(-1,N);prev=p.reshape(-1,N)[np.arange(c.shape[0])%(N**(n-2))] if n>2 else np.tile(p,(c.shape[0],1))
  p=((c+20*prev)/(c.sum(1,keepdims=True)+20)).ravel()
np.save('q4.npy',np.log(p))
lp=np.log(p)
def sc(t):
  y=[ix[ch] for ch in t];k=[((y[i]*N+y[i+1])*N+y[i+2])*N+y[i+3] for i in range(len(y)-3)];return lp[k].mean()
for t in ['iiiiiiiiiiiiiiii','laserenitauostrahauerainteso','eeeeeeeeeeeeeee','dicheuostraserenitasaraauisata']:print(t,sc(t))
