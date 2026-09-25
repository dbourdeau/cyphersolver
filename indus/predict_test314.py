"""Three-hundred-and-fourteenth registered prediction set (PREDICTIONS.md, MT1-MT3): decipherment loop 139, the tier 3
restoration check on lines with two illegible signs. ICIT lines of 5+ signs with exactly two illegible signs whose
aligned M77 lines agree on two legible signs (at most one other mismatch in lines of 6+). For each, the two-direction
model is retrained without copies of the line (all positions but the two gaps agree, at most one mismatch, or the
line as a contiguous run) and the pair is chosen jointly over the 60 commonest signs; each gap sign is compared with
M77, against the context baseline of set 285 applied to each gap. Writes results/predict_test314.md."""
from collections import Counter

import icit_full
import rtools as R
from famlm import M3, fit3
from m77_gaps import DEFAULT, m77_lines
from predict_test285 import ctx_pred
from prizebench import _lp
from progress import MODEL, data


def copy2(t, ks, u):
    if len(u) == len(t) and sum(a != b for i, (a, b) in enumerate(zip(t, u)) if i not in ks) <= 1:
        return True
    n = len(t)
    return any(all(u[j + i] == t[i] for i in range(n) if i not in ks) for j in range(len(u) - n + 1))


def cases():
    R.load_all()
    icit_full.LINES_REVERSED = True
    L = m77_lines(DEFAULT)
    out = []
    for rec in icit_full.records(R.FPATH):
        for li, ln in enumerate(icit_full.lines_of(rec[34])):
            s = ln['signs']
            if len(s) < 5 or sum(g is None for g in s) != 2 or '?' in s:
                continue
            ks = [i for i, g in enumerate(s) if g is None]
            t = tuple('???' if g is None else g for g in s)
            vals = Counter(tuple(m[k] for k in ks) for mid, m in L if len(m) == len(t) and sum(a != b for j, (a, b) in enumerate(zip(t, m)) if j not in ks) <= (1 if len(t) >= 6 else 0))
            if len(vals) == 1 and all(v not in ('000', '?') for v in next(iter(vals))):
                out.append((rec[1] or rec[0], t, ks, next(iter(vals))))
    return out


def main():
    rd = R.Round('Three-hundred-and-fourteenth registered predictions: decipherment loop 139, restoration of lines with two illegible signs', 'predict_test314')
    DL, tr, te = data()
    keys = MODEL['keys']
    m1 = c1 = n = 0
    for cid, t, ks, gold in cases():
        train = [u for u in DL if not copy2(t, ks, u)]
        wf, _ = fit3(train, keys)
        mf = M3(train)
        rtr = [tuple(reversed(x)) for x in train]
        wb, _ = fit3(rtr, keys)
        mb = M3(rtr)
        cands = [g for g, c in Counter(g for x in train for g in x).most_common(60)]
        best, bs = None, None
        for a in cands:
            for b in cands:
                u = list(t)
                u[ks[0]], u[ks[1]] = a, b
                u = tuple(u)
                sc = _lp(mf, u, wf) + _lp(mb, tuple(reversed(u)), wb)
                if bs is None or sc > bs:
                    best, bs = (a, b), sc
        ctx = tuple(ctx_pred(train, t, k) for k in ks)
        for j in range(2):
            n += 1
            m1 += best[j] == gold[j]
            c1 += ctx[j] == gold[j]
        rd.say('- %s %s: M77 %s; model %s; context %s.' % (cid, ' '.join(t), ' '.join(gold), ' '.join(best), ' '.join(str(x) for x in ctx)))
    rd.say()
    rd.rec('MT1', 'model right on 25%+ of the gap signs (10+ signs)', '%d of %d' % (m1, n), n >= 10 and m1 >= 0.25 * n)
    rd.rec('MT2', 'model beats the context baseline', '%d against %d' % (m1, c1), m1 > c1)
    rd.rec('MT3', 'progress rule: MT1 and MT2 (the tier 3 restoration line gains these cases)', 'MT1 %s, MT2 %s' % (n >= 10 and m1 >= 0.25 * n, m1 > c1), n >= 10 and m1 >= 0.25 * n and m1 > c1)
    rd.finish()


if __name__ == '__main__':
    main()
