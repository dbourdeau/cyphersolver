"""Forty-ninth registered prediction set (PREDICTIONS.md, TL1-TL10): the tally entries. Writes
results/predict_test49.md."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test43 import sp_perm
from predict_test44 import nonname

random.seed(69)


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Forty-ninth registered predictions: the tally entries', 'predict_test49')
    fl = []
    for r in F:
        for ln in r['seq']:
            if nonname(ln) and any(g in R.NUMS for g in ln):
                res = tuple(g for g in ln if g not in R.NUMS)
                if res:
                    fl.append(dict(r=r, ln=ln, res=res, v=sum(R.NUMS[g][0] for g in ln if g in R.NUMS)))
    grp = defaultdict(list)
    for f in fl:
        grp[f['res']].append(f)
    tg = {k: v for k, v in grp.items() if len({f['v'] for f in v}) >= 2}
    tset = {id(f) for v in tg.values() for f in v}
    rd.say('- numeral formulas %d; tally groups %d holding %d formulas.' % (len(fl), len(tg), len(tset)))
    rd.say()
    allv = [f['v'] for f in fl]
    sizes = [len(v) for v in tg.values()]

    def draws(stat):
        return sum(stat(random.sample(allv, s)) for s in sizes)
    rng = lambda vs: max(vs) - min(vs)
    obs = sum(rng([f['v'] for f in v]) for v in tg.values())
    le = sum(draws(rng) <= obs for _ in range(R.N))
    p = (le + 1) / (R.N + 1)
    rd.rec('TL1', 'a tally keeps to a range', 'summed range %d; p = %.4f' % (obs, p), p < 0.05)
    site = lambda f: f['r']['site'].strip()
    rd.gtl('TL2', 'Harappa keeps tallies', 'tally formulas, Harappa', [id(f) in tset for f in fl if site(f) == 'Harappa'],
           [id(f) in tset for f in fl if site(f) == 'Mohenjo-daro'])
    rd.thr('TL3', 'the tallied thing is short', 'groups with a 1-2 sign residue', sum(len(k) <= 2 for k in tg), len(tg), 0.8)
    bsig = {g for b, _ in T.names(AB) for g in b}
    own = lambda f: any(g not in bsig for g in f['res'])
    rd.gtl('TL4', 'tallies use formula-only signs', 'residue with a formula-only sign, tally formulas',
           [own(f) for f in fl if id(f) in tset], [own(f) for f in fl if id(f) not in tset])
    vc = Counter(allv)
    o, p = sp_perm(list(range(1, 13)), [-vc[v] for v in range(1, 13)])
    rd.rec('TL5', 'large counts are rare', 'counts for 1-12: %s; Spearman(value, -count) %.3f; p = %.4f' % (
        ', '.join(str(vc[v]) for v in range(1, 13)), o, p), o > 0 and p < 0.05)
    big = [(k, f['v']) for k, v in tg.items() if len(v) >= 5 for f in v]
    rd.mi('TL6', 'each item has its counts', 'tally groups with 5+ formulas', [k for k, _ in big], [v for _, v in big])
    tab = lambda f: f['r']['type'].startswith('TAB')
    rd.gtl('TL7', 'tallies are on tablets', 'tablet, tally formulas', [tab(f) for f in fl if id(f) in tset],
           [tab(f) for f in fl if id(f) not in tset])
    mem = [f for v in tg.values() for f in v]
    sites = [site(f) for f in mem]
    one = lambda ss: sum(len(set(ss[i:i + s])) == 1 for i, s in zip(_offsets(sizes), sizes))
    obs = one(sites)
    ss = sites[:]
    ge = 0
    for _ in range(R.N):
        random.shuffle(ss)
        ge += one(ss) >= obs
    p = (ge + 1) / (R.N + 1)
    rd.rec('TL8', 'a tally stays at one site', 'groups %d; one site %d; p = %.4f' % (len(tg), obs, p), p < 0.05)
    same = sum(len({f['ln'][0] in R.NUMS for f in v}) == 1 for v in tg.values())
    rd.thr('TL9', 'the number keeps its place', 'groups with the numeral in the same position', same, len(tg), 0.8)
    cons = lambda vs: any(x + 1 in set(vs) for x in vs)
    obs = sum(cons([f['v'] for f in v]) for v in tg.values())
    ge = sum(draws(cons) >= obs for _ in range(R.N))
    p = (ge + 1) / (R.N + 1)
    rd.rec('TL10', 'tallies count on', 'groups with consecutive values %d of %d; p = %.4f' % (obs, len(tg), p), p < 0.05)
    rd.finish()


def _offsets(sizes):
    o, out = 0, []
    for s in sizes:
        out.append(o)
        o += s
    return out


if __name__ == '__main__':
    main()
