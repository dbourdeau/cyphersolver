"""Fifty hypotheses on Linear A in ten themed batches, each tested against a null on data already in hand.

Every test returns an effect and a one-sided p-value (permutation or resampling unless stated). Because fifty
tests will produce false positives by chance, the Benjamini-Hochberg procedure is applied across all fifty at a
false-discovery rate of 5%, and only tests that survive it are called supported. Tests that cannot be run for lack
of data are marked untestable and left out of the correction.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
import json
from math import log, log2, radians, sin, cos, asin, sqrt
from pathlib import Path
import random
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import names_lb as N  # noqa: E402
import name_shapes as S  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
READ = json.loads((ROOT / 'reading/reading.json').read_text(encoding='utf-8'))
CORPUS = {r['name']: r for r in json.loads((ROOT / 'data/corpus.json').read_text(encoding='utf-8'))}
ADMIN = {'Tablet', 'Lames (short thin tablet)', '3-sided bar', '4-sided bar', 'Label'}
SEAL = {'Nodule', 'Roundel', 'Sealing'}
FV = dict(J=F(1, 2), E=F(1, 4), F=F(1, 8), B=F(1, 5), D=F(1, 6), K=F(1, 10), L2=F(1, 20), L3=F(1, 30), L4=F(1, 40), L6=F(1, 60))
REPS = 2000
rng = random.Random(20260923)
SYL = re.compile(r'^[a-z]+[0-9]?$')


# ---------- helpers
def pv(null, real):
    return (sum(n >= real for n in null) + 1) / (len(null) + 1)


def diff_means(a, b, reps=REPS):
    """a > b ?"""
    real = sum(a) / len(a) - sum(b) / len(b)
    pool, k = list(a) + list(b), len(a)
    null = []
    for _ in range(reps):
        rng.shuffle(pool)
        null.append(sum(pool[:k]) / k - sum(pool[k:]) / (len(pool) - k))
    return round(real, 4), pv(null, real)


def chi2(a, b):
    ct = Counter(zip(a, b))
    ra, cb, n = Counter(a), Counter(b), len(a)
    return sum((ct.get((x, y), 0) - ra[x] * cb[y] / n) ** 2 / (ra[x] * cb[y] / n) for x in ra for y in cb)


def chi2_perm(a, b, reps=REPS):
    real = chi2(a, b)
    b = list(b)
    null = []
    for _ in range(reps):
        rng.shuffle(b)
        null.append(chi2(a, b))
    return round(real, 2), pv(null, real)


def jsd(p, q):
    keys = set(p) | set(q)
    m = {k: (p.get(k, 0) + q.get(k, 0)) / 2 for k in keys}
    kl = lambda a: sum(a[k] * log2(a[k] / m[k]) for k in keys if a.get(k, 0) > 0)
    return (kl(p) + kl(q)) / 2


def dist(items):
    c = Counter(items)
    n = sum(c.values())
    return {k: v / n for k, v in c.items()}


def spearman(x, y):
    def ranks(v):
        o = sorted(range(len(v)), key=lambda i: v[i])
        r = [0] * len(v)
        for k, i in enumerate(o):
            r[i] = k
        return r
    rx, ry = ranks(x), ranks(y)
    n = len(x)
    mx, my = sum(rx) / n, sum(ry) / n
    cov = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    return cov / sqrt(sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry))


def vowel(s):
    m = re.search(r'([aeiou])[0-9]?$', s)
    return m.group(1) if m else None


def cons(s):
    m = re.match(r'^([a-z]*?)[aeiou]', s)
    return m.group(1) if m else s


def words_of(pred=lambda r, t: True):
    out = []
    for r in READ['records']:
        for t in r['tokens']:
            if t['cls'] == 'word' and pred(r, t):
                w = tuple(t['label'].lower().split('-'))
                if len(w) >= 2 and all(SYL.match(s) for s in w):
                    out.append((r, t, w))
    return out


def commodity_of_entries(r):
    by = defaultdict(list)
    for t in r['tokens']:
        by[t['entry']].append(t)
    return by


LA_TYPES = sorted({w for _, _, w in words_of()})
LA_ADMIN = [(r, t, w) for r, t, w in words_of(lambda r, t: r['support'] in ADMIN)]
LA_RELIG = [(r, t, w) for r, t, w in words_of(lambda r, t: r['support'] not in ADMIN | SEAL)]
LA_NAMES = S.la_names()
KN, PY, GREEK = S.lb_groups('anthroponym')
LB_SITES, _ = N.lb_vocabulary()
LB_CAT = N.lb_categories()
LB_RECS = N.load_js_map(ROOT / 'data/linearb/LinearBInscriptions.js')


# ---------- batch A: accounting
def A1():
    tot = READ['totals']
    ncom = {r['name']: len({re.findall(r'[A-Z]{3,}', t['label'])[0] for t in r['tokens'] if t['cls'] == 'commodity'})
            for r in READ['records']}
    single = [c['balances_in_some_window'] for c in tot if ncom.get(c['record'], 0) <= 1]
    multi = [c['balances_in_some_window'] for c in tot if ncom.get(c['record'], 0) > 1]
    e, p = diff_means([int(x) for x in single], [int(x) for x in multi])
    return 'Totals balance more often on single-commodity tablets', e, p, f'{sum(single)}/{len(single)} vs {sum(multi)}/{len(multi)}'


def A2():
    stated, entries = [], []
    for r in READ['records']:
        if r['support'] not in ADMIN:
            continue
        toks = r['tokens']
        for i, t in enumerate(toks):
            if t['cls'] == 'number' and t['value'] >= 10:
                prev = next((y for y in reversed(toks[:i]) if y['cls'] != 'apparatus'), None)
                (stated if prev and prev['label'] in ('KU-RO', 'PO-TO-KU-RO') else entries).append(int(t['value'] % 10 == 0))
    e, p = diff_means(stated, entries)
    return 'Totals are round (multiples of 10) more often than entries', e, p, f'{sum(stated)}/{len(stated)} vs {sum(entries)}/{len(entries)}'


def A3():
    lists = []
    for r in READ['records']:
        if r['support'] not in ADMIN:
            continue
        seq = []
        for t in r['tokens']:
            if t['cls'] == 'number':
                seq.append(t['value'])
            elif t['label'] in ('KU-RO', 'KI-RO', 'PO-TO-KU-RO') or t['label'] == '—':
                if len(seq) >= 4:
                    lists.append(seq)
                seq = []
        if len(seq) >= 4:
            lists.append(seq)

    def tau(v):
        c = d = 0
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                c += v[i] > v[j]
                d += v[i] < v[j]
        return (c - d) / max(1, c + d)
    real = sum(tau(v) for v in lists) / len(lists)
    null = []
    for _ in range(REPS):
        tot = 0
        for v in lists:
            w = v[:]
            rng.shuffle(w)
            tot += tau(w)
        null.append(tot / len(lists))
    return 'Entries within a list are written in descending order of size', round(real, 3), pv(null, real), f'{len(lists)} lists'


def A4():
    firsts = [int(str(int(t['value']))[0]) for r in READ['records'] if r['support'] in ADMIN
              for t in r['tokens'] if t['cls'] == 'number' and t['value'] >= 10]
    obs = Counter(firsts)
    n = len(firsts)
    benford = {d: log(1 + 1 / d, 10) for d in range(1, 10)}
    stat = lambda o: sum((o.get(d, 0) - n * benford[d]) ** 2 / (n * benford[d]) for d in range(1, 10))
    real = stat(obs)
    null = [stat(Counter(rng.choices(range(1, 10), weights=[benford[d] for d in range(1, 10)], k=n))) for _ in range(REPS)]
    p_fit = pv(null, real)  # small p = departs from Benford
    return 'Quantities >= 10 follow Benford\'s law (p here = evidence AGAINST Benford)', round(real, 2), p_fit, f'n={n}, first digits {dict(sorted(obs.items()))}'


def A5():
    tot = READ['totals']
    ok = [F(c['stated']) for c in tot if c['balances_in_some_window']]
    bad = [F(c['stated']) for c in tot if not c['balances_in_some_window'] and not c['stated_damaged']]
    e, p = diff_means([float(x) for x in bad], [float(x) for x in ok])
    return 'Larger totals are more often wrong', e, p, f'median wrong {sorted(bad)[len(bad)//2]}, right {sorted(ok)[len(ok)//2]}'


# ---------- batch B: fractions
def frac_tokens():
    out = []
    for r in READ['records']:
        by = commodity_of_entries(r)
        rec_com = [re.findall(r'[A-Z]{3,}', t['label'])[0] for t in r['tokens'] if t['cls'] == 'commodity']
        for e, ts in by.items():
            com = [re.findall(r'[A-Z]{3,}', t['label'])[0] for t in ts if t['cls'] == 'commodity']
            c = com[0] if com else (rec_com[-1] if rec_com else None)
            q = [t for t in ts if t['cls'] in ('number', 'fraction', 'fraction-disputed', 'fraction-unvalued')]
            if q and c:
                fs = [s for t in q for s in t.get('fraction_signs', [])]
                out.append((r, c, fs))
    return out


def B1():
    ft = frac_tokens()
    vir = [int(bool(fs)) for r, c, fs in ft if c == 'VIR']
    oth = [int(bool(fs)) for r, c, fs in ft if c != 'VIR']
    e, p = diff_means(oth, vir)
    return 'Persons (VIR) are never counted in fractions, unlike goods', e, p, f'VIR {sum(vir)}/{len(vir)}, goods {sum(oth)}/{len(oth)}'


def B2():
    freq = Counter(s for r, c, fs in frac_tokens() for s in fs if s in FV)
    signs = [s for s in freq]
    x = [float(FV[s]) for s in signs]
    y = [freq[s] for s in signs]
    real = spearman(x, y)
    null = []
    for _ in range(REPS):
        rng.shuffle(y)
        null.append(spearman(x, y))
    return 'Larger fraction values (Corazza) are used more often', round(real, 3), pv(null, real), dict(freq)


def B3():
    rows = [(r['site'], s) for r, c, fs in frac_tokens() for s in fs if r['site'] in ('Haghia Triada', 'Khania')]
    a, b = [x for x, _ in rows], [y for _, y in rows]
    e, p = chi2_perm(a, b)
    return 'Haghia Triada and Khania use different fraction repertoires', e, p, dict(Counter(rows))


def B4():
    cl = [(c, ' '.join(fs)) for r, c, fs in frac_tokens() if len(fs) >= 2]
    cyp = [int(f == 'K L2') for c, f in cl if c == 'CYP']
    oth = [int(f == 'K L2') for c, f in cl if c != 'CYP']
    e, p = diff_means(cyp, oth)
    return 'The combination K L2 belongs to cyperus', e, p, f'CYP {sum(cyp)}/{len(cyp)}, others {sum(oth)}/{len(oth)}'


def B5():
    tot, ent = [], []
    for r in READ['records']:
        toks = [t for t in r['tokens'] if t['cls'] != 'apparatus']
        for i, t in enumerate(toks):
            if t['cls'] in ('number', 'fraction'):
                prev = toks[i - 1] if i else None
                if prev and prev['cls'] in ('number', 'fraction'):
                    continue
                has = int(i + 1 < len(toks) and toks[i + 1]['cls'] == 'fraction' or t['cls'] == 'fraction')
                (tot if prev and prev['label'] in ('KU-RO', 'PO-TO-KU-RO') else ent).append(has)
    e, p = diff_means(tot, ent)
    return 'Totals carry fractions more often than entries', e, p, f'{sum(tot)}/{len(tot)} vs {sum(ent)}/{len(ent)}'


# ---------- batch C: sign sequences
def C1():
    pos, sign = [], []
    for w in LA_TYPES:
        for i, s in enumerate(w):
            pos.append('I' if i == 0 else 'F' if i == len(w) - 1 else 'M')
            sign.append(s)
    real = chi2(sign, pos)
    null = []
    for _ in range(300):
        sh = []
        for w in LA_TYPES:
            x = list(w)
            rng.shuffle(x)
            sh.extend(x)
        null.append(chi2(sh, pos))
    return 'Signs prefer particular positions in the word (initial, medial, final)', round(real, 1), pv(null, real), 'null: signs shuffled within words'


def pooled_shuffle(words):
    pool = [s for w in words for s in w]
    rng.shuffle(pool)
    out, k = [], 0
    for w in words:
        out.append(tuple(pool[k:k + len(w)]))
        k += len(w)
    return out


def C2():
    rate = lambda ws: sum(a == b for w in ws for a, b in zip(w, w[1:])) / sum(len(w) - 1 for w in ws)
    real = rate(LA_TYPES)
    null = [rate(pooled_shuffle(LA_TYPES)) for _ in range(1000)]
    return 'Reduplication (the same sign twice in a row) is more common than chance', round(real, 4), pv(null, real), f'null mean {round(sum(null)/len(null),4)}'


def C3():
    rate = lambda ws: sum(cons(a) == cons(b) and a != b for w in ws for a, b in zip(w, w[1:])) / sum(len(w) - 1 for w in ws)
    real = rate(LA_TYPES)
    null = [rate(pooled_shuffle(LA_TYPES)) for _ in range(1000)]
    return 'Neighbouring syllables share a consonant more than chance', round(real, 4), pv(null, real), f'null mean {round(sum(null)/len(null),4)}'


def C4():
    v, pos = [], []
    for w in LA_TYPES:
        for i, s in enumerate(w):
            if vowel(s):
                v.append(vowel(s))
                pos.append('final' if i == len(w) - 1 else 'nonfinal')
    e, p = chi2_perm(pos, v)
    fin = dist([x for x, q in zip(v, pos) if q == 'final'])
    return 'Word-final syllables have a different vowel mix', e, p, {k: round(x, 3) for k, x in fin.items()}


def C5():
    def cond_ent(ws):
        big = Counter((a, b) for w in ws for a, b in zip(w, w[1:]))
        first = Counter(a for (a, b), n in big.items() for _ in range(n))
        n = sum(big.values())
        return -sum(c / n * log2(c / first[a]) for (a, b), c in big.items())
    real = -cond_ent(LA_TYPES)
    null = [-cond_ent(pooled_shuffle(LA_TYPES)) for _ in range(300)]
    return 'The next sign is more predictable than chance (lower conditional entropy)', round(-real, 3), pv(null, real), f'null {round(-sum(null)/len(null),3)} bits'


# ---------- batch D: names
def redup(w):
    return any(a == b for a, b in zip(w, w[1:]))


def D1():
    e, p = diff_means([int(redup(w)) for w in KN], [int(redup(w)) for w in PY])
    la = sum(redup(w) for w in LA_NAMES) / len(LA_NAMES)
    return 'Reduplicated names are commoner at Knossos than Pylos', e, p, f'LA {round(la,3)}, KN {round(sum(map(redup,KN))/len(KN),3)}, PY {round(sum(map(redup,PY))/len(PY),3)}'


def D2():
    la = sum(map(len, LA_NAMES)) / len(LA_NAMES)
    dk = [abs(len(w) - la) for w in KN]
    dp = [abs(len(w) - la) for w in PY]
    e, p = diff_means(dp, dk)
    return 'Knossos names are closer in length to Linear A names than Pylos names', e, p, f'mean length LA {round(la,2)}, KN {round(sum(map(len,KN))/len(KN),2)}, PY {round(sum(map(len,PY))/len(PY),2)}'


TOP_LA_END = [s for s, _ in Counter(w[-1] for w in LA_NAMES).most_common(8)]


def D3():
    e, p = diff_means([int(w[-1] in TOP_LA_END) for w in KN], [int(w[-1] in TOP_LA_END) for w in PY])
    return f'Typical Linear A name endings ({", ".join(TOP_LA_END)}) are commoner at Knossos', e, p, ''


def la_score(w):
    pla, ppy = S.profile(LA_NAMES, 'all'), S.profile(PY, 'all')
    return sum(log((pla.get(s, 0) + 1e-3) / (ppy.get(s, 0) + 1e-3)) for s in w) / len(w)


def D4():
    topo = [w for w, s in LB_SITES.items() if s == {'Knossos'} and LB_CAT.get(w) == 'toponym' and len(w) >= 2]
    e, p = diff_means([la_score(w) for w in topo], [la_score(w) for w in KN])
    return 'Knossos place names are more Linear A-like than Knossos personal names', e, p, f'{len(topo)} place names'


def D5():
    where = defaultdict(set)
    for name, rec in LB_RECS:
        if rec.get('site') == 'Knossos':
            rct = 'RCT' in (rec.get('findspot') or '') or 'Chariot' in (rec.get('findspot') or '')
            for t in rec.get('transliteratedWords', []):
                where[tuple(t.strip().lower().split('-'))].add(rct)
    rct = [la_score(w) for w in KN if where.get(w) == {True}]
    oth = [la_score(w) for w in KN if where.get(w) == {False}]
    if len(rct) < 10:
        return 'Names in the early Room of the Chariot Tablets are more Linear A-like', None, None, 'untestable'
    e, p = diff_means(rct, oth)
    return 'Names in the early Room of the Chariot Tablets are more Linear A-like', e, p, f'RCT {len(rct)}, other {len(oth)}'


# ---------- batch E: document structure
def E1():
    head = [len(w) for r, t, w in LA_ADMIN if t.get('function') == 'heading']
    ent = [len(w) for r, t, w in LA_ADMIN if t.get('function') == 'entry label']
    e, p = diff_means(head, ent)
    return 'Heading words are longer than entry words', e, p, f'{len(head)} vs {len(ent)}'


def E2():
    by = defaultdict(set)
    scribe = {}
    for r, t, w in LA_ADMIN:
        if r['site'] == 'Haghia Triada':
            by[r['name']].add(w)
            scribe[r['name']] = r['scribe']
    recs = [n for n in by if scribe[n] and len(by[n]) >= 3]
    jac = lambda a, b: len(by[a] & by[b]) / len(by[a] | by[b])
    pairs = [(a, b) for i, a in enumerate(recs) for b in recs[i + 1:]]
    lab = [scribe[n] for n in recs]
    idx = {n: i for i, n in enumerate(recs)}

    def stat(labels):
        same = [jac(a, b) for a, b in pairs if labels[idx[a]] == labels[idx[b]]]
        diff = [jac(a, b) for a, b in pairs if labels[idx[a]] != labels[idx[b]]]
        return sum(same) / max(1, len(same)) - sum(diff) / len(diff)
    real = stat(lab)
    null = []
    for _ in range(500):
        rng.shuffle(lab)
        null.append(stat(lab))
    return 'Tablets by the same scribe share more vocabulary', round(real, 4), pv(null, real), f'{len(recs)} attributed tablets'


def E3():
    sites = defaultdict(set)
    for r, t, w in LA_ADMIN + LA_RELIG:
        sites[w].add(r['site'])
    multi = [len(w) for w, s in sites.items() if len(s) >= 2]
    single = [len(w) for w, s in sites.items() if len(s) == 1]
    e, p = diff_means(single, multi)
    return 'Words shared between sites are shorter than site-specific words', e, p, f'{len(multi)} shared, {len(single)} local'


def E4():
    last, other = [], []
    for r in READ['records']:
        toks = [t for t in r['tokens'] if t['cls'] != 'apparatus']
        for i, t in enumerate(toks):
            if t['cls'] in ('word', 'term'):
                rest = toks[i + 1:]
                nxt = [y for y in rest if y['entry'] > t['entry']]
                is_end = not nxt or nxt[0]['label'] in ('—',)
                (last if t['label'] == 'KU-RO' else other).append(int(is_end or all(y['cls'] != 'word' for y in nxt[:3])))
    e, p = diff_means(last, other)
    return 'KU-RO closes its section (no further entries follow)', e, p, f'KU-RO {sum(last)}/{len(last)}, other words {sum(other)}/{len(other)}'


def E5():
    seal = [t['label'].lower() for r in READ['records'] if r['support'] in SEAL for t in r['tokens']
            if t['cls'] == 'single-sign']
    init = [w[0] for r, t, w in LA_ADMIN]
    fin = [w[-1] for r, t, w in LA_ADMIN]
    ds, di, df = dist(seal), dist(init), dist(fin)
    real = jsd(ds, df) - jsd(ds, di)
    null = []
    for _ in range(REPS):
        b = rng.choices(seal, k=len(seal))
        null.append(jsd(dist(b), df) - jsd(dist(b), di))
    p = (sum(n <= 0 for n in null) + 1) / (len(null) + 1)
    return 'Single signs on sealings are abbreviations of word beginnings (closer to initial than final signs)', round(real, 4), p, f'{len(seal)} sealing signs; p = share of bootstrap with no advantage'


# ---------- batch F: religious register
def F1():
    e, p = diff_means([len(w) for _, _, w in LA_RELIG], [len(w) for _, _, w in LA_ADMIN])
    return 'Religious (formula) words are longer than administrative words', e, p, f'{len(LA_RELIG)} vs {len(LA_ADMIN)} tokens'


def F2():
    rel = {w for _, _, w in LA_RELIG}
    adm = {w for _, _, w in LA_ADMIN}
    real = -len(rel & adm) / len(rel)
    pool = sorted(rel | adm)
    null = []
    for _ in range(REPS):
        s = set(rng.sample(pool, len(rel)))
        rest = set(pool) - s
        null.append(-len(s & adm) / len(s))
    return 'The religious vocabulary overlaps the administrative less than chance', round(-real, 3), pv(null, real), f'{len(rel & adm)} of {len(rel)} religious types also administrative'


def F3():
    e, p = diff_means([int(w[0] == 'ja') for _, _, w in LA_RELIG], [int(w[0] == 'ja') for _, _, w in LA_ADMIN])
    return 'Words beginning JA- belong to the religious register', e, p, ''


def F4():
    e, p = diff_means([int(w[0] == 'u') for _, _, w in LA_RELIG], [int(w[0] == 'u') for _, _, w in LA_ADMIN])
    return 'Words beginning U- belong to the religious register', e, p, ''


def F5():
    v = [(k, vowel(s)) for k, ws in (('rel', LA_RELIG), ('adm', LA_ADMIN)) for _, _, w in ws for s in w if vowel(s)]
    e, p = chi2_perm([a for a, _ in v], [b for _, b in v])
    return 'Religious and administrative words differ in vowel mix', e, p, ''


# ---------- batch G: script continuity
def lb_site_syllables(site):
    return [s for w, st in LB_SITES.items() if st == {site} for s in w]


def G1():
    la = Counter(s for w in LA_TYPES for s in w)
    kn, py = Counter(lb_site_syllables('Knossos')), Counter(lb_site_syllables('Pylos'))
    common = [s for s in la if s in kn and s in py]
    x = [la[s] for s in common]
    real = spearman(x, [kn[s] for s in common]) - spearman(x, [py[s] for s in common])
    kw, pw = [w for w, st in LB_SITES.items() if st == {'Knossos'}], [w for w, st in LB_SITES.items() if st == {'Pylos'}]
    null = []
    for _ in range(500):
        bk = Counter(s for w in rng.choices(kw, k=len(kw)) for s in w)
        bp = Counter(s for w in rng.choices(pw, k=len(pw)) for s in w)
        null.append(spearman(x, [bk[s] for s in common]) - spearman(x, [bp[s] for s in common]))
    p = (sum(n <= 0 for n in null) + 1) / (len(null) + 1)
    return 'Knossos Linear B uses syllables at rates closer to Linear A than Pylos does', round(real, 3), p, f'{len(common)} shared syllables; p = bootstrap share with no Knossos advantage'


DOUBLETS = {'pa3', 'ra2', 'ta2', 'pu2', 'ra3', 'ro2', 'nwa', 'a2', 'a3', 'dwe', 'dwo', 'twe', 'two', 'ju', 'pte', 'swa'}


def G2():
    k = [int(bool(set(w) & DOUBLETS)) for w, st in LB_SITES.items() if st == {'Knossos'}]
    p_ = [int(bool(set(w) & DOUBLETS)) for w, st in LB_SITES.items() if st == {'Pylos'}]
    e, p = diff_means(k, p_)
    return 'Knossos uses the special signs (pa3, ra2, ta2, pu2...) more than Pylos', e, p, f'{sum(k)}/{len(k)} vs {sum(p_)}/{len(p_)}'


def G3():
    rows = CORPUS.values()
    kept = {'GRA', 'VIN', 'OLIV', 'OLE', 'CYP', 'VIR', 'MUL', 'CAP', 'OVIS', 'SUS', 'BOS', 'TELA', 'AROM', 'FIC'}
    c = Counter()
    for r in rows:
        for t in r['transliteratedWords']:
            m = re.match(r'^\*?([A-Z]{3,}|\d{3}[A-Z]?)', t.replace('*', ''))
            if m and not re.match(r'^[A-Z]+-', t):
                c[m.group(1)] += 1
    a = [n for s, n in c.items() if s in kept]
    b = [n for s, n in c.items() if re.match(r'^\d{3}', s)]
    e, p = diff_means(a, b)
    return 'Logograms Linear B kept were commoner in Linear A than numbered ones it did not', e, p, f'{len(a)} kept, {len(b)} numbered'


def G4():
    k = [int(any(x.startswith('*') for x in w)) for w, st in LB_SITES.items() if st == {'Knossos'}]
    p_ = [int(any(x.startswith('*') for x in w)) for w, st in LB_SITES.items() if st == {'Pylos'}]
    e, p = diff_means(k, p_)
    return 'Undeciphered Linear B signs (*18, *47, *56...) are commoner at Knossos', e, p, f'{sum(k)}/{len(k)} vs {sum(p_)}/{len(p_)}'


def G5():
    kn_all = [w for w, st in LB_SITES.items() if st == {'Knossos'} and LB_CAT.get(w) == 'anthroponym']
    star = [la_score(tuple(x for x in w if not x.startswith('*'))) for w in kn_all if any(x.startswith('*') for x in w) and len([x for x in w if not x.startswith('*')]) >= 1]
    plain = [la_score(w) for w in kn_all if not any(x.startswith('*') for x in w)]
    if len(star) < 8:
        return 'Knossos names with undeciphered signs are more Linear A-like', None, None, f'untestable ({len(star)} names)'
    e, p = diff_means(star, plain)
    return 'Knossos names with undeciphered signs are more Linear A-like', e, p, f'{len(star)} names with * signs'


# ---------- batch H: robustness of the Knossos name result
def names_at(site):
    return [w for w, st in LB_SITES.items() if st == {site} and LB_CAT.get(w) == 'anthroponym' and len(w) >= 2
            and not any(x.startswith('*') for x in w)]


def H1():
    th = names_at('Thebes')
    if len(th) < 20:
        return 'Knossos names are more Linear A-like than Thebes names', None, None, f'untestable ({len(th)} Theban names)'
    t = S.test(LA_NAMES, KN, th, rng, REPS)['all']
    return 'Knossos names are more Linear A-like than Thebes names', t['D'], t['p_knossos_closer'], f'{len(th)} Theban names'


def H2():
    main = [w for w, st in LB_SITES.items() if st and not st & {'Knossos', 'Khania', 'Vases - Khania'} and 'Pylos' not in st
            and LB_CAT.get(w) == 'anthroponym' and len(w) >= 2]
    if len(main) < 20:
        return 'Knossos names are more Linear A-like than non-Pylian mainland names', None, None, f'untestable ({len(main)})'
    t = S.test(LA_NAMES, KN, main, rng, REPS)['all']
    return 'Knossos names are more Linear A-like than non-Pylian mainland names', t['D'], t['p_knossos_closer'], f'{len(main)} names'


def bigram_profile(ws):
    return dist([(a, b) for w in ws for a, b in zip(w, w[1:])])


def H3():
    pla = bigram_profile(LA_NAMES)
    real = jsd(pla, bigram_profile(PY)) - jsd(pla, bigram_profile(KN))
    pool, k = KN + PY, len(KN)
    null = []
    for _ in range(1000):
        rng.shuffle(pool)
        null.append(jsd(pla, bigram_profile(pool[k:])) - jsd(pla, bigram_profile(pool[:k])))
    return 'Knossos names are closer to Linear A names in syllable pairs too', round(real, 4), pv(null, real), ''


def H4():
    by = lambda ws: defaultdict(list, {L: [w for w in ws if len(w) == L] for L in set(map(len, ws))})
    bk, bp = by(KN), by(PY)
    need = Counter(len(w) for w in PY)
    ks = [w for L, n in need.items() for w in rng.sample(bk[L], min(n, len(bk[L])))]
    t = S.test(LA_NAMES, ks, PY, rng, REPS)['all']
    return 'The Knossos name effect survives matching word lengths', t['D'], t['p_knossos_closer'], f'{len(ks)} length-matched Knossos names'


def H5():
    rel = sorted({w for _, _, w in LA_RELIG})
    t = S.test(rel, KN, PY, rng, REPS)['all']
    return 'Linear A religious words also resemble Knossos names more than Pylos names', t['D'], t['p_knossos_closer'], f'{len(rel)} religious word types'


# ---------- batch I: chronology and geography
def period(r):
    c = CORPUS.get(r['name'], {}).get('context', '') or ''
    return 'MM' if c.startswith('MM') else 'LM' if c.startswith('LM') else None


def I1():
    rows = [(period(r), s) for r, t, w in words_of() for s in w if period(r)]
    e, p = chi2_perm([a for a, _ in rows], [b for _, b in rows], 500)
    return 'Middle Minoan and Late Minoan texts use syllables differently', e, p, dict(Counter(a for a, _ in rows))


def I2():
    mm = [len(w) for r, t, w in words_of() if period(r) == 'MM']
    lm = [len(w) for r, t, w in words_of() if period(r) == 'LM']
    e, p = diff_means(lm, mm)
    return 'Words are longer in Late Minoan texts than Middle Minoan', e, p, f'{len(mm)} MM, {len(lm)} LM tokens'


def I3():
    mm = [int(vowel(s) == 'o') for r, t, w in words_of() if period(r) == 'MM' for s in w]
    lm = [int(vowel(s) == 'o') for r, t, w in words_of() if period(r) == 'LM' for s in w]
    e, p = diff_means(mm, lm)
    return 'o-syllables were commoner earlier (Middle Minoan) than later', e, p, f'MM {round(sum(mm)/len(mm),3)}, LM {round(sum(lm)/len(lm),3)}'


COORD = {'Haghia Triada': (35.059, 24.792), 'Phaistos': (35.051, 24.814), 'Knossos': (35.298, 25.163),
         'Zakros': (35.098, 26.261), 'Khania': (35.517, 24.018), 'Malia': (35.293, 25.493),
         'Palaikastro': (35.197, 26.262), 'Tylissos': (35.300, 25.019), 'Arkhanes': (35.237, 25.162),
         'Iouktas': (35.263, 25.117), 'Petras': (35.205, 26.123), 'Gournia': (35.106, 25.793)}


def km(a, b):
    (la1, lo1), (la2, lo2) = COORD[a], COORD[b]
    la1, lo1, la2, lo2 = map(radians, (la1, lo1, la2, lo2))
    h = sin((la2 - la1) / 2) ** 2 + cos(la1) * cos(la2) * sin((lo2 - lo1) / 2) ** 2
    return 6371 * 2 * asin(sqrt(h))


def I4():
    syl = defaultdict(list)
    for r, t, w in words_of():
        if r['site'] in COORD:
            syl[r['site']].extend(w)
    sites = [s for s in syl if len(syl[s]) >= 60]
    pairs = [(a, b) for i, a in enumerate(sites) for b in sites[i + 1:]]
    d = [km(a, b) for a, b in pairs]
    div = lambda lab: [jsd(dist(syl[lab[a]]), dist(syl[lab[b]])) for a, b in pairs]
    ident = {s: s for s in sites}
    real = spearman(d, div(ident))
    null = []
    for _ in range(1000):
        perm = sites[:]
        rng.shuffle(perm)
        null.append(spearman(d, div(dict(zip(sites, perm)))))
    return 'Sites farther apart differ more in syllable use (Mantel test)', round(real, 3), pv(null, real), f'{len(sites)} sites: {sites}'


def I5():
    syl = defaultdict(list)
    for r, t, w in words_of():
        syl[r['site']].extend(w)
    ht, kh, za = syl['Haghia Triada'], syl['Khania'], syl['Zakros']
    real = jsd(dist(ht), dist(kh)) - jsd(dist(ht), dist(za))
    null = []
    for _ in range(1000):
        pool = kh + za
        rng.shuffle(pool)
        null.append(jsd(dist(ht), dist(pool[:len(kh)])) - jsd(dist(ht), dist(pool[len(kh):])))
    return 'Khania differs more from Haghia Triada than Zakros does', round(real, 4), pv(null, real), f'{len(kh)} KH, {len(za)} ZA syllables'


# ---------- batch J: quantities
def entries_with(pred):
    out = []
    for r in READ['records']:
        if r['support'] not in ADMIN:
            continue
        section = None
        for e, ts in sorted(commodity_of_entries(r).items()):
            if any(t['label'] == 'KI-RO' for t in ts) and not any(t['cls'] == 'number' for t in ts):
                section = 'KI-RO'
            if any(t['label'] == 'KU-RO' for t in ts):
                section = None
            q = sum(t['value'] for t in ts if t['cls'] == 'number')
            com = [re.findall(r'[A-Z]{3,}', t['label'])[0] for t in ts if t['cls'] == 'commodity']
            words = [t['label'] for t in ts if t['cls'] in ('word', 'term')]
            if q and pred(ts):
                out.append({'q': q, 'com': com[0] if com else None, 'section': section, 'words': words, 'record': r['name']})
    return out


def J1():
    rows = [x for x in entries_with(lambda ts: True) if x['com'] in ('VIR', 'GRA', 'VIN', 'OLE', 'CYP', 'OLIV')]
    e, p = chi2_perm([x['com'] for x in rows], ['1' if x['q'] == 1 else 'small' if x['q'] < 10 else 'large' for x in rows])
    return 'Amount sizes depend on the commodity', e, p, {c: round(sum(x['q'] for x in rows if x['com'] == c) / max(1, sum(1 for x in rows if x['com'] == c)), 1) for c in ('VIR', 'GRA', 'VIN', 'OLE', 'CYP', 'OLIV')}


def J2():
    ent = entries_with(lambda ts: any(t['cls'] == 'word' and t.get('function') == 'entry label' for t in ts))
    vir_recs = {r['name'] for r in READ['records'] if any(t['cls'] == 'commodity' and t['label'].startswith('VIR') for t in r['tokens'])}
    a = [int(x['q'] == 1) for x in ent if x['record'] in vir_recs]
    b = [int(x['q'] == 1) for x in ent if x['record'] not in vir_recs]
    e, p = diff_means(a, b)
    return 'In lists of men, each named entry is usually a single person (1)', e, p, f'{sum(a)}/{len(a)} vs {sum(b)}/{len(b)}'


def J3():
    ent = entries_with(lambda ts: True)
    a = [x['q'] for x in ent if x['section'] == 'KI-RO']
    b = [x['q'] for x in ent if x['section'] != 'KI-RO']
    e, p = diff_means(b, a)
    return 'Amounts in KI-RO sections are smaller than elsewhere', e, p, f'{len(a)} KI-RO entries'


def J4():
    ent = entries_with(lambda ts: True)
    a = [log(x['q']) for x in ent if 'SA-RA2' in x['words']]
    b = [log(x['q']) for x in ent if 'SA-RA2' not in x['words'] and x['com'] in ('GRA', 'CYP')]
    e, p = diff_means(a, b)
    return 'Amounts entered with SA-RA2 are larger than other grain and cyperus amounts', e, p, f'{len(a)} SA-RA2 entries'


def J5():
    q = [int(x['q'] % 2 == 0) for x in entries_with(lambda ts: True) if x['q'] >= 2]
    real = sum(q) / len(q)
    null = [sum(rng.random() < 0.5 for _ in q) / len(q) for _ in range(REPS)]
    return 'Even amounts are commoner than odd ones (rationing in pairs)', round(real, 3), pv(null, real), f'{sum(q)}/{len(q)}'


BATCHES = {'A accounting': [A1, A2, A3, A4, A5], 'B fractions': [B1, B2, B3, B4, B5],
           'C sign sequences': [C1, C2, C3, C4, C5], 'D names': [D1, D2, D3, D4, D5],
           'E document structure': [E1, E2, E3, E4, E5], 'F religious register': [F1, F2, F3, F4, F5],
           'G script continuity': [G1, G2, G3, G4, G5], 'H Knossos-name robustness': [H1, H2, H3, H4, H5],
           'I chronology and geography': [I1, I2, I3, I4, I5], 'J quantities': [J1, J2, J3, J4, J5]}


def main():
    rows = []
    for batch, fns in BATCHES.items():
        for fn in fns:
            try:
                h, e, p, note = fn()
            except Exception as ex:  # recorded, not hidden
                h, e, p, note = fn.__name__, None, None, f'error: {ex}'
            rows.append({'id': fn.__name__, 'batch': batch, 'hypothesis': h, 'effect': e,
                         'p': None if p is None else round(p, 4), 'note': str(note)})
            print(f"{fn.__name__:3} {'-' if p is None else round(p,4):>7}  {h}  | effect {e} | {str(note)[:120]}")
    tested = sorted([r for r in rows if r['p'] is not None], key=lambda r: r['p'])
    m = len(tested)
    cut = 0
    for i, r in enumerate(tested, 1):
        if r['p'] <= 0.05 * i / m:
            cut = i
    for i, r in enumerate(tested, 1):
        r['bh_supported'] = i <= cut
    for r in rows:
        r.setdefault('bh_supported', None)
    res = {'method': __doc__.strip(), 'tested': m, 'bh_supported': cut, 'results': rows}
    (ROOT / 'reading/batches_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str) + '\n', encoding='utf-8')
    print(f'\n{m} tested; {cut} survive Benjamini-Hochberg at 5%:')
    for r in tested[:cut]:
        print(f"  {r['id']} p {r['p']}  {r['hypothesis']}")


if __name__ == '__main__':
    main()
