"""Hundred-and-sixty-ninth registered prediction set (PREDICTIONS.md, WR1-WR10): writing-system statistics of the Indus
signs against Linear B signs, Linear B words and Ur III lemmas at a matched sample size. Writes
results/predict_test169.md."""
import math
import os
import random
from collections import Counter

import rtools as R
import ur3_seals
from predict_test152 import LINB

random.seed(189)
N_TOK, DRAWS = 5000, 100


def linb_lines():
    signs, words = [], []
    with open(os.path.join(LINB, 'corpus_damos_lines.txt'), encoding='utf-8') as f:
        for ln in f:
            p = ln.rstrip('\n').split('\t')
            if len(p) < 3:
                continue
            s, w = [], []
            for t in p[2].split():
                if t == ',' or t.isdigit() or '~' in t:
                    continue
                if t[0].islower() or (t[0].isdigit() is False and '-' in t and t.lower() == t):
                    w.append(t)
                    s += t.split('-')
                elif t.isupper() or t.startswith('*'):
                    s.append(t)
            if s:
                signs.append(tuple(s))
            if w:
                words.append(tuple(w))
    return signs, words


def H(c):
    n = sum(c.values())
    return -sum(v / n * math.log2(v / n) for v in c.values() if v)


def stats(lines):
    out = {k: 0.0 for k in ('types', 'hapax', 'hcond', 'top10', 'hnorm', 'dbl', 'ratio', 'top1')}
    for _ in range(DRAWS):
        ls = list(lines)
        random.shuffle(ls)
        sample, n = [], 0
        for x in ls:
            sample.append(x)
            n += len(x)
            if n >= N_TOK:
                break
        uni = Counter(g for x in sample for g in x)
        bi = Counter((a, b) for x in sample for a, b in zip(x, x[1:]))
        first = Counter(a for x in sample for a in x[:-1])
        tot = sum(uni.values())
        h1 = H(uni)
        hc = H(bi) - H(first) if bi else 0.0
        out['types'] += len(uni)
        out['hapax'] += sum(v == 1 for v in uni.values()) / len(uni)
        out['hcond'] += hc
        out['top10'] += sum(v for g, v in uni.most_common(10)) / tot
        out['hnorm'] += h1 / math.log2(len(uni))
        out['dbl'] += sum(a == b for x in sample for a, b in zip(x, x[1:])) / tot
        out['ratio'] += hc / h1
        out['top1'] += uni.most_common(1)[0][1] / tot
    return {k: v / DRAWS for k, v in out.items()}


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-sixty-ninth registered predictions: writing-system statistics against two read scripts', 'predict_test169')
    ind = sorted({tuple(ln) for r in F for ln in r['seq'] if ln})
    lbs, lbw = linb_lines()
    U = ur3_seals.load()
    ur = sorted({tuple(cf for l_ in o['lines'] for cf, pos in l_) for o in U.values()})
    S = {'Indus signs': stats(ind), 'Linear B signs': stats(lbs), 'Linear B words': stats(lbw), 'Ur III lemmas': stats(ur)}
    keys = ('types', 'hapax', 'hcond', 'top10', 'hnorm', 'dbl', 'ratio', 'top1')
    rd.say('| unit | ' + ' | '.join(keys) + ' |')
    rd.say('|---|' + '---|' * len(keys))
    for u, v in S.items():
        rd.say('| %s | %s |' % (u, ' | '.join('%.3f' % v[k] if k != 'types' else '%.0f' % v[k] for k in keys)))
    rd.say()
    i, s, w = S['Indus signs'], S['Linear B signs'], S['Linear B words']
    btw = lambda k: min(s[k], w[k]) < i[k] < max(s[k], w[k])
    for key, k, title in (('WR1', 'types', 'types'), ('WR2', 'hapax', 'hapax share'), ('WR3', 'hcond', 'conditional entropy'),
                          ('WR4', 'top10', 'top-ten coverage'), ('WR5', 'hnorm', 'normalised entropy')):
        rd.rec(key, '%s between signs and words' % title, 'Indus %.3f; Linear B signs %.3f; Linear B words %.3f' % (i[k], s[k], w[k]), btw(k))
    d_s = abs(math.log(i['types']) - math.log(s['types']))
    d_w = abs(math.log(i['types']) - math.log(w['types']))
    rd.rec('WR6', 'Indus is more sign-like than word-like', 'log distance to Linear B signs %.2f, to words %.2f' % (d_s, d_w), d_s < d_w)
    rd.rec('WR7', 'fewer types than Ur III lemmas', 'Indus %.0f; Ur III lemmas %.0f' % (i['types'], S['Ur III lemmas']['types']), i['types'] < S['Ur III lemmas']['types'])
    rd.rec('WR8', 'doubling between signs and words', 'Indus %.4f; Linear B signs %.4f; words %.4f' % (i['dbl'], s['dbl'], w['dbl']), btw('dbl'))
    rd.rec('WR9', 'predictability between signs and words', 'Indus %.3f; Linear B signs %.3f; words %.3f' % (i['ratio'], s['ratio'], w['ratio']), btw('ratio'))
    rd.rec('WR10', 'one dominant sign', 'commonest-unit share: Indus %.3f; Linear B signs %.3f' % (i['top1'], s['top1']), i['top1'] > s['top1'])
    rd.finish()


if __name__ == '__main__':
    main()
