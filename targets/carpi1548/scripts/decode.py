"""Decode a block with the key rebuilt from letter 1 (key/key_d1_rebuilt.json): Viterbi over group boundaries,
scored with a letter-bigram model taken from the letter 1 decipherment (decipherment/d1_contemporary.txt).
Units: two-digit letter groups, two-digit word groups (printed in brackets), the recurring one- and three-digit units
of the key, and nulls (penalised; printed as a middle dot).
Usage (from the target folder): python3 scripts/decode.py transcription/d2_block_digits.txt w2"""
import collections, json, math, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
d = json.load(open(ROOT / 'key/key_d1_rebuilt.json'))
units = collections.defaultdict(list)
for g, x in d['K'].items(): units[g].append(x)
for g, w in d['CODE'].items(): units[g].append('[' + w + ']')
txt = ' '.join(l for l in (ROOT / 'decipherment/d1_contemporary.txt').read_text(encoding='utf-8').splitlines()
               if l and not l.startswith('#'))
L = re.sub(r'[^a-z]', '', txt.lower().replace('à', 'a').replace('v', 'u'))
big = collections.Counter(zip(L, L[1:])); uni = collections.Counter(L)
lp = lambda a, b: math.log((big[(a, b)] + 0.1) / (uni[a] + 2.6))
path, prefix = sys.argv[1], sys.argv[2]
s = ''
for line in pathlib.Path(path).read_text(encoding='utf-8').splitlines():
    if line.startswith(prefix):
        s += re.sub(r'[^0-9d]', '', line.split(None, 1)[1].split('[')[0]).replace('d', '8')
N = len(s); best = [dict() for _ in range(N + 1)]; best[0]['^'] = (0.0, None)
for i in range(N):
    for last, (sc, _) in list(best[i].items()):
        for n in (1, 2, 3):
            g = s[i:i+n]
            if len(g) < n: continue
            for x in units.get(g, []):
                if x.startswith('['):
                    w = x[1:-1]; nl = w[-1]
                    add = (lp(last, w[0]) if last != '^' else 0) + sum(lp(a, b) for a, b in zip(w, w[1:])) + 1.0
                else:
                    nl = x; add = (lp(last, x) if last != '^' else 0) - (2.5 if n != 2 else 0)
                k = best[i+n].get(nl)
                if k is None or sc + add > k[0]: best[i+n][nl] = (sc + add, (i, last, g, x))
        for n, pen in ((1, -9.0), (2, -7.0)):
            g = s[i:i+n]
            if len(g) < n: continue
            k = best[i+n].get(last)
            if k is None or sc + pen > k[0]: best[i+n][last] = (sc + pen, (i, last, g, '·'))
last = max(best[N], key=lambda k: best[N][k][0]); i = N; out = []
while i > 0:
    sc, (pi, pl, g, x) = best[i][last]; out.append((g, x)); i, last = pi, pl
out.reverse()
print(f'# {path} ({prefix}): {N} digits, decoded with key/key_d1_rebuilt.json by scripts/decode.py')
print(''.join(x for _, x in out))
print('# groups')
print(' '.join(f'{g}={x}' for g, x in out))
