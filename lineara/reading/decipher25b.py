"""Twenty-five further hypotheses, building on decipher25.py: the coronal conditioning of Minoan e/o, persons kept
by one scribe, recopied lists, and a recheck of earlier per-tablet results with the two sides of each tablet merged
(the corpus stores HT 9a and HT 9b as separate records).

Each has a prediction stated before the test ran and one primary test with its own null. Benjamini-Hochberg at
5% runs across all twenty-five. Every per-tablet test here merges sides a and b.

Rechecks with sides merged
E1  Amounts on a tablet share a common divisor above 1 more often than chance (V7).
E2  Amounts on a tablet are exact doubles of each other more often than chance (L3).
E3  Tablets by the same scribe share more vocabulary than tablets by different scribes (H-batch).
E4  KI-RO is rarer on personnel (VIR) tablets than on other tablets with totals (V6).
The coronal pattern
E5  e alone follows coronals more than non-coronals, more so than in Linear B.
E6  The coronal pattern holds outside Haghia Triada (and at Haghia Triada).
E7  The coronal pattern holds in Linear A list names.
E8  The consonant of the same syllable predicts e/o more than the consonant of the next syllable.
E9  Among e, i, o, u, e/o take a larger share after coronals than in Linear B (e/o stand where i/u stand elsewhere).
Scribes and persons
E10 Scribes specialise in commodities (scribe-commodity association above chance).
E11 Scribes specialise in transaction terms (SA-RA2, KA-PA, A-DU, DA-RE, KU-PA).
E12 Recopied lists (tablet pairs sharing three or more entry words) give the same amounts for the same entries.
E13 Recurring entry words stay at one site more than chance.
Vowels
E14 Eteocretan e/o follow coronals more than non-coronals, more so than in Greek.
E15 Knossos-only place names show the coronal e/o pattern more than Pylos-only ones (ending removed).
E16 u follows labial and velar consonants (p m w k q) more than other consonants, more so than in Linear B.
E17 e/o syllables cluster within words (words with two or more e/o syllables exceed chance). Control: Linear B.
Knossos names (scored on the stem, final syllable removed, to avoid the -a artefact of D13)
E18 Minoan-shaped Knossos names cluster by Linear B scribe.
E19 Knossos names on personnel (VIR) tablets are more Minoan-shaped than names on other tablets.
Signs
E20 The consonant-row cohesion of decipher10 Y1 holds with left-context features only.
E21 It holds with right-context features only.
E22 The Z row keeps company with the J row more than with other rows.
Accounts
E23 Fraction use depends on the scribe (scribe-fraction association above chance).
E24 Entry words in KI-RO sections recur on other tablets more than main-section entry words.
E25 Recopied lists keep their order (shared entries in the same order, Kendall tau above chance).
"""
from collections import Counter, defaultdict
from functools import reduce
import json
from math import gcd, log
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import decipher25 as T  # noqa: E402

B, D, Db, E, V = T.B, T.D, T.Db, T.E, T.V
ROOT = B.ROOT
rng = T.rng
REPS = 1000
out = D.out
out.clear()
record = D.record
grid = D.grid
LA, LB = T.LA, T.LB
COR, NONCOR, RARE = T.COR, T.NONCOR, T.RARE
whole = lambda rec: re.sub(r'(?<=\d)[ab]$', '', rec)
SCRIBE_W = {}
for _rec, _s in T.SCRIBE.items():
    if _s:
        SCRIBE_W.setdefault(whole(_rec), _s)
TERMS = {'SA-RA2', 'A-DU', 'KA-PA', 'DA-RE', 'KU-PA', 'SA-MA', 'KU-RO', 'KI-RO', 'PO-TO-KU-RO'}


def chi2(pairs):
    c = Counter(pairs)
    n = len(pairs)
    rows = Counter(a for a, _ in pairs)
    cols = Counter(b for _, b in pairs)
    return sum((c[(r, k)] - rows[r] * cols[k] / n) ** 2 / (rows[r] * cols[k] / n) for r in rows for k in cols)


def shuffle_test(stat, labels, reps=REPS, lower=False):
    real = stat(labels)
    labs = list(labels)
    null = []
    for _ in range(reps):
        rng.shuffle(labs)
        null.append(stat(labs))
    return real, (T.pv_lower(null, real) if lower else B.pv(null, real)), sum(null) / len(null)


# ------------------------------------------------------------------ per-tablet data, sides merged
def tablets():
    tabs = defaultdict(lambda: {'q': [], 'com': set(), 'words': set(), 'frac': False, 'kiro': False, 'kuro': False,
                                'site': None, 'terms': set()})
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        t = tabs[whole(r['name'])]
        t['site'] = r['site']
        for tok in r['tokens']:
            if tok['cls'] == 'commodity':
                m = re.findall(r'[A-Z]{3,}', tok['label'])
                if m:
                    t['com'].add(m[0])
            if tok['cls'] in ('word', 'term'):
                t['words'].add(tok['label'])
                if tok['label'] in TERMS:
                    t['terms'].add(tok['label'])
            if tok['cls'] in ('fraction', 'fraction-disputed', 'fraction-unvalued'):
                t['frac'] = True
            if tok['label'] == 'KI-RO':
                t['kiro'] = True
            if tok['label'] in ('KU-RO', 'PO-TO-KU-RO'):
                t['kuro'] = True
    for x in T.ENTRIES:
        tabs[whole(x['record'])]['q'].append(int(x['q']))
    return dict(tabs)


TABS = tablets()


# ------------------------------------------------------------------ rechecks
def amount_shuffle(lists, stat, reps=REPS):
    real = stat(lists)
    allq = [x for q in lists for x in q]
    null = []
    for _ in range(reps):
        rng.shuffle(allq)
        k, sh = 0, []
        for q in lists:
            sh.append(allq[k:k + len(q)])
            k += len(q)
        null.append(stat(sh))
    return real, B.pv(null, real), sum(null) / len(null)


def E1():
    lists = [t['q'] for t in TABS.values() if len(t['q']) >= 3]
    share = lambda ls: sum(reduce(gcd, q) >= 2 for q in ls) / len(ls)
    real, p, nm = amount_shuffle(lists, share)
    record('E1 common divisor, sides merged', 'Amounts on a whole tablet share a common divisor above 1 more than chance',
           {'share': round(real, 3), 'null_mean': round(nm, 3), 'p': round(p, 4), 'tablets': len(lists)}, {'earlier (sides separate)': '10.7% vs 5.1%, p 0.0005'})
    return p


def E2():
    lists = [t['q'] for t in TABS.values() if len(t['q']) >= 2]
    dbl = lambda ls: sum(1 for q in ls for i, a in enumerate(q) for b in q[i + 1:] if a > 0 and b > 0 and (a == 2 * b or b == 2 * a))
    real, p, nm = amount_shuffle(lists, dbl)
    record('E2 doubled amounts, sides merged', 'Amounts on a whole tablet are exact doubles of each other more than chance',
           {'double_pairs': real, 'null_mean': round(nm, 2), 'p': round(p, 4)}, {'earlier (sides separate)': 'p 0.015'})
    return p


def E3():
    tabs = [(k, t) for k, t in TABS.items() if k in SCRIBE_W and len(t['words']) >= 2]
    names = [k for k, _ in tabs]
    words = {k: t['words'] - TERMS for k, t in tabs}
    jac = {}
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            u = words[a] | words[b]
            jac[(a, b)] = len(words[a] & words[b]) / len(u) if u else 0

    def stat(labs):
        sc = dict(zip(names, labs))
        same = [v for (a, b), v in jac.items() if sc[a] == sc[b]]
        diff = [v for (a, b), v in jac.items() if sc[a] != sc[b]]
        return sum(same) / max(1, len(same)) - sum(diff) / max(1, len(diff))
    real, p, nm = shuffle_test(stat, [SCRIBE_W[k] for k in names])
    record('E3 scribe vocabulary, sides merged', 'Whole tablets by the same scribe share more vocabulary (transaction terms removed)',
           {'jaccard_diff': round(real, 4), 'null_mean': round(nm, 4), 'p': round(p, 4), 'tablets': len(names)}, {})
    return p


def E4():
    tabs = [t for t in TABS.values() if t['kuro'] or t['kiro']]
    labs = [t['kiro'] for t in tabs]
    vir = [('VIR' in t['com']) for t in tabs]

    def stat(lb):
        k = [v for v, l in zip(vir, lb) if l]
        o = [v for v, l in zip(vir, lb) if not l]
        return sum(k) / max(1, len(k)) - sum(o) / max(1, len(o))
    real, p, nm = shuffle_test(stat, labs, lower=True)
    record('E4 KI-RO off personnel tablets, sides merged', 'KI-RO is rarer on VIR tablets than on other tablets with totals',
           {'kiro_with_vir': f"{sum(v for v, l in zip(vir, labs) if l)}/{sum(labs)}",
            'other_with_vir': f"{sum(v for v, l in zip(vir, labs) if not l)}/{len(labs) - sum(labs)}", 'p': round(p, 4)}, {})
    return p


# ------------------------------------------------------------------ coronal pattern
def log_or_v(words, target, pool=None, cons_sets=(COR, NONCOR), offset=0):
    """log odds ratio: target vowel(s) after coronal vs non-coronal consonant. offset=1 uses the next sign's consonant."""
    c = Counter()
    for w in words:
        for i, x in enumerate(w):
            g = grid(x)
            if not g or (pool and g[1] not in pool):
                continue
            j = i + offset
            if j >= len(w):
                continue
            gc = grid(w[j])
            if not gc or gc[0] not in cons_sets[0] | cons_sets[1]:
                continue
            c[(gc[0] in cons_sets[0], g[1] in target)] += 1
    a, b, cc, d = (c[(True, True)] + .5, c[(True, False)] + .5, c[(False, True)] + .5, c[(False, False)] + .5)
    return log(a * d / (b * cc))


def compare(a_words, b_words, fn, lower=False):
    return T.label_perm(lambda x, y: fn(x) - fn(y), a_words, b_words, lower=lower)


def E5():
    fe = lambda ws: log_or_v(ws, {'e'})
    fo = lambda ws: log_or_v(ws, {'o'})
    real, p, nm = compare(LA, LB, fe)
    r2, p2, _ = compare(LA, LB, fo)
    record('E5 e alone after coronals', 'e alone follows coronals more than non-coronals, more so than in Linear B',
           {'logOR_LA_e': round(fe(LA), 3), 'logOR_LB_e': round(fe(LB), 3), 'p': round(p, 4)},
           {'o alone': {'LA': round(fo(LA), 3), 'LB': round(fo(LB), 3), 'p': round(p2, 4)}})
    return p


def E6():
    f = lambda ws: log_or_v(ws, RARE)
    ht = D.site_words(lambda s: s == 'Haghia Triada')
    oth = D.site_words(lambda s: s != 'Haghia Triada')
    real, p, nm = compare(oth, LB, f)
    r2, p2, _ = compare(ht, LB, f)
    record('E6 coronal pattern by site', 'The coronal e/o pattern holds outside Haghia Triada (primary) and at Haghia Triada',
           {'logOR_other_sites': round(f(oth), 3), 'logOR_LB': round(f(LB), 3), 'p': round(p, 4), 'words': len(oth)},
           {'Haghia Triada': {'logOR': round(f(ht), 3), 'p': round(p2, 4), 'words': len(ht)}})
    return p


def E7():
    f = lambda ws: log_or_v(ws, RARE)
    names = list(B.LA_NAMES)
    nonnames = [w for w in LA if w not in set(names)]
    real, p, nm = compare(names, LB, f)
    r2, p2, _ = compare(nonnames, LB, f)
    record('E7 coronal pattern in names', 'The coronal e/o pattern holds in Linear A list names',
           {'logOR_names': round(f(names), 3), 'logOR_LB': round(f(LB), 3), 'p': round(p, 4), 'names': len(names)},
           {'non-name words': {'logOR': round(f(nonnames), 3), 'p': round(p2, 4)}})
    return p


def E8():
    same = lambda ws: log_or_v(ws, RARE)
    nxt = lambda ws: log_or_v(ws, RARE, offset=1)
    real = same(LA) - nxt(LA)
    boot = []
    for _ in range(REPS):
        smp = [rng.choice(LA) for _ in LA]
        boot.append(same(smp) - nxt(smp))
    p = T.pv_lower(boot, 0.0)
    p = (sum(b <= 0 for b in boot) + 1) / (len(boot) + 1)
    record('E8 same syllable, not the next', 'The consonant of the same syllable predicts e/o more than the next syllable\'s consonant',
           {'logOR_same': round(same(LA), 3), 'logOR_next': round(nxt(LA), 3), 'bootstrap p': round(p, 4)},
           {'Linear B': {'same': round(same(LB), 3), 'next': round(nxt(LB), 3)}})
    return p


def E9():
    f = lambda ws: log_or_v(ws, RARE, pool=set('eiou'))
    real, p, nm = compare(LA, LB, f)
    record('E9 e/o in place of i/u', 'Among e, i, o, u, e/o take a larger share after coronals than in Linear B',
           {'logOR_LA': round(f(LA), 3), 'logOR_LB': round(f(LB), 3), 'p': round(p, 4)}, {})
    return p


# ------------------------------------------------------------------ scribes and persons
def E10():
    tabs = [(SCRIBE_W[k], t) for k, t in TABS.items() if k in SCRIBE_W and t['com']]
    by = Counter(s for s, _ in tabs)
    tabs = [(s, t) for s, t in tabs if by[s] >= 3]
    names = [s for s, _ in tabs]
    coms = [t['com'] for _, t in tabs]
    stat = lambda cs: chi2([(s, c) for s, cset in zip(names, cs) for c in cset])
    real, p, nm = shuffle_test(stat, coms)
    record('E10 scribes and commodities', 'Scribes specialise in commodities',
           {'chi2': round(real, 2), 'null_mean': round(nm, 2), 'p': round(p, 4), 'tablets': len(tabs), 'scribes': len(by)}, {})
    return p


def E11():
    tabs = [(SCRIBE_W[k], t) for k, t in TABS.items() if k in SCRIBE_W]
    by = Counter(s for s, _ in tabs)
    tabs = [(s, t) for s, t in tabs if by[s] >= 3]
    names = [s for s, _ in tabs]
    terms = [frozenset(t['terms'] - {'KU-RO', 'KI-RO', 'PO-TO-KU-RO'}) or frozenset({'none'}) for _, t in tabs]
    stat = lambda ts: chi2([(s, x) for s, tset in zip(names, ts) for x in tset])
    real, p, nm = shuffle_test(stat, terms)
    record('E11 scribes and transaction terms', 'Scribes specialise in transaction terms',
           {'chi2': round(real, 2), 'null_mean': round(nm, 2), 'p': round(p, 4), 'tablets': len(tabs)},
           {'terms by scribe': {s: dict(Counter(x for s2, tset in zip(names, terms) if s2 == s for x in tset if x != 'none')) for s in sorted(set(names))}})
    return p


def entry_seq():
    seq = defaultdict(list)
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        ents = defaultdict(list)
        for tok in r['tokens']:
            ents[tok['entry']].append(tok)
        for e_, toks in sorted(ents.items()):
            words = [t['label'] for t in toks if t['cls'] == 'word' and t.get('function') == 'entry label' and t['label'] not in TERMS]
            q = sum(t['value'] for t in toks if t['cls'] == 'number')
            for w in words:
                seq[whole(r['name'])].append((w, q))
    return seq


SEQ = entry_seq()
PAIRS = [(a, b) for i, a in enumerate(sorted(SEQ)) for b in sorted(SEQ)[i + 1:]
         if len({w for w, _ in SEQ[a]} & {w for w, _ in SEQ[b]}) >= 3]


def E12():
    items = []
    for a, b in PAIRS:
        qa = {w: q for w, q in SEQ[a]}
        qb = {w: q for w, q in SEQ[b]}
        for w in set(qa) & set(qb):
            items.append((a, b, w, qa[w], qb[w]))
    real = sum(x[3] == x[4] for x in items)
    null = []
    for _ in range(REPS):
        hit = 0
        for a, b in PAIRS:
            qa = {w: q for w, q in SEQ[a]}
            qb_vals = [q for _, q in SEQ[b]]
            rng.shuffle(qb_vals)
            qb = dict(zip([w for w, _ in SEQ[b]], qb_vals))
            hit += sum(qa[w] == qb[w] for w in set(qa) & set(qb))
        null.append(hit)
    p = B.pv(null, real)
    record('E12 recopied lists, same amounts', 'Recopied lists give the same amounts for the same entries',
           {'identical': f'{real}/{len(items)}', 'null_mean': round(sum(null) / len(null), 2), 'p': round(p, 4)},
           {'tablet pairs sharing 3+ entry words': ['/'.join(p_) for p_ in PAIRS],
            'entries': [f'{a}/{b} {w}: {x} vs {y}' for a, b, w, x, y in items]})
    return p


def E13():
    occ = defaultdict(set)
    for k, s in SEQ.items():
        for w, _ in s:
            occ[w].add(k)
    occ = {w: rs for w, rs in occ.items() if len(rs) >= 2}
    tabs = sorted({r for rs in occ.values() for r in rs})
    site = {k: TABS[k]['site'] if k in TABS else None for k in tabs}

    def stat(labs):
        sm = dict(zip(tabs, labs))
        pr = [(a, b) for rs in occ.values() for i, a in enumerate(sorted(rs)) for b in sorted(rs)[i + 1:]]
        return sum(sm[a] == sm[b] for a, b in pr) / max(1, len(pr))
    real, p, nm = shuffle_test(stat, [site[k] for k in tabs])
    record('E13 persons stay at one site', 'Recurring entry words stay at one site more than chance',
           {'share_same_site': round(real, 3), 'null_mean': round(nm, 3), 'p': round(p, 4), 'words': len(occ)}, {})
    return p


# ------------------------------------------------------------------ vowels
def E14():
    ete = []
    for text in E.ET.ETEOCRETAN.values():
        for chunk in text.split():
            for piece in chunk.split('|'):
                ete += E.ET.stretches(piece)
    gre = []
    for text in (E.ET.GREEK, E.ET.HOMER):
        gre += [s for w in text.split() for s in E.ET.greek_stretches(w)]
    es, gs = E.spelled(ete), E.spelled(gre)
    f = lambda ws: log_or_v(ws, RARE)
    real, p, nm = compare(es, gs, f)
    record('E14 Eteocretan coronal pattern', 'Eteocretan e/o follow coronals more than non-coronals, more so than in Greek',
           {'logOR_eteocretan': round(f(es), 3), 'logOR_greek': round(f(gs), 3), 'p': round(p, 4), 'pieces': [len(es), len(gs)]}, {})
    return p


def E15():
    kn = [w[:-1] for w in V.kn_only if T.CAT.get(w) in ('toponym', 'ethnic') and T.clean(w) and len(w) >= 3]
    py = [w[:-1] for w in V.py_only if T.CAT.get(w) in ('toponym', 'ethnic') and T.clean(w) and len(w) >= 3]
    f = lambda ws: log_or_v(ws, RARE)
    real, p, nm = compare(kn, py, f)
    record('E15 Cretan place names', 'Knossos-only place names show the coronal e/o pattern more than Pylos-only ones',
           {'logOR_KN': round(f(kn), 3), 'logOR_PY': round(f(py), 3), 'p': round(p, 4), 'n': [len(kn), len(py)]}, {})
    return p


def E16():
    lab_vel = set('pmwkq')
    other = set('tdnrsz')
    f = lambda ws: log_or_v(ws, {'u'}, cons_sets=(lab_vel, other))
    real, p, nm = compare(LA, LB, f)
    record('E16 u after labials and velars', 'u follows labial and velar consonants more than others, more so than in Linear B',
           {'logOR_LA': round(f(LA), 3), 'logOR_LB': round(f(LB), 3), 'p': round(p, 4)}, {})
    return p


def cluster_test(words, reps):
    ws = [list(w) for w in words if all(grid(x) for x in w) and len(w) >= 2]
    stat = lambda wl: sum(1 for w in wl if sum(grid(x)[1] in RARE for x in w) >= 2)
    real = stat(ws)
    flat = [x for w in ws for x in w]
    null = []
    for _ in range(reps):
        rng.shuffle(flat)
        k, sh = 0, []
        for w in ws:
            sh.append(flat[k:k + len(w)])
            k += len(w)
        null.append(stat(sh))
    return real, B.pv(null, real), sum(null) / len(null)


def E17():
    r, p, nm = cluster_test(LA, REPS)
    lr, lp, lnm = cluster_test(LB, 300)
    record('E17 e/o cluster in words', 'Words with two or more e/o syllables exceed chance',
           {'words': r, 'null_mean': round(nm, 1), 'p': round(p, 4)}, {'Linear B control': {'words': lr, 'null_mean': round(lnm, 1), 'p': round(lp, 4)}})
    return p


# ------------------------------------------------------------------ Knossos names, stem-scored
stem_score = lambda w: T.minoan(w[:-1]) if len(w) >= 3 else T.minoan(w)


def E18():
    sc = defaultdict(Counter)
    for _, r in B.LB_RECS:
        if r.get('site') != 'Knossos' or not r.get('scribe'):
            continue
        for t in r.get('transliteratedWords', []):
            tl = t.strip().lower()
            if '-' in tl and not any(ch in tl for ch in '[]?'):
                sc[tuple(tl.split('-'))][r['scribe']] += 1
    names = [w for w in T.KN_N if w in sc]
    scribe = [sc[w].most_common(1)[0][0] for w in names]
    keep = Counter(scribe)
    idx = [i for i, s in enumerate(scribe) if keep[s] >= 5]
    names = [names[i] for i in idx]
    scribe = [scribe[i] for i in idx]
    vals = [stem_score(w) for w in names]
    mu = sum(vals) / len(vals)

    def between(v):
        g = defaultdict(list)
        for s, x in zip(scribe, v):
            g[s].append(x)
        return sum(len(xs) * (sum(xs) / len(xs) - mu) ** 2 for xs in g.values())
    real, p, nm = shuffle_test(between, vals)
    g = defaultdict(list)
    for s, x in zip(scribe, vals):
        g[s].append(x)
    record('E18 Minoan names by Knossos scribe', 'Minoan-shaped Knossos names (stem-scored) cluster by Linear B scribe',
           {'between_SS': round(real, 3), 'null_mean': round(nm, 3), 'p': round(p, 4), 'names': len(names), 'scribes': len(g)},
           {'most Minoan scribes (mean stem score)': sorted(((round(sum(v) / len(v), 3), s, len(v)) for s, v in g.items()), reverse=True)[:6]})
    return p


def E19():
    a, b = T.names_by(lambda logos, words: 'VIR' in logos)
    stat = lambda x, y: V.auc([stem_score(w) for w in x], [stem_score(w) for w in y])
    real, p, nm = T.label_perm(stat, a, b)
    record('E19 names on personnel tablets', 'Knossos names on VIR tablets are more Minoan-shaped (stem-scored) than names on other tablets',
           {'auc': round(real, 3), 'null_mean': round(nm, 3), 'p': round(p, 4), 'n': [len(a), len(b)]}, {})
    return p


# ------------------------------------------------------------------ signs
def side_cohesion(words, side):
    raw = {s: c for s, c in D.contexts(words).items() if grid(s)}
    ctx = {s: D.norm(Counter({f: v for f, v in c.items() if f.startswith(side)})) for s, c in raw.items()}
    signs = sorted(s for s in ctx if ctx[s])
    lab = {s: grid(s)[0] for s in signs}
    sims = {(a, b): D.cos(ctx[a], ctx[b]) for i, a in enumerate(signs) for b in signs[i + 1:]}

    def stat(lb):
        same = [v for (a, b), v in sims.items() if lb[a] == lb[b]]
        diff = [v for (a, b), v in sims.items() if lb[a] != lb[b]]
        return sum(same) / len(same) - sum(diff) / len(diff)
    real = stat(lab)
    labs = [lab[s] for s in signs]
    null = []
    for _ in range(2000):
        rng.shuffle(labs)
        null.append(stat(dict(zip(signs, labs))))
    return real, B.pv(null, real)


def E20():
    r, p = side_cohesion(LA, 'L:')
    lr, lp = side_cohesion(LB, 'L:')
    record('E20 rows by left context', 'Consonant-row cohesion holds with left-context features only',
           {'diff': round(r, 4), 'p': round(p, 4)}, {'Linear B control': {'diff': round(lr, 4), 'p': round(lp, 4)}})
    return p


def E21():
    r, p = side_cohesion(LA, 'R:')
    lr, lp = side_cohesion(LB, 'R:')
    record('E21 rows by right context', 'Consonant-row cohesion holds with right-context features only',
           {'diff': round(r, 4), 'p': round(p, 4)}, {'Linear B control': {'diff': round(lr, 4), 'p': round(lp, 4)}})
    return p


def z_to(words, target_row):
    vecs = Db.ctx_vectors(words)
    signs = [s for s in vecs if grid(s)]
    zs = [s for s in signs if grid(s)[0] == 'z']
    tgt = [s for s in signs if grid(s)[0] == target_row]
    rest = [s for s in signs if grid(s)[0] not in ('z', target_row)]

    def stat(group):
        a = [D.cos(vecs[x], vecs[y]) for x in group for y in tgt]
        b = [D.cos(vecs[x], vecs[y]) for x in group for y in rest if y not in group]
        return sum(a) / len(a) - sum(b) / len(b)
    real = stat(zs)
    null = [stat(rng.sample(rest, len(zs))) for _ in range(2000)]
    return real, B.pv(null, real), zs


def E22():
    r, p, zs = z_to(LA, 'j')
    lr, lp, _ = z_to(LB, 'j')
    record('E22 Z row and J row', 'The Z signs keep company with the J row more than other signs do',
           {'diff': round(r, 4), 'p': round(p, 4), 'z_signs': zs}, {'Linear B control': {'diff': round(lr, 4), 'p': round(lp, 4)}})
    return p


# ------------------------------------------------------------------ accounts
def E23():
    tabs = [(SCRIBE_W[k], t['frac']) for k, t in TABS.items() if k in SCRIBE_W and t['q']]
    by = Counter(s for s, _ in tabs)
    tabs = [x for x in tabs if by[x[0]] >= 3]
    names = [s for s, _ in tabs]
    stat = lambda fl: chi2(list(zip(names, fl)))
    real, p, nm = shuffle_test(stat, [f for _, f in tabs])
    record('E23 fractions by scribe', 'Fraction use depends on the scribe',
           {'chi2': round(real, 2), 'null_mean': round(nm, 2), 'p': round(p, 4), 'tablets': len(tabs)},
           {'fraction tablets by scribe': {s: f'{sum(f for s2, f in tabs if s2 == s)}/{n}' for s, n in by.items() if n >= 3}})
    return p


def E24():
    rows = [(x['record'], w, x['section'] == 'KI-RO') for x in T.ENTRIES for w in x['words'] if w not in TERMS]
    tabs_of = defaultdict(set)
    for rec, w, _ in rows:
        tabs_of[w].add(whole(rec))
    recur = lambda w: len(tabs_of[w]) >= 2

    def stat(flags):
        k = [recur(w) for (_, w, _), f in zip(rows, flags) if f]
        o = [recur(w) for (_, w, _), f in zip(rows, flags) if not f]
        return sum(k) / max(1, len(k)) - sum(o) / max(1, len(o))
    real, p, nm = shuffle_test(stat, [f for _, _, f in rows])
    record('E24 KI-RO persons recur', 'Entry words in KI-RO sections recur on other tablets more than main-section words',
           {'diff': round(real, 3), 'null_mean': round(nm, 3), 'p': round(p, 4), 'kiro_entries': sum(f for _, _, f in rows)},
           {'KI-RO words recurring elsewhere': sorted({w for _, w, f in rows if f and recur(w)})})
    return p


def kendall(a, b):
    c = d = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            s = (a[i] - a[j]) * (b[i] - b[j])
            c += s > 0
            d += s < 0
    return (c - d) / max(1, c + d)


def E25():
    orders = []
    for a, b in PAIRS:
        oa = [w for w, _ in SEQ[a]]
        ob = [w for w, _ in SEQ[b]]
        shared = [w for w in dict.fromkeys(oa) if w in set(ob)]
        if len(shared) >= 3:
            orders.append(([oa.index(w) for w in shared], [ob.index(w) for w in shared]))
    real = sum(kendall(x, y) for x, y in orders) / len(orders)
    null = []
    for _ in range(5000):
        tot = 0
        for x, y in orders:
            y2 = list(y)
            rng.shuffle(y2)
            tot += kendall(x, y2)
        null.append(tot / len(orders))
    p = B.pv(null, real)
    record('E25 recopied lists keep order', 'Shared entries of recopied lists appear in the same order',
           {'mean_tau': round(real, 3), 'p': round(p, 4), 'pairs': len(orders)},
           {'per pair tau': [round(kendall(x, y), 2) for x, y in orders], 'tablet pairs': ['/'.join(p_) for p_ in PAIRS]})
    return p


TESTS = [E1, E2, E3, E4, E5, E6, E7, E8, E9, E10, E11, E12, E13, E14, E15, E16, E17, E18, E19, E20, E21, E22, E23, E24, E25]


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
    (ROOT / 'reading/decipher25b_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str) + '\n', encoding='utf-8')
    print('\nprimary p:', {k: round(v, 4) for k, v in ps.items()})
    print('survive BH at 5%:', supported)


if __name__ == '__main__':
    main()
