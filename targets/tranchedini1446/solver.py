"""Coordinate-ascent solver for f. 139: every sign type takes one value (letter, table syllable, double letter or word) from a pool;
the score is the mean it-cinquecento log-probability per letter of the decoded runs. Controls: (a) the same runs with the sign
order shuffled, (b) a synthetic cipher with the same run lengths and type counts, enciphered from real Italian.
Run from the repository root: python targets/tranchedini1446/solver.py [restarts=12]"""
import os, random, sys, collections
sys.path.insert(0, os.getcwd())
import numpy as np
from lang import lm
m = lm.load('it-cinquecento', order=5, spaces=False)
LET = list('abcdefghilmnopqrstuz')
SYL = 'ce ci co de du fa li lo me mi na ne no pi re ri ro si ta te to pe sa ma tu fo nu da le pa do ss ee ll tt'.split()
WORDS = 'non che con et in per conte sforza veneziani'.split()
POOL = LET + SYL
CAP = {v: (6 if v in 'aeio' else 4 if len(v) == 1 else 1) for v in POOL}   # most types per value
FIXED = {'WV': 'veneziani', 'c83': 'non', 'c59': 'in', 'c66': 'sforza', 'WC': 'che'}
def load_runs(path):
    return [ln.split() for ln in open(path) if ln.strip()]
def decode(runs, mp):
    return [lm.norm(''.join(mp[t] for t in r), 'early') for r in runs]
def score(runs, mp):
    return m.per_char(''.join(decode(runs, mp)))
def solve(runs, fixed, restarts, seed):
    rnd = random.Random(seed); types = sorted({t for r in runs for t in r}); free = [t for t in types if t not in fixed]
    best = (-99, None)
    for _ in range(restarts):
        mp = dict(fixed); use = collections.Counter()
        for t in free:
            v = rnd.choice([v for v in LET if use[v] < CAP[v]]); mp[t] = v; use[v] += 1
        cur = score(runs, mp); improved = True
        while improved:
            improved = False; rnd.shuffle(free)
            for t in free:
                bv, bs = mp[t], cur
                use = collections.Counter(mp[x] for x in free)
                for v in POOL:
                    if v == mp[t] or use[v] >= CAP[v]: continue
                    old = mp[t]; mp[t] = v; s = score(runs, mp); mp[t] = old
                    if s > bs + 1e-9: bv, bs = v, s
                if bv != mp[t]: mp[t] = bv; cur = bs; improved = True
        if cur > best[0]: best = (cur, dict(mp))
    return best
def synthetic(runs, seed):
    """Italian plaintext cut into pool units, units mapped to the same number of types with the real type frequencies."""
    rnd = random.Random(seed); cnt = collections.Counter(t for r in runs for t in r); types = list(cnt)
    text = open('lang/corpora/it-quattrocento-tuscan.txt', encoding='utf8', errors='ignore').read()
    text = lm.norm(text[:400000], 'early')
    while True:   # a clean stretch of the corpus (the scan has OCR junk)
        i = rnd.randrange(len(text) - 6000); cut = text[i:i + 6000]
        if m.per_char(cut.replace(' ', '')) > -2.2: break
    text = cut
    units = []; j = 0; byl = sorted(POOL, key=lambda x: -len(x))
    while j < len(text):
        for u in byl:
            if text.startswith(u, j) and (len(u) == 1 or rnd.random() < 0.35): units.append(u); j += len(u); break
        else: j += 1
    ucnt = collections.Counter(units); keep = [u for u, _ in ucnt.most_common(len(types))]
    # the real frequency profile: the k-th most frequent type is the k-th most frequent unit
    tmap = {u: t for u, t in zip(keep, [t for t, _ in cnt.most_common()])}
    stream = [tmap[u] for u in units if u in tmap]
    out = []; k = 0
    for r in runs: out.append(stream[k:k + len(r)]); k += len(r)
    truth = {t: u for u, t in tmap.items()}
    return out, truth
if __name__ == '__main__':
    R = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    runs = load_runs('targets/tranchedini1446/texts/f139_runs.txt')
    s, mp = solve(runs, FIXED, R, 1)
    print('real runs: score', round(s, 3)); print({t: v for t, v in sorted(mp.items())})
    flat = [t for r in runs for t in r]; random.Random(2).shuffle(flat); k = 0; sh = []
    for r in runs: sh.append(flat[k:k + len(r)]); k += len(r)
    s2, _ = solve(sh, FIXED, R, 1); print('order shuffled: score', round(s2, 3))
    syn, truth = synthetic(runs, 3)
    s3, mp3 = solve(syn, {}, R, 1)
    ok = sum(1 for t in truth if mp3.get(t) == truth[t]); tokens = sum(1 for r in syn for t in r if mp3.get(t) == truth.get(t))
    print('synthetic: score', round(s3, 3), 'types recovered', ok, '/', len(truth), 'tokens', tokens, '/', sum(map(len, syn)),
          'score of true key', round(score(syn, truth), 3))
