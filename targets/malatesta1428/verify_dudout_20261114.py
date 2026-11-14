"""Independent check of malatesta1428 (Brice Dudout, Claude Opus 5.5, 14 Nov 2026).

1) Decodes transcription_tomokiyo_corrected.txt with key.json (not dec.py) and looks for each run, letter for letter,
   in texts/p1_reading.md (u=v, i=j; the unread sign 23 and the letters the scribe left out are allowed for).
2) Compares this project's own sign-by-sign transcription p1v2.txt (22 Sept 2026, made before any key was known, with
   its own sign names) with the corrected transcription, position by position. The two use different names, so each
   p1v2 name is given the key value it meets most often in an alignment (seeded only with the six pairs that NOTES
   reads at the ends of run 1); the script then reports how many positions agree and which names carry two values.
   Of p1v2's marks, ':' is kept as a sign; '|', '/' and '.' are dropped as separators.
usage: python3 verify_dudout_20261114.py targets/malatesta1428
"""
import json, re, sys, collections, difflib
T = sys.argv[1] if len(sys.argv) > 1 else '.'
key = json.load(open(f'{T}/key.json', encoding='utf8'))
rows = [l.strip().strip(';') for l in open(f'{T}/transcription_tomokiyo_corrected.txt', encoding='utf8')
        if l.strip() and not l.startswith('#')]
runs_t = [[t for r in rows[a:b] for t in r.split(';') if t] for a, b in ((0, 3), (3, 6), (6, 10))]
val = lambda t: '?' if key[t] == '[?]' else key[t]
norm = lambda s: re.sub(r'[^a-z?]', '', s.lower()).replace('u', 'v').replace('j', 'i')
reading = norm(open(f'{T}/texts/p1_reading.md', encoding='utf8').read())
print('1) key.json on the corrected transcription')
for n, r in enumerate(runs_t, 1):
    dec = norm(''.join(val(t) for t in r))
    sm = difflib.SequenceMatcher(None, dec, reading, autojunk=False)
    blk = sm.find_longest_match(0, len(dec), 0, len(reading))
    lo = max(0, blk.b - blk.a - 5); win = reading[lo:lo + len(dec) + 10]
    sm = difflib.SequenceMatcher(None, dec, win, autojunk=False)
    diffs = [(op, dec[i1:i2], win[j1:j2]) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != 'equal']
    diffs = [d for d in diffs if not (d[0] == 'insert' and d is diffs[0] or d is diffs[-1] and d[0] == 'insert')]
    print(f'   run {n}: {len(r)} signs, {len(dec)} letters; against p1_reading.md: {diffs}')
ours = {}
for l in open(f'{T}/p1v2.txt', encoding='utf8'):
    m = re.match(r'(L\d\d):\s*(.*)', l)
    if m: ours[m.group(1)] = [t for t in m.group(2).split() if not t.startswith('{')]
SEP = {'|', '/', '.'}
runs_o = [[t for L in Ls for t in ours[L] if t not in SEP] for Ls in
          (('L04', 'L05', 'L06'), ('L07', 'L08', 'L09'), ('L10', 'L11', 'L12', 'L13'))]
seed = {'cc': 'd', 'ss': 'e', 'Z': 's', 'K': 'v', 'bz': 'i', 'x': 'b'}   # NOTES: cc ss Z K bz Z = d-e-s-u-i-s; ... x = b
def align(a, b, score):
    n, m = len(a), len(b); INF = 1e9
    D = [[INF] * (m + 1) for _ in range(n + 1)]; P = [[None] * (m + 1) for _ in range(n + 1)]; D[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            d = D[i][j]
            if d == INF: continue
            for di, dj, c in ((1, 0, 1), (0, 1, 1), (1, 1, None)):
                if i + di > n or j + dj > m: continue
                cc = d + (score(a[i], b[j]) if c is None else c)
                if cc < D[i + di][j + dj]: D[i + di][j + dj] = cc; P[i + di][j + dj] = (i, j)
    out = []; i, j = n, m
    while (i, j) != (0, 0):
        pi, pj = P[i][j]; out.append((a[pi] if pi < i else None, b[pj] if pj < j else None)); i, j = pi, pj
    return out[::-1]
mp = dict(seed)
for _ in range(10):
    score = lambda t, o: 0.6 if o not in mp else (0.0 if mp[o] == val(t) else 1.2)
    als = [align(a, b, score) for a, b in zip(runs_t, runs_o)]
    co = collections.defaultdict(collections.Counter)
    for al in als:
        for t, o in al:
            if t and o: co[o][val(t)] += 1
    new = {o: c.most_common(1)[0][0] for o, c in co.items()}
    if new == mp: break
    mp = new
pairs = [(t, o) for al in als for t, o in al]
indel = sum(1 for t, o in pairs if not (t and o))
same = sum(1 for t, o in pairs if t and o and mp[o] == val(t))
print(f'2) p1v2.txt against the corrected transcription: {sum(map(len, runs_t))} vs {sum(map(len, runs_o))} signs, '
      f'{indel} insertions/deletions, {same} positions with the same value')
names = collections.defaultdict(collections.Counter)
for t, o in pairs:
    if t and o: names[o][(t, val(t))] += 1
for o in sorted(names, key=lambda x: -sum(names[x].values())):
    c = names[o]; vs = {v for (_, v) in c}
    flag = '   <- two values' if len(vs) > 1 else ''
    print(f'   {o:4} ' + ', '.join(f'{t}={v or "null"} x{k}' for (t, v), k in c.most_common()) + flag)
