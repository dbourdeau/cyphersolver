"""Print one line's tokens with the beam's chosen value per token."""
import sys, json
sys.path.insert(0,'..')
import beam
from solve import build
C = beam.cands('cands.json'); L,_ = build(['p1.txt','p2.txt','p3.txt'])
for name,toks in L:
    if name not in sys.argv[1:]: continue
    out=[]; cur=[]
    for t in toks+['...']:
        if t=='...':
            if cur:
                c,s,ch=beam.decode(cur,C); out+= [f'{a}:{b}' for a,b in zip(cur,ch)]
            cur=[]; out.append('…')
        else: cur.append(t)
    print(name,' '.join(out[:-1]))
