"""Six hypotheses following the regional results of decipher9i.py (ligatures and vocabulary differ by site) and the
R/T vowel rule.

Each has a prediction stated before the test ran and one primary test with its own null. Benjamini-Hochberg at
5% runs across the six.

J1  Sites closer together share more vocabulary: Jaccard similarity of word types falls with distance (Mantel).
J2  Tylissos shares more of its vocabulary with Haghia Triada than other sites do, for their size.
J3  Syllables after R and T use a richer set of vowels (higher vowel entropy) than after other consonants, more so
    than in Linear B.
J4  Unread signs (no Linear B value) are site-specific: sign and site are associated beyond chance.
J5  Variant spellings of the libation-formula words cluster by site.
J6  Amounts differ by site within the same commodity (site effect after stratifying by commodity).
"""
from collections import Counter, defaultdict
import json
from math import log
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import decipher9i as I  # noqa: E402

H, X, T, B, D, V = I.H, I.X, I.T, I.B, I.D, I.V
ROOT = B.ROOT
rng = I.rng
REPS = 2000
out = D.out
out.clear()
record = D.record
grid = D.grid
LA, LB = X.LA, X.LB


def site_vocab():
    voc = defaultdict(set)
    for r in B.READ['records']:
        for t in r['tokens']:
            if t['cls'] in ('word', 'word-with-unknown-sign') and t['label'] not in X.TERMS and '-' in t['label']:
                voc[r['site']].add(t['label'])
    return voc


VOC = site_vocab()


def J1():
    sites = [s for s in VOC if s in B.COORD and len(VOC[s]) >= 15]
    pairs = [(a, b) for i, a in enumerate(sites) for b in sites[i + 1:]]
    d = [B.km(a, b) for a, b in pairs]
    jac = lambda a, b: len(VOC[a] & VOC[b]) / len(VOC[a] | VOC[b])
    sim = [jac(a, b) for a, b in pairs]
    real = B.spearman(d, sim)
    null = []
    for _ in range(5000):
        perm = sites[:]
        rng.shuffle(perm)
        m = dict(zip(sites, perm))
        null.append(B.spearman([B.km(m[a], m[b]) for a, b in pairs], sim))
    p = T.pv_lower(null, real)
    record('J1 shared vocabulary and distance', 'Closer sites share more word types (Mantel, Spearman)',
           {'rho': round(real, 3), 'p': round(p, 4), 'sites': sites},
           {'pairs (km, jaccard)': sorted([(f'{a}-{b}', round(x), round(y, 3)) for (a, b), x, y in zip(pairs, d, sim)], key=lambda z: -z[2])[:10]})
    return p


def J2():
    ht = VOC['Haghia Triada']
    others = [s for s in VOC if s != 'Haghia Triada' and len(VOC[s]) >= 10]
    share = {s: len(VOC[s] & ht) / len(VOC[s]) for s in others}
    # null: rebuild each site's vocabulary by drawing the same number of word types from the pooled non-HT vocabulary
    pool = sorted(set().union(*(VOC[s] for s in others)))
    real = share['Tylissos']
    null = [len(set(rng.sample(pool, len(VOC['Tylissos']))) & ht) / len(VOC['Tylissos']) for _ in range(REPS)]
    p = B.pv(null, real)
    record('J2 Tylissos and Haghia Triada', 'Tylissos shares more of its vocabulary with Haghia Triada than other sites do',
           {'tylissos_share_with_HT': round(real, 3), 'null_mean': round(sum(null) / len(null), 3), 'p': round(p, 4), 'tylissos_words': len(VOC['Tylissos'])},
           {'share with HT by site': {s: round(v, 3) for s, v in sorted(share.items(), key=lambda kv: -kv[1])},
            'shared words': sorted(VOC['Tylissos'] & ht)})
    return p


def entropy_by_class(words, cls):
    c = Counter(grid(x)[1] for w in words for x in w if grid(x) and grid(x)[0] and (grid(x)[0] in 'rt') == cls)
    n = sum(c.values())
    return -sum(v / n * log(v / n) for v in c.values())


def J3():
    f = lambda ws: entropy_by_class(ws, True) - entropy_by_class(ws, False)
    real, p, nm = T.label_perm(lambda a, b: f(a) - f(b), LA, LB, reps=REPS)
    record('J3 richer vowels after R and T', 'Vowel entropy after R/T exceeds that after other consonants more than in Linear B',
           {'LA_rt_minus_other': round(f(LA), 3), 'LB_rt_minus_other': round(f(LB), 3), 'p': round(p, 4)},
           {'LA entropies (R/T, other)': (round(entropy_by_class(LA, True), 3), round(entropy_by_class(LA, False), 3)),
            'LB entropies (R/T, other)': (round(entropy_by_class(LB, True), 3), round(entropy_by_class(LB, False), 3))})
    return p


def J4():
    rows = []
    for r in B.READ['records']:
        for t in r['tokens']:
            if t['cls'] in ('word-with-unknown-sign', 'unidentified-sign'):
                for x in re.findall(r'\*\d+[A-Z]?', t['label']):
                    rows.append((r['site'], x))
    sc, gc = Counter(s for s, _ in rows), Counter(g for _, g in rows)
    rows = [(s, g) for s, g in rows if sc[s] >= 10 and gc[g] >= 5]
    sites = [s for s, _ in rows]
    real, p, nm = X.shuffle_test(lambda ls: X.chi2(list(zip(ls, [g for _, g in rows]))), sites, reps=REPS)
    tab = defaultdict(Counter)
    for s, g in rows:
        tab[g][s] += 1
    single = {g: dict(c) for g, c in tab.items() if len(c) == 1}
    record('J4 regional unread signs', 'Unread signs are associated with sites beyond chance',
           {'chi2': round(real, 1), 'null_mean': round(nm, 1), 'p': round(p, 4), 'tokens': len(rows), 'signs': len(tab)},
           {'signs attested at one site only': single})
    return p


FAMILIES = {'a-ta-i-*301': r'^A-TA-I-\*301', 'ja-sa-sa-ra': r'^J?A-SA-SA-RA', 'u-na-ka-na': r'^U-NA-(RU-)?KA-NA',
            'i-pi-na-ma': r'^I-PI-NA-M', 'si-ru-te': r'^SI-RU-T', 'ta-na-ra': r'^TA-NA-RA', 'a-di-ki-te': r'^A-DI-KI-TE'}


def J5():
    rows = []
    for r in B.READ['records']:
        if r['support'] in B.ADMIN:
            continue
        for t in r['tokens']:
            for fam, pat in FAMILIES.items():
                if re.match(pat, t['label']):
                    rows.append((fam, t['label'], r['site']))
    fams = defaultdict(list)
    for i, (fam, lab, site) in enumerate(rows):
        fams[fam].append(i)

    def stat(sites):
        tot = 0.0
        for fam, idx in fams.items():
            sub = [(rows[i][1], sites[i]) for i in idx]
            if len({v for v, _ in sub}) > 1 and len({s for _, s in sub}) > 1:
                tot += X.chi2(sub)
        return tot
    sites = [s for _, _, s in rows]
    real = stat(sites)
    null = []
    for _ in range(REPS):
        sh = list(sites)
        for fam, idx in fams.items():
            vals = [sites[i] for i in idx]
            rng.shuffle(vals)
            for i, v in zip(idx, vals):
                sh[i] = v
        null.append(stat(sh))
    p = B.pv(null, real)
    record('J5 regional formula variants', 'Formula word variants cluster by site',
           {'chi2_sum': round(real, 2), 'null_mean': round(sum(null) / len(null), 2), 'p': round(p, 4), 'tokens': len(rows)},
           {'variants by site': {fam: dict(Counter(f'{rows[i][1]} @ {rows[i][2]}' for i in idx)) for fam, idx in fams.items()}})
    return p


def J6():
    rows = [(x['record'], x['com'], x['q']) for x in T.ENTRIES if x['com'] and x['q'] > 0]
    site = {r['name']: r['site'] for r in B.READ['records']}
    rows = [(site.get(rec), c, log(q)) for rec, c, q in rows if site.get(rec)]
    sc = Counter((s, c) for s, c, _ in rows)
    rows = [r for r in rows if sc[(r[0], r[1])] >= 5]
    by_com = defaultdict(list)
    for i, (s, c, v) in enumerate(rows):
        by_com[c].append(i)

    def stat(sites):
        ss = 0.0
        for c, idx in by_com.items():
            vals = [rows[i][2] for i in idx]
            mu = sum(vals) / len(vals)
            g = defaultdict(list)
            for i in idx:
                g[sites[i]].append(rows[i][2])
            ss += sum(len(v) * (sum(v) / len(v) - mu) ** 2 for v in g.values())
        return ss
    sites = [s for s, _, _ in rows]
    real = stat(sites)
    null = []
    for _ in range(REPS):
        sh = list(sites)
        for c, idx in by_com.items():
            vals = [sites[i] for i in idx]
            rng.shuffle(vals)
            for i, v in zip(idx, vals):
                sh[i] = v
        null.append(stat(sh))
    p = B.pv(null, real)
    means = defaultdict(list)
    for s, c, v in rows:
        means[(c, s)].append(v)
    record('J6 amounts by site within commodity', 'Amounts differ by site within the same commodity',
           {'between_SS': round(real, 2), 'null_mean': round(sum(null) / len(null), 2), 'p': round(p, 4), 'entries': len(rows)},
           {'median-ish (geometric mean) by commodity and site': {f'{c} @ {s}': round(2.718281828 ** (sum(v) / len(v)), 1)
                                                                  for (c, s), v in sorted(means.items())}})
    return p


TESTS = [J1, J2, J3, J4, J5, J6]


def main():
    ps = {}
    for fn in TESTS:
        try:
            ps[fn.__name__] = fn()
        except Exception as ex:
            import traceback
            traceback.print_exc()
            out[fn.__name__] = {'error': str(ex)}
    tested = sorted([(p, k) for k, p in ps.items() if p is not None])
    m, cut = len(tested), 0
    for i, (p, k) in enumerate(tested, 1):
        if p <= 0.05 * i / m:
            cut = i
    supported = [k for _, k in tested[:cut]]
    res = {'method': __doc__.strip(), 'primary_p': ps, 'bh_supported': supported, 'details': out}
    (ROOT / 'reading/decipher6j_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str) + '\n', encoding='utf-8')
    print('\nprimary p:', {k: round(v, 4) for k, v in ps.items()})
    print('survive BH at 5%:', supported)


if __name__ == '__main__':
    main()
