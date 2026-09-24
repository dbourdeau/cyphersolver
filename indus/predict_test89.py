"""Eighty-ninth registered prediction set (PREDICTIONS.md, HS1-HS20): the three heading signs. Writes
results/predict_test89.md."""
import random
from collections import Counter, defaultdict

import rtools as R
from predict_test44 import nonname
from predict_test82 import suffix_lines
from signs import FISH

random.seed(109)
HEAD = ('817', '820', '861')


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Eighty-ninth registered predictions: the three heading signs', 'predict_test89')
    full = lambda r: '' if recs[r['sealid']][18].strip() in ('', 'None') else recs[r['sealid']][18].strip()
    DL = sorted({tuple(t) for t in AB})
    hd = lambda t: len(t) >= 2 and t[0] in HEAD
    isn = lambda t: bool(R.name_of(list(t)) and R.name_of(list(t))[0])
    H = [t for t in DL if hd(t)]
    rd.say('- distinct headed lines %d (%s).' % (len(H), dict(Counter(t[0] for t in H))))
    rd.say()

    def hs1(lines, key, lab):
        x = [(t[0], R.name_of(list(t))[0][-1]) for t in lines if hd(t) and isn(t)]
        rd.mi(key, 'the name chooses its heading%s' % lab, 'headed name lines', [a for a, _ in x], [b for _, b in x])
    hs1(DL, 'HS1', '')
    FD = sorted({(r['site'].strip(), r['type'][:3], tuple(ln)) for r in F for ln in r['seq'] if ln})
    fh = [(s, ty, t[0]) for s, ty, t in FD if hd(t)]
    cs = [(s, h) for s, ty, h in fh if s in ('Harappa', 'Mohenjo-daro')]
    rd.mi('HS2', 'the city chooses the heading', 'F headed lines', [a for a, _ in cs], [b for _, b in cs])
    ts = [(ty, h) for s, ty, h in fh if ty in ('SEA', 'TAB')]
    rd.mi('HS3', 'the object chooses the heading', 'F headed lines', [a for a, _ in ts], [b for _, b in ts])
    rd.gtl('HS4', '861 heads formulas', 'formula, 861 lines', [nonname(list(t)) for t in H if t[0] == '861'], [nonname(list(t)) for t in H if t[0] == '817'])

    def two_after(lines, h):
        x = [t[1] == '2' for t in lines if hd(t) and t[0] == h]
        return sum(x), len(x)
    for key, h in (('HS5', '817'), ('HS6', '820'), ('HS7', '861')):
        k, n = two_after(DL, h)
        rd.thr(key, '%s takes 2' % h, '%s headings followed by 2' % h, k, n, 0.9)
    rd.mi('HS8', 'the heading chooses its number', 'headed lines', [t[0] for t in H], [t[1] == '2' for t in H])
    hb = defaultdict(set)
    for t in H:
        if isn(t):
            hb[R.name_of(list(t))[0]].add(t[0])
    hc = Counter(R.name_of(list(t))[0] for t in H if isn(t))
    rep = [b for b in hc if hc[b] >= 2]
    rd.thr('HS9', 'the heading signs are interchangeable', 'bodies after 2+ heading signs', sum(len(hb[b]) >= 2 for b in rep), len(rep), 0.2)
    ni = [(t, i) for t in DL for i in range(1, len(t)) if t[i] in HEAD]
    rd.thr('HS10', 'inside a line the heading sign is counted', 'non-initial tokens after a numeral', sum(t[i - 1] in R.NUMS for t, i in ni), len(ni), 0.5)
    rd.thr('HS11', 'one heading per line', 'lines with two heading-sign tokens', sum(sum(g in HEAD for g in t) >= 2 for t in DL), len(DL), 0.02, above=False)
    MDL = sorted({tuple(ln) for r in F if r['site'].strip() == 'Mohenjo-daro' for ln in r['seq'] if ln})
    rd.rank('HS12', 'Mohenjo-daro headed names are longer', 'headed against unheaded bodies', [len(R.name_of(list(t))[0]) for t in MDL if hd(t) and isn(t)],
            [len(R.name_of(list(t))[0]) for t in MDL if not hd(t) and isn(t)])
    a = [R.name_of(list(t))[1] == '740' for t in DL if hd(t) and isn(t)]
    c = [R.name_of(list(t))[1] == '740' for t in DL if not hd(t) and isn(t)]
    p = min(1, 2 * min(R.hyper_ge(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c)), R.fisher_less(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c))))
    rd.rec('HS13', 'the heading does not touch the class', '740, headed %s' % R.fl(sum(a), len(a), sum(c), len(c), p), p >= 0.05)
    fish = lambda t: any(g in FISH for g in R.name_of(list(t))[0])
    rd.ltl('HS14', 'headed names are not fish names', 'fish, headed names', [fish(t) for t in DL if hd(t) and isn(t)], [fish(t) for t in DL if not hd(t) and isn(t)])
    sm = [(hd(t), f != '#') for t in MDL if isn(t) for b, e, f in suffix_lines([t])]
    rd.ltl('HS15', 'headed names are not suffixed', 'suffix, headed MD name lines', [x for h, x in sm if h], [x for h, x in sm if not h])
    so = [(any(hd(tuple(ln)) for ln in r['seq'] if ln), full(r).split(':')[0].strip() == 'Bull1') for r in F if r['type'].startswith('SEAL') and full(r)]
    rd.gtl('HS16', 'headed seals are unicorns', 'unicorn, headed seals', [u for h, u in so if h], [u for h, u in so if not h])
    objs = defaultdict(set)
    hflag = {}
    for r in F:
        for ln in r['seq']:
            if ln and R.name_of(ln) and R.name_of(ln)[0]:
                k = R.name_of(ln)
                objs[k].add(r['sealid'])
                hflag[k] = hflag.get(k, False) or hd(tuple(ln))
    rd.gtl('HS17', 'headed names are personal', 'one-off, headed names', [len(objs[k]) == 1 for k in objs if hflag[k]], [len(objs[k]) == 1 for k in objs if not hflag[k]])
    al = [len([l_ for l_ in r['seq'] if l_]) == 1 for r in F for ln in r['seq'] if ln and hd(tuple(ln))]
    rd.thr('HS18', 'a headed line stands alone', 'headed lines alone on their object', sum(al), len(al), 0.95)
    DB = sorted({tuple(t) for t in B})
    hs1(DB, 'HS19', ' (B)')
    k, n = two_after(DB, '861')
    rd.thr('HS20', '861 takes 2 (B)', '861 headings followed by 2', k, n, 0.9)
    rd.finish()


if __name__ == '__main__':
    main()
