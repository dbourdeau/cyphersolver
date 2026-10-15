"""Rebuild the R483 key by hard-EM alignment of each cipher line with the clerk's interlinear Latin."""
import re, math, glob, collections, json, unicodedata
from pathlib import Path
ROOT = Path(__file__).resolve().parent

def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = re.sub(r'\([^)]*\)|\[[^\]]*\]', '', s)
    s = ''.join(ch for ch in s if ch.isalpha())
    return s.replace('j', 'i').replace('v', 'u')

def lines():
    out = []
    for f in sorted(glob.glob(str(ROOT / 'tr' / 'R483_p*.txt'))):
        p = None
        for l in open(f, encoding='utf8'):
            if l.startswith('P:'):
                p = l[2:].strip()
            elif l.startswith('C:'):
                c = re.sub(r'\{clear:[^}]*\}', ' ', l[2:])
                groups = [re.sub(r'\D', '', g) for g in c.split() if re.sub(r'\D', '', g)]
                if p and p != '(none)' and groups:
                    words = [w for w in re.split(r'[\s|]+', p) if w and not w.endswith('?')]
                    out.append((Path(f).stem, groups, norm(' '.join(re.split(r'[\s|]+', p)))))
                p = None
    return out

L = lines()
MAXLEN = 4
prob = collections.defaultdict(lambda: collections.Counter())

def cost(code, s, it):
    c = prob[code]; tot = sum(c.values())
    lenprior = {0: 4.0, 1: 1.2, 2: 0.6, 3: 1.4, 4: 2.5}[len(s)]
    if it == 0 or tot == 0:
        return lenprior + 1.0
    return -math.log((c[s] + 0.05) / (tot + 0.05 * 40)) + 0.3 * lenprior

def viterbi(groups, text, it):
    n, m = len(groups), len(text)
    INF = float('inf')
    D = [[INF] * (m + 1) for _ in range(n + 1)]; B = [[0] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0
    for i in range(n):
        for j in range(m + 1):
            if D[i][j] == INF: continue
            for k in range(0, MAXLEN + 1):
                if j + k > m: break
                v = D[i][j] + cost(groups[i], text[j:j + k], it)
                if v < D[i + 1][j + k]:
                    D[i + 1][j + k] = v; B[i + 1][j + k] = j
    if D[n][m] == INF: return None, INF
    seg, j = [], m
    for i in range(n, 0, -1):
        pj = B[i][j]; seg.append(text[pj:j]); j = pj
    return seg[::-1], D[n][m] / max(n, 1)

for it in range(12):
    new = collections.defaultdict(collections.Counter); bad = 0
    res = []
    for src, g, t in L:
        seg, c = viterbi(g, t, it)
        if seg is None: continue
        res.append((src, g, t, seg, c))
        if it > 2 and c > 3.2: bad += 1; continue  # line whose interlinear does not fit: skip it
        for code, s in zip(g, seg):
            new[code][s] += 1
    prob.clear(); prob.update(new)

key = {}
for code, c in prob.items():
    s, n = c.most_common(1)[0]; tot = sum(c.values())
    key[code] = {'value': s, 'n': n, 'of': tot, 'alts': dict(c.most_common(3))}
json.dump(dict(sorted(key.items(), key=lambda x: int(x[0]))), open(ROOT / 'R483_key_rebuilt.json', 'w', encoding='utf8'), indent=1, ensure_ascii=False)
print('lines', len(L), 'skipped as ill-fitting', bad, 'codes', len(key))
for code, v in sorted(key.items(), key=lambda x: -x[1]['of'])[:70]:
    print(code, v['value'], f"{v['n']}/{v['of']}", v['alts'])
