"""Align a proposed plaintext reading to each cipher line and measure it.
reading file format:  t1.5: plain text words   (letters only count; [..] = gap left unread)
Each token has a value set (key.json). DP alignment: token matches a chunk of the reading at cost 0 if the chunk
is one of its values, 1 otherwise (sign read against the key); token as null costs 0 for declared nulls, 1.2 otherwise;
reading letter with no token costs 1."""
import sys, json, re, unicodedata
from decode import load
import os
KEY = json.load(open(os.environ.get('KEY', 'key_v7.json'), encoding='utf8'))
def norm(s):
    s = ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z\[\]]', '', s).replace('j', 'i').replace('v', 'u')
def vals(t):
    v = KEY.get(t, '*').split(',')
    return [x.replace('j','i').replace('v','u') for x in v]
def align(toks, text):
    n, m = len(toks), len(text); INF = 1e9
    D = [[INF]*(m+1) for _ in range(n+1)]; B = [[None]*(m+1) for _ in range(n+1)]
    D[0][0] = 0
    for i in range(n+1):
        for j in range(m+1):
            d = D[i][j]
            if d >= INF: continue
            if j < m and d+1 < D[i][j+1]: D[i][j+1] = d+1; B[i][j+1] = (i, j, None, text[j])
            if i < n:
                vs = vals(toks[i])
                c = 0 if '' in vs else 1
                if d+c < D[i+1][j]: D[i+1][j] = d+c; B[i+1][j] = (i, j, toks[i], '')
                for L in range(1, 9):
                    if j+L > m: break
                    ch = text[j:j+L]
                    c = 0 if ch in vs else (1 if L == 1 else 9)
                    if d+c < D[i+1][j+L]: D[i+1][j+L] = d+c; B[i+1][j+L] = (i, j, toks[i], ch)
    i, j = n, m; path = []
    while (i, j) != (0, 0):
        pi, pj, t, ch = B[i][j]; path.append((t, ch)); i, j = pi, pj
    return path[::-1]
if __name__ == '__main__':
    files = sys.argv[1].split(','); rd = {}
    for line in open(sys.argv[2], encoding='utf8'):
        if ':' in line and not line.startswith('#'):
            k, v = line.split(':', 1); rd[k.strip()] = v.strip()
    L = dict(load(files)); tot = ok = 0
    for name, toks in L.items():
        toks = [t for t in toks if t != '...']
        tot += len(toks)
        if name not in rd: continue
        text = norm(rd[name]).replace('[', '').replace(']', '')
        p = align(toks, text); good = 0; bad = []
        for t, ch in p:
            if t is None: bad.append(f'+{ch}')
            elif ch in vals(t) or (ch == '' and '' in vals(t)): good += 1
            else: bad.append(f'{t}={ch or "null"}')
        ok += good
        print(f'{name:6} {good}/{len(toks)}  ' + ' '.join(bad))
    print(f'read {ok}/{tot} = {ok/tot:.3f}')
