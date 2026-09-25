"""Two-hundred-and-eighty-sixth registered prediction set (PREDICTIONS.md, DX1-DX4): decipherment loop 111, the damaged
texts' legible runs (sample D, damaged.py) as extra training text. A run with a cut start is prefixed with the
pseudo-sign '<cut>', a run with a cut end is followed by '<cutend>', so the runs add interior contexts without teaching
false line starts or ends. Test lines unchanged. Writes results/predict_test286.md."""
from collections import Counter

import rtools as R
from damaged import segments
from famlm import M3, fit3, score3
from prizebench import _lp
from progress import MODEL, data
from signs import load


def runs(exclude=()):
    ex = set(exclude)
    out = []
    for s in segments():
        t = tuple(s['signs'])
        if t in ex:
            continue
        out.append((('<cut>',) if s['open_start'] else ()) + t + (('<cutend>',) if s['open_end'] else ()))
    return out


def sign_top1(train, test, cand_from, ncand=150):
    keys = MODEL['keys']
    w, _ = fit3(train, keys)
    m = M3(train)
    rtr = [tuple(reversed(x)) for x in train]
    wb, _ = fit3(rtr, keys)
    mb = M3(rtr)
    cands = [g for g, c in Counter(g for t in cand_from for g in t).most_common(ncand)]
    top = n = 0
    for t in test:
        t = tuple(t)
        for i, g in enumerate(t):
            best = max(cands, key=lambda c: (_lp(m, t[:i] + (c,) + t[i + 1:], w) + _lp(mb, tuple(reversed(t[:i] + (c,) + t[i + 1:])), wb), c))
            n += 1
            top += best == g
    return top / n


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-eighty-sixth registered predictions: decipherment loop 111, damaged-text runs as extra training text', 'predict_test286')
    DL, tr, te = data()
    D = runs(exclude=te)
    rd.say('- %d runs, %d signs added to %d training lines.' % (len(D), sum(len([g for g in t if not g.startswith('<')]) for t in D), len(tr)))
    s0, _ = score3(tr, te, MODEL['keys'])
    s1, _ = score3(tr + D, te, MODEL['keys'])
    rd.rec('DX1', 'S on the fixed test falls by 0.005 bits or more', 'S %.4f -> %.4f (gain %.4f)' % (s0, s1, s0 - s1), s0 - s1 >= 0.005)
    DA = sorted({tuple(t) for t in A})
    DBx = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    b0, _ = score3(DA, DBx, MODEL['keys'])
    b1, _ = score3(DA + runs(exclude=DBx), DBx, MODEL['keys'])
    rd.rec('DX2', 'and A -> B', '%.4f -> %.4f (gain %.4f)' % (b0, b1, b0 - b1), b1 < b0)
    a1 = sign_top1(tr, te, tr)
    c1 = sign_top1(tr + D, te, tr)
    rd.rec('DX3', 'SIGN top-1 does not fall', 'before %.1f%%, after %.1f%%' % (100 * a1, 100 * c1), c1 >= a1)
    ok = s0 - s1 >= 0.005 and b1 < b0 and c1 >= a1
    rd.rec('DX4', 'progress rule: DX1, DX2 and DX3', 'DX1 %s, DX2 %s, DX3 %s' % (s0 - s1 >= 0.005, b1 < b0, c1 >= a1), ok)
    rd.finish()


if __name__ == '__main__':
    main()
