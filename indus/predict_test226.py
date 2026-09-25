"""Two-hundred-and-twenty-sixth registered prediction set (PREDICTIONS.md, UA1-UA4): decipherment loop 51, are Parpola's
description families (descfam.py) used alike, in A and in B separately? Writes results/predict_test226.md."""
import random
from collections import defaultdict
from itertools import combinations

import rtools as R
from descfam import families
from predict_test62 import sims
from signs import load


def coherence(members, S, C, rnd, n=1000):
    m = [g for g in members if g in S]
    if len(m) < 3:
        return None, None, len(m)
    mean = lambda xs: sum(C[(a, b)] for a, b in combinations(xs, 2)) / (len(xs) * (len(xs) - 1) / 2)
    mm = mean(m)
    ge = sum(mean(rnd.sample(S, len(m))) >= mm for _ in range(n))
    return mm, (ge + 1) / (n + 1), len(m)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-twenty-sixth registered predictions: decipherment loop 51, description families used alike?', 'predict_test226')
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln})
    fam = defaultdict(list)
    for g, f in families().items():
        fam[f].append(g)
    _, SA, CA = sims(DA, 20)
    _, SB, CB = sims(DB, 20)
    passed = []
    for f, mem in sorted(fam.items(), key=lambda kv: -len(kv[1])):
        a = coherence(mem, SA, CA, random.Random(226))
        b = coherence(mem, SB, CB, random.Random(227))
        if a[0] is None or b[0] is None:
            continue
        both = a[1] < 0.05 and b[1] < 0.05
        rd.say('- %s: A mean %.3f over %d, p = %.4f; B mean %.3f over %d, p = %.4f%s.' % (f, a[0], a[2], a[1], b[0], b[2], b[1], ' - both' if both else ''))
        if both:
            passed.append(f)
    rd.say()
    rd.rec('UA1', 'a non-fish family used alike in A and B', 'passing both: %s' % (', '.join(passed) or 'none'), any(f != 'd:fish' for f in passed))
    rd.rec('UA2', "the 'person' family", 'passes both: %s' % ('d:person' in passed), 'd:person' in passed)
    rd.rec('UA3', 'the fish family', 'passes both: %s' % ('d:fish' in passed), 'd:fish' in passed)
    rd.rec('UA4', 'progress rule', 'UA1 %s; families for M+: %s' % (any(f != 'd:fish' for f in passed), ', '.join(passed) or 'none'), any(f != 'd:fish' for f in passed))
    rd.finish()


if __name__ == '__main__':
    main()
