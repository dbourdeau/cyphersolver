"""Two tests that do not need a full page table.

1. Terminal test. Page renumbering (37000 from 18470; 5950 from 13040 with a block shift) keeps the last figure, and keeps the
   last two figures when blocks stay put. So text in a family member should share the terminal-pair profile of the family:
   frequent words sit at fixed terminals. Score = cosine of terminal-pair counts against the family's, under each block rule,
   with a control of the same statistic on the other families and on uniform random groups.

2. Dutchman pages. Mendelsohn pp. 92-95 lists double-numbered pages of 37000, 20000, 29000, 2500 with their 18470 page.
   Only those pages can be converted. Convert the quoted 18470 groups on them and count hits, against shuffled page pairs.
"""
import re, sys, math, random, collections
sys.stdout.reconfigure(encoding='utf-8')
m = open('refs/m.txt', encoding='utf-8').read().split('\n')
T = {}; cur = None
for l in open('transcription_pass1.txt', encoding='utf-8'):
    if l.startswith('#'): continue
    if l.startswith('@'):
        cur = l.split()[0][1:]; T[cur] = []; continue
    T[cur] += [g for g in l.split() if re.fullmatch(r'\d+', g)]
fam = {'A': ['w763', 'w765', 'w735', 'w2635'], 'B': ['w749', 'w746', 'w512', 'w513'], 'C': ['w752'], 'D': ['w643'],
       'E': ['w791'], 'F': ['w769', 'w716', 'w628', 'w611', 'w592']}
SHIFT = {0: 1, 1: 2, 2: 3, 3: 4, 4: 0, 5: 6, 6: 7, 7: 8, 8: 9, 9: 5}
def groups(ids): return [int(g) for t in ids for g in T[t] if len(g) in (4, 5) and 1000 <= int(g) < 31000]
# reference: running 18470/1777/12444 specimen text and running 13040 specimens. Only groups inside vocabulary range.
def ref(a, b): return [int(x) for x in re.findall(r'(?<![\d-])\d{4,5}(?![\d-])', ' '.join(m[a:b])) if 1000 <= int(x) < 31000]
R18 = ref(10393, 13700); R13 = ref(1197, 2060)
def prof(gs, shift=False):
    c = collections.Counter()
    for g in gs:
        q, r = (g // 10) % 10, g % 10
        c[(SHIFT[q] if shift else q) * 10 + r] += 1
    return c
def cos(a, b):
    k = set(a) | set(b); dot = sum(a[i] * b[i] for i in k)
    return dot / math.sqrt(sum(v * v for v in a.values()) * sum(v * v for v in b.values()) or 1)
rng = random.Random(3)
print('terminal-pair cosine; control = same number of uniform random terminals, mean and max of 500')
for rn, R in (('18470 family', R18), ('13040 family', R13)):
    for shift in (False, True):
        P = prof(R, shift)
        for f, ids in fam.items():
            G = groups(ids)
            if len(G) < 15: continue
            obs = cos(prof(G), P)
            ctrl = [cos(collections.Counter(rng.randrange(100) for _ in G), P) for _ in range(500)]
            print(f'  {rn} shift={shift!s:5} {f} n={len(G):3d} obs={obs:.3f} ctrl mean={sum(ctrl)/500:.3f} max={max(ctrl):.3f}')
print()
print('Dutchman double-numbered pages')
a = next(i for i, l in enumerate(m) if 'DOUBLE-NUMBERED PAGES IN 87000' in l or 'DOUBLE-NUMBERED PAGES IN 37000' in l)
heads = [(i, re.search(r'IN (\S+)', l).group(1)) for i, l in enumerate(m) if 'NUMBERED PAGES IN' in l and i >= a]
print(' heads', heads)
stop = next(i for i, l in enumerate(m) if i > a and l.startswith('We observe that code 37000'))
base = set(int(x) for x in re.findall(r'(?<![\d-])\d{4,5}(?![\d-])', ' '.join(m[7094:13700])) if 1000 <= int(x) <= 30999)
ends = [h[0] for h in heads[1:]] + [stop]
for (st, name), en in zip(heads, ends):
    pairs = []
    for i in range(st, en - 1):
        x = re.fullmatch(r'\s*(\d{2,3})\s*[-—–]\s*(\d{2,3})\s*', m[i])
        y = re.fullmatch(r'\s*(\d{2,3})\s*', m[i + 1])
        if x and y: pairs.append((int(x.group(1)), int(x.group(2)), int(y.group(1))))
    print(f' {name}: {len(pairs)} pages parsed', pairs[:5])
    sh = name in ('20000', '29000', '29000,')
    def conv(pp):
        S = set()
        for p1, p2, p18 in pp:
            for g in base:
                if g // 100 == p18:
                    q, r = (g // 10) % 10, g % 10
                    if sh: q = SHIFT[q]
                    S.add(p1 * 100 + q * 10 + r); S.add(p2 * 100 + q * 10 + r)
        return S
    S = conv(pairs)
    for f, ids in fam.items():
        G = [int(g) for t in ids for g in T[t] if len(g) in (4, 5)]
        obs = sum(g in S for g in G)
        ctrl = []
        for _ in range(200):
            v = [p[2] for p in pairs]; rng.shuffle(v)
            S2 = conv([(p[0], p[1], w) for p, w in zip(pairs, v)])
            ctrl.append(sum(g in S2 for g in G))
        print(f'    {f} n={len(G):3d} hits={obs:2d} ctrl mean={sum(ctrl)/200:4.1f} max={max(ctrl)}')
