"""Follow-up on the one near-signal: system A against the 13040 terminal-pair profile, no block shift (0.864, control max 0.868).
Uses only groups in the 13040 column (the number directly before a word in the specimens), a larger control, the last four
figures of prefix groups, and the Bernstorff 1917 text as a negative control of the same outward shape."""
import re, sys, math, random, collections, statistics as st
sys.stdout.reconfigure(encoding='utf-8')
m = open('refs/m.txt', encoding='utf-8').read().split('\n')
pairs = []
for i in range(1197, 2060):
    a, b = m[i].strip(), m[i + 1].strip()
    if re.fullmatch(r'\d{4,5}', a) and re.match(r'[A-Za-z(]', b): pairs.append((int(a), b[:24]))
print('13040 group-word pairs', len(pairs))
P = collections.Counter(g % 100 for g, _ in pairs)
print('top terminals', P.most_common(10))
T = {}; cur = None
for l in open('transcription_pass1.txt', encoding='utf-8'):
    if l.startswith('#'): continue
    if l.startswith('@'):
        cur = l.split()[0][1:]; T[cur] = []; continue
    T[cur] += [g for g in l.split() if re.fullmatch(r'\d+', g)]
def cos(a, b):
    k = set(a) | set(b)
    return sum(a[i] * b[i] for i in k) / math.sqrt(sum(v * v for v in a.values()) * sum(v * v for v in b.values()) or 1)
sets = {'A': [g for t in ('w763', 'w765', 'w735', 'w2635') for g in T[t] if len(g) in (4, 5)],
        'B': [g for t in ('w749', 'w746', 'w512', 'w513') for g in T[t] if len(g) in (4, 5)],
        'C': [g for g in T['w752'] if len(g) in (4, 5)], 'D': [g for g in T['w643'] if len(g) in (4, 5)],
        'E': [g for g in T['w791'] if len(g) == 5],
        'Bernstorff (control)': re.findall(r'\b\d{4,5}\b', open('../bernstorff1917/transcription.txt', encoding='utf-8').read())}
rng = random.Random(11)
for k, G in sets.items():
    n = len(G)
    obs = cos(collections.Counter(int(g) % 100 for g in G), P)
    c = [cos(collections.Counter(rng.randrange(100) for _ in range(n)), P) for _ in range(5000)]
    mu, sd = st.mean(c), st.pstdev(c)
    print(f'{k:22s} n={n:4d} obs={obs:.3f} mean={mu:.3f} sd={sd:.3f} z={(obs-mu)/sd:5.1f} frac>={sum(x>=obs for x in c)/5000:.4f}')
print('A: most frequent terminals and their 13040 words')
A = collections.Counter(int(g) % 100 for g in sets['A'])
w = collections.defaultdict(list)
for g, b in pairs: w[g % 100].append(f'{g} {b}')
for t, n in A.most_common(10): print(' ', t, n, w[t][:5])
