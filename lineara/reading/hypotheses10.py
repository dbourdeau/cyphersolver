"""Ten further hypotheses on Linear A, each tested on data already in the repository against a null.

H1  Vowel harmony: adjacent syllables within a Linear A word share their vowel more often than chance.
H2  Initial a-: Linear A words begin with the bare vowel A more often than Linear B words do; and Knossos
    personal names more often than Pylos personal names.
H3  O deficit: Linear A uses o-syllables less than Linear B; Knossos names sit between Linear A and Pylos names.
H4  Script adaptation: Linear A syllabograms that Linear B did not keep were rarer in Linear A words than the
    ones it kept.
H5  Which syllables make Knossos names look Minoan: final and first syllables over-represented in Knossos names
    relative to Pylos names, and also frequent in Linear A names (per-syllable tests, Benjamini-Hochberg).
H6  Where the Minoan-looking names are at Knossos: a Linear A-likeness score per Knossos name (log-likelihood
    ratio of Linear A name syllables against Pylos name syllables) differs between Linear B tablet series.
H7  The libation formula's prefix (JA-, A-, none) depends on the site.
H8  Commodity specialisation: names recurring on several tablets keep the same commodity more than chance.
H9  Transaction words (SA-RA2, A-DU, KA-PA, KI-RO, KU-RO) go with particular commodities more than chance.
H10 Endings and commodities: a word's final sign depends on the commodity of its entry, within the same stem
    family, beyond chance (agreement-like morphology).

Every test is a permutation test unless stated; the null is named in each result.
"""
from collections import Counter, defaultdict
import json
from math import log
from pathlib import Path
import random
import re
import sys
import unicodedata as ud

sys.path.insert(0, str(Path(__file__).resolve().parent))
import names_lb as N  # noqa: E402
import name_shapes as S  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
READ = json.loads((ROOT / 'reading/reading.json').read_text(encoding='utf-8'))
ADMIN = {'Tablet', 'Lames (short thin tablet)', '3-sided bar', '4-sided bar', 'Label'}
REPS = 5000


def vowel(s):
    m = re.search(r'([aeiou])[0-9]?$', s)
    return m.group(1) if m else None


def p_ge(null, real):
    return round((sum(n >= real for n in null) + 1) / (len(null) + 1), 4)


def la_word_types():
    out = set()
    for r in READ['records']:
        for t in r['tokens']:
            if t['cls'] == 'word':
                w = tuple(t['label'].lower().split('-'))
                if len(w) >= 2 and all(re.match(r'^[a-z]+[0-9]?$', s) for s in w):
                    out.add(w)
    return sorted(out)


def lb_types():
    sites, _ = N.lb_vocabulary()
    return sorted(w for w in sites if len(w) >= 2 and not any(x.startswith('*') for x in w)), sites


def h1(rng, la, lb):
    def rate(ws):
        pairs = [(vowel(a), vowel(b)) for w in ws for a, b in zip(w, w[1:])]
        pairs = [p for p in pairs if None not in p]
        return sum(a == b for a, b in pairs) / len(pairs)
    out = {}
    for name, ws in (('Linear A', la), ('Linear B', lb)):
        real = rate(ws)
        pool = [s for w in ws for s in w]
        lens = [len(w) for w in ws]
        null = []
        for _ in range(1000):
            rng.shuffle(pool)
            k, sh = 0, []
            for L in lens:
                sh.append(tuple(pool[k:k + L]))
                k += L
            null.append(rate(sh))
        out[name] = {'same_vowel_rate': round(real, 4), 'null_mean': round(sum(null) / len(null), 4), 'p_ge': p_ge(null, real)}
    return out


def two_prop_perm(a, b, rng, reps=REPS):
    """p that group a has a higher share of True than group b, by label permutation."""
    real = sum(a) / len(a) - sum(b) / len(b)
    pool, k = list(a) + list(b), len(a)
    null = []
    for _ in range(reps):
        rng.shuffle(pool)
        null.append(sum(pool[:k]) / k - sum(pool[k:]) / (len(pool) - k))
    return round(real, 4), p_ge(null, real)


def h2(rng, la, lb, kn, py):
    d1, p1 = two_prop_perm([w[0] == 'a' for w in la], [w[0] == 'a' for w in lb], rng)
    d2, p2 = two_prop_perm([w[0] == 'a' for w in kn], [w[0] == 'a' for w in py], rng)
    return {'Linear A vs Linear B': {'share_la': round(sum(w[0] == 'a' for w in la) / len(la), 3),
                                     'share_lb': round(sum(w[0] == 'a' for w in lb) / len(lb), 3), 'diff': d1, 'p': p1},
            'Knossos vs Pylos names': {'share_kn': round(sum(w[0] == 'a' for w in kn) / len(kn), 3),
                                       'share_py': round(sum(w[0] == 'a' for w in py) / len(py), 3), 'diff': d2, 'p': p2}}


def h3(rng, la, lb, kn, py):
    share = lambda ws: sum(vowel(s) == 'o' for w in ws for s in w) / sum(len(w) for w in ws)
    flat = lambda ws: [vowel(s) == 'o' for w in ws for s in w]
    d1, p1 = two_prop_perm(flat(lb), flat(la), rng, 2000)
    d2, p2 = two_prop_perm(flat(py), flat(kn), rng, 2000)
    return {'o_share': {'Linear A': round(share(la), 3), 'Knossos names': round(share(kn), 3),
                        'Pylos names': round(share(py), 3), 'Linear B all': round(share(lb), 3)},
            'Linear B exceeds Linear A': {'diff': d1, 'p': p1}, 'Pylos names exceed Knossos names': {'diff': d2, 'p': p2}}


def h4(rng):
    rows = json.loads((ROOT / 'data/corpus.json').read_text(encoding='utf-8'))
    freq = Counter()
    for r in rows:
        for w in r['words']:
            ids = []
            for c in w:
                m = re.fullmatch(r'LINEAR A SIGN (AB|A)(\d+)([A-Z]*)', ud.name(c, ''))
                if m and int(m[2]) < 100 or (m and m[1] == 'A' and 300 <= int(m[2]) < 400):
                    ids.append(m[1] + m[2])
            if len(ids) >= 2:
                freq.update(ids)
    kept = [n for s, n in freq.items() if s.startswith('AB')]
    dropped = [n for s, n in freq.items() if s.startswith('A') and not s.startswith('AB')]
    med = lambda x: sorted(x)[len(x) // 2]
    real = sum(kept) / len(kept) - sum(dropped) / len(dropped)
    pool, k = kept + dropped, len(kept)
    null = []
    for _ in range(REPS):
        rng.shuffle(pool)
        null.append(sum(pool[:k]) / k - sum(pool[k:]) / (len(pool) - k))
    return {'kept_signs': len(kept), 'dropped_signs': len(dropped), 'median_freq_kept': med(kept),
            'median_freq_dropped': med(dropped), 'mean_diff': round(real, 2), 'p': p_ge(null, real)}


def h5(rng, la, kn, py):
    out = {}
    for part, idx in (('last', -1), ('first', 0)):
        cla, ckn, cpy = Counter(w[idx] for w in la), Counter(w[idx] for w in kn), Counter(w[idx] for w in py)
        tests = []
        labels = [0] * len(kn) + [1] * len(py)
        vals = [w[idx] for w in kn] + [w[idx] for w in py]
        for s in set(ckn) | set(cpy):
            if ckn[s] + cpy[s] < 8:
                continue
            real = ckn[s] / len(kn) - cpy[s] / len(py)
            null = []
            lab = labels[:]
            for _ in range(2000):
                rng.shuffle(lab)
                a = sum(1 for l, v in zip(lab, vals) if l == 0 and v == s)
                b = sum(1 for l, v in zip(lab, vals) if l == 1 and v == s)
                null.append(a / len(kn) - b / len(py))
            tests.append({'syllable': s, 'kn_share': round(ckn[s] / len(kn), 3), 'py_share': round(cpy[s] / len(py), 3),
                          'la_share': round(cla[s] / len(la), 3), 'p': p_ge(null, real)})
        tests.sort(key=lambda t: t['p'])
        m = len(tests)
        for i, t in enumerate(tests):
            t['bh_significant'] = t['p'] <= 0.05 * (i + 1) / m
        out[part] = [t for t in tests if t['bh_significant']] or tests[:5]
    return out


def lb_series():
    series = defaultdict(list)
    for name, rec in N.load_js_map(ROOT / 'data/linearb/LinearBInscriptions.js'):
        if rec.get('site') != 'Knossos':
            continue
        m = re.match(r'KN\s+([A-Z][a-z]?)', rec.get('label', ''))
        if not m:
            continue
        for t in rec.get('transliteratedWords', []):
            t = t.strip().lower()
            parts = tuple(t.split('-'))
            if len(parts) >= 2:
                series[parts].append(m.group(1)[0])  # major series letter
    return series


def h6(rng, la, kn, py):
    pla, ppy = S.profile(la, 'all'), S.profile(py, 'all')
    eps = 1e-3
    score = lambda w: sum(log((pla.get(s, 0) + eps) / (ppy.get(s, 0) + eps)) for s in w) / len(w)
    ser = lb_series()
    rows = [(Counter(ser[w]).most_common(1)[0][0], score(w)) for w in kn if w in ser]
    by = defaultdict(list)
    for s, v in rows:
        by[s].append(v)
    by = {s: v for s, v in by.items() if len(v) >= 15}
    grand = sum(v for s, vs in by.items() for v in vs) / sum(len(vs) for vs in by.values())
    stat = lambda groups: sum(len(v) * (sum(v) / len(v) - grand) ** 2 for v in groups.values())
    real = stat(by)
    pool = [v for vs in by.values() for v in vs]
    sizes = {s: len(v) for s, v in by.items()}
    null = []
    for _ in range(2000):
        rng.shuffle(pool)
        k, g = 0, {}
        for s, n in sizes.items():
            g[s] = pool[k:k + n]
            k += n
        null.append(stat(g))
    means = {s: round(sum(v) / len(v), 3) for s, v in sorted(by.items(), key=lambda x: -sum(x[1]) / len(x[1]))}
    return {'names_scored': len(rows), 'series_mean_score (higher = more Linear A-like)': means,
            'series_sizes': sizes, 'p_series_differ': p_ge(null, real)}


def h7(rng):
    f = json.loads((ROOT / 'reading/formula_results.json').read_text(encoding='utf-8'))
    obs = []
    for q in f['sequences']:
        for w in q['words']:
            m = re.match(r'^(JA-|A-)?(SA-SA-RA|DI-KI-T|U-NA-)', w)
            if m:
                obs.append((q['site'], {'JA-': 'JA', 'A-': 'A', None: 'none'}[m.group(1)]))
    sites = [s for s, _ in obs]
    pref = [p for _, p in obs]

    def chi(ss, pp):
        ct = Counter(zip(ss, pp))
        rs, cs, n = Counter(ss), Counter(pp), len(ss)
        return sum((ct.get((r, c), 0) - rs[r] * cs[c] / n) ** 2 / (rs[r] * cs[c] / n) for r in rs for c in cs)
    real = chi(sites, pref)
    null = []
    for _ in range(REPS):
        rng.shuffle(pref)
        null.append(chi(sites, pref))
    return {'observations': Counter(f'{s}:{p}' for s, p in obs), 'chi2': round(real, 2), 'p': p_ge(null, real)}


def entry_commodities():
    """(record, word, function, commodity of its entry or of the record) for administrative words."""
    out = []
    for r in READ['records']:
        if r['support'] not in ADMIN:
            continue
        rec_com = [re.findall(r'[A-Z]{3,}', t['label'])[0] for t in r['tokens'] if t['cls'] == 'commodity']
        by = defaultdict(list)
        for t in r['tokens']:
            by[t['entry']].append(t)
        for e, ts in by.items():
            com = [re.findall(r'[A-Z]{3,}', t['label'])[0] for t in ts if t['cls'] == 'commodity']
            c = com[0] if com else (rec_com[0] if rec_com else None)
            for t in ts:
                if t['cls'] in ('word', 'term') and c:
                    out.append((r['name'], t['label'], t.get('function', t['cls']), c))
    return out


def h8(rng):
    ec = [x for x in entry_commodities() if x[2] == 'entry label']
    by = defaultdict(list)
    for rec, w, f, c in ec:
        by[w].append((rec, c))
    rec_words = [(w, v) for w, v in by.items() if len({r for r, _ in v}) >= 2]
    def same(groups):
        return sum(1 for v in groups if len({c for _, c in v}) == 1)
    real = same([v for _, v in rec_words])
    allc = [c for _, _, _, c in ec]
    null = []
    for _ in range(REPS):
        sh = [[(r, rng.choice(allc)) for r, _ in v] for _, v in rec_words]
        null.append(same(sh))
    return {'recurring_names': len(rec_words), 'same_commodity_every_time': real,
            'null_mean': round(sum(null) / len(null), 2), 'p': p_ge(null, real)}


def h9(rng):
    ec = entry_commodities()
    terms = {'SA-RA2', 'A-DU', 'KA-PA', 'KI-RO', 'KU-RO'}
    rows = [(w, c) for _, w, _, c in ec if w in terms]
    ws, cs = [w for w, _ in rows], [c for _, c in rows]

    def chi(a, b):
        ct = Counter(zip(a, b))
        rs, cc, n = Counter(a), Counter(b), len(a)
        return sum((ct.get((r, c), 0) - rs[r] * cc[c] / n) ** 2 / (rs[r] * cc[c] / n) for r in rs for c in cc)
    real = chi(ws, cs)
    # null: commodities drawn from all administrative words, so terms are compared with the general mix
    allc = [c for _, _, _, c in ec]
    null = [chi(ws, [rng.choice(allc) for _ in ws]) for _ in range(REPS)]
    table = {w: dict(Counter(c for x, c in rows if x == w)) for w in terms}
    return {'occurrences': len(rows), 'table': table, 'chi2': round(real, 2), 'p': p_ge(null, real)}


def h10(rng):
    ec = [x for x in entry_commodities() if x[2] == 'entry label' and '-' in x[1]]
    fam = defaultdict(list)
    for rec, w, f, c in ec:
        s = w.split('-')
        if len(s) >= 3:
            fam['-'.join(s[:-1])].append((s[-1], c))
    fam = {k: v for k, v in fam.items() if len({e for e, _ in v}) >= 2 and len({c for _, c in v}) >= 2}

    def cmi(groups):
        tot = 0.0
        for v in groups.values():
            n = len(v)
            ce, cc, cec = Counter(e for e, _ in v), Counter(c for _, c in v), Counter(v)
            tot += sum(k * log(k * n / (ce[e] * cc[c])) for (e, c), k in cec.items())
        return tot
    real = cmi(fam)
    null = []
    for _ in range(REPS):
        sh = {}
        for k, v in fam.items():
            cs = [c for _, c in v]
            rng.shuffle(cs)
            sh[k] = [(e, c) for (e, _), c in zip(v, cs)]
        null.append(cmi(sh))
    return {'families': len(fam), 'tokens': sum(len(v) for v in fam.values()), 'cmi': round(real, 3),
            'null_mean': round(sum(null) / len(null), 3), 'p': p_ge(null, real)}


def main(seed=20260923):
    rng = random.Random(seed)
    la = la_word_types()
    lb, _ = lb_types()
    la_names = S.la_names()
    kn, py, _ = S.lb_groups('anthroponym')
    res = {'method': __doc__.strip()}
    res['H1 vowel harmony'] = h1(rng, la, lb)
    res['H2 initial a-'] = h2(rng, la, lb, kn, py)
    res['H3 o deficit'] = h3(rng, la, lb, kn, py)
    res['H4 dropped signs rarer'] = h4(rng)
    res['H5 syllables driving Knossos likeness'] = h5(rng, la_names, kn, py)
    res['H6 Knossos series'] = h6(rng, la_names, kn, py)
    res['H7 formula prefix by site'] = h7(rng)
    res['H8 commodity specialisation'] = h8(rng)
    res['H9 transaction words and commodities'] = h9(rng)
    res['H10 endings and commodities'] = h10(rng)
    (ROOT / 'reading/hypotheses10_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str) + '\n',
                                                           encoding='utf-8')
    for k, v in res.items():
        if k != 'method':
            print('==', k)
            print('  ', json.dumps(v, ensure_ascii=False, default=str)[:900])


if __name__ == '__main__':
    main()
