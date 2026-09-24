"""Hundred-and-ninety-eighth registered prediction set (PREDICTIONS.md, GC1-GC5): decipherment loop 23, the genre control
for set 197: name lists on both sides (Sanskrit Monier-Williams names, Sangam poets' names; Japanese, Turkish given
names). Writes results/predict_test198.md."""
import random

import lang_names as L
import rtools as R
from predict_test171 import skt_syl, tam_aks
from predict_test197 import indus_measures, measures, rank


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-ninety-eighth registered predictions: decipherment loop 23, the genre control', 'predict_test198')
    full = L.indus(F)
    C = {'Sanskrit (MW)': [x for x in (skt_syl(k1) for k1, mem, syl in L.skt()) if len(x) >= 2],
         'Old Tamil (Sangam poets)': [x for x in (tam_aks(n.split()[-1]) for n in L.tam()) if len(x) >= 2],
         'Japanese': [m for m, fem in L.jp_names() if len(m) >= 2],
         'Turkish': [s for s, fem in L.tr_names() if len(s) >= 2]}
    rnd = random.Random(198)
    fl = sorted(set(full))
    rnd.shuffle(fl)
    h = len(fl) // 2
    n = min([len(v) for v in C.values()] + [sum(len(x) >= 3 for x in part) for part in (fl[:h], fl[h:])])
    rd.say('- names: %s; rarefied to %d.' % (', '.join('%s %d' % (k, len(v)) for k, v in C.items()), n))
    langs = {k: measures(v, n) for k, v in C.items()}
    order, ranks, d = rank(indus_measures(full, n), langs)
    for k in order:
        r, ln, head, dom = langs[k]
        rd.say('- %s: mean rank %.2f; R %.2f, head share %.2f, dominant final %.2f; distances %s.' % (k, ranks[k], r, head, dom, ', '.join('%.3f' % x for x in d[k])))
    rd.say()
    cand, dec = ('Sanskrit (MW)', 'Old Tamil (Sangam poets)'), ('Japanese', 'Turkish')
    pos = {k: i for i, k in enumerate(order)}
    rd.rec('GC1', 'a candidate list beats both decoys', 'order: %s' % ', '.join(order), min(pos[k] for k in cand) < min(pos[k] for k in dec))
    rd.rec('GC2', 'both candidate lists beat both decoys', 'positions %s' % {k: pos[k] + 1 for k in order}, max(pos[k] for k in cand) < min(pos[k] for k in dec))
    rd.rec('GC3', 'Sanskrit nearer than Japanese', 'Sanskrit %d, Japanese %d' % (pos[cand[0]] + 1, pos['Japanese'] + 1), pos[cand[0]] < pos['Japanese'])
    firsts = []
    for half in (fl[:h], fl[h:]):
        o, rk, _ = rank(indus_measures(half, n), langs)
        firsts.append(o[0])
        rd.say('- half: order %s.' % ', '.join(o))
    rd.rec('GC4', 'the same nearest list in both halves', 'nearest: %s' % ', '.join(firsts), firsts[0] == firsts[1])
    ok = min(pos[k] for k in cand) < min(pos[k] for k in dec) and firsts[0] == firsts[1]
    rd.rec('GC5', 'progress rule', 'GC1 %s, GC4 %s' % (min(pos[k] for k in cand) < min(pos[k] for k in dec), firsts[0] == firsts[1]), ok)
    rd.finish()


if __name__ == '__main__':
    main()
