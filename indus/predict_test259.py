"""Two-hundred-and-fifty-ninth registered prediction set (PREDICTIONS.md, AC1-AC4): decipherment loop 84, an anti-cache
for non-adjacent repeats. At each sign position (not the line end) the model's probability of a sign already written
earlier in the line, other than the immediately preceding sign, is multiplied by GAMMA and the distribution
renormalised (the mass of those signs computed at the same position with the line's length kept). GAMMA = 0.5 was
fixed in a design run on the training lines' own split (4.6772 -> 4.6736). Writes results/predict_test259.md."""
import math

import rtools as R
from famlm import M3, fit3
from prizebench import _lp
from progress import MODEL, data
from signs import load

GAMMA = 0.5


def score(train, test, gamma):
    w, _ = fit3(train, MODEL['keys'])
    m = M3(train)
    mix = lambda r: max(sum(w[k] * r[k] for k in w), 1e-12)
    tot = n = 0
    for t in test:
        t = tuple(t)
        rows = m.rows(t, True)
        for i in range(len(t) + 1):
            p = mix(rows[i])
            if i < len(t) and gamma != 1.0:
                rep = set(t[:max(0, i - 1)]) - ({t[i - 1]} if i >= 1 else set())
                if rep:
                    pr = sum(mix(m.rows(t[:i] + (v,) + t[i + 1:], True)[i]) for v in rep)
                    p = p * (gamma if t[i] in rep else 1.0) / (1 - (1 - gamma) * min(pr, 0.999))
            tot += -math.log2(p)
            n += 1
    return tot / n


def sign_task_ac(tr, te, gamma, ncand=150):
    from collections import Counter
    keys = MODEL['keys']
    w, _ = fit3(tr, keys)
    m = M3(tr)
    rtr = [tuple(reversed(x)) for x in tr]
    wb, _ = fit3(rtr, keys)
    mb = M3(rtr)
    freq = Counter(g for t in tr for g in t)
    cands = [g for g, c in freq.most_common(ncand)]
    top1 = n = 0
    for t in te:
        for i, g in enumerate(t):
            far = set(t[:max(0, i - 1)]) | set(t[i + 2:])
            sc = sorted(cands, key=lambda c: -(_lp(m, t[:i] + (c,) + t[i + 1:], w) + _lp(mb, tuple(reversed(t[:i] + (c,) + t[i + 1:])), wb)
                                               + (math.log(gamma) if c in far else 0.0)))
            n += 1
            top1 += sc[0] == g
    return top1 / n


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-fifty-ninth registered predictions: decipherment loop 84, an anti-cache for non-adjacent repeats', 'predict_test259')
    DL, tr, te = data()
    s0, s1 = score(tr, te, 1.0), score(tr, te, GAMMA)
    rd.rec('AC1', 'S on the fixed test falls by 0.002 bits or more', 'S %.4f -> %.4f (gain %.4f)' % (s0, s1, s0 - s1), s0 - s1 >= 0.002)
    DA = sorted({tuple(t) for t in A})
    DBx = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    b0, b1 = score(DA, DBx, 1.0), score(DA, DBx, GAMMA)
    rd.rec('AC2', 'and A -> B', '%.4f -> %.4f (gain %.4f)' % (b0, b1, b0 - b1), b1 < b0)
    a1, c1 = sign_task_ac(tr, te, 1.0), sign_task_ac(tr, te, GAMMA)
    rd.rec('AC3', 'SIGN top-1 does not fall', 'before %.1f%%, after %.1f%%' % (100 * a1, 100 * c1), c1 >= a1)
    ok = s0 - s1 >= 0.002 and b1 < b0 and c1 >= a1
    rd.rec('AC4', 'progress rule: AC1, AC2 and AC3', 'AC1 %s, AC2 %s, AC3 %s' % (s0 - s1 >= 0.002, b1 < b0, c1 >= a1), ok)
    rd.finish()


if __name__ == '__main__':
    main()
