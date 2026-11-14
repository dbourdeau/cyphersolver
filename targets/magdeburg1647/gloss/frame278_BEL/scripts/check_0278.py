"""Second check of the frozen key: frame 0278 cipher/gloss pairs (see PREREG2_frame0278.md). Run once."""
import csv, json, sys, random, difflib
from pathlib import Path
base = Path(sys.argv[1])
key = json.load(open(base/'results/key.json'))['key']
def norm(s):
    s = s.lower()
    for a, b in (('ä','a'),('ö','o'),('ü','u'),('v','u'),('j','i'),(' ','')): s = s.replace(a, b)
    return s
ci = {r['id']: r['cipher_as_seen'] for r in csv.DictReader(open(base/'transcription/f0278_cipher_as_seen.tsv'), delimiter='\t')}
gl = {r['id']: norm(r['clear_as_seen']) for r in csv.DictReader(open(base/'transcription/f0278_gloss_as_seen.tsv'), delimiter='\t')}
pairs = [(i, ci[i], gl[i]) for i in sorted(ci)]
def score(k, show=False):
    m = t = 0
    for i, c, p in pairs:
        d = ''.join(k.get(x, '?') for x in c)
        mb = sum(b.size for b in difflib.SequenceMatcher(None, d, p, autojunk=False).get_matching_blocks())
        m += mb; t += len(p)
        if show: print(f'{i}\t{c}\t{d}\t{p}\t{mb}/{len(p)}')
    return m / t
real = score(key, show=True)
rng = random.Random(278); ks = list(key); vs = list(key.values()); null = []
for _ in range(200):
    rng.shuffle(vs); null.append(score(dict(zip(ks, vs))))
best = max(null)
ext = dict(key, x='m', W='p')
res = {'score': round(real, 4), 'best_shuffled': round(best, 4), 'mean_shuffled': round(sum(null)/len(null), 4),
       'margin': round(real - best, 4), 'pass': real >= 0.85 and real - best >= 0.30, 'n_pairs': len(pairs),
       'descriptive_with_x_m_W_p': round(score(ext), 4)}
json.dump(res, open(base/'results/check_0278_result.json', 'w'), indent=1)
print(res)
