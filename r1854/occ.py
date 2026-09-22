"""Per-occurrence choice for one sign: python occ.py tokens key SIGN opt1,opt2,...  (uses '_' for null)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm
key=dict(l.strip().rsplit('=',1) for l in open(sys.argv[2],encoding='utf-8') if '=' in l)
S=sys.argv[3]; opts=sys.argv[4].split(',')
m=lm.load('la', spaces=False)
C=float(os.environ.get('NULLC','-2.6'))
lines=[(l.split(':',1)[0], [t for t in l.split(':',1)[1].split() if t not in ('_','?')]) for l in open(sys.argv[1],encoding='utf-8') if l.startswith('L')]
toks=[(lab,t) for lab,ts in lines for t in ts]
idx=[i for i,(lab,t) in enumerate(toks) if t==S]
ch={i:key[S] for i in idx}
def txt(lo,hi,over):
    return ''.join((over.get(i,ch.get(i)) if toks[i][1]==S else key.get(toks[i][1],'?')).replace('_','') for i in range(lo,hi))
for rnd in range(2):
    for i in idx:
        lo,hi=max(0,i-12),min(len(toks),i+13)
        best=max(opts,key=lambda o: m.score(txt(lo,hi,{i:o}))+(C if o=='_' else 0))
        ch[i]=best
for i in idx:
    lo,hi=max(0,i-8),min(len(toks),i+9)
    print(toks[i][0], i, ch[i], txt(lo,i,{}), '['+ch[i]+']', txt(i+1,hi,{}))
