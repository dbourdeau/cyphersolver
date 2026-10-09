import sys; sys.argv=sys.argv
from measure import *
lid, ln, rd = sys.argv[1], int(sys.argv[2]), sys.argv[3]
L={l[0]:l for l in LETTERS}[lid]
tl=[l.split() for l in open(L[1],encoding='utf-8') if l.strip() and not l.startswith('#')]
tk=[t for t in tl[ln-1] if not t.startswith('"')]
units,words=parse_reading(' '.join(w for w in rd.split() if not w.startswith('+')))
toks=tuple(tuple(cands(t,L[3],EXTRA.get(lid,{}))) for t in tk)
p=align(toks,tuple(units))
if p is None:
    # longest prefix diagnostic
    best=0
    for cut in range(len(tk),0,-1):
        pass
    print('FAIL'); print(' '.join(f'{t}:{"|".join(c) or "-"}' for t,c in zip(tk,toks)))
else:
    out=[]
    for (i,j,k) in p:
        out.append(f"{tk[i]}>{''.join(u[1] or '#' for u in units[j:j+k]) if k else '-'}")
    print('OK',' '.join(out))
