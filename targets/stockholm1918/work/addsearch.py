"""Does any telegram family sit on a known German code group set, plain or with a constant additive?
Sets: all 4-5 figure groups quoted in Mendelsohn 1937 sections (13040/5950 specimens; 18470/1777/12444 specimens)."""
import re, sys, collections, statistics as st
sys.stdout.reconfigure(encoding='utf-8')
T = {}; cur = None
for l in open('transcription_pass1.txt', encoding='utf-8'):
    if l.startswith('#'): continue
    if l.startswith('@'):
        cur = l.split()[0][1:]; T[cur] = []; continue
    T[cur] += [g for g in l.split() if re.fullmatch(r'\d+', g)]
fam = {'A 1219': ['w763', 'w765', 'w735', 'w2635'], 'B 44xx': ['w749', 'w746', 'w512', 'w513'],
       'C w752': ['w752'], 'D w643': ['w643'], 'E Ludendorff': ['w791'], 'F legation': ['w769', 'w716', 'w628', 'w611', 'w592']}
m = open('refs/m.txt', encoding='utf-8').read().split('\n')
sets = {'13040/5950': (1197, 2060), 's8-26': (2351, 10393), 's27': (10393, 13700)}
for sn, (a, b) in sets.items():
    S = set(int(x) for x in re.findall(r'(?<![\d-])\d{4,5}(?![\d-])', ' '.join(m[a:b])))
    for fn, ids in fam.items():
        G = [int(g) for t in ids for g in T[t] if len(g) in (4, 5)]
        res = []
        for d in range(-999, 1000):
            res.append((sum((g + d) in S for g in G), d))
        v = [r[0] for r in res]; mu, sd = st.mean(v), st.pstdev(v)
        top = sorted(res, reverse=True)[:3]
        d0 = next(r[0] for r in res if r[1] == 0)
        print(f'{sn:10s} {fn:12s} n={len(G):4d} d0={d0:3d} mean={mu:5.1f} sd={sd:4.1f} top={[(c, d, round((c-mu)/sd, 1)) for c, d in top]}')
print()
print('digit statistics by telegram family: index of coincidence by digit column, 5-figure groups only')
for fn, ids in fam.items():
    G = [g for t in ids for g in T[t] if len(g) == 5]
    row = []
    for c in range(5):
        cnt = collections.Counter(g[c] for g in G); n = len(G)
        row.append(round(10*sum(v*(v-1) for v in cnt.values())/(n*(n-1)), 2))
    print(f'{fn:12s} n={len(G):4d} IC per column {row}')
