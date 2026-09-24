"""Hundred-and-seventy-second registered prediction set (PREDICTIONS.md, LT1-LT6): the Tamil comparison repaired (the
honorific -ār removed by a fixed rule) and the ending profile. Writes results/predict_test172.md."""
import math
from collections import Counter

import lang_names as L
import rtools as R
from predict_test165 import jsd
from predict_test171 import lens, ratio, skt_syl, tam_aks


def core(name):
    w = name.split()[-1]
    return w[:-3] + '்' if w.endswith('ார்') else w


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-seventy-second registered predictions: the Tamil comparison repaired, and the ending profile', 'predict_test172')
    full = L.indus(F)
    ind = [n[:-1] for n in full if len(n) >= 3]
    tn = L.tam()
    tc = [tam_aks(core(n)) for n in tn]
    changed = sum(core(n) != n.split()[-1] for n in tn)
    tc2 = [x for x in tc if len(x) >= 2]
    ss = [x for x in (skt_syl(k1) for k1, mem, syl in L.skt()) if len(x) >= 2]
    lb = [x for x in L.linb() if len(x) >= 2]
    ri, _, _ = ratio(ind)
    rt, tf, tl = ratio(tc2)
    rs, _, _ = ratio(ss)
    rd.say('- Tamil names %d, honorific removed in %d; cores with 2+ aksharas %d; first types %.0f, last %.0f.' % (len(tn), changed, len(tc2), tf, tl))
    rd.say()
    rd.rec('LT1', 'Tamil cores close the last element', 'R %.2f' % rt, rt < 1)
    dt, ds = abs(math.log(ri / rt)), abs(math.log(ri / rs))
    rd.rec('LT2', 'Indus R nearer Tamil cores than Sanskrit', 'Indus %.2f; Tamil cores %.2f; Sanskrit %.2f; log distances %.2f and %.2f' % (ri, rt, rs, dt, ds), dt < ds)
    li, lt, ls = lens(ind), lens(tc2), lens(ss)
    rd.rec('LT3', 'Indus lengths nearer Tamil cores than Sanskrit', 'JSD to Tamil cores %.3f, to Sanskrit %.3f' % (jsd(li, lt), jsd(li, ls)), jsd(li, lt) < jsd(li, ls))
    mi, mt = sum(map(len, ind)) / len(ind), sum(map(len, tc2)) / len(tc2)
    rd.rec('LT4', 'Tamil cores as long as Indus bodies', 'Indus %.2f signs; Tamil cores %.2f aksharas' % (mi, mt), abs(mi - mt) <= 1)
    top = lambda xs: Counter(xs).most_common(1)[0]
    fi, ft, fs = top([n[-1] for n in full]), top([x[-1] for x in tc if x]), top([x[-1] for x in ss])
    si, st, s_s = fi[1] / len(full), ft[1] / len([x for x in tc if x]), fs[1] / len(ss)
    rd.rec('LT5', 'Indus ending concentration nearer Tamil', 'commonest final: Indus %s %.2f; Tamil cores %s %.2f; Sanskrit %s %.2f' % (
        fi[0], si, ft[0], st, fs[0], s_s), abs(si - st) < abs(si - s_s))
    fl = top([x[-1] for x in lb])
    rd.rec('LT6', 'Linear B endings are spread', 'Linear B commonest final %s %.2f against Indus %.2f' % (fl[0], fl[1] / len(lb), si), fl[1] / len(lb) < si)
    rd.finish()


if __name__ == '__main__':
    main()
