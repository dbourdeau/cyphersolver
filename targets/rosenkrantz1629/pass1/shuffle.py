"""shuffle.py: frozen key vs 5000 shuffled keys (letter values permuted among the sign classes that carry a letter), seeds 20261112 and 7.
Scored with the same da1620 model (5-gram, 3-gram for short runs), on the HELD-OUT letters and on the training letters."""
import sys,random
sys.path.insert(0,'/home/claude/keyless/rosenkrantz1629/tools')
from common import *
key={l.split('\t')[0]:l.split('\t')[1] for l in open(R+'/KEY.tsv').read().splitlines()[1:]}
rows=load(); lm=LM()
def sc(k,which):
    tot=0;n=0
    for r in rows:
        if r[0] in which:
            for s in r[3]:
                x=''.join(k.get(t,'') for t in s).replace('_',''); tot+=lm.score(x); n+=len(x)
    return tot,n
labs=[k for k,v in key.items() if len(v)==1 and v!='_']
for which,name in ((HELD,'held-out N21 N22 N23'),(TRAIN,'training N12 N13 N14 N20')):
    real,n=sc(key,which)
    for seed in (20261112,7):
        rnd=random.Random(seed); ge=0; best=-1e9; tot=0
        for i in range(5000):
            vals=[key[l] for l in labs]; rnd.shuffle(vals); k=dict(key); k.update(zip(labs,vals))
            s,_=sc(k,which); tot+=s; best=max(best,s); ge+=s>=real
        print(f'{name}: letters {n}, real {real:.1f} ({real/n:.3f}/letter); seed {seed}: shuffles >= real {ge}/5000, best shuffle {best:.1f}, mean {tot/5000:.1f}')
