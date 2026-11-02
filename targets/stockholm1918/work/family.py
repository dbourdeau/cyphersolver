"""Convert the 18470 groups Mendelsohn prints into 12444, 1777 and 2310 through his page tables (pp. 21-24) and the
block shift of p. 8, then test each telegram family against the converted sets. Control: the same test with the page
table shuffled, so the expected chance level is measured, not assumed."""
import re, sys, random
sys.stdout.reconfigure(encoding='utf-8')
m = open('refs/m.txt', encoding='utf-8').read().split('\n')
def triples(a, b):
    rows, cur = [], []
    for l in m[a:b]:
        s = l.strip()
        if re.fullmatch(r'\d{1,3}', s):
            cur.append(int(s))
            if len(cur) == 3:
                rows.append(tuple(cur)); cur = []
        elif len(s) > 25 or s.startswith('REF ID'):
            cur = []
    return rows
TAB = {'12444': (2563, 3462), '1777': (3466, 4362), '2310': (4365, 5245)}
PAGE = {}
for code, (a, b) in TAB.items():
    votes = {}
    for x, c, y in triples(a, b):
        # central c as 18470 -> left x in the derived code; central c as derived -> right y in 18470
        if c >= 10 and x >= 10: votes.setdefault(c, []).append(x)
        if c >= 10 and y >= 10: votes.setdefault(y, []).append(c)
    d, conflict = {}, 0
    for k, v in votes.items():
        if len(set(v)) == 1: d[k] = v[0]
        else: conflict += 1
    PAGE[code] = d
    print(code, 'pages mapped', len(d), 'conflicting pages dropped', conflict)
for code, pairs in {'12444': [(24, 19), (108, 188), (271, 258), (186, 63)], '1777': [(24, 12), (108, 14), (191, 36)]}.items():
    print(code, 'known page pairs', [(a, PAGE[code].get(a), b) for a, b in pairs])
SHIFT = {0: 1, 1: 2, 2: 3, 3: 4, 4: 0, 5: 6, 6: 7, 7: 8, 8: 9, 9: 5}
def conv(g, table):
    p, q, r = g // 100, (g // 10) % 10, g % 10
    if p not in table: return None
    return table[p] * 100 + SHIFT[q] * 10 + r
base = set(int(x) for x in re.findall(r'(?<![\d-])\d{4,5}(?![\d-])', ' '.join(m[7094:13700])) if 1000 <= int(x) <= 30999)
print('18470-family groups quoted', len(base))
T = {}; cur = None
for l in open('transcription_pass1.txt', encoding='utf-8'):
    if l.startswith('#'): continue
    if l.startswith('@'):
        cur = l.split()[0][1:]; T[cur] = []; continue
    T[cur] += [g for g in l.split() if re.fullmatch(r'\d+', g)]
fam = {'A 1219': ['w763', 'w765', 'w735', 'w2635'], 'B 44xx': ['w749', 'w746', 'w512', 'w513'],
       'C w752': ['w752'], 'D w643': ['w643'], 'E Ludendorff': ['w791'], 'F legation': ['w769', 'w716', 'w628', 'w611', 'w592']}
rng = random.Random(7)
for code, table in PAGE.items():
    S = set(v for v in (conv(g, table) for g in base) if v)
    for fn, ids in fam.items():
        G = [int(g) for t in ids for g in T[t] if len(g) in (4, 5)]
        obs = sum(g in S for g in G)
        ctrl = []
        for _ in range(300):
            ks = list(table); vs = list(table.values()); rng.shuffle(vs); t2 = dict(zip(ks, vs))
            S2 = set(v for v in (conv(g, t2) for g in base) if v)
            ctrl.append(sum(g in S2 for g in G))
        mu = sum(ctrl) / len(ctrl)
        print(f'{code:6s} {fn:12s} n={len(G):4d} hits={obs:3d} control mean={mu:5.1f} max={max(ctrl):3d}')
