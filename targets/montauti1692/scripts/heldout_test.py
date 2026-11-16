"""Score key_v1 on held-out pairs; compare with 200 shuffled keys (values permuted among the key's groups)."""
import json, random, sys
key = {k: v for k, v in json.load(open(sys.argv[1])).items() if not k.startswith('_')}
rows = [l.rstrip('\n').split('\t') for l in open(sys.argv[2]) if not l.startswith('#') and not l.startswith('seg')]
pairs = [(r[2], r[3]) for r in rows if r[3] != '?']
cov = [(g, p) for g, p in pairs if g in key]
def score(k): return sum(k[g] == p for g, p in cov) / len(cov)
real = score(key)
random.seed(0); vals = list(key.values()); gs = list(key); sh = []
for _ in range(200):
    random.shuffle(vals); sh.append(score(dict(zip(gs, vals))))
print(f'held-out pairs {len(pairs)}, covered {len(cov)} ({len(cov)/len(pairs):.0%}); real key {real:.1%}; shuffled max {max(sh):.1%}, mean {sum(sh)/len(sh):.1%}')
