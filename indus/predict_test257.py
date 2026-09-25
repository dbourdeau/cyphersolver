"""Two-hundred-and-fifty-seventh registered prediction set (PREDICTIONS.md, IF1-IF4): decipherment loop 82, an infill
component for the SIGN task. The hidden sign is scored by the two-direction model (set 204) plus alpha * log p(c | left
neighbour, right neighbour), the infill probability counted on the training lines (line edges as neighbours) and
smoothed toward the sign's frequency. alpha is chosen on a development split of the training lines only (famlm.split),
then applied once to the fixed test lines. Writes results/predict_test257.md."""
import math
from collections import Counter, defaultdict

import rtools as R
from famlm import M3, fit3, split
from prizebench import _lp
from progress import MODEL, data

ALPHAS = (0.0, 0.25, 0.5, 1.0, 1.5, 2.0, 3.0)
BETA = 1.0


def table(tr):
    tri = defaultdict(Counter)
    for t in tr:
        s = ('<s>',) + tuple(t) + ('</s>',)
        for i in range(1, len(s) - 1):
            tri[(s[i - 1], s[i + 1])][s[i]] += 1
    return tri


def scores(tr, te, ncand=150):
    """Per test position: (true sign, two-direction scores, infill log-probs) over the candidates."""
    keys = MODEL['keys']
    w, _ = fit3(tr, keys)
    m = M3(tr)
    rtr = [tuple(reversed(x)) for x in tr]
    wb, _ = fit3(rtr, keys)
    mb = M3(rtr)
    freq = Counter(g for t in tr for g in t)
    tot = sum(freq.values())
    cands = [g for g, n in freq.most_common(ncand)]
    tri = table(tr)
    out = []
    for t in te:
        s = ('<s>',) + tuple(t) + ('</s>',)
        for i, g in enumerate(t):
            base = [_lp(m, t[:i] + (c,) + t[i + 1:], w) + _lp(mb, tuple(reversed(t[:i] + (c,) + t[i + 1:])), wb) for c in cands]
            ctx = tri[(s[i], s[i + 2])]
            n = sum(ctx.values())
            inf = [math.log((ctx[c] + BETA * freq[c] / tot) / (n + BETA)) for c in cands]
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
    rd = R.Round('Two-hundred-and-fifty-seventh registered predictions: decipherment loop 82, an infill component for the SIGN task', 'predict_test257')
    DL, tr, te = data()
    itr, dv = split(tr)
    drows = scores(list(itr), list(dv))
    dev = {a: evaluate(drows, a) for a in ALPHAS}
    best = max(ALPHAS, key=lambda a: (dev[a][0], dev[a][1], -a))
    rd.say('- development split: %s; alpha chosen %.2f.' % ('; '.join('%.2f: %.1f%% / %.1f%%' % (a, 100 * v[0], 100 * v[1]) for a, v in dev.items()), best))
    rows = scores(tr, te)
    b1, b5 = evaluate(rows, 0.0)
    n1, n5 = evaluate(rows, best)
    rd.say('- test (%d signs): two-direction %.1f%% / %.1f%%; with infill %.1f%% / %.1f%%.' % (len(rows), 100 * b1, 100 * b5, 100 * n1, 100 * n5))
    rd.say()
    rd.rec('IF1', 'SIGN top-1 rises by 0.5 point or more', '%.1f%% -> %.1f%%' % (100 * b1, 100 * n1), n1 - b1 >= 0.005)
    rd.rec('IF2', 'SIGN top-5 does not fall', '%.1f%% -> %.1f%%' % (100 * b5, 100 * n5), n5 >= b5)
    rd.rec('IF3', 'the development split gives the infill weight (alpha > 0)', 'alpha %.2f' % best, best > 0)
    rd.rec('IF4', 'progress rule: IF1 and IF2', 'SIGN %.1f%% / %.1f%%' % (100 * n1, 100 * n5), n1 - b1 >= 0.005 and n5 >= b5)
    rd.finish()


if __name__ == '__main__':
    main()
