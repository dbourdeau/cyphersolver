"""Second stage: repair OCR-garbled fr. numbers (3<->5, 8<->6, 1<->l ...) with neighbour order within each Ancien-fonds tome,
then summarise per volume. usage: python fixnum.py items.json out.json  (items from parse_omont.py)"""
import json, re, sys, itertools
rows = json.load(open(sys.argv[1], encoding='utf8'))
RANGE = {'p1cataloguegnr01bibluoft': (1, 3130), 'p1cataloguegnr02bibluoft': (3131, 3766), 'p1cataloguegnr03bibluoft': (3767, 4586),
         'p1cataloguegnr04bibluoft': (4587, 5300), 'p1cataloguegnr05bibluoft': (5300, 6170)}
SW = {'5': '3', '3': '5', '8': '6', '6': '8', '0': '6', '1': '7', '7': '1'}
def variants(n):
    s = str(n); out = {n}
    pos = [i for i, c in enumerate(s) if c in SW]
    for k in (1, 2):
        for comb in itertools.combinations(pos, k):
            t = list(s)
            for i in comb: t[i] = SW[t[i]]
            out.add(int(''.join(t)))
    return out
res = []
by = {}
for r in rows: by.setdefault(r['vol'], []).append(r)
def nchg(a, b): return sum(x != y for x, y in zip(str(a), str(b))) if len(str(a)) == len(str(b)) else 9
for vol, rs in by.items():
    rs.sort(key=lambda r: r['off'])
    lo, hi = RANGE.get(vol, (1, 99999))
    for r in rs:
        n = r['num']
        if lo <= n <= hi: best = n
        else:
            c = [v for v in variants(n) if lo <= v <= hi]
            best = min(c, key=lambda v: nchg(n, v)) if c else None
        r['fr_raw'] = n; r['fr'] = best
        res.append(r)
json.dump(res, open(sys.argv[2], 'w', encoding='utf8'), ensure_ascii=False, indent=0)
print(sum(1 for r in res if r['fr'] is None), 'unresolved of', len(res))
