"""Two-hundred-and-fifty-second registered prediction set (PREDICTIONS.md, PC1-PC6): decipherment loop 77, do signs whose
drawing shows X occur on objects whose picture shows X? Writes results/predict_test252.md."""
from collections import Counter, defaultdict

import rtools as R
from descfam import families
from predict_test178 import depiction
from predict_test200 import objects
from predict_test237 import merged
from predict_test7 import fisher_less
from signs import FISH

QUAD = {'Bult', 'Bull', 'Bull1', 'Bull2', 'Gaur', 'Goat', 'Elep', 'Rhin', 'Hare', 'Buff', 'Zebu', 'Tigr', 'Mult'}


def classes():
    fam = families()
    dep = depiction()
    by = lambda fams, fcat: {g for g, f in fam.items() if f in fams} | {g for g, c in dep.items() if c == fcat}
    return {'PLANT': (by({'d:leaf', 'd:leave', 'd:half-leave', 'd:tree', 'd:plant', 'd:branching'}, 'plant'), {'Phyt', 'Pipal'}),
            'FISH': (set(FISH), {'Fish'}),
            'PERSON': (by({'d:person', 'd:people'}, 'human'), {'Anth'}),
            'ANIMAL': (by({'d:deer', 'd:animal', "d:cow'", "d:cat'"}, 'animal'), QUAD)}


def texts(objs):
    g = defaultdict(list)
    for t, m in merged(objs):
        g[t].append(m)
    return {t: Counter(ms).most_common(1)[0][0] for t, ms in g.items()}


def test(tx, signs, pics):
    a = [any(x in signs for x in t) for t, m in tx.items() if m in pics]
    b = [any(x in signs for x in t) for t, m in tx.items() if m not in pics]
    p = fisher_less(sum(b), len(b) - sum(b), sum(a), len(a) - sum(a))
    return sum(a), len(a), sum(b), len(b), p


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-fifty-second registered predictions: decipherment loop 77, does a sign\'s drawing match the object\'s picture?', 'predict_test252')
    C = classes()
    rd.say('- class sizes: %s.' % ', '.join('%s %d signs' % (k, len(v[0])) for k, v in C.items()))
    s1, s2 = texts(objects(F, recs, ('TAB:C', 'TAB:I'))), texts(objects(F, recs, ('TAB:B',)))
    rd.say('- distinct texts: individually made %d, moulded %d.' % (len(s1), len(s2)))
    rd.say()
    passed, near = [], []
    for key, cl in (('PC1', 'PLANT'), ('PC2', 'FISH'), ('PC3', 'PERSON'), ('PC4', 'ANIMAL')):
        signs, pics = C[cl]
        r1, r2 = test(s1, signs, pics), test(s2, signs, pics)
        ok = all(r[4] < 0.05 and r[0] / max(1, r[1]) > r[2] / max(1, r[3]) for r in (r1, r2))
        rd.rec(key, '%s signs with %s pictures' % (cl, '/'.join(sorted(pics))[:40]), 'individually made: %d of %d matching texts against %d of %d others, p = %.4f; moulded: %d of %d against %d of %d, p = %.4f' % (*r1, *r2), ok)
        if ok:
            passed.append(cl)
        if min(r1[4], r2[4]) < 0.05 and max(r1[4], r2[4]) < 0.10:
            near.append(cl)
    rd.rec('PC5', 'one sample p < 0.05, the other p < 0.10', ', '.join(near) or 'none', bool(near))
    rd.rec('PC6', 'progress rule', 'classes passing both samples: %s' % (', '.join(passed) or 'none'), bool(passed))
    rd.finish()


if __name__ == '__main__':
    main()
