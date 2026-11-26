"""Rounds 5-8. Run with python -X utf8 rounds_5_8.py from any directory."""
import csv
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
from random import Random
from statistics import median
from paired_inventory import rows, alphabet
from check import secure

root = Path(__file__).resolve().parent
with (root/'lower-register.tsv').open(encoding='utf8') as f:
    cells = list(csv.DictReader(f, delimiter='\t'))

def suffix_scores(a,b):
    def length(x,y,allow_gaps):
        prev=[0]*(len(y)+1)
        best=0
        for t in x:
            cur=[0]
            for j,u in enumerate(y):
                same=t==u and secure(t)
                n=prev[j]+1 if same else 0
                if allow_gaps:
                    n=max(n,prev[j+1],cur[-1])
                cur.append(n)
            best=max(best,max(cur))
            prev=cur
        return best
    def edges(seq):
        return {tuple(sorted(pair)) for pair in zip(seq,seq[1:]) if all(map(secure,pair))}
    return [length(a,b,False),length(a,b[::-1],False),length(a,b,True),
            length(a,b[::-1],True),len(edges(a)&edges(b))]

def copying():
    # Interior positions 1-11 (including the previously seen triplet) excluded.
    a,b=[rows[r][11:] for r in (1,3)]
    original=suffix_scores(a,b)
    rng=Random(5705)
    null=[]
    for _ in range(5000):
        shuffled=[]
        for seq in (a,b):
            pool=[s for s in seq if secure(s)]
            rng.shuffle(pool)
            shuffled.append([pool.pop() if secure(s) else s for s in seq])
        null.append(suffix_scores(*shuffled))
    print('suffix secure scores',original)
    print('null at least observed of 5000',[sum(v[j]>=n for v in null) for j,n in enumerate(original)])

def transducers():
    # Target indices for source positions, after each possible omission.
    layouts={
        'straight':list(range(22)), 'mirror':list(reversed(range(22))),
        'neighbor swap':[i^1 for i in range(22)], 'half turn':[(i+11)%22 for i in range(22)],
        'fold from ends':[i//2 if i%2==0 else 21-i//2 for i in range(22)]}
    for name,order in layouts.items():
        fits=[]
        for drop in range(23):
            even=rows[1][:drop]+rows[1][drop+1:]
            mapping=defaultdict(Counter)
            for i,j in enumerate(order):
                a,b=even[i],rows[3][j]
                if secure(a) and secure(b):mapping[a][b]+=1
            errors=sum(sum(v.values())-max(v.values()) for v in mapping.values())
            # Require an unambiguous even-pair majority to predict a held-out odd cell.
            predictions={}
            for i,j in enumerate(order):
                counts=mapping.get(rows[0][i],{})
                if counts and secure(rows[2][j]):
                    best=[v for v,n in counts.items() if n==max(counts.values())]
                    if len(best)==1: predictions[j]=best[0]
            fits.append((errors,predictions))
        low=min(e for e,p in fits)
        best=[p for e,p in fits if e==low]
        consensus={j:v for j,v in best[0].items() if all(p.get(j)==v for p in best)}
        print(name,'training conflicts',low,'best omissions',len(best),
              'odd successes / consensus',sum(rows[2][j]==v for j,v in consensus.items()),len(consensus))

def marks():
    for task in ['forward step','backward step','mirror sum','next-column offset','skip-one step']:
        cases=[]
        for cell in cells:
            if not cell['interior_position']:continue
            r=int(cell['row'])-1
            i=int(cell['interior_position'])-1
            label=cell['lower']
            if '?' in label or label=='lost':continue
            j=i+{'backward step':-1,'skip-one step':2}.get(task,1)
            if not 0<=j<len(rows[r]):continue
            a,b=rows[r][i],rows[r][j]
            if not secure(b) or (task!='next-column offset' and not secure(a)):continue
            y=alphabet.index(b)
            if task=='mirror sum': value=y+alphabet.index(a)
            elif task=='next-column offset':value=y-j
            else:value=y-alphabet.index(a)
            cases.append((r,i,label,value%22))
        outcomes=[]
        for hold in [(0,),(2,),(1,3)]:
            for r,i,label,actual in cases:
                if r not in hold:continue
                train=[(s,v) for s,k,l,v in cases if s not in hold and l==label]
                if len({s for s,v in train})>=2 and len({v for s,v in train})==1:
                    outcomes.append(train[0][1]==actual)
        conflicting=[l for l in sorted({x[2] for x in cases})
                     if len({v for r,i,k,v in cases if k==l})>1]
        print(task,'observed',len(cases),'conflicting classes',conflicting,'correct / eligible',sum(outcomes),len(outcomes))

def spacing():
    coords=[[int(c['x_preview']) for c in cells if int(c['row'])==r and c['x_preview']] for r in (2,3,4)]
    def normalized(x):
        return [(x[0]-v)/(x[0]-x[-1]) for v in x]
    a,b,c=map(normalized,coords)
    ref=[sum(t)/2 for t in zip(b,c)]
    def scores(x):
        # Endpoints fixed. Units are fractions of the observed row width.
        return [sum(abs(p-q) for p,q in zip(x,b)),sum(abs(p-q) for p,q in zip(x,c)),
                sum((p-q)**2 for p,q in zip(x,ref)),max(abs(p-q) for p,q in zip(x,ref)),
                sum(abs((x[j+1]-x[j])-(ref[j+1]-ref[j])) for j in range(25))]
    candidates={d+1:scores(a[:d]+a[d+1:]) for d in range(2,25)}
    for k in range(5):
        ordered=sorted(candidates,key=lambda d:candidates[d][k])
        low=candidates[ordered[0]][k]
        print('spacing model',k+1,'best full positions',[d for d in ordered if abs(candidates[d][k]-low)<1e-10],
              'best score',round(low,6),'runner up',ordered[1],round(candidates[ordered[1]][k],6))
if __name__=='__main__':
    copying()
    transducers()
    marks()
    spacing()
