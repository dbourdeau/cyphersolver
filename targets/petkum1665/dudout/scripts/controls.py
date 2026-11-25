"""Per-control scores for a measure (same code path as scripts/measure.py, which prints only the summary).

Usage (from dudout/):  python3 -I scripts/controls.py key/table_T2.json transcriptions/H2.txt > results/controls_T2_on_H2.tsv
Writes one line per control: seed, character score. Control = the VALUES of the key permuted among its keys
(random.Random(seed).shuffle, seeds 1..200), applied to the same held-out transcription, same score.
Last lines: the true key's score, the best and the mean of the 200 controls, and how many controls reach the true score.
"""
import sys, json, random, re, unicodedata
T = json.load(open(sys.argv[1], encoding='utf-8'))['T']
rows = []
for l in open(sys.argv[2], encoding='utf-8'):
    if l.startswith('#') or not l.strip():
        continue
    g, gl = l.rstrip('\n').split('\t')
    rows.append((g.split('.'), gl))
def norm(s):
    s = unicodedata.normalize('NFD', s.lower()); return re.sub('[^a-z]', '', s)
def lev(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]
R = ''.join(norm(gl) for _, gl in rows)
def score(tab):
    P = ''.join(''.join(tab.get(x, '') for x in g) for g, _ in rows)
    return 1 - lev(P, R) / max(len(P), len(R))
true = score(T)
keys = list(T); vals = [T[k] for k in keys]; wit = []
print('# seed\tscore')
for seed in range(1, 201):
    r = random.Random(seed); v = vals[:]; r.shuffle(v); s = score(dict(zip(keys, v))); wit.append(s)
    print('%d\t%.4f' % (seed, s))
print('# true key\t%.4f' % true)
print('# best control\t%.4f' % max(wit))
print('# mean control\t%.4f' % (sum(wit) / len(wit)))
print('# controls >= true\t%d of 200' % sum(1 for s in wit if s >= true))
