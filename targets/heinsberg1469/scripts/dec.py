import sys,re
sys.path.insert(0,'scripts')
from norm import load
K=dict(l.rstrip('\n').split('\t') for l in open(sys.argv[1]) if '\t' in l and not l.startswith('#'))
for h,b in load(sys.argv[2],sys.argv[3],sys.argv[4]):
    b2=b.replace('-','').replace('/',' / ').replace('.','').replace(',','')
    print(h.ljust(7), ' '.join(''.join(K.get(c,c if c in '=' else '#') for c in w) for w in b2.split()))
