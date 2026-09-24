"""Hundred-and-seventy-fourth registered prediction set (PREDICTIONS.md, TD1-TD10): Tamil names from donation records
(DHARMA, English translations) as the Dravidian comparator matching set 173's Prakrit donor names. Writes
results/predict_test174.md."""
import math
import random
import re
from collections import Counter

import lang_names as L
import rtools as R
from predict_test157 import kind, profile
from predict_test163 import shuffled_shared
from predict_test165 import jsd
from predict_test171 import lens
from predict_test173 import aks, ratio

random.seed(194)
V = re.compile(r'(ai|au|[aāiīuūeēoō])')


def taks(w):
    w = w.lower().replace('-', '')
    parts, cur = [], ''
    i = 0
    while i < len(w):
        m = V.match(w, i)
        if m:
            cur += m.group(0)
            parts.append(cur)
            cur = ''
            i = m.end()
        else:
            cur += w[i]
            i += 1
    if cur and parts:
        parts[-1] += cur
    return tuple(parts)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-seventy-fourth registered predictions: the matching Dravidian comparator, Tamil names from donation records', 'predict_test174')
    tr = [(taks(n), rep) for n, rep in L.tam_records()]
    tr = [(a, rep) for a, rep in tr if a]
    cat = {'SII': Counter(), 'Pallava': Counter()}
    for a, rep in tr:
        k = 'SII' if 'sii' in rep else ('Pallava' if 'pallava' in rep else None)
        if k:
            cat[k][a] += 1
    p = profile(cat)
    rd.say('- Tamil record names: %d occurrences, %d distinct; SII %d, Pallava %d distinct.' % (len(tr), len({a for a, r in tr}), len(cat['SII']), len(cat['Pallava'])))
    rd.say()
    rd.rec('TD1', 'Tamil record names are person-like', '%s; %.2f, %.2f, %.2f -> %s' % (p['n'], p['ratio'], p['shared'], p['one'], kind(p)), kind(p) == 'person-like')
    ic = {'Mohenjo-daro': Counter(), 'Harappa': Counter()}
    for r in F:
        c = recs[r['sealid']][3]
        if r['type'].startswith('SEAL') and c in ic:
            for b, e in {x for x in R.names_in(r) if x[0]}:
                ic[c][b + (e,)] += 1
    q = profile(ic)['ratio'] / p['ratio']
    rd.rec('TD2', 'Indus as open as Tamil record names', 'Indus %.2f, Tamil records %.2f; quotient %.2f' % (profile(ic)['ratio'], p['ratio'], q), 0.5 <= q <= 2)
    ind = [n[:-1] for n in L.indus(F) if len(n) >= 3]
    pk = sorted({aks(n) for n, s, f in L.pra_luders()})
    pk = [a for a in pk if len(a) >= 2]
    td = sorted({a for a, r in tr if len(a) >= 2})
    n = min(len(ind), len(pk), len(td))
    ri, rp, rt = ratio(ind, n), ratio(pk, n), ratio(td, n)
    rd.say('- R at %d names: Indus %.2f, Prakrit %.2f, Tamil records %.2f.' % (n, ri, rp, rt))
    rd.rec('TD3', 'Tamil record names close the last element', 'R %.2f' % rt, rt < 1)
    d4 = (abs(math.log(ri / rp)), abs(math.log(ri / rt)))
    rd.rec('TD4', 'Indus R nearer Prakrit than Tamil records', 'log distances %.2f and %.2f' % d4, d4[0] < d4[1])
    li, lp, lt = lens(ind), lens(pk), lens(td)
    d5 = (jsd(li, lp), jsd(li, lt))
    rd.say('- mean lengths: Indus %.2f, Prakrit %.2f, Tamil records %.2f.' % (sum(map(len, ind)) / len(ind), sum(map(len, pk)) / len(pk), sum(map(len, td)) / len(td)))
    rd.rec('TD5', 'Indus lengths nearer Prakrit than Tamil records', 'JSD to Prakrit %.3f, to Tamil records %.3f' % d5, d5[0] < d5[1])
    t3 = [a for a in td if len(a) >= 3]
    ft = Counter(a[-2:] for a in t3)
    cov_t = sum(v for k, v in ft.most_common(10)) / len(t3)
    p3 = [a for a in pk if len(a) >= 3]
    cov_p = sum(v for k, v in Counter(a[-2:] for a in p3).most_common(10)) / len(p3)
    cov_i = sum(v for k, v in Counter(b[-1] for b in ind).most_common(10)) / len(ind)
    rd.rec('TD6', 'Tamil record names end in stock heads like Indus', 'Tamil records top ten final pairs %.2f (%s); Indus heads %.2f' % (
        cov_t, ', '.join('-' + ''.join(k) for k, v in ft.most_common(10)), cov_i), abs(cov_t - cov_i) <= 0.15)
    rd.rec('TD7', 'Indus head share nearer Prakrit than Tamil records', 'Indus %.2f; Prakrit %.2f; Tamil records %.2f' % (cov_i, cov_p, cov_t), abs(cov_i - cov_p) < abs(cov_i - cov_t))
    full = L.indus(F)
    si = Counter(x[-1] for x in full).most_common(1)[0][1] / len(full)
    ftt = Counter(a[-1][-1:] if a[-1][-1] not in 'aāiīuūeēoō' else a[-1] for a in td).most_common(1)[0]
    st = ftt[1] / len(td)
    fpp = Counter(a[-1] for a in pk).most_common(1)[0]
    sp = fpp[1] / len(pk)
    rd.rec('TD8', 'the dominant ending is nearer Tamil', 'Indus 740 %.2f; Tamil records final %s %.2f; Prakrit final %s %.2f' % (si, ftt[0], st, fpp[0], sp), abs(si - st) < abs(si - sp))
    S1, S2 = set(cat['SII']), set(cat['Pallava'])
    sh = shuffled_shared(S1, S2)
    real = len(S1 & S2)
    rd.rec('TD9', 'Tamil record names recur beyond combinatorics', 'real shared %d; shuffled mean %.1f; above %d of 1000' % (real, sum(sh) / len(sh), sum(x < real for x in sh)), sum(x < real for x in sh) >= 950)
    fav = sum([d4[0] < d4[1], d5[0] < d5[1], abs(cov_i - cov_p) < abs(cov_i - cov_t)])
    rd.rec('TD10', 'name structure nearer Indo-Aryan donor names', '%d of 3 comparisons favour the Prakrit names' % fav, fav >= 2)
    rd.finish()


if __name__ == '__main__':
    main()
