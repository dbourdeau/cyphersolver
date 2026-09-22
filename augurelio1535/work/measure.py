"""Measure a reading against its transcription: align letters to signs (DP, 0-3 letters per sign), then a word
counts as read when it has no '?', and every sign under it takes an established value (>= 5% of that sign's
aligned uses and seen at least twice, counted over all pages given). Prints per-page and total fractions.
  python measure.py trans1 read1 [trans2 read2 ...]
"""
import re, sys, math, os
FAIL = []
SLIP = int(os.environ.get('SLIP', 0))
from collections import defaultdict, Counter
def toks(s):
    s = re.sub(r'\{[^}]*\}', '', s).replace('a+', 'B').replace('o-', '%').replace('E+', 'Z').replace('ɔo', 'ɔ').replace('ꝏo', 'ꝏ')
    s = re.sub(r'\[[^\]]*\]', '', s)
    return re.sub(r'[-.:~?> ]', '', s)
def normw(w):
    w = w.lower().replace('ä', 'a').replace('ö', 'o').replace('ü', 'u').replace('ß', 'ss').replace('j', 'i').replace('v', 'u').replace('y', 'i')
    return re.sub(r'[^a-z]', '', w)
pairs = sys.argv[1:]
data = []
for tf, rf in zip(pairs[::2], pairs[1::2]):
    T = {m.group(1): toks(m.group(2)) for m in (re.match(r'(\d\d) (.*)', l) for l in open(tf, encoding='utf8')) if m}
    R = {}
    for l in open(rf, encoding='utf8'):
        m = re.match(r'\s*(\d\d)\s+(.*)', l)
        if m and m.group(1) in T and m.group(1) not in R: R[m.group(1)] = m.group(2)
    data.append((rf, T, R))

def align(s, words, P):
    t = ''.join(w for w, _ in words); owner = [i for i, (w, _) in enumerate(words) for _ in w]
    n, m = len(s), len(t)
    def sc(g, v):
        d = P.get(g)
        if not d: return -3.0 if v else -6
        c = d.get(v, 0); N = sum(d.values())
        return math.log((c + 0.2) / (N + 1)) if (c or v) else -6
    NEG = -1e18
    D = [[NEG] * (m + 1) for _ in range(n + 1)]; B = [[None] * (m + 1) for _ in range(n + 1)]; D[0][0] = 0
    for i in range(n):
        for j in range(m + 1):
            if D[i][j] == NEG: continue
            for L in (0, 1, 2, 3):
                if j + L > m: break
                v = D[i][j] + sc(s[i], t[j:j + L])
                if v > D[i + 1][j + L]: D[i + 1][j + L] = v; B[i + 1][j + L] = (j, t[j:j + L])
    if D[n][m] == NEG: return None
    j = m; al = []
    for i in range(n, 0, -1):
        pj, v = B[i][j]; al.append((s[i - 1], v, owner[pj] if v else (owner[pj] if pj < m else len(words) - 1))); j = pj
    return al[::-1]

def words_of(r):
    out = []
    for w in re.sub(r'\[[^\]]*[A-Za-z][^\]]*\]', ' ', r).split():
        if w.startswith('[..'): out.append(('', True)); continue
        doubt = '?' in w or '[' in w
        nw = normw(w)
        if nw: out.append((nw, doubt))
        elif doubt: out.append(('', True))
    return out

P = {}
for it in range(3):
    cnt = defaultdict(Counter); res = []
    for rf, T, R in data:
        good = tot = 0
        for no, r in R.items():
            ws = words_of(r); real = [(w, d) for w, d in ws if w]
            tot += len(ws)
            al = align(T[no], real, P) if real else None
            if al is None: continue
            ok = [not d for _, d in real]; bad = [0] * len(real); why = ['?' if d else '' for _, d in real]
            for g, v, wi in al:
                cnt[g][v] += 1
                if P:
                    c = P.get(g, Counter()); N = sum(c.values()) or 1
                    if N > 3 and (c.get(v, 0) < 2 or c.get(v, 0) / N < 0.05): bad[wi] += 1; ok[wi] = ok[wi] and bad[wi] <= SLIP; why[wi] += f' {g}={v or "_"}'
            good += sum(ok)
            if it == 2 and os.environ.get('V'): FAIL.append((rf, no, [(w, y) for (w, _), o, y in zip(real, ok, why) if not o]))
        res.append((rf, good, tot))
    P = cnt
for rf, g, t in res: print(f'{rf}: {g}/{t} words read = {g / max(t, 1):.3f}')
G = sum(g for _, g, _ in res); Tt = sum(t for *_, t in res)
print(f'TOTAL {G}/{Tt} = {G / max(Tt, 1):.3f}')

for rf, no, f in FAIL:
    if f: print(rf[:2], no, '; '.join(f'{w}[{y.strip()}]' for w, y in f))
