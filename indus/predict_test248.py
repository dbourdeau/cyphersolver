"""Two-hundred-and-forty-eighth registered prediction set (PREDICTIONS.md, GP1-GP3): decipherment loop 73, a grammar prior
(lambda = 2 bits if the line parses, grammar.parse5) in the two-direction SIGN task. Writes results/predict_test248.md."""
from collections import Counter

import grammar as G
import rtools as R
from famlm import M3, fit3
from predict_test108 import genre
from predict_test215 import slots
from prizebench import _lp
from progress import MODEL, data
from signs import load


def sign_g(tr, te, keys, lam=2.0, ncand=150):
    H = G.heads_from(tr)
    hc, mc = G.head_stats(tr)
    labels = {g for g, v in Counter(s[0] for s in (slots(t) for t in tr if genre(t) == 'count') if s).most_common(10)}
    wf, _ = fit3(tr, keys)
    mf = M3(tr)
    rtr = [tuple(reversed(t)) for t in tr]
    wb, _ = fit3(rtr, keys)
    mb = M3(rtr)
    cands = [g for g, n in Counter(g for t in tr for g in t).most_common(ncand)]
    h0 = h1 = n = 0
    for t in te:
        for i, g in enumerate(t):
            sc = {}
            for c in cands:
                u = t[:i] + (c,) + t[i + 1:]
                sc[c] = (_lp(mf, u, wf) + _lp(mb, tuple(reversed(u)), wb), G.parse5(u, H, hc, mc, labels) is not None)
            h0 += max(cands, key=lambda c: sc[c][0]) == g
            h1 += max(cands, key=lambda c: sc[c][0] + lam * sc[c][1]) == g
            n += 1
    return h0 / n, h1 / n, n


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-forty-eighth registered predictions: decipherment loop 73, the grammar as a prior in SIGN', 'predict_test248')
    DL, tr, te = data()
    a0, a1, n = sign_g(tr, te, MODEL['keys'])
    rd.rec('GP1', 'grammar prior raises SIGN (fixed test)', 'top-1 %.1f%% -> %.1f%% (%d signs)' % (100 * a0, 100 * a1, n), a1 - a0 >= 0.003)
    DA = sorted({tuple(t) for t in A})
    DBx = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))[:300]
    b0, b1, m = sign_g(DA, DBx, MODEL['keys'])
    rd.rec('GP2', 'and A -> B', 'top-1 %.1f%% -> %.1f%% (%d signs)' % (100 * b0, 100 * b1, m), b1 > b0)
    rd.rec('GP3', 'progress rule', 'GP1 %s, GP2 %s' % (a1 - a0 >= 0.003, b1 > b0), a1 - a0 >= 0.003 and b1 > b0)
    rd.finish()


if __name__ == '__main__':
    main()
