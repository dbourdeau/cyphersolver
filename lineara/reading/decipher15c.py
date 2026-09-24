"""Fifteen hypotheses building on decipher25b.py: the coronal rule used as a tool, scribal practice, where the
Minoan-shaped names sit in the Linear B archives, and what the left-context result implies.

Each has a prediction stated before the test ran and one primary test with its own null. Benjamini-Hochberg at
5% runs across the fifteen. Per-tablet tests merge sides a and b.

The coronal rule as a tool
F1  If e/o after dentals are variants of i/u, words that differ only by i~e or u~o alternate after dentals
    (TI/TE, RU/RO ...) more often than after other consonants.
F2  Treating dental e/o as i/u gains more Linear A - Knossos name matches than treating non-dental e/o the same way.
F3  The rule is stronger in Late Minoan than in Middle Minoan texts.
F4  The rule holds in the religious texts.
Scribes and totals
F5  Near-identical spellings of the same word (one sign different) come from different scribes more than chance.
F6  The preference for even amounts differs by scribe.
F14 When a total does not balance, the gap equals one of the tablet's entry amounts more than chance.
Names in the Linear B archives (stem-scored, final syllable removed)
F7  Minoan-shaped Knossos names cluster by tablet series.
F8  Pylos names cluster by series on the same measure.
F13 Knossos scribes whose names are more Minoan-shaped also use more undeciphered signs.
F15 Pylos names on the women's-work tablets (Aa, Ab, Ad) are more Minoan-shaped than other Pylos names.
Signs
F9  Neighbouring syllables avoid consonants of the same place of articulation, more than in Linear B.
F10 A syllable's vowel predicts the next syllable's consonant row more than in Linear B.
F11 The preceding sign alone recovers a hidden sign's consonant row better than chance.
Accounts
F12 Doubled amounts (one entry twice another) stand on neighbouring lines more than chance.
"""
from collections import Counter, defaultdict
from fractions import Fraction
import json
from math import log
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import decipher25b as X  # noqa: E402

T, B, D, Db, E, V = X.T, X.B, X.D, X.Db, X.E, X.V
ROOT = B.ROOT
rng = X.rng
REPS = 1000
out = D.out
out.clear()
record = D.record
grid = D.grid
LA, LB = X.LA, X.LB
COR, NONCOR, RARE = X.COR, X.NONCOR, X.RARE
DENT = set('tdnrs')
PLACE = {'p': 'lab', 'm': 'lab', 'w': 'lab', 't': 'den', 'd': 'den', 'n': 'den', 'r': 'den', 's': 'den', 'z': 'den',
         'k': 'vel', 'q': 'vel'}


# ------------------------------------------------------------------ coronal rule as a tool
def vowel_alternations(words):
    idx = defaultdict(set)
    for w in words:
        for i in range(len(w)):
            idx[(len(w), i, w[:i] + w[i + 1:])].add(w[i])
    alts = []
    for _, signs in idx.items():
        signs = sorted(signs)
        for i, a in enumerate(signs):
            for b in signs[i + 1:]:
                ga, gb = grid(a), grid(b)
                if ga and gb and ga[0] and ga[0] == gb[0] and ga[1] != gb[1]:
                    alts.append((ga[0], frozenset((ga[1], gb[1]))))
    return alts


def F1():
    alts = vowel_alternations(LA)
    target = lambda v: v in (frozenset('ie'), frozenset('uo'))
    is_t = [target(v) for _, v in alts]
    dent = [c in DENT for c, _ in alts]

    def stat(flags):
        a = [d for d, f in zip(dent, flags) if f]
        b = [d for d, f in zip(dent, flags) if not f]
        return sum(a) / max(1, len(a)) - sum(b) / max(1, len(b))
    real, p, nm = X.shuffle_test(stat, is_t)
    ex = Counter(c + '/' + ''.join(sorted(v)) for c, v in alts if target(v))
    record('F1 dental i~e, u~o alternations', 'i~e and u~o alternations occur after dentals more than other vowel alternations do',
           {'dental_share_ie_uo': round(sum(d for d, f in zip(dent, is_t) if f) / max(1, sum(is_t)), 3),
            'dental_share_other': round(sum(d for d, f in zip(dent, is_t) if not f) / max(1, len(is_t) - sum(is_t)), 3),
            'p': round(p, 4), 'alternations': [sum(is_t), len(is_t) - sum(is_t)]}, {'i~e / u~o by consonant': dict(ex)})
    return p


def collapse(w, cons):
    outw = []
    for x in w:
        g = grid(x)
        if g and g[0] in cons and g[1] in 'eo':
            outw.append(g[0] + {'e': 'i', 'o': 'u'}[g[1]])
        else:
            outw.append(x)
    return tuple(outw)


def gain(la, lb, cons):
    base = sum(1 for w in la if w in set(lb))
    lbc = {collapse(w, cons) for w in lb}
    return sum(1 for w in la if collapse(w, cons) in lbc) - base


def F2():
    la = [w for w in LA if len(w) >= 2]
    kn = T.KN_N
    nond = set('pmwkqj')
    real = gain(la, kn, DENT) - gain(la, kn, nond)
    boot = []
    for _ in range(REPS):
        smp = [rng.choice(la) for _ in la]
        boot.append(gain(smp, kn, DENT) - gain(smp, kn, nond))
    p = (sum(b <= 0 for b in boot) + 1) / (len(boot) + 1)
    lbc = {collapse(w, DENT): w for w in kn}
    new = sorted(f"{'-'.join(w).upper()} ~ {'-'.join(lbc[collapse(w, DENT)])}" for w in la
                 if w not in set(kn) and collapse(w, DENT) in lbc)
    record('F2 matches under the rule', 'Collapsing dental e/o to i/u gains more Linear A - Knossos name matches than collapsing non-dental ones',
           {'gain_dental': gain(la, kn, DENT), 'gain_nondental': gain(la, kn, nond), 'bootstrap p': round(p, 4)},
           {'new matches under the dental collapse': new,
            'control, Pylos names': {'dental': gain(la, T.PY_N, DENT), 'nondental': gain(la, T.PY_N, nond)}})
    return p


def period_words(label):
    return sorted({w for r, t, w in B.words_of() if B.period(r) == label and not any(x in Db.LOGO for x in w)})


def F3():
    mm, lm = period_words('MM'), period_words('LM')
    f = lambda ws: X.log_or_v(ws, RARE)
    real, p, nm = X.compare(lm, mm, f)
    record('F3 rule over time', 'The coronal rule is stronger in Late Minoan than Middle Minoan texts',
           {'logOR_LM': round(f(lm), 3), 'logOR_MM': round(f(mm), 3), 'p': round(p, 4), 'words': [len(lm), len(mm)]}, {})
    return p


def F4():
    rel = sorted({w for _, _, w in B.LA_RELIG})
    f = lambda ws: X.log_or_v(ws, RARE)
    real, p, nm = X.compare(rel, LB, f)
    rel_nf = [w for w in rel if not V.FORMULA.search('-'.join(w).upper())]
    r2, p2, _ = X.compare(rel_nf, LB, f)
    record('F4 rule in religious texts', 'The coronal rule holds in the religious texts',
           {'logOR_religious': round(f(rel), 3), 'logOR_LB': round(f(LB), 3), 'p': round(p, 4), 'words': len(rel)},
           {'formula removed': {'logOR': round(f(rel_nf), 3), 'p': round(p2, 4)}})
    return p


# ------------------------------------------------------------------ scribes and totals
def F5():
    sc = defaultdict(set)
    for r, t, w in B.words_of():
        s = X.SCRIBE_W.get(X.whole(r['name']))
        if s:
            sc[w].add(s)
    types = [w for w in sc if len(w) >= 3]
    idx = defaultdict(list)
    for w in types:
        for i in range(len(w)):
            idx[(len(w), i, w[:i] + w[i + 1:])].append(w)
    pairs = {tuple(sorted((a, b))) for ws in idx.values() for i, a in enumerate(ws) for b in ws[i + 1:]}
    disjoint = lambda a, b: not (sc[a] & sc[b])
    real = sum(disjoint(a, b) for a, b in pairs) / len(pairs)
    by_len = defaultdict(list)
    for w in types:
        by_len[len(w)].append(w)
    null = []
    for _ in range(REPS):
        hits = 0
        for a, b in pairs:
            x, y = rng.sample(by_len[len(a)], 2)
            hits += disjoint(x, y)
        null.append(hits / len(pairs))
    p = B.pv(null, real)
    record('F5 spelling variants across scribes', 'Near-identical spellings come from different scribes more than random word pairs do',
           {'share_disjoint': round(real, 3), 'null_mean': round(sum(null) / len(null), 3), 'p': round(p, 4), 'pairs': len(pairs)},
           {'examples (different scribes)': sorted(f"{'-'.join(a).upper()} / {'-'.join(b).upper()}" for a, b in pairs if disjoint(a, b))[:15]})
    return p


def F6():
    rows = [(X.SCRIBE_W.get(X.whole(x['record'])), int(x['q']) % 2 == 0) for x in T.ENTRIES if int(x['q']) > 0]
    rows = [r for r in rows if r[0]]
    by = Counter(s for s, _ in rows)
    rows = [r for r in rows if by[r[0]] >= 10]
    names = [s for s, _ in rows]
    stat = lambda fl: X.chi2(list(zip(names, fl)))
    real, p, nm = X.shuffle_test(stat, [f for _, f in rows])
    record('F6 even amounts by scribe', 'The preference for even amounts differs by scribe',
           {'chi2': round(real, 2), 'null_mean': round(nm, 2), 'p': round(p, 4), 'entries': len(rows)},
           {'even share by scribe': {s: round(sum(f for s2, f in rows if s2 == s) / n, 2) for s, n in by.items() if n >= 10}})
    return p


def frac(s):
    return Fraction(s) if s not in (None, '') else None


def F14():
    items = []
    q_of = defaultdict(list)
    for x in T.ENTRIES:
        q_of[x['record']].append(Fraction(x['q']))
    for c in B.READ['totals']:
        if c['balances_in_some_window'] or c['stated_damaged'] or c['stated_has_unvalued'] or c['damage_in_windows']:
            continue
        d = frac(c['smallest_discrepancy'])
        if d and q_of.get(c['record']):
            items.append((c['record'], d, q_of[c['record']]))
    hit = lambda d, qs: d in set(qs)
    real = sum(hit(d, qs) for _, d, qs in items)
    lists = [qs for _, _, qs in items]
    null = []
    for _ in range(5000):
        rng.shuffle(lists)
        null.append(sum(hit(d, qs) for (_, d, _), qs in zip(items, lists)))
    p = B.pv(null, real)
    record('F14 errors of one entry', 'When a total does not balance, the gap equals an entry amount more than chance',
           {'hits': f'{real}/{len(items)}', 'null_mean': round(sum(null) / len(null), 2), 'p': round(p, 4)},
           {'totals': [f'{r}: gap {d}' for r, d, _ in items]})
    return p


# ------------------------------------------------------------------ names in the Linear B archives
def series_of(label):
    parts = label.split()
    return re.sub(r'\(.*\)', '', parts[1]) if len(parts) > 1 else ''


def name_series(site):
    sc = defaultdict(Counter)
    for _, r in B.LB_RECS:
        if r.get('site') != site:
            continue
        s = series_of(r.get('label', ''))
        if not s or s.startswith('X'):
            continue
        for t in r.get('transliteratedWords', []):
            tl = t.strip().lower()
            if '-' in tl and not any(ch in tl for ch in '[]?'):
                sc[tuple(tl.split('-'))][s] += 1
    return sc


MLA = V.nb_model(B.LA_NAMES)
MCOM = V.nb_model([w for w, s in B.LB_SITES.items() if T.CAT.get(w) == 'other' and T.clean(w)])
score_common = lambda w: sum(MLA(s) - MCOM(s) for s in w[:-1]) / len(w[:-1]) if len(w) >= 3 else sum(MLA(s) - MCOM(s) for s in w) / len(w)


def cluster(names, groups, scorer, min_n=5):
    keep = Counter(groups)
    idx = [i for i, g in enumerate(groups) if keep[g] >= min_n]
    names = [names[i] for i in idx]
    groups = [groups[i] for i in idx]
    vals = [scorer(w) for w in names]
    mu = sum(vals) / len(vals)

    def between(v):
        g = defaultdict(list)
        for s, x in zip(groups, v):
            g[s].append(x)
        return sum(len(xs) * (sum(xs) / len(xs) - mu) ** 2 for xs in g.values())
    real, p, nm = X.shuffle_test(between, vals)
    g = defaultdict(list)
    for s, x in zip(groups, vals):
        g[s].append(x)
    top = sorted(((round(sum(v) / len(v), 3), s, len(v)) for s, v in g.items()), reverse=True)
    return real, p, nm, len(names), top


def F7():
    sc = name_series('Knossos')
    names = [w for w in T.KN_N if w in sc]
    groups = [sc[w].most_common(1)[0][0] for w in names]
    real, p, nm, n, top = cluster(names, groups, X.stem_score)
    record('F7 Knossos names by series', 'Minoan-shaped Knossos names cluster by tablet series',
           {'between_SS': round(real, 3), 'null_mean': round(nm, 3), 'p': round(p, 4), 'names': n},
           {'most Minoan series': top[:6], 'least Minoan series': top[-4:]})
    return p


def F8():
    sc = name_series('Pylos')
    names = [w for w in T.PY_N if w in sc]
    groups = [sc[w].most_common(1)[0][0] for w in names]
    real, p, nm, n, top = cluster(names, groups, score_common)
    record('F8 Pylos names by series', 'Minoan-shaped Pylos names cluster by tablet series',
           {'between_SS': round(real, 3), 'null_mean': round(nm, 3), 'p': round(p, 4), 'names': n},
           {'most Minoan series': top[:6], 'least Minoan series': top[-4:]})
    return p


def F15():
    sc = name_series('Pylos')
    women = [w for w in T.PY_N if w in sc and set(sc[w]) & {'Aa', 'Ab', 'Ad'}]
    other = [w for w in T.PY_N if w in sc and w not in set(women)]
    real, p, nm = T.label_perm(lambda a, b: V.auc([score_common(w) for w in a], [score_common(w) for w in b]), women, other)
    record('F15 Pylos women\'s-work names', 'Pylos names on Aa/Ab/Ad tablets are more Minoan-shaped (stem-scored) than other Pylos names',
           {'auc': round(real, 3), 'null_mean': round(nm, 3), 'p': round(p, 4), 'n': [len(women), len(other)]}, {})
    return p


def F13():
    per = defaultdict(lambda: {'names': [], 'star': 0, 'words': 0})
    for _, r in B.LB_RECS:
        if r.get('site') != 'Knossos' or not r.get('scribe'):
            continue
        d = per[r['scribe']]
        for t in r.get('transliteratedWords', []):
            tl = t.strip().lower()
            if '-' in tl and not any(ch in tl for ch in '[]?'):
                w = tuple(tl.split('-'))
                d['words'] += 1
                d['star'] += any(x.startswith('*') for x in w)
                if w in set(T.KN_N):
                    d['names'].append(w)
    rows = [(s, sum(map(X.stem_score, d['names'])) / len(d['names']), d['star'] / d['words']) for s, d in per.items()
            if len(d['names']) >= 5 and d['words'] >= 20]
    xs, ys = [r[1] for r in rows], [r[2] for r in rows]
    real = B.spearman(xs, ys)
    null = []
    for _ in range(5000):
        y2 = list(ys)
        rng.shuffle(y2)
        null.append(B.spearman(xs, y2))
    p = B.pv(null, real)
    record('F13 Minoan names and undeciphered signs by scribe', 'Knossos scribes with more Minoan-shaped names use more undeciphered signs',
           {'spearman': round(real, 3), 'p': round(p, 4), 'scribes': len(rows)}, {})
    return p


# ------------------------------------------------------------------ signs
def adjacent_place(words, reps):
    ws = [w for w in words if all(grid(x) for x in w)]

    def stat(wl):
        pairs = [(grid(w[i])[0], grid(w[i + 1])[0]) for w in wl for i in range(len(w) - 1)]
        pairs = [(a, b) for a, b in pairs if a in PLACE and b in PLACE]
        return sum(PLACE[a] == PLACE[b] for a, b in pairs) / len(pairs)
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
    nm = sum(null) / len(null)
    return real, nm, T.pv_lower(null, real)


def F9():
    r, nm, p = adjacent_place(LA, REPS)
    lr, lnm, lp = adjacent_place(LB, 300)
    record('F9 place dissimilation', 'Neighbouring syllables avoid consonants of the same place of articulation',
           {'same_place_share': round(r, 4), 'null_mean': round(nm, 4), 'ratio': round(r / nm, 3), 'p': round(p, 4)},
           {'Linear B control': {'share': round(lr, 4), 'null_mean': round(lnm, 4), 'ratio': round(lr / lnm, 3), 'p': round(lp, 4)}})
    return p


def vc_nmi(words):
    pairs = [(grid(w[i])[1], grid(w[i + 1])[0] or 'V') for w in words for i in range(len(w) - 1) if grid(w[i]) and grid(w[i + 1])]
    n = len(pairs)
    a, b, ab = Counter(x for x, _ in pairs), Counter(y for _, y in pairs), Counter(pairs)
    h = -sum(c / n * log(c / n) for c in b.values())
    mi = sum(c / n * log(c * n / (a[x] * b[y])) for (x, y), c in ab.items())
    return mi / h, n


def F10():
    real, n = vc_nmi(LA)
    null = []
    for _ in range(500):
        smp, k = [], 0
        while k < n:
            w = rng.choice(LB)
            smp.append(w)
            k += max(0, len(w) - 1)
        null.append(vc_nmi(smp)[0])
    p = B.pv(null, real)
    # the Linear A value is inflated by its small sample only if shuffled Linear A shows the same; check
    flat = [list(w) for w in LA]
    sh_null = []
    for _ in range(300):
        pool = [x for w in flat for x in w]
        rng.shuffle(pool)
        k, sh = 0, []
        for w in flat:
            sh.append(tuple(pool[k:k + len(w)]))
            k += len(w)
        sh_null.append(vc_nmi(sh)[0])
    record('F10 vowel predicts next consonant', 'A syllable\'s vowel predicts the next consonant row more than in Linear B',
           {'nmi_LA': round(real, 4), 'nmi_LB_subsampled': round(sum(null) / len(null), 4), 'p': round(p, 4)},
           {'Linear A with signs shuffled': round(sum(sh_null) / len(sh_null), 4)})
    return p


def left_vectors(words):
    raw = {s: Counter({f: v for f, v in c.items() if f.startswith('L:')}) for s, c in D.contexts(words).items() if grid(s)}
    tot = sum(sum(c.values()) for c in raw.values())
    feat = Counter()
    for c in raw.values():
        feat.update(c)
    vec = {}
    for s, c in raw.items():
        ns = sum(c.values())
        vec[s] = {f: log(x * tot / (ns * feat[f])) for f, x in c.items() if x * tot > ns * feat[f]}
    return {s: v for s, v in vec.items() if v}


def F11():
    vecs = left_vectors(LA)
    signs = sorted(vecs)
    labels = {s: grid(s) for s in signs}
    acc = lambda lab: sum(Db.knn_predict(vecs, s, lab, 0) == lab[s][0] for s in signs) / len(signs)
    real = acc(labels)
    labs = [labels[s] for s in signs]
    null = []
    for _ in range(300):
        rng.shuffle(labs)
        null.append(acc(dict(zip(signs, labs))))
    p = B.pv(null, real)
    lbv = left_vectors(LB)
    lb_acc = sum(Db.knn_predict(lbv, s, {t: grid(t) for t in lbv}, 0) == grid(s)[0] for s in lbv) / len(lbv)
    record('F11 left context recovers the row', 'The preceding sign alone recovers a hidden sign\'s consonant row',
           {'accuracy': round(real, 3), 'null_mean': round(sum(null) / len(null), 3), 'p': round(p, 4), 'signs': len(signs)},
           {'Linear B control accuracy': round(lb_acc, 3)})
    return p


# ------------------------------------------------------------------ accounts
def F12():
    lists = []
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        seq = []
        ents = defaultdict(list)
        for tok in r['tokens']:
            ents[tok['entry']].append(tok)
        for _, toks in sorted(ents.items()):
            q = sum(t['value'] for t in toks if t['cls'] == 'number')
            if q:
                seq.append(q)
        if len(seq) >= 3:
            lists.append(seq)
    adj = lambda ls: sum(1 for q in ls for i in range(len(q) - 1) if q[i] == 2 * q[i + 1] or q[i + 1] == 2 * q[i])
    real = adj(lists)
    null = []
    for _ in range(REPS):
        sh = []
        for q in lists:
            q2 = list(q)
            rng.shuffle(q2)
            sh.append(q2)
        null.append(adj(sh))
    p = B.pv(null, real)
    record('F12 doubles on neighbouring lines', 'Doubled amounts stand on neighbouring lines more than chance',
           {'adjacent_doubles': real, 'null_mean': round(sum(null) / len(null), 2), 'p': round(p, 4), 'lists': len(lists)}, {})
    return p


TESTS = [F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, F13, F14, F15]


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
    (ROOT / 'reading/decipher15c_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str) + '\n', encoding='utf-8')
    print('\nprimary p:', {k: round(v, 4) for k, v in ps.items()})
    print('survive BH at 5%:', supported)


if __name__ == '__main__':
    main()
