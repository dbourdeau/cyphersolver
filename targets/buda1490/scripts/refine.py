import sys,json
from hsolve import load_tokens,solve
t=load_tokens(sys.argv[1]); init=json.load(open(sys.argv[2])); fixed=json.load(open(sys.argv[4])) if len(sys.argv)>4 else None
best=None
for sd in range(4):
    sc,k,tx=solve(t,1,150000,'la',int(__import__('os').environ.get('ORD','4')),seed=sd,verbose=False,init=init,T0=0.6,fixed=fixed)
    print(sd,round(sc,3))
    if not best or sc>best[0]: best=(sc,k)
json.dump(best[1],open(sys.argv[3],'w')); print('best',round(best[0],3))
