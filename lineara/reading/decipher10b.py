"""Ten more hypotheses aimed at reading Linear A, building on decipher10.py (the Linear B consonant rows behave
as sound classes in Linear A; the Z row does not; vowels are recoverable from context, consonants were not).

Each has a prediction stated before the test ran, one primary test with its own null, and a Linear B control
wherever the method can run on the deciphered script. Benjamini-Hochberg at 5% runs across the ten.

Z1  The special signs (PA3, RA2, PU2, TA2) sit nearest the consonant row their Linear B value gives them.
Z2  A better method (nearest neighbours on PPMI-weighted contexts) recovers a hidden sign's consonant row
    better than chance, where row centroids failed.
Z3  The Z signs (ZA, ZU) keep company with the dental and sibilant rows (S, T, D) more than with other rows.
Z4  Rows that share a place of articulation (labial P M W; dental T D N R S Z; velar K Q) have more similar
    signs than rows that do not, beyond the same-row effect.
Z5  O and U merged: within a consonant row, the o-sign's contexts are closer to the u-sign's than to the a-, e-
    and i-signs'.
Z6  E and I merged: within a row, the e-sign's contexts are closer to the i-sign's than to the a-, o- and u-signs'.
Z7  Words that differ in one internal sign differ by a close sound: the two signs share a consonant or a vowel
    more often than chance.
Z8  Vowel harmony: neighbouring syllables share their vowel more often than chance.
Z9  The Z2 method's predictions for the unread signs turn their words into Linear B words more often than random
    values.
Z10 Vowel signs stand inside words (after another sign) more often in Linear A than in Linear B, pointing to
    vowel sequences or diphthongs in Minoan.
"""
from collections import Counter, defaultdict
import json
from math import log, sqrt
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import batches as B  # noqa: E402
import decipher10 as D  # noqa: E402

ROOT = B.ROOT
rng = B.rng
REPS = B.REPS
out = D.out
out.clear()
record = D.record
grid = D.grid
LOGO = {'vin', 'arom', 'ole', 'gra', 'oliv', 'cyp', 'fic', 'vir', 'hide', 'cap', 'ovis', 'sus', 'bos', 'tela'}
LA_W = [w for w in D.LA_PLAIN if not any(x in LOGO for x in w)]
LA_ALL = [w for w in D.LA if not any(x in LOGO for x in w)]
LB_W = D.LB_PLAIN
SPECIAL_ROW = {'pa3': 'p', 'ra2': 'r', 'pu2': 'p', 'ta2': 't', 'a2': '', 'a3': '', 'au': '', 'ro2': 'r',
               'ra3': 'r', 'nwa': 'n', 'pte': 'p', 'dwe': 'd', 'dwo': 'd', 'twe': 't', 'two': 't'}


def ctx_vectors(words, min_n=8, ppmi=False):
    raw = D.contexts(words, min_n)
    if not ppmi:
        return {s: D.norm(c) for s, c in raw.items()}
    tot = sum(sum(c.values()) for c in raw.values())
    feat = Counter()
    for c in raw.values():
        feat.update(c)
    out_ = {}
    for s, c in raw.items():
        ns = sum(c.values())
        v = {f: max(0.0, log(x * tot / (ns * feat[f]))) for f, x in c.items()}
        out_[s] = {f: x for f, x in v.items() if x > 0}
    return out_


def row_rank(vecs, s, row, rows_from):
    cent = defaultdict(Counter)
    for t, v in vecs.items():
        if t != s and t in rows_from:
            for f, x in v.items():
                cent[rows_from[t]][f] += x
    order = sorted(cent, key=lambda r: -D.cos(vecs[s], dict(cent[r])))
    return order.index(row) + 1, len(order), order[:3]


# ------------------------------------------------------------------ Z1
def special_test(words):
    vecs = ctx_vectors(words, min_n=4)
    rows_from = {s: grid(s)[0] for s in vecs if grid(s)}
    res = {}
    for s, row in SPECIAL_ROW.items():
        if s in vecs:
            res[s] = row_rank(vecs, s, row, rows_from) + (row,)
    ranks = [(r, n) for r, n, _, _ in res.values()]
    real = sum(r / n for r, n in ranks) / len(ranks)
    null = [sum(rng.randint(1, n) / n for _, n in ranks) / len(ranks) for _ in range(20000)]
    p = (sum(x <= real for x in null) + 1) / (len(null) + 1)
    return real, p, {s: {'assigned': a or 'vowel', 'rank': r, 'of': n, 'nearest': [x or 'vowel' for x in top]} for s, (r, n, top, a) in res.items()}


def Z1():
    real, p, det = special_test(LA_W)
    lb_real, lb_p, lb_det = special_test(LB_W)
    record('Z1 special signs', 'PA3, RA2, PU2, TA2 sit nearest the row their Linear B value gives them',
           {'mean_relative_rank': round(real, 3), 'chance': 'about 0.54', 'p': round(p, 4), 'signs': det},
           {'Linear B control': {'mean_relative_rank': round(lb_real, 3), 'p': round(lb_p, 4), 'signs': lb_det}})
    return p


# ------------------------------------------------------------------ Z2, Z9
def knn_predict(vecs, s, labels, part, k=3):
    others = sorted((t for t in vecs if t != s and t in labels), key=lambda t: -D.cos(vecs[s], vecs[t]))[:k]
    votes = Counter(labels[t][part] for t in others)
    best = max(votes.values())
    tied = [x for x, n in votes.items() if n == best]
    return next(labels[t][part] for t in others if labels[t][part] in tied)


def knn_accuracy(words, labels=None, k=3):
    vecs = ctx_vectors(words, ppmi=True)
    signs = sorted(s for s in vecs if grid(s))
    labels = labels or {s: grid(s) for s in signs}
    acc = {}
    for part, name in ((0, 'cons'), (1, 'vow')):
        acc[name] = sum(knn_predict(vecs, s, labels, part, k) == labels[s][part] for s in signs) / len(signs)
    return acc, signs


def Z2():
    acc, signs = knn_accuracy(LA_W)
    labs = [grid(s) for s in signs]
    null = []
    for _ in range(300):
        rng.shuffle(labs)
        null.append(knn_accuracy(LA_W, dict(zip(signs, labs)))[0])
    pc = B.pv([n['cons'] for n in null], acc['cons'])
    pvw = B.pv([n['vow'] for n in null], acc['vow'])
    lb, lb_signs = knn_accuracy(LB_W)
    k1 = knn_accuracy(LA_W, k=1)[0]
    record('Z2 nearest-neighbour recovery', 'A hidden sign\'s consonant row is recovered from its nearest neighbours',
           {'consonant_accuracy': round(acc['cons'], 3), 'null_cons': round(sum(n['cons'] for n in null) / len(null), 3), 'p': round(pc, 4), 'signs': len(signs)},
           {'vowel_accuracy': round(acc['vow'], 3), 'null_vow': round(sum(n['vow'] for n in null) / len(null), 3), 'p_vow': round(pvw, 4),
            'k=1': {k: round(v, 3) for k, v in k1.items()},
            'Linear B control': {k: round(v, 3) for k, v in lb.items()}})
    return pc


def Z9():
    vecs = ctx_vectors(LA_ALL, min_n=2, ppmi=True)
    labels = {s: grid(s) for s in vecs if grid(s)}
    unread = Counter(x for w in LA_ALL for x in set(w) if D.UNREAD.match(x))
    values = sorted({s for w in LB_W for s in w if grid(s)})
    pred = {}
    for u, n in unread.items():
        if n >= 4 and u in vecs:
            c, v = knn_predict(vecs, u, labels, 0), knn_predict(vecs, u, labels, 1)
            pred[u] = c + v
    real = sum(len(D.lb_hits(u, val)) for u, val in pred.items())
    null = [sum(len(D.lb_hits(u, rng.choice(values))) for u in pred) for _ in range(REPS)]
    p = B.pv(null, real)
    record('Z9 unread signs by nearest neighbours', 'kNN-predicted values turn unread-sign words into Linear B words more than random values',
           {'matches': real, 'null_mean': round(sum(null) / len(null), 3), 'p': round(p, 4), 'signs': len(pred)},
           {'predictions': {u: {'value': v, 'lb_matches': D.lb_hits(u, v)} for u, v in pred.items()}})
    return p


# ------------------------------------------------------------------ Z3
DENTAL_SIB = {'s', 't', 'd'}


def z_affinity(words, zset):
    vecs = ctx_vectors(words)
    signs = [s for s in vecs if grid(s)]
    zs = [s for s in signs if grid(s)[0] == 'z']
    tgt = [s for s in signs if grid(s)[0] in DENTAL_SIB]
    rest = [s for s in signs if grid(s)[0] not in DENTAL_SIB | {'z'}]

    def stat(group):
        a = [D.cos(vecs[x], vecs[y]) for x in group for y in tgt]
        b = [D.cos(vecs[x], vecs[y]) for x in group for y in rest if y not in group]
        return sum(a) / len(a) - sum(b) / len(b)
    real = stat(zs)
    pool = rest
    null = []
    for _ in range(REPS):
        null.append(stat(rng.sample(pool, len(zs))))
    return real, B.pv(null, real), zs


def Z3():
    real, p, zs = z_affinity(LA_W, None)
    lb_real, lb_p, lb_zs = z_affinity(LB_W, None)
    record('Z3 Z row and dentals', 'ZA, ZU keep company with the S, T, D rows more than other signs do',
           {'diff': round(real, 4), 'p': round(p, 4), 'z_signs': zs},
           {'Linear B control (ZA, ZE, ZO)': {'diff': round(lb_real, 4), 'p': round(lb_p, 4), 'z_signs': lb_zs}})
    return p


# ------------------------------------------------------------------ Z4
PLACE = {'p': 'lab', 'm': 'lab', 'w': 'lab', 't': 'den', 'd': 'den', 'n': 'den', 'r': 'den', 's': 'den', 'z': 'den',
         'k': 'vel', 'q': 'vel'}


def place_test(words, reps):
    vecs = ctx_vectors(words)
    signs = [s for s in vecs if grid(s) and grid(s)[0] in PLACE]
    sims = [(grid(a)[0], grid(b)[0], D.cos(vecs[a], vecs[b])) for i, a in enumerate(signs) for b in signs[i + 1:]
            if grid(a)[0] != grid(b)[0]]
    rows = sorted({grid(s)[0] for s in signs})

    def stat(pl):
        same = [v for a, b, v in sims if pl[a] == pl[b]]
        diff = [v for a, b, v in sims if pl[a] != pl[b]]
        return sum(same) / len(same) - sum(diff) / len(diff)
    real = stat(PLACE)
    labs = [PLACE[r] for r in rows]
    null = []
    for _ in range(reps):
        rng.shuffle(labs)
        null.append(stat(dict(zip(rows, labs))))
    return real, B.pv(null, real)


def Z4():
    real, p = place_test(LA_W, REPS)
    lb_real, lb_p = place_test(LB_W, REPS)
    record('Z4 place of articulation', 'Rows sharing a place of articulation have more similar signs',
           {'diff': round(real, 4), 'p': round(p, 4)}, {'Linear B control': {'diff': round(lb_real, 4), 'p': round(lb_p, 4)}})
    return p


# ------------------------------------------------------------------ Z5, Z6
def merger(words, v1, v2, reps):
    vecs = ctx_vectors(words, min_n=4)
    rows = defaultdict(dict)
    for s in vecs:
        g = grid(s)
        if g and g[0] in PLACE:
            rows[g[0]][g[1]] = s
    usable = {r: d for r, d in rows.items() if v1 in d and v2 in d and len(d) >= 3}

    def stat(assign):
        vals = []
        for r, d in assign.items():
            s1, s2 = d[v1], d[v2]
            others = [d[v] for v in d if v not in (v1, v2)]
            vals.append(D.cos(vecs[s1], vecs[s2]) - sum(D.cos(vecs[s1], vecs[o]) for o in others) / len(others))
        return sum(vals) / len(vals)
    real = stat(usable)
    per_row = {r: stat({r: d}) for r, d in usable.items()}
    null = []
    for _ in range(reps):
        perm = {}
        for r, d in usable.items():
            vs = list(d)
            sg = [d[v] for v in vs]
            rng.shuffle(sg)
            perm[r] = dict(zip(vs, sg))
        null.append(stat(perm))
    return real, B.pv(null, real), per_row


def contrast(la_rows, lb_rows):
    a, b = list(la_rows.values()), list(lb_rows.values())
    real = sum(a) / len(a) - sum(b) / len(b)
    pool, k, null = a + b, len(a), []
    for _ in range(20000):
        rng.shuffle(pool)
        null.append(sum(pool[:k]) / k - sum(pool[k:]) / len(pool[k:]))
    return {'LA minus LB (per-row means)': round(real, 4), 'p (row-label permutation)': round(B.pv(null, real), 4),
            'LA rows': {k: round(v, 3) for k, v in la_rows.items()}, 'LB rows': {k: round(v, 3) for k, v in lb_rows.items()}}


def Z5():
    r, p, rows = merger(LA_W, 'o', 'u', REPS)
    lr, lp, lrows = merger(LB_W, 'o', 'u', REPS)
    record('Z5 o and u merged', 'Within a row the o-sign behaves like the u-sign',
           {'diff': round(r, 4), 'p': round(p, 4), 'rows': sorted(rows)},
           {'Linear B control': {'diff': round(lr, 4), 'p': round(lp, 4)}, 'Linear A against Linear B': contrast(rows, lrows)})
    return p


def Z6():
    r, p, rows = merger(LA_W, 'e', 'i', REPS)
    lr, lp, lrows = merger(LB_W, 'e', 'i', REPS)
    record('Z6 e and i merged', 'Within a row the e-sign behaves like the i-sign',
           {'diff': round(r, 4), 'p': round(p, 4), 'rows': sorted(rows)},
           {'Linear B control': {'diff': round(lr, 4), 'p': round(lp, 4)}, 'Linear A against Linear B': contrast(rows, lrows)})
    return p


# ------------------------------------------------------------------ Z7
def internal_pairs(words):
    ws = [w for w in words if len(w) >= 3]
    by = defaultdict(list)
    for w in ws:
        for i in range(len(w) - 1):
            by[(len(w), i, w[:i] + w[i + 1:])].append(w[i])
    pairs = []
    for (_, _, _), signs in by.items():
        signs = sorted(set(signs))
        pairs += [(a, b) for i, a in enumerate(signs) for b in signs[i + 1:] if grid(a) and grid(b)]
    return pairs


def close_share(pairs):
    return sum(grid(a)[0] == grid(b)[0] or grid(a)[1] == grid(b)[1] for a, b in pairs) / max(1, len(pairs))


def pair_null(words, pairs, reps):
    freq = Counter(x for w in words for x in w[:-1] if grid(x))
    pool = list(freq.elements())
    null = []
    for _ in range(reps):
        null.append(sum((lambda b: grid(a)[0] == grid(b)[0] or grid(a)[1] == grid(b)[1])(rng.choice([x for x in (rng.choice(pool),) if x != a] or [a]))
                        for a, _ in pairs) / max(1, len(pairs)))
    return null


def Z7():
    pairs = internal_pairs(LA_W)
    real = close_share(pairs)
    null = pair_null(LA_W, pairs, REPS)
    p = B.pv(null, real)
    lbp = internal_pairs(LB_W)
    lb_real = close_share(lbp)
    lb_null = pair_null(LB_W, lbp, 300)
    cons = sum(grid(a)[0] == grid(b)[0] for a, b in pairs) / max(1, len(pairs))
    vow = sum(grid(a)[1] == grid(b)[1] for a, b in pairs) / max(1, len(pairs))
    record('Z7 internal alternations', 'Words differing in one internal sign differ by a close sound (same consonant or vowel)',
           {'share_close': round(real, 3), 'null_mean': round(sum(null) / len(null), 3), 'p': round(p, 4), 'pairs': len(pairs)},
           {'same consonant': round(cons, 3), 'same vowel': round(vow, 3),
            'Linear B control': {'share_close': round(lb_real, 3), 'null_mean': round(sum(lb_null) / len(lb_null), 3),
                                 'p': round(B.pv(lb_null, lb_real), 4), 'pairs': len(lbp)}})
    return p


# ------------------------------------------------------------------ Z8
def harmony(words, reps):
    ws = [[x for x in w] for w in words if all(grid(x) for x in w)]
    stat = lambda wl: sum(grid(w[i])[1] == grid(w[i + 1])[1] for w in wl for i in range(len(w) - 1)) / sum(len(w) - 1 for w in wl)
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
    return real, B.pv(null, real), sum(null) / len(null)


def Z8():
    r, p, nm = harmony(LA_W, REPS)
    lr, lp, lnm = harmony(LB_W, 500)
    record('Z8 vowel harmony', 'Neighbouring syllables share their vowel more than chance',
           {'share_same_vowel': round(r, 4), 'null_mean': round(nm, 4), 'p': round(p, 4)},
           {'Linear B control': {'share': round(lr, 4), 'null_mean': round(lnm, 4), 'p': round(lp, 4)}})
    return p


# ------------------------------------------------------------------ Z10
def vowel_internal(words):
    occ = [(i > 0) for w in words for i, x in enumerate(w) if grid(x) and grid(x)[0] == '']
    return sum(occ) / len(occ), len(occ)


def Z10():
    la_r, la_n = vowel_internal(LA_W)
    lb_r, lb_n = vowel_internal(LB_W)
    real = la_r - lb_r
    pool = [(w, 0) for w in LA_W] + [(w, 1) for w in LB_W]
    labs = [l for _, l in pool]
    null = []
    for _ in range(REPS):
        rng.shuffle(labs)
        a = [w for (w, _), l in zip(pool, labs) if l == 0]
        b = [w for (w, _), l in zip(pool, labs) if l == 1]
        null.append(vowel_internal(a)[0] - vowel_internal(b)[0])
    p = B.pv(null, real)
    by_v = {v: (round(sum(1 for w in LA_W for i, x in enumerate(w) if x == v and i > 0) / max(1, sum(1 for w in LA_W for x in w if x == v)), 3),
                round(sum(1 for w in LB_W for i, x in enumerate(w) if x == v and i > 0) / max(1, sum(1 for w in LB_W for x in w if x == v)), 3))
            for v in 'aeiou'}
    prev = Counter(w[i - 1] for w in LA_W for i, x in enumerate(w) if i > 0 and x in ('i', 'u'))
    record('Z10 internal vowel signs', 'Vowel signs stand inside words more often in Linear A than in Linear B',
           {'LA_internal_share': round(la_r, 3), 'LB_internal_share': round(lb_r, 3), 'p': round(p, 4), 'occurrences': [la_n, lb_n]},
           {'by vowel (LA, LB)': by_v, 'signs before internal I/U in Linear A': dict(prev.most_common(8))})
    return p


def main():
    ps = {}
    for fn in (Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10):
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
    (ROOT / 'reading/decipher10b_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str) + '\n', encoding='utf-8')
    print('\nprimary p:', {k: round(v, 4) for k, v in ps.items()})
    print('survive BH at 5%:', supported)


if __name__ == '__main__':
    main()
