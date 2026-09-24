"""Twenty-five hypotheses building on the supported results so far: the Minoan vowel profile and its consonant
conditioning (decipher10c-e), the consonant rows (decipher10), the Minoan names at Knossos (vigorous*, names), and
the bookkeeping habits (batches*, vigorous).

Each has a prediction stated before the test ran and one primary test with its own null. Benjamini-Hochberg at
5% runs across all twenty-five. Linear B, ordinary Greek or Pylos serve as controls where the method allows.

Vowels and the Pre-Greek link
D1  Linear A e/o prefer coronal consonants (t d n r s z) over non-coronals more than Linear B e/o do.
D2  Pre-Greek stems show that coronal preference more than ordinary Greek stems.
D3  Knossos personal names show it more than Pylos personal names.
D4  Linear A's e/o share by consonant correlates with Pre-Greek's more than with ordinary Greek's.
Morphology
D5  -TE is a suffix: Linear A words ending in -TE have an attested bare stem more often than words with other finals.
D6  -JA is a suffix, by the same test.
D7  -NE is a suffix, by the same test.
D8  s and t alternate: words differing only in one sign's consonant (same vowel) alternate s/t more than chance.
D9  z and s alternate, by the same test.
Signs
D10 Sonorant rows (n r j w m) cohere in context more than obstruent rows (p t k d s q z). Control: Linear B.
D11 Doublet signs (RA/RA2, TA/TA2, PA/PA3, PU/PU2) differ in their position in the word more than chance.
D12 Special signs (PA3, RA2, PU2, TA2) are commoner in entry labels (names) than in headings.
People at Knossos
D13 Knossos personal names on tablets with women (MUL) are more Minoan-shaped than other Knossos names.
D14 Knossos personal names on sheep tablets (OVIS) are more Minoan-shaped than other Knossos names.
D15 Minoan-shaped Knossos names stand on the same tablets as Cretan place names more than other names do.
D16 Minoan-shaped Knossos names are more often attested only once.
D25 Knossos common words without a Greek etymology have fewer e/o syllables than those with one.
Bookkeeping
D17 Tablets whose amounts share a common divisor cluster by scribe.
D18 Tablets sharing a heading word share a commodity more often than chance.
D19 The same entry word on different tablets carries similar amounts (closer than random same-commodity entries).
D20 Entry words recurring on several tablets stay with the same scribe more than chance.
D21 Entry words recurring on several tablets stay with the same commodity more than chance.
D22 Recurring entry words recur together (teams): more word pairs share two or more tablets than chance.
Typology
D23 Pre-Greek stems' first-syllable consonants resemble Linear A's more than ordinary Greek's do.
D24 Linear A's word lengths resemble Pre-Greek stems more than ordinary Greek stems.
"""
from collections import Counter, defaultdict
import json
from functools import reduce
from math import gcd, log, log2
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import batches as B  # noqa: E402
import decipher10 as D  # noqa: E402
import decipher10b as Db  # noqa: E402
import decipher10e as E  # noqa: E402
import vigorous as V  # noqa: E402

ROOT = B.ROOT
LEX = ROOT / 'data/lexica'
rng = B.rng
REPS = 1000
out = D.out
out.clear()
record = D.record
grid = D.grid
CAT = B.LB_CAT
clean = lambda w: not any(x.startswith('*') for x in w)
RARE = {'e', 'o'}
COR, NONCOR = set('tdnrsz'), set('pmwkqj')
LA = Db.LA_W
LB = Db.LB_W
KN_N = [w for w in V.kn_only if CAT.get(w) == 'anthroponym' and clean(w)]
PY_N = [w for w in V.py_only if CAT.get(w) == 'anthroponym' and clean(w)]


def pv_lower(null, real):
    return (sum(n <= real for n in null) + 1) / (len(null) + 1)


def label_perm(stat, a, b, reps=REPS, lower=False):
    real = stat(a, b)
    pool, k, null = list(a) + list(b), len(a), []
    for _ in range(reps):
        rng.shuffle(pool)
        null.append(stat(pool[:k], pool[k:]))
    return real, (pv_lower(null, real) if lower else B.pv(null, real)), sum(null) / len(null)


def spearman(x, y):
    return B.spearman(x, y)


# ------------------------------------------------------------------ Pre-Greek sets (as in decipher10e.C1)
def pregreek_sets():
    pre = [json.loads(l)['word'] for l in open(LEX / 'pregreek_wiktionary.jsonl', encoding='utf-8')]
    ordn = []
    for line in open(LEX / 'AncientGreek_head.jsonl', encoding='utf-8'):
        r = json.loads(line)
        if r.get('pos') in ('noun', 'adj', 'verb', 'name') and ' ' not in r['word']:
            ordn.append(r['word'])
    pre_s = E.spelled([E.PG.romanise(w) for w in pre])
    ord_s = [w for w in E.spelled([E.PG.romanise(w) for w in ordn]) if w not in set(pre_s)]
    by_len = defaultdict(list)
    for w in ord_s:
        by_len[len(w)].append(w)
    need = Counter(len(w) for w in pre_s)
    matched = [w for L_, n in need.items() for w in rng.sample(by_len[L_], min(n, len(by_len[L_])))]
    unmatched = rng.sample(ord_s, len(pre_s))
    stem = lambda ws: [w[:-1] for w in ws if len(w) >= 3]
    return stem(pre_s), stem(matched), stem(unmatched)


PRE, GRK, GRK_U = pregreek_sets()


# ------------------------------------------------------------------ vowels
def log_or(words):
    c = Counter()
    for w in words:
        for x in w:
            g = grid(x)
            if g and g[0] in COR | NONCOR:
                c[(g[0] in COR, g[1] in RARE)] += 1
    a, b, cc, d = (c[(True, True)] + .5, c[(True, False)] + .5, c[(False, True)] + .5, c[(False, False)] + .5)
    return log(a * d / (b * cc))


def coronal_test(a, b, name, pred, ctrl_note):
    real, p, nm = label_perm(lambda x, y: log_or(x) - log_or(y), a, b)
    record(name, pred, {'logOR_target': round(log_or(a), 3), 'logOR_comparison': round(log_or(b), 3), 'p': round(p, 4),
                        'null_mean_diff': round(nm, 3)}, {'comparison': ctrl_note})
    return p


def D1():
    return coronal_test(LA, LB, 'D1 coronal e/o in Linear A', 'Linear A e/o prefer coronals more than Linear B e/o do', 'Linear B word types')


def D2():
    return coronal_test(PRE, GRK, 'D2 coronal e/o in Pre-Greek', 'Pre-Greek stems prefer e/o after coronals more than Greek stems',
                        'length-matched ordinary Greek stems')


def D3():
    return coronal_test([w[:-1] for w in KN_N if len(w) >= 2], [w[:-1] for w in PY_N if len(w) >= 2], 'D3 coronal e/o in Knossos names',
                        'Knossos names prefer e/o after coronals more than Pylos names (ending removed)', 'Pylos names')


def eo_by_cons(words):
    tot, hit = Counter(), Counter()
    for w in words:
        for x in w:
            g = grid(x)
            if g and g[0]:
                tot[g[0]] += 1
                hit[g[0]] += g[1] in RARE
    return {c: hit[c] / tot[c] for c in tot if tot[c] >= 15}


def D4():
    la = eo_by_cons(LA)

    def stat(pre, grk):
        p_, g_ = eo_by_cons(pre), eo_by_cons(grk)
        cs = sorted(set(la) & set(p_) & set(g_))
        return spearman([la[c] for c in cs], [p_[c] for c in cs]) - spearman([la[c] for c in cs], [g_[c] for c in cs])
    real, p, nm = label_perm(stat, PRE, GRK, reps=500)
    p_, g_ = eo_by_cons(PRE), eo_by_cons(GRK)
    cs = sorted(set(la) & set(p_) & set(g_))
    record('D4 same conditioning as Pre-Greek', 'Linear A e/o share by consonant correlates with Pre-Greek more than with Greek',
           {'rho_LA_PreGreek': round(spearman([la[c] for c in cs], [p_[c] for c in cs]), 3),
            'rho_LA_Greek': round(spearman([la[c] for c in cs], [g_[c] for c in cs]), 3), 'p': round(p, 4), 'consonants': cs},
           {'by consonant (LA, Pre-Greek, Greek)': {c: (round(la[c], 2), round(p_[c], 2), round(g_[c], 2)) for c in cs}})
    return p


# ------------------------------------------------------------------ morphology
def suffix_test(sfx, words=LA):
    wset = set(words)
    long_ = [w for w in words if len(w) >= 3]
    stem_ok = lambda w: w[:-1] in wset
    real = sum(stem_ok(w) for w in long_ if w[-1] == sfx) / max(1, sum(1 for w in long_ if w[-1] == sfx))
    stems, fins = [w[:-1] for w in long_], [w[-1] for w in long_]
    null = []
    for _ in range(REPS):
        rng.shuffle(fins)
        sel = [s in wset for s, f in zip(stems, fins) if f == sfx]
        null.append(sum(sel) / max(1, len(sel)))
    pairs = sorted('-'.join(w).upper() for w in long_ if w[-1] == sfx and stem_ok(w))
    return real, B.pv(null, real), sum(null) / len(null), sum(1 for w in long_ if w[-1] == sfx), pairs


def suffix_record(key, sfx):
    real, p, nm, n, pairs = suffix_test(sfx)
    extra = {'pairs (X-%s with X attested)' % sfx.upper(): pairs[:20]}
    if sfx == 'te':
        rel = {w for _, _, w in B.LA_RELIG}
        extra['-TE forms in religious register'] = sum(1 for p_ in pairs if tuple(p_.lower().split('-')) in rel)
        extra['their bare stems in religious register'] = sum(1 for p_ in pairs if tuple(p_.lower().split('-'))[:-1] in rel)
    record(key, f'-{sfx.upper()} is a suffix: X-{sfx.upper()} words have an attested bare stem X more often than chance',
           {'share_with_stem': round(real, 3), 'null_mean': round(nm, 3), 'p': round(p, 4), 'words': n}, extra)
    return p


def D5():
    return suffix_record('D5 -TE suffix', 'te')


def D6():
    return suffix_record('D6 -JA suffix', 'ja')


def D7():
    return suffix_record('D7 -NE suffix', 'ne')


def cons_pairs(words):
    idx = defaultdict(list)
    for w in words:
        for i in range(len(w)):
            idx[(len(w), i, w[:i] + w[i + 1:])].append(w[i])
    pairs = []
    for key, signs in idx.items():
        signs = sorted(set(signs))
        for i, a in enumerate(signs):
            for b in signs[i + 1:]:
                ga, gb = grid(a), grid(b)
                if ga and gb and ga[0] and gb[0] and ga[1] == gb[1] and ga[0] != gb[0]:
                    pairs.append((ga[0], gb[0]))
    return pairs


def alternation_test(target, words=LA):
    pairs = cons_pairs(words)
    cf = Counter(grid(x)[0] for w in words for x in w if grid(x) and grid(x)[0])
    real = sum({a, b} == target for a, b in pairs)
    cs = list(cf)
    null = []
    for _ in range(REPS):
        hit = 0
        for a, _ in pairs:
            opts = [c for c in cs if c != a]
            b = rng.choices(opts, weights=[cf[c] for c in opts])[0]
            hit += {a, b} == target
        null.append(hit)
    return real, B.pv(null, real), sum(null) / len(null), len(pairs)


def D8():
    real, p, nm, n = alternation_test({'s', 't'})
    lb = alternation_test({'s', 't'}, LB)
    record('D8 s/t alternation', 'Words differing in one consonant alternate s/t more than chance',
           {'s_t_pairs': real, 'expected': round(nm, 2), 'p': round(p, 4), 'consonant_pairs': n},
           {'Linear B control': {'pairs': lb[0], 'expected': round(lb[2], 2), 'p': round(lb[1], 4)},
            'commonest alternations in Linear A': Counter(''.join(sorted(x)) for x in cons_pairs(LA)).most_common(8)})
    return p


def D9():
    real, p, nm, n = alternation_test({'z', 's'})
    lb = alternation_test({'z', 's'}, LB)
    record('D9 z/s alternation', 'Words differing in one consonant alternate z/s more than chance',
           {'z_s_pairs': real, 'expected': round(nm, 2), 'p': round(p, 4)},
           {'Linear B control': {'pairs': lb[0], 'expected': round(lb[2], 2), 'p': round(lb[1], 4)}})
    return p


# ------------------------------------------------------------------ signs
SONOR = set('nrjwm')
OBSTR = set('ptkdsqz')


def row_cohesion(words):
    vecs = Db.ctx_vectors(words)
    signs = [s for s in vecs if grid(s) and grid(s)[0]]
    per = {}
    for s in signs:
        own = [D.cos(vecs[s], vecs[t]) for t in signs if t != s and grid(t)[0] == grid(s)[0]]
        oth = [D.cos(vecs[s], vecs[t]) for t in signs if grid(t)[0] != grid(s)[0]]
        if own:
            per[s] = sum(own) / len(own) - sum(oth) / len(oth)
    rows = defaultdict(list)
    for s, v in per.items():
        rows[grid(s)[0]].append(v)
    return {r: sum(v) / len(v) for r, v in rows.items()}


def D10():
    def test(words):
        rc = row_cohesion(words)
        rows = [r for r in rc if r in SONOR | OBSTR]
        stat = lambda cls: (sum(rc[r] for r in rows if cls[r]) / max(1, sum(cls[r] for r in rows))
                            - sum(rc[r] for r in rows if not cls[r]) / max(1, sum(not cls[r] for r in rows)))
        base = {r: r in SONOR for r in rows}
        real = stat(base)
        labs = [base[r] for r in rows]
        null = []
        for _ in range(5000):
            rng.shuffle(labs)
            null.append(stat(dict(zip(rows, labs))))
        return real, B.pv(null, real), {r: round(rc[r], 3) for r in rows}
    r, p, rows = test(LA)
    lr, lp, lrows = test(LB)
    record('D10 sonorant rows cohere', 'Sonorant consonant rows cohere more than obstruent rows',
           {'diff': round(r, 4), 'p': round(p, 4)}, {'rows': rows, 'Linear B control': {'diff': round(lr, 4), 'p': round(lp, 4)}})
    return p


DOUBLETS = [('ra', 'ra2'), ('ta', 'ta2'), ('pa', 'pa3'), ('pu', 'pu2')]


def pos(i, n):
    return 'I' if i == 0 else 'F' if i == n - 1 else 'M'


def doublet_test(words):
    occ = []
    for a, b in DOUBLETS:
        for w in words:
            for i, x in enumerate(w):
                if x in (a, b):
                    occ.append(((a, b), x == b, pos(i, len(w))))

    def stat(o):
        tot = 0.0
        for pair in DOUBLETS:
            sub = [(isb, ps) for pp, isb, ps in o if pp == pair]
            if not sub or all(isb for isb, _ in sub) or not any(isb for isb, _ in sub):
                continue
            c = Counter(sub)
            n = len(sub)
            rows = Counter(isb for isb, _ in sub)
            cols = Counter(ps for _, ps in sub)
            tot += sum((c[(r, k)] - rows[r] * cols[k] / n) ** 2 / (rows[r] * cols[k] / n) for r in rows for k in cols)
        return tot
    real = stat(occ)
    null = []
    for _ in range(REPS):
        flags = [isb for _, isb, _ in occ]
        byp = defaultdict(list)
        for i, (pp, isb, ps) in enumerate(occ):
            byp[pp].append(i)
        sh = list(occ)
        for pp, idx in byp.items():
            fl = [occ[i][1] for i in idx]
            rng.shuffle(fl)
            for i, f in zip(idx, fl):
                sh[i] = (pp, f, occ[i][2])
        null.append(stat(sh))
    prof = {f'{a}/{b}': {x: dict(Counter(ps for pp, isb, ps in occ if pp == (a, b) and isb == (x == b))) for x in (a, b)} for a, b in DOUBLETS}
    return real, B.pv(null, real), prof


def D11():
    r, p, prof = doublet_test(LA)
    lr, lp, _ = doublet_test(LB)
    record('D11 doublet signs by position', 'RA/RA2, TA/TA2, PA/PA3, PU/PU2 differ in word position more than chance',
           {'chi2_sum': round(r, 2), 'p': round(p, 4)}, {'positions (I initial, M medial, F final)': prof,
                                                          'Linear B control': {'chi2_sum': round(lr, 2), 'p': round(lp, 4)}})
    return p


def D12():
    fn = E.la_functions() if hasattr(E, 'la_functions') else None
    fnc = defaultdict(Counter)
    for r, t, w in B.LA_ADMIN:
        fnc[w][t.get('function')] += 1
    major = {w: c.most_common(1)[0][0] for w, c in fnc.items()}
    ent = [w for w, f in major.items() if f == 'entry label']
    head = [w for w, f in major.items() if f == 'heading']
    spec = lambda ws: sum(1 for w in ws for x in w if x in ('pa3', 'ra2', 'pu2', 'ta2')) / max(1, sum(len(w) for w in ws))
    real, p, nm = label_perm(lambda a, b: spec(a) - spec(b), ent, head)
    record('D12 special signs in names', 'Special signs are commoner in entry labels than in headings',
           {'entry_share': round(spec(ent), 4), 'heading_share': round(spec(head), 4), 'p': round(p, 4), 'n': [len(ent), len(head)]}, {})
    return p


# ------------------------------------------------------------------ people at Knossos
def knossos_records():
    recs = []
    for _, r in B.LB_RECS:
        if r.get('site') != 'Knossos':
            continue
        logos, words = set(), set()
        for t in r.get('transliteratedWords', []):
            t = t.strip()
            m = re.match(r'^\*?([A-Z]{3,})', t)
            if m:
                logos.add(m.group(1))
            tl = t.lower()
            if '-' in tl and not any(ch in tl for ch in '[]?'):
                words.add(tuple(tl.split('-')))
        recs.append((logos, words))
    return recs


KREC = knossos_records()
_MLA, _MPY = V.nb_model(B.LA_NAMES), V.nb_model(PY_N)
minoan = lambda w: sum(_MLA(s) - _MPY(s) for s in w) / len(w)


def names_by(pred):
    on = set()
    for logos, words in KREC:
        if pred(logos, words):
            on |= words
    a = [w for w in KN_N if w in on]
    b = [w for w in KN_N if w not in on]
    return a, b


def auc_test(a, b, key, pred_text):
    stat = lambda x, y: V.auc([minoan(w) for w in x], [minoan(w) for w in y])
    real, p, nm = label_perm(stat, a, b)
    record(key, pred_text, {'auc': round(real, 3), 'null_mean': round(nm, 3), 'p': round(p, 4), 'n': [len(a), len(b)]}, {})
    return p


def D13():
    a, b = names_by(lambda logos, words: 'MUL' in logos)
    return auc_test(a, b, 'D13 names on women\'s tablets', 'Knossos names on MUL tablets are more Minoan-shaped than other Knossos names')


def D14():
    a, b = names_by(lambda logos, words: 'OVIS' in logos)
    return auc_test(a, b, 'D14 names on sheep tablets', 'Knossos names on OVIS tablets are more Minoan-shaped than other Knossos names')


def D15():
    topo = {w for w in V.kn_only if CAT.get(w) in ('toponym', 'ethnic')}
    a, b = names_by(lambda logos, words: bool(words & topo))
    return auc_test(a, b, 'D15 names beside Cretan place names', 'Knossos names on tablets with a Knossos-only place name are more Minoan-shaped')


def D16():
    _, count = B.N.lb_vocabulary()
    a = [w for w in KN_N if count[w] == 1]
    b = [w for w in KN_N if count[w] >= 2]
    return auc_test(a, b, 'D16 hapax names', 'Knossos names attested once are more Minoan-shaped than recurring ones')


def D25():
    oth = [w for w in V.kn_only if CAT.get(w) == 'other' and clean(w) and len(w) >= 2]
    ng = [w for w in oth if w not in B.GREEK]
    gk = [w for w in oth if w in B.GREEK]
    internal = lambda ws: [w[:-1] for w in ws]
    real, p, nm = label_perm(lambda x, y: E.eo(internal(x)) - E.eo(internal(y)), ng, gk, lower=True)
    record('D25 non-Greek common words', 'Knossos common words without a Greek etymology have fewer e/o syllables',
           {'non_greek': round(E.eo(internal(ng)), 4), 'greek': round(E.eo(internal(gk)), 4), 'p': round(p, 4), 'n': [len(ng), len(gk)]}, {})
    return p


# ------------------------------------------------------------------ bookkeeping
SCRIBE = {r['name']: r['scribe'] for r in B.READ['records']}
ENTRIES = B.entries_with(lambda ts: True)


def D17():
    recs = defaultdict(list)
    for x in ENTRIES:
        recs[x['record']].append(int(x['q']))
    tabs = [(SCRIBE.get(k), reduce(gcd, q) >= 2) for k, q in recs.items() if len(q) >= 3 and SCRIBE.get(k)]
    by = Counter(s for s, _ in tabs)
    tabs = [t for t in tabs if by[t[0]] >= 3]

    def stat(ts):
        c = Counter(ts)
        n = len(ts)
        rows = Counter(s for s, _ in ts)
        cols = Counter(f for _, f in ts)
        return sum((c[(r, k)] - rows[r] * cols[k] / n) ** 2 / (rows[r] * cols[k] / n) for r in rows for k in cols)
    real = stat(tabs)
    flags = [f for _, f in tabs]
    null = []
    for _ in range(REPS):
        rng.shuffle(flags)
        null.append(stat([(s, f) for (s, _), f in zip(tabs, flags)]))
    p = B.pv(null, real)
    record('D17 common divisors by scribe', 'Common-divisor tablets cluster by scribe',
           {'chi2': round(real, 2), 'p': round(p, 4), 'tablets': len(tabs)},
           {'per scribe (divisor tablets / tablets)': {s: f'{sum(f for s2, f in tabs if s2 == s)}/{n}' for s, n in by.items() if n >= 3}})
    return p


def tablet_sets():
    heads, coms = defaultdict(set), defaultdict(set)
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        for t in r['tokens']:
            if t['cls'] == 'word' and t.get('function') == 'heading':
                heads[r['name']].add(t['label'])
            if t['cls'] == 'commodity':
                m = re.findall(r'[A-Z]{3,}', t['label'])
                if m:
                    coms[r['name']].add(m[0])
    return heads, coms


def D18():
    heads, coms = tablet_sets()
    tabs = [t for t in heads if coms.get(t)]
    pairs = [(a, b) for i, a in enumerate(tabs) for b in tabs[i + 1:] if heads[a] & heads[b]]
    share = lambda cm: sum(bool(cm[a] & cm[b]) for a, b in pairs) / max(1, len(pairs))
    real = share(coms)
    sets = [coms[t] for t in tabs]
    null = []
    for _ in range(REPS):
        rng.shuffle(sets)
        null.append(share(dict(zip(tabs, sets))))
    p = B.pv(null, real)
    record('D18 shared headings, shared commodities', 'Tablets sharing a heading word share a commodity more than chance',
           {'share': round(real, 3), 'null_mean': round(sum(null) / len(null), 3), 'p': round(p, 4), 'pairs': len(pairs)},
           {'shared heading words': Counter(w for a, b in pairs for w in heads[a] & heads[b]).most_common(10)})
    return p


def entry_rows():
    rows = []
    for x in ENTRIES:
        for w in x['words']:
            if w not in ('KU-RO', 'KI-RO', 'PO-TO-KU-RO'):
                rows.append((w, x['com'], x['q'], x['record']))
    return rows


def D19():
    rows = [r for r in entry_rows() if r[1] and r[2] > 0]
    by_word = defaultdict(list)
    for i, r in enumerate(rows):
        by_word[r[0]].append(i)

    def stat(words):
        bw = defaultdict(list)
        for i, w in enumerate(words):
            bw[w].append(i)
        d = []
        for w, idx in bw.items():
            recs = {rows[i][3] for i in idx}
            if len(recs) < 2:
                continue
            for a in range(len(idx)):
                for b in range(a + 1, len(idx)):
                    i, j = idx[a], idx[b]
                    if rows[i][3] != rows[j][3]:
                        d.append(abs(log(rows[i][2]) - log(rows[j][2])))
        return sum(d) / len(d) if d else 0.0, len(d)
    words = [r[0] for r in rows]
    real, npairs = stat(words)
    by_com = defaultdict(list)
    for i, r in enumerate(rows):
        by_com[r[1]].append(i)
    null = []
    for _ in range(REPS):
        sh = list(words)
        for c, idx in by_com.items():
            ws = [words[i] for i in idx]
            rng.shuffle(ws)
            for i, w in zip(idx, ws):
                sh[i] = w
        null.append(stat(sh)[0])
    p = pv_lower(null, real)
    record('D19 same person, similar amounts', 'The same entry word on different tablets carries similar amounts',
           {'mean_abs_log_diff': round(real, 3), 'null_mean': round(sum(null) / len(null), 3), 'p': round(p, 4), 'pairs': npairs}, {})
    return p


def recurring_occ():
    occ = defaultdict(set)
    for w, c, q, rec in entry_rows():
        occ[w].add(rec)
    return {w: recs for w, recs in occ.items() if len(recs) >= 2}


def D20():
    occ = recurring_occ()
    recs = sorted({r for rs in occ.values() for r in rs if SCRIBE.get(r)})
    same = lambda sc: sum(sc[a] == sc[b] for rs in occ.values() for i, a in enumerate(sorted(rs)) for b in sorted(rs)[i + 1:]
                          if a in sc and b in sc) / max(1, sum(1 for rs in occ.values() for i, a in enumerate(sorted(rs))
                                                               for b in sorted(rs)[i + 1:] if a in sc and b in sc))
    sc = {r: SCRIBE[r] for r in recs}
    real = same(sc)
    labs = [sc[r] for r in recs]
    null = []
    for _ in range(REPS):
        rng.shuffle(labs)
        null.append(same(dict(zip(recs, labs))))
    p = B.pv(null, real)
    record('D20 recurring persons, same scribe', 'Recurring entry words stay with the same scribe more than chance',
           {'share_same_scribe': round(real, 3), 'null_mean': round(sum(null) / len(null), 3), 'p': round(p, 4), 'words': len(occ)}, {})
    return p


def D21():
    rows = [r for r in entry_rows() if r[1]]
    words = [r[0] for r in rows]
    coms = [r[1] for r in rows]

    def stat(ws):
        bw = defaultdict(list)
        for w, c, r in zip(ws, coms, rows):
            bw[w].append((c, r[3]))
        s, n = 0, 0
        for w, lst in bw.items():
            if len({x[1] for x in lst}) < 2:
                continue
            for i in range(len(lst)):
                for j in range(i + 1, len(lst)):
                    if lst[i][1] != lst[j][1]:
                        n += 1
                        s += lst[i][0] == lst[j][0]
        return s / max(1, n)
    real = stat(words)
    null = []
    for _ in range(REPS):
        sh = list(words)
        rng.shuffle(sh)
        null.append(stat(sh))
    p = B.pv(null, real)
    record('D21 recurring persons, same commodity', 'Recurring entry words stay with the same commodity more than chance',
           {'share_same_commodity': round(real, 3), 'null_mean': round(sum(null) / len(null), 3), 'p': round(p, 4)}, {})
    return p


def D22():
    tab_words = defaultdict(set)
    for w, c, q, rec in entry_rows():
        tab_words[rec].add(w)
    occ = recurring_occ()
    tabs = sorted(tab_words)

    def teams(tw):
        pc = Counter()
        for t, ws in tw.items():
            ws = sorted(w for w in ws if w in occ)
            for i, a in enumerate(ws):
                for b in ws[i + 1:]:
                    pc[(a, b)] += 1
        return sum(1 for v in pc.values() if v >= 2), [k for k, v in pc.items() if v >= 2]
    real, pairs = teams(tab_words)
    slots = [(t, w) for t in tabs for w in tab_words[t]]
    ws = [w for _, w in slots]
    null = []
    for _ in range(REPS):
        rng.shuffle(ws)
        tw = defaultdict(set)
        for (t, _), w in zip(slots, ws):
            tw[t].add(w)
        null.append(teams(tw)[0])
    p = B.pv(null, real)
    record('D22 teams', 'Recurring entry words recur together on two or more tablets more than chance',
           {'pairs_on_2plus_tablets': real, 'null_mean': round(sum(null) / len(null), 2), 'p': round(p, 4)},
           {'pairs': ['/'.join(x) for x in pairs[:20]]})
    return p


# ------------------------------------------------------------------ typology
def first_cons(words):
    c = Counter(grid(w[0])[0] or 'V' for w in words if grid(w[0]))
    n = sum(c.values())
    return {k: v / n for k, v in c.items()}


def jsd_d(p, q):
    keys = set(p) | set(q)
    m = {k: (p.get(k, 0) + q.get(k, 0)) / 2 for k in keys}
    kl = lambda a: sum(a[k] * log2(a[k] / m[k]) for k in keys if a.get(k, 0) > 0)
    return (kl(p) + kl(q)) / 2


def D23():
    la = first_cons(LA)
    stat = lambda pre, grk: jsd_d(la, first_cons(grk)) - jsd_d(la, first_cons(pre))
    real, p, nm = label_perm(stat, PRE, GRK)
    record('D23 first consonants', 'Pre-Greek first-syllable consonants resemble Linear A more than Greek ones do',
           {'jsd_LA_PreGreek': round(jsd_d(la, first_cons(PRE)), 4), 'jsd_LA_Greek': round(jsd_d(la, first_cons(GRK)), 4), 'p': round(p, 4)}, {})
    return p


def D24():
    lens = lambda ws: {L_: v / len(ws) for L_, v in Counter(min(len(w), 6) for w in ws).items()}
    la = lens(LA)
    stat = lambda pre, grk: jsd_d(la, lens(grk)) - jsd_d(la, lens(pre))
    real, p, nm = label_perm(stat, PRE, GRK_U)
    record('D24 word length', 'Linear A word lengths resemble Pre-Greek stems more than ordinary Greek stems',
           {'jsd_LA_PreGreek': round(jsd_d(la, lens(PRE)), 4), 'jsd_LA_Greek': round(jsd_d(la, lens(GRK_U)), 4), 'p': round(p, 4)},
           {'mean length (LA, Pre-Greek stems, Greek stems)': (round(sum(map(len, LA)) / len(LA), 2), round(sum(map(len, PRE)) / len(PRE), 2),
                                                               round(sum(map(len, GRK_U)) / len(GRK_U), 2))})
    return p


TESTS = [D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25]


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
    (ROOT / 'reading/decipher25_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str) + '\n', encoding='utf-8')
    print('\nprimary p:', {k: round(v, 4) for k, v in ps.items()})
    print('survive BH at 5%:', supported)


if __name__ == '__main__':
    main()
