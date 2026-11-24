"""Shuffle control (as corsi1513 blind633/627): dictionary cover (Ariosto/Dante word list, words >= 3 letters) of each
doc's decode under the real key vs 5,000 keys with the letter values permuted among signs, seeds 20261112 and 7.
Multi-valued signs score with their first value; nulls and code groups stay fixed.
Usage: python3 -I shuffle.py <blind_dir> <wordlist>
The word list (Ariosto, Orlando furioso + Dante, Commedia, one word per line, 25,566 lines) is not committed."""
import csv, json, sys, os, random
H = os.path.dirname(os.path.abspath(__file__))
B = sys.argv[1]
k = json.load(open(os.path.join(H, '../../aaymeloglu/key.json')))['signs']
m = dict(r for r in csv.reader(open(os.path.join(H, '../sheet_to_key.tsv')), delimiter='\t')); m.pop('label', None)
W = set(w.strip().lower() for w in open(sys.argv[2] if len(sys.argv) > 2 else 'wordlist_ariosto_dante.txt', encoding='utf-8', errors='ignore') if len(w.strip()) >= 3)
ML = max(map(len, W))
base = {l: v['values'][0] for l, v in k.items()}
letters = [l for l, v in base.items() if v and v.isalpha() and len(v) <= 2 and not v.startswith('[')]

def runs(doc):
    rows = list(csv.DictReader(open(os.path.join(B, f'BLIND_{doc}.tsv'), encoding='utf-8'), delimiter='\t'))
    return [[m.get(t.rstrip('?')) for t in r['labels'].split()] for r in rows]

def dec(run, key):
    return ''.join((key.get(l) or '') if l and (key.get(l) or '').isalpha() else '#' if l is None or key.get(l) == '?' else '' for l in run)

def cover(s):
    best = 0; tot = 0
    for part in s.split('#'):
        n = len(part); b = [0] * (n + 1)
        for i in range(1, n + 1):
            b[i] = b[i - 1]
            for L in range(3, min(ML, i) + 1):
                if part[i - L:i] in W:
                    b[i] = max(b[i], b[i - L] + L)
        best += b[n]; tot += n
    return best, tot

def score(R, key):
    c = t = 0
    for run in R:
        a, b = cover(dec(run, key)); c += a; t += b
    return c / t if t else 0.0

for doc in ('d42', 'd49', 'd81', 'd90'):
    R = runs(doc)
    real = score(R, base)
    n = sum(len(r) for r in R)
    print(doc, 'signs', n, 'real', round(real, 4))
    for seed in (20261112, 7):
        r = random.Random(seed); ge = 0; mx = 0
        vals = [base[l] for l in letters]
        for _ in range(5000):
            v = vals[:]; r.shuffle(v)
            kk = dict(base); kk.update(zip(letters, v))
            s = score(R, kk); mx = max(mx, s); ge += s >= real
        print(doc, 'seed', seed, '>=real', ge, '/5000 max', round(mx, 4))
