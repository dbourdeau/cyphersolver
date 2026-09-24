"""Hundred-and-seventy-fifth registered prediction set (PREDICTIONS.md, TB1-TB10): contemporary Tamil-Brahmi donor
names (Mahadevan 2003, Appendix II, transcribed from the scan) against the Prakrit donor names of set 173 and the
Indus names. Writes results/predict_test175.md."""
import math
import random
from collections import Counter

import lang_names as L
import rtools as R
from predict_test165 import jsd
from predict_test171 import lens
from predict_test173 import aks, ratio
from predict_test174 import taks

random.seed(195)


def final_share(names):
    fin = Counter(a[-1][-1:] if a[-1][-1] not in 'aāiīuūeēoō' else a[-1] for a in names)
    k, v = fin.most_common(1)[0]
    return k, v / len(names)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-seventy-fifth registered predictions: contemporary Tamil-Brahmi donor names', 'predict_test175')
    tb = [taks(last) for full, last, fem in L.tb_names()]
    tb = [a for a in tb if len(a) >= 2]
    ind = [n[:-1] for n in L.indus(F) if len(n) >= 3]
    pk = sorted({aks(n) for n, s, f in L.pra_luders()})
    pk = [a for a in pk if len(a) >= 2]
    tr = sorted({taks(n) for n, rep in L.tam_records()})
    tr = [a for a in tr if len(a) >= 2]
    n = min(len(ind), len(pk), len(tb))
    rd.say('- names: Tamil-Brahmi %d, Prakrit %d, Indus %d; rarefied to %d.' % (len(tb), len(pk), len(ind), n))
    ri, rp, rt = ratio(ind, n), ratio(pk, n), ratio(tb, n)
    rd.say('- R: Indus %.2f, Prakrit %.2f, Tamil-Brahmi %.2f.' % (ri, rp, rt))
    rd.say()
    rd.rec('TB1', 'Tamil-Brahmi names close the last element', 'R %.2f' % rt, rt < 1)
    d2 = (abs(math.log(ri / rp)), abs(math.log(ri / rt)))
    rd.rec('TB2', 'Indus R nearer Prakrit than Tamil-Brahmi', 'log distances %.2f and %.2f' % d2, d2[0] < d2[1])
    li, lp, lt = lens(ind), lens(pk), lens(tb)
    d3 = (jsd(li, lp), jsd(li, lt))
    rd.rec('TB3', 'Indus lengths nearer Prakrit than Tamil-Brahmi', 'JSD to Prakrit %.3f, to Tamil-Brahmi %.3f' % d3, d3[0] < d3[1])
    cov = lambda ns: sum(v for k, v in Counter(a[-2:] for a in ns if len(a) >= 3).most_common(10)) / max(1, sum(1 for a in ns if len(a) >= 3))
    ct, cp = cov(tb), cov(pk)
    ci = sum(v for k, v in Counter(b[-1] for b in ind).most_common(10)) / len(ind)
    top_t = ', '.join('-' + ''.join(k) for k, v in Counter(a[-2:] for a in tb if len(a) >= 3).most_common(10))
    rd.rec('TB4', 'Tamil-Brahmi names end in stock heads like Indus', 'Tamil-Brahmi top ten final pairs %.2f (%s); Indus heads %.2f' % (ct, top_t, ci), abs(ct - ci) <= 0.15)
    rd.rec('TB5', 'Indus head share nearer Prakrit than Tamil-Brahmi', 'Indus %.2f; Prakrit %.2f; Tamil-Brahmi %.2f' % (ci, cp, ct), abs(ci - cp) < abs(ci - ct))
    full = L.indus(F)
    si = Counter(x[-1] for x in full).most_common(1)[0][1] / len(full)
    kt, st = final_share(tb)
    kp, sp = final_share(pk)
    rd.rec('TB6', 'the dominant ending is nearer Tamil-Brahmi', 'Indus 740 %.2f; Tamil-Brahmi final %s %.2f; Prakrit final %s %.2f' % (si, kt, st, kp, sp), abs(si - st) < abs(si - sp))
    mi, mt = sum(map(len, ind)) / len(ind), sum(map(len, tb)) / len(tb)
    rd.rec('TB7', 'Tamil-Brahmi names as long as Indus bodies', 'Indus %.2f signs; Tamil-Brahmi %.2f aksharas' % (mi, mt), abs(mi - mt) <= 1)
    fav = sum([d2[0] < d2[1], d3[0] < d3[1], abs(ci - cp) < abs(ci - ct)])
    rd.rec('TB8', 'name structure nearer Indo-Aryan donor names', '%d of 3 comparisons favour the Prakrit names' % fav, fav >= 2)
    kr, sr = final_share(tr)
    rd.rec('TB9', 'Tamil naming is stable over time', 'Tamil-Brahmi %s %.2f; Tamil records %s %.2f' % (kt, st, kr, sr), abs(st - sr) <= 0.15)
    rd.rec('TB10', 'the two languages are distinguishable', 'Tamil-Brahmi %.2f against Prakrit %.2f' % (st, sp), abs(st - sp) > 0.2)
    rd.finish()


if __name__ == '__main__':
    main()
