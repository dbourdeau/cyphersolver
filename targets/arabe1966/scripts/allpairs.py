"""Digit-level substitution, both directions: fix digits 1 and 2 to every ordered pair of letters in turn, search the
other five digits with the classical vocabulary (classical.py machinery), keep the global best segmentations."""
import json, math, re, sys, collections, itertools
def norm(w):
    w = re.sub('[ً-ْـٰ]', '', w)
    for a,b in (('أ','ا'),('إ','ا'),('آ','ا'),('ٱ','ا'),('ى','ي'),('ة','ه'),('ؤ','و'),('ئ','ي'),('ء','')): w = w.replace(a,b)
    return w
ARS = "ابجدهوزحطيكلمنسعفصقرشتثخذضظغ"; AR = set(ARS)
raw = open(sys.argv[1], encoding='utf-8').read()
cnt = collections.Counter(w for w in (norm(x) for x in re.findall('[ء-ْٰٱ]+', raw)) if w and not (set(w) - AR))
tot = sum(cnt.values())
words = {w: math.log10(c / tot) for w, c in cnt.items() if c >= 3 and (len(w) > 1 or w == 'و')}
def pat(t):
    d = {}; return tuple(d.setdefault(c, len(d)) for c in t)
bypat = collections.defaultdict(list)
for w, lf in words.items(): bypat[pat(w)].append((w, lf))
LTR = "71589217218921518421924"
BON, PEN, KEEP = 0.75, 1.0, 2.5
G = []
def solve(s, fix, tag):
    fixrev = {v: k for k, v in fix.items()}; n = len(s); cand = {}
    for i in range(n):
        for L in range(1, min(9, n - i) + 1):
            t = s[i:i+L]
            c = [(w, lf) for w, lf in bypat.get(pat(t), ()) if all(fix.get(a, b) == b and fixrev.get(b, a) == a for a, b in zip(t, w))]
            if c: c.sort(key=lambda x: -x[1]); cand[i, L] = c
    ub = [0.0] * (n + 1)
    for i in range(n - 1, -1, -1):
        ub[i] = max([cand[i, L][0][1] + BON*L - PEN + ub[i+L] for L in range(1, 10) if (i, L) in cand] or [-1e9])
    if ub[0] < -16: return
    best = [-16.0]; nodes = [0]
    def dfs(i, m, used, sc, ws):
        nodes[0] += 1
        if nodes[0] > 400000: return
        if i == n:
            G.append((sc, ' '.join(ws), tag)); best[0] = max(best[0], sc); return
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
for dname, s in (('rtl', LTR[::-1]), ('ltr', LTR)):
    for x, y in itertools.permutations(ARS, 2):
        solve(s, {'1': x, '2': y}, f"{dname} 1={x} 2={y}")
G.sort(reverse=True)
seen = set()
for sc, k, tag in G:
    if k in seen: continue
    seen.add(k); print("%.1f" % sc, k, ' |', tag)
    if len(seen) >= 60: break
