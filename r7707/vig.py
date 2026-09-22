import sys,itertools
sys.path.insert(0,'.')
from lang import lm
ORD='I G R L Y Q S P J T B V X E K F O Z H W N A C U M D'.split()
t=[s for s in open('r7707/ct.txt').read().split() if s!='%']
x=[ORD.index(s) for s in t]
AL='abcdefghijklmnopqrstuvwxyz'
for lang in ['fr-modern','en-modern']:
  m=lm.load(lang,order=4,spaces=False)
  for P in [5,10]:
   for mode in ['vig','beau','var']:
    key=[0]*P; 
    def dec(k):
      o=[]
      for i,v in enumerate(x):
        kk=k[i%P]
        o.append(AL[(v-kk)%26] if mode=='vig' else AL[(kk-v)%26] if mode=='beau' else AL[(v+kk)%26])
      return ''.join(o)
    best=-1e9
    for rnd in range(6):
      improved=True
      while improved:
        improved=False
        for j in range(P):
          for s in range(26):
            k2=key[:];k2[j]=s;sc=m.score(dec(k2))
            if sc>best+1e-9: best,key,improved=sc,k2,True
      if rnd<5: key=[(k+7*rnd)%26 for k in key]
    print(lang,P,mode,round(best/len(x),2),dec(key)[:120])
