# 5,000 shuffled keys per seed (plain values permuted within the vowel class and within the consonant class),
# scored with the same Hungarian no-space 4-gram model as the solver. python3 -I shuffle.py
import sys, gzip, json, random, re
B='/home/claude/keyless/postcards/jolanka'; sys.path.insert(0,B+'/tools')
from decode_lib import toks
m=json.load(gzip.open(B+'/hu-1900-lit.nospace.json.gz','rt',encoding='utf-8')); lp=m['logp4']; fl=m['floor4']
rows=[l.split('\t') for l in open(B+'/KEY.tsv',encoding='utf-8').read().split('\n')[1:] if l]
key={r[0]:r[1] for r in rows}; cls={r[0]:r[2] for r in rows}
segs={'all':[], 'heldout':[], 'training':[]}
for l in open(B+'/TRANSCRIPTION.tsv',encoding='utf-8').read().split('\n')[1:]:
    if not l: continue
    p=l.split('\t'); seg=[]
    for t in toks(p[6])+['[.]']:
        if t[0] in '{[' or t in ',.':
            if seg:
                segs['all'].append(seg); segs['heldout' if p[5]=='1' else 'training'].append(seg); seg=[]
            continue
        seg.append(t.rstrip('?'))
def score(k, S):
    tot=0.0; n=0
    for s in S:
        x=''.join(k.get(t,'q') for t in s)
        for i in range(len(x)-3): tot+=lp.get(x[i:i+4],fl); n+=1
    return tot/n
out=[]
for part in ('all','heldout','training'):
    real=score(key,segs[part]); out.append('%s: real key %.4f per 4-gram (%d signs)'%(part,real,sum(len(s) for s in segs[part])))
    for seed in (20261112,7):
        rnd=random.Random(seed); sc=[]
        for _ in range(5000):
            k=dict(key)
            for c in ('vowel','consonant'):
                ks=[s for s in key if cls[s]==c]; vs=[key[s] for s in ks]; rnd.shuffle(vs); k.update(zip(ks,vs))
            sc.append(score(k,segs[part]))
        sc.sort(); mean=sum(sc)/len(sc); sd=(sum((x-mean)**2 for x in sc)/len(sc))**0.5
        out.append('  seed %d: 5000 shuffles, best %.4f, mean %.4f, sd %.4f; shuffles >= real: %d; real is %.1f sd above the mean'%(seed,sc[-1],mean,sd,sum(1 for x in sc if x>=real),(real-mean)/sd))
open(B+'/shuffle_out.txt','w').write('\n'.join(out)+'\n'); print('\n'.join(out))
