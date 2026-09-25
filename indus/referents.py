"""The picture-referent method with its criteria as parameters (sets 233, 237, 243, 254; loop 112 on).

A unit (a whole text, or an adjacent sign pair) qualifies when it stands on k or more pictured objects of one pool, in 2
or more distinct texts (pairs; part-texts merged), with one picture on a share s or more of them. Pools: individually
made tablets (TAB:C, TAB:I) and moulded tablets (TAB:B), each with the pictured damaged tablets' legible runs (no pair
across a gap). coverage() is prizebench.referent_fixed's measure; with k = 3, s = 0.8 it reproduces it.
"""
import random
from collections import Counter, defaultdict

import rtools as R
from predict_test200 import objects
from predict_test237 import merged
from predict_test254 import frag_objects

POOLS = {'made': ('TAB:C', 'TAB:I'), 'moulded': ('TAB:B',)}


def ok(ms, k, s):
    if len(ms) < k:
        return None
    m, v = Counter(ms).most_common(1)[0]
    return m if v / len(ms) >= s else None


def q_texts(objs, k, s):
    g = defaultdict(list)
    for t, m in objs:
        g[t].append(m)
    return {t: m for t, ms in g.items() for m in [ok(ms, k, s)] if m}


def q_pairs(objs, k, s, n=2):
    occ, texts = defaultdict(list), defaultdict(set)
    for t, m in objs:
        for p in {t[i:i + n] for i in range(len(t) - n + 1)}:
            if '|' in p:
                continue
            occ[p].append(m)
            texts[p].add(t)
    return {p: m for p, ms in occ.items() if len(texts[p]) >= 2 for m in [ok(ms, k, s)] if m}


def pools(F, recs):
    out = {}
    for lab, types in POOLS.items():
        clean = objects(F, recs, types)
        out[lab] = (clean, merged(clean + frag_objects(types)))
    return out


def units(P, k, s, ns=(2,)):
    """{'texts': qualifying whole texts of the individually made pool, (lab, n): qualifying n-sign runs per pool}.
    ns = (2,) is the pair method of sets 237-287; set 288 tests adding 1 and 3."""
    out = {'texts': q_texts(P['made'][0], k, s)}
    for lab, (clean, both) in P.items():
        for n in ns:
            out[(lab, n)] = q_pairs(both, k, s, n)
    return out


def count(u):
    return sum(len(v) for v in u.values())


def coverage(DL, P, u):
    used = {lab: {t for t, m in P[lab][0]} for lab in P}
    cov = 0
    for t in DL:
        if t in u['texts']:
            cov += len(t)
            continue
        mark = set()
        for key, qq in u.items():
            if key == 'texts' or t not in used[key[0]]:
                continue
            n = key[1]
            for i in range(len(t) - n + 1):
                if t[i:i + n] in qq:
                    mark |= set(range(i, i + n))
        cov += len(mark)
    return cov / sum(len(t) for t in DL)


def null_count(P, k, s, n=100, seed=287, ns=(2,)):
    """Mean number of qualifying units with pictures shuffled among the objects of each pool."""
    rnd = random.Random(seed)
    tot = 0
    for _ in range(n):
        Q = {}
        for lab, (clean, both) in P.items():
            pics = [m for t, m in both]
            rnd.shuffle(pics)
            sh = list(zip([t for t, m in both], pics))
            cp = [m for t, m in clean]
            rnd.shuffle(cp)
            Q[lab] = (list(zip([t for t, m in clean], cp)), sh)
        tot += count(units(Q, k, s, ns))
    return tot / n
