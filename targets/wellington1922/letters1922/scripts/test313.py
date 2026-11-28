"""Pre-registered test of Narvaez's key 313, unchanged, on six felicista letters (PLAN.md, SHA-256 304a1ffa...).
C2: Spanish letter-trigram score (Archivo Santander vol. XIV, Bogota 1918, Internet Archive archivosantander14bogo,
_djvu.txt; folded to 27 letters, add-one smoothing) of each letter's runs: 313 against 1,000 random shift triples
(each 0-26, random.seed(20261125)) and its rank among all 27^3 triples (chosen variant).
P2: share of the letters covered by words of 3+ letters in a best segmentation with the Santander word list
(words seen at least twice); 100 random triples as controls (random.seed(20261126)).
Variant per letter: higher C2 score on the first third of its runs (rounded up), tie -> A; then frozen.
Pass: C2 (313 above all 1,000 random triples, a draw equal to 3-1-3 not counted) and P2 (>= 0.50 and above all 100
controls); fewer than 60 decodable letters -> too short to decide.
python3 -I scripts/test313.py test313_transcription.tsv <archivosantander14bogo_djvu.txt> test313"""
import sys, os, math, random, collections, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from f313 import A, KEY, clean, units, dec_unit, load, fold
from pathlib import Path
trans, corpus_path, outdir = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
IDX = {c: i for i, c in enumerate(A)}
text = fold(open(corpus_path, encoding='utf-8', errors='replace').read())
stream = [IDX[c] for c in text if c in IDX]
N3 = collections.Counter(); N2 = collections.Counter()
for i in range(len(stream) - 2):
    N3[(stream[i], stream[i+1], stream[i+2])] += 1; N2[(stream[i], stream[i+1])] += 1
LT = [0.0] * (27 ** 3)
for a in range(27):
    for b in range(27):
        d = N2[(a, b)] + 27
        for c in range(27):
            LT[(a * 27 + b) * 27 + c] = math.log((N3[(a, b, c)] + 1) / d)
words = collections.Counter(w for w in text.split() if len(w) >= 2)
WL = {w for w, n in words.items() if n >= 2} | {'A', 'E', 'O', 'U', 'Y'}
MAXW = max(len(w) for w in WL)

def prep(runs, variant):
    """per run: list of (cipher index or None, phase); trigram triples of positions (no '?')."""
    P = []
    for r in runs:
        seq = []
        for u in units(clean(r['run']), variant):
            for j, ch in enumerate(u):
                seq.append((IDX.get(ch), j % 3))
        P.append(seq)
    return P

def tri_list(P):
    T = []
    for seq in P:
        if len(seq) < 3: continue
        for i in range(len(seq) - 2):
            a, b, c = seq[i], seq[i+1], seq[i+2]
            if None in (a[0], b[0], c[0]): continue
            T.append((a[0], a[1], b[0], b[1], c[0], c[1]))
    return T

def score(T, k):
    s = 0.0
    for c1, p1, c2, p2, c3, p3 in T:
        s += LT[(((c1 - k[p1]) % 27) * 27 + (c2 - k[p2]) % 27) * 27 + (c3 - k[p3]) % 27]
    return s / len(T) if T else float('nan')

def decs(P, k):
    return [''.join('?' if c is None else A[(c - k[p]) % 27] for c, p in seq) for seq in P]

def coverage(strings):
    cov = tot = 0
    for s in strings:
        n = len(s); best = [0] * (n + 1)
        for i in range(1, n + 1):
            b = best[i-1]
            for L in range(3, min(MAXW, i) + 1):
                if s[i-L:i] in WL and best[i-L] + L > b: b = best[i-L] + L
            best[i] = b
        cov += best[n]; tot += sum(ch != '?' for ch in s)
    return cov / tot if tot else float('nan')

R = load(trans)
rng = random.Random(20261125); RAND = [tuple(rng.randrange(27) for _ in range(3)) for _ in range(1000)]
rng2 = random.Random(20261126); RAND2 = [tuple(rng2.randrange(27) for _ in range(3)) for _ in range(100)]
outdir.mkdir(parents=True, exist_ok=True)
summary = []
for L in ['L1', 'L2', 'L3', 'L4', 'L5', 'L6']:
    runs = [r for r in R if r['id'].startswith(L + '.')]
    third = runs[:math.ceil(len(runs) / 3)]
    sA = score(tri_list(prep(third, 'A')), KEY); sB = score(tri_list(prep(third, 'B')), KEY)
    var = 'B' if (sB > sA) else 'A'
    res = {'letter': L, 'runs': len(runs), 'first_third_runs': len(third), 'first_third_A': sA, 'first_third_B': sB, 'variant': var}
    for v in ('A', 'B'):
        P = prep(runs, v); T = tri_list(P)
        n_letters = sum(c is not None for seq in P for c, _ in seq)
        s313 = score(T, KEY); cs = [score(T, k) for k in RAND]
        res[v] = {'letters': n_letters, 'trigrams': len(T), 's313': s313, 'rand_max_other': max(c for c, k in zip(cs, RAND) if k != KEY),
                  'rand_mean': sum(cs) / len(cs), 'rand_below': sum(c < s313 for c in cs), 'rand_equal_313': sum(k == KEY for k in RAND)}
        if v == var:
            allsc = [(score(T, k), k) for k in itertools.product(range(27), repeat=3)]
            allsc.sort(reverse=True)
            res[v]['rank_313_of_19683'] = [k for _, k in allsc].index(KEY) + 1
            res[v]['top5'] = [(''.join(map(str, k)) if all(x < 10 for x in k) else '-'.join(map(str, k)), round(s, 3)) for s, k in allsc[:5]]
            cov = coverage(decs(P, KEY)); ccov = [coverage(decs(P, k)) for k in RAND2]
            res[v]['P2_313'] = cov; res[v]['P2_ctrl_max'] = max(ccov); res[v]['P2_ctrl_mean'] = sum(ccov) / len(ccov)
            c2 = res[v]['rand_max_other'] < s313
            p2 = cov >= 0.5 and cov > max(ccov)
            res['verdict'] = 'too short to decide' if n_letters < 60 else ('PASS' if (c2 and p2) else 'MISS')
            res['C2_pass'] = c2; res['P2_pass'] = p2
        with open(outdir / f'decryption_{L}_{v}.tsv', 'w', encoding='utf-8', newline='\n') as f:
            f.write(f'# {L}, key 313, variant {v} (mechanical output of scripts/test313.py)\n# id\timage\tdecryption\n')
            for r in runs:
                f.write(f"{r['id']}\t{r['image']}\t{' '.join(dec_unit(u) for u in units(clean(r['run']), v))}\n")
    summary.append(res)
    print(res, flush=True)
import json
json.dump(summary, open(outdir / 'test313_results.json', 'w', encoding='utf-8', newline='\n'), indent=1, ensure_ascii=False)
