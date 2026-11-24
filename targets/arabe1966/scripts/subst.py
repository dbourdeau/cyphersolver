"""H1: plain substitution, one digit = one letter. Word segmentation with a consistent, injective digit->letter map,
scored by word frequency. Words are pre-filtered per position by repeat pattern and by the fixed letters.
Usage: subst.py [rtl|ltr] [fix] [N]   (fix: 1=ا, 2=ل; N = vocabulary size, default 20000)"""
import math, re, sys
from wordfreq import top_n_list, word_frequency
def norm(w):
    w = re.sub('[ً-ْـ]', '', w)
    for a,b in (('أ','ا'),('إ','ا'),('آ','ا'),('ى','ي'),('ة','ه'),('ؤ','و'),('ئ','ي'),('ء','')): w = w.replace(a,b)
    return w
AR = set("ابجدهوزحطيكلمنسعفصقرشتثخذضظغ")
args = sys.argv[1:]
N = next((int(a) for a in args if a.isdigit()), 20000)
words = {}
for w in top_n_list('ar', N):
    n = norm(w)
    if not n or set(n) - AR: continue
    if len(n) == 1 and n != 'و': continue
    words[n] = max(words.get(n, 0), word_frequency(w, 'ar'))
def pat(t):
    d = {}; return tuple(d.setdefault(c, len(d)) for c in t)
bypat = {}
for w, f in words.items(): bypat.setdefault(pat(w), []).append((w, math.log10(f)))
LTR = "71589217218921518421924"
s = LTR if 'ltr' in args else LTR[::-1]
fix = {'1': 'ا', '2': 'ل'} if 'fix' in args else {}
fixrev = {v: k for k, v in fix.items()}
cand = {}
for i in range(len(s)):
    for L in range(1, min(9, len(s) - i) + 1):
        t = s[i:i+L]
        c = [(w, lf) for w, lf in bypat.get(pat(t), ())
             if all((fix.get(a, b) == b) and (fixrev.get(b, a) == a) for a, b in zip(t, w))]
        c.sort(key=lambda x: -x[1])
        if c: cand[i, L] = c
out = []
BON = 0.9; PEN = 1.5
# optimistic bound on the rest of the string, ignoring consistency
ub = [0.0] * (len(s) + 1)
for i in range(len(s) - 1, -1, -1):
    ub[i] = max([cand[i, L][0][1] + BON*L - PEN + ub[i+L] for L in range(1, 10) if (i, L) in cand] or [-1e9])
best = [-1e9]; KEEP = 12.0
def dfs(i, m, used, sc, ws):
    if sc + ub[i] < best[0] - KEEP: return
    if i == len(s):
        out.append((sc, ws, m)); best[0] = max(best[0], sc); return
    for L in range(min(9, len(s) - i), 0, -1):
        t = s[i:i+L]
        for w, lf in cand.get((i, L), ()):
            m2 = dict(m); u2 = set(used); ok = True
            for a, b in zip(t, w):
                cur = m2.get(a)
                if cur is None:
                    if b in u2: ok = False; break
                    m2[a] = b; u2.add(b)
                elif cur != b: ok = False; break
            if ok: dfs(i+L, m2, u2, sc + lf + BON*L - PEN, ws + [w])
dfs(0, dict(fix), set(fix.values()), 0.0, [])
out.sort(key=lambda x: -x[0])
print(len(out), "segmentations kept;", s, "ub", round(ub[0], 1))
seen = set()
for sc, ws, m in out:
    k = ' '.join(ws)
    if k in seen: continue
    seen.add(k); print("%.1f" % sc, k, ' ', ''.join(f"{d}{m[d]}" for d in sorted(m)))
    if len(seen) >= 40: break
