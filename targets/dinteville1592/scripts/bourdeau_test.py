"""Re-run Bourdeau's align.py test (one sign -> one letter, homophones allowed, up to 3 null sign-types,
exact length) on f. 128 line C, varying (a) diacritic-aware vs merged signs, (b) his gloss vs the corrected gloss."""
import itertools
def solve(signs, plain, maxnull=3):
    types = sorted(set(signs)); res = []
    for k in range(0, maxnull + 1):
        for nulls in itertools.combinations(types, k):
            s = [x for x in signs if x not in nulls]
            if len(s) != len(plain): continue
            m = {}; ok = True
            for a, b in zip(s, plain):
                if m.setdefault(a, b) != b: ok = False; break
            if ok: res.append((nulls, m))
    return res
C = 'II D al Y Px W M o al # 1. Q 6s o f 3 c 1. D 9 1. f R o 6s'.split()     # 'auoir veu dessendre a gennes'
MERGE = {'6s': 'o', '6p': 'o', 'Vt': 'V', 'D+': 'D', 'Y+': 'Y'}
merged = [MERGE.get(s, s) for s in C]
glosses = {'his gloss "auoir veu dascendre a geneve"': 'auoirueudascendreageneue',
           'corrected "auoir veu dessendre a gennes"': 'auoirueudessendreagennes'}
for gname, g in glosses.items():
    for sname, S in (('diacritic-aware signs', C), ('diacritics merged', merged)):
        r = solve(S, g)
        print(f'{gname:42s} | {sname:22s} | solutions: {len(r)}' + (f'  e.g. nulls={r[0][0]}' if r else ''))
