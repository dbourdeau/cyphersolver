"""Hundred-and-twenty-first registered prediction set (PREDICTIONS.md, C5A-C5L): what else marks the 520 class.
Writes results/predict_test121.md."""
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test72 import cval
from predict_test81 import classes_of
from signs import FISH

NF520 = ('175', '382', '70', '72')


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-twenty-first registered predictions: what else marks the 520 class', 'predict_test121')
    ns = sorted({(b, e) for b, e in T.names(AB) if b})
    cl = classes_of(ns)
    rd.say('- 520 class: %s.' % ', '.join(sorted(h for h in cl if cl[h] == '520')))
    rd.say()
    pf = lambda b: len(b) >= 2 and b[-2] in FISH
    rd.gtl('C5A', 'fish precede the non-fish 520 heads', 'fish before, non-fish 520 heads', [pf(b) for b, e in ns if b[-1] in NF520],
           [pf(b) for b, e in ns if cl.get(b[-1]) == '740'])

    def c5b(names, key, lab):
        rd.gtl(key, '520 names open with a fish%s' % lab, 'fish opener, 520 names', [b[0] in FISH for b, e in names if e == '520' and len(b) >= 2],
               [b[0] in FISH for b, e in names if e == '740' and len(b) >= 2])
    c5b(ns, 'C5B', '')
    cv = [(cl[b[-1]], min(cval(b)[0], 5)) for b, e in ns if cval(b) and b[-1] in cl]
    rd.mi('C5C', 'the class sets the count', 'counted heads', [a for a, _ in cv], [v for _, v in cv])
    FL = sorted({tuple(ln) for r in F for ln in r['seq'] if ln})
    n = sum(1 for t in FL if any(x == '520' and y == '90' for x, y in zip(t, t[1:])))
    rd.rec('C5D', '90 never follows 520', "distinct F lines with '520 90': %d; threshold 1" % n, n <= 1)
    tok = Counter(b for b, e in T.names(AB) if e == '520' and b)
    rd.thr('C5E', '520 names repeat', 'five commonest 520 bodies (%s)' % '; '.join(' '.join(b) for b, _ in tok.most_common(5)), sum(n_ for _, n_ in tok.most_common(5)), sum(tok.values()), 0.2)
    ln_ = defaultdict(set)
    for b, e in ns:
        for i in range(1, len(b)):
            ln_[b[i]].add(b[i - 1])
    fishL = set().union(*[ln_[f] for f in FISH if f in ln_])
    jac = lambda a, b: len(a & b) / max(1, len(a | b))
    h5 = [h for h in cl if cl[h] == '520' and h not in FISH and len(ln_[h]) >= 3]
    h7 = [h for h in cl if cl[h] == '740' and h not in FISH and len(ln_[h]) >= 3]
    m5 = sum(jac(ln_[h], fishL) for h in h5) / max(1, len(h5))
    m7 = sum(jac(ln_[h], fishL) for h in h7) / max(1, len(h7))
    rd.rec('C5F', '520 heads keep fish company', 'mean Jaccard with fish left neighbours: 520 heads %.3f (%d), 740 heads %.3f (%d)' % (m5, len(h5), m7, len(h7)), m5 > m7)
    j = jac(ln_['222'], ln_['220'])
    rd.rec('C5G', '222 and 220 take different words', 'Jaccard %.3f (222: %d, 220: %d neighbours); threshold 0.3' % (j, len(ln_['222']), len(ln_['220'])), j <= 0.3)
    fh = [(bool(cval(b)), e) for b, e in ns if b[-1] in FISH]
    rd.gtl('C5H', 'counted fish take 520', '520, counted fish heads', [e == '520' for c, e in fh if c], [e == '520' for c, e in fh if not c])

    def c5i(lines, key, lab):
        x = [t for t in lines if any(g == '520' for g in t)]
        rd.thr(key, 'a fish stands before 520%s' % lab, 'lines with a fish directly before 520', sum(any(t[i] == '520' and i > 0 and t[i - 1] in FISH for i in range(len(t))) for t in x), len(x), 0.4)
    DL = sorted({tuple(t) for t in AB})
    c5i(DL, 'C5I', '')
    fb = [(b[-2], e) for b, e in ns if len(b) >= 2 and b[-1] in FISH]
    rd.mi('C5J', 'the sign before the fish chooses the class', 'fish-headed names', [a for a, _ in fb], [e for _, e in fb])
    nsB = sorted({(b, e) for b, e in T.names(B) if b})
    c5b(nsB, 'C5K', ' (B)')
    c5i(sorted({tuple(t) for t in B}), 'C5L', ' (B)')
    rd.finish()


if __name__ == '__main__':
    main()
