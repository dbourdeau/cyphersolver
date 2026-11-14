"""Held-out test on RIGHT-page booklet pairs with the frozen key (see PREREG.md)."""
import csv, json, sys, random, difflib
from pathlib import Path
base = Path(sys.argv[1])
key = json.load(open(base/'results/key.json'))['key']
def norm_clear(s):
    s = s.lower()
    for a, b in (('ä','a'),('ö','o'),('ü','u'),('v','u'),('j','i'),(' ','')): s = s.replace(a, b)
    return s
pairs = [(r['cipher_as_seen'], norm_clear(r['clear_as_seen']), r['entry'])
         for r in csv.DictReader(open(base/'transcription/booklet_pairs.tsv', encoding='utf-8'), delimiter='\t') if r['page'] == 'R']
def score(k, show=False):
    m = t = 0
    for c, p, e in pairs:
        d = ''.join(k.get(x, '?') for x in c)
        mb = sum(b.size for b in difflib.SequenceMatcher(None, d, p, autojunk=False).get_matching_blocks())
        m += mb; t += len(p)
        if show: print(f'{e}\t{c}\t{d}\t{p}\t{mb}/{len(p)}')
    return m / t
real = score(key, show=True)
rng = random.Random(1647); ks = list(key); vs = list(key.values()); null = []
for _ in range(200):
    rng.shuffle(vs); null.append(score(dict(zip(ks, vs))))
best = max(null)
res = {'score': round(real, 4), 'best_shuffled': round(best, 4), 'mean_shuffled': round(sum(null)/len(null), 4),
       'margin': round(real - best, 4), 'pass': real >= 0.85 and real - best >= 0.30, 'n_pairs': len(pairs)}
json.dump(res, open(base/'results/heldout_result.json', 'w'), indent=1)
print(res)
