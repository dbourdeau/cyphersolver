"""Long runs of one message at chosen widths with shuffled control. python wN.py <name> <its> <restarts> w1 w2 ..."""
import sys,json,re
from joint import *
R=json.load(open('letter_runs.json',encoding='utf-8'))
DEF={'lejava0405':['041-0787'],'lejava0426':['042-0250'],'voikov0505':['042-0614'],'krasin0516':['042-0627'],'voikov0616':['043-0436']}
name=sys.argv[1];its,rs=int(sys.argv[2]),int(sys.argv[3]);ws=[int(x) for x in sys.argv[4:]]
s=''.join(''.join(r['groups']) for r in R if any(k in r['file'] for k in DEF[name]))
m=enc(re.sub('[^A-Z]','',s));c=m.copy();np.random.default_rng(2).shuffle(c);print(name,len(m),flush=True)
for w in ws:
    r=[solve([m],w,its,i) for i in range(rs)];b=max(r,key=lambda x:x[0]);k=solve([c],w,its,99)
    print(name,w,[round(x[0],2) for x in r],'ctrl',round(k[0],2),show(m,b[1])[:140],flush=True)
    json.dump(b[1],open(f'K_{name}_{w}.json','w'))
