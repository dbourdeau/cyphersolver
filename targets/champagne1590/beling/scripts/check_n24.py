"""Held-out check of key no. 25 on no. 24's interlinear glosses (PREREG.md). Run once."""
import csv, json, random, sys
sys.path.insert(0, 'scripts')
from key25 import load
key = load('key/key25.md')
fig = {(r['run'], r['pos']): r['figure_as_seen'] for r in csv.DictReader(open('transcription/n24_figures.tsv'), delimiter='\t')}
gl = [(r['run'], r['pos'], r['gloss_as_seen'].strip().lower()) for r in csv.DictReader(open('transcription/n24_glosses.tsv'), delimiter='\t') if r['gloss_as_seen'].strip()]
norm = lambda c: {'v': 'u', 'j': 'i'}.get(c, c)
def score(k, show=False):
    m = 0
    for run, pos, g in gl:
        f = fig[(run, pos)]; v = k.get(f, '')
        ok = norm(v) == norm(g); m += ok
        if show: print(run, pos, f, repr(v), g, int(ok), sep='\t')
    return m / len(gl)
real = score(key, True)
rng = random.Random(1590); ks = list(key); vs = list(key.values()); null = []
for _ in range(200):
    rng.shuffle(vs); null.append(score(dict(zip(ks, vs))))
res = {'n_glossed': len(gl), 'score': round(real, 4), 'best_shuffled': round(max(null), 4),
       'mean_shuffled': round(sum(null) / len(null), 4), 'margin': round(real - max(null), 4),
       'pass': len(gl) >= 8 and real >= 0.85 and real - max(null) >= 0.30}
json.dump(res, open('results/check_n24_result.json', 'w'), indent=1); print(res)
