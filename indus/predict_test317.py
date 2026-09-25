"""Three-hundred-and-seventeenth registered prediction set (PREDICTIONS.md, WP1-WP3): decipherment loop 142, the WORD
task with the two-direction scorer (set 274) plus a body-frequency prior: score = forward + backward log-probability +
beta * log(1 + training count of the body); beta chosen on a development split of the training lines (famlm split) from
0, 0.5, 1, 2, then applied once to the fixed test lines. Writes results/predict_test317.md."""
import math
from collections import Counter

import rtools as R
from famlm import M3, fit3
from predict_test122 import split
from prizebench import _lp
from progress import MODEL, data

BETAS = (0.0, 0.5, 1.0, 2.0)


def nb(t):
    nm = R.name_of(list(t))
    return tuple(nm[0]) if nm and nm[0] else None


def run(tr, te):
    keys = MODEL['keys']
    w, _ = fit3(tr, keys)
    m = M3(tr)
    rtr = [tuple(reversed(x)) for x in tr]
    wb, _ = fit3(rtr, keys)
    mb = M3(rtr)
    bodies = Counter(nb(t) for t in tr if nb(t))
    cands = [b for b, c in bodies.most_common()]
    rows = []
    for t in te:
        b = nb(t)
        if not b:
            continue
        j = next((j for j in range(len(t) - len(b) + 1) if tuple(t[j:j + len(b)]) == b), None)
        if j is None:
            continue
        pre, post = tuple(t[:j]), tuple(t[j + len(b):])
        base = {c: _lp(m, pre + c + post, w) + _lp(mb, tuple(reversed(pre + c + post)), wb) for c in cands}
        rows.append((b, base, bodies))
    return rows


def top10(rows, beta):
    hits = 0
    for b, base, bodies in rows:
        sc = sorted(base, key=lambda c: (-(base[c] + beta * math.log(1 + bodies[c])), c))
        hits += b in sc[:10]
    return hits


def main():
    rd = R.Round('Three-hundred-and-seventeenth registered predictions: decipherment loop 142, WORD with a body-frequency prior', 'predict_test317')
    DL, tr, te = data()
    itr, dv = split(tr)
    drows = run(list(itr), list(dv))
    dev = {b: top10(drows, b) for b in BETAS}
    best = max(BETAS, key=lambda b: (dev[b], -b))
    rd.say('- development split (%d names): %s; beta chosen %.1f.' % (len(drows), ', '.join('%.1f: %d' % kv for kv in dev.items()), best))
    rows = run(tr, te)
    n = len(rows)
    t0, t1 = top10(rows, 0.0), top10(rows, best)
    rd.say('- test: %d names; two-direction top-10 %d, with prior %d.' % (n, t0, t1))
    rd.say()
    rd.rec('WP1', 'WORD top-10 1 point or more above the one-direction bench figure (3.4%)', '%.1f%%' % (100 * t1 / n), t1 / n - 0.034 >= 0.01)
    rd.rec('WP2', 'the prior takes weight on the development split (beta > 0)', 'beta %.1f' % best, best > 0)
    rd.rec('WP3', 'progress rule: WP1 (the WORD task then uses this scorer)', 'top-10 %.1f%%' % (100 * t1 / n), t1 / n - 0.034 >= 0.01)
    rd.finish()


if __name__ == '__main__':
    main()
