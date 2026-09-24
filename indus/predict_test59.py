"""Fifty-ninth registered prediction set (PREDICTIONS.md, HD1-HD10): the headings. Writes results/predict_test59.md."""
import random
from collections import Counter

import rtools as R
from predict_test44 import nonname

random.seed(79)
HEAD = ('817', '820', '861')


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Fifty-ninth registered predictions: the headings', 'predict_test59')
    hd = lambda t: len(t) >= 2 and t[0] in HEAD
    H = [t for t in AB if hd(t)]
    rd.say('- headed lines %d (%s).' % (len(H), ', '.join('%s x%d' % kv for kv in Counter(t[0] for t in H).most_common())))
    rd.say()
    gk = [(t[0], bool(R.name_of(t))) for t in H if R.name_of(t) or nonname(t)]
    rd.mi('HD1', 'the heading goes with the genre', 'headed lines', [a for a, _ in gk], [b for _, b in gk])
    num = lambda t: any(g in R.NUMS for g in t)
    hf = [t for t in H if nonname(t)]
    rd.gtl('HD2', '861 heads counts', 'numeral, 861-headed formulas', [num(t) for t in hf if t[0] == '861'], [num(t) for t in hf if t[0] == '817'])
    nl = [t for t in AB if R.name_of(t)]
    rd.rank('HD3', 'headed names are longer', 'headed against unheaded name lines', [len(t) for t in nl if hd(t)], [len(t) for t in nl if not hd(t)])
    rd.thr('HD4', 'a number follows the heading', 'headed lines with a numeral second', sum(t[1] in R.NUMS for t in H), len(H), 0.5)
    items = [(r['type'].startswith('SEAL'), R.lstrat(len(ln)), 1 if hd(ln) else 0) for r in F if r['type'].startswith(('SEAL', 'TAB'))
             for ln in r['seq'] if len(ln) >= 2]
    rd.strat('HD5', 'seals are headed', 'seals minus tablets', items)
    cs = [(r['site'].strip(), ln[0]) for r in F if r['site'].strip() in ('Harappa', 'Mohenjo-daro') for ln in r['seq'] if hd(ln)]
    rd.mi('HD6', 'each city has its heading', 'F headed lines', [a for a, _ in cs], [b for _, b in cs])
    hb = {R.name_of(t)[0] for t in nl if hd(t)}
    ub = {R.name_of(t)[0] for t in nl if not hd(t)}
    rd.thr('HD7', 'the heading is optional', 'headed bodies also unheaded', len(hb & ub), len(hb), 0.3)
    rd.gtl('HD8', 'headed names take 740', '740, headed name lines', [R.name_of(t)[1] == '740' for t in nl if hd(t)],
           [R.name_of(t)[1] == '740' for t in nl if not hd(t)])
    pos = [i == 0 for t in AB for i, g in enumerate(t) if g in HEAD]
    rd.thr('HD9', 'headings stand first', 'heading tokens line-first', sum(pos), len(pos), 0.9)
    k = [R.kind(t[1]) == 'short' for t in H if t[1] in R.NUMS]
    rd.thr('HD10', 'a short number after the heading', 'short numerals after a heading (%s)' % ', '.join(
        '%s x%d' % kv for kv in Counter(t[1] for t in H if t[1] in R.NUMS).most_common(5)), sum(k), len(k), 0.8)
    rd.finish()


if __name__ == '__main__':
    main()
