"""Hundred-and-fifty-first registered prediction set (PREDICTIONS.md, CU1-CU5): copper tablets by area at Mohenjo-daro.
Writes results/predict_test151.md."""
import random
from collections import Counter
from itertools import combinations

import rtools as R
from predict_test18 import level
from predict_test140 import GENERIC, pair_perm

random.seed(171)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-fifty-first registered predictions: copper tablets by area', 'predict_test151')
    cu = [r for r in F if r['type'] == 'TAB:C' and recs[r['sealid']][3] == 'Mohenjo-daro' and recs[r['sealid']][4].strip() not in GENERIC]
    sub = lambda r: recs[r['sealid']][4].strip()
    pic = lambda r: recs[r['sealid']][18].strip()
    rd.say('- copper tablets with a sub-area: %d; by sub-area %s; pictures %s.' % (len(cu), dict(Counter(sub(r) for r in cu)), dict(Counter(pic(r) for r in cu))))
    rd.say()
    pc = [r for r in cu if pic(r) not in ('-', '')]
    rd.mi('CU1', 'the picture depends on the area', 'copper tablets with a picture field', [pic(r) for r in pc], [sub(r) for r in pc])
    rd.mi('CU2', 'having a picture depends on the area', 'copper tablets', [pic(r) != 'None' for r in pc], [sub(r) for r in pc])
    o, e, p, n = pair_perm([(pic(r), sub(r)) for r in pc if pic(r) != 'None'])
    rd.rec('CU3', 'same picture, same area', 'pairs %d; same area %.3f against %.3f; p = %.4f' % (n, o, e, p), o > e and p < 0.05)
    sg = [set(g for g in r['flat'] if g not in R.NUMS) for r in cu]
    idx = list(combinations(range(len(cu)), 2))

    def diff(labs):
        a = [bool(sg[i] & sg[j]) for i, j in idx if labs[i] == labs[j]]
        c = [bool(sg[i] & sg[j]) for i, j in idx if labs[i] != labs[j]]
        return sum(a) / max(1, len(a)) - sum(c) / max(1, len(c))
    labs = [sub(r) for r in cu]
    obs = diff(labs)
    ge = 0
    for _ in range(1000):
        random.shuffle(labs)
        ge += diff(labs) >= obs
    p = (ge + 1) / 1001
    rd.rec('CU4', 'one area, shared signs', 'share-a-sign difference (same area minus different) %+.3f; p = %.4f' % (obs, p), obs > 0 and p < 0.05)
    lv = [(level('Mohenjo-daro', recs[r['sealid']]), sub(r)) for r in cu]
    lv = [(l_, s) for l_, s in lv if l_]
    o, e, p, n = pair_perm([(s, l_) for l_, s in lv])
    rd.rec('CU5', 'one area, one level', 'tablets with a level %d; same-area pairs %d; same level %.3f against %.3f; p = %.4f' % (len(lv), n, o, e, p), o > e and p < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
