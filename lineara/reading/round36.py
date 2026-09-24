"""Round 36 (loop round 8 of 10): the religious texts (supports that are neither tablets nor sealings).

Y1  The formula words keep a fixed order across inscriptions (known, Davis 2014; replicated here).
Y2  Religious word types are attested at two or more sites more often than administrative word types.
Y3  Religious vocabulary repeats more (lower type/token ratio) than administrative vocabulary of the same size.
Y4  The word-initial preference of Q-row signs holds in religious words (against Linear B).
Y5  Inscriptions differ in length (words per inscription) by object type.
Y6  Non-formula religious words are more name-shaped than formula words (model: Linear A entry labels against
    headings).
Y7  Inscriptions from the same site share non-formula words more than inscriptions from different sites.
Y8  Religious words ending in -TE are attested at a single site more often than other religious words.
Y9  Religious texts repeat word pairs (bigrams) more than administrative texts of the same size.
Y10 *301 is concentrated in religious words relative to other unread signs.
"""
from collections import Counter, defaultdict
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402

B, X, V, D = R.B, R.X, R.V, R.D
grid = R.grid
FORM = V.FORMULA


def religious_records():
    recs = []
    for r in B.READ['records']:
        if r['support'] in B.ADMIN or r['support'] in B.SEAL:
            continue
        words = [t['label'] for t in r['tokens'] if t['cls'] in ('word', 'word-with-unknown-sign', 'term') and '-' in t['label']]
        if words:
            recs.append({'name': r['name'], 'site': r['site'], 'support': r['support'], 'words': words})
    return recs


REL = religious_records()
ADM_TOK = [t['label'] for r in B.READ['records'] if r['support'] in B.ADMIN for t in r['tokens'] if t['cls'] in ('word', 'term') and '-' in t['label']]
REL_TOK = [w for r in REL for w in r['words']]
FAMILY = {'a-ta-i': r'^A-TA-I-\*301', 'ja-sa-sa-ra': r'^J?A-SA-SA-RA', 'u-na-ka-na': r'^U-NA-(RU-)?KA-NA', 'i-pi-na-ma': r'^I-PI-NA-M', 'si-ru-te': r'^SI-RU-T'}
CANON = ['a-ta-i', 'ja-sa-sa-ra', 'u-na-ka-na', 'i-pi-na-ma', 'si-ru-te']


def fam(w):
    for f, pat in FAMILY.items():
        if re.match(pat, w):
            return f
    return None


def Y1():
    seqs = []
    for r in REL:
        s = [fam(w) for w in r['words'] if fam(w)]
        s = list(dict.fromkeys(s))
        if len(s) >= 2:
            seqs.append([CANON.index(f) for f in s])
    conc = lambda ss: sum(1 for s in ss for i in range(len(s)) for j in range(i + 1, len(s)) if s[i] < s[j])
    pairs = sum(len(s) * (len(s) - 1) // 2 for s in seqs)
    real = conc(seqs)
    null = []
    for _ in range(R.REPS):
        sh = []
        for s in seqs:
            s2 = list(s)
            R.rng.shuffle(s2)
            sh.append(s2)
        null.append(conc(sh))
    p = R.pv_hi(null, real)
    return p, 'The formula words keep a fixed order across inscriptions', {'in_order_pairs': f'{real}/{pairs}', 'null': round(sum(null) / len(null), 1), 'p': round(p, 4), 'inscriptions': len(seqs)}, {}


def Y2():
    sites = defaultdict(set)
    reg = {}
    for r in B.READ['records']:
        rel = r['support'] not in B.ADMIN and r['support'] not in B.SEAL
        for t in r['tokens']:
            if t['cls'] in ('word', 'term', 'word-with-unknown-sign') and '-' in t['label']:
                sites[t['label']].add(r['site'])
                reg.setdefault(t['label'], set()).add('rel' if rel else 'adm' if r['support'] in B.ADMIN else 'seal')
    words = [w for w, s in reg.items() if s in ({'rel'}, {'adm'})]
    r_, p, a, b = R.flag_compare(words, lambda w: reg[w] == {'rel'}, lambda w: len(sites[w]) >= 2)
    return p, 'Religious word types are attested at 2+ sites more often than administrative ones', {'religious': a, 'admin': b, 'p': round(p, 4)}, {}


def Y3():
    n = len(REL_TOK)
    real = len(set(REL_TOK)) / n
    null = [len(set(R.rng.sample(ADM_TOK, n))) / n for _ in range(R.REPS)]
    p = R.pv_lo(null, real)
    return p, 'Religious vocabulary repeats more than administrative vocabulary of the same size', {'type_token_religious': round(real, 3), 'admin_same_size': round(sum(null) / len(null), 3), 'p': round(p, 4), 'tokens': n}, {}


def Y4():
    rel = sorted({tuple(x.lower() for x in w.split('-')) for w in REL_TOK if all(re.fullmatch(r'[A-Z]+[0-9]?', x) for x in w.split('-'))})
    q = lambda ws: sum(1 for w in ws for i, x in enumerate(w) if grid(x) and grid(x)[0] == 'q' and i == 0) / max(1, sum(1 for w in ws for x in w if grid(x) and grid(x)[0] == 'q'))
    r_, p, nm = R.compare(rel, R.LB, q)
    return p, 'Q-row signs are word-initial in religious words more than in Linear B', {'religious': round(q(rel), 3), 'LB': round(q(R.LB), 3), 'p': round(p, 4)}, {}


def Y5():
    items = [(r['support'], len(r['words'])) for r in REL]
    c = Counter(s for s, _ in items)
    items = [x for x in items if c[x[0]] >= 3]
    import round34 as W
    vals = [v for _, v in items]
    real, p, nm = X.shuffle_test(lambda s: W.between(vals, s), [s for s, _ in items], reps=R.REPS)
    g = defaultdict(list)
    for s, v in items:
        g[s].append(v)
    return p, 'Inscription length differs by object type', {'between_SS': round(real, 2), 'null': round(nm, 2), 'p': round(p, 4)}, {'mean words': {s: round(sum(v) / len(v), 2) for s, v in g.items()}}


def Y6():
    fn = defaultdict(Counter)
    for r, t, w in B.LA_ADMIN:
        fn[w][t.get('function')] += 1
    ent = [w for w, c in fn.items() if c.most_common(1)[0][0] == 'entry label']
    head = [w for w, c in fn.items() if c.most_common(1)[0][0] == 'heading']
    me, mh = V.nb_model(ent), V.nb_model(head)
    score = lambda w: sum(me(s) - mh(s) for s in w) / len(w)
    plain = lambda w: all(re.fullmatch(r'[A-Z]+[0-9]?', x) for x in w.split('-'))
    words = sorted({w for w in REL_TOK if plain(w)})
    nonf = [tuple(x.lower() for x in w.split('-')) for w in words if not FORM.search(w)]
    form = [tuple(x.lower() for x in w.split('-')) for w in words if FORM.search(w)]
    r_, p, nm = R.compare(nonf, form, lambda ws: sum(map(score, ws)) / len(ws))
    return p, 'Non-formula religious words are more name-shaped than formula words', {'nonformula_mean': round(sum(map(score, nonf)) / len(nonf), 3), 'formula_mean': round(sum(map(score, form)) / len(form), 3), 'p': round(p, 4), 'n': [len(nonf), len(form)]}, {}


def Y7():
    items = [(r['site'], {w for w in r['words'] if not FORM.search(w)}) for r in REL]
    items = [x for x in items if x[1]]
    pairs = [(i, j) for i in range(len(items)) for j in range(i + 1, len(items))]
    share = {(i, j): bool(items[i][1] & items[j][1]) for i, j in pairs}
    sites = [s for s, _ in items]

    def stat(st):
        same = [v for (i, j), v in share.items() if st[i] == st[j]]
        diff = [v for (i, j), v in share.items() if st[i] != st[j]]
        return sum(same) / max(1, len(same)) - sum(diff) / max(1, len(diff))
    real, p, nm = X.shuffle_test(stat, sites, reps=R.REPS)
    return p, 'Same-site inscriptions share non-formula words more than cross-site ones', {'diff': round(real, 4), 'null': round(nm, 4), 'p': round(p, 4), 'inscriptions': len(items)}, {}


def Y8():
    sites = defaultdict(set)
    for r in REL:
        for w in r['words']:
            sites[w].add(r['site'])
    words = sorted(sites)
    r_, p, a, b = R.flag_compare(words, lambda w: w.endswith('-TE'), lambda w: len(sites[w]) == 1)
    return p, 'Religious words in -TE are attested at a single site more often', {'TE_single_site': a, 'other': b, 'p': round(p, 4)}, {}


def bigram_rate(seqs):
    bg = Counter((s[i], s[i + 1]) for s in seqs for i in range(len(s) - 1))
    tot = sum(bg.values())
    return sum(n for n in bg.values() if n >= 2) / max(1, tot)


def Y9():
    rel = [r['words'] for r in REL if len(r['words']) >= 2]
    adm = []
    for r in B.READ['records']:
        if r['support'] in B.ADMIN:
            s = [t['label'] for t in r['tokens'] if t['cls'] in ('word', 'term') and '-' in t['label']]
            if len(s) >= 2:
                adm.append(s)
    n = sum(len(s) - 1 for s in rel)
    real = bigram_rate(rel)
    null = []
    for _ in range(1000):
        smp, k = [], 0
        while k < n:
            s = R.rng.choice(adm)
            smp.append(s)
            k += len(s) - 1
        null.append(bigram_rate(smp))
    p = R.pv_hi(null, real)
    return p, 'Religious texts repeat word pairs more than administrative texts of the same size', {'religious': round(real, 3), 'admin_same_size': round(sum(null) / len(null), 3), 'p': round(p, 4)}, {}


def Y10():
    occ = []
    for r in B.READ['records']:
        rel = r['support'] not in B.ADMIN and r['support'] not in B.SEAL
        for t in r['tokens']:
            for x in re.findall(r'\*\d+[A-Z]?', t['label']):
                occ.append((x, rel))
    r_, p, a, b = R.flag_compare(occ, lambda o: o[0] == '*301', lambda o: o[1])
    return p, '*301 is concentrated in religious words relative to other unread signs', {'301_religious': a, 'other_unread_religious': b, 'p': round(p, 4)}, {}


if __name__ == '__main__':
    R.run('round36', 'the religious texts', __doc__, [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10])
