import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..')); from lang import lm
from syl import RC
m=lm.load('es-modern')
segs=["99-16-85-66-61-55-24-87-96-28-12-66-34-94","61-96-84-20-16-28-39-12-33-16-37-96-31","50-62-51-67-95-36-85","32-12-82-15-66-14-67-99-10-85-65-12-22-92-36-16-21"]
res=[]
for o in (0,1):
 for a in range(10):
  for b in range(10):
   t=' '.join(''.join(RC[str(((int(g[o])+a)%10))+str(((int(g[1-o])+b)%10))] for g in s.split('-')) for s in segs)
   res.append((m.per_char(lm.norm(t.replace('ñ','n'),'modern')),o,a,b,t[:70]))
res.sort(reverse=True)
for r in res[:3]: print(r)
