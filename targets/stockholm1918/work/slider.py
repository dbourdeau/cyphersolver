"""Slider 1 of Mendelsohn 1937 p. 98 (rebuilt there from decoded messages), all 1000 settings, on every family.
Encipher: digits 2,3,4 go through three cyclic tapes, first and fifth figures stay. Worked example at 718: 41259 -> 40429."""
import re, sys, statistics as st
sys.stdout.reconfigure(encoding='utf-8')
TAPE = ['7092635814', '1946273508', '8346527190']
def tab(tape, set_):
    k = tape.index(set_)
    return {str(i): tape[(k + i) % 10] for i in range(10)}
def enc(g, s):
    t = [tab(TAPE[j], s[j]) for j in range(3)]
    return g[0] + t[0][g[1]] + t[1][g[2]] + t[2][g[3]] + g[4]
assert enc('41259', '718') == '40429', enc('41259', '718')
T = {}; cur = None
for l in open('transcription_pass1.txt', encoding='utf-8'):
    if l.startswith('#'): continue
    if l.startswith('@'):
        cur = l.split()[0][1:]; T[cur] = []; continue
    T[cur] += [g for g in l.split() if re.fullmatch(r'\d+', g)]
fam = {'A 1219': ['w763', 'w765', 'w735', 'w2635'], 'B 44xx': ['w749', 'w746', 'w512', 'w513'],
       'C w752': ['w752'], 'D w643': ['w643'], 'E Ludendorff': ['w791'], 'F legation': ['w769', 'w716', 'w628', 'w611', 'w592']}
m = open('refs/m.txt', encoding='utf-8').read().split('\n')
sets = {'VB (part III)': (15044, 15686), '13040/5950': (1197, 2060)}
for sn, (a, b) in sets.items():
    S = set(x.zfill(5) for x in re.findall(r'(?<![\d-])\d{4,5}(?![\d-])', ' '.join(m[a:b])))
    print(sn, 'set size', len(S))
    for fn, ids in fam.items():
        G = [g.zfill(5) for t in ids for g in T[t] if len(g) in (4, 5)]
        res = []
        for x in range(10):
            for y in range(10):
                for z in range(10):
                    s = f'{x}{y}{z}'
                    t = [tab(TAPE[j], s[j]) for j in range(3)]
                    inv = [{v: k for k, v in d.items()} for d in t]
                    # both directions: the telegram as enciphered text, and as basic text
                    h1 = sum((g[0] + inv[0][g[1]] + inv[1][g[2]] + inv[2][g[3]] + g[4]) in S for g in G)
                    h2 = sum((g[0] + t[0][g[1]] + t[1][g[2]] + t[2][g[3]] + g[4]) in S for g in G)
                    res.append((h1, s, 'dec')); res.append((h2, s, 'enc'))
        v = [r[0] for r in res]; mu, sd = st.mean(v), st.pstdev(v)
        top = sorted(res, reverse=True)[:3]
        print(f'  {fn:12s} n={len(G):4d} mean={mu:5.2f} sd={sd:4.2f} top={[(c, s, k, round((c-mu)/sd, 1)) for c, s, k in top]}')
