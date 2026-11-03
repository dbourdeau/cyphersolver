"""Build the key from the pairs: align each cipher line (sign sequence) with the interlinear clear of that line
(letters only) by dynamic programming, and re-estimate P(letter | unit) by hard EM. A unit is one sign or two signs.
Seeds are only used to start EM. usage: learn.py TRANSCRIPTION GLOSS LINE_PREFIXES(comma) OUT_KEY"""
import sys, re, math, unicodedata, collections, json

def toks(s):
    s = re.sub(r'\[TXT\]|\(|\)|\||,|\.', ' ', s)
    out = []
    for t in s.split():
        b = t.split('^')[0].rstrip('~?')
        if b and b != '?': out.append(b)
    return out

def letters(g):
    g = unicodedata.normalize('NFD', g)
    g = ''.join(c for c in g if not unicodedata.combining(c)).lower()
    words = [w.strip() for w in g.split('|')]
    words = [w for w in words if w and not re.fullmatch(r'[\d\W]+', w)]
    # drop the reader's doubled words (same word twice in a row)
    ded = [w for i, w in enumerate(words) if i == 0 or w != words[i - 1]]
    return re.sub(r'[^a-z]', '', ''.join(ded))

SEED = {'3': 'c', 'ps': 'h', 's': 'e', 'm': 'o', '[]': 's', '1': 'e', 'o +': 'e', 'o_+': 'e', 'o_v': 'r', 'n_o': 's', 'h_c': 'm', 'q': 'a', 'x': 'i', 'w': 'i',
        'T': 'l', 'n o': 's', 'v': 'r', '8': 'o'}
NULL, SKIP = 3.5, 3.5

def align(S, L, P):
    n, m = len(S), len(L)
    INF = 1e9
    D = [[INF] * (m + 1) for _ in range(n + 1)]; B = [[None] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            d = D[i][j]
            if d >= INF: continue
            if i < n and d + NULL < D[i + 1][j]: D[i + 1][j] = d + NULL; B[i + 1][j] = (i, j, S[i], '')
            if j < m and d + SKIP < D[i][j + 1]: D[i][j + 1] = d + SKIP; B[i][j + 1] = (i, j, '', L[j])
            for k in (1, 2):
                if i + k <= n and j < m:
                    u = ' '.join(S[i:i + k]); c = d + P(u, L[j]) + (0.8 if k == 2 else 0)
                    if c < D[i + k][j + 1]: D[i + k][j + 1] = c; B[i + k][j + 1] = (i, j, u, L[j])
    path = []; i, j = n, m
    while (i, j) != (0, 0):
        pi, pj, u, l = B[i][j]; path.append((u, l)); i, j = pi, pj
    return D[n][m], path[::-1]

def main():
    tr = dict(l.rstrip('\n').split('\t', 1) for l in open(sys.argv[1], encoding='utf8') if '\t' in l)
    gl = {}
    for l in open(sys.argv[2], encoding='utf8'):
        p = l.rstrip('\n').split('\t')
        if len(p) == 3 and p[1] == 'G': gl[p[0]] = p[2]
    pref = sys.argv[3].split(',')
    lines = [n for n in tr if any(n.startswith(p) for p in pref) and n in gl]
    cnt = collections.Counter({(u, l): 5 for u, l in SEED.items()})
    for it in range(8):
        tot = collections.Counter(); 
        for (u, l), c in cnt.items(): tot[u] += c
        P = lambda u, l: -math.log((cnt[(u, l)] + 0.05) / (tot[u] + 0.05 * 26 + 2))
        new = collections.Counter(); cost = 0
        for n in lines:
            c, path = align(toks(tr[n]), letters(gl[n]), P)
            cost += c
            for u, l in path:
                if u and l: new[(u, l)] += 1
        cnt = new + collections.Counter({(u, l): 1 for u, l in SEED.items()})
        print('iter', it, round(cost))
    by = collections.defaultdict(collections.Counter)
    for (u, l), c in cnt.items(): by[u][l] += c
    rows = sorted(by.items(), key=lambda x: -sum(x[1].values()))
    with open(sys.argv[4], 'w', encoding='utf8') as f:
        for u, c in rows:
            f.write(f"{u}\t{sum(c.values())}\t" + ' '.join(f'{l}:{k}' for l, k in c.most_common(4)) + '\n')
    for u, c in rows[:60]:
        print(f"{u:6s} {sum(c.values()):4d}  " + ' '.join(f'{l}:{k}' for l, k in c.most_common(4)))

if __name__ == '__main__':
    main()
