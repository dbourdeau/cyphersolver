"""Held-out test: key built only from page-3 segments S01-S15 (frozen), applied to page-4 segments
S16-S23; the mechanical decryption is compared with the contemporary pencil gloss.
Score = 1 - edit_distance(decryption, gloss) / len(gloss), letters only, per segment and pooled.
Groups absent from the frozen key are written '?' (count as errors). Control: the same score for
200 keys whose values are shuffled among the groups."""
import sys, random, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_key import load, build
def ed(a, b):
    d = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        p, d[0] = d[0], i
        for j, cb in enumerate(b, 1):
            p, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, p + (ca != cb))
    return d[-1]
segs, gl = load()
train = ['S%02d' % i for i in range(1, 16)]; test = ['S%02d' % i for i in range(16, 24)]
key, _ = build(train, segs, gl)
key = {g: v for g, v in key.items() if v and len(v) <= 2 or g in ('82', '90', '91', '96', '99')}
def score(k):
    E = L = 0; rows = []
    for s in test:
        dec = ''.join(k.get(g, '?') for g in segs[s]); e = ed(dec, gl[s]); E += e; L += len(gl[s])
        rows.append((s, dec, gl[s], 1 - e / len(gl[s])))
    return 1 - E / L, rows
sc, rows = score(key)
for s, dec, g, x in rows: print(f'{s}\t{x:.3f}\n  dec  {dec}\n  gloss {g}')
unk = sorted({g for s in test for g in segs[s] if g not in key}); ntest = sum(len(segs[s]) for s in test)
print(f'pooled held-out letter agreement {sc:.3f} over {sum(len(gl[s]) for s in test)} gloss letters, {ntest} groups; groups not in frozen key: {unk}')
random.seed(1); vals = list(key.values()); ctrl = []
for _ in range(200):
    random.shuffle(vals); ctrl.append(score(dict(zip(key.keys(), vals)))[0])
print(f'shuffled-key control: max {max(ctrl):.3f}, mean {sum(ctrl)/len(ctrl):.3f}')
