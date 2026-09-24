"""Two-hundred-and-seventh registered prediction set (PREDICTIONS.md, KF1-KF6): decipherment loop 32, blind key fitting
on Linear B (keyfit.py) as a language-identification gate. Writes results/predict_test207.md."""
import csv
import os
from collections import Counter

import lang_names as L
import rtools as R
from equation_rebus import lexicon_mw
from keyfit import Fit, shuffle_within, units
from linb_control import adjust
from lmkey import CharLM, score
from predict_test205 import LB, lb_lines
from predict_test206 import plain


def wordlists():
    return {'Greek': [w for w in (plain(adjust(x.strip())) for x in open(os.path.join(LB, 'greek', 'greek_translit_wordlist.txt'), encoding='utf-8') if x.strip()) if w],
            'Sanskrit': [w for w in (plain(a) for a, _ in lexicon_mw(os.path.join(L.SP, 'skt', 'mw.txt'))) if w],
            'Dravidian': [w for w in (plain(r['Form'].strip().strip('-')) for r in csv.DictReader(open(os.path.join(L.SP, 'drav', 'forms.csv'), encoding='utf-8'))) if w],
            'Sumerian': [w for w in (plain(r['cf']) for r in csv.DictReader(open(os.path.join(L.SP, 'sux', 'sux_gloss.tsv'), encoding='utf-8'), delimiter='\t')) if w]}


def gains(odd, even, W, seed, iters=30000):
    so, se = shuffle_within(odd, 0), shuffle_within(even, 1)
    out, keys = {}, {}
    for lg, ws in W.items():
        inv = units(ws)
        lm3, lm5 = CharLM(ws, 3), CharLM(ws, 5)
        k = Fit(odd, lm3, inv, seed).run(iters)
        ks = Fit(so, lm3, inv, seed).run(iters)
        out[lg] = (score(even, k, lm5), score(se, ks, lm5))
        keys[lg] = dict(k)
    return out, keys


def main():
    rd = R.Round('Two-hundred-and-seventh registered predictions: decipherment loop 32, blind key fitting on Linear B', 'predict_test207')
    lines, ventris = lb_lines()
    odd, even = lines[1::2], lines[0::2]
    W = wordlists()
    g1, k1 = gains(odd, even, W, 1)
    gain1 = {lg: a - b for lg, (a, b) in g1.items()}
    for lg, (a, b) in g1.items():
        rd.say('- seed 1, %s: held-out real %.3f, shuffled %.3f, gain %.3f bits/char.' % (lg, a, b, a - b))
    order = sorted(gain1, key=gain1.get, reverse=True)
    rd.say()
    rd.rec('KF1', 'Greek has the largest gain', 'order: %s' % ', '.join('%s %.3f' % (lg, gain1[lg]) for lg in order), order[0] == 'Greek')
    rd.rec('KF2', 'by 0.05 bits/char or more', 'Greek %.3f, next %s %.3f' % (gain1['Greek'], [x for x in order if x != 'Greek'][0], max(v for x, v in gain1.items() if x != 'Greek')), gain1['Greek'] - max(v for x, v in gain1.items() if x != 'Greek') >= 0.05)
    freq = Counter(g for t in lines for g in t)
    top = [g for g, n in freq.most_common(30)]
    agree = [g for g in top if g in ventris and plain(ventris[g]) == k1['Greek'].get(g)]
    rd.rec('KF3', "the fitted Greek key agrees with Ventris", '%d of 30 commonest signs (%s)' % (len(agree), ', '.join('%s=%s' % (g, ventris[g]) for g in agree)), len(agree) >= 6)
    g2, _ = gains(odd, even, W, 2)
    gain2 = {lg: a - b for lg, (a, b) in g2.items()}
    o2 = sorted(gain2, key=gain2.get, reverse=True)
    rd.rec('KF4', 'second seed', 'order: %s' % ', '.join('%s %.3f' % (lg, gain2[lg]) for lg in o2), o2[0] == 'Greek')
    rd.rec('KF5', 'every gain positive', 'seed 1 %s' % ', '.join('%s %.3f' % kv for kv in gain1.items()), all(v > 0 for v in gain1.values()))
    rd.rec('KF6', 'progress rule', 'KF1 %s, KF4 %s' % (order[0] == 'Greek', o2[0] == 'Greek'), order[0] == 'Greek' and o2[0] == 'Greek')
    rd.finish()


if __name__ == '__main__':
    main()
