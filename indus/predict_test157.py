"""Hundred-and-fifty-seventh registered prediction set (PREDICTIONS.md, GC1-GC7): which kinds of text are names, which
titles? Capture-recapture profiles against the Linear B persons and titles of set 152. Writes
results/predict_test157.md."""
from collections import Counter

import rtools as R
from predict_test108 import genre
from predict_test140 import major
from predict_test147 import chapman

PERSONS = {'ratio': 3.57, 'shared': 0.181, 'one': 0.709}
TITLES = {'ratio': 1.56, 'shared': 0.500, 'one': 0.512}


def profile(catch):
    """catch: {label: Counter(unit -> objects)} for two labels."""
    (a, x), (b, y) = sorted(catch.items())
    X, Y = set(x), set(y)
    obs = len(X | Y)
    m = len(X & Y)
    lp = chapman(len(X), len(Y), m)
    tot = x + y
    one = sum(v == 1 for v in tot.values())
    return {'ratio': lp / max(1, obs), 'shared': m / max(1, min(len(X), len(Y))), 'one': one / max(1, obs),
            'n': (len(X), len(Y), m, obs), 'm': m, 'small': min(len(X), len(Y))}


def kind(p):
    near_p = sum(abs(p[k] - PERSONS[k]) < abs(p[k] - TITLES[k]) for k in PERSONS)
    return 'person-like' if near_p >= 2 else 'title-like'


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-fifty-seventh registered predictions: which kinds of text are names, which titles?', 'predict_test157')
    cities = ('Mohenjo-daro', 'Harappa')
    cat = {k: {c: Counter() for c in cities} for k in ('740', '520', 'closer', 'count')}
    for r in F:
        c = recs[r['sealid']][3]
        if c not in cities or r['type'] == 'TAB:C':
            continue
        seal = r['type'].startswith('SEAL')
        units = {'740': set(), '520': set(), 'closer': set(), 'count': set()}
        for ln in r['seq']:
            t = tuple(ln)
            if not t:
                continue
            nm = R.name_of(list(t))
            if seal and nm and nm[0] and nm[1] in ('740', '520'):
                units[nm[1]].add(nm)
            g = genre(t)
            if seal and g == 'closer':
                units['closer'].add(t)
            if g == 'count':
                units['count'].add(t)
        for k, us in units.items():
            for u in us:
                cat[k][c][u] += 1
    cu = {'DK': Counter(), 'other': Counter()}
    for r in F:
        if r['type'] == 'TAB:C' and recs[r['sealid']][3] == 'Mohenjo-daro':
            mj = major(recs[r['sealid']][4])
            if mj:
                cu['DK' if mj == 'DK' else 'other'][tuple(r['flat'])] += 1
    P = {k: profile(v) for k, v in cat.items()}
    P['copper'] = profile(cu)
    for k, p in P.items():
        rd.say('- %s: catches %d / %d, shared %d, together %d; estimate/observed %.2f; shared %.2f; on one object %.2f -> %s.' % (
            k, p['n'][0], p['n'][1], p['n'][2], p['n'][3], p['ratio'], p['shared'], p['one'], kind(p)))
    rd.say('- Linear B persons: %.2f, %.2f, %.2f; titles: %.2f, %.2f, %.2f.' % (
        PERSONS['ratio'], PERSONS['shared'], PERSONS['one'], TITLES['ratio'], TITLES['shared'], TITLES['one']))
    rd.say()
    for key, k, want in (('GC1', '740', 'person-like'), ('GC2', '520', 'title-like'), ('GC3', 'closer', 'title-like'),
                         ('GC4', 'count', 'title-like'), ('GC5', 'copper', 'title-like')):
        rd.rec(key, '%s texts are %s' % (k, want), '%s profile: %.2f, %.2f, %.2f -> %s' % (k, P[k]['ratio'], P[k]['shared'], P[k]['one'], kind(P[k])), kind(P[k]) == want)
    sh = lambda k: [True] * P[k]['m'] + [False] * (P[k]['small'] - P[k]['m'])
    rd.gtl('GC6', '520 names are shared more than 740 names', 'shared, 520 names', sh('520'), sh('740'))
    rd.gtl('GC7', 'closer texts are shared more than 740 names', 'shared, closer texts', sh('closer'), sh('740'))
    rd.finish()


if __name__ == '__main__':
    main()
