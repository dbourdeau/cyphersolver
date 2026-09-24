"""Round 68 (after the saturation loop): the two open leads that need no new inscriptions. BH at 5% across the eight.

Part 1, the Z row. ZA and ZU are the one Linear A row that does not keep together.
M1 Some other consonant row is closer in context to ZA/ZU than chance: the largest row affinity (mean cosine of
   ZA/ZU with the row's signs minus with all other signs) exceeds the same maximum for random sign pairs.

Part 2, a sound-pattern comparison across 107 languages (NorthEuraLex 4.0, Dellert et al. 2020, CC-BY 4.0).
Every word is respelled as Linear B spells Greek: consonants fold into the Linear A rows (t d k q p m n r s j w z),
h and glottals are dropped, a consonant before another consonant is dropped if it is r/l, n, m or s and otherwise
written with the next vowel, and word-final consonants are dropped. Six features are computed on the respelled
syllables: share of e/o, the coronal e/o log-odds (after t r s n q against after k p m j w), consonant harmony
(adjacent syllables with the same consonant, over its expectation), hiatus (vowel-only syllables inside the word),
and the shares of a, i and u. Distance = Euclidean on features standardised across the 107 languages.

L0 Control: the Linear B vocabulary (Greek, in its own spelling) has Modern Greek among its 10 nearest languages.
L1 Linear A's coronal e/o log-odds is higher than in 95% of the languages (rank p).
L2 Linear A's e/o share is lower than in 95% of the languages (rank p).
L3 Linear A's harmony ratio is higher than in 95% of the languages (rank p).
L4 One family is over-represented among Linear A's 10 nearest languages (largest family count against family
   labels shuffled among languages).
L5 Languages nearer Crete are nearer Linear A in sound pattern (Spearman of fingerprint distance against
   great-circle distance from Crete, predicted positive).
L6 Linear A's nearest languages differ from Linear B's: the overlap of the two 10-nearest lists is smaller than
   between Linear B and itself after a 50% resample of its words (a check that the comparison separates the two).
"""
from collections import Counter, defaultdict
from math import log, radians, sin, cos, asin, sqrt
import csv
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import decipher10b as ZB  # noqa: E402

B, D, grid = R.B, R.D, R.grid
ROOT = Path(__file__).resolve().parents[1]
NEL = ROOT / 'data' / 'northeuralex'
TAKE, AVOID = set('trsnq'), set('kpmjw')
CRETE = (35.2, 24.9)

# ------------------------------------------------------------------ Part 1: Z row


def M1():
    vecs = ZB.ctx_vectors(ZB.LA_W)
    signs = [s for s in vecs if grid(s)]
    zs = [s for s in signs if grid(s)[0] == 'z']
    rows = defaultdict(list)
    for s in signs:
        if grid(s)[0] not in ('z', ''):
            rows[grid(s)[0]].append(s)
    rows = {c: v for c, v in rows.items() if len(v) >= 2}
    nonz = [s for s in signs if grid(s)[0] != 'z']

    def aff(group):
        out = {}
        for c, members in rows.items():
            a = [D.cos(vecs[x], vecs[y]) for x in group for y in members if y not in group]
            b = [D.cos(vecs[x], vecs[y]) for x in group for y in signs if y not in group and y not in members]
            if a and b:
                out[c] = sum(a) / len(a) - sum(b) / len(b)
        return out
    real = aff(zs)
    best = max(real, key=real.get)
    null = []
    for _ in range(R.REPS):
        g = R.rng.sample(nonz, len(zs))
        null.append(max(aff(g).values()))
    p = R.pv_hi(null, real[best])
    ranked = sorted(real.items(), key=lambda kv: -kv[1])
    return p, 'Another row is closer to ZA/ZU than chance', {'best_row': best, 'affinity': round(real[best], 4), 'null_max': round(sum(null) / len(null), 4), 'p': round(p, 4), 'z_signs': zs}, {'ranking': [(c, round(v, 4)) for c, v in ranked]}

# ------------------------------------------------------------------ Part 2: respelling


VOW = {}
for chars, v in (('aɑæɐäɒᴀ', 'a'), ('eɛəøœɜɘɤ', 'e'), ('iɪɨyʏɯ', 'i'), ('oɔɵ', 'o'), ('uʊʉ', 'u')):
    for ch in chars:
        VOW[ch] = v
CONS = {}
for chars, c in (('tθ', 't'), ('dð', 'd'), ('kgxɣqɢχɡ', 'k'), ('pbfɸ', 'p'), ('m', 'm'), ('nɲŋɴɳ', 'n'),
                 ('rɾʀʁlɫʎɭɽɹɻʟ', 'r'), ('szʃʒɕʑʂʐ', 's'), ('j', 'j'), ('wvʋβɥ', 'w')):
    for ch in chars:
        CONS[ch] = c
DROP = set('hħʕʔɦʜʢ')


def seg_class(seg):
    s = unicodedata.normalize('NFD', seg)
    base = ''.join(ch for ch in s if not unicodedata.combining(ch) and ch not in 'ːˑʰʷʲˠˤ̃͡‿ˀ')
    if not base:
        return None
    if 'ʷ' in s and base[0] in 'kg':
        return ('C', 'q')
    if len(base) >= 2 and base[0] in 'td' and base[1] in 'szʃʒɕʑʂʐ':
        return ('C', 'z')
    ch = base[0]
    if ch in VOW:
        return ('V', VOW[ch])
    if ch in CONS:
        return ('C', CONS[ch])
    if ch in DROP:
        return None
    return ('?', ch)


def respell(segments):
    """IPA segment list -> list of (consonant or '', vowel) syllables, Linear B spelling rules; None if unknown."""
    cls = []
    for seg in segments:
        c = seg_class(seg)
        if c is None:
            continue
        if c[0] == '?':
            return None
        cls.append(c)
    out, cluster = [], []
    for kind, val in cls:
        if kind == 'C':
            cluster.append(val)
            continue
        if cluster:
            for c in cluster[:-1]:
                if c not in ('r', 'n', 'm', 's'):
                    out.append((c, val))
            out.append((cluster[-1], val))
        else:
            out.append(('', val))
        cluster = []
    return out or None


def la_syll(word):
    out = []
    for s in word:
        g = grid(s)
        if not g or g[1] not in 'aeiou':
            return None
        out.append((g[0], g[1]))
    return out


# ------------------------------------------------------------------ features


def features(words):
    sy = [s for w in words for s in w]
    n = len(sy)
    eo = sum(1 for _, v in sy if v in 'eo')
    t_eo = sum(1 for c, v in sy if c in TAKE and v in 'eo'); t_n = sum(1 for c, _ in sy if c in TAKE)
    a_eo = sum(1 for c, v in sy if c in AVOID and v in 'eo'); a_n = sum(1 for c, _ in sy if c in AVOID)
    lo = lambda k, m: log((k + 0.5) / (m - k + 0.5))
    cor = lo(t_eo, t_n) - lo(a_eo, a_n)
    cc = Counter(c for c, _ in sy if c)
    tot = sum(cc.values())
    exp = sum((x / tot) ** 2 for x in cc.values())
    pairs = [(w[i][0], w[i + 1][0]) for w in words for i in range(len(w) - 1) if w[i][0] and w[i + 1][0]]
    harm = (sum(a == b for a, b in pairs) / len(pairs)) / exp if pairs else 0
    inner = [s for w in words for s in w[1:]]
    hiat = sum(1 for c, _ in inner if not c) / max(1, len(inner))
    vc = Counter(v for _, v in sy)
    return {'eo': eo / n, 'cor': cor, 'harm': harm, 'hiat': hiat, 'a': vc['a'] / n, 'i': vc['i'] / n, 'u': vc['u'] / n}


FEATS = ['eo', 'cor', 'harm', 'hiat', 'a', 'i', 'u']


def load_nel():
    langs = {}
    with open(NEL / 'languages.csv', encoding='utf-8') as f:
        for r in csv.DictReader(f):
            langs[r['ID']] = r
    words = defaultdict(set)
    with open(NEL / 'forms.csv', encoding='utf-8') as f:
        for r in csv.DictReader(f):
            words[r['Language_ID']].add(r['Segments'])
    out = {}
    for lid, segs in words.items():
        ws = [respell(s.split()) for s in segs]
        ws = [w for w in ws if w and len(w) >= 2]
        if len(ws) >= 300:
            out[lid] = {'name': langs[lid]['Name'], 'family': langs[lid]['Family'], 'lat': float(langs[lid]['Latitude']),
                        'lon': float(langs[lid]['Longitude']), 'n': len(ws), 'f': features(ws)}
    return out


NELF = load_nel()
LA_WORDS = [w for w in (la_syll(x) for x in ZB.LA_W) if w and len(w) >= 2]
LB_WORDS = [w for w in (la_syll(x) for x in D.LB_PLAIN) if w and len(w) >= 2]
LAF, LBF = features(LA_WORDS), features(LB_WORDS)
MU = {k: sum(v['f'][k] for v in NELF.values()) / len(NELF) for k in FEATS}
SD = {k: (sum((v['f'][k] - MU[k]) ** 2 for v in NELF.values()) / len(NELF)) ** 0.5 for k in FEATS}


def dist(f, g):
    return sqrt(sum(((f[k] - g[k]) / SD[k]) ** 2 for k in FEATS))


def nearest(f, k=10):
    return sorted(NELF, key=lambda l: dist(f, NELF[l]['f']))[:k]


def rank_p(value, key, higher):
    vals = [v['f'][key] for v in NELF.values()]
    beat = sum(1 for x in vals if (x >= value if higher else x <= value))
    return (beat + 1) / (len(vals) + 1), beat


def L0():
    near = nearest(LBF)
    rk = sorted(NELF, key=lambda l: dist(LBF, NELF[l]['f'])).index('ell') + 1 if 'ell' in NELF else None
    p = rk / (len(NELF) + 1) if rk else 1.0
    return p, 'Linear B finds Greek among its nearest languages', {'greek_rank': rk, 'of': len(NELF), 'p': round(p, 4)}, {'nearest10': [NELF[l]['name'] for l in near], 'LB_features': {k: round(v, 3) for k, v in LBF.items()}}


def L1():
    p, beat = rank_p(LAF['cor'], 'cor', True)
    return p, 'Linear A coronal e/o conditioning is extreme', {'LA_cor': round(LAF['cor'], 3), 'languages_as_high': beat, 'p': round(p, 4)}, {'top5': sorted(((round(v['f']['cor'], 2), v['name']) for v in NELF.values()), reverse=True)[:5]}


def L2():
    p, beat = rank_p(LAF['eo'], 'eo', False)
    return p, 'Linear A e/o share is extreme', {'LA_eo': round(LAF['eo'], 3), 'languages_as_low': beat, 'p': round(p, 4)}, {'lowest5': sorted((round(v['f']['eo'], 3), v['name']) for v in NELF.values())[:5]}


def L3():
    p, beat = rank_p(LAF['harm'], 'harm', True)
    return p, 'Linear A harmony is extreme', {'LA_harm': round(LAF['harm'], 3), 'languages_as_high': beat, 'p': round(p, 4)}, {'top5': sorted(((round(v['f']['harm'], 2), v['name']) for v in NELF.values()), reverse=True)[:5]}


def L4():
    near = nearest(LAF)
    ids = list(NELF)
    fams = [NELF[l]['family'] for l in ids]
    stat = lambda fm: Counter(f for l, f in zip(ids, fm) if l in near).most_common(1)[0][1]
    real = stat(fams)
    null = []
    for _ in range(R.REPS):
        f2 = list(fams)
        R.rng.shuffle(f2)
        null.append(stat(f2))
    p = R.pv_hi(null, real)
    return p, 'One family dominates Linear A\'s nearest languages', {'max_family_count': real, 'null': round(sum(null) / len(null), 2), 'p': round(p, 4)}, {'nearest10': [(NELF[l]['name'], NELF[l]['family'], round(dist(LAF, NELF[l]['f']), 2)) for l in near], 'LA_features': {k: round(v, 3) for k, v in LAF.items()}}


def gc(a, b):
    la1, lo1, la2, lo2 = map(radians, (a[0], a[1], b[0], b[1]))
    h = sin((la2 - la1) / 2) ** 2 + cos(la1) * cos(la2) * sin((lo2 - lo1) / 2) ** 2
    return 2 * 6371 * asin(sqrt(h))


def L5():
    ids = list(NELF)
    xs = [dist(LAF, NELF[l]['f']) for l in ids]
    ys = [gc(CRETE, (NELF[l]['lat'], NELF[l]['lon'])) for l in ids]
    real = B.spearman(xs, ys)
    null = []
    for _ in range(R.REPS):
        y2 = list(ys)
        R.rng.shuffle(y2)
        null.append(B.spearman(xs, y2))
    p = R.pv_hi(null, real)
    return p, 'Languages nearer Crete are nearer Linear A', {'spearman': round(real, 3), 'p': round(p, 4), 'languages': len(ids)}, {}


def L6():
    la_near, lb_near = set(nearest(LAF)), set(nearest(LBF))
    real = len(la_near & lb_near)
    null = []
    for _ in range(200):
        half = R.rng.sample(LB_WORDS, len(LB_WORDS) // 2)
        null.append(len(set(nearest(features(half))) & lb_near))
    p = (sum(1 for x in null if x <= real) + 1) / (len(null) + 1)
    return p, 'Linear A and Linear B have different nearest languages', {'overlap': real, 'lb_resample_overlap': round(sum(null) / len(null), 2), 'p': round(p, 4)}, {}


if __name__ == '__main__':
    print('languages', len(NELF), 'LA words', len(LA_WORDS), 'LB words', len(LB_WORDS))
    R.run('round68', 'the Z row, and Linear A\'s sound pattern among 107 languages', __doc__, [M1, L0, L1, L2, L3, L4, L5, L6])
