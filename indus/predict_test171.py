"""Hundred-and-seventy-first registered prediction set (PREDICTIONS.md, LN1-LN10): the structure of names across
candidate languages (lang_names.py). Writes results/predict_test171.md."""
import math
import random
import re
from collections import Counter

import lang_names as L
import rtools as R
from predict_test165 import jsd

random.seed(191)
N, DRAWS = 400, 500


def skt_syl(k1):
    k1 = k1.replace('/', '').replace('^', '')
    s = re.findall(r'[^aAiIuUfFxXeEoO]*[aAiIuUfFxXeEoO]', k1)
    tail = re.sub(r'.*[aAiIuUfFxXeEoO]', '', k1)
    if s and tail:
        s[-1] += tail
    return tuple(s)


def tam_aks(w):
    out = []
    for ch in w:
        if ('அ' <= ch <= 'ஔ') or ('க' <= ch <= 'ஹ'):
            out.append(ch)
        elif out and 'ா' <= ch <= '்':
            out[-1] += ch
    return tuple(out)


def ratio(names):
    tf = tl = 0.0
    for _ in range(DRAWS):
        s = random.sample(names, min(N, len(names)))
        tf += len({x[0] for x in s})
        tl += len({x[-1] for x in s})
    return tl / tf, tf / DRAWS, tl / DRAWS


def lens(names):
    return Counter(min(len(x), 8) for x in names)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-seventy-first registered predictions: the structure of names across candidate languages', 'predict_test171')
    ind = [n[:-1] for n in L.indus(F) if len(n) >= 3]
    owners, fathers = L.sum_names()
    sm = [s for cf, s in owners if len(s) >= 2 and 'x' not in s]
    tm = [tam_aks(n.split()[-1]) for n in L.tam()]
    tm = [x for x in tm if len(x) >= 2]
    sk = L.skt()
    ss = [skt_syl(k1) for k1, mem, syl in sk]
    ss = [x for x in ss if len(x) >= 2]
    sc = [tuple(m.replace('/', '').replace('^', '') for m in mem) for k1, mem, syl in sk if len(mem) >= 2]
    lb = [x for x in L.linb() if len(x) >= 2]
    C = {'Indus': ind, 'Ur III': sm, 'Old Tamil': tm, 'Sanskrit syllables': ss, 'Linear B': lb, 'Sanskrit members': sc}
    Rt = {}
    for k, v in C.items():
        r, tf, tl = ratio(v)
        Rt[k] = r
        rd.say('- %s: names %d; first types %.0f, last types %.0f at %d names; R %.2f; mean length %.2f.' % (k, len(v), tf, tl, min(N, len(v)), r, sum(map(len, v)) / len(v)))
    rd.say()
    rd.rec('LN1', 'Sumerian names close the first element', 'R %.2f' % Rt['Ur III'], Rt['Ur III'] > 1)
    for key, k in (('LN2', 'Indus'), ('LN3', 'Old Tamil'), ('LN4', 'Sanskrit syllables'), ('LN5', 'Linear B')):
        rd.rec(key, '%s names close the last element' % k, 'R %.2f' % Rt[k], Rt[k] < 1)
    d_t, d_s = abs(math.log(Rt['Indus'] / Rt['Old Tamil'])), abs(math.log(Rt['Indus'] / Rt['Sanskrit syllables']))
    rd.rec('LN6', 'Indus R nearer Tamil than Sanskrit', 'log distance to Old Tamil %.2f, to Sanskrit %.2f' % (d_t, d_s), d_t < d_s)
    li, lt, ls, lu = lens(ind), lens(tm), lens(ss), lens(sm)
    fmt = lambda c: ', '.join('%d: %.2f' % (k, c[k] / sum(c.values())) for k in sorted(c))
    rd.say('- lengths: Indus %s | Old Tamil %s | Sanskrit %s | Ur III %s.' % (fmt(li), fmt(lt), fmt(ls), fmt(lu)))
    rd.rec('LN7', 'Indus lengths nearer Tamil than Sanskrit', 'JSD to Old Tamil %.3f, to Sanskrit %.3f' % (jsd(li, lt), jsd(li, ls)), jsd(li, lt) < jsd(li, ls))
    rd.rec('LN8', 'Indus lengths nearer Tamil than Sumerian', 'JSD to Old Tamil %.3f, to Ur III %.3f' % (jsd(li, lt), jsd(li, lu)), jsd(li, lt) < jsd(li, lu))
    rd.rec('LN9', 'Sanskrit compounds close the last member', 'member-level R %.2f (%d compound names)' % (Rt['Sanskrit members'], len(sc)), Rt['Sanskrit members'] < 1)
    q = Rt['Indus'] / Rt['Sanskrit members']
    rd.rec('LN10', 'Indus signs behave like name members', 'Indus R %.2f against Sanskrit member R %.2f; quotient %.2f' % (Rt['Indus'], Rt['Sanskrit members'], q), 0.5 <= q <= 2)
    rd.finish()


if __name__ == '__main__':
    main()
