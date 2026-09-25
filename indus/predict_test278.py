"""Two-hundred-and-seventy-eighth registered prediction set (PREDICTIONS.md, SE1-SE3): decipherment loop 103, a SIGN
ensemble over two family maps. The two-direction SIGN score (set 204) is computed with the decade-block families (M3)
and with Parpola's description families (descfam, set 208), and the two scores are averaged with equal weight.
Writes results/predict_test278.md."""
from collections import Counter

import rtools as R
from descfam import families
from famlm import M3, fit3, with_fam
from prizebench import _lp
from progress import MODEL, data


def scorer(tr, cls):
    keys = MODEL['keys']
    w, _ = fit3(tr, keys, cls=cls)
    m = cls(tr)
    rtr = [tuple(reversed(x)) for x in tr]
    wb, _ = fit3(rtr, keys, cls=cls)
    mb = cls(rtr)
    return lambda t: _lp(m, t, w) + _lp(mb, tuple(reversed(t)), wb)


def main():
    rd = R.Round('Two-hundred-and-seventy-eighth registered predictions: decipherment loop 103, a SIGN ensemble over two family maps', 'predict_test278')
    DL, tr, te = data()
    fams = families()
    dfam = lambda g: fams.get(g, g)
    s1 = scorer(tr, M3)
    s2 = scorer(tr, with_fam(dfam))
    freq = Counter(g for t in tr for g in t)
    cands = [g for g, c in freq.most_common(150)]
    a1 = a5 = b1 = b5 = n = 0
    for t in te:
        t = tuple(t)
        for i, g in enumerate(t):
            x = {c: s1(t[:i] + (c,) + t[i + 1:]) for c in cands}
            y = {c: s2(t[:i] + (c,) + t[i + 1:]) for c in cands}
            r1 = sorted(cands, key=lambda c: (-x[c], c))
            r2 = sorted(cands, key=lambda c: (-(x[c] + y[c]), c))
            n += 1
            a1 += r1[0] == g
            a5 += g in r1[:5]
            b1 += r2[0] == g
            b5 += g in r2[:5]
    rd.say('- %d test signs; decade families %.1f%% / %.1f%%; ensemble %.1f%% / %.1f%%.' % (n, 100 * a1 / n, 100 * a5 / n, 100 * b1 / n, 100 * b5 / n))
    rd.say()
    rd.rec('SE1', 'SIGN top-1 rises by 0.5 point or more', '%.1f%% -> %.1f%%' % (100 * a1 / n, 100 * b1 / n), b1 - a1 >= 0.005 * n)
    rd.rec('SE2', 'SIGN top-5 does not fall', '%.1f%% -> %.1f%%' % (100 * a5 / n, 100 * b5 / n), b5 >= a5)
    rd.rec('SE3', 'progress rule: SE1 and SE2', 'SIGN %.1f%% / %.1f%%' % (100 * b1 / n, 100 * b5 / n), b1 - a1 >= 0.005 * n and b5 >= a5)
    rd.finish()


if __name__ == '__main__':
    main()
