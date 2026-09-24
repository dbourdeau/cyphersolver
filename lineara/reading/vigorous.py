"""Ten hypotheses that extend results already supported, each tested vigorously.

Each hypothesis states its prediction before the data are touched, has one primary test with its own null, and at
least one robustness check (held-out data, an alternative null, a stricter subset, a control that should fail).
Benjamini-Hochberg at 5% is applied across the ten primary p-values. A hypothesis is called supported only if its
primary test survives the correction and its robustness checks point the same way.

V1  Held-out prediction: a syllable model trained on Linear A names against part of the Pylos names scores Knossos
    names as more Minoan than held-out Pylos names (AUC > 0.5). Control: common words should not separate.
V2  Undeciphered Linear B signs: their frequencies at Knossos track the frequencies of the same sign numbers in
    Linear A more closely than their frequencies at Pylos do.
V3  The Linear A words found as stems of Knossos names (stem + one syllable) are Linear A names (entry labels) more
    often than Linear A words of the same length in general.
V4  The Knossos stem excess survives with stems of three or more signs only, and against Thebes, Mycenae and Tiryns.
V5  Paired A-: within stems attested both with A- and without it, the A- form stands in heading position more often.
V6  KI-RO appears on personnel tablets (VIR) more than other tablets with totals.
V7  The amounts on a tablet share a common divisor above 1 more often than amounts shuffled between tablets.
V8  Largest-first listing holds scribe by scribe at Haghia Triada, not only in aggregate.
V9  Linear A religious words resemble Knossos names more than Pylos names even without the libation-formula words.
V10 The largest-first convention for fractions is real: under the published values the attested pairs break it far
    less often than under random reassignments of the same values, so a firm exception such as HT 34 is meaningful.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
import json
from math import gcd, log
from functools import reduce
from itertools import permutations
from pathlib import Path
import re
import sys
import unicodedata as ud

sys.path.insert(0, str(Path(__file__).resolve().parent))
import batches as B  # noqa: E402

ROOT = B.ROOT
rng = B.rng
LA_SET = set(B.LA_TYPES)
LB = B.LB_SITES
CAT = B.LB_CAT
kn_only = [w for w, s in LB.items() if s == {'Knossos'}]
py_only = [w for w, s in LB.items() if s == {'Pylos'}]
out = {}


def record(key, prediction, primary, robustness, verdict_hint=''):
    out[key] = {'prediction': prediction, 'primary': primary, 'robustness': robustness}
    print(f"== {key}: {prediction}\n   primary {primary}\n   robustness {robustness}")


# V1 held-out prediction ---------------------------------------------------
def nb_model(words):
    c = Counter(s for w in words for s in w)
    n, v = sum(c.values()), len(c) + 1
    return lambda s: log((c.get(s, 0) + 0.5) / (n + 0.5 * v))


def auc(pos, neg):
    """Mann-Whitney AUC by ranks (ties averaged)."""
    allv = sorted([(v, 0) for v in pos] + [(v, 1) for v in neg])
    ranks, i = {}, 0
    rsum = 0.0
    while i < len(allv):
        j = i
        while j < len(allv) and allv[j][0] == allv[i][0]:
            j += 1
        r = (i + j + 1) / 2
        rsum += r * sum(1 for k in range(i, j) if allv[k][1] == 0)
        i = j
    n1, n2 = len(pos), len(neg)
    return (rsum - n1 * (n1 + 1) / 2) / (n1 * n2)


def heldout_auc(la_model, kn, py, splits):
    out_ = []
    for _ in range(splits):
        pys = py[:]
        rng.shuffle(pys)
        cut = int(0.7 * len(pys))
        mpy = nb_model(pys[:cut])
        score = lambda w: sum(la_model(s) - mpy(s) for s in w) / len(w)
        out_.append(auc([score(w) for w in kn], [score(w) for w in pys[cut:]]))
    return out_


def V1():
    la = B.LA_NAMES
    kn = [w for w in kn_only if CAT.get(w) == 'anthroponym' and not any(x.startswith('*') for x in w)]
    py = [w for w in py_only if CAT.get(w) == 'anthroponym' and not any(x.startswith('*') for x in w)]
    kn_c = [w for w in kn_only if w in CAT and CAT[w] not in ('anthroponym', 'toponym', 'ethnic', 'theonym')]
    py_c = [w for w in py_only if w in CAT and CAT[w] not in ('anthroponym', 'toponym', 'ethnic', 'theonym')]
    mla = nb_model(la)
    aucs = sorted(heldout_auc(mla, kn, py, 200))
    ctrl = sorted(heldout_auc(mla, kn_c, py_c, 200))
    real = sum(aucs) / len(aucs)
    # null: shuffle the Knossos/Pylos labels among the names, then repeat the whole train/test procedure
    pool, k, null = kn + py, len(kn), []
    for _ in range(400):
        rng.shuffle(pool)
        a = heldout_auc(mla, pool[:k], pool[k:], 10)
        null.append(sum(a) / len(a))
    p = B.pv(null, real)
    record('V1 held-out prediction', 'Knossos names score as more Minoan than held-out Pylos names',
           {'mean_auc': round(real, 3), 'auc_95_over_splits': [round(aucs[5], 3), round(aucs[194], 3)],
            'label_permutation_null_mean': round(sum(null) / len(null), 3), 'p': round(p, 4)},
           {'control common words auc': round(sum(ctrl) / len(ctrl), 3), 'control_95': [round(ctrl[5], 3), round(ctrl[194], 3)],
            'note': 'held-out Pylos names were never in the Pylos model; Knossos names were never in any model'})
    return p


# V2 undeciphered signs ------------------------------------------------------
def la_sign_freq():
    c = Counter()
    for r in B.CORPUS.values():
        for w in r['words']:
            for ch in w:
                m = re.fullmatch(r'LINEAR A SIGN AB?(\d+)[A-Z]*', ud.name(ch, ''))
                if m:
                    c[int(m.group(1))] += 1
    return c


def V2():
    la = la_sign_freq()
    kn = Counter(int(x[1:3]) for w in kn_only for x in w if re.fullmatch(r'\*\d+', x))
    py = Counter(int(x[1:3]) for w in py_only for x in w if re.fullmatch(r'\*\d+', x))
    signs = sorted(set(kn) | set(py))
    x = [la.get(s, 0) for s in signs]
    real = B.spearman(x, [kn.get(s, 0) for s in signs]) - B.spearman(x, [py.get(s, 0) for s in signs])
    kn_tok = [(int(x_[1:3])) for w in kn_only for x_ in w if re.fullmatch(r'\*\d+', x_)]
    py_tok = [(int(x_[1:3])) for w in py_only for x_ in w if re.fullmatch(r'\*\d+', x_)]
    null = []
    pool = kn_tok + py_tok
    for _ in range(B.REPS):
        rng.shuffle(pool)
        k, p_ = Counter(pool[:len(kn_tok)]), Counter(pool[len(kn_tok):])
        null.append(B.spearman(x, [k.get(s, 0) for s in signs]) - B.spearman(x, [p_.get(s, 0) for s in signs]))
    p = B.pv(null, real)
    in_la = [s for s in signs if la.get(s, 0) > 0]
    record('V2 undeciphered signs', 'Knossos use of undeciphered signs tracks Linear A frequencies more than Pylos use',
           {'rho_KN': round(B.spearman(x, [kn.get(s, 0) for s in signs]), 3), 'rho_PY': round(B.spearman(x, [py.get(s, 0) for s in signs]), 3),
            'difference': round(real, 3), 'p': round(p, 4), 'signs': len(signs)},
           {'signs attested in Linear A': f'{len(in_la)} of {len(signs)}',
            'share of Knossos * tokens on signs attested in LA': round(sum(kn[s] for s in in_la) / max(1, sum(kn.values())), 3),
            'share of Pylos * tokens on signs attested in LA': round(sum(py[s] for s in in_la) / max(1, sum(py.values())), 3)})
    return p


# V3 stems are name stems ------------------------------------------------------
def V3():
    names_la = {w for w in B.LA_NAMES}
    kn_names = [w for w in kn_only if CAT.get(w) == 'anthroponym']
    stems = {w[:-1] for w in kn_names if len(w) >= 3 and w[:-1] in LA_SET}
    real = sum(s in names_la for s in stems) / len(stems)
    by_len = defaultdict(list)
    for w in LA_SET:
        by_len[len(w)].append(w)
    need = Counter(len(s) for s in stems)
    null = []
    for _ in range(B.REPS):
        smp = [w for L, n in need.items() for w in rng.sample(by_len[L], min(n, len(by_len[L])))]
        null.append(sum(w in names_la for w in smp) / len(smp))
    p = B.pv(null, real)
    pystems = {w[:-1] for w in py_only if CAT.get(w) == 'anthroponym' and len(w) >= 3 and w[:-1] in LA_SET}
    record('V3 stems are name stems', 'Linear A stems of Knossos names are Linear A names more often than same-length Linear A words',
           {'share_names': round(real, 3), 'null_mean': round(sum(null) / len(null), 3), 'p': round(p, 4), 'stems': len(stems)},
           {'same share for stems of Pylos names': round(sum(s in names_la for s in pystems) / max(1, len(pystems)), 3),
            'pylos stems': len(pystems)})
    return p


# V4 stems, strict --------------------------------------------------------------
def stem_rate(ws, la, minstem):
    elig = [w for w in ws if len(w) >= minstem + 1]
    return sum(1 for w in elig if w[:-1] in la) / len(elig)


def V4():
    la3 = {w for w in LA_SET if len(w) >= 3}
    real = stem_rate(kn_only, la3, 3) - stem_rate(py_only, la3, 3)
    pool, k = kn_only + py_only, len(kn_only)
    null = []
    for _ in range(B.REPS):
        rng.shuffle(pool)
        null.append(stem_rate(pool[:k], la3, 3) - stem_rate(pool[k:], la3, 3))
    p = B.pv(null, real)
    la2 = {w for w in LA_SET if len(w) >= 2}
    other_main = [w for w, s in LB.items() if s and s <= {'Thebes', 'Mycenae', 'Tiryns', 'Vases - Thebes', 'Vases - Tiryns', 'Vases - Mycenae'}]
    r2 = stem_rate(kn_only, la2, 2) - stem_rate(other_main, la2, 2)
    pool2, k2 = kn_only + other_main, len(kn_only)
    null2 = []
    for _ in range(B.REPS):
        rng.shuffle(pool2)
        null2.append(stem_rate(pool2[:k2], la2, 2) - stem_rate(pool2[k2:], la2, 2))
    record('V4 stems, strict', 'The Knossos stem excess holds for 3+-sign stems, and against other mainland sites',
           {'KN_rate_3plus': round(stem_rate(kn_only, la3, 3), 4), 'PY_rate_3plus': round(stem_rate(py_only, la3, 3), 4),
            'difference': round(real, 4), 'p': round(p, 4)},
           {'vs Thebes/Mycenae/Tiryns (2+ stems)': {'KN': round(stem_rate(kn_only, la2, 2), 4), 'other': round(stem_rate(other_main, la2, 2), 4),
                                                    'p': round(B.pv(null2, r2), 4), 'n_other': len(other_main)}})
    return p


# V5 paired A- ------------------------------------------------------------------
def V5():
    fn = defaultdict(Counter)
    for r, t, w in B.LA_ADMIN:
        fn[w][t.get('function')] += 1
    pairs = []
    for w in list(fn):
        if w[0] == 'a' and len(w) >= 3 and w[1:] in fn:
            a, b = fn[w], fn[w[1:]]
            ha = a['heading'] / sum(a.values())
            hb = b['heading'] / sum(b.values())
            pairs.append(('-'.join(w).upper(), round(ha, 2), round(hb, 2)))
    plus = sum(1 for _, a, b in pairs if a > b)
    minus = sum(1 for _, a, b in pairs if a < b)
    n = plus + minus
    from math import comb
    p = sum(comb(n, k) for k in range(plus, n + 1)) / 2 ** n if n else 1.0
    record('V5 paired A-', 'Within the same stem the A- form is a heading more often than the bare form',
           {'pairs': len(pairs), 'A- more often heading': plus, 'bare more often heading': minus, 'sign_test_p': round(p, 4)},
           {'pairs_detail': pairs})
    return p if n else None


# V6 KI-RO and personnel ------------------------------------------------------
def V6():
    recs = [r for r in B.READ['records'] if r['support'] in B.ADMIN and any(t['label'] in ('KU-RO', 'KI-RO') for t in r['tokens'])]
    has_vir = lambda r: int(any(t['cls'] == 'commodity' and t['label'].startswith('VIR') for t in r['tokens']))
    kiro = [has_vir(r) for r in recs if any(t['label'] == 'KI-RO' for t in r['tokens'])]
    other = [has_vir(r) for r in recs if not any(t['label'] == 'KI-RO' for t in r['tokens'])]
    e, p = B.diff_means(kiro, other)
    # robustness: KI-RO lists with all-1 entries (from batches2 L4 logic)
    ones = [x['q'] == 1 for x in B.entries_with(lambda ts: True) if x['section'] == 'KI-RO']
    record('V6 KI-RO and personnel', 'KI-RO appears on personnel (VIR) tablets more than other tablets with totals',
           {'KI-RO tablets with VIR': f'{sum(kiro)}/{len(kiro)}', 'other total tablets with VIR': f'{sum(other)}/{len(other)}', 'p': round(p, 4)},
           {'KI-RO entries equal to 1': f'{sum(ones)}/{len(ones)}'})
    return p


# V7 common divisor -------------------------------------------------------------
def V7():
    recs = defaultdict(list)
    for x in B.entries_with(lambda ts: True):
        recs[x['record']].append(int(x['q']))
    lists = [q for q in recs.values() if len(q) >= 3]
    share = lambda ls: sum(reduce(gcd, q) >= 2 for q in ls) / len(ls)
    real = share(lists)
    def perm_p(ls, reps):
        allq = [x for q in ls for x in q]
        null = []
        for _ in range(reps):
            pool = allq[:]
            rng.shuffle(pool)
            k, sh = 0, []
            for q in ls:
                sh.append(pool[k:k + len(q)])
                k += len(q)
            null.append(share(sh))
        return B.pv(null, share(ls)), sum(null) / len(null)
    p, nm = perm_p(lists, B.REPS)
    no10 = [q for q in lists if not all(x % 10 == 0 for x in q)]
    p10, nm10 = perm_p(no10, B.REPS)
    # within-site shuffle: amounts move only between tablets of the same site
    site_of = {r['name']: r['site'] for r in B.READ['records']}
    by_site = defaultdict(list)
    for rec, q in recs.items():
        if len(q) >= 3:
            by_site[site_of.get(rec)].append(q)
    null_s = []
    for _ in range(B.REPS):
        sh = []
        for ls in by_site.values():
            pool = [x for q in ls for x in q]
            rng.shuffle(pool)
            k = 0
            for q in ls:
                sh.append(pool[k:k + len(q)])
                k += len(q)
        null_s.append(share(sh))
    record('V7 common divisor', 'Amounts on a tablet share a common divisor above 1 more often than chance',
           {'share_gcd_ge_2': round(real, 3), 'null_mean': round(nm, 3), 'p': round(p, 4), 'tablets': len(lists)},
           {'without all-multiples-of-10 tablets': {'share': round(share(no10), 3), 'null_mean': round(nm10, 3), 'p': round(p10, 4), 'tablets': len(no10)},
            'within-site shuffle p': round(B.pv(null_s, real), 4),
            'gcd distribution': dict(Counter(min(reduce(gcd, q), 11) for q in lists))})
    return p


# V8 largest first by scribe ------------------------------------------------------
def V8():
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

    def tau(v):
        c = d = 0
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                c += v[i] > v[j]
                d += v[i] < v[j]
        return (c - d) / max(1, c + d)
    scribes = {s: sum(map(tau, v)) / len(v) for s, v in by.items() if len(v) >= 3}
    plus = sum(1 for x in scribes.values() if x > 0)
    n = sum(1 for x in scribes.values() if x != 0)
    from math import comb
    p = sum(comb(n, k) for k in range(plus, n + 1)) / 2 ** n if n else 1.0
    record('V8 largest first by scribe', 'The largest-first habit holds scribe by scribe at Haghia Triada',
           {'scribes': len(scribes), 'with positive tau': plus, 'sign_test_p': round(p, 4)},
           {'per_scribe_tau': {s: round(v, 3) for s, v in scribes.items()}})
    return p


# V9 religious words without the formula --------------------------------------------
FORMULA = re.compile(r'A-TA-I-\*301|DI-KI-T|SA-SA-RA|U-NA-(RU-)?KA|I-PI-NA-M|SI-RU|U-TI-NU|TU-RU-SA|O-SU-QA-RE|I-DA')


def V9():
    rel = sorted({w for r, t, w in B.LA_RELIG if not FORMULA.search('-'.join(w).upper())})
    kn = [w for w in kn_only if CAT.get(w) == 'anthroponym' and not any(x.startswith('*') for x in w)]
    py = [w for w in py_only if CAT.get(w) == 'anthroponym' and not any(x.startswith('*') for x in w)]
    t = B.S.test(rel, kn, py, rng, B.REPS)
    record('V9 religious words without the formula', 'Non-formula religious words also resemble Knossos names more than Pylos names',
           {'words': len(rel), 'D_all': t['all']['D'], 'p': t['all']['p_knossos_closer']},
           {'first syllables': (t['first']['D'], t['first']['p_knossos_closer'])})
    return t['all']['p_knossos_closer']


# V10 fraction order convention --------------------------------------------------------
def V10():
    order = json.loads((ROOT / 'fraction_order_results.json').read_text(encoding='utf-8'))
    vals = dict(J=F(1, 2), E=F(1, 4), F=F(1, 8), H=F(1, 16), A=F(1, 24), B=F(1, 5), D=F(1, 6), K=F(1, 10), L2=F(1, 20),
                L3=F(1, 30), L4=F(1, 40), L6=F(1, 60))
    pairs = []
    for key, info in order['adjacent_pairs'].items():
        a, b = key.split()
        if a in vals and b in vals and key not in ('E J',):  # E J flagged doubtful by Corazza et al.
            pairs += [(a, b)] * info['count']
    viol = lambda v: sum(v[a] <= v[b] for a, b in pairs)
    real = viol(vals)
    signs, values = list(vals), list(vals.values())
    null = []
    for _ in range(20000):
        rng.shuffle(values)
        null.append(viol(dict(zip(signs, values))))
    p = (sum(n <= real for n in null) + 1) / (len(null) + 1)
    bad = [f'{a} {b}' for a, b in pairs if vals[a] <= vals[b]]
    record('V10 fraction order convention', 'Published values break largest-first far less than random reassignments',
           {'pairs': len(pairs), 'violations_published': real, 'violations_random_mean': round(sum(null) / len(null), 2),
            'p': round(p, 5)},
           {'the violations': bad,
            'P(random assignment has <= 1 violation)': round(sum(n <= 1 for n in null) / len(null), 5),
            'circularity': 'Corazza et al. 2021 used the descending-order premise when assigning some of these values, '
                           'so agreement with it is partly built in; this is not independent support'})
    return p


def main():
    ps = {}
    for fn in (V1, V2, V3, V4, V5, V6, V7, V8, V9, V10):
        try:
            ps[fn.__name__] = fn()
        except Exception as ex:
            out[fn.__name__] = {'error': str(ex)}
            ps[fn.__name__] = None
            print(fn.__name__, 'error', ex)
    tested = sorted([(p, k) for k, p in ps.items() if p is not None])
    m, cut = len(tested), 0
    for i, (p, k) in enumerate(tested, 1):
        if p <= 0.05 * i / m:
            cut = i
    supported = [k for _, k in tested[:cut]]
    res = {'method': __doc__.strip(), 'primary_p': ps, 'bh_supported': supported, 'details': out}
    (ROOT / 'reading/vigorous_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str) + '\n', encoding='utf-8')
    print('\nprimary p:', {k: (round(v, 4) if v is not None else None) for k, v in ps.items()})
    print('survive BH at 5%:', supported)


if __name__ == '__main__':
    main()
