"""Greedy coordinate ascent on the word-segmentation objective: for every sign try every letter."""
import sys,os,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))+'/..')
os.environ.setdefault('LAM','1.0')
import word as W
from solve import load_runs
LET=W.LET
start=json.load(open(sys.argv[1]))
runs=[r for r in load_runs() if len(r)>=3]
signs=sorted({s for r in runs for s in r})
key={s:start.get(s,'e') for s in signs}
LAM=float(os.environ.get('LAM','1.0'))
def sc(k):
    t=0.0
    for r in runs:
        s=''.join(k[x] for x in r); t+=LAM*W.seg_score(s)+W.CH.score(s)
    return t
cur=sc(key); print('start',round(cur,1),file=sys.stderr)
improved=True; rounds=0
while improved and rounds<8:
    improved=False; rounds+=1
    for s in signs:
        old=key[s]; best=(cur,old)
        for c in LET:
            if c==old: continue
            key[s]=c; v=sc(key)
            if v>best[0]: best=(v,c)
        key[s]=best[1]
        if best[1]!=old:
            cur=best[0]; improved=True
            print(f'{s}: {old} -> {best[1]}  {round(cur,1)}',file=sys.stderr)
print(json.dumps(key,sort_keys=True))
print('score',round(cur,1))
