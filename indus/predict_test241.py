"""Two-hundred-and-forty-first registered prediction set (PREDICTIONS.md, JC1-JC4): decipherment loop 66, picture diversity
of pairs containing closers, count labels, or endings, against lexical pairs, on moulded tablets. Writes
results/predict_test241.md."""
from collections import Counter, defaultdict

import rtools as R
from predict_test103 import CL
from predict_test108 import genre
from predict_test200 import objects
from predict_test215 import slots
from predict_test240 import GRAM


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-forty-first registered predictions: decipherment loop 66, the pictures judge the closers and the count labels', 'predict_test241')
    DA = sorted({tuple(t) for t in A})
    labels = {g for g, v in Counter(s[0] for s in (slots(t) for t in DA if genre(t) == 'count') if s).most_common(10)}
    occ = defaultdict(list)
    for t, m in objects(F, recs, ('TAB:B',)):
        for p in {t[i:i + 2] for i in range(len(t) - 1)}:
            occ[p].append(m)
    div = {p: len(set(ms)) / len(ms) for p, ms in occ.items() if len(ms) >= 3}
    gram = lambda x: x in GRAM or x in R.NUMS
    lex = [d for p, d in div.items() if not any(gram(x) for x in p) and not any(x in labels for x in p)]
    clo = [d for p, d in div.items() if any(x in CL for x in p) and not any(gram(x) and x not in CL for x in p)]
    lab = [d for p, d in div.items() if any(x in labels for x in p) and not any(gram(x) for x in p)]
    end = [d for p, d in div.items() if any(x in R.END for x in p)]
    def rk(key, title, lab_, a, b):
        if not a or not b:
            rd.rec(key, title, '%s: %d against %d pairs - too few to test' % (lab_, len(a), len(b)), False)
        else:
            rd.rank(key, title, lab_, a, b)
        return rd.res[-1][1]
    ok1 = rk('JC1', 'closer pairs more picture-diverse than lexical pairs', 'closer pairs against lexical pairs', clo, lex)
    rk('JC2', 'count-label pairs more picture-diverse', 'count-label pairs against lexical pairs', lab, lex)
    rk('JC3', 'ending pairs more picture-diverse', 'pairs with 740 / 520 against lexical pairs', end, lex)
    rd.rec('JC4', 'progress rule', 'JC1 %s' % ok1, ok1)
    rd.finish()


if __name__ == '__main__':
    main()
