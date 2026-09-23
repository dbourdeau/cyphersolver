import sys, json, collections
sys.path.insert(0,'..')
import beam
from solve import build
C = beam.cands(sys.argv[1]); L,_ = build(['p1.txt','p2.txt','p3.txt'])
cnt = collections.defaultdict(collections.Counter)
for name,toks in L:
    cur=[]
    for t in toks+['...']:
        if t=='...':
            if cur:
                c,s,ch=beam.decode(cur,C)
                for a,b in zip(cur,ch): cnt[a][b]+=1
            cur=[]
        else: cur.append(t)
for a in sorted(cnt, key=lambda a:-sum(cnt[a].values())):
    print(a, sum(cnt[a].values()), dict(cnt[a].most_common()))
json.dump({a:dict(v) for a,v in cnt.items()}, open('stats.json','w'))
