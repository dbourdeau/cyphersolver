"""Twenty-five further hypotheses in five batches, following up the strongest leads of batches.py.

Same conventions: a null for each test, one-sided p-values, and Benjamini-Hochberg at a 5% false-discovery rate
across the twenty-five. Helpers and data come from batches.py.
"""
from collections import Counter, defaultdict
import json
from math import log
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import batches as B  # noqa: E402

ROOT = B.ROOT
rng = B.rng
LA_SET = set(B.LA_TYPES)
LB = B.LB_SITES
CAT = B.LB_CAT
kn_only = [w for w, s in LB.items() if s == {'Knossos'}]
py_only = [w for w, s in LB.items() if s == {'Pylos'}]


# ---------- K: the Knossos trace
def K1():
    star = lambda w: any(x.startswith('*') for x in w)
    names = [int(CAT.get(w) == 'anthroponym') for w in kn_only if star(w)]
    base = [int(CAT.get(w) == 'anthroponym') for w in kn_only if not star(w)]
    e, p = B.diff_means(names, base)
    return 'At Knossos, words with undeciphered signs are more often personal names', e, p, f'{sum(names)}/{len(names)} vs {sum(base)}/{len(base)}'


def K2():
    both = [B.la_score(w) for w, s in LB.items() if {'Knossos', 'Pylos'} <= s and len(w) >= 2 and not any(x.startswith('*') for x in w)]
    kn = [B.la_score(w) for w in kn_only if len(w) >= 2 and not any(x.startswith('*') for x in w)]
    e, p = B.diff_means(kn, both)
    return 'Knossos-only words are more Linear A-like than words shared by Knossos and Pylos', e, p, f'{len(kn)} vs {len(both)}'


def K3():
    names = [w for w in kn_only if CAT.get(w) == 'anthroponym']
    other = [w for w in kn_only if CAT.get(w) not in ('anthroponym', 'toponym', 'ethnic', 'theonym') and w in CAT]
    la = Counter(s for w in B.LA_TYPES for s in w)
    common = lambda ws: [s for s in la if s in Counter(x for w in ws for x in w)]
    def rho(ws):
        c = Counter(x for w in ws for x in w)
        cs = [s for s in la if s in c]
        return B.spearman([la[s] for s in cs], [c[s] for s in cs])
    real = rho(names) - rho(other)
    null = []
    pool, k = names + other, len(names)
    for _ in range(500):
        rng.shuffle(pool)
        null.append(rho(pool[:k]) - rho(pool[k:]))
    return 'At Knossos, names follow Linear A syllable rates more closely than common words', round(real, 3), B.pv(null, real), f'{len(names)} names, {len(other)} common words'


def K4():
    mainland_topo = [w for w, s in LB.items() if CAT.get(w) == 'toponym' and not s & {'Knossos', 'Khania'}]
    crete_topo = [w for w, s in LB.items() if CAT.get(w) == 'toponym' and s <= {'Knossos', 'Khania', 'Vases - Khania'}]
    e, p = B.diff_means([B.la_score(w) for w in crete_topo], [B.la_score(w) for w in mainland_topo])
    return 'Cretan place names in Linear B are more Linear A-like than mainland place names', e, p, f'{len(crete_topo)} vs {len(mainland_topo)}'


def K5():
    eth = [w for w in kn_only if len(w) >= 3 and w[-1] in ('jo', 'ja')]
    stem_hit = lambda ws, la: sum(1 for w in ws if w[:-1] in la or (w[-2] == 'i' and w[:-2] in la)) / len(ws)
    real = stem_hit(eth, LA_SET)
    null = []
    words = list(LA_SET)
    freq = Counter(s for w in words for s in w)
    signs = sorted(freq, key=lambda s: -freq[s])
    size = -(-len(signs) // 10)
    bins = [signs[i:i + size] for i in range(0, len(signs), size)]
    for _ in range(1000):
        mp = {}
        for b in bins:
            v = b[:]
            rng.shuffle(v)
            mp.update(zip(b, v))
        null.append(stem_hit(eth, {tuple(mp[s] for s in w) for w in words}))
    return 'Knossos adjectives in -jo/-ja are built on Linear A words (stem + suffix)', round(real, 4), B.pv(null, real), f'{len(eth)} -jo/-ja words'


# ---------- L: bookkeeping follow-ups
def L1():
    res = {}
    for label, pred in (('Haghia Triada', lambda r: r['site'] == 'Haghia Triada'), ('other sites', lambda r: r['site'] != 'Haghia Triada')):
        lists = []
        for r in B.READ['records']:
            if r['support'] not in B.ADMIN or not pred(r):
                continue
            seq = []
            for t in r['tokens']:
                if t['cls'] == 'number':
                    seq.append(t['value'])
                elif t['label'] in ('KU-RO', 'KI-RO', 'PO-TO-KU-RO', '—'):
                    if len(seq) >= 4:
                        lists.append(seq)
                    seq = []
            if len(seq) >= 4:
                lists.append(seq)
        res[label] = lists
    def tau(v):
        c = d = 0
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                c += v[i] > v[j]
                d += v[i] < v[j]
        return (c - d) / max(1, c + d)
    lists = res['other sites']
    real = sum(map(tau, lists)) / len(lists)
    null = []
    for _ in range(B.REPS):
        tot = 0
        for v in lists:
            w = v[:]
            rng.shuffle(w)
            tot += tau(w)
        null.append(tot / len(lists))
    return 'Largest-first listing holds outside Haghia Triada too', round(real, 3), B.pv(null, real), f'{len(lists)} non-HT lists'


def L2():
    ent = B.entries_with(lambda ts: True)
    g = [int(x['q'] % 2 == 0) for x in ent if x['com'] == 'GRA' and x['q'] >= 2 and x['q'] % 5]
    v = [int(x['q'] % 2 == 0) for x in ent if x['com'] == 'VIR' and x['q'] >= 2 and x['q'] % 5]
    e, p = B.diff_means(g, v)
    return 'The even-amount preference is stronger for grain than for men', e, p, f'GRA {sum(g)}/{len(g)}, VIR {sum(v)}/{len(v)}'


def L3():
    recs = defaultdict(list)
    for x in B.entries_with(lambda ts: True):
        recs[x['record']].append(x['q'])
    def pairs2(lists):
        return sum(1 for q in lists for i in range(len(q)) for j in range(len(q)) if i != j and q[i] == 2 * q[j] and q[j] > 1)
    lists = [q for q in recs.values() if len(q) >= 3]
    real = pairs2(lists)
    allq = [x for q in lists for x in q]
    null = []
    for _ in range(B.REPS):
        pool = allq[:]
        rng.shuffle(pool)
        k, sh = 0, []
        for q in lists:
            sh.append(pool[k:k + len(q)])
            k += len(q)
        null.append(pairs2(sh))
    return 'Amounts on the same tablet are doubles of each other more than chance', real, B.pv(null, real), f'null mean {round(sum(null)/len(null),1)}'


def L4():
    ent = B.entries_with(lambda ts: True)
    a = [int(x['q'] == 1) for x in ent if x['section'] == 'KI-RO']
    b = [int(x['q'] == 1) for x in ent if x['section'] != 'KI-RO']
    e, p = B.diff_means(a, b)
    return 'KI-RO entries are mostly single units (1)', e, p, f'{sum(a)}/{len(a)} vs {sum(b)}/{len(b)}'


def L5():
    ft = B.frac_tokens()
    liq = [int(bool(fs)) for r, c, fs in ft if c in ('VIN', 'OLE')]
    dry = [int(bool(fs)) for r, c, fs in ft if c in ('GRA', 'OLIV', 'CYP')]
    e, p = B.diff_means(liq, dry)
    return 'Liquids (wine, oil) take fractions more often than dry goods', e, p, f'liquid {sum(liq)}/{len(liq)}, dry {sum(dry)}/{len(dry)}'


# ---------- M: word structure
def admin_by_function(fn):
    return [w for r, t, w in B.LA_ADMIN if t.get('function') == fn]


def M1():
    ent, head = admin_by_function('entry label'), admin_by_function('heading')
    e, p = B.diff_means([int(w[-1] == 'ti') for w in ent], [int(w[-1] == 'ti') for w in head])
    return 'Words ending -TI are entry labels (names) rather than headings', e, p, ''


def M2():
    ent, head = admin_by_function('entry label'), admin_by_function('heading')
    e, p = B.diff_means([int(w[0] == 'a') for w in head], [int(w[0] == 'a') for w in ent])
    return 'Words beginning A- are headings rather than entry labels', e, p, f'{sum(w[0]=="a" for w in head)}/{len(head)} vs {sum(w[0]=="a" for w in ent)}/{len(ent)}'


def M3():
    e, p = B.diff_means([int(w[-1] == 'ja') for _, _, w in B.LA_RELIG], [int(w[-1] == 'ja') for _, _, w in B.LA_ADMIN])
    return 'Words ending -JA belong to the religious register', e, p, ''


def M4():
    ws = [w for w in B.LA_TYPES if len(w) >= 3 and B.vowel(w[0]) and B.vowel(w[-1])]
    real = sum(B.vowel(w[0]) == B.vowel(w[-1]) for w in ws) / len(ws)
    firsts = [B.vowel(w[0]) for w in ws]
    lasts = [B.vowel(w[-1]) for w in ws]
    null = []
    for _ in range(B.REPS):
        rng.shuffle(lasts)
        null.append(sum(a == b for a, b in zip(firsts, lasts)) / len(ws))
    return 'The first and last syllables of a word share their vowel more than chance', round(real, 3), B.pv(null, real), ''


def M5():
    short = {w for w in B.LA_TYPES if len(w) == 2}
    longw = [w for w in B.LA_TYPES if len(w) >= 4]
    comp = lambda ws, sh: sum(1 for w in ws if any(w[:i] in sh and (w[i:] in sh or w[i:] in LA_SET) for i in range(2, len(w) - 1))) / len(ws)
    real = comp(longw, short)
    null = []
    for _ in range(500):
        sh = B.pooled_shuffle(sorted(short))
        null.append(comp(longw, set(sh)))
    return 'Long words are compounds of attested shorter words more than chance', round(real, 3), B.pv(null, real), f'{len(longw)} long words'


# ---------- N: sealings and documents
def seal_signs(kind):
    return [t['label'].lower() for r in B.READ['records'] if r['support'] == kind for t in r['tokens'] if t['cls'] == 'single-sign']


def N1():
    rou, nod = seal_signs('Roundel'), seal_signs('Nodule')
    e, p = B.chi2_perm(['R'] * len(rou) + ['N'] * len(nod), rou + nod)
    return 'Roundels and nodules carry different signs', e, p, f'{len(rou)} roundel, {len(nod)} nodule signs'


def N2():
    seal = B.seal_signs if hasattr(B, 'seal_signs') else None
    s = seal_signs('Roundel') + seal_signs('Nodule')
    top = [w for w, _ in Counter(w for _, _, w in B.LA_ADMIN).most_common(20)]
    heads = {w[0] for w in top}
    real = sum(x in heads for x in s) / len(s)
    allsig = [x for w in B.LA_TYPES for x in w]
    null = []
    for _ in range(B.REPS):
        rs = set(rng.sample(sorted(set(allsig)), len(heads)))
        null.append(sum(x in rs for x in s) / len(s))
    return 'Sealing signs are the first signs of the commonest administrative words', round(real, 3), B.pv(null, real), f'heads {sorted(heads)}'


def N3():
    rel = [r for r in B.READ['records'] if r['support'] not in B.ADMIN | B.SEAL]
    adm = [r for r in B.READ['records'] if r['support'] in B.ADMIN]
    rate = lambda rs: [sum(1 for t in r['tokens'] if t['glyphs'] == '\U00010101' if 'glyphs' in t) for r in rs]
    div = lambda r: sum(1 for t in r['tokens'] if t['cls'] == 'apparatus' and t['label'] in ('𐄁', ''))
    words = lambda r: max(1, sum(1 for t in r['tokens'] if t['cls'].startswith('word')))
    a = [div(r) / words(r) for r in rel if words(r) >= 2]
    b = [div(r) / words(r) for r in adm if words(r) >= 2]
    e, p = B.diff_means(a, b)
    return 'Religious inscriptions use word dividers more than tablets', e, p, f'{len(a)} religious, {len(b)} administrative'


def N4():
    after, other = [], []
    for r in B.READ['records']:
        toks = [t for t in r['tokens'] if t['cls'] != 'apparatus']
        for i, t in enumerate(toks[:-1]):
            nxt = toks[i + 1]
            if t['cls'] == 'number' and nxt['entry'] != t['entry']:
                prev_word = next((y for y in reversed(toks[:i]) if y['cls'] in ('word', 'term')), None)
                (after if prev_word and prev_word['label'] == 'KU-RO' else other).append(int(nxt['cls'] == 'commodity'))
    e, p = B.diff_means(after, other)
    return 'After a KU-RO total, the next line opens with a new commodity', e, p, f'{sum(after)}/{len(after)} vs {sum(other)}/{len(other)}'


SANCT = {'Iouktas', 'Kophinas', 'Troullos', 'Syme', 'Palaikastro', 'Psykhro', 'Vrysinas', 'Apodoulou', 'Platanos'}


def N5():
    by = defaultdict(set)
    for r, t, w in B.LA_RELIG:
        by[r['site']].add(w)
    sites = [s for s in by if len(by[s]) >= 2]
    lab = {s: s in SANCT for s in sites}
    jac = lambda a, b: len(by[a] & by[b]) / len(by[a] | by[b])
    pairs = [(a, b) for i, a in enumerate(sites) for b in sites[i + 1:]]
    def stat(l):
        same = [jac(a, b) for a, b in pairs if l[a] and l[b]]
        mixed = [jac(a, b) for a, b in pairs if l[a] != l[b]]
        return (sum(same) / max(1, len(same))) - (sum(mixed) / max(1, len(mixed)))
    real = stat(lab)
    null = []
    vals = list(lab.values())
    for _ in range(B.REPS):
        rng.shuffle(vals)
        null.append(stat(dict(zip(sites, vals))))
    return 'Peak-sanctuary inscriptions share vocabulary with each other more than with other religious objects', round(real, 4), B.pv(null, real), f'{sum(lab.values())} sanctuary sites of {len(sites)}'


# ---------- O: Minoan stems inside Linear B
def stem_rate(ws, la):
    return sum(1 for w in ws if len(w) >= 3 and w[:-1] in la) / len([w for w in ws if len(w) >= 3])


def O1():
    la2 = {w for w in LA_SET if len(w) >= 2}
    e_real = stem_rate(kn_only, la2) - stem_rate(py_only, la2)
    pool, k = kn_only + py_only, len(kn_only)
    null = []
    for _ in range(B.REPS):
        rng.shuffle(pool)
        null.append(stem_rate(pool[:k], la2) - stem_rate(pool[k:], la2))
    return 'Knossos words are Linear A words plus one final syllable more often than Pylos words', round(e_real, 4), B.pv(null, e_real), f'KN {round(stem_rate(kn_only, la2),4)}, PY {round(stem_rate(py_only, la2),4)}'


def O2():
    la2 = {w for w in LA_SET if len(w) >= 2}
    kn_names = [w for w in kn_only if CAT.get(w) == 'anthroponym']
    real = stem_rate(kn_names, la2)
    freq = Counter(s for w in la2 for s in w)
    signs = sorted(freq, key=lambda s: -freq[s])
    size = -(-len(signs) // 10)
    bins = [signs[i:i + size] for i in range(0, len(signs), size)]
    null = []
    for _ in range(1000):
        mp = {}
        for b in bins:
            v = b[:]
            rng.shuffle(v)
            mp.update(zip(b, v))
        null.append(stem_rate(kn_names, {tuple(mp[s] for s in w) for w in la2}))
    return 'Knossos names contain Linear A words as stems (plus a Greek ending) beyond chance', round(real, 4), B.pv(null, real), f'{len(kn_names)} names'


def O3():
    crete_topo = [w for w, s in LB.items() if CAT.get(w) == 'toponym' and s <= {'Knossos', 'Khania', 'Vases - Khania'} and len(w) >= 2]
    main_topo = [w for w, s in LB.items() if CAT.get(w) == 'toponym' and not s & {'Knossos', 'Khania'} and len(w) >= 2]
    hit = lambda ws: [int(w in LA_SET or w[:-1] in LA_SET) for w in ws]
    e, p = B.diff_means(hit(crete_topo), hit(main_topo))
    return 'Cretan place names in Linear B recur in Linear A (as words or stems) more than mainland ones', e, p, f'{sum(hit(crete_topo))}/{len(crete_topo)} vs {sum(hit(main_topo))}/{len(main_topo)}'


def O4():
    la = Counter(s for w in B.LA_TYPES for s in w)
    lb = Counter(s for w in LB for s in w if not s.startswith('*'))
    common = [s for s in la if s in lb]
    x, y = [la[s] for s in common], [lb[s] for s in common]
    real = B.spearman(x, y)
    null = []
    for _ in range(B.REPS):
        rng.shuffle(y)
        null.append(B.spearman(x, y))
    return 'Linear A and Linear B use their shared syllables at correlated rates', round(real, 3), B.pv(null, real), f'{len(common)} shared syllables'


def O5():
    kn = [w for w in kn_only if CAT.get(w) == 'anthroponym']
    py = [w for w in py_only if CAT.get(w) == 'anthroponym']
    e, p = B.diff_means([int(B.vowel(w[-1]) == 'o') for w in py], [int(B.vowel(w[-1]) == 'o') for w in kn])
    return 'Pylos names end in -o (Greek o-stems) more often than Knossos names', e, p, f'KN {round(sum(B.vowel(w[-1])=="o" for w in kn)/len(kn),3)}, PY {round(sum(B.vowel(w[-1])=="o" for w in py)/len(py),3)}'


BATCHES = {'K Knossos trace': [K1, K2, K3, K4, K5], 'L bookkeeping': [L1, L2, L3, L4, L5],
           'M word structure': [M1, M2, M3, M4, M5], 'N sealings and documents': [N1, N2, N3, N4, N5],
           'O Minoan stems in Linear B': [O1, O2, O3, O4, O5]}


def main():
    rows = []
    for batch, fns in BATCHES.items():
        for fn in fns:
            try:
                h, e, p, note = fn()
            except Exception as ex:
                h, e, p, note = fn.__name__, None, None, f'error: {ex}'
            rows.append({'id': fn.__name__, 'batch': batch, 'hypothesis': h, 'effect': e,
                         'p': None if p is None else round(p, 4), 'note': str(note)})
            print(f"{fn.__name__:3} {'-' if p is None else round(p,4):>7}  {h}  | effect {e} | {str(note)[:110]}")
    tested = sorted([r for r in rows if r['p'] is not None], key=lambda r: r['p'])
    m, cut = len(tested), 0
    for i, r in enumerate(tested, 1):
        if r['p'] <= 0.05 * i / m:
            cut = i
    for i, r in enumerate(tested, 1):
        r['bh_supported'] = i <= cut
    for r in rows:
        r.setdefault('bh_supported', None)
    res = {'method': __doc__.strip(), 'tested': m, 'bh_supported': cut, 'results': rows}
    (ROOT / 'reading/batches2_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str) + '\n', encoding='utf-8')
    print(f'\n{m} tested; {cut} survive Benjamini-Hochberg at 5%:')
    for r in tested[:cut]:
        print(f"  {r['id']} p {r['p']}  {r['hypothesis']}")


if __name__ == '__main__':
    main()
