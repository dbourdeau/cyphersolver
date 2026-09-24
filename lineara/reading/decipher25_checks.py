"""Robustness checks for the five survivors of decipher25.py (D1, D8, D13, D20, D22), added after the first run."""
from collections import Counter, defaultdict
import json
from math import log
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import decipher25 as T  # noqa: E402

B, D, V, E = T.B, T.D, T.V, T.E
grid, rng = T.grid, T.rng
res = {}

# D1: word-internal syllables only
internal = lambda ws: [w[:-1] for w in ws if len(w) >= 2]
r, p, nm = T.label_perm(lambda x, y: T.log_or(internal(x)) - T.log_or(internal(y)), T.LA, T.LB)
res['D1 internal only'] = {'logOR_LA': round(T.log_or(internal(T.LA)), 3), 'logOR_LB': round(T.log_or(internal(T.LB)), 3), 'p': round(p, 4)}
res['D1 e/o share after coronals vs non-coronals (LA)'] = {
    k: round(sum(1 for w in T.LA for x in w if grid(x) and grid(x)[0] in S and grid(x)[1] in T.RARE) /
             sum(1 for w in T.LA for x in w if grid(x) and grid(x)[0] in S), 3) for k, S in (('coronal', T.COR), ('non-coronal', T.NONCOR))}

# D8: every consonant pair, observed against frequency-expected
pairs = T.cons_pairs(T.LA)
cf = Counter(grid(x)[0] for w in T.LA for x in w if grid(x) and grid(x)[0])
tot = sum(cf.values())
exp = Counter()
for a, _ in pairs:
    denom = tot - cf[a]
    for c, n in cf.items():
        if c != a:
            exp[frozenset((a, c))] += n / denom
obs = Counter(frozenset(p_) for p_ in pairs)
ratio = sorted(((obs[k] / exp[k], ''.join(sorted(k)), obs[k], round(exp[k], 1)) for k in obs if exp[k] >= 1), reverse=True)
res['D8 consonant pairs ranked by observed/expected'] = [(n, round(r_, 2), o, e) for r_, n, o, e in ratio[:10]]
st_rank = [n for _, n, _, _ in ratio].index('st') + 1
res['D8 rank of s/t among pairs with expected >= 1'] = f'{st_rank} of {len(ratio)}'
idx = defaultdict(list)
for w in T.LA:
    for i in range(len(w)):
        idx[(len(w), i, w[:i] + w[i + 1:])].append(w)
st_words = sorted({' / '.join(sorted('-'.join(x).upper() for x in ws)) for k, ws in idx.items() if len(ws) >= 2 and
                   {grid(x[k[1]])[0] for x in ws if grid(x[k[1]])} >= {'s', 't'}})
res['D8 s/t word pairs'] = st_words

# D13: final syllable removed (women's names end in -a), and MUL names against VIR-tablet names
a, b = T.names_by(lambda logos, words: 'MUL' in logos)
stem_score = lambda w: T.minoan(w[:-1]) if len(w) >= 2 else T.minoan(w)
r, p, nm = T.label_perm(lambda x, y: V.auc([stem_score(w) for w in x], [stem_score(w) for w in y]), a, b)
res['D13 final syllable removed'] = {'auc': round(r, 3), 'p': round(p, 4)}
va, _ = T.names_by(lambda logos, words: 'VIR' in logos and 'MUL' not in logos)
va = [w for w in va if w not in a]
r, p, nm = T.label_perm(lambda x, y: V.auc([T.minoan(w) for w in x], [T.minoan(w) for w in y]), a, va)
res['D13 MUL names against VIR-only names'] = {'auc': round(r, 3), 'p': round(p, 4), 'n': [len(a), len(va)]}
res['D13 share of MUL names ending in -a'] = round(sum(grid(w[-1]) is not None and grid(w[-1])[1] == 'a' for w in a) / len(a), 3)
res['D13 share of other names ending in -a'] = round(sum(grid(w[-1]) is not None and grid(w[-1])[1] == 'a' for w in b) / len(b), 3)

# D20, D22: without transaction terms; Haghia Triada only; which tablets carry the teams
TERMS = {'SA-RA2', 'A-DU', 'KA-PA', 'DA-RE', 'KU-PA', 'SA-MA', 'KU-RO', 'KI-RO', 'PO-TO-KU-RO', 'KU-NI-SU'}
rows = [r_ for r_ in T.entry_rows() if r_[0] not in TERMS]
occ = defaultdict(set)
for w, c, q, rec in rows:
    occ[w].add(rec)
occ = {w: rs for w, rs in occ.items() if len(rs) >= 2}


def same_scribe(sc, oc):
    pr = [(a, b) for rs in oc.values() for i, a in enumerate(sorted(rs)) for b in sorted(rs)[i + 1:] if a in sc and b in sc]
    return sum(sc[a] == sc[b] for a, b in pr) / max(1, len(pr)), len(pr)


for label, keep in (('without transaction terms', lambda rec: True),
                    ('without terms, Haghia Triada only', lambda rec: rec.startswith('HT'))):
    oc = {w: {r_ for r_ in rs if keep(r_)} for w, rs in occ.items()}
    oc = {w: rs for w, rs in oc.items() if len(rs) >= 2}
    recs = sorted({r_ for rs in oc.values() for r_ in rs if T.SCRIBE.get(r_)})
    sc = {r_: T.SCRIBE[r_] for r_ in recs}
    real, npair = same_scribe(sc, oc)
    labs = [sc[r_] for r_ in recs]
    null = []
    for _ in range(1000):
        rng.shuffle(labs)
        null.append(same_scribe(dict(zip(recs, labs)), oc)[0])
    res[f'D20 {label}'] = {'share': round(real, 3), 'null_mean': round(sum(null) / len(null), 3), 'p': round(B.pv(null, real), 4), 'pairs': npair}

tab_words = defaultdict(set)
for w, c, q, rec in rows:
    tab_words[rec].add(w)
pc = defaultdict(set)
for t, ws in tab_words.items():
    ws = sorted(w for w in ws if w in occ)
    for i, x in enumerate(ws):
        for y in ws[i + 1:]:
            pc[(x, y)].add(t)
teams = {k: v for k, v in pc.items() if len(v) >= 2}
res['D22 without terms: pairs on 2+ tablets'] = len(teams)
res['D22 tablet sets carrying the teams'] = dict(Counter(' + '.join(sorted(v)) for v in teams.values()).most_common(10))
slots = [(t, w) for t in tab_words for w in tab_words[t]]
ws_ = [w for _, w in slots]
null = []
for _ in range(1000):
    rng.shuffle(ws_)
    tw = defaultdict(set)
    for (t, _), w in zip(slots, ws_):
        tw[t].add(w)
    cnt = Counter()
    for t, s in tw.items():
        s = sorted(x for x in s if x in occ)
        for i, x in enumerate(s):
            for y in s[i + 1:]:
                cnt[(x, y)] += 1
    null.append(sum(1 for v in cnt.values() if v >= 2))
res['D22 without terms p'] = round(B.pv(null, len(teams)), 4)
res['D22 null mean'] = round(sum(null) / len(null), 2)

(T.ROOT / 'reading/decipher25_checks.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for k, v in res.items():
    print(k, ':', v)

# Sides merged: HT9a and HT9b are one tablet. Rerun D20 and D22 on whole tablets, and s/t on words of 3+ signs.
import re as _re
whole = lambda rec: _re.sub(r'(?<=\d)[ab]$', '', rec)
res2 = {}
occ_w = defaultdict(set)
for w, c, q, rec in rows:
    occ_w[w].add(whole(rec))
occ_w = {w: rs for w, rs in occ_w.items() if len(rs) >= 2}
sc_w = {}
for rec, s in T.SCRIBE.items():
    if s:
        sc_w.setdefault(whole(rec), s)
recs = sorted({r_ for rs in occ_w.values() for r_ in rs if r_ in sc_w})
sc = {r_: sc_w[r_] for r_ in recs}
real, npair = same_scribe(sc, occ_w)
labs = [sc[r_] for r_ in recs]
null = []
for _ in range(1000):
    rng.shuffle(labs)
    null.append(same_scribe(dict(zip(recs, labs)), occ_w)[0])
res2['D20 sides merged, without terms'] = {'share': round(real, 3), 'null_mean': round(sum(null) / len(null), 3),
                                           'p': round(B.pv(null, real), 4), 'pairs': npair}
tw_w = defaultdict(set)
for w, c, q, rec in rows:
    tw_w[whole(rec)].add(w)
pc = defaultdict(set)
for t, ws in tw_w.items():
    ws = sorted(w for w in ws if w in occ_w)
    for i, x in enumerate(ws):
        for y in ws[i + 1:]:
            pc[(x, y)].add(t)
teams = {k: v for k, v in pc.items() if len(v) >= 2}
slots = [(t, w) for t in tw_w for w in tw_w[t]]
ws_ = [w for _, w in slots]
null = []
for _ in range(1000):
    rng.shuffle(ws_)
    tw = defaultdict(set)
    for (t, _), w in zip(slots, ws_):
        tw[t].add(w)
    cnt = Counter()
    for t, s in tw.items():
        s = sorted(x for x in s if x in occ_w)
        for i, x in enumerate(s):
            for y in s[i + 1:]:
                cnt[(x, y)] += 1
    null.append(sum(1 for v in cnt.values() if v >= 2))
res2['D22 sides merged, without terms'] = {'pairs': len(teams), 'null_mean': round(sum(null) / len(null), 2), 'p': round(B.pv(null, len(teams)), 4),
                                           'tablet sets': dict(Counter(' + '.join(sorted(v)) for v in teams.values()))}
long3 = [w for w in T.LA if len(w) >= 3]
pairs3 = T.cons_pairs(long3)
cf3 = Counter(grid(x)[0] for w in long3 for x in w if grid(x) and grid(x)[0])
tot3 = sum(cf3.values())
exp3 = sum(cf3['t' if a == 's' else 's'] / (tot3 - cf3[a]) for a, _ in pairs3 if a in ('s', 't'))
res2['D8 words of 3+ signs'] = {'s_t_pairs': sum({a, b} == {'s', 't'} for a, b in pairs3), 'expected_approx': round(exp3, 2), 'pairs': len(pairs3)}
res.update(res2)
(T.ROOT / 'reading/decipher25_checks.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for k, v in res2.items():
    print(k, ':', v)
