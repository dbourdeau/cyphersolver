# show alignment of reading to tokens: al.py reading line1 [line2 ...]
import sys,os
os.environ.setdefault('KEY','key_v5.json')
import check
from decode import load
rd={}
for line in open(sys.argv[1],encoding='utf8'):
    if ':' in line and not line.startswith('#'):
        k,v=line.split(':',1); rd[k.strip()]=v.strip()
L=dict(load(['t1.txt','t2.txt','t3.txt']))
for name in sys.argv[2:]:
    toks=[t for t in L[name] if t!='...']
    text=check.norm(rd.get(name,'')).replace('[','').replace(']','')
    p=check.align(toks,text)
    out=[]
    for t,ch in p:
        v=check.vals(t) if t else []
        ok = t is not None and (ch in v or (ch=='' and '' in v))
        s=f'{t or ""}:{ch or "_"}'
        out.append(s if ok else s.upper() if False else '*'+s)
    print(name, rd.get(name,''))
    print('   ',' '.join(out))
