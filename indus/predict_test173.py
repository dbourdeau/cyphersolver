"""Hundred-and-seventy-third registered prediction set (PREDICTIONS.md, PK1-PK10): early Prakrit donor names (Lueders
1912) as an Indo-Aryan comparator. Writes results/predict_test173.md."""
import math
import random
import re
from collections import Counter

import lang_names as L
import rtools as R
from predict_test157 import kind, profile
from predict_test163 import shuffled_shared
from predict_test165 import jsd
from predict_test171 import lens, tam_aks
from predict_test172 import core

random.seed(193)


def aks(w):
    w = re.sub(r'[^a-z]', '', w)
    s = re.findall(r'[^aeiou]*[aeiou]', w)
    tail = re.sub(r'.*[aeiou]', '', w)
    if s and tail:
        s[-1] += tail
    return tuple(s)


def ratio(names, n, draws=500):
    tf = tl = 0.0
    for _ in range(draws):
        s = random.sample(names, n)
        tf += len({x[0] for x in s})
        tl += len({x[-1] for x in s})
    return tl / tf


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-seventy-third registered predictions: early Prakrit donor names as an Indo-Aryan comparator', 'predict_test173')
    pk = [(aks(n), s) for n, s, f in L.pra_luders()]
    pk = [(a, s) for a, s in pk if a]
    cat = {'Sanchi': Counter(), 'Bharhut': Counter()}
    for a, s in pk:
        if s in cat:
            cat[s][a] += 1
    p = profile(cat)
    rd.say('- Prakrit donor names %d (Sanchi %d, Bharhut %d distinct).' % (len(pk), len(cat['Sanchi']), len(cat['Bharhut'])))
    rd.say()
    rd.rec('PK1', 'Prakrit donors are person-like', '%s; %.2f, %.2f, %.2f -> %s' % (p['n'], p['ratio'], p['shared'], p['one'], kind(p)), kind(p) == 'person-like')
    ic = {'Mohenjo-daro': Counter(), 'Harappa': Counter()}
    for r in F:
        c = recs[r['sealid']][3]
        if r['type'].startswith('SEAL') and c in ic:
            for b, e in {x for x in R.names_in(r) if x[0]}:
                ic[c][b + (e,)] += 1
    byL = lambda d, L_: {k: Counter({x: n for x, n in v.items() if len(x) == L_}) for k, v in d.items()}
    ok_len = all(min(len(v) for v in byL(cat, L_).values()) >= 20 and min(len(v) for v in byL(ic, L_).values()) >= 20 for L_ in (3, 4))
    if ok_len:
        qs = [profile(byL(ic, L_))['ratio'] / profile(byL(cat, L_))['ratio'] for L_ in (3, 4)]
        rd.rec('PK2', 'Indus and Prakrit equally open at matched length', 'quotients at 3 and 4 units: %.2f, %.2f' % tuple(qs), all(0.5 <= q <= 2 for q in qs))
    else:
        q = profile(ic)['ratio'] / p['ratio']
        rd.rec('PK2', 'Indus and Prakrit equally open', 'too few names per catch at 3 and 4 units; pooled: Indus %.2f, Prakrit %.2f, quotient %.2f' % (
            profile(ic)['ratio'], p['ratio'], q), 0.5 <= q <= 2)
    ind = [n[:-1] for n in L.indus(F) if len(n) >= 3]
    pn = [a for a, s in pk if len(a) >= 2]
    tc = [x for x in (tam_aks(core(n)) for n in L.tam()) if len(x) >= 2]
    n = min(len(ind), len(pn), len(tc))
    ri, rp, rt = ratio(ind, n), ratio(pn, n), ratio(tc, n)
    rd.say('- R at %d names: Indus %.2f, Prakrit %.2f, Old Tamil cores %.2f.' % (n, ri, rp, rt))
    rd.rec('PK3', 'Prakrit names close the last element', 'R %.2f' % rp, rp < 1)
    rd.rec('PK4', 'Indus R nearer Prakrit than Tamil', 'log distances %.2f and %.2f' % (abs(math.log(ri / rp)), abs(math.log(ri / rt))), abs(math.log(ri / rp)) < abs(math.log(ri / rt)))
    li, lp, lt = lens(ind), lens(pn), lens(tc)
    rd.rec('PK5', 'Indus lengths nearer Prakrit than Tamil', 'JSD to Prakrit %.3f, to Old Tamil %.3f' % (jsd(li, lp), jsd(li, lt)), jsd(li, lp) < jsd(li, lt))
    p3 = [a for a in pn if len(a) >= 3]
    fp = Counter(a[-2:] for a in p3)
    cov_p = sum(v for k, v in fp.most_common(10)) / len(p3)
    rd.rec('PK6', 'Prakrit names end in compound heads', 'top ten final pairs cover %.2f (%s)' % (cov_p, ', '.join('-' + ''.join(k) for k, v in fp.most_common(10))), cov_p >= 0.3)
    hd = Counter(b[-1] for b in ind)
    cov_i = sum(v for k, v in hd.most_common(10)) / len(ind)
    rd.rec('PK7', 'Indus heads as concentrated as Prakrit heads', 'Indus top ten heads cover %.2f; Prakrit %.2f' % (cov_i, cov_p), abs(cov_i - cov_p) <= 0.15)
    S, Bh = set(cat['Sanchi']), set(cat['Bharhut'])
    rd.rank('PK8', 'shared Prakrit names are shorter', 'akshara length, one-site against both-site names', [len(a) for a in (S | Bh) - (S & Bh)], [len(a) for a in S & Bh])
    sh = shuffled_shared(S, Bh)
    real = len(S & Bh)
    rd.rec('PK9', 'Prakrit names recur beyond combinatorics', 'real shared %d; shuffled mean %.1f; above %d of 1000' % (real, sum(sh) / len(sh), sum(x < real for x in sh)), sum(x < real for x in sh) >= 950)
    hc = {k: Counter({a[-2:]: 1 for a in v if len(a) >= 3}) for k, v in cat.items()}
    for k, v in cat.items():
        hc[k] = Counter()
        for a, c_ in v.items():
            if len(a) >= 3:
                hc[k][a[-2:]] += c_
    ph = profile(hc)
    rd.rec('PK10', 'Prakrit compound heads are title-like', '%s; %.2f, %.2f, %.2f -> %s' % (ph['n'], ph['ratio'], ph['shared'], ph['one'], kind(ph)), kind(ph) == 'title-like')
    rd.finish()


if __name__ == '__main__':
    main()
