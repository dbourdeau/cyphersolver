"""Held-out test (run once, 14 Nov 2026): frozen key on the cipher of 1410,135 against the contemporary decipherment 1410,110.
Normalisation: accents dropped, v=u, y=i=j, ç=z, initial h dropped, doubled letters simplified. Characters = 1 - Levenshtein/len(clear);
a word counts when all its letters align. Controls: 100 permutations of the consonant values (seeds 1-100) and 100 shuffles of the unit order (seeds 1-100).
Usage: python3 scripts/heldout.py key_frozen.json transcription_1410_135.txt plaintext_1410_110.txt"""
import json, random, re, sys, unicodedata, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from decode import decode, units
def norm(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    s = s.replace('v', 'u').replace('y', 'i').replace('j', 'i').replace('ç', 'z')
    s = re.sub(r'[^a-z? ]', '', s); s = re.sub(r'(?<![a-z])h', '', s); return re.sub(r'([a-z])\1+', r'\1', s)
def score(dec, clear):
    words = norm(clear).split(); a = ''.join(words); b = norm(dec).replace(' ', ''); n, m = len(a), len(b)
    D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1): D[i][0] = i
    for j in range(m + 1): D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1): D[i][j] = min(D[i-1][j] + 1, D[i][j-1] + 1, D[i-1][j-1] + (a[i-1] != b[j-1]))
    i, j = n, m; ok = [False] * n; ins = [0] * (n + 1)
    while i > 0 or j > 0:
        if i > 0 and j > 0 and D[i][j] == D[i-1][j-1] + (a[i-1] != b[j-1]): ok[i-1] = a[i-1] == b[j-1]; i -= 1; j -= 1
        elif i > 0 and D[i][j] == D[i-1][j] + 1: i -= 1
        else: ins[i] += 1; j -= 1
    pos = good = 0
    for w in words:
        L = len(w); good += all(ok[pos:pos+L]) and not any(ins[pos+1:pos+L]); pos += L
    return good / len(words), 1 - D[n][m] / n, len(words), n
K = json.load(open(sys.argv[1], encoding='utf-8')); U = units(sys.argv[2])
clear = ' '.join(l.strip() for l in open(sys.argv[3], encoding='utf-8') if l.strip() and not l.startswith('#'))
w, c, nw, nc = score(decode(U, K), clear); print(f'frozen key: words {w:.3f}  characters {c:.3f}  ({nw} words, {nc} characters)')
W, C = [], []; nums = list(K['cons'])
for s in range(1, 101):
    r = random.Random(s); v = [K['cons'][k] for k in nums]; r.shuffle(v); K2 = dict(K); K2['cons'] = dict(zip(nums, v))
    a, b, _, _ = score(decode(U, K2), clear); W.append(a); C.append(b)
flat = [u for l in U for u in l]
for s in range(1, 101):
    r = random.Random(s); f = flat[:]; r.shuffle(f); a, b, _, _ = score(decode([f], K), clear); W.append(a); C.append(b)
print(f'200 controls: words max {max(W):.3f} mean {sum(W)/200:.3f} | characters max {max(C):.3f} mean {sum(C)/200:.3f}')
print('criterion (characters >= 0.85 and >= best control + 0.30):', 'met' if c >= 0.85 and c >= max(C) + 0.30 else 'not met')
