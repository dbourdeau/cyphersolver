"""Crib search on the labelled runs of f. 139: where does a plausible word (from the clear text of f. 134/139 and Sforza's reply f. 147)
fit the decoded table values, an unmatched sign standing for 1-2 unknown letters? Compared with 300 order-shuffled copies of the runs.
Run from the repository root: python targets/tranchedini1446/cribs.py"""
import os, sys, random, statistics as st
sys.path.insert(0, os.getcwd()); sys.path.insert(0, 'targets/tranchedini1446')
import solver2 as S
runs = S.load_runs(); fixed, free = S.build(runs)
CRIBS = 'denaro danari stantie stantia cavalli cosimo fiorentini milanesi signoria soldati ducati fiorini montevarchi conte compagnie gente pace guerra duca'.split()
def val(t):
    v, c = S.cands(t)
    return v if v else None
def fits(run, w):
    """positions i where tokens i.. spell w: known token = exact letters, unknown = 1-2 letters; >= 3 exact letters and >= 60% exact"""
    vals = [val(t) for t in run]; hits = []
    def go(i, j, exact):
        if j == len(w): return exact
        if i == len(vals): return None
        v = vals[i]
        if v:
            return go(i + 1, j + len(v), exact + len(v)) if w.startswith(v, j) else None
        for k in (1, 2):
            if j + k <= len(w):
                r = go(i + 1, j + k, exact)
                if r is not None: return r
        return None
    for i in range(len(run)):
        e = go(i, 0, 0)
        if e is not None and e >= max(3, 0.6 * len(w)): hits.append(i)
    return hits
def count(rs):
    return {w: sum(len(fits(r, w)) for r in rs) for w in CRIBS}
real = count(runs)
flat = [t for r in runs for t in r]; ctrl = []
for s in range(300):
    random.Random(s).shuffle(flat); k = 0; sh = []
    for r in runs: sh.append(flat[k:k + len(r)]); k += len(r)
    ctrl.append(count(sh))
for w in CRIBS:
    c = [x[w] for x in ctrl]; mu, sd = st.mean(c), st.pstdev(c) or 1
    print(f'{w:12s} real {real[w]:2d}  shuffled {mu:5.2f} (sd {sd:4.2f})  z {(real[w]-mu)/sd:5.1f}')
for w in CRIBS:
    for r in runs:
        for i in fits(r, w): print(w, '|', ' '.join(r[max(0, i - 2):i + 8]))
