import sys,os
os.environ.setdefault('KEY','key_v5.json')
import check
from decode import load
rd={}
for line in open(sys.argv[1],encoding='utf8'):
    if ':' in line: k,v=line.split(':',1); rd[k.strip()]=v.strip()
L=dict(load(['t1.txt','t2.txt','t3.txt']))
for nm in sys.argv[2:]:
    toks=[t for t in L[nm] if t!='...']
    print(nm, rd.get(nm,''))
    print('  ', ' '.join(f"{t}={check.KEY.get(t,'*')}" for t in toks))
    text=check.norm(rd.get(nm,'')).replace('[','').replace(']','')
    p=check.align(toks,text)
    print('  ', ' '.join((f"{t}:{ch}" if t and ch in check.vals(t) else f"[{t}:{ch}]") for t,ch in p))
