import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'caprile1519'))   # shared anneal.py / fastanneal.py (split 14 Oct 2026)
import fastanneal as F
from anneal import runs
fixed={'0':'e','25':'e','15':'s','90':'s','45':'i','65':'n','y':'n','70':'o','75':'p','85':'r','86':'a','95':'t','30':'c'}
seqs=runs('r1137_transcription.txt')
(sc,key),toks=F.run(seqs,150000,int(sys.argv[1]),seed=int(sys.argv[2]),fixed=fixed)
print('best',sc);print({t:F.M.alpha[k] for t,k in zip(toks,key)})
ti={t:i for i,t in enumerate(toks)}
for s in seqs: print(' '.join(s)); print('   ',''.join(F.M.alpha[key[ti[t]]] for t in s))
