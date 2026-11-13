"""Ciphertext-only test for LXVIII-1.7.890.1: one value per group (simple substitution), scored with
letter trigrams taken from Dan's Spanish lexicon (lang/lexicons/es.json.gz, word counts), with word
boundaries. Random restarts, swap/replace moves. usage: hillclimb.py WORKTREE TRANSCRIPTION"""
import sys, gzip, json, math, random, collections, re, os
lex = json.load(gzip.open(os.path.join(sys.argv[1], 'lang', 'lexicons', 'es.json.gz'), 'rt', encoding='utf8'))
tri = collections.Counter()
for w, n in lex.items():
    w = '_' + re.sub(r'[^a-z]', '', w) + '_'
    for i in range(len(w) - 2): tri[w[i:i+3]] += n
tot = sum(tri.values()); LOG = {k: math.log(v / tot) for k, v in tri.items()}; FL = math.log(0.5 / tot)
runs = []; ids = []
for ln in open(sys.argv[2], encoding='utf8'):
    if ln.startswith('#') or not ln.strip(): continue
    g = ln.split(' | ')[1].strip().split('-'); runs.append([x for x in g if '?' not in x]); ids.append(ln.split('	')[0])
allruns = runs
if len(sys.argv) > 3:  # fit only on the listed segments, then print every segment
    keep = sys.argv[3].split(','); runs = [r for r, i in zip(runs, ids) if i in keep]
syms = sorted({x for r in runs for x in r}); alpha = 'abcdefghijlmnopqrstuvyz'
def score(k):
    s = 0
    for r in runs:
        t = '_' + ''.join(k[x] for x in r) + '_'
        s += sum(LOG.get(t[i:i+3], FL) for i in range(len(t) - 2))
    return s
best_all = None
random.seed(7)
for rs in range(40):
    pool = list('eaosnridltucmpbgvyqhfzj'); random.shuffle(pool)
    k = {x: pool[i] for i, x in enumerate(syms)}; spare = pool[len(syms):]; cur = score(k)
    for it in range(8000):
        x, y = random.sample(syms, 2)
        if random.random() < 0.2 and spare:
            j = random.randrange(len(spare)); old = k[x]; k[x], spare[j] = spare[j], old; new = score(k)
            if new >= cur: cur = new
            else: spare[j], k[x] = k[x], old
            continue
        k[x], k[y] = k[y], k[x]; new = score(k)
        if new >= cur: cur = new
        else: k[x], k[y] = k[y], k[x]
    if best_all is None or cur > best_all[0]: best_all = (cur, dict(k))
cur, k = best_all
print('score', round(cur, 1), 'symbols', len(syms))
print(' '.join(f'{x}={k[x]}' for x in syms))
for i, r in zip(ids, allruns): print(i, ''.join(k.get(x, '?') for x in r))
