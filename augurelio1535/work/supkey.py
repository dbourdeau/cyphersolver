"""Supervised key: align human readings (NN <text>) to the sign lines of a transcription and count values.
Each sign emits 0-3 letters; DP maximises sum log P(value|sign) from a prior key (unknown value = -6).
  python supkey.py prior.json out.json trans1.txt read1.txt [trans2.txt read2.txt ...]
"""
import re, sys, json, math
from collections import defaultdict, Counter
P = json.load(open(sys.argv[1], encoding='utf8'))
def toks(s):
    s = re.sub(r'\{[^}]*\}', '', s).replace('a+', 'B').replace('o-', '%').replace('E+', 'Z').replace('ɔo', 'ɔ').replace('ꝏo', 'ꝏ')
    s = re.sub(r'\[[^\]]*\]', '', s)
    return re.sub(r'[-.:~?> ]', '', s)
def norm(r):
    r = re.sub(r'\[[^\]]*\]', '', r.lower())
    r = r.replace('ä', 'a').replace('ö', 'o').replace('ü', 'u').replace('ß', 'ss').replace('j', 'i').replace('v', 'u').replace('y', 'i')
    return re.sub(r'[^a-z]', '', r)
def sc(g, v):
    d = P.get(g, {})
    if v in d: return math.log(d[v])
    if v == '': return -7
    return -5.0 - 1.0 * (len(v) - 1)
cnt = defaultdict(Counter); tot = 0
args = sys.argv[3:]
for tf, rf in zip(args[::2], args[1::2]):
    T = {m.group(1): toks(m.group(2)) for m in (re.match(r'(\d\d) (.*)', l) for l in open(tf, encoding='utf8')) if m}
    R = {}
    for l in open(rf, encoding='utf8'):
        m = re.match(r'\s*(\d\d)\s+(.*)', l)
        if m and m.group(1) in T and m.group(1) not in R: R[m.group(1)] = m.group(2)
    for no, r in R.items():
        if '[..' in r or '?' in r:  # use only confident stretches: drop words with ? and unreadable runs
            pass
        s = T[no]; t = norm(r)
        n, m = len(s), len(t)
        if not n or not m or abs(n - m) > 0.4 * n + 6: continue
        NEG = -1e9
        D = [[NEG] * (m + 1) for _ in range(n + 1)]; B = [[None] * (m + 1) for _ in range(n + 1)]
        D[0][0] = 0
        for i in range(n):
            for j in range(m + 1):
                if D[i][j] == NEG: continue
                for L in (0, 1, 2, 3):
                    if j + L > m: break
                    v = D[i][j] + sc(s[i], t[j:j + L])
                    if v > D[i + 1][j + L]: D[i + 1][j + L] = v; B[i + 1][j + L] = (j, t[j:j + L])
        if D[n][m] == NEG: continue
        j = m; al = []
        for i in range(n, 0, -1):
            pj, v = B[i][j]; al.append((s[i - 1], v)); j = pj
        # skip lines whose alignment is poor (mean score very low)
        if D[n][m] / n < -2.5: continue
        tot += 1
        for g, v in al: cnt[g][v] += 1
out = {}
for g, c in cnt.items():
    N = sum(c.values())
    out[g] = {v: round((k + 0.3) / (N + 1), 3) for v, k in c.most_common(5) if v != '' or k > 2}
json.dump(out, open(sys.argv[2], 'w', encoding='utf8'), ensure_ascii=False, indent=0)
print('lines aligned', tot)
for g in sorted(out): print(g, dict(cnt[g].most_common(6)))
