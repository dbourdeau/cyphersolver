"""Forty-eighth registered prediction set (PREDICTIONS.md, ML1-ML10): objects with more than one line. Writes
results/predict_test48.md. Pair baselines shuffle the second member of each within-object pair across objects."""
import random
from collections import Counter

import rtools as R
from predict_test44 import nonname

random.seed(68)


def kind(ln):
    return 'n' if R.name_of(ln) else ('f' if nonname(ln) else 'o')


def pair_perm(pairs, f, lower=False):
    a = [x for x, _ in pairs]
    b = [y for _, y in pairs]
    obs = sum(f(x, y) for x, y in pairs)
    c = 0
    for _ in range(R.N):
        random.shuffle(b)
        k = sum(f(x, y) for x, y in zip(a, b))
        c += (k <= obs) if lower else (k >= obs)
    return obs, (c + 1) / (R.N + 1)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Forty-eighth registered predictions: objects with more than one line', 'predict_test48')
    obj = [[ln for ln in r['seq'] if ln] for r in F]
    multi = [r for r, o in zip(F, obj) if len(o) >= 2]
    ml = [[ln for ln in r['seq'] if ln] for r in multi]
    rd.say('- objects %d, multi-line %d.' % (len(F), len(multi)))
    rd.say()
    kinds = [[kind(ln) for ln in o] for o in ml]
    both = lambda ks: 'n' in ks and 'f' in ks
    obs = sum(map(both, kinds))
    flat = [k for ks in kinds for k in ks]
    ge = 0
    for _ in range(R.N):
        random.shuffle(flat)
        i = k = 0
        for ks in kinds:
            k += both(flat[i:i + len(ks)])
            i += len(ks)
        ge += k >= obs
    p = (ge + 1) / (R.N + 1)
    rd.rec('ML1', 'a name with a formula', 'objects %d; with both %d; p = %.4f' % (len(ml), obs, p), p < 0.05)
    num = lambda t: any(g in R.NUMS for g in t)
    single = [o[0] for o in obj if len(o) == 1]
    rd.gtl('ML2', 'the formula beside a name is a count', 'numeral, formulas beside a name line',
           [num(ln) for o in ml if any(kind(x) == 'n' for x in o) for ln in o if kind(ln) == 'f'],
           [num(ln) for ln in single if kind(ln) == 'f'])
    pr = [(o[0], o[1]) for o in ml]
    o_, p = pair_perm(pr, lambda x, y: bool(set(x) & set(y)))
    rd.rec('ML3', 'the lines of an object share signs', 'pairs %d; sharing %d; p = %.4f' % (len(pr), o_, p), p < 0.05)
    rd.rank('ML4', 'multi-line lines are shorter', 'one-line against multi-line lines', [len(x) for x in single],
            [len(x) for o in ml for x in o])
    npr = []
    for o in ml:
        nm = [R.name_of(x) for x in o if R.name_of(x)]
        if len(nm) >= 2:
            npr.append((nm[0], nm[1]))
    o_, p = pair_perm(npr, lambda x, y: x[1] == y[1])
    rd.rec('ML5', 'names on one object share the ending', 'pairs %d; same ending %d; p = %.4f' % (len(npr), o_, p), p < 0.05)
    hp = [(x, y) for x, y in npr if x[0] and y[0]]
    o_, p = pair_perm(hp, lambda x, y: x[0][-1] == y[0][-1])
    rd.rec('ML6', 'names on one object share the head', 'pairs %d; same last body sign %d; p = %.4f' % (len(hp), o_, p), p < 0.05)
    items = [(len(o) >= 2, R.lstrat(len(ln)), 1 if ln[0] in R.NUMS else 0) for o in obj for ln in o if kind(ln) == 'f']
    rd.strat('ML7', 'multi-line formulas open with a number', 'multi-line minus one-line', items)
    md = [len(o) >= 2 for r, o in zip(F, obj) if r['site'].strip() == 'Mohenjo-daro']
    ha = [len(o) >= 2 for r, o in zip(F, obj) if r['site'].strip() == 'Harappa']
    rd.gtl('ML8', 'Mohenjo-daro writes more lines', 'multi-line, Mohenjo-daro', md, ha)
    tabs = [(tuple(tuple(x) for x in o), len(o) >= 2) for r, o in zip(F, obj) if r['type'].startswith('TAB') and o]
    tc = Counter(t for t, _ in tabs)
    d = {t: m for t, m in tabs}
    rd.gtl('ML9', 'multi-line tablets repeat', 'texts on 2+ objects, multi-line tablet texts',
           [tc[t] >= 2 for t in d if d[t]], [tc[t] >= 2 for t in d if not d[t]])
    # the partner of each numeral line is drawn from all lines of two-line objects (shuffling the partners among
    # themselves would leave the count unchanged)
    two = [(o[0], o[1]) for o in obj if len(o) == 2]
    pool = [x for pr_ in two for x in pr_]
    two = [(x, y) if num(x) else (y, x) for x, y in two if num(x) or num(y)]
    o_ = sum(num(y) for _, y in two)
    le = sum(sum(num(random.choice(pool)) for _ in two) <= o_ for _ in range(R.N))
    p = (le + 1) / (R.N + 1)
    rd.rec('ML10', 'one line counts', 'two-line objects with a numeral %d; both lines %d; p = %.4f' % (len(two), o_, p), p < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
