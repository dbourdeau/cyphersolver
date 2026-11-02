"""dec14: decode p1r..p4r.txt (round 6 transcriptions) with key14.json.
Pair rules (left to right): 'o H' + u-sign -> q ; 'H o' -> p ; '6'/'6A' + 'gA' -> ll ;
'G a' / 'G p' -> null pair ; 'v e D'/'v e x' -> code group '#' ; O after a u-sign (qB,M,oo,ooA) -> m ;
R6: 'n' + u-sign (qB,qA,M,oo,ooA,ooB) -> q (unit 'nq'); 'n' elsewhere -> i (unit 'ni': fideliter, beneficio, diem).
Polyphonic key values (R6): 'u/s' (oo, ooA, ooB) -> 'U'; 'u/s/f' (qB) -> 'W'; 'h/f' (s) -> 'S'.
Majority value = first listed; minority = the others (s for U, s/f for W, f for S).
'#' = sign with no value (8C, wL, Ob, Bd, sl, fo); '_' = lost sign.
usage: dec14.py [key.json] [-u]   (writes allr14.txt)"""
import sys,json
U={'qB','qA','M','oo','ooA','ooB'}
USIGN={'qB','M','oo','ooA'}
PAIRS={'oH','Ho','LL','Ga','Gp'}
POLY={'u/s':'U','u/s/f':'W','h/f':'S'}
SETS={'U':'us','W':'usf','S':'hf'}
MAJ={'U':'u','W':'u','S':'h'}
def units(toks):
    out=[];i=0
    while i<len(toks):
        t=toks[i]; n=toks[i+1] if i+1<len(toks) else None; n2=toks[i+2] if i+2<len(toks) else None
        if t=='o' and n=='H' and n2 in U: out.append('oH');i+=2;continue
        if t=='H' and n=='o': out.append('Ho');i+=2;continue
        if t in('6','6A') and n=='gA': out.append('LL');i+=2;continue
        if t=='G' and n in('a','p'): out.append('G'+n);i+=2;continue
        if t=='v' and n=='e' and n2 in('D','x'): out.append('veD');i+=3;continue
        if t=='O' and out and out[-1] in USIGN: out.append('Om');i+=1;continue
        if t=='n': out.append('nq' if n in U else 'ni');i+=1;continue
        out.append(t);i+=1
    return out
def ntok(u): return 3 if u=='veD' else (2 if u in PAIRS else 1)
def lines():
    for p in (1,2,3,4):
        for l in open(f'p{p}r.txt'):
            if ':' not in l: continue
            h,b=l.split(':',1); yield f'P{p}{h.strip()}',[x.rstrip('?') for x in b.split(']')[-1].split()]
def val(k,x):
    if x=='': return '_'
    v=k.get(x)
    if v is None: return '#'
    return POLY.get(v,v)
def dec(k,u): return ''.join(val(k,x) for x in u)
if __name__=='__main__':
    a=[x for x in sys.argv[1:] if not x.startswith('-')]
    k=json.load(open(a[0] if a else 'key14.json'))
    with open('allr14.txt','w') as f:
        for h,t in lines(): f.write(f'{h}: '+' '.join(t)+'\n')
    for h,t in lines():
        u=units(t); print(h,dec(k,u) if '-u' not in sys.argv else ' '.join(f'{x}={val(k,x)}' for x in u))
