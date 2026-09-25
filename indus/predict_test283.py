"""Two-hundred-and-eighty-third registered prediction set (PREDICTIONS.md, MC1-MC4): decipherment loop 108, the M77
restoration check without copies. For each of set 282's 15 cases (gap lines of 4+ signs with an agreed legible M77
reading), the two-direction SIGN model is retrained on the distinct lines minus every copy of the gap line: a line of
the same length agreeing on all other positions but at most one, or a line containing the whole gap line (any sign in
the gap) as a contiguous run. Predictions are made and compared in this script, never printed before comparison.
Writes results/predict_test283.md."""
import csv
import os
from collections import Counter

import rtools as R
from famlm import M3, fit3
from prizebench import _lp
from progress import MODEL, data

HERE = os.path.dirname(os.path.abspath(__file__))


def copy_of(t, k, u):
    if len(u) == len(t) and sum(a != b for i, (a, b) in enumerate(zip(t, u)) if i != k) <= 1:
        return True
    n = len(t)
    for j in range(len(u) - n + 1):
        if all(u[j + i] == t[i] for i in range(n) if i != k):
            return True
    return False


def predict(train, t, k, cands):
    keys = MODEL['keys']
    wf, _ = fit3(train, keys)
    mf = M3(train)
    rtr = [tuple(reversed(x)) for x in train]
    wb, _ = fit3(rtr, keys)
    mb = M3(rtr)
    sc = {}
    for c in cands:
        u = t[:k] + (c,) + t[k + 1:]
        sc[c] = _lp(mf, u, wf) + _lp(mb, tuple(reversed(u)), wb)
    return sorted(cands, key=lambda c: (-sc[c], c))[:5]


def main():
    rd = R.Round('Two-hundred-and-eighty-third registered predictions: decipherment loop 108, the M77 restoration check without copies', 'predict_test283')
    DL, tr, te = data()
    with open(os.path.join(HERE, 'results', 'restoration_m77.tsv'), encoding='utf-8') as f:
        cases = [r for r in csv.DictReader(f, delimiter='\t') if r['reading'] not in ('no match', 'conflict', 'illegible') and len(r['text_with_gap'].split()) >= 4]
    top = Counter(g for x in DL for g in x).most_common(1)[0][0]
    h1 = h5 = hb = 0
    for r in cases:
        t = tuple(r['text_with_gap'].split())
        k = t.index('???')
        train = [u for u in DL if not copy_of(t, k, u)]
        cands = [g for g, n in Counter(g for x in train for g in x).most_common(150)]
        pred = predict(train, t, k, cands)
        g = r['reading']
        h1 += pred[0] == g
        h5 += g in pred
        hb += top == g
        rd.say('- %s %s: M77 %s; %d copies removed; predicted %s.' % (r['cisi'] or r['id'], r['text_with_gap'], g, len(DL) - len(train), ' '.join(pred)))
    n = len(cases)
    rd.say()
    rd.rec('MC1', 'top-1 matches the M77 reading in 25%+ of the 15 cases', '%d of %d' % (h1, n), n >= 10 and h1 >= 0.25 * n)
    rd.rec('MC2', 'top-5 contains it in 50%+', '%d of %d' % (h5, n), n >= 10 and h5 >= 0.5 * n)
    rd.rec('MC3', 'top-1 beats the frequency baseline (%s)' % top, 'top-1 %d against %d' % (h1, hb), n >= 10 and h1 > hb)
    rd.rec('MC4', 'progress rule: MC1 and MC3 (tier 3 gains its first line)', 'MC1 %s, MC3 %s' % (n >= 10 and h1 >= 0.25 * n, n >= 10 and h1 > hb), n >= 10 and h1 >= 0.25 * n and h1 > hb)
    rd.finish()


if __name__ == '__main__':
    main()
