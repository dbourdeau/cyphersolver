import sys,json
from decode import load
k=json.load(open(sys.argv[1],encoding='utf8')); k.update({'1':'de','n':'et'})
L=load(['t1.txt','t2.txt','t3.txt'])
want=sys.argv[2:]
for name,toks in L:
    if want and name not in want: continue
    print(name, ' '.join(f"{t}={k.get(t,'?')}" if t!='...' else '…' for t in toks))
