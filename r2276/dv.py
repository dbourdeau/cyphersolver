import sys,json
from decode import load
import os
K=json.load(open(os.environ.get('KEY','key_v6.json'),encoding='utf8'))
L=dict(load(['t1.txt','t2.txt','t3.txt']))
for n in sys.argv[1:]:
    toks=L[n]
    print(n,' '.join(toks))
    print('   ',' '.join(K.get(t,'*'+t).split(',')[0] if t!='...' else '...' for t in toks))
    print('   ',''.join(K.get(t,'*').split(',')[0] if t!='...' else '[...]' for t in toks))
