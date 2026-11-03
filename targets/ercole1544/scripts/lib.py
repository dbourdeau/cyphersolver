# shared helpers: tokenise transcriptions, decode with a table, DP alignment against clear text
import re
L2P = dict(zip('abcdefghnopqrstuxyzk', 'nopqrstuabcdefghilmz'))   # the single-letter table (see key.tsv); S is ss


def tokens(path):
    out = []
    for line in open(path, encoding='utf8'):
        if line.startswith('#') or not line.strip():
            continue
        lab, _, body = line.strip().partition(' ')
        for t in re.findall(r'L\^\w+|\d+|\?|[A-Za-z]', body):
            out.append((lab, t))
    return out


def plain_text(path, skip_head=1):
    ls = [l for l in open(path, encoding='utf8') if not l.startswith('#') and l.strip()]
    s = ''.join(ls[skip_head:]).lower().replace('v', 'u').replace('j', 'i').replace('y', 'i')
    return re.sub(r'[^a-z]', '', s)


def is_letter(t):
    return len(t) == 1 and t.isalpha() and t not in 'LS'


def align(toks, plain, tab, maxgroup=14):
    """Global DP. Letter signs take one plain letter, S takes two, code signs take 0..maxgroup letters."""
    n, m = len(toks), len(plain)
    INF = -10 ** 9
    D = [[INF] * (m + 1) for _ in range(n + 1)]
    B = [[None] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0
    for j in range(1, m + 1):
        D[0][j] = D[0][j - 1] - 1
        B[0][j] = ('gapP', 0, j - 1)
    for i in range(1, n + 1):
        t = toks[i - 1]
        for j in range(m + 1):
            best = (D[i - 1][j] - 1, ('gapS', i - 1, j))
            if j and D[i][j - 1] - 1 > best[0]:
                best = (D[i][j - 1] - 1, ('gapP', i, j - 1))
            if t == 'S':
                if j >= 2:
                    v = D[i - 1][j - 2] + (4 if plain[j - 2:j] == 'ss' else -1)
                    if v > best[0]:
                        best = (v, ('sub', i - 1, j - 2))
            elif is_letter(t):
                if j:
                    v = D[i - 1][j - 1] + (2 if tab.get(t) == plain[j - 1] else -1)
                    if v > best[0]:
                        best = (v, ('sub', i - 1, j - 1))
            else:
                for k in range(0, min(maxgroup, j) + 1):
                    v = D[i - 1][j - k] + (0.5 if k else 0)
                    if v > best[0]:
                        best = (v, ('sub', i - 1, j - k))
            D[i][j] = best[0]
            B[i][j] = best[1]
    i, j = n, m
    pairs = []
    while i or j:
        op, pi, pj = B[i][j]
        if op == 'sub':
            pairs.append((toks[i - 1], plain[pj:j]))
        elif op == 'gapS':
            pairs.append((toks[i - 1], ''))
        else:
            pairs.append(('', plain[pj:j]))
        i, j = pi, pj
    return pairs[::-1], D[n][m]
