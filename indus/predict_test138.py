"""Hundred-and-thirty-eighth registered prediction set (PREDICTIONS.md, PA1-PA10): Parpola's, Mahadevan's and
Knorozov's structural claims (from the OCR text of Parpola 1994). Writes results/predict_test138.md."""
from collections import Counter

import predict_test13 as T
import rtools as R
from predict_test112 import runs
from signs import FISH

HEAD = ('817', '820', '861')
ROOF = ('235', '236')


def fish_counts(lines):
    out = []
    for t in lines:
        for i, j, r in runs(t):
            if j < len(t) and t[j] in FISH and not (i > 0 and t[i - 1] in HEAD):
                out.append((sum(R.NUMS[g][0] for g in r), t[j], t))
    return out


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round("Hundred-and-thirty-eighth registered predictions: Parpola's, Mahadevan's and Knorozov's structural claims", 'predict_test138')
    DL = sorted({tuple(t) for t in AB})
    fc = fish_counts(DL)
    vc = Counter(v for v, f, t in fc)
    rd.say('- numeral + fish (not after a heading), distinct lines: %d; values %s.' % (len(fc), dict(vc.most_common(8))))
    rd.say()
    top = vc.most_common(2)
    rd.rec('PA1', "'6 + fish' is the commonest", 'commonest value %s' % (top[0],), top[0][0] == 6)
    rd.rec('PA2', "'3 + fish' is next", 'second value %s' % (top[1],), len(top) > 1 and top[1][0] == 3)
    solo = [(r['sealid'], ln) for r in F for ln in r['seq'] if len(ln) == 2 and ln[0] in R.NUMS and R.NUMS[ln[0]][0] == 7 and ln[1] in FISH
            and len([x for x in r['seq'] if x]) == 1]
    rd.rec('PA3', "a seal says just '7 + fish'", 'objects: %d (%s)' % (len(solo), '; '.join('%s %s' % (s, ' '.join(l)) for s, l in solo[:5])), len(solo) >= 1)
    dbl = sum(1 for t in DL if any(x == y and x in FISH for x, y in zip(t, t[1:])))
    rd.rec('PA4', 'fish doubled', 'distinct lines with a doubled fish: %d; threshold 5' % dbl, dbl >= 5)
    ns = sorted({(b, e) for b, e in T.names(AB) if b})
    x = []
    for b, e in ns:
        ni = [i for i, g in enumerate(b) if g in R.NUMS]
        fi = [i for i, g in enumerate(b) if g in FISH]
        if ni and fi and any(f > n for n in ni for f in fi):
            x.append(any(b[i + 1] in FISH for i in ni if i + 1 < len(b)))
    rd.thr('PA5', 'number and fish belong together', 'bodies with the numeral directly before a fish', sum(x), len(x), 0.9)
    FD = sorted({(r['type'][:3], tuple(ln)) for r in F if r['type'] != 'TAB:C' for ln in r['seq'] if ln})
    fin7 = lambda t: [i == len(t) - 1 or (i == len(t) - 2 and t[-1] in ('400', '90', '151')) for i, g in enumerate(t) if g == '740']
    rd.gtl('PA6', 'the jar ends seal texts', 'line-final 740, seals', [v for ty, t in FD if ty == 'SEA' for v in fin7(t)], [v for ty, t in FD if ty == 'TAB' for v in fin7(t)])
    bodies = {b for b, e in ns}
    b3 = [b for b in bodies if len(b) >= 3]
    rd.thr('PA7', 'prefixed signs are optional', 'bodies of 3+ whose tail is attested', sum(b[1:] in bodies for b in b3), len(b3), 0.3)
    one = [(t, i) for t in DL for i in range(1, len(t)) if t[i] == '1' and t[i - 1] == '740']
    rd.thr('PA8', 'the stroke after the jar is final', "'740 1' with the line ending within one more sign", sum(len(t) - 1 - i <= 1 for t, i in one), len(one), 0.5)
    hd = lambda g: [b[-1] == g for b, e in ns if g in b]
    a = [b[-1] in ROOF for b, e in ns if any(x_ in ROOF for x_ in b)]
    c = [b[-1] == '220' for b, e in ns if '220' in b]
    p = min(1, 2 * min(R.hyper_ge(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c)), R.fisher_less(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c))))
    rd.rec('PA9', 'the roof fish is a word like the fish', 'head, roof fish %s' % R.fl(sum(a), len(a), sum(c), len(c), p),
           p >= 0.05 or sum(a) / max(1, len(a)) > sum(c) / max(1, len(c)))
    FL = sorted({t for ty, t in FD})
    ff = fish_counts(FL)
    rd.thr('PA10', 'six and seven are the star counts', 'counted fish worth 6 or 7 in F (%s)' % dict(Counter(v for v, f, t in ff).most_common(6)),
           sum(v in (6, 7) for v, f, t in ff), len(ff), 0.2)
    rd.finish()


if __name__ == '__main__':
    main()
