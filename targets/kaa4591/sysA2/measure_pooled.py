"""measure2.py with the pooled key: a word counts as read when it has no '?' and every sign under it takes a value
that sign takes at least 5% of the time and at least twice in the pooled hand readings of all the System A' letters
(R9407, R9408, R9409, R9410 both letters, R9413, R9427), since the letters share one key with per-hand variants.
  python measure_pooled.py REC        (REC in r9408 r9409 r9410 r9410b r9413 r9427)
"""
import io, os, runpy, sys, contextlib
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
PAIRS = {'r9408': '../r9408/reading.txt', 'r9409': '../r9409/reading.txt', 'r9410': '../r9410/reading.txt',
         'r9410b': '../r9410/reading_p3p6.txt', 'r9413': '../r9413/reading.txt', 'r9427': '../r9427/reading.txt',
         'r9407': 'r9407_reading_fg.txt'}
def run(rec):
    sys.argv = ['measure2.py', os.path.join(HERE, rec + '.tok'), os.path.join(HERE, PAIRS[rec])]
    with contextlib.redirect_stdout(io.StringIO()):
        return runpy.run_path(os.path.join(HERE, 'measure2.py'))
recs = sys.argv[1:] or [r for r in PAIRS if r != 'r9407']
G = {r: run(r) for r in PAIRS}
POOL = defaultdict(Counter)
for r in PAIRS:
    if (r == 'r9410b') == False:
        for s, c in G[r]['P'].items(): POOL[s].update(c)
LATIN = defaultdict(Counter)
for s, c in G['r9410b']['P'].items(): LATIN[s].update(c)
for rec in recs:
    g = G[rec]; P = POOL if rec != 'r9410b' else LATIN
    if rec == 'r9410b':                       # the Latin letter: its own counts plus the German pool for shared signs
        P = defaultdict(Counter, {s: Counter(c) for s, c in POOL.items()})
        for s, c in LATIN.items(): P[s].update(c)
    _, T, R = g['data'][0]
    good = tot = 0
    for no, r in R.items():
        ws = g['words_of'](r); real = [(w, d) for w, d in ws if w]
        tot += len(ws)
        al = g['align'](T[no], real, P) if real else None
        if al is None: continue
        ok = [not d for _, d in real]
        for gg, v, wi in al:
            c = P.get(gg, Counter()); N = sum(c.values()) or 1
            if N > 3 and (c.get(v, 0) < 2 or c.get(v, 0) / N < 0.05): ok[wi] = False
        good += sum(ok)
    print(f'{rec}: pooled-key measure {good}/{tot} = {good / max(tot, 1):.3f}')
