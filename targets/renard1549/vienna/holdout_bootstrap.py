#!/usr/bin/env python3
"""Attempt 3 (post-hoc, recorded as such): training-only bootstrap. Stage 1 = EM on the 54 training lines with the page-1 seed;
stage 2 = EM again on the same training lines seeded with stage-1 values that have n_total>=5 and share>=0.7. No held-out line is used before the single decode."""
import sys,os,random,collections,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import pipeline as p
P=p.load_plain();C=p.load_cipher()
text=''.join(t for _,t in P); toks=[s for _,s in C]; ratio=len(text)/len(toks)
lines=list(collections.OrderedDict((l,1) for l,_ in C)); ntrain=round(len(lines)*0.8); trl=set(lines[:ntrain])
tr=[s for l,s in C if l in trl]; ho=[s for l,s in C if l not in trl]
seed=json.load(open(p.W+'seed_page1_only.json'))
for stage in (1,2,3):
    counts,seg,end=p.em(tr,text,seed,ratio,free_end=True)
    key=p.key_from(counts)
    seed={t:v for t,(v,n,tt) in key.items() if tt>=5 and n/tt>=0.7 and v}
    print('stage',stage,'boundary',end,'confident signs',len(seed))
truth=text[end:]; dec=p.decode(ho,key); a=p.acc(dec,truth)
print('HELD-OUT DECODE :',dec); print('HELD-OUT TRUTH  :',truth)
print('held-out letter accuracy: %.4f (edit distance %d, decoded %d, truth %d)'%(a,p.lev(dec,truth),len(dec),len(truth)))
signs=sorted(key); vals=[key[t][0] for t in signs]
for sd in (20261112,7):
    rng=random.Random(sd); best=0;tot=0;ge=0;N=5000
    for _ in range(N):
        v=vals[:]; rng.shuffle(v); k=dict(zip(signs,v))
        s=p.acc(''.join(k.get(t,'?') for t in ho),truth); tot+=s; best=max(best,s); ge+=(s>=a)
    print('control seed %d: %d shuffles: mean %.4f max %.4f, shuffles >= real: %d'%(sd,N,tot/N,best,ge))
