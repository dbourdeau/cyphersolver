"""Align the /73 cipher signs (transcription/d73_transcription.md) with the clear paragraph, sign by sign.

Each sign emits 0, 1 or 2 plaintext letters. Starting from the seed key in dec1474.py, the alignment is redone
until the key stops changing; the key taken is the majority value of each sign over the alignment.
"""
import re, sys
from collections import Counter, defaultdict

PLAIN = ("noresmenossenyoryohesabidocomoelmatrimoniodelainfantamiermananoseesrompidosegunt"
         "stavapraticadoeconcertadodequemesoadmiradoypuesassiessupplicohumilmentevraalteza"
         "leremededeloquemepmendoquesiayehombrealgunoanapolsporestosfechosquevayamossen"
         "santclimentporqueyendoellmisfechossefacanabueltasdelosotroseassiseseguiragrant"
         "benefficio")

def signs(path):
    blk = re.search(r'```(.*?)```', open(path).read(), re.S).group(1)
    out = []
    for ln in blk.splitlines():
        m = re.match(r'(K\d\d) (.*)', ln)
        if m:
            for t in re.findall(r'"[^"]*"|\S+', m.group(2)):
                if not t.startswith('"') and t not in ('/', '//'):
                    out.append((m.group(1), t))
    return out

SEED = dict(p.split('=') for p in "tt=m o-=t y°=r q=i lp=m 9.=o 6=n ro=i 2f:=o A=e d=a 7=n -+-=s l=f oo=e -o-=s 3-=n +=a o-o=e".split())

def align(S, P, key):
    n, m = len(S), len(P)
    INF = 10**9
    D = [[INF] * (m + 1) for _ in range(n + 1)]
    B = [[None] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0
    for j in range(1, m + 1):          # plaintext letters with no sign (dropped by the cipher clerk)
        D[0][j] = D[0][j - 1] + 3; B[0][j] = ('skip', 1)
    for i in range(1, n + 1):
        s = S[i - 1][1]
        v = key.get(s)
        for j in range(0, m + 1):
            best, arg = INF, None
            # null sign
            c = D[i - 1][j] + (0 if v == '' else 2)
            if c < best: best, arg = c, ('null', 0)
            for k in (1, 2):
                if j >= k:
                    seg = P[j - k:j]
                    if v is None:
                        cost = 1 if k == 1 else 2
                    else:
                        cost = 0 if seg == v else (3 if k == 1 else 4)
                    c = D[i - 1][j - k] + cost
                    if c < best: best, arg = c, ('emit', k)
            if j >= 1 and D[i][j - 1] + 3 < best:
                best, arg = D[i][j - 1] + 3, ('skip', 1)
            D[i][j], B[i][j] = best, arg
    # trace back
    i, j, pairs = n, m, []
    while i > 0 or j > 0:
        a = B[i][j]
        if a[0] == 'skip':
            pairs.append((None, P[j - 1])); j -= 1
        elif a[0] == 'null':
            pairs.append((S[i - 1], '')); i -= 1
        else:
            k = a[1]; pairs.append((S[i - 1], P[j - k:j])); i -= 1; j -= k
    return D[n][m], pairs[::-1]

def main():
    S = signs(sys.argv[1])
    key = dict(SEED)
    for it in range(8):
        cost, pairs = align(S, PLAIN, key)
        votes = defaultdict(Counter)
        for s, p in pairs:
            if s: votes[s[1]][p] += 1
        new = {s: c.most_common(1)[0][0] for s, c in votes.items()}
        if new == key: break
        key = new
    print('cost', cost, 'iterations', it + 1)
    for s, c in sorted(votes.items(), key=lambda kv: -sum(kv[1].values())):
        print(f"{s:6} {sum(c.values()):3}  " + ' '.join(f"{v or '-'}:{n}" for v, n in c.most_common()))
    print()
    line = None; buf = []
    for s, p in pairs:
        if s and s[0] != line:
            if buf: print(line, ' '.join(buf))
            line, buf = s[0], []
        buf.append(f"{s[1] if s else '+'}={p or '-'}")
    print(line, ' '.join(buf))
    if len(sys.argv) > 2:                     # also write the pairs for docs/_validate.py
        with open(sys.argv[2], 'w') as f:
            f.write('# model: es-golden-age\n# source: transcription/d73_transcription.md aligned on '
                    'decryption/d73_clear.md (align1474.py); d64 (1473) is a different cipher and is not in this file\n'
                    '# note: per-occurrence values from the alignment; "-" = the sign reads as nothing\n')
            for s, p in pairs:
                if s: f.write(f"{s[1]}\t{p or '-'}\n")

main()
