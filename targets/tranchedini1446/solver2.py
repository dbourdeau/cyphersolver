"""Constrained solver for f. 139 on the agents' labelled transcription (texts/f139_A.md, f139_B.md).
Labels that match the Domnina/Lasry table keep the table value (the letters of the table fit f. 139: see table_test.py);
labels with two candidates (pe/de) and unmatched shapes (@NN, ?) are free. Runs are cut at every clear word.
Score: mean log-probability per letter of the concatenated decoded runs under it-cinquecento without spaces.
Controls: (a) token order shuffled, (b) held-out table labels: free the k most frequent matched labels, see whether the solver
restores their table values. Run from the repository root: python targets/tranchedini1446/solver2.py"""
import os, re, sys, random, collections
sys.path.insert(0, os.getcwd())
from lang import lm
m = lm.load('it-cinquecento', order=5, spaces=False)
WORD = {'NON': 'non', 'VENEZIANI': 'DUCA', 'CON': 'con', 'ET': 'et', 'IN': 'in', 'CHE': 'che', 'CONTE': 'conte', 'SFORZA': 'FIOR', 'PER': 'per'}
SYL = 'ce ci co de du fa li lo me mi na ne no pi re ri ro si ta te to pe sa ma tu fo nu da le pa do'.split()
LET = list('abcdefghilmnopqrstuz')
DBL = ['ss', 'ee', 'll', 'tt']
POOL = LET + SYL + DBL
SYMAP = {'s2': 's', 's3': 's', 's4': 's', 'ss/s3': 'ss'}
def base(t): return t.rstrip('?').replace("'", '').replace('"', '')
def val(t):
    t = base(t)
    if t in WORD: return WORD[t]
    t = SYMAP.get(t, t)
    return t if t in POOL else None
def cands(tok):
    """None = fixed value; list = candidate values for a free type."""
    alts = [base(x) for x in tok.split('/')]
    vs = [val(x) for x in alts]
    if len(alts) == 1 and vs[0] and not tok.endswith('?'): return vs[0], None
    if len(alts) > 1 and all(vs): return None, sorted(set(vs))
    return None, POOL
def load_runs():
    runs = []
    for f in ('f139_A.md', 'f139_B.md'):
        for ln in open('targets/tranchedini1446/texts/' + f, encoding='utf8'):
            if not re.match(r'L\d+:', ln): continue
            cur = []
            for w in ln.split()[1:]:
                mt = re.fullmatch(r'<(.+)>', w)
                if mt: cur.append(mt.group(1))
                else:
                    if cur: runs.append(cur)
                    cur = []
            if cur: runs.append(cur)
    return [r for r in runs if len(r) >= 2]
def build(runs):
    fixed, free = {}, {}
    for r in runs:
        for t in r:
            v, c = cands(t)
            if c is None and v is not None: fixed[t] = v
            elif c is not None and t != '?': free[t] = c
    return fixed, {t: c for t, c in free.items() if t not in fixed}
def score(runs, mp):
    return m.per_char(''.join(mp.get(t, '') for r in runs for t in r if True))
def solve(runs, fixed, free, restarts=6, seed=1):
    rnd = random.Random(seed); best = (-99, None); ft = list(free)
    for _ in range(restarts):
        mp = dict(fixed); mp.update({t: rnd.choice(free[t]) for t in ft}); mp['?'] = ''
        cur = score(runs, mp); imp = True
        while imp:
            imp = False; rnd.shuffle(ft)
            for t in ft:
                bv, bs = mp[t], cur
                for v in free[t]:
                    if v == mp[t]: continue
                    old = mp[t]; mp[t] = v; s = score(runs, mp); mp[t] = old
                    if s > bs + 1e-9: bv, bs = v, s
                if bv != mp[t]: mp[t] = bv; cur = bs; imp = True
        if cur > best[0]: best = (cur, dict(mp))
    return best
if __name__ == '__main__':
    runs = load_runs(); fixed, free = build(runs)
    ntok = sum(map(len, runs)); nf = sum(1 for r in runs for t in r if t in fixed)
    print(len(runs), 'runs', ntok, 'tokens;', nf, 'fixed tokens,', len(fixed), 'fixed types;', len(free), 'free types')
    s0 = score(runs, dict(fixed, **{t: free[t][0] for t in free}, **{'?': ''}))
    s, mp = solve(runs, fixed, free); print('real: start', round(s0, 3), 'solved', round(s, 3))
    print('free values:', {t: mp[t] for t in sorted(free, key=lambda t: -sum(r.count(t) for r in runs))[:40]})
    flat = [t for r in runs for t in r]; res = []
    for sd in range(3):
        random.Random(sd).shuffle(flat); k = 0; sh = []
        for r in runs: sh.append(flat[k:k + len(r)]); k += len(r)
        f2, fr2 = build(sh); s2, _ = solve(sh, f2, fr2, 4, sd); res.append(round(s2, 3))
    print('order-shuffled controls (same labels, same constraints):', res)
    # held-out: free the most frequent matched labels
    cnt = collections.Counter(t for r in runs for t in r if t in fixed)
    for k in (5, 10):
        top = [t for t, _ in cnt.most_common() if t not in WORD.values() and t not in WORD][:k]
        f3 = {t: v for t, v in fixed.items() if t not in top}; fr3 = dict(free); fr3.update({t: POOL for t in top})
        s3, mp3 = solve(runs, f3, fr3, 6, 5)
        rec = sum(1 for t in top if mp3[t] == fixed[t])
        print(f'held out {k} frequent labels:', [(t, fixed[t], mp3[t]) for t in top], 'recovered', rec, '/', k, 'score', round(s3, 3))
