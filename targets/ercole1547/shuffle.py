# shuffle.py: 5,000 shuffled keys per seed (values permuted within classes), scored with the same language model
# (local 5-gram, no spaces: work/build_lm.py). Real key against shuffles, on the held-out lines 7-8 and on the full text.
# python3 -I shuffle.py > shuffle_out.txt
import sys, random, re
import numpy as np
sys.path.insert(0,'/home/claude/keyless/_cs'); sys.path.insert(0,'/home/claude/keyless/ercole1547')
from lang import lm
import decode_once as D
LM=lm.DenseLM(np.load('/home/claude/keyless/ercole1547/work/it1540.o5.ns.npy'),5,lm.alphabet('early',False))
CONS=['S01','S02','S03','S04','S10','S11','S12','S13','S14','S17','S19','S22','S24','S25']
VOWB=['S06','S07','S08','S09','S15','S16','S18','S20','S21','S23']
MARK=['^4','^+','^s','^6','^7','^8','^9','^2','^/','^\\','^I']
def score(key,lines):
    tot=0.0;n=0
    for pg,ln,u in D.decode(key):
        if ln not in lines: continue
        s=''.join(u)
        for seg in re.split(r'\?|\{[^}]*\}',s):
            x=LM.encode(seg)
            if len(x)>=5: tot+=LM.score_idx(x); n+=len(x)-4
    return tot/max(1,n)
def shuffled(key,rnd):
    base,mark,special=key; b=dict(base); m=dict(mark)
    for cls,d in ((CONS,b),(VOWB,b),(MARK,m)):
        vals=[d[k] for k in cls]; rnd.shuffle(vals)
        for k,v in zip(cls,vals): d[k]=v
    return b,m,special
real=D.load_key()
for name,lines in (('held-out lines 7-8',(7,8)),('full text lines 1-8',tuple(range(1,9))),('build lines 1-6',tuple(range(1,7)))):
    r=score(real,lines)
    for seed in (20261112,7):
        rnd=random.Random(seed)
        sc=np.array([score(shuffled(real,rnd),lines) for _ in range(5000)])
        print('%s | seed %d | real %.4f | shuffles: mean %.4f sd %.4f best %.4f | shuffles >= real: %d of 5000 | z %.1f'%(name,seed,r,sc.mean(),sc.std(),sc.max(),int((sc>=r).sum()),(r-sc.mean())/sc.std()))
        sys.stdout.flush()
