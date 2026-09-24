"""Hundred-and-fifty-eighth registered prediction set (PREDICTIONS.md, UR1-UR7): Ur III seal legends (ORACC, ur3_seals.py)
as a read control. Writes results/predict_test158.md."""
from collections import Counter

import rtools as R
import ur3_seals
from predict_test103 import CL
from predict_test157 import kind, profile

SKIP = ('dumu', 'arad', 'lugal')


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-fifty-eighth registered predictions: Ur III seal legends as a read control', 'predict_test158')
    U = ur3_seals.load()
    legends = {}
    for (text, seal), o in U.items():
        key = tuple(tuple(ln) for ln in o['lines'])
        legends.setdefault(key, set()).add(o['site'])
    rd.say('- seal surfaces %d; distinct legends %d; sites %s.' % (len(U), len(legends), dict(Counter(s for v in legends.values() for s in v).most_common(5))))
    rd.say()
    sites = ('Umma', 'Girsu')

    def owner(lg):
        return next((cf for cf, pos in lg[0] if pos == 'PN'), None) if lg else None

    def titles(lg):
        return [cf for ln in lg[1:] for cf, pos in ln if pos == 'N' and cf not in SKIP]

    def fathers(lg):
        out = []
        for ln in lg:
            for i, (cf, pos) in enumerate(ln):
                if cf == 'dumu':
                    out += [c for c, p in ln[i + 1:i + 2] if p == 'PN']
        return out
    cats = {k: {s: Counter() for s in sites} for k in ('owner', 'title', 'legend', 'father')}
    for lg, ss in legends.items():
        for s in ss:
            if s in sites:
                if owner(lg):
                    cats['owner'][s][owner(lg)] += 1
                for t in set(titles(lg)):
                    cats['title'][s][t] += 1
                cats['legend'][s][lg] += 1
                for f in set(fathers(lg)):
                    cats['father'][s][f] += 1
    P = {k: profile(v) for k, v in cats.items()}
    for k, p in P.items():
        rd.say('- %s: Umma/Girsu %d / %d, shared %d; estimate/observed %.2f; shared %.2f; in one legend %.2f -> %s.' % (
            k, p['n'][0], p['n'][1], p['n'][2], p['ratio'], p['shared'], p['one'], kind(p)))
    rd.say()
    for key, k, want in (('UR1', 'owner', 'person-like'), ('UR2', 'title', 'title-like'), ('UR3', 'legend', 'person-like'), ('UR4', 'father', 'person-like')):
        rd.rec(key, 'Ur III %s names are %s' % (k, want) if k != 'legend' else 'Ur III whole legends are person-like',
               '%s profile %.2f, %.2f, %.2f -> %s' % (k, P[k]['ratio'], P[k]['shared'], P[k]['one'], kind(P[k])), kind(P[k]) == want)
    lgs = list(legends)
    two_u = sum(sum(pos == 'PN' for ln in lg for cf, pos in ln) >= 2 for lg in lgs) / len(lgs)
    seals = [r for r in F if r['type'].startswith('SEAL') and recs[r['sealid']][3] in ('Mohenjo-daro', 'Harappa')]
    two_i = sum(len([x for x in R.names_in(r) if x[0]]) >= 2 or sum(g in R.END for g in r['flat']) >= 2 for r in seals) / len(seals)
    rd.rec('UR5', 'the filiation format', 'Indus seals with two names %.3f; Ur III legends with 2+ PNs %.3f; threshold half' % (two_i, two_u), two_i >= two_u / 2)

    def post(r):
        out = []
        named = False
        for ln in r['seq']:
            t = list(ln)
            nm = R.name_of(t)
            if nm and nm[0]:
                named = True
                k = max(i for i, g in enumerate(t) if g in R.END)
                out += [g for g in t[k + 1:] if g in CL or g in ('400', '90')]
            elif t:
                out.append(t[-1])
        return named, out
    pi = [post(r) for r in seals]
    named = [o for n, o in pi if n]
    share_i = sum(bool(o) for o in named) / max(1, len(named))
    withown = [lg for lg in lgs if owner(lg)]
    share_u = sum(bool(titles(lg)) for lg in withown) / max(1, len(withown))
    rd.rec('UR6', 'a title field as often', 'Indus named seals with a post-name field %.3f; Ur III owner legends with a title %.3f; within a factor 2: %s' % (
        share_i, share_u, 0.5 <= share_i / max(1e-9, share_u) <= 2), 0.5 <= share_i / max(1e-9, share_u) <= 2)
    tu = Counter(titles(lg)[0] for lg in withown if titles(lg))
    ti = Counter(o[-1] for o in named if o)
    cu_ = sum(n for g, n in tu.most_common(10)) / max(1, sum(tu.values()))
    ci = sum(n for g, n in ti.most_common(10)) / max(1, sum(ti.values()))
    rd.rec('UR7', 'both title stocks are closed', 'Ur III top ten titles %.2f (%s); Indus top ten post-name signs %.2f (%s)' % (
        cu_, ', '.join(g for g, n in tu.most_common(10)), ci, ', '.join(g for g, n in ti.most_common(10))), cu_ >= 0.6 and ci >= 0.6)
    rd.finish()


if __name__ == '__main__':
    main()
