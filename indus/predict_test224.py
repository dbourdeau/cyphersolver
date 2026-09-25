"""Two-hundred-and-twenty-fourth registered prediction set (PREDICTIONS.md, WD1-WD3): decipherment loop 49, forward weight
0.7 against equal weights in the two-direction SIGN task. Writes results/predict_test224.md."""
from collections import Counter

import rtools as R
from famlm import M3, fit3
from prizebench import _lp
from progress import MODEL, data
from signs import load


def sign_w(tr, te, keys, weights=(0.5, 0.7), ncand=150):
    wf, _ = fit3(tr, keys)
    mf = M3(tr)
    rtr = [tuple(reversed(t)) for t in tr]
    wb, _ = fit3(rtr, keys)
    mb = M3(rtr)
    cands = [g for g, n in Counter(g for t in tr for g in t).most_common(ncand)]
    hits = Counter()
    n = 0
    for t in te:
        for i, g in enumerate(t):
            sf = {c: _lp(mf, t[:i] + (c,) + t[i + 1:], wf) for c in cands}
            sb = {c: _lp(mb, tuple(reversed(t[:i] + (c,) + t[i + 1:])), wb) for c in cands}
            for a in weights:
                hits[a] += max(cands, key=lambda c: a * sf[c] + (1 - a) * sb[c]) == g
            n += 1
    return {a: hits[a] / n for a in weights}, n


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-twenty-fourth registered predictions: decipherment loop 49, direction weights in SIGN', 'predict_test224')
    DL, tr, te = data()
    r, n = sign_w(tr, te, MODEL['keys'])
    rd.rec('WD1', 'weight 0.7 beats equal weights (fixed test)', 'top-1 equal %.1f%%, 0.7 %.1f%% (%d signs)' % (100 * r[0.5], 100 * r[0.7], n), r[0.7] - r[0.5] >= 0.003)
    DA = sorted({tuple(t) for t in A})
    DBx = sorted({tuple(ln) for r_ in load(only_m77=True) for ln in r_['seq'] if ln} - set(DA))[:300]
    q, m = sign_w(DA, DBx, MODEL['keys'])
    rd.rec('WD2', 'and A -> B', 'top-1 equal %.1f%%, 0.7 %.1f%% (%d signs)' % (100 * q[0.5], 100 * q[0.7], m), q[0.7] > q[0.5])
    rd.rec('WD3', 'progress rule', 'WD1 %s, WD2 %s' % (r[0.7] - r[0.5] >= 0.003, q[0.7] > q[0.5]), r[0.7] - r[0.5] >= 0.003 and q[0.7] > q[0.5])
    rd.finish()


if __name__ == '__main__':
    main()
