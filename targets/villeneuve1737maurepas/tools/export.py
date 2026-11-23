import sys,json
sys.path.insert(0,sys.argv[1]); from vlib import *
pages=sys.argv[2].split(','); mode=sys.argv[4] if len(sys.argv)>4 else 'page'
rs=rows(pages)
P=list(passages(rs).values()) if mode=='page' else chunks(rs,int(mode))
with open(sys.argv[3],'w') as f:
    f.write(f"{len(P)}\n")
    for p in P:
        cs=[(-1 if c=='GAP' else int(c) if c.isdigit() else -2) for c in p['codes']]
        g=p['g'] or '#'
        f.write(f"{len(cs)} {len(g)}\n{' '.join(map(str,cs))}\n{g}\n")
