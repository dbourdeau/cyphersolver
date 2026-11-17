"""Decode a pass file (A or B or reconciled) run by run with a key. Runs = rows sharing leaf + base run letter (a, a(cont.) ...), in reading order.
usage: decode_runs.py <key.json> <pass.tsv> [--w6i] [--both-offsets]"""
import json, sys, re
key={k:v for k,v in json.load(open(sys.argv[1])).items() if not k.startswith('_')}
extra=[a for a in sys.argv[3:]]
if '--w6i' in extra: key['w6']='i'
def toks(s):
    s=re.sub(r'\[([^/\]]+)/[^\]]*\]',r'\1',s)
    return [t for t in s.split() if t and not t.startswith('[')]
rows=[l.rstrip('\n').split('\t') for l in open(sys.argv[2]) if not l.startswith('#') and not l.startswith('leaf')]
rows=[r for r in rows if len(r)>=5 and not r[2].startswith('x') and r[0] not in ('19r','62r')]
if 'passB' in sys.argv[2]: rows=rows[::-1]
runs={}; order=[]
for r in rows:
    base=r[2].split('(')[0]
    k=(r[0],base)
    if k not in runs: runs[k]=[]; order.append(k)
    runs[k].append(r)
# sort rows within run by line_y
tot=hit=0
for k in order:
    rr=sorted(runs[k],key=lambda r:float(r[1]))
    s=[t for r in rr for t in toks(r[4])]
    best=None
    for off in (0,1):
        p=[s[j]+s[j+1] for j in range(off,len(s)-1,2)]
        h=sum(g in key for g in p)
        if best is None or h>best[0]: best=(h,off,p)
    h,off,p=best
    tot+=len(p); hit+=h
    print(f"{k[0]}\t{k[1]}\toff{off}\t{h}/{len(p)}\t{''.join(key.get(g,'.') for g in p)}\t{' '.join(p)}\t[{rr[0][3]} | {rr[-1][5]}]")
print(f'TOTAL {hit}/{tot} = {100*hit/tot:.1f}%')
