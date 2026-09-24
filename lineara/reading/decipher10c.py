"""Ten hypotheses following the vowel lead of decipher10b.py and the name results, aimed at reading Linear A.

The fourteenth round found, exploratorily, that Linear A's e/i and o/u sign pairs behave more alike than Linear
B's. If Minoan had marginal e and o, several independent predictions follow; A1-A6 test them on data the
exploratory comparison did not use. A7-A10 use vowel-free matching (consonant skeletons), which such a vowel
system would favour, to look for Linear A words in the Linear B record.

Each has a prediction stated before the test ran, one primary test with its own null, and a Linear B control
where the method can run on the deciphered script. Benjamini-Hochberg at 5% runs across the ten.

A1  Variant spellings of Knossos names (Linear B, one vowel different, same consonant) alternate e/i or o/u more
    often than variant spellings of Pylos names.
A2  Linear A words that match a Linear B word but for one vowel (same consonant) differ by e/i or o/u more often
    than vowel frequencies predict.
A3  Linear A words that differ in one internal vowel (same consonant) differ by e/i or o/u more often than vowel
    frequencies predict. Control: Linear B.
A4  Across consonant rows, e-signs resemble i-signs and o-signs resemble u-signs in context more than other
    vowel pairs do (the within-row comparison of Z5/Z6 excluded). Control: Linear B.
A5  Knossos personal names have fewer e-syllables inside the word than Pylos names (an e-deficit, like the
    o-deficit).
A6  Linear A words on the same stem whose final signs differ only in vowel differ by e/i or o/u more often than
    vowel frequencies predict. Control: Linear B.
A7  Consonant-skeleton matches (same length and consonants, vowels ignored) between Linear A words and Linear B
    personal names are commoner for Knossos names than Pylos names, beyond the exact matches.
A8  Linear A religious words skeleton-match Linear B religious words and theonyms more often than Linear A
    administrative words do.
A9  Linear A heading words skeleton-match Linear B place names more often than Linear A entry words do.
A10 Linear A entry words skeleton-match Linear B personal names more often than Linear A heading words do.
"""
from collections import Counter, defaultdict
import json
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import batches as B  # noqa: E402
import decipher10 as D  # noqa: E402
import decipher10b as Db  # noqa: E402
import vigorous as V  # noqa: E402

ROOT = B.ROOT
rng = B.rng
REPS = B.REPS
out = D.out
out.clear()
record = D.record
grid = D.grid
CAT = B.LB_CAT
LA_W = Db.LA_W
LB_W = Db.LB_W
TARGET = ({'e', 'i'}, {'o', 'u'})
clean = lambda w: not any(x.startswith('*') for x in w)
KN_N = [w for w in V.kn_only if CAT.get(w) == 'anthroponym' and clean(w)]
PY_N = [w for w in V.py_only if CAT.get(w) == 'anthroponym' and clean(w)]


def is_target(a, b):
    return {a, b} in TARGET


def vowel_pairs(words_a, words_b=None, positions='any'):
    """(vowel in a, vowel in b) for word pairs of equal length differing in exactly one sign, where both signs are
    grid signs with the same consonant and different vowels. words_b None: pairs within words_a."""
    same = words_b is None
    words_b = words_a if same else words_b
    idx = defaultdict(list)
    for w in words_b:
        for i in range(len(w)):
            idx[(len(w), i, w[:i] + w[i + 1:])].append(w[i])
    out_ = []
    seen = set()
    for w in words_a:
        for i in range(len(w)):
            if positions == 'internal' and i == len(w) - 1:
                continue
            if positions == 'final' and i != len(w) - 1:
                continue
            a = w[i]
            ga = grid(a)
            if not ga:
                continue
            for b in idx.get((len(w), i, w[:i] + w[i + 1:]), ()):
                gb = grid(b)
                if gb and b != a and gb[0] == ga[0]:
                    key = (w[:i] + w[i + 1:], i, frozenset((a, b))) if same else (w, i, b)
                    if key not in seen:
                        seen.add(key)
                        out_.append((ga[1], gb[1]))
    return out_


def share_vs_freq(pairs, vfreq, reps=REPS):
    real = sum(is_target(a, b) for a, b in pairs) / max(1, len(pairs))
    vs = list(vfreq)
    null = []
    for _ in range(reps):
        hit = 0
        for a, _ in pairs:
            opts = [v for v in vs if v != a]
            b = rng.choices(opts, weights=[vfreq[v] for v in opts])[0]
            hit += is_target(a, b)
        null.append(hit / max(1, len(pairs)))
    return real, B.pv(null, real), sum(null) / len(null)


def vfreq_of(words):
    return Counter(grid(x)[1] for w in words for x in w if grid(x))


# ------------------------------------------------------------------ A1
def A1():
    kp = vowel_pairs(KN_N)
    pp = vowel_pairs(PY_N)
    lab = [0] * len(kp) + [1] * len(pp)
    allp = kp + pp
    share = lambda ps: sum(is_target(a, b) for a, b in ps) / max(1, len(ps))
    real = share(kp) - share(pp)
    null = []
    for _ in range(REPS):
        rng.shuffle(lab)
        null.append(share([p for p, l in zip(allp, lab) if l == 0]) - share([p for p, l in zip(allp, lab) if l == 1]))
    p = B.pv(null, real)
    record('A1 Knossos name variants', 'Knossos name variants alternate e/i or o/u more than Pylos name variants',
           {'KN_share': round(share(kp), 3), 'PY_share': round(share(pp), 3), 'p': round(p, 4), 'pairs': [len(kp), len(pp)]},
           {'KN alternations': dict(Counter(''.join(sorted(x)) for x in kp)), 'PY alternations': dict(Counter(''.join(sorted(x)) for x in pp))})
    return p


# ------------------------------------------------------------------ A2
def A2():
    pairs = vowel_pairs(LA_W, [w for w in LB_W if len(w) >= 2])
    pairs = [p for p in pairs]
    real, p, nm = share_vs_freq(pairs, vfreq_of(LB_W))
    kn = vowel_pairs(LA_W, KN_N)
    py = vowel_pairs(LA_W, PY_N)
    s = lambda ps: round(sum(is_target(a, b) for a, b in ps) / max(1, len(ps)), 3)
    record('A2 Linear A-Linear B near matches', 'One-vowel near matches between Linear A and Linear B words are e/i or o/u more than expected',
           {'share': round(real, 3), 'expected': round(nm, 3), 'p': round(p, 4), 'pairs': len(pairs)},
           {'against Knossos names': {'share': s(kn), 'pairs': len(kn)}, 'against Pylos names': {'share': s(py), 'pairs': len(py)},
            'alternations': dict(Counter(''.join(sorted(x)) for x in pairs))})
    return p


# ------------------------------------------------------------------ A3, A6
def within(words, positions):
    pairs = vowel_pairs(words, positions=positions)
    return pairs, share_vs_freq(pairs, vfreq_of(words))


def A3():
    pairs, (real, p, nm) = within(LA_W, 'internal')
    lp, (lr, lpv, lnm) = within(LB_W, 'internal')
    record('A3 internal vowel alternations', 'Linear A words differing in one internal vowel differ by e/i or o/u more than expected',
           {'share': round(real, 3), 'expected': round(nm, 3), 'p': round(p, 4), 'pairs': len(pairs)},
           {'Linear B control': {'share': round(lr, 3), 'expected': round(lnm, 3), 'p': round(lpv, 4), 'pairs': len(lp)},
            'alternations': dict(Counter(''.join(sorted(x)) for x in pairs))})
    return p


def A6():
    pairs, (real, p, nm) = within(LA_W, 'final')
    lp, (lr, lpv, lnm) = within(LB_W, 'final')
    record('A6 final vowel alternations', 'Linear A final-sign vowel alternations are e/i or o/u more than expected',
           {'share': round(real, 3), 'expected': round(nm, 3), 'p': round(p, 4), 'pairs': len(pairs)},
           {'Linear B control': {'share': round(lr, 3), 'expected': round(lnm, 3), 'p': round(lpv, 4), 'pairs': len(lp)},
            'alternations': dict(Counter(''.join(sorted(x)) for x in pairs))})
    return p


# ------------------------------------------------------------------ A4
def cross_row(words, reps):
    vecs = Db.ctx_vectors(words)
    signs = [s for s in vecs if grid(s)]
    sims = [(grid(a), grid(b), D.cos(vecs[a], vecs[b])) for i, a in enumerate(signs) for b in signs[i + 1:]
            if grid(a)[0] != grid(b)[0] and grid(a)[1] != grid(b)[1]]

    def stat(vl):
        t = [v for a, b, v in sims if is_target(vl[a], vl[b])]
        o = [v for a, b, v in sims if not is_target(vl[a], vl[b])]
        return sum(t) / len(t) - sum(o) / len(o)
    base = {grid(s): grid(s)[1] for s in signs}
    real = stat(base)
    keys = list(base)
    null = []
    for _ in range(reps):
        vals = [k[1] for k in keys]
        rng.shuffle(vals)
        m = dict(zip(keys, vals))
        sims_perm = [(a, b, v) for a, b, v in sims if m[a] != m[b]]
        t = [v for a, b, v in sims_perm if is_target(m[a], m[b])]
        o = [v for a, b, v in sims_perm if not is_target(m[a], m[b])]
        if t and o:
            null.append(sum(t) / len(t) - sum(o) / len(o))
    return real, B.pv(null, real)


def A4():
    r, p = cross_row(LA_W, REPS)
    lr, lp = cross_row(LB_W, REPS)
    record('A4 cross-row vowel affinity', 'Across rows, e-signs resemble i-signs and o-signs u-signs more than other vowel pairs',
           {'diff': round(r, 4), 'p': round(p, 4)}, {'Linear B control': {'diff': round(lr, 4), 'p': round(lp, 4)}})
    return p


# ------------------------------------------------------------------ A5
def internal_share(ws, v):
    s = [x for w in ws for x in w[:-1] if grid(x)]
    return sum(grid(x)[1] == v for x in s) / len(s)


def A5():
    stat = lambda a, b: internal_share(b, 'e') - internal_share(a, 'e')
    real, p, nm = Db.label_perm(stat, KN_N, PY_N, REPS) if hasattr(Db, 'label_perm') else (None, None, None)
    if real is None:
        pool, k, null = KN_N + PY_N, len(KN_N), []
        real = stat(KN_N, PY_N)
        for _ in range(REPS):
            rng.shuffle(pool)
            null.append(stat(pool[:k], pool[k:]))
        p = B.pv(null, real)
    no_eu = lambda ws: [w for w in ws if not (len(w) >= 2 and w[-2:] == ('e', 'u'))]
    kn2, py2 = no_eu(KN_N), no_eu(PY_N)
    pool2, k2, null2 = kn2 + py2, len(kn2), []
    r2 = stat(kn2, py2)
    for _ in range(REPS):
        rng.shuffle(pool2)
        null2.append(stat(pool2[:k2], pool2[k2:]))
    first = lambda ws: sum(grid(w[0])[1] == 'e' for w in ws if grid(w[0])) / len(ws)
    sf = lambda a, b: first(b) - first(a)
    pool3, null3 = kn2 + py2, []
    r3 = sf(kn2, py2)
    for _ in range(REPS):
        rng.shuffle(pool3)
        null3.append(sf(pool3[:k2], pool3[k2:]))
    kn_c = [w for w in V.kn_only if CAT.get(w) == 'other' and clean(w) and len(w) >= 2]
    py_c = [w for w in V.py_only if CAT.get(w) == 'other' and clean(w) and len(w) >= 2]
    pool4, k4, null4 = kn_c + py_c, len(kn_c), []
    r4 = stat(kn_c, py_c)
    for _ in range(REPS):
        rng.shuffle(pool4)
        null4.append(stat(pool4[:k4], pool4[k4:]))
    record('A5 e-deficit in Knossos names', 'Knossos names have fewer internal e-syllables than Pylos names',
           {'KN': round(internal_share(KN_N, 'e'), 4), 'PY': round(internal_share(PY_N, 'e'), 4), 'p': round(p, 4)},
           {'Linear A internal e': round(internal_share(LA_W, 'e'), 4), 'Linear B all words internal e': round(internal_share(LB_W, 'e'), 4),
            'i for comparison (KN, PY)': (round(internal_share(KN_N, 'i'), 4), round(internal_share(PY_N, 'i'), 4)),
            'names ending -e-u removed': {'KN': round(internal_share(kn2, 'e'), 4), 'PY': round(internal_share(py2, 'e'), 4), 'p': round(B.pv(null2, r2), 4),
                                          'removed': [len(KN_N) - len(kn2), len(PY_N) - len(py2)]},
            'first syllable only (-e-u names removed)': {'KN': round(first(kn2), 4), 'PY': round(first(py2), 4), 'p': round(B.pv(null3, r3), 4)},
            'control common words': {'KN': round(internal_share(kn_c, 'e'), 4), 'PY': round(internal_share(py_c, 'e'), 4), 'p': round(B.pv(null4, r4), 4)}})
    return p


# ------------------------------------------------------------------ skeletons
def skel(w):
    out_ = []
    for x in w:
        g = grid(x)
        if g:
            out_.append(g[0] or 'V')
        elif x in Db.SPECIAL_ROW:
            out_.append(Db.SPECIAL_ROW[x] or 'V')
        else:
            return None
    return tuple(out_)


def skel_index(words):
    idx = defaultdict(set)
    for w in words:
        if len(w) >= 3:
            s = skel(w)
            if s:
                idx[s].add(w)
    return idx


LA3 = [w for w in LA_W if len(w) >= 3]


def skel_rate(la, lb_words, exclude_exact=True):
    idx = skel_index(lb_words)
    lbs = set(lb_words)
    hits = [w for w in la if skel(w) in idx and not (exclude_exact and w in lbs)]
    return len(hits) / max(1, len(la)), hits


# ------------------------------------------------------------------ A7
def A7():
    kn3 = [w for w in KN_N if len(w) >= 3]
    py3 = [w for w in PY_N if len(w) >= 3]
    la_sk = Counter(skel(w) for w in LA3 if skel(w))
    la_set = set(LA3)
    # rate per Linear B name: its skeleton occurs in Linear A, but the name itself is not a Linear A word
    rate = lambda ns: sum(1 for w in ns if skel(w) in la_sk and w not in la_set) / max(1, len(ns))
    real = rate(kn3) - rate(py3)
    pool, k, null = kn3 + py3, len(kn3), []
    for _ in range(REPS):
        rng.shuffle(pool)
        null.append(rate(pool[:k]) - rate(pool[k:]))
    p = B.pv(null, real)
    # control: common words
    kn_c = [w for w in V.kn_only if CAT.get(w) == 'other' and clean(w) and len(w) >= 3]
    py_c = [w for w in V.py_only if CAT.get(w) == 'other' and clean(w) and len(w) >= 3]
    rc = rate(kn_c) - rate(py_c)
    pool2, k2, null2 = kn_c + py_c, len(kn_c), []
    for _ in range(REPS):
        rng.shuffle(pool2)
        null2.append(rate(pool2[:k2]) - rate(pool2[k2:]))
    by_len = {}
    for L, name in ((3, 'three signs'), (4, 'four or more signs')):
        a = [w for w in kn3 if (len(w) == 3 if L == 3 else len(w) >= 4)]
        b = [w for w in py3 if (len(w) == 3 if L == 3 else len(w) >= 4)]
        pl, kk, nl = a + b, len(a), []
        rr = rate(a) - rate(b)
        for _ in range(REPS):
            rng.shuffle(pl)
            nl.append(rate(pl[:kk]) - rate(pl[kk:]))
        by_len[name] = {'KN': round(rate(a), 4), 'PY': round(rate(b), 4), 'p': round(B.pv(nl, rr), 4), 'n': [len(a), len(b)]}
    no_eu = [w for w in py3 if w[-2:] != ('e', 'u')]
    pl, kk, nl = kn3 + no_eu, len(kn3), []
    rr = rate(kn3) - rate(no_eu)
    for _ in range(REPS):
        rng.shuffle(pl)
        nl.append(rate(pl[:kk]) - rate(pl[kk:]))
    record('A7 skeleton matches by site', 'Knossos names skeleton-match Linear A words more than Pylos names, beyond exact matches',
           {'KN_rate': round(rate(kn3), 4), 'PY_rate': round(rate(py3), 4), 'p': round(p, 4), 'n': [len(kn3), len(py3)]},
           {'control common words': {'KN': round(rate(kn_c), 4), 'PY': round(rate(py_c), 4), 'p': round(B.pv(null2, rc), 4)},
            'by length': by_len, 'Pylos -e-u names removed': {'PY': round(rate(no_eu), 4), 'p': round(B.pv(nl, rr), 4)},
            'mean length (KN, PY)': (round(sum(map(len, kn3)) / len(kn3), 2), round(sum(map(len, py3)) / len(py3), 2))})
    return p


# ------------------------------------------------------------------ A8
REL_KEYS = ('theonym', 'god', 'goddess', 'deity', 'sanctuary', 'priest', 'priestess', 'offering', 'religious', 'cult', 'shrine')


def lb_religious():
    lex = json.loads((ROOT / 'data/linearb/tiripode_lexicon.json').read_text(encoding='utf-8'))
    out_ = set()
    for k, v in lex.items():
        d = v['definition'].lower()
        if any(re.search(r'\b' + x + r'\b', d) for x in REL_KEYS):
            out_.add(tuple(k.lower().split('-')))
    return out_


def la_register_types():
    rel = {w for _, _, w in B.LA_RELIG if len(w) >= 3 and all(grid(x) or x in Db.SPECIAL_ROW for x in w)}
    adm = {w for _, _, w in B.LA_ADMIN if len(w) >= 3 and all(grid(x) or x in Db.SPECIAL_ROW for x in w)} - rel
    return sorted(rel), sorted(adm)


def A8():
    lbr = sorted(w for w in lb_religious() if len(w) >= 3)
    rel, adm = la_register_types()
    stat = lambda a, b: skel_rate(a, lbr, False)[0] - skel_rate(b, lbr, False)[0]
    real = stat(rel, adm)
    pool, k, null = rel + adm, len(rel), []
    for _ in range(REPS):
        rng.shuffle(pool)
        null.append(stat(pool[:k], pool[k:]))
    p = B.pv(null, real)
    idx = skel_index(lbr)
    hits = {'-'.join(w).upper(): sorted('-'.join(x) for x in idx[skel(w)]) for w in rel if skel(w) in idx}
    record('A8 religious skeleton matches', 'Linear A religious words skeleton-match Linear B religious words more than administrative words do',
           {'rel_rate': round(skel_rate(rel, lbr, False)[0], 4), 'adm_rate': round(skel_rate(adm, lbr, False)[0], 4), 'p': round(p, 4),
            'n': [len(rel), len(adm)], 'lb_religious_words': len(lbr)},
           {'matches': hits})
    return p


# ------------------------------------------------------------------ A9, A10
def la_by_function():
    fn = defaultdict(Counter)
    for r, t, w in B.LA_ADMIN:
        if len(w) >= 3 and all(grid(x) or x in Db.SPECIAL_ROW for x in w):
            fn[w][t.get('function')] += 1
    head = sorted(w for w, c in fn.items() if c.most_common(1)[0][0] == 'heading')
    ent = sorted(w for w, c in fn.items() if c.most_common(1)[0][0] == 'entry label')
    return head, ent


def function_test(target_cat, a_is_head):
    lbw = sorted(w for w in B.LB_SITES if len(w) >= 3 and CAT.get(w) == target_cat and clean(w))
    head, ent = la_by_function()
    a, b = (head, ent) if a_is_head else (ent, head)
    stat = lambda x, y: skel_rate(x, lbw, False)[0] - skel_rate(y, lbw, False)[0]
    real = stat(a, b)
    pool, k, null = a + b, len(a), []
    for _ in range(REPS):
        rng.shuffle(pool)
        null.append(stat(pool[:k], pool[k:]))
    idx = skel_index(lbw)
    hits = {'-'.join(w).upper(): sorted('-'.join(x) for x in idx[skel(w)])[:6] for w in a if skel(w) in idx}
    return real, B.pv(null, real), skel_rate(a, lbw, False)[0], skel_rate(b, lbw, False)[0], len(a), len(b), len(lbw), hits


def A9():
    real, p, ra, rb, na, nb, nl, hits = function_test('toponym', True)
    record('A9 headings and place names', 'Linear A headings skeleton-match Linear B place names more than entry words do',
           {'heading_rate': round(ra, 4), 'entry_rate': round(rb, 4), 'p': round(p, 4), 'n': [na, nb], 'lb_toponyms': nl},
           {'heading matches': hits})
    return p


def A10():
    real, p, ra, rb, na, nb, nl, hits = function_test('anthroponym', False)
    record('A10 entries and personal names', 'Linear A entry words skeleton-match Linear B personal names more than headings do',
           {'entry_rate': round(ra, 4), 'heading_rate': round(rb, 4), 'p': round(p, 4), 'n': [na, nb], 'lb_names': nl},
           {'number of entry words with a match': len(hits)})
    return p


def main():
    ps = {}
    for fn in (A1, A2, A3, A4, A5, A6, A7, A8, A9, A10):
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
    (ROOT / 'reading/decipher10c_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str) + '\n', encoding='utf-8')
    print('\nprimary p:', {k: round(v, 4) for k, v in ps.items()})
    print('survive BH at 5%:', supported)


if __name__ == '__main__':
    main()
