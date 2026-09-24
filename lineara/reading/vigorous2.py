"""Ten more follow-ups to the supported results of vigorous.py, tested the same way.

Each hypothesis has a prediction stated before the data are touched, one primary test with its own null, and at
least one robustness check. Benjamini-Hochberg at 5% runs across the ten primary p-values; a hypothesis counts as
supported only if it survives and its robustness checks agree.

W1  Not just Pylos: the V1 model (Linear A names against 70% of the Pylos names) rates Knossos names as more Minoan
    than the personal names of Thebes, Mycenae and Tiryns, which it never saw.
W2  Not just Haghia Triada: a model trained on Linear A names from sites other than Haghia Triada still rates
    Knossos names above held-out Pylos names.
W3  The earliest Knossos deposit, the Room of Chariot Tablets (LM II-IIIA1), has more Minoan-looking personal names
    than the later Knossos deposits.
W4  Knossos words written with undeciphered signs are Minoan in their other syllables too: with the undeciphered
    signs removed, they score as more Linear A-like than other Knossos words.
W5  The word-internal o-deficit of Knossos names holds against Thebes, Mycenae and Tiryns names, not only Pylos.
W6  Religious words as a training set: a model trained on Linear A religious words (no list names) against 70% of
    the Pylos names also rates Knossos names above held-out Pylos names.
W7  Tablets whose amounts share a common divisor (V7) are single-commodity lists more often than other tablets.
W8  KI-RO (rare on personnel tablets, V6) stands on tablets of produce (grain, wine, oil, olives, figs, spice) more
    than other tablets with totals.
W9  Largest-first at Haghia Triada is not carried by one scribe: a within-list order-shuffle test stays significant
    with the scribe who wrote most lists removed.
W10 The Linear A words that turn up as stems of Knossos words are widespread words: attested at more Linear A sites
    than Linear A words of the same length.
"""
from collections import Counter, defaultdict
import json
from math import comb
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import batches as B  # noqa: E402
import vigorous as V  # noqa: E402

ROOT = B.ROOT
rng = B.rng
LA_SET = set(B.LA_TYPES)
LB, CAT = B.LB_SITES, B.LB_CAT
kn_only, py_only = V.kn_only, V.py_only
MAIN = {'Thebes', 'Mycenae', 'Tiryns', 'Vases - Thebes', 'Vases - Tiryns', 'Vases - Mycenae', 'Midea', 'Vases - Midea'}
clean = lambda w: not any(x.startswith('*') for x in w)
KN_N = [w for w in kn_only if CAT.get(w) == 'anthroponym' and clean(w)]
PY_N = [w for w in py_only if CAT.get(w) == 'anthroponym' and clean(w)]
MA_N = [w for w, s in LB.items() if s and s <= MAIN and CAT.get(w) == 'anthroponym' and clean(w) and len(w) >= 2]
out = {}
record = V.record


def fixed_model_auc(la_model, py_train, pos, neg):
    mpy = V.nb_model(py_train)
    score = lambda w: sum(la_model(s) - mpy(s) for s in w) / len(w)
    return V.auc([score(w) for w in pos], [score(w) for w in neg])


def label_perm(stat, a, b, reps):
    real = stat(a, b)
    pool, k, null = a + b, len(a), []
    for _ in range(reps):
        rng.shuffle(pool)
        null.append(stat(pool[:k], pool[k:]))
    return real, B.pv(null, real), sum(null) / len(null)


# W1 --------------------------------------------------------------------------------
def W1():
    mla = V.nb_model(B.LA_NAMES)
    splits = []
    for _ in range(20):
        p = PY_N[:]
        rng.shuffle(p)
        splits.append(p[:int(0.7 * len(p))])
    stat = lambda a, b: sum(fixed_model_auc(mla, tr, a, b) for tr in splits[:5]) / 5
    real, p, nm = label_perm(stat, KN_N, MA_N, 1000)
    # robustness: Pylos-free model, Linear A names against all common Linear B words
    commons = [w for w, s in LB.items() if CAT.get(w) == 'other' and clean(w)]
    alt = fixed_model_auc(mla, commons, KN_N, MA_N)
    alt_r, alt_p, _ = label_perm(lambda a, b: fixed_model_auc(mla, commons, a, b), KN_N, MA_N, 1000)
    record('W1 not just Pylos', 'Knossos names score as more Minoan than Thebes/Mycenae/Tiryns names',
           {'auc': round(real, 3), 'null_mean': round(nm, 3), 'p': round(p, 4), 'n_kn': len(KN_N), 'n_mainland': len(MA_N)},
           {'model without Pylos (LA names vs Linear B common words)': {'auc': round(alt, 3), 'p': round(alt_p, 4)}})
    return p


# W2 --------------------------------------------------------------------------------
def la_names_by_site():
    by = defaultdict(set)
    for r in B.READ['records']:
        for t in r['tokens']:
            if t['cls'] == 'word' and t.get('function') == 'entry label':
                w = tuple(t['label'].lower().split('-'))
                if w in set(B.LA_NAMES):
                    by[r['site']].add(w)
    return by


def W2():
    by = la_names_by_site()
    non_ht = sorted({w for s, ws in by.items() if s != 'Haghia Triada' for w in ws})
    ht = sorted(by['Haghia Triada'])
    non_ht_kn = sorted({w for s, ws in by.items() if s not in ('Haghia Triada', 'Knossos') for w in ws})
    res = {}
    for name, la in (('non-HT', non_ht), ('HT', ht), ('non-HT, non-Knossos', non_ht_kn)):
        mla = V.nb_model(la)
        real = sum(V.heldout_auc(mla, KN_N, PY_N, 100)) / 100
        pool, k, null = KN_N + PY_N, len(KN_N), []
        for _ in range(300):
            rng.shuffle(pool)
            a = V.heldout_auc(mla, pool[:k], pool[k:], 5)
            null.append(sum(a) / len(a))
        res[name] = {'names': len(la), 'auc': round(real, 3), 'p': round(B.pv(null, real), 4)}
    record('W2 not just Haghia Triada', 'A model from non-HT Linear A names still separates Knossos from Pylos names',
           res['non-HT'], {'HT-only model': res['HT'], 'without Linear A names from Knossos': res['non-HT, non-Knossos'], 'sites in non-HT set': sorted(s for s in by if s != 'Haghia Triada')})
    return res['non-HT']['p']


# W3 --------------------------------------------------------------------------------
def knossos_findspots():
    fs = defaultdict(set)
    for name, rec in B.LB_RECS:
        if rec.get('site') != 'Knossos':
            continue
        spot = rec.get('findspot', '') or ''
        for t in rec.get('transliteratedWords', []):
            t = t.strip().lower()
            if '-' in t and not any(ch in t for ch in '[]?'):
                fs[tuple(t.split('-'))].add('RCT' if 'RCT' in spot else ('unknown' if not spot else 'later'))
    return fs


def W3():
    fs = knossos_findspots()
    rct = [w for w in KN_N if fs.get(w) == {'RCT'}]
    later = [w for w in KN_N if fs.get(w) == {'later'}]
    mla, mpy = V.nb_model(B.LA_NAMES), V.nb_model(PY_N)
    score = lambda w: sum(mla(s) - mpy(s) for s in w) / len(w)
    stat = lambda a, b: V.auc([score(w) for w in a], [score(w) for w in b])
    real, p, nm = label_perm(stat, rct, later, B.REPS)
    # robustness: JSD form, and with RCT names also found later included in RCT
    rct_any = [w for w in KN_N if 'RCT' in fs.get(w, set())]
    later_only = [w for w in KN_N if fs.get(w) == {'later'}]
    r2, p2, _ = label_perm(stat, rct_any, later_only, B.REPS)
    t = B.S.test(B.LA_NAMES, rct, later, rng, 2000)
    record('W3 earliest deposit', 'Room of Chariot Tablets names are more Minoan than later Knossos names',
           {'auc': round(real, 3), 'null_mean': round(nm, 3), 'p': round(p, 4), 'n_rct': len(rct), 'n_later': len(later)},
           {'RCT-any vs later-only': {'auc': round(r2, 3), 'p': round(p2, 4), 'n': [len(rct_any), len(later_only)]},
            'JSD test (RCT as the "Knossos" side)': {k: (v['D'], v['p_knossos_closer']) for k, v in t.items()}})
    return p


# W4 --------------------------------------------------------------------------------
def W4():
    mla = V.nb_model(B.LA_NAMES + [w for w in B.LA_TYPES])
    mpy = V.nb_model([w for w in py_only if clean(w)])

    def score(w):
        s = [x for x in w if not x.startswith('*')]
        return sum(mla(x) - mpy(x) for x in s) / len(s) if s else None
    star = [w for w in kn_only if not clean(w) and sum(1 for x in w if not x.startswith('*')) >= 2]
    plain = [w for w in kn_only if clean(w) and len(w) >= 2]
    a = [score(w) for w in star]
    b = [score(w) for w in plain]
    stat = lambda x, y: V.auc(x, y)
    real, p, nm = label_perm(stat, a, b, B.REPS)
    # robustness: same comparison at Pylos (should be weaker), and names only at Knossos
    pstar = [score(w) for w in py_only if not clean(w) and sum(1 for x in w if not x.startswith('*')) >= 2]
    pplain = [score(w) for w in py_only if clean(w) and len(w) >= 2]
    pr, pp, _ = label_perm(stat, pstar, pplain, B.REPS)
    # neutral reference: words from Thebes, Mycenae and Tiryns (neither Knossos nor Pylos) in place of Pylos words
    mref = V.nb_model([w for w, s_ in LB.items() if s_ and s_ <= MAIN and clean(w)])

    def score_n(w):
        s = [x for x in w if not x.startswith('*')]
        return sum(mla(x) - mref(x) for x in s) / len(s)
    neutral = {}
    for site, ws in (('Knossos', kn_only), ('Pylos', py_only)):
        st = [score_n(w) for w in ws if not clean(w) and sum(1 for x in w if not x.startswith('*')) >= 2]
        pl = [score_n(w) for w in ws if clean(w) and len(w) >= 2]
        r_, p_, _ = label_perm(stat, st, pl, B.REPS)
        neutral[site] = {'auc': round(r_, 3), 'p': round(p_, 4)}
    record('W4 undeciphered-sign words', 'Knossos words with undeciphered signs are more Linear A-like in their other syllables',
           {'auc': round(real, 3), 'null_mean': round(nm, 3), 'p': round(p, 4), 'n_star': len(a), 'n_plain': len(b)},
           {'same at Pylos (Pylos plain words were in the reference model, biased upward)': {'auc': round(pr, 3), 'p': round(pp, 4), 'n_star': len(pstar)},
            'neutral reference model (Thebes/Mycenae/Tiryns words)': neutral})
    return p


# W5 --------------------------------------------------------------------------------
def internal_o(ws):
    s = [x for w in ws for x in w[:-1]]
    return sum(x.endswith('o') for x in s) / len(s)


def W5():
    real, p, nm = label_perm(lambda a, b: internal_o(b) - internal_o(a), KN_N, MA_N, B.REPS)
    r2, p2, _ = label_perm(lambda a, b: internal_o(b) - internal_o(a), KN_N, PY_N, B.REPS)
    record('W5 o-deficit vs other mainland', 'Knossos names have fewer internal o-syllables than Thebes/Mycenae/Tiryns names',
           {'KN': round(internal_o(KN_N), 4), 'mainland': round(internal_o(MA_N), 4), 'p': round(p, 4)},
           {'vs Pylos (replication)': {'PY': round(internal_o(PY_N), 4), 'p': round(p2, 4)},
            'Linear A internal o': round(internal_o(B.LA_TYPES), 4)})
    return p


# W6 --------------------------------------------------------------------------------
def W6():
    names = set(B.LA_NAMES)
    rel = sorted({w for _, _, w in B.LA_RELIG if w not in names})
    rel_nf = [w for w in rel if not V.FORMULA.search('-'.join(w).upper())]
    res = {}
    for name, la in (('religious', rel), ('religious, formula removed', rel_nf)):
        mla = V.nb_model(la)
        real = sum(V.heldout_auc(mla, KN_N, PY_N, 100)) / 100
        pool, k, null = KN_N + PY_N, len(KN_N), []
        for _ in range(300):
            rng.shuffle(pool)
            a = V.heldout_auc(mla, pool[:k], pool[k:], 5)
            null.append(sum(a) / len(a))
        res[name] = {'words': len(la), 'auc': round(real, 3), 'p': round(B.pv(null, real), 4)}
    record('W6 religious-word model', 'A model trained on Linear A religious words picks out Knossos names out of sample',
           res['religious'], {'formula removed': res['religious, formula removed']})
    return res['religious']['p']


# W7 --------------------------------------------------------------------------------
def tablet_lists():
    recs = defaultdict(lambda: {'q': [], 'com': set()})
    for x in B.entries_with(lambda ts: True):
        recs[x['record']]['q'].append(int(x['q']))
        if x['com']:
            recs[x['record']]['com'].add(x['com'])
    return {k: v for k, v in recs.items() if len(v['q']) >= 3}


def W7():
    from functools import reduce
    from math import gcd
    t = tablet_lists()
    div = [int(len(v['com']) <= 1) for v in t.values() if reduce(gcd, v['q']) >= 2]
    oth = [int(len(v['com']) <= 1) for v in t.values() if reduce(gcd, v['q']) < 2]
    e, p = B.diff_means(div, oth)
    div2 = [int(len(v['com']) <= 1) for v in t.values() if reduce(gcd, v['q']) >= 2 and not all(x % 10 == 0 for x in v['q'])]
    e2, p2 = B.diff_means(div2, oth)
    coms = Counter(c for v in t.values() if reduce(gcd, v['q']) >= 2 for c in v['com'])
    record('W7 common-divisor tablets', 'Tablets with a common divisor are single-commodity lists more often',
           {'divisor tablets single-commodity': f'{sum(div)}/{len(div)}', 'others': f'{sum(oth)}/{len(oth)}', 'p': round(p, 4)},
           {'without all-tens tablets': {'share': f'{sum(div2)}/{len(div2)}', 'p': round(p2, 4)},
            'commodities on divisor tablets': dict(coms)})
    return p


# W8 --------------------------------------------------------------------------------
PRODUCE = ('GRA', 'VIN', 'OLE', 'OLIV', 'FIC', 'CYP', 'HORD')


def W8():
    recs = [r for r in B.READ['records'] if r['support'] in B.ADMIN and any(t['label'] in ('KU-RO', 'KI-RO') for t in r['tokens'])]
    has = lambda r, keys: int(any(t['cls'] == 'commodity' and any(t['label'].startswith(k) for k in keys) for t in r['tokens']))
    is_k = lambda r: any(t['label'] == 'KI-RO' for t in r['tokens'])
    kiro = [has(r, PRODUCE) for r in recs if is_k(r)]
    other = [has(r, PRODUCE) for r in recs if not is_k(r)]
    e, p = B.diff_means(kiro, other)
    ht = [r for r in recs if r['site'] == 'Haghia Triada']
    e2, p2 = B.diff_means([has(r, PRODUCE) for r in ht if is_k(r)], [has(r, PRODUCE) for r in ht if not is_k(r)])
    com = Counter(re.findall(r'[A-Z]{3,}', t['label'])[0] for r in recs if is_k(r) for t in r['tokens'] if t['cls'] == 'commodity')
    record('W8 KI-RO and produce', 'KI-RO stands on produce tablets more than other tablets with totals',
           {'KI-RO tablets with produce': f'{sum(kiro)}/{len(kiro)}', 'others': f'{sum(other)}/{len(other)}', 'p': round(p, 4)},
           {'Haghia Triada only p': round(p2, 4), 'commodities on KI-RO tablets': dict(com)})
    return p


# W9 --------------------------------------------------------------------------------
def ht_lists():
    by = defaultdict(list)
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN or r['site'] != 'Haghia Triada' or not r['scribe']:
            continue
        seq = []
        for t in r['tokens']:
            if t['cls'] == 'number':
                seq.append(t['value'])
            elif t['label'] in ('KU-RO', 'KI-RO', 'PO-TO-KU-RO', '—'):
                if len(seq) >= 4:
                    by[r['scribe']].append(seq[1:])
                seq = []
        if len(seq) >= 4:
            by[r['scribe']].append(seq[1:])
    return by


def tau(v):
    c = d = 0
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            c += v[i] > v[j]
            d += v[i] < v[j]
    return (c - d) / max(1, c + d)


def order_test(lists, reps):
    real = sum(map(tau, lists)) / len(lists)
    null = []
    for _ in range(reps):
        tot = 0
        for v in lists:
            v2 = v[:]
            rng.shuffle(v2)
            tot += tau(v2)
        null.append(tot / len(lists))
    return real, B.pv(null, real)


def W9():
    by = ht_lists()
    top = max(by, key=lambda s: len(by[s]))
    rest = [v for s, vs in by.items() if s != top for v in vs]
    real, p = order_test(rest, 2000)
    loo = {}
    for s in by:
        if len(by[s]) >= 2:
            ls = [v for s2, vs in by.items() if s2 != s for v in vs]
            loo[s] = round(order_test(ls, 1000)[1], 4)
    allr, allp = order_test([v for vs in by.values() for v in vs], 2000)
    record('W9 largest first without the main scribe', f'Largest-first holds at Haghia Triada with {top} removed',
           {'mean_tau': round(real, 3), 'p': round(p, 4), 'lists': len(rest), 'removed': top},
           {'all scribes': {'mean_tau': round(allr, 3), 'p': round(allp, 4)}, 'leave-one-scribe-out p': loo})
    return p


# W10 --------------------------------------------------------------------------------
def la_sites_of():
    s = defaultdict(set)
    for r in B.READ['records']:
        for t in r['tokens']:
            if t['cls'] == 'word':
                s[tuple(t['label'].lower().split('-'))].add(r['site'])
    return s


def W10():
    sites = la_sites_of()
    stems = sorted({w[:-1] for w in kn_only if len(w) >= 3 and w[:-1] in LA_SET})
    real = sum(len(sites.get(s, ())) for s in stems) / len(stems)
    by_len = defaultdict(list)
    for w in LA_SET:
        by_len[len(w)].append(w)
    need = Counter(len(s) for s in stems)
    null = []
    for _ in range(B.REPS):
        smp = [w for L, n in need.items() for w in rng.sample(by_len[L], min(n, len(by_len[L])))]
        null.append(sum(len(sites.get(w, ())) for w in smp) / len(smp))
    p = B.pv(null, real)
    py_stems = sorted({w[:-1] for w in py_only if len(w) >= 3 and w[:-1] in LA_SET})
    need_p = Counter(len(s) for s in py_stems)
    real_p = sum(len(sites.get(s, ())) for s in py_stems) / len(py_stems)
    null_p = []
    for _ in range(B.REPS):
        smp = [w for L, n in need_p.items() for w in rng.sample(by_len[L], min(n, len(by_len[L])))]
        null_p.append(sum(len(sites.get(w, ())) for w in smp) / len(smp))
    # Knossos against Pylos stems directly
    kp_real, kp_p, _ = label_perm(lambda a, b: sum(len(sites.get(s, ())) for s in a) / len(a) - sum(len(sites.get(s, ())) for s in b) / len(b),
                                  stems, py_stems, B.REPS)
    multi = lambda ss: sum(len(sites.get(s, ())) >= 2 for s in ss) / max(1, len(ss))
    record('W10 stems are widespread words', 'Linear A words used as Knossos stems are attested at more Linear A sites',
           {'mean_sites': round(real, 3), 'null_mean': round(sum(null) / len(null), 3), 'p': round(p, 4), 'stems': len(stems)},
           {'share at 2+ sites': round(multi(stems), 3), 'Pylos stems share at 2+ sites': round(multi(py_stems), 3),
            'pylos stems': len(py_stems), 'Pylos stems mean sites': round(real_p, 3), 'Pylos stems p vs null': round(B.pv(null_p, real_p), 4),
            'Knossos minus Pylos stems': {'diff': round(kp_real, 3), 'p': round(kp_p, 4)}})
    return p


def main():
    ps = {}
    for fn in (W1, W2, W3, W4, W5, W6, W7, W8, W9, W10):
        try:
            ps[fn.__name__] = fn()
        except Exception as ex:
            import traceback
            traceback.print_exc()
            V.out[fn.__name__] = {'error': str(ex)}
            ps[fn.__name__] = None
    tested = sorted([(p, k) for k, p in ps.items() if p is not None])
    m, cut = len(tested), 0
    for i, (p, k) in enumerate(tested, 1):
        if p <= 0.05 * i / m:
            cut = i
    supported = [k for _, k in tested[:cut]]
    res = {'method': __doc__.strip(), 'primary_p': ps, 'bh_supported': supported, 'details': V.out}
    (ROOT / 'reading/vigorous2_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str) + '\n', encoding='utf-8')
    print('\nprimary p:', {k: (round(v, 4) if v is not None else None) for k, v in ps.items()})
    print('survive BH at 5%:', supported)


if __name__ == '__main__':
    main()
