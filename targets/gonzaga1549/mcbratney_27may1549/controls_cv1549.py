"""Shuffled-key control: permute the values of key_cv1549.tsv among the labels that have a value (basis != none),
5,000 keys per seed, seeds 20261112 and 7; score each with decode_cv1549.score; count keys >= the real total.
Second control: each block's decode scored against the other blocks' reference passages (wrong-reference control)."""
import json, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import decode_cv1549 as d
key, tr = d.load_key(), d.load_tr()
refs = json.load(open(os.path.join(d.D,'ref_blocks.json'), encoding='utf-8'))
def tot(k):
    r = d.score(k, tr, refs); return sum(x['matched'] for x in r.values()), sum(x['ref_letters'] for x in r.values())
real_m, real_r = tot(key)
out = [f'real: {real_m} of {real_r} = {100*real_m/real_r:.1f}%']
labs = [l for l,(v,b) in key.items() if b != 'none']
for seed in (20261112, 7):
    rng = random.Random(seed); vals = [key[l][0] for l in labs]; best = 0; ge = 0; ss = []
    for _ in range(5000):
        rng.shuffle(vals); k2 = dict(key); k2.update({l:(v,'table') for l,v in zip(labs, vals)})
        m, r = tot(k2); ss.append(m/r); best = max(best, m/r); ge += (m >= real_m)
    ss.sort()
    out.append(f'seed {seed}: 5000 shuffled keys, >= real: {ge}; best {100*best:.1f}%; median {100*ss[2500]:.1f}%; 99th pct {100*ss[4950]:.1f}%')
for a in ('B1','B2','B3'):
    for b in ('B1','B2','B3'):
        if a == b: continue
        r2 = dict(refs); r2[a] = refs[b]
        res = d.score(key, tr, r2)[a]
        out.append(f'wrong reference: decode {a} vs reference {b}: {res["matched"]} of {res["ref_letters"]} = {100*res["matched"]/res["ref_letters"]:.1f}%')
open(os.path.join(d.D,'27may1549_controls.txt'),'w').write('\n'.join(out)+'\n'); print('\n'.join(out))
