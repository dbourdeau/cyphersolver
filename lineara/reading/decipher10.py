"""Ten hypotheses aimed at reading Linear A: sound values, inflection, sign identities, and word meanings.

Each has a prediction stated before the test ran, one primary test with its own null, and robustness checks
(a Linear B positive control wherever the method can be run on the deciphered sister script). Benjamini-Hochberg
at 5% runs across the ten primary p-values.

Y1  Grid transfer: Linear A signs that share a Linear B consonant have more similar contexts (neighbouring signs)
    than signs that do not. Robustness: vowels; the same test on Linear B.
Y2  Kober's bridge: when two Linear A words differ only in their final sign, the two finals share a consonant
    more often than chance (inflection changes the vowel). Positive control: Linear B.
Y3  Paradigms: Linear A stems occur with two or more different final signs more often than when finals are
    reassigned at random. Positive control: Linear B.
Y4  Value recovery: with a known sign hidden, its consonant row and vowel column can be predicted from context
    alone (nearest row/column centroid) better than chance. Positive control: Linear B.
Y5  Values for unread signs: the grid positions predicted by the Y4 method for the unread Linear A signs (*301,
    *118, *21F ...) turn their words into attested Linear B words more often than random values do.
Y6  Shared undeciphered signs: Linear A words containing *34, *47, *49 or *86 share neighbouring syllables with
    Linear B words containing the same sign more than with Linear B words containing another of the four.
Y7  Acrophony: the syllable ligatured to a commodity sign (OLE+KI, GRA+PA, VIN+RA ...) is the first sign of a word
    on the same tablet more often than chance. Robustness: first sign against any other position.
Y8  Commodity words: more words are bound to a single commodity (co-occur on the same tablets) than chance allows.
Y9  Linear A words on tablets of a commodity resemble (syllable edit distance <= 1) Linear B words for the same
    commodity more often than chance.
Y10 A- is a prefix: pairs A-X / X are commoner than pairs formed by other initial signs, beyond chance.
"""
from collections import Counter, defaultdict
import json
from math import sqrt
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import batches as B  # noqa: E402

ROOT = B.ROOT
rng = B.rng
REPS = B.REPS
out = {}
GRID = re.compile(r'^([bcdfghjklmnpqrstvwxyz]?)([aeiou])$')
UNREAD = re.compile(r'^\*\d+[A-Za-z]?$')


def record(key, prediction, primary, robustness):
    out[key] = {'prediction': prediction, 'primary': primary, 'robustness': robustness}
    print(f"== {key}: {prediction}\n   primary {primary}\n   robustness {robustness}")


# ------------------------------------------------------------------ data
def la_words():
    """Linear A word types, syllables lower-case, unread signs kept as '*301' etc."""
    ws = set()
    for r in B.READ['records']:
        for t in r['tokens']:
            if t['cls'] not in ('word', 'word-with-unknown-sign', 'term'):
                continue
            parts = []
            for p in t['label'].split('-'):
                if re.fullmatch(r'[A-Z]+[0-9]?', p):
                    parts.append(p.lower())
                elif UNREAD.fullmatch(p):
                    parts.append(p.upper())
                else:
                    parts = None
                    break
            if parts and len(parts) >= 2:
                ws.add(tuple(parts))
    return sorted(ws)


LA = la_words()
LA_PLAIN = [w for w in LA if not any(UNREAD.match(x) for x in w)]
LB_ALL = sorted(w for w in B.LB_SITES if len(w) >= 2)
LB_PLAIN = [w for w in LB_ALL if not any(x.startswith('*') for x in w)]
LB_SET = set(LB_ALL)


def grid(s):
    m = GRID.match(s)
    return (m.group(1), m.group(2)) if m else None


def contexts(words, min_n=8):
    ctx = defaultdict(Counter)
    for w in words:
        seq = ('#',) + w + ('#',)
        for i in range(1, len(seq) - 1):
            ctx[seq[i]]['L:' + seq[i - 1]] += 1
            ctx[seq[i]]['R:' + seq[i + 1]] += 1
    return {s: c for s, c in ctx.items() if sum(c.values()) >= 2 * min_n}


def cos(a, b):
    num = sum(v * b.get(k, 0) for k, v in a.items())
    return num / (sqrt(sum(v * v for v in a.values())) * sqrt(sum(v * v for v in b.values())) or 1)


def norm(c):
    n = sum(c.values())
    return {k: v / n for k, v in c.items()}


# ------------------------------------------------------------------ Y1
def strip_harmony(ctx):
    """Drop context features whose neighbour shares the sign's own consonant (harmony, reduplication)."""
    out_ = {}
    for s, c in ctx.items():
        g = grid(s)
        keep = Counter({f: v for f, v in c.items() if not (grid(f[2:]) and grid(f[2:])[0] == g[0])})
        out_[s] = keep
    return out_


def site_words(pred):
    ws = set()
    for r in B.READ['records']:
        if not pred(r['site']):
            continue
        for t in r['tokens']:
            if t['cls'] in ('word', 'term'):
                w = tuple(x.lower() for x in t['label'].split('-'))
                if len(w) >= 2 and all(re.fullmatch(r'[a-z]+[0-9]?', x) for x in w):
                    ws.add(w)
    return sorted(ws)


def grid_similarity(words, part, harmony=True, min_n=8, no_vowel_row=False, no_boundary=False):
    raw = {s: c for s, c in contexts(words, min_n).items() if grid(s) and not (no_vowel_row and grid(s)[0] == '')}
    if no_boundary:
        raw = {s: Counter({f: v for f, v in c.items() if f[2:] != '#'}) for s, c in raw.items()}
    if not harmony:
        raw = strip_harmony(raw)
    ctx = {s: norm(c) for s, c in raw.items() if sum(c.values())}
    signs = sorted(ctx)
    lab = {s: grid(s)[0 if part == 'cons' else 1] for s in signs}
    sims = {(a, b): cos(ctx[a], ctx[b]) for i, a in enumerate(signs) for b in signs[i + 1:]}

    def stat(lb):
        same = [v for (a, b), v in sims.items() if lb[a] == lb[b]]
        diff = [v for (a, b), v in sims.items() if lb[a] != lb[b]]
        return sum(same) / len(same) - sum(diff) / len(diff)
    real = stat(lab)
    labels = [lab[s] for s in signs]
    null = []
    for _ in range(REPS):
        rng.shuffle(labels)
        null.append(stat(dict(zip(signs, labels))))
    return round(real, 4), B.pv(null, real), len(signs)


def Y1():
    c = grid_similarity(LA_PLAIN, 'cons')
    v = grid_similarity(LA_PLAIN, 'vow')
    lbc = grid_similarity(LB_PLAIN, 'cons')
    lbv = grid_similarity(LB_PLAIN, 'vow')
    nh = grid_similarity(LA_PLAIN, 'cons', harmony=False)
    lbnh = grid_similarity(LB_PLAIN, 'cons', harmony=False)
    nv = grid_similarity(LA_PLAIN, 'cons', no_vowel_row=True, no_boundary=True)
    lbnv = grid_similarity(LB_PLAIN, 'cons', no_vowel_row=True, no_boundary=True)
    ht = grid_similarity(site_words(lambda s: s == 'Haghia Triada'), 'cons', min_n=5)
    oth = grid_similarity(site_words(lambda s: s != 'Haghia Triada'), 'cons', min_n=5)
    record('Y1 grid transfer', 'Linear A signs sharing a Linear B consonant have more similar contexts',
           {'diff': c[0], 'p': round(c[1], 4), 'signs': c[2]},
           {'Linear A vowels': {'diff': v[0], 'p': round(v[1], 4)},
            'Linear B consonants (control)': {'diff': lbc[0], 'p': round(lbc[1], 4), 'signs': lbc[2]},
            'Linear B vowels (control)': {'diff': lbv[0], 'p': round(lbv[1], 4)},
            'Linear A consonants, same-consonant neighbours removed': {'diff': nh[0], 'p': round(nh[1], 4)},
            'Linear B consonants, same-consonant neighbours removed': {'diff': lbnh[0], 'p': round(lbnh[1], 4)},
            'Linear A, vowel row and word-boundary features removed': {'diff': nv[0], 'p': round(nv[1], 4), 'signs': nv[2]},
            'Linear B, vowel row and word-boundary features removed': {'diff': lbnv[0], 'p': round(lbnv[1], 4)},
            'Haghia Triada words only': {'diff': ht[0], 'p': round(ht[1], 4), 'signs': ht[2]},
            'other sites only': {'diff': oth[0], 'p': round(oth[1], 4), 'signs': oth[2]}})
    return c[1]


# ------------------------------------------------------------------ Y2, Y3
def finals_stats(words):
    ws = [w for w in words if len(w) >= 3 and grid(w[-1])]
    by = defaultdict(set)
    for w in ws:
        by[w[:-1]].add(w[-1])
    pairs = [(a, b) for fs in by.values() for i, a in enumerate(sorted(fs)) for b in sorted(fs)[i + 1:]]
    stems_multi = sum(1 for fs in by.values() if len(fs) >= 2)
    share_c = sum(grid(a)[0] == grid(b)[0] for a, b in pairs) / max(1, len(pairs))
    share_v = sum(grid(a)[1] == grid(b)[1] for a, b in pairs) / max(1, len(pairs))
    return stems_multi, share_c, share_v, len(pairs)


def finals_null(words, reps):
    ws = [w for w in words if len(w) >= 3 and grid(w[-1])]
    stems = [w[:-1] for w in ws]
    fins = [w[-1] for w in ws]
    res = []
    for _ in range(reps):
        rng.shuffle(fins)
        res.append(finals_stats([s + (f,) for s, f in zip(stems, fins)]))
    return res


def Y2_Y3():
    real = finals_stats(LA)
    null = finals_null(LA, REPS)
    lb_real = finals_stats(LB_ALL)
    lb_null = finals_null(LB_ALL, 500)
    p2 = B.pv([n[1] for n in null], real[1])
    p3 = B.pv([n[0] for n in null], real[0])
    mean = lambda k, xs: round(sum(x[k] for x in xs) / len(xs), 4)
    record('Y2 Kober bridge', 'Alternating finals on the same stem share a consonant more than chance',
           {'share_same_consonant': round(real[1], 4), 'null_mean': mean(1, null), 'p': round(p2, 4), 'pairs': real[3]},
           {'share_same_vowel': round(real[2], 4), 'null_vowel': mean(2, null),
            'Linear B control': {'share_same_consonant': round(lb_real[1], 4), 'null_mean': mean(1, lb_null),
                                 'p': round(B.pv([n[1] for n in lb_null], lb_real[1]), 4), 'pairs': lb_real[3]}})
    record('Y3 paradigms', 'Stems take two or more different finals more often than with finals reassigned',
           {'stems_with_2plus_finals': real[0], 'null_mean': mean(0, null), 'p': round(p3, 4)},
           {'Linear B control': {'stems': lb_real[0], 'null_mean': mean(0, lb_null),
                                 'p': round(B.pv([n[0] for n in lb_null], lb_real[0]), 4)}})
    return p2, p3


# ------------------------------------------------------------------ Y4
def loo_accuracy(words, labels_override=None):
    ctx = {s: norm(c) for s, c in contexts(words).items() if grid(s)}
    signs = sorted(ctx)
    lab = labels_override or {s: grid(s) for s in signs}
    hits = {'cons': 0, 'vow': 0}
    for s in signs:
        for k, part in (('cons', 0), ('vow', 1)):
            groups = defaultdict(Counter)
            for t in signs:
                if t != s:
                    for f, v in ctx[t].items():
                        groups[lab[t][part]][f] += v
            best = max(groups, key=lambda g: cos(ctx[s], norm(groups[g])))
            hits[k] += best == lab[s][part]
    return {k: v / len(signs) for k, v in hits.items()}, signs


def Y4():
    acc, signs = loo_accuracy(LA_PLAIN)
    labels = [grid(s) for s in signs]
    null = []
    for _ in range(200):
        rng.shuffle(labels)
        null.append(loo_accuracy(LA_PLAIN, dict(zip(signs, labels)))[0])
    pc = B.pv([n['cons'] for n in null], acc['cons'])
    pv_ = B.pv([n['vow'] for n in null], acc['vow'])
    p = min(1.0, 2 * min(pc, pv_))  # Bonferroni over the two parts
    lb_acc, lb_signs = loo_accuracy(LB_PLAIN)
    record('Y4 value recovery', 'A hidden sign\'s consonant row or vowel column is predicted from context better than chance',
           {'consonant_accuracy': round(acc['cons'], 3), 'null_cons': round(sum(n['cons'] for n in null) / len(null), 3), 'p_cons': round(pc, 4),
            'vowel_accuracy': round(acc['vow'], 3), 'null_vow': round(sum(n['vow'] for n in null) / len(null), 3), 'p_vow': round(pv_, 4),
            'p (Bonferroni over the two)': round(p, 4), 'signs': len(signs)},
           {'Linear B control': {'consonant_accuracy': round(lb_acc['cons'], 3), 'vowel_accuracy': round(lb_acc['vow'], 3), 'signs': len(lb_signs)}})
    return p


# ------------------------------------------------------------------ Y5
def predict_unread(min_types=4):
    allw = LA
    ctx_all = {s: norm(c) for s, c in contexts(allw, min_n=min_types // 2 or 1).items()}
    known = {s: grid(s) for s in ctx_all if grid(s)}
    rows, cols = defaultdict(Counter), defaultdict(Counter)
    for s, (c, v) in known.items():
        for f, x in ctx_all[s].items():
            rows[c][f] += x
            cols[v][f] += x
    unread = Counter(x for w in LA for x in set(w) if UNREAD.match(x))
    pred = {}
    for u, n in unread.items():
        if n < min_types or u not in ctx_all:
            continue
        rc = sorted(rows, key=lambda g: -cos(ctx_all[u], norm(rows[g])))
        vc = sorted(cols, key=lambda g: -cos(ctx_all[u], norm(cols[g])))
        pred[u] = {'types': n, 'consonant_ranked': rc[:3], 'vowel_ranked': vc[:3], 'value': rc[0] + vc[0]}
    return pred


def lb_hits(u, value):
    hits = []
    for w in LA:
        if u in w:
            cand = tuple(value if x == u else x for x in w)
            if not any(UNREAD.match(x) for x in cand) and cand in LB_SET:
                hits.append('-'.join(cand))
    return hits


def Y5():
    pred = predict_unread()
    values = sorted({s for w in LB_PLAIN for s in w if grid(s)})
    real = sum(len(lb_hits(u, d['value'])) for u, d in pred.items())
    null = []
    for _ in range(REPS):
        null.append(sum(len(lb_hits(u, rng.choice(values))) for u in pred))
    p = B.pv(null, real)
    detail = {u: {**d, 'lb_matches': lb_hits(u, d['value'])} for u, d in pred.items()}
    # exploratory, not tested: the value giving most Linear B matches for each sign
    best = {}
    for u in pred:
        sc = sorted(((len(lb_hits(u, v)), v) for v in values), reverse=True)[:3]
        best[u] = [(v, n, lb_hits(u, v)) for n, v in sc if n]
    record('Y5 values for unread signs', 'Context-predicted values turn unread-sign words into Linear B words more than random values',
           {'matches': real, 'null_mean': round(sum(null) / len(null), 3), 'p': round(p, 4), 'signs': len(pred)},
           {'predictions': detail, 'exploratory best-match values (not a test)': best})
    return p


# ------------------------------------------------------------------ Y6
SHARED = ('*34', '*47', '*49', '*86')


def neighbours(w, s):
    out_ = set()
    for i, x in enumerate(w):
        if x == s:
            if i > 0:
                out_.add(('L', w[i - 1]))
            if i < len(w) - 1:
                out_.add(('R', w[i + 1]))
    return out_


def Y6():
    la = {s: [w for w in LA if s in w] for s in SHARED}
    lb_words = [w for w in LB_ALL if any(x in SHARED for x in w)]
    lb_sign = [next(x for x in w if x in SHARED) for w in lb_words]

    def stat(signs_of_lb):
        by = defaultdict(set)
        for w, s in zip(lb_words, signs_of_lb):
            by[s] |= neighbours(w, s)
        same = sum(len(neighbours(w, s) & by[s]) > 0 for s in SHARED for w in la[s])
        return same
    real = stat(lb_sign)
    labels = lb_sign[:]
    null = []
    for _ in range(REPS):
        rng.shuffle(labels)
        null.append(stat(labels))
    p = B.pv(null, real)
    exact = [('-'.join(w)) for s in SHARED for w in la[s] if w in LB_SET]
    shared_ctx = {s: sorted('-'.join(n) for n in set().union(*(neighbours(w, s) for w in la[s])) &
                            set().union(*(neighbours(w, s) for w, t in zip(lb_words, lb_sign) if t == s))) for s in SHARED if la[s]}
    record('Y6 shared undeciphered signs', 'Linear A words with *34/*47/*49/*86 share neighbours with Linear B words holding the same sign',
           {'la_words_with_shared_neighbour': real, 'null_mean': round(sum(null) / len(null), 3), 'p': round(p, 4),
            'la_words': {s: len(la[s]) for s in SHARED}, 'lb_words': dict(Counter(lb_sign))},
           {'exact word matches': exact, 'shared neighbours by sign': shared_ctx})
    return p


# ------------------------------------------------------------------ Y7
FRACTION_LETTERS = {'A', 'B', 'D', 'E', 'F', 'H', 'J', 'K', 'L', 'L2', 'L3', 'L4', 'L6'}


def Y7():
    items = []
    for r in B.READ['records']:
        words = [tuple(x.lower() for x in t['label'].split('-')) for t in r['tokens'] if t['cls'] in ('word', 'term')]
        for t in r['tokens']:
            if t['cls'] != 'commodity' or '+' not in t['label']:
                continue
            base, *rest = t['label'].split('-')[-1].split('+')
            for syl in rest:
                if syl in FRACTION_LETTERS or not re.fullmatch(r'[A-Z]{1,2}[0-9]?', syl):
                    continue
                items.append((syl.lower(), words))
    first = lambda s, ws: any(w and w[0] == s for w in ws)
    other = lambda s, ws: any(s in w[1:] for w in ws)
    real = sum(first(s, ws) for s, ws in items)
    syls = [s for s, _ in items]
    null = []
    for _ in range(REPS):
        rng.shuffle(syls)
        null.append(sum(first(s, ws) for s, (_, ws) in zip(syls, items)))
    p = B.pv(null, real)
    real_o = sum(other(s, ws) for s, ws in items)
    null_o = []
    syls2 = [s for s, _ in items]
    for _ in range(REPS):
        rng.shuffle(syls2)
        null_o.append(sum(other(s, ws) for s, (_, ws) in zip(syls2, items)))
    examples = Counter((s, '-'.join(w).upper()) for s, ws in items for w in ws if w and w[0] == s)
    record('Y7 acrophony', 'The ligatured syllable begins a word on the same tablet more often than chance',
           {'ligatures_with_matching_first_sign': f'{real}/{len(items)}', 'null_mean': round(sum(null) / len(null), 2), 'p': round(p, 4)},
           {'same syllable in a non-initial position': {'real': real_o, 'null_mean': round(sum(null_o) / len(null_o), 2), 'p': round(B.pv(null_o, real_o), 4)},
            'examples': [f'{s.upper()}: {w} x{n}' for (s, w), n in examples.most_common(15)]})
    return p


# ------------------------------------------------------------------ Y8, Y9
def record_sets():
    recs = []
    for r in B.READ['records']:
        com = {re.findall(r'[A-Z]{3,}', t['label'])[0] for t in r['tokens']
               if t['cls'] == 'commodity' and re.findall(r'[A-Z]{3,}', t['label'])}
        words = {t['label'] for t in r['tokens'] if t['cls'] in ('word', 'term', 'word-with-unknown-sign')}
        if com and words:
            recs.append((words, com))
    return recs


def bound_pairs(recs, thresh=0.01):
    from math import comb
    n = len(recs)
    wc, cc, co = Counter(), Counter(), Counter()
    for ws, cs in recs:
        wc.update(ws)
        cc.update(cs)
        for w in ws:
            for c in cs:
                co[(w, c)] += 1
    sig = []
    for (w, c), k in co.items():
        if wc[w] < 3 or k < 2:
            continue
        K, N_, m = cc[c], n, wc[w]
        p = sum(comb(K, i) * comb(N_ - K, m - i) for i in range(k, min(K, m) + 1)) / comb(N_, m)
        if p < thresh:
            sig.append((w, c, k, m, round(p, 5)))
    return sig


def Y8():
    recs = record_sets()
    real = bound_pairs(recs)
    coms = [c for _, c in recs]
    null = []
    for _ in range(300):
        rng.shuffle(coms)
        null.append(len(bound_pairs([(w, c) for (w, _), c in zip(recs, coms)])))
    p = B.pv(null, len(real))
    record('Y8 commodity words', 'More words are bound to one commodity than chance allows',
           {'bound_pairs_p<0.01': len(real), 'null_mean': round(sum(null) / len(null), 2), 'p': round(p, 4), 'tablets': len(recs)},
           {'pairs (word, commodity, tablets together, tablets with word, p)': sorted(real, key=lambda x: x[4])})
    return p


COMMODITY_WORDS = {'CYP': ('cyperus',), 'VIN': ('wine',), 'OLE': ('olive oil', ' oil'), 'OLIV': ('olive',),
                   'FIC': ('fig',), 'GRA': ('barley', 'wheat', 'grain'), 'CAP': ('goat',), 'OVIS': ('sheep', 'ram', 'ewe'),
                   'SUS': ('pig', 'swine'), 'BOS': ('ox', 'cattle', 'cow', 'bull'), 'TELA': ('cloth', 'linen'),
                   'HIDE': ('hide', 'leather')}


def ed(a, b):
    d = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        prev, d[0] = d[0], i
        for j, y in enumerate(b, 1):
            prev, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, prev + (x != y))
    return d[-1]


def Y9():
    lex = json.loads((ROOT / 'data/linearb/tiripode_lexicon.json').read_text(encoding='utf-8'))
    lbc = defaultdict(set)
    for k, v in lex.items():
        d = ' ' + v['definition'].lower()
        for c, keys in COMMODITY_WORDS.items():
            if any(re.search(r'\b' + re.escape(x.strip()) + r'\b', d) for x in keys):
                lbc[c].add(tuple(k.lower().split('-')))
    recs = [({tuple(w.lower().split('-')) for w in ws if re.fullmatch(r'[A-Z0-9-]+', w)}, cs) for ws, cs in record_sets()]

    def count(recs_):
        hits = set()
        for ws, cs in recs_:
            for c in cs:
                for w in ws:
                    if len(w) >= 2:
                        for x in lbc.get(c, ()):
                            if len(x) >= 2 and ed(w, x) <= (0 if min(len(w), len(x)) < 3 else 1):
                                hits.add(('-'.join(w).upper(), c, '-'.join(x)))
        return hits
    real = count(recs)
    coms = [c for _, c in recs]
    null = []
    for _ in range(REPS // 4):
        rng.shuffle(coms)
        null.append(len(count([(w, c) for (w, _), c in zip(recs, coms)])))
    p = B.pv(null, len(real))
    record('Y9 commodity words in Linear B', 'Linear A words on a commodity\'s tablets resemble the Linear B words for it',
           {'matches': len(real), 'null_mean': round(sum(null) / len(null), 2), 'p': round(p, 4)},
           {'matches': sorted(real), 'Linear B commodity words per logogram': {c: len(v) for c, v in lbc.items()}})
    return p


# ------------------------------------------------------------------ Y10
def prefix_pairs(words, s):
    ws = set(words)
    return sum(1 for w in ws if len(w) >= 3 and w[0] == s and w[1:] in ws)


def Y10():
    words = LA_PLAIN
    real = prefix_pairs(words, 'a')
    long_ = [w for w in words if len(w) >= 3]
    short = [w for w in words if len(w) < 3]
    heads = [w[0] for w in long_]
    null = []
    for _ in range(REPS):
        rng.shuffle(heads)
        null.append(prefix_pairs(short + [(h,) + w[1:] for h, w in zip(heads, long_)], 'a'))
    p = B.pv(null, real)
    others = {}
    for s in ('i', 'u', 'ja', 'e', 'o'):
        r_ = prefix_pairs(words, s)
        nl = []
        for _ in range(500):
            rng.shuffle(heads)
            nl.append(prefix_pairs(short + [(h,) + w[1:] for h, w in zip(heads, long_)], s))
        others[s.upper() + '-'] = {'pairs': r_, 'null_mean': round(sum(nl) / len(nl), 2), 'p': round(B.pv(nl, r_), 4)}
    ex = sorted('-'.join(w).upper() for w in set(words) if len(w) >= 3 and w[0] == 'a' and w[1:] in set(words))
    record('Y10 A- prefix', 'Pairs A-X / X are commoner than chance',
           {'pairs': real, 'null_mean': round(sum(null) / len(null), 2), 'p': round(p, 4)},
           {'other initial signs': others, 'A- pairs': ex})
    return p


def main():
    ps = {}
    for name, fn in (('Y1', Y1), ('Y2_Y3', Y2_Y3), ('Y4', Y4), ('Y5', Y5), ('Y6', Y6), ('Y7', Y7), ('Y8', Y8), ('Y9', Y9), ('Y10', Y10)):
        try:
            r = fn()
            if name == 'Y2_Y3':
                ps['Y2'], ps['Y3'] = r
            else:
                ps[name] = r
        except Exception as ex:
            import traceback
            traceback.print_exc()
            out[name] = {'error': str(ex)}
    tested = sorted([(p, k) for k, p in ps.items() if p is not None])
    m, cut = len(tested), 0
    for i, (p, k) in enumerate(tested, 1):
        if p <= 0.05 * i / m:
            cut = i
    supported = [k for _, k in tested[:cut]]
    res = {'method': __doc__.strip(), 'primary_p': ps, 'bh_supported': supported, 'details': out}
    (ROOT / 'reading/decipher10_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str) + '\n', encoding='utf-8')
    print('\nprimary p:', {k: round(v, 4) for k, v in ps.items()})
    print('survive BH at 5%:', supported)


if __name__ == '__main__':
    main()
