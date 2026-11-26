"""Alphabet repair bounds and two searches for the seven-sign recipe sequence.
Run with python -X utf8 recipe_rounds.py bound|route|key.
"""
from collections import Counter
from itertools import product
from math import gcd
import sys
from paired_inventory import alphabet, rows, x_at
from check import secure

def repair(row):
    counts=Counter(t for t in row if secure(t))
    return sum(n-1 for n in counts.values())

def bounds():
    choices=[]
    for drop in range(23):
        for x in alphabet:
            nums=[]
            for r,orig in enumerate(rows):
                row=orig.copy()
                if r in x_at: row[x_at[r]]=x
                if r==1: del row[drop]
                nums.append(repair(row))
            choices.append((sum(nums),nums,drop+1,x))
    best=min(c[0] for c in choices)
    fits=[c for c in choices if c[0]==best]
    print('row minima',[min(c[1][i] for c in choices) for i in range(4)])
    print('joint',best,'deletions',sorted({c[2] for c in fits}),'X', ''.join(x for x in alphabet if any(c[3]==x for c in fits)))
    for r,row in enumerate(rows):print('duplicates before any deletion, without X',r+1,{s:n for s,n in Counter(t for t in row if secure(t)).items() if n>1})

# Each path is seven distinct cells. No unknown supports a match.
target='רתנוהרת'
def scan(routes):
    seen=set()
    complete=set()
    best=0
    for line in routes:
        for seq in (line,line[::-1]):
            for p in range(len(seq)-6):
                part=tuple(seq[p:p+7])
                if part in seen: continue
                seen.add(part)
                if not all(map(secure,part)):continue
                complete.add(part)
                best=max(best,sum(a==b for a,b in zip(target,part)))
    return len(complete),best,tuple(target) in complete

def paths(grid,mode):
    if mode=='rails':
        for r,s in [(0,1),(1,2),(2,3),(0,2),(1,3),(0,3)]:
            for phase in (0,1):
                yield [grid[(r,s)[(c+phase)%2]][c] for c in range(22)]
    if mode=='bounce':
        for phase in range(6):
            yield [grid[(0,1,2,3,2,1)[(c+phase)%6]][c] for c in range(22)]
    if mode=='helix':
        for dr,dc in product((1,-1),(1,-1,2,-2)):
            for r,c in product(range(4),range(22)):
                yield [grid[(r+k*dr)%4][(c+k*dc)%22] for k in range(7)]
    if mode=='spiral':
        for fliprows,flipcols in product((0,1),repeat=2):
            mat=[r[::-1] if flipcols else r[:] for r in (grid[::-1] if fliprows else grid)]
            line=[]
            while mat:
                line.extend(mat.pop(0))
                mat=[list(r) for r in zip(*mat)][::-1]
            yield line
    if mode=='nested ends':
        for r in grid:
            order=[i//2 if i%2==0 else 21-i//2 for i in range(22)]
            yield [r[i] for i in order]
            yield [r[21-i] for i in order]

def routesearch():
    for mode in ('rails','bounce','helix','spiral','nested ends'):
        def lines():
            for d in range(23):
                grid=[r[:] for r in rows]
                del grid[1][d]
                yield from paths(grid,mode)
        print(mode,scan(lines()))

def keys():
    # Compare complete horizontal seven-cell windows, including the copied frame
    # but omitting the entirely lost far frame of row 1.
    interior=[['א',f]+seq+([f,'א'] if i else ['.','.'])
              for i,(seq,f) in enumerate(zip(rows,'יהוה'))]
    words={tuple(r[j:j+7]) for r in interior for j in range(len(r)-6)
           if all(map(secure,r[j:j+7]))}
    words|={w[::-1] for w in words}
    q=[alphabet.index(t) for t in target]
    def compatible(w,mode):
        out=[alphabet.index(t) for t in w]
        if mode=='shift':return len({(y-x)%22 for x,y in zip(q,out)})==1
        if mode=='affine':return any(len({(y-a*x)%22 for x,y in zip(q,out)})==1
                                     for a in range(22) if gcd(a,22)==1)
        if mode=='alternating shifts':return all(len({(out[j]-q[j])%22 for j in range(p,7,2)})==1 for p in range(2))
        m=dict(zip(q,out))
        if any(m[x]!=y for x,y in zip(q,out)) or len(set(m.values()))!=len(m):return False
        if mode=='frame fixed':return all(m.get(i,i)==i and (i not in m.values() or m.get(i)==i) for i in map(alphabet.index,'איהו'))
        return all(m.get(y,x)==x for x,y in m.items())
    for mode in ('shift','affine','alternating shifts','frame fixed','involution'):
        print(mode,len(words),[''.join(w) for w in sorted(words) if compatible(w,mode)])
if __name__=='__main__':
    {'bound':bounds,'route':routesearch,'key':keys}[sys.argv[1]]()
