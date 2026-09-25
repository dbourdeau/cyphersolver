"""Two-hundred-and-eightieth registered prediction set (PREDICTIONS.md, TY1-TY4): decipherment loop 105, the object type
as context. Each line is prefixed with a pseudo-sign for its object class (seal, tablet, tag, pot, other; 'unk' where
the full ICIT records do not give one; a line on several classes takes its commonest), so the model's contexts at the
line start include the medium. The pseudo-sign itself is not scored. Writes results/predict_test280.md."""
import math
from collections import Counter, defaultdict

import rtools as R
from famlm import M3, fit3
from prizebench import _lp
from progress import MODEL, data
from signs import load


def tc(ty):
    return 'seal' if ty.startswith('SEAL') else 'tab' if ty.startswith('TAB') else 'tag' if ty.startswith('TAG') else 'pot' if ty.startswith('POT') else 'oth'


def type_map(F):
    m = defaultdict(Counter)
    for r in F:
        for ln in r['seq']:
            if ln:
                m[tuple(ln)][tc(r['type'])] += 1
    return lambda t: '<T:%s>' % (m[t].most_common(1)[0][0] if t in m else 'unk')


def bits(train, test, prefix):
    keys = MODEL['keys']
    tr = [((prefix(t),) + tuple(t)) if prefix else tuple(t) for t in train]
    te = [((prefix(t),) + tuple(t)) if prefix else tuple(t) for t in test]
    w, _ = fit3(tr, keys)
    m = M3(tr)
    tot = n = 0
    for t in te:
        rows = m.rows(t, True)[1:] if prefix else m.rows(t, True)
        for r in rows:
            tot += -math.log2(max(sum(w[k] * r[k] for k in w), 1e-12))
            n += 1
    return tot / n


def sign_top1(train, test, prefix, ncand=150):
    keys = MODEL['keys']
    tr = [((prefix(t),) + tuple(t)) if prefix else tuple(t) for t in train]
    w, _ = fit3(tr, keys)
    m = M3(tr)
    rtr = [tuple(reversed(x)) for x in tr]
    wb, _ = fit3(rtr, keys)
    mb = M3(rtr)
    freq = Counter(g for t in train for g in t)
    cands = [g for g, c in freq.most_common(ncand)]
    top = n = 0
    for t in test:
        t = tuple(t)
        p = (prefix(t),) if prefix else ()
        for i, g in enumerate(t):
            best = max(cands, key=lambda c: (_lp(m, p + t[:i] + (c,) + t[i + 1:], w) + _lp(mb, tuple(reversed(p + t[:i] + (c,) + t[i + 1:])), wb), c))
            n += 1
            top += best == g
    return top / n


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-eightieth registered predictions: decipherment loop 105, the object type as context', 'predict_test280')
    DL, tr, te = data()
    pre = type_map(F)
    rd.say('- classes of the test lines: %s.' % ', '.join('%s %d' % kv for kv in Counter(pre(tuple(t)) for t in te).most_common()))
    s0, s1 = bits(tr, te, None), bits(tr, te, pre)
    rd.rec('TY1', 'S on the fixed test falls by 0.005 bits or more', 'S %.4f -> %.4f (gain %.4f)' % (s0, s1, s0 - s1), s0 - s1 >= 0.005)
    DA = sorted({tuple(t) for t in A})
    DBx = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    b0, b1 = bits(DA, DBx, None), bits(DA, DBx, pre)
    rd.rec('TY2', 'and A -> B', '%.4f -> %.4f (gain %.4f)' % (b0, b1, b0 - b1), b1 < b0)
    a1, c1 = sign_top1(tr, te, None), sign_top1(tr, te, pre)
    rd.rec('TY3', 'SIGN top-1 does not fall', 'before %.1f%%, after %.1f%%' % (100 * a1, 100 * c1), c1 >= a1)
    ok = s0 - s1 >= 0.005 and b1 < b0 and c1 >= a1
    rd.rec('TY4', 'progress rule: TY1, TY2 and TY3', 'TY1 %s, TY2 %s, TY3 %s' % (s0 - s1 >= 0.005, b1 < b0, c1 >= a1), ok)
    rd.finish()


if __name__ == '__main__':
    main()
