"""Two-hundred-and-sixty-eighth registered prediction set (PREDICTIONS.md, GP1-GP4): decipherment loop 93, a grammar prior
for the SIGN task. Each candidate is scored by the two-direction model (set 204) plus alpha if the line it completes
parses under the grammar (parse11, frames learned from the training lines only). alpha is chosen on a development split
of the training lines, then applied once to the fixed test lines. Writes results/predict_test268.md."""
import math
from collections import Counter, defaultdict

import rtools as R
from famlm import M3, fit3, split
from prizebench import _lp
from progress import MODEL, data

ALPHAS = (0.0, 0.25, 0.5, 1.0, 1.5, 2.0, 3.0)


def grammar_of(tr):
    from grammar import head_stats, heads_from, lexical, parse11
    from predict_test108 import genre
    from predict_test215 import slots
    heads = heads_from(tr)
    hc, mc = head_stats(tr)
    labels = {g for g, v in Counter(sl[0] for sl in (slots(t) for t in tr if genre(t) == 'count') if sl).most_common(10)}
    occ = Counter(g for t in tr for g in t)
    hd = Counter(t[i - 1] for t in tr for i, g in enumerate(t) if g in R.END and i > 0)
    low = {g for g in occ if occ[g] >= 3 and hd[g] / occ[g] < 0.05 and lexical(g)}
    last, first = Counter(t[-1] for t in tr), Counter(t[0] for t in tr)
    endp = {g for g in occ if occ[g] >= 5 and last[g] / occ[g] >= 0.5 and lexical(g)}
    openp = {g for g in occ if occ[g] >= 5 and first[g] / occ[g] >= 0.5 and lexical(g)}
    return lambda t: parse11(t, heads, hc, mc, labels, low, endp, openp) is not None


def scores(tr, te, ncand=150):
    """Per test position: (true sign, two-direction scores, parse flags) over the candidates."""
    keys = MODEL['keys']
    w, _ = fit3(tr, keys)
    m = M3(tr)
    rtr = [tuple(reversed(x)) for x in tr]
    wb, _ = fit3(rtr, keys)
    mb = M3(rtr)
    freq = Counter(g for t in tr for g in t)
    cands = [g for g, n in freq.most_common(ncand)]
    ok = grammar_of([tuple(x) for x in tr])
    out = []
    for t in te:
        t = tuple(t)
        for i, g in enumerate(t):
            base = [_lp(m, t[:i] + (c,) + t[i + 1:], w) + _lp(mb, tuple(reversed(t[:i] + (c,) + t[i + 1:])), wb) for c in cands]
            inf = [1.0 if ok(t[:i] + (c,) + t[i + 1:]) else 0.0 for c in cands]
            out.append((g, cands, base, inf))
    return out


def evaluate(rows, a):
    t1 = t5 = 0
    for g, cands, base, inf in rows:
        sc = sorted(range(len(cands)), key=lambda k: -(base[k] + a * inf[k]))
        t1 += cands[sc[0]] == g
        t5 += g in [cands[k] for k in sc[:5]]
    return t1 / len(rows), t5 / len(rows)


def main():
    rd = R.Round('Two-hundred-and-sixty-eighth registered predictions: decipherment loop 93, a grammar prior for the SIGN task', 'predict_test268')
    DL, tr, te = data()
    itr, dv = split(tr)
    drows = scores(list(itr), list(dv))
    dev = {a: evaluate(drows, a) for a in ALPHAS}
    best = max(ALPHAS, key=lambda a: (dev[a][0], dev[a][1], -a))
    rd.say('- development split: %s; alpha chosen %.2f.' % ('; '.join('%.2f: %.1f%% / %.1f%%' % (a, 100 * v[0], 100 * v[1]) for a, v in dev.items()), best))
    rows = scores(tr, te)
    b1, b5 = evaluate(rows, 0.0)
    n1, n5 = evaluate(rows, best)
    rd.say('- test (%d signs): two-direction %.1f%% / %.1f%%; with grammar prior %.1f%% / %.1f%%.' % (len(rows), 100 * b1, 100 * b5, 100 * n1, 100 * n5))
    rd.say()
    rd.rec('GP1', 'SIGN top-1 rises by 0.5 point or more', '%.1f%% -> %.1f%%' % (100 * b1, 100 * n1), n1 - b1 >= 0.005)
    rd.rec('GP2', 'SIGN top-5 does not fall', '%.1f%% -> %.1f%%' % (100 * b5, 100 * n5), n5 >= b5)
    rd.rec('GP3', 'the development split gives the grammar prior weight (alpha > 0)', 'alpha %.2f' % best, best > 0)
    rd.rec('GP4', 'progress rule: IF1 and IF2', 'SIGN %.1f%% / %.1f%%' % (100 * n1, 100 * n5), n1 - b1 >= 0.005 and n5 >= b5)
    rd.finish()


if __name__ == '__main__':
    main()
