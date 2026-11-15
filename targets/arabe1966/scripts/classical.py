"""Substitution search scored with a classical Arabic vocabulary (Sahih al-Bukhari, hadith-json).
Usage: classical.py CORPUS.json MODE [fix]
MODE: digits-rtl | digits-ltr | tok21-rtl | tok21-ltr | tok12-rtl | tok12-ltr
One cipher symbol = one letter, injective; word boundaries free; depth-first with an optimistic bound."""
import json, math, re, sys, collections
def norm(w):
    w = re.sub('[ً-ْـٰ]', '', w)
    for a,b in (('أ','ا'),('إ','ا'),('آ','ا'),('ٱ','ا'),('ى','ي'),('ة','ه'),('ؤ','و'),('ئ','ي'),('ء','')): w = w.replace(a,b)
    return w
AR = set("ابجدهوزحطيكلمنسعفصقرشتثخذضظغ")
raw = open(sys.argv[1], encoding='utf-8').read()
cnt = collections.Counter(w for w in (norm(x) for x in re.findall('[ء-ْٰٱ]+', raw)) if w and not (set(w) - AR))
tot = sum(cnt.values())
words = {w: math.log10(c / tot) for w, c in cnt.items() if c >= 3 and (len(w) > 1 or w == 'و')}
print(len(words), "word forms from", tot, "tokens", file=sys.stderr)
def pat(t):
    d = {}; return tuple(d.setdefault(c, len(d)) for c in t)
bypat = collections.defaultdict(list)
for w, lf in words.items(): bypat[pat(w)].append((w, lf))
LTR = "71589217218921518421924"
mode = sys.argv[2]
if mode.startswith('digits'): s = list(LTR)
elif mode.startswith('tok21'): s = "7 15 8 9 21 7 21 8 9 21 5 18 4 21 9 24".split()
else: s = "17 5 8 9 12 7 12 8 9 12 15 8 4 12 9 2 4".split()
if mode.endswith('rtl'): s = s[::-1]
fix = {'1': 'ا', '2': 'ل'} if 'fix' in sys.argv else {}
fixrev = {v: k for k, v in fix.items()}
n = len(s); cand = {}
for i in range(n):
    for L in range(1, min(9, n - i) + 1):
        t = s[i:i+L]
        c = [(w, lf) for w, lf in bypat.get(pat(t), ()) if all(fix.get(a, b) == b and fixrev.get(b, a) == a for a, b in zip(t, w))]
        c.sort(key=lambda x: -x[1])
        if c: cand[i, L] = c[:4000]
BON, PEN = 0.75, 1.0
ub = [0.0] * (n + 1)
for i in range(n - 1, -1, -1):
    ub[i] = max([cand[i, L][0][1] + BON*L - PEN + ub[i+L] for L in range(1, 10) if (i, L) in cand] or [-1e9])
out = []; best = [-1e9]; KEEP = 5.0; nodes = [0]
def dfs(i, m, used, sc, ws):
    nodes[0] += 1
    if sc + ub[i] < best[0] - KEEP or nodes[0] > 60_000_000: return
    if i == n:
        out.append((sc, ws, m)); best[0] = max(best[0], sc); return
    for L in range(min(9, n - i), 0, -1):
        t = s[i:i+L]
        for w, lf in cand.get((i, L), ()):
            sc2 = sc + lf + BON*L - PEN
            if sc2 + ub[i+L] < best[0] - KEEP: break
            m2 = dict(m); u2 = set(used); ok = True
            for a, b in zip(t, w):
                cur = m2.get(a)
                if cur is None:
                    if b in u2: ok = False; break
                    m2[a] = b; u2.add(b)
                elif cur != b: ok = False; break
            if ok: dfs(i+L, m2, u2, sc2, ws + [w])
dfs(0, dict(fix), set(fix.values()), 0.0, [])
out.sort(key=lambda x: -x[0])
print(mode, 'fix' if fix else '', len(out), "kept; nodes", nodes[0], "ub %.1f" % ub[0])
seen = set()
for sc, ws, m in out:
    k = ' '.join(ws)
    if k in seen: continue
    seen.add(k); print("%.1f" % sc, k, ' ', ' '.join(f"{d}={m[d]}" for d in sorted(m, key=int)))
    if len(seen) >= 25: break
