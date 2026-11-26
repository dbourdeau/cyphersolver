"""Search paired inventories and literal straight-line openings in K5.7."""
from collections import Counter, defaultdict
from itertools import product
from check import TRANSCRIPTION, secure

alphabet = 'אבגדהוזחטיכלמנסעפצקרשת'
rows = [s.split() for s in TRANSCRIPTION]
x_at = {1:9, 2:3, 3:7}  # zero-based row and interior offsets
def variants(r, value):
    row = list(rows[r])
    if r in x_at:
        row[x_at[r]] = value
    drops = range(len(row)) if r==1 else [None]
    for drop in drops:
        yield drop, [a for i,a in enumerate(row) if i!=drop]

def counts(row):
    return Counter(t for t in row if secure(t))

def inventory(a,b):
    return sum((counts(a)|counts(b)).values())

def inventory_search():
    for r,s in [(1,3),(0,2)]:
        fits=[]
        domains=defaultdict(set)
        for x in alphabet+'X':
            for drop,a in variants(r,x):
                for _,b in variants(s,x):
                    if inventory(a,b)>22: continue
                    fits.append((x,drop))
                    for side,row in enumerate([a,b]):
                        for j,t in enumerate(row):
                            if secure(t): continue
                            original=j+int(side==0 and drop is not None and j>=drop)
                            for v in alphabet+'X':
                                changed=row.copy()
                                changed[j]=v
                                if inventory(changed,[a,b][1-side])<=22:
                                    domains[side,original+1].add(v)
        print('rows',r+1,s+1,'fits',len(fits),'x', ''.join(sorted({x for x,d in fits})),
              'omissions', sorted({d+1 for x,d in fits if d is not None}))
        print('restricted domains:',{k:''.join(sorted(v)) for k,v in domains.items() if len(v)<23})
        if r==1: print('intact marked X omitted in',sum(d==x_at[r] for _,d in fits),'fits')

def routes():
    anchor=rows[1][:7]
    hits=set()
    for drop,even in variants(1,'-'):
        grid=[rows[0],even,rows[2],rows[3]]
        for r,c in product(range(4),range(22)):
            for dr,dc in product([-1,0,1],repeat=2):
                if (dr,dc)==(0,0):continue
                if not(0<=r+6*dr<4 and 0<=c+6*dc<22):continue
                cells=[grid[r+k*dr][c+k*dc] for k in range(7)]
                if cells==anchor: hits.add((r+1,c+1,dr,dc))
    print('secure straight-line hits in normalized grids',sorted(hits))
if __name__=='__main__':
    inventory_search()
    routes()
