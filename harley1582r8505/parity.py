import sys,os,json,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))+'/..')
import word as W
from solve import load_runs
LET=W.LET; key=json.load(open(sys.argv[1]))
runs=[r for r in load_runs() if len(r)>=3]
st=collections.defaultdict(collections.Counter)
for r in runs:
    base=[key.get(s,'e') for s in r]
    for i,s in enumerate(r):
        if s not in ('E','X','dd','R','d'): continue
        best=None
        for c in LET:
            t=''.join(base[:i]+[c]+base[i+1:])
            v=W.seg_score(t)+W.CH.score(t)
            if best is None or v>best[0]: best=(v,c)
        st[(s,i%2)][best[1]]+=1
for k,c in sorted(st.items()): print(k, c.most_common(4))
