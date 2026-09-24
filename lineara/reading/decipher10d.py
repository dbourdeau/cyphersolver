"""Ten hypotheses building on the vowel deficits (decipher10c.py), the Knossos names, and the accounting signs.

Each has a prediction stated before the test ran, one primary test with its own null, and a Linear B control
where the method can run on the deciphered script. Benjamini-Hochberg at 5% runs across the ten.

B1  Rare vowels are lexically confined: e- and o-signs occur in fewer distinct Linear A words per occurrence than
    a-, i- and u-signs of similar frequency. Control: Linear B.
B2  e- and o-signs stand word-finally more often than a-, i- and u-signs (rare vowels live in endings).
B3  Linear A words containing e- or o-signs are attested at fewer sites than other words of the same frequency.
B4  A model trained on Knossos personal names against Knossos common words scores Linear A entry labels as more
    name-like than Linear A headings (an independent check that entry labels are personal names).
B5  The same model scores Linear A religious words as more name-like than administrative words that are not
    entry labels (deity or personal names in the religious texts).
B6  Single syllabic signs on tablets abbreviate words on the same tablet: they match a word's first sign more
    often than chance.
B7  Single syllabic signs on tablets are bound to particular commodities (mutual information above chance).
B8  Commodity ligatures continue from Linear A to Linear B: the two scripts share more (commodity, syllable)
    ligature pairs than chance.
B9  Knossos personal names begin with a pure vowel sign more often than Pylos names.
B10 Cretan place names in Linear B (attested only at Knossos) have fewer e- and o-syllables than place names
    attested only at Pylos.
"""
from collections import Counter, defaultdict
import json
from math import log
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
clean = lambda w: not any(x.startswith('*') for x in w)
KN_N = [w for w in V.kn_only if CAT.get(w) == 'anthroponym' and clean(w)]
PY_N = [w for w in V.py_only if CAT.get(w) == 'anthroponym' and clean(w)]
RARE, COMMON = {'e', 'o'}, {'a', 'i', 'u'}
FRACTION_LETTERS = {'A', 'B', 'D', 'E', 'F', 'H', 'J', 'K', 'L', 'L2', 'L3', 'L4', 'L6'}


def label_perm(stat, a, b, reps=REPS):
    real = stat(a, b)
    pool, k, null = a + b, len(a), []
    for _ in range(reps):
        rng.shuffle(pool)
        null.append(stat(pool[:k], pool[k:]))
    return real, B.pv(null, real), sum(null) / len(null)


# ------------------------------------------------------------------ B1, B2
def la_tokens():
    return [w for _, _, w in B.words_of() if not any(x in Db.LOGO for x in w)]


def lb_tokens():
    sites, count = B.N.lb_vocabulary()
    return [w for w, n in count.items() for _ in range(n) if clean(w)]


def sign_table(tokens):
    occ, types, final = Counter(), defaultdict(set), Counter()
    for w in tokens:
        for i, x in enumerate(w):
            if grid(x) and grid(x)[0]:
                occ[x] += 1
                types[x].add(w)
                final[x] += i == len(w) - 1
    return {s: (occ[s], len(types[s]), final[s]) for s in occ if occ[s] >= 10}


def resid(tab):
    xs = {s: log(o) for s, (o, t, f) in tab.items()}
    ys = {s: log(t) for s, (o, t, f) in tab.items()}
    n = len(xs)
    mx, my = sum(xs.values()) / n, sum(ys.values()) / n
    b = sum((xs[s] - mx) * (ys[s] - my) for s in xs) / sum((xs[s] - mx) ** 2 for s in xs)
    return {s: ys[s] - (my + b * (xs[s] - mx)) for s in xs}


def vowel_contrast(values, reps):
    signs = [s for s in values if grid(s)[1] in RARE | COMMON]
    lab = {s: grid(s)[1] in RARE for s in signs}

    def stat(lb):
        a = [values[s] for s in signs if lb[s]]
        b = [values[s] for s in signs if not lb[s]]
        return sum(a) / len(a) - sum(b) / len(b)
    real = stat(lab)
    labs = [lab[s] for s in signs]
    null = []
    for _ in range(reps):
        rng.shuffle(labs)
        null.append(stat(dict(zip(signs, labs))))
    return real, null


def B1():
    la = resid(sign_table(la_tokens()))
    real, null = vowel_contrast(la, REPS)
    p = (sum(n <= real for n in null) + 1) / (len(null) + 1)  # prediction: lower type diversity
    lb = resid(sign_table(lb_tokens()))
    lr, lnull = vowel_contrast(lb, REPS)
    record('B1 rare vowels lexically confined', 'e/o-signs occur in fewer distinct words per occurrence than a/i/u-signs',
           {'residual_diff (e/o minus a/i/u, negative = confined)': round(real, 3), 'p': round(p, 4)},
           {'Linear B control': {'diff': round(lr, 3), 'p_lower': round((sum(n <= lr for n in lnull) + 1) / (len(lnull) + 1), 4)},
            'most confined Linear A signs': sorted(((round(v, 2), s) for s, v in la.items()))[:8]})
    return p


def B2():
    tab = sign_table(la_tokens())
    fin = {s: f / o for s, (o, t, f) in tab.items()}
    real, null = vowel_contrast(fin, REPS)
    p = B.pv(null, real)
    ltab = sign_table(lb_tokens())
    lfin = {s: f / o for s, (o, t, f) in ltab.items()}
    lr, lnull = vowel_contrast(lfin, REPS)
    mean = lambda d, vs: round(sum(v for s, v in d.items() if grid(s)[1] in vs) / max(1, sum(1 for s in d if grid(s)[1] in vs)), 3)
    per_sign = {s_: round(v, 2) for s_, v in sorted(fin.items(), key=lambda kv: -kv[1]) if grid(s_)[1] in RARE}
    # leave out the five commonest word types, then re-test
    toks = la_tokens()
    top = {w for w, _ in Counter(toks).most_common(5)}
    tab2 = sign_table([w for w in toks if w not in top])
    fin2 = {s_: f / o for s_, (o, t, f) in tab2.items()}
    r2, n2 = vowel_contrast(fin2, REPS)
    # type-level (each word counted once)
    tab3 = sign_table(sorted(set(toks)))
    fin3 = {s_: f / o for s_, (o, t, f) in tab3.items()}
    r3, n3 = vowel_contrast(fin3, REPS)
    record('B2 rare vowels in endings', 'e/o-signs stand word-finally more often than a/i/u-signs',
           {'final_share e/o': mean(fin, RARE), 'final_share a/i/u': mean(fin, COMMON), 'p': round(p, 4)},
           {'Linear B control': {'e/o': mean(lfin, RARE), 'a/i/u': mean(lfin, COMMON), 'p': round(B.pv(lnull, lr), 4)},
            'five commonest words removed p': round(B.pv(n2, r2), 4), 'word types (each once) p': round(B.pv(n3, r3), 4),
            'final share per e/o sign': per_sign})
    return p


# ------------------------------------------------------------------ B3
def B3():
    toks = Counter(w for w in la_tokens())
    sites = defaultdict(set)
    for r, t, w in B.words_of():
        sites[w].add(r['site'])
    words = [w for w in toks if len(w) >= 2]
    has = {w: any(grid(x) and grid(x)[1] in RARE for x in w) for w in words}
    stratum = lambda n: 0 if n == 1 else 1 if n == 2 else 2 if n <= 4 else 3
    strata = defaultdict(list)
    for w in words:
        strata[stratum(toks[w])].append(w)

    def stat(lb):
        a = [len(sites[w]) for w in words if lb[w]]
        b = [len(sites[w]) for w in words if not lb[w]]
        return sum(a) / len(a) - sum(b) / len(b)
    real = stat(has)
    null = []
    for _ in range(REPS):
        lb = {}
        for ws in strata.values():
            labs = [has[w] for w in ws]
            rng.shuffle(labs)
            lb.update(zip(ws, labs))
        null.append(stat(lb))
    p = (sum(n <= real for n in null) + 1) / (len(null) + 1)
    record('B3 rare-vowel words are local', 'Words with e/o-signs are attested at fewer sites (frequency held fixed)',
           {'diff_in_mean_sites': round(real, 3), 'p': round(p, 4), 'words_with_e_o': sum(has.values()), 'words': len(words)},
           {'mean sites with e/o': round(sum(len(sites[w]) for w in words if has[w]) / sum(has.values()), 3),
            'mean sites without': round(sum(len(sites[w]) for w in words if not has[w]) / (len(words) - sum(has.values())), 3)})
    return p


# ------------------------------------------------------------------ B4, B5
def name_model():
    kn_c = [w for w in V.kn_only if CAT.get(w) == 'other' and clean(w)]
    mn, mc = V.nb_model(KN_N), V.nb_model(kn_c)
    return lambda w: sum(mn(s) - mc(s) for s in w) / len(w)


def la_functions():
    fn = defaultdict(Counter)
    for r, t, w in B.LA_ADMIN:
        fn[w][t.get('function')] += 1
    return {w: c.most_common(1)[0][0] for w, c in fn.items()}


def B4():
    score = name_model()
    fn = la_functions()
    ent = [w for w, f in fn.items() if f == 'entry label']
    head = [w for w, f in fn.items() if f == 'heading']
    stat = lambda a, b: V.auc([score(w) for w in a], [score(w) for w in b])
    real, p, nm = label_perm(stat, ent, head)
    # control: the same model at Pylos (names vs common words at Pylos) should agree
    py_c = [w for w in V.py_only if CAT.get(w) == 'other' and clean(w)]
    mn, mc = V.nb_model(PY_N), V.nb_model(py_c)
    sp = lambda w: sum(mn(s) - mc(s) for s in w) / len(w)
    alt = V.auc([sp(w) for w in ent], [sp(w) for w in head])
    record('B4 entry labels are name-like', 'A Knossos name model scores Linear A entry labels above headings',
           {'auc': round(real, 3), 'null_mean': round(nm, 3), 'p': round(p, 4), 'n': [len(ent), len(head)]},
           {'Pylos-trained model auc': round(alt, 3)})
    return p


def B5():
    score = name_model()
    fn = la_functions()
    names = set(B.LA_NAMES)
    rel = sorted({w for _, _, w in B.LA_RELIG} - set(fn))
    adm = [w for w, f in fn.items() if f != 'entry label' and w not in names]
    stat = lambda a, b: V.auc([score(w) for w in a], [score(w) for w in b])
    real, p, nm = label_perm(stat, rel, adm)
    rel_nf = [w for w in rel if not V.FORMULA.search('-'.join(w).upper())]
    r2, p2, _ = label_perm(stat, rel_nf, adm)
    record('B5 religious words are name-like', 'A Knossos name model scores Linear A religious words above non-label administrative words',
           {'auc': round(real, 3), 'null_mean': round(nm, 3), 'p': round(p, 4), 'n': [len(rel), len(adm)]},
           {'formula words removed': {'auc': round(r2, 3), 'p': round(p2, 4)}})
    return p


# ------------------------------------------------------------------ B6, B7
def single_items():
    items = []
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        words = [tuple(x.lower() for x in t['label'].split('-')) for t in r['tokens'] if t['cls'] in ('word', 'term')]
        com = {re.findall(r'[A-Z]{3,}', t['label'])[0] for t in r['tokens'] if t['cls'] == 'commodity' and re.findall(r'[A-Z]{3,}', t['label'])}
        for t in r['tokens']:
            if t['cls'] == 'single-sign' and re.fullmatch(r'[A-Z]{1,2}[0-9]?', t['label']):
                items.append((t['label'].lower(), words, com, r['name']))
    return items


def B6():
    items = single_items()
    first = lambda s, ws: any(w and w[0] == s for w in ws)
    later = lambda s, ws: any(s in w[1:] for w in ws)
    real = sum(first(s, ws) for s, ws, _, _ in items)
    syl = [s for s, _, _, _ in items]
    null, null_l = [], []
    real_l = sum(later(s, ws) for s, ws, _, _ in items)
    for _ in range(REPS):
        rng.shuffle(syl)
        null.append(sum(first(s, ws) for s, (_, ws, _, _) in zip(syl, items)))
        null_l.append(sum(later(s, ws) for s, (_, ws, _, _) in zip(syl, items)))
    p = B.pv(null, real)
    ex = Counter((s.upper(), '-'.join(w).upper()) for s, ws, _, _ in items for w in ws if w and w[0] == s)
    record('B6 single signs as abbreviations', 'Single signs on tablets match the first sign of a word on the same tablet',
           {'matches': f'{real}/{len(items)}', 'null_mean': round(sum(null) / len(null), 2), 'p': round(p, 4)},
           {'non-initial position': {'real': real_l, 'null_mean': round(sum(null_l) / len(null_l), 2), 'p': round(B.pv(null_l, real_l), 4)},
            'examples': [f'{a}: {b} x{n}' for (a, b), n in ex.most_common(12)]})
    return p


def mi(pairs):
    n = len(pairs)
    a, b, ab = Counter(x for x, _ in pairs), Counter(y for _, y in pairs), Counter(pairs)
    return sum(c / n * log(c * n / (a[x] * b[y])) for (x, y), c in ab.items())


def B7():
    items = [(s, com, rec) for s, _, com, rec in single_items() if com]
    pairs = lambda its: [(s, c) for s, com, _ in its for c in com]
    real = mi(pairs(items))
    recs = sorted({rec for _, _, rec in items})
    com_of = {rec: com for _, com, rec in items}
    null = []
    for _ in range(REPS):
        coms = [com_of[r] for r in recs]
        rng.shuffle(coms)
        m = dict(zip(recs, coms))
        null.append(mi([(s, c) for s, _, rec in items for c in m[rec]]))
    p = B.pv(null, real)
    tab = Counter((s.upper(), c) for s, com, _ in items for c in com)
    record('B7 single signs bound to commodities', 'Single signs co-occur with particular commodities beyond chance',
           {'mi': round(real, 4), 'null_mean': round(sum(null) / len(null), 4), 'p': round(p, 4), 'tokens': len(items), 'tablets': len(recs)},
           {'commonest pairs': [f'{a}+{b} x{n}' for (a, b), n in tab.most_common(15)]})
    return p


# ------------------------------------------------------------------ B8
def base_of(label):
    b = label.split('+')[0].split(';')[0].lstrip('*')
    b = re.sub(r'[a-z]+$', '', b)
    return {'CAPm': 'CAP', 'CAPf': 'CAP'}.get(b, b)


def B8():
    la = set()
    for r in B.READ['records']:
        for t in r['tokens']:
            if t['cls'] == 'commodity' and '+' in t['label']:
                lab = t['label'].split('-')[-1]
                parts = lab.split('+')
                for syl in parts[1:]:
                    if syl not in FRACTION_LETTERS and re.fullmatch(r'[A-Z]{1,2}[0-9]?', syl):
                        la.add((base_of(parts[0]), syl))
    lb_items = []
    for _, r in B.LB_RECS:
        for t in r.get('transliteratedWords', []):
            if '+' in t and re.match(r'^[A-Z*]', t):
                parts = t.split('+')
                syl = parts[-1]
                if re.fullmatch(r'[A-Z]{1,2}[0-9]?', syl):
                    lb_items.append((base_of(parts[0]), syl))
    lb = set(lb_items)
    real = len(la & lb)
    bases = [b for b, _ in sorted(lb)]
    syls = [s for _, s in sorted(lb)]
    null = []
    for _ in range(REPS):
        rng.shuffle(syls)
        null.append(len(la & set(zip(bases, syls))))
    p = B.pv(null, real)
    record('B8 ligature continuity', 'Linear A and Linear B share more (commodity, syllable) ligatures than chance',
           {'shared': real, 'null_mean': round(sum(null) / len(null), 2), 'p': round(p, 4), 'LA_pairs': len(la), 'LB_pairs': len(lb)},
           {'shared pairs': sorted(f'{a}+{b}' for a, b in la & lb), 'LA pairs': sorted(f'{a}+{b}' for a, b in la)})
    return p


# ------------------------------------------------------------------ B9, B10
def vowel_initial(ws):
    return sum(1 for w in ws if grid(w[0]) and grid(w[0])[0] == '') / len(ws)


def B9():
    stat = lambda a, b: vowel_initial(a) - vowel_initial(b)
    real, p, nm = label_perm(stat, KN_N, PY_N)
    kn_c = [w for w in V.kn_only if CAT.get(w) == 'other' and clean(w) and len(w) >= 2]
    py_c = [w for w in V.py_only if CAT.get(w) == 'other' and clean(w) and len(w) >= 2]
    r2, p2, _ = label_perm(stat, kn_c, py_c)
    record('B9 vowel-initial names', 'Knossos names begin with a pure vowel more often than Pylos names',
           {'KN': round(vowel_initial(KN_N), 4), 'PY': round(vowel_initial(PY_N), 4), 'p': round(p, 4)},
           {'Linear A words': round(vowel_initial(B.LA_TYPES), 4), 'Linear A names': round(vowel_initial(B.LA_NAMES), 4),
            'control common words': {'KN': round(vowel_initial(kn_c), 4), 'PY': round(vowel_initial(py_c), 4), 'p': round(p2, 4)}})
    return p


def eo_share(ws):
    s = [x for w in ws for x in w if grid(x)]
    return sum(grid(x)[1] in RARE for x in s) / len(s)


def B10():
    kn_t = [w for w in V.kn_only if CAT.get(w) in ('toponym', 'ethnic') and clean(w)]
    py_t = [w for w in V.py_only if CAT.get(w) in ('toponym', 'ethnic') and clean(w)]
    strip = lambda ws: [w[:-1] for w in ws if len(w) >= 3]
    stat = lambda a, b: eo_share(strip(b)) - eo_share(strip(a))
    real, p, nm = label_perm(stat, kn_t, py_t)
    r_all, p_all, _ = label_perm(lambda a, b: eo_share(b) - eo_share(a), kn_t, py_t)
    kn_c = [w for w in V.kn_only if CAT.get(w) == 'other' and clean(w)]
    py_c = [w for w in V.py_only if CAT.get(w) == 'other' and clean(w)]
    rc, pc, _ = label_perm(stat, kn_c, py_c)
    main_t = [w for w, s_ in B.LB_SITES.items() if s_ and s_ <= Db.__dict__.get('MAIN', {'Thebes', 'Mycenae', 'Tiryns'}) | {'Thebes', 'Mycenae', 'Tiryns'}
              and CAT.get(w) in ('toponym', 'ethnic') and clean(w)]
    rm, pm, _ = label_perm(stat, kn_t, main_t)
    record('B10 Cretan place names', 'Knossos-only place names and ethnics have fewer e/o-syllables (ending removed) than Pylos-only ones',
           {'KN': round(eo_share(strip(kn_t)), 4), 'PY': round(eo_share(strip(py_t)), 4), 'p': round(p, 4), 'n': [len(kn_t), len(py_t)]},
           {'whole words': {'KN': round(eo_share(kn_t), 4), 'PY': round(eo_share(py_t), 4), 'p': round(p_all, 4)},
            'Linear A all words': round(eo_share(B.LA_TYPES), 4),
            'control common words (ending removed)': {'KN': round(eo_share(strip(kn_c)), 4), 'PY': round(eo_share(strip(py_c)), 4), 'p': round(pc, 4)},
            'against Thebes/Mycenae/Tiryns place names': {'other': round(eo_share(strip(main_t)), 4), 'p': round(pm, 4), 'n': len(main_t)}})
    return p


def main():
    ps = {}
    for fn in (B1, B2, B3, B4, B5, B6, B7, B8, B9, B10):
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
    (ROOT / 'reading/decipher10d_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str) + '\n', encoding='utf-8')
    print('\nprimary p:', {k: round(v, 4) for k, v in ps.items()})
    print('survive BH at 5%:', supported)


if __name__ == '__main__':
    main()
