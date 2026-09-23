"""For each sign occurrence, which letter does the context want? Reveals merged shapes / polyphony."""
import sys,os,json,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))+'/..')
import word as W
from solve import load_runs
LET=W.LET
key=json.load(open(sys.argv[1]))
runs=[r for r in load_runs() if len(r)>=3]
want=collections.defaultdict(collections.Counter)
for r in runs:
    base=[key.get(s,'e') for s in r]
    for i,s in enumerate(r):
        best=None
        for c in LET:
            t=''.join(base[:i]+[c]+base[i+1:])
            v=W.seg_score(t)+W.CH.score(t)
            if best is None or v>best[0]: best=(v,c)
        want[s][best[1]]+=1
rows=[]
for s,c in want.items():
    tot=sum(c.values()); top=c.most_common(3)
    rows.append((tot, s, key.get(s), top))
rows.sort(reverse=True)
for tot,s,k,top in rows:
    frac=top[0][1]/tot
    flag='  <-- SPLIT?' if frac<0.6 and tot>=15 else ''
    print(f'{s:5s} key={k}  n={tot:4d}  ' + ' '.join(f'{ch}:{n}' for ch,n in top) + flag)
