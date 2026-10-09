"""Sum sense.tsv per letter and overall; language check of the readings with the shared lang/ engine."""
import sys, os, re
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from collections import defaultdict
T=defaultdict(int); R=defaultdict(int); txt=defaultdict(str)
for l in open(os.path.join(os.path.dirname(__file__),'sense.tsv'),encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    d,line,t,r,u,rd=l.rstrip('\n').split('\t')
    T[d]+=int(t); R[d]+=int(r); txt[d]+=' '+rd
for d in T: print(f'{d}: {R[d]}/{T[d]} = {R[d]/T[d]:.3f}')
a=sum(R[d] for d in T if d!='no68'); b=sum(T[d] for d in T if d!='no68')
print(f'nos. 45+79+47: {a}/{b} = {a/b:.3f}')
print(f'all four: {sum(R.values())}/{sum(T.values())} = {sum(R.values())/sum(T.values()):.3f}')
try:
    from lang import lm
    for d in ('no45','no79','no47'):
        s=re.sub(r'\[[^\]]*\]|\([^)]*\)|·','',txt[d])
        print(d,'best_language:',lm.best_language(s)[:3] if isinstance(lm.best_language(s),list) else lm.best_language(s))
except Exception as e: print('lm check failed:',e)
