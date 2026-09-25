"""Two-hundred-and-forty-second registered prediction set (PREDICTIONS.md, CL1-CL3): decipherment loop 67, are count-label
pairs less picture-diverse than ending pairs (content, not grammar)? Writes results/predict_test242.md."""
from collections import Counter, defaultdict

import rtools as R
from predict_test108 import genre
from predict_test17 import rank_perm
from predict_test200 import objects
from predict_test215 import slots
from predict_test240 import GRAM


def groups(objs, labels):
    occ = defaultdict(list)
    for t, m in objs:
        for p in {t[i:i + 2] for i in range(len(t) - 1)}:
            occ[p].append(m)
    div = {p: len(set(ms)) / len(ms) for p, ms in occ.items() if len(ms) >= 3}
    gram = lambda x: x in GRAM or x in R.NUMS
    lab = [d for p, d in div.items() if any(x in labels for x in p) and not any(gram(x) for x in p)]
    end = [d for p, d in div.items() if any(x in R.END for x in p)]
    return lab, end


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-forty-second registered predictions: decipherment loop 67, are the count labels content words?', 'predict_test242')
    DA = sorted({tuple(t) for t in A})
    labels = {g for g, v in Counter(s[0] for s in (slots(t) for t in DA if genre(t) == 'count') if s).most_common(10)}
    dirs = []
    for key, types, lab in (('CL1', ('TAB:C', 'TAB:I'), 'individually made tablets'), ('CL2', ('SEAL:S', 'SEAL:R'), 'seals')):
        a, b = groups(objects(F, recs, types), labels)
        if not a or not b:
            rd.rec(key, 'count-label pairs less diverse (%s)' % lab, '%d label pairs, %d ending pairs - too few' % (len(a), len(b)), False)
            dirs.append((False, None))
            continue
        d, p = rank_perm(a, b)
        ok = d < 0 and p < 0.05
        rd.rec(key, 'count-label pairs less diverse (%s)' % lab, '%d against %d pairs; means %.2f and %.2f; rank difference %+.1f; p = %.4f' % (len(a), len(b), sum(a) / len(a), sum(b) / len(b), d, p), ok)
        dirs.append((ok, d < 0))
    ok = any(o for o, _ in dirs) and all(dd for _, dd in dirs if dd is not None)
    rd.rec('CL3', 'progress rule', '%s' % dirs, ok)
    rd.finish()


if __name__ == '__main__':
    main()
