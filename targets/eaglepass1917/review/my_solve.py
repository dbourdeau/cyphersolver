# Reviewer's own solver: general monoalphabetic simple substitution by simulated annealing,
# Spanish quadgram model built from es.wikipedia extracts (work/dl/*.json). Run with python3 -I.
import json, glob, math, random, sys, unicodedata, collections, re
dl, ctfile = sys.argv[1], sys.argv[2]
seed = int(sys.argv[3]) if len(sys.argv) > 3 else 1
txt = ''
for f in sorted(glob.glob(dl + '/*.json')):
    d = json.load(open(f))
    for p in d['query']['pages'].values():
        txt += p.get('extract', '') + ' '
def fold(s):
    s = unicodedata.normalize('NFD', s.upper())
    return ''.join(c for c in s if 'A' <= c <= 'Z')
T = fold(txt)
q = collections.Counter(T[i:i+4] for i in range(len(T)-3))
N = sum(q.values()); floor = math.log10(0.01/N)
Q = {k: math.log10(v/N) for k, v in q.items()}
def score(s): return sum(Q.get(s[i:i+4], floor) for i in range(len(s)-3))
ct = ''.join(c for c in open(ctfile).read().upper() if 'A' <= c <= 'Z')
A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def dec(k): return ct.translate(str.maketrans(A, k))
random.seed(seed)
best = None
for restart in range(int(sys.argv[4]) if len(sys.argv) > 4 else 20):
    k = list(A); random.shuffle(k); cur = score(dec(''.join(k))); t = 20.0
    for it in range(40000):
        i, j = random.sample(range(26), 2); k[i], k[j] = k[j], k[i]
        s = score(dec(''.join(k)))
        if s > cur or random.random() < math.exp((s-cur)/t): cur = s
        else: k[i], k[j] = k[j], k[i]
        t = max(0.2, t*0.9997)
    if best is None or cur > best[0]: best = (cur, ''.join(k))
print('corpus letters', len(T), 'ct letters', len(ct))
print('score', round(best[0], 1), 'per-letter', round(best[0]/len(ct), 3))
print('key (cipher A-Z -> plain):', best[1])
print(dec(best[1]))
