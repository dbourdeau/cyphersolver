"""Ten hypotheses testing the Minoan vowel profile (few e and o) against the other records of the language and
its neighbours, and inside Linear A. Builds on decipher10c.py and decipher10d.py: Linear A, Knossos personal names
and Cretan place names all lack e and o.

All vowel counts use the same Linear B-style spelling (lang_test.spell) for every language, so that a syllabic
script and alphabetic texts are compared on equal terms; for Linear A and Linear B the syllable vowels are used
directly. Each hypothesis has a prediction stated before the test ran and one primary test with its own null.
Benjamini-Hochberg at 5% runs across the ten.

C1  Pre-Greek substrate words (Beekes, via Wiktionary) use fewer e/o vowels than ordinary Greek words.
C2  Eteocretan (Praisos, Dreros) uses fewer e/o vowels than Greek.
C3  Cretan Hieroglyphic sign groups, read with Linear A values, have Linear A's low e/o share rather than
    Linear B's.
C4  Linear A's vowel profile is closer to Luwian's (a three-vowel language) than to Hittite's.
C5  Knossos personal names without a Greek etymology have fewer e/o syllables than those with one.
C6  The same at Pylos: names without a Greek etymology have fewer e/o syllables than those with one.
C7  Linear B words written with undeciphered signs have fewer e/o syllables among their readable signs.
C8  Linear A words ending in an e-sign belong to the religious register more often than other words.
C9  Within each consonant row, Linear A gives i and u a larger share against a than Linear B does.
C10 Linear A's e/o depend on the consonant more than Linear B's do (e/o conditioned by the consonant).
"""
from collections import Counter, defaultdict
import json
from math import log, log2
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import batches as B  # noqa: E402
import decipher10 as D  # noqa: E402
import decipher10b as Db  # noqa: E402
import vigorous as V  # noqa: E402
import lang_test as L  # noqa: E402
import pregreek as PG  # noqa: E402
import eteocretan as ET  # noqa: E402
import chic as CH  # noqa: E402

ROOT = B.ROOT
LEX = ROOT / 'data/lexica'
rng = B.rng
REPS = B.REPS
out = D.out
out.clear()
record = D.record
grid = D.grid
CAT = B.LB_CAT
clean = lambda w: not any(x.startswith('*') for x in w)
RARE = {'e', 'o'}
VOWELS = 'aeiou'


def vowels_of(words):
    """Vowels of syllabic words (tuples of syllables)."""
    return [grid(x)[1] for w in words for x in w if grid(x)]


def eo(words):
    v = vowels_of(words)
    return sum(x in RARE for x in v) / max(1, len(v))


def profile(words):
    c = Counter(vowels_of(words))
    n = sum(c.values())
    return {v: c.get(v, 0) / n for v in VOWELS}


def jsd(p, q):
    m = {k: (p[k] + q[k]) / 2 for k in VOWELS}
    kl = lambda a: sum(a[k] * log2(a[k] / m[k]) for k in VOWELS if a[k] > 0)
    return (kl(p) + kl(q)) / 2


def label_perm(stat, a, b, reps=REPS, lower=False):
    real = stat(a, b)
    pool, k, null = a + b, len(a), []
    for _ in range(reps):
        rng.shuffle(pool)
        null.append(stat(pool[:k], pool[k:]))
    p = (sum(n <= real for n in null) + 1) / (len(null) + 1) if lower else B.pv(null, real)
    return real, p


def spelled(words):
    out_ = []
    for w in words:
        sp = L.spell(w)
        if sp and len(sp) >= 2:
            out_.append(tuple(sp))
    return out_


LA = [w for w in Db.LA_W]
LB = Db.LB_W


# ------------------------------------------------------------------ C1
def C1():
    pre = [json.loads(l)['word'] for l in open(LEX / 'pregreek_wiktionary.jsonl', encoding='utf-8')]
    ordn = []
    for line in open(LEX / 'AncientGreek_head.jsonl', encoding='utf-8'):
        r = json.loads(line)
        if r.get('pos') in ('noun', 'adj', 'verb', 'name') and ' ' not in r['word']:
            ordn.append(r['word'])
    pre_s = spelled([PG.romanise(w) for w in pre])
    ord_s = spelled([PG.romanise(w) for w in ordn])
    pre_set = set(pre_s)
    ord_s = [w for w in ord_s if w not in pre_set]
    by_len = defaultdict(list)
    for w in ord_s:
        by_len[len(w)].append(w)
    need = Counter(len(w) for w in pre_s)
    sample = [w for L_, n in need.items() for w in rng.sample(by_len[L_], min(n, len(by_len[L_])))]
    stat = lambda a, b: eo(a) - eo(b)
    real, p = label_perm(stat, pre_s, sample, lower=True)
    stem = lambda ws: [w[:-1] for w in ws if len(w) >= 3]
    r2, p2 = label_perm(lambda a, b: eo(stem(a)) - eo(stem(b)), pre_s, sample, lower=True)
    record('C1 Pre-Greek words', 'Pre-Greek substrate words use fewer e/o vowels than length-matched ordinary Greek words',
           {'pre_greek_eo': round(eo(pre_s), 4), 'greek_eo': round(eo(sample), 4), 'p': round(p, 4), 'n': [len(pre_s), len(sample)]},
           {'final syllable removed': {'pre': round(eo(stem(pre_s)), 4), 'greek': round(eo(stem(sample)), 4), 'p': round(p2, 4)},
            'stem profiles (final syllable removed)': {'pre-Greek': {k: round(v, 3) for k, v in profile(stem(pre_s)).items()},
                                                       'Greek': {k: round(v, 3) for k, v in profile(stem(sample)).items()}},
            'e alone, stems': label_perm(lambda a, b: profile(stem(a))['e'] - profile(stem(b))['e'], pre_s, sample, lower=True)[1],
            'o alone, stems': label_perm(lambda a, b: profile(stem(a))['o'] - profile(stem(b))['o'], pre_s, sample, lower=True)[1],
            'profiles': {'pre-Greek': {k: round(v, 3) for k, v in profile(pre_s).items()},
                         'Greek': {k: round(v, 3) for k, v in profile(sample).items()},
                         'Linear A': {k: round(v, 3) for k, v in profile(LA).items()}}})
    return p


# ------------------------------------------------------------------ C2
def C2():
    ete = []
    for text in ET.ETEOCRETAN.values():
        for chunk in text.split():
            for piece in chunk.split('|'):
                ete += ET.stretches(piece)
    gre = []
    for text in (ET.GREEK, ET.HOMER):
        gre += [s for w in text.split() for s in ET.greek_stretches(w)]
    e_s, g_s = spelled(ete), spelled(gre)
    stat = lambda a, b: eo(a) - eo(b)
    real, p = label_perm(stat, e_s, g_s, lower=True)
    record('C2 Eteocretan', 'Eteocretan uses fewer e/o vowels than Greek',
           {'eteocretan_eo': round(eo(e_s), 4), 'greek_eo': round(eo(g_s), 4), 'p': round(p, 4), 'pieces': [len(e_s), len(g_s)]},
           {'profiles': {'Eteocretan': {k: round(v, 3) for k, v in profile(e_s).items()},
                         'Greek text': {k: round(v, 3) for k, v in profile(g_s).items()}},
            'caution': 'Eteocretan is known from five short inscriptions; spelling rules add copy vowels to clusters'})
    return p


# ------------------------------------------------------------------ C3
def C3():
    groups = CH.lexicon_groups()
    values = {**CH.GRID1_CERTAIN, **CH.GRID1_PROBABLE}
    read = [tuple(x.lower() for x in v) for v in CH.read(groups, values).values()]
    lb_sample = LB
    stat = lambda a, b: eo(a) - eo(b)
    real, p = label_perm(stat, read, lb_sample, lower=True)
    rl, pl = label_perm(stat, read, LA)
    inv = [v.lower() for v in values.values()]
    inv_eo = sum(1 for v in inv if grid(v) and grid(v)[1] in RARE) / max(1, sum(1 for v in inv if grid(v)))
    record('C3 Cretan Hieroglyphic', 'Hieroglyphic sign groups read with Linear A values have a lower e/o share than Linear B',
           {'chic_eo': round(eo(read), 4), 'lb_eo': round(eo(lb_sample), 4), 'p': round(p, 4), 'groups': len(read)},
           {'against Linear A (two-sided)': {'la_eo': round(eo(LA), 4), 'p': round(pl, 4)},
            'e/o share of the value inventory itself': round(inv_eo, 3),
            'caution': 'only signs with an accepted Linear A equivalent can be read, which limits the vowels available'})
    return p


# ------------------------------------------------------------------ C4
def C4():
    lu = spelled([w for w, _ in L.luwian()])
    hi = spelled([w.replace('-', '') for w, _ in L.kaikki('Hittite', 'forms') + L.kaikki('Hittite', 'romanization-entry')])
    pla = profile(LA)
    real = jsd(pla, profile(hi)) - jsd(pla, profile(lu))
    boot = []
    for _ in range(2000):
        a = [rng.choice(LA) for _ in LA]
        l_ = [rng.choice(lu) for _ in lu]
        h_ = [rng.choice(hi) for _ in hi]
        pa = profile(a)
        boot.append(jsd(pa, profile(h_)) - jsd(pa, profile(l_)))
    p = (sum(b <= 0 for b in boot) + 1) / (len(boot) + 1)
    ranking = {}
    for name, (kind, fn) in L.SOURCES.items():
        try:
            ws = spelled([w for w, _ in fn()])
            if len(ws) >= 50:
                ranking[name] = round(jsd(pla, profile(ws)), 4)
        except Exception as ex:  # a missing cache should not stop the round
            ranking[name] = f'unavailable: {ex}'
    ranking['Hittite'] = round(jsd(pla, profile(hi)), 4)
    ranking['Pre-Greek'] = None
    record('C4 Luwian against Hittite', 'Linear A\'s vowel profile is closer to Luwian than to Hittite',
           {'jsd_LA_Luwian': round(jsd(pla, profile(lu)), 4), 'jsd_LA_Hittite': round(jsd(pla, profile(hi)), 4),
            'bootstrap p (Luwian not closer)': round(p, 4)},
           {'JSD to Linear A by language (lower = closer)': dict(sorted(((k, v) for k, v in ranking.items() if isinstance(v, float)), key=lambda kv: kv[1])),
            'profiles': {'Linear A': {k: round(v, 3) for k, v in pla.items()}, 'Luwian': {k: round(v, 3) for k, v in profile(lu).items()},
                         'Hittite': {k: round(v, 3) for k, v in profile(hi).items()}},
            'caution': 'cuneiform and hieroglyphic Luwian cannot write e or o distinctly, so its profile is partly orthographic'})
    return p


# ------------------------------------------------------------------ C5, C6
def greek_split(site_only):
    names = [w for w in site_only if CAT.get(w) == 'anthroponym' and clean(w)]
    gk = [w for w in names if w in B.GREEK]
    ng = [w for w in names if w not in B.GREEK]
    return ng, gk


def internal(ws):
    return [w[:-1] for w in ws if len(w) >= 2]


def C5():
    ng, gk = greek_split(V.kn_only)
    stat = lambda a, b: eo(internal(a)) - eo(internal(b))
    real, p = label_perm(stat, ng, gk, lower=True)
    record('C5 non-Greek names at Knossos', 'Knossos names without a Greek etymology have fewer e/o syllables',
           {'non_greek': round(eo(internal(ng)), 4), 'greek': round(eo(internal(gk)), 4), 'p': round(p, 4), 'n': [len(ng), len(gk)]},
           {'Linear A': round(eo(LA), 4)})
    return p


def C6():
    ng, gk = greek_split(V.py_only)
    stat = lambda a, b: eo(internal(a)) - eo(internal(b))
    real, p = label_perm(stat, ng, gk, lower=True)
    record('C6 non-Greek names at Pylos', 'Pylos names without a Greek etymology have fewer e/o syllables',
           {'non_greek': round(eo(internal(ng)), 4), 'greek': round(eo(internal(gk)), 4), 'p': round(p, 4), 'n': [len(ng), len(gk)]}, {})
    return p


# ------------------------------------------------------------------ C7
def C7():
    ws = [w for w, s in B.LB_SITES.items() if s & {'Knossos', 'Pylos'} and len(w) >= 2]
    star = [tuple(x for x in w if not x.startswith('*')) for w in ws if not clean(w)]
    star = [w for w in star if len(w) >= 1]
    plain = [w for w in ws if clean(w)]
    stat = lambda a, b: eo(a) - eo(b)
    real, p = label_perm(stat, star, plain, lower=True)
    record('C7 undeciphered-sign words', 'Linear B words with undeciphered signs have fewer e/o syllables among their readable signs',
           {'star_words_eo': round(eo(star), 4), 'other_words_eo': round(eo(plain), 4), 'p': round(p, 4), 'n': [len(star), len(plain)]}, {})
    return p


# ------------------------------------------------------------------ C8
def C8():
    rel = {w for _, _, w in B.LA_RELIG}
    adm = {w for _, _, w in B.LA_ADMIN} - rel
    words = sorted(rel | adm)
    efin = lambda w: bool(grid(w[-1])) and grid(w[-1])[1] == 'e'
    real = sum(efin(w) for w in words if w in rel) / len(rel) - sum(efin(w) for w in words if w in adm) / len(adm)
    labs = [w in rel for w in words]
    null = []
    for _ in range(REPS):
        rng.shuffle(labs)
        r_ = [w for w, l in zip(words, labs) if l]
        a_ = [w for w, l in zip(words, labs) if not l]
        null.append(sum(map(efin, r_)) / len(r_) - sum(map(efin, a_)) / len(a_))
    p = B.pv(null, real)
    ex = sorted('-'.join(w).upper() for w in rel if efin(w))[:20]
    rel_nf = [w for w in words if w in rel and not V.FORMULA.search('-'.join(w).upper())]
    adm_l = [w for w in words if w in adm]
    r2, p2 = label_perm(lambda a, b: sum(map(efin, a)) / len(a) - sum(map(efin, b)) / len(b), rel_nf, adm_l)
    tfin = lambda w: w[-1] == 'te'
    r3, p3 = label_perm(lambda a, b: sum(map(tfin, a)) / len(a) - sum(map(tfin, b)) / len(b), [w for w in words if w in rel], adm_l)
    record('C8 e-final words are religious', 'Linear A words ending in an e-sign lean to the religious register',
           {'religious_e_final': round(sum(map(efin, rel)) / len(rel), 3), 'admin_e_final': round(sum(map(efin, adm)) / len(adm), 3),
            'p': round(p, 4), 'n': [len(rel), len(adm)]},
           {'formula words removed': {'share': round(sum(map(efin, rel_nf)) / len(rel_nf), 3), 'p': round(p2, 4), 'n': len(rel_nf)},
            '-TE final alone': {'religious': round(sum(map(tfin, [w for w in words if w in rel])) / len(rel), 3),
                                'admin': round(sum(map(tfin, adm_l)) / len(adm_l), 3), 'p': round(p3, 4)},
            'religious e-final words': ex})
    return p


# ------------------------------------------------------------------ C9
def iu_ratio(words):
    by = defaultdict(Counter)
    for w in words:
        for x in w:
            g = grid(x)
            if g and g[0] and g[1] in 'aiu':
                by[g[0]][g[1]] += 1
    return {c: (v['i'] + v['u']) / (v['a'] + v['i'] + v['u']) for c, v in by.items() if sum(v.values()) >= 20}


def C9():
    la, lb = iu_ratio(LA), iu_ratio(LB)
    rows = sorted(set(la) & set(lb))
    diffs = [la[r] - lb[r] for r in rows]
    plus = sum(d > 0 for d in diffs)
    n = sum(d != 0 for d in diffs)
    from math import comb
    p = sum(comb(n, k) for k in range(plus, n + 1)) / 2 ** n
    record('C9 i and u against a', 'Within consonant rows Linear A gives i and u a larger share against a than Linear B',
           {'rows_LA_higher': f'{plus}/{n}', 'sign_test_p': round(p, 4)},
           {'per row (LA, LB)': {r: (round(la[r], 3), round(lb[r], 3)) for r in rows}})
    return p


# ------------------------------------------------------------------ C10
def mi_cons_eo(words, internal_only=False, drop=()):
    pairs = [(grid(x)[0], grid(x)[1] in RARE) for w in words for i, x in enumerate(w)
             if grid(x) and grid(x)[0] and grid(x)[0] not in drop and not (internal_only and i == len(w) - 1)]
    n = len(pairs)
    a, b, ab = Counter(x for x, _ in pairs), Counter(y for _, y in pairs), Counter(pairs)
    h = -sum(c / n * log(c / n) for c in b.values())
    mi = sum(c / n * log(c * n / (a[x] * b[y])) for (x, y), c in ab.items())
    return mi / h if h else 0.0, n


def C10():
    real, n = mi_cons_eo(LA)
    toks = [w for w in LB]
    null = []
    for _ in range(1000):
        smp, k = [], 0
        while k < n:
            w = rng.choice(toks)
            smp.append(w)
            k += sum(1 for x in w if grid(x) and grid(x)[0])
        null.append(mi_cons_eo(smp)[0])
    p = B.pv(null, real)
    variants = {}
    rows_with_eo = {grid(x)[0] for w in LA for x in w if grid(x) and grid(x)[1] in RARE}
    no_eo_rows = tuple(sorted({grid(x)[0] for w in LA + LB for x in w if grid(x) and grid(x)[0]} - rows_with_eo))
    for name, kw in (('internal positions only', {'internal_only': True}), ('Q row removed', {'drop': ('q',)}),
                     ('only rows where Linear A uses an e/o sign', {'drop': no_eo_rows})):
        rv, nv = mi_cons_eo(LA, **kw)
        nl = []
        for _ in range(500):
            smp, k = [], 0
            while k < nv:
                w = rng.choice(toks)
                smp.append(w)
                k += sum(1 for i, x in enumerate(w) if grid(x) and grid(x)[0] and grid(x)[0] not in kw.get('drop', ())
                         and not (kw.get('internal_only') and i == len(w) - 1))
            nl.append(mi_cons_eo(smp, **kw)[0])
        variants[name] = {'la': round(rv, 4), 'lb_mean': round(sum(nl) / len(nl), 4), 'p': round(B.pv(nl, rv), 4)}
    record('C10 consonant-conditioned e/o', 'Linear A e/o depend on the consonant more than Linear B e/o do (normalised MI)',
           {'la_nmi': round(real, 4), 'lb_nmi_subsampled_mean': round(sum(null) / len(null), 4), 'p': round(p, 4)},
           {**variants, 'e/o share by consonant in Linear A': {c: round(v, 3) for c, v in sorted(
               ((c, sum(1 for w in LA for x in w if grid(x) and grid(x)[0] == c and grid(x)[1] in RARE) /
                 max(1, sum(1 for w in LA for x in w if grid(x) and grid(x)[0] == c))) for c in 'dkmnpqrstwzj'), key=lambda kv: -kv[1])}})
    return p


def main():
    ps = {}
    for fn in (C1, C2, C3, C4, C5, C6, C7, C8, C9, C10):
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
    (ROOT / 'reading/decipher10e_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str) + '\n', encoding='utf-8')
    print('\nprimary p:', {k: round(v, 4) for k, v in ps.items()})
    print('survive BH at 5%:', supported)


if __name__ == '__main__':
    main()
