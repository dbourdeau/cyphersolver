#!/usr/bin/env python3
"""eaglepass1917: simple-substitution solver per PLAN.md (SHA-256 in PLAN.sha256)."""
import re, sys, os, json, glob, math, random, unicodedata
import numpy as np

HC = "/Users/sharedprojects/Documents/Shared Projects/Historical Ciphers"
OUT = HC + "/output/eaglepass1917_2026-11-23"
REPO = HC + "/sources/raw/db_repo_2026-11-22/repo/targets"
SANT = HC + "/sources/raw/ill_photo_leads_2026-11-23/archivosantander14bogo/archivosantander14bogo_djvu.txt"
CORPUS_TARGETS = "coahuila1906 delabarra1913 fuentes1914 gonzalez1913 hernandez1911 mccarty1911 mexico1911 murguia1914 nuevaclave1911 rubio1913 limantour1909 dallas1911 carranza1914".split()
A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def norm(s):
    s = s.replace('ñ', 'n').replace('Ñ', 'N')
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return s.upper()

def letters(s): return re.sub('[^A-Z]', '', norm(s))

def corpus_text():
    parts = [open(SANT, encoding='utf-8', errors='ignore').read()]
    for t in CORPUS_TARGETS:
        for f in sorted(glob.glob(f"{REPO}/{t}/decryption*.txt") + glob.glob(f"{REPO}/{t}/reading*.md")):
            parts.append(open(f, encoding='utf-8', errors='ignore').read())
    return '\n'.join(parts)

def build_model():
    raw = corpus_text()
    words = re.findall('[A-Z]+', norm(raw))
    L = letters(raw)
    x = np.frombuffer(L.encode(), dtype=np.uint8) - 65
    idx = ((x[:-3].astype(np.int64) * 26 + x[1:-2]) * 26 + x[2:-1]) * 26 + x[3:]
    cnt = np.bincount(idx, minlength=26 ** 4).astype(np.float64) + 0.5
    lp = np.log(cnt / cnt.sum())
    from collections import Counter
    wc = Counter(words)
    wl = {w for w, n in wc.items() if n >= 3 and (len(w) >= 2 or w in ('Y', 'A', 'O', 'E', 'U'))}
    return lp, wl, len(L), wc

def to_int(s): return np.frombuffer(s.encode(), dtype=np.uint8).astype(np.int64) - 65

def score_int(p, lp):
    idx = ((p[:-3] * 26 + p[1:-2]) * 26 + p[2:-1]) * 26 + p[3:]
    return float(lp[idx].sum())

def anneal(c, lp, seed, steps=20000, t0=10.0, t1=0.2):
    rng = random.Random(seed)
    key = list(range(26)); rng.shuffle(key)   # key[cipher] = plain
    k = np.array(key)
    cur = score_int(k[c], lp); best, bestk = cur, k.copy()
    for i in range(steps):
        T = t0 * (t1 / t0) ** (i / steps)
        a, b = rng.randrange(26), rng.randrange(26)
        if a == b: continue
        k[a], k[b] = k[b], k[a]
        s = score_int(k[c], lp)
        if s >= cur or rng.random() < math.exp((s - cur) / T):
            cur = s
            if s > best: best, bestk = s, k.copy()
        else:
            k[a], k[b] = k[b], k[a]
    k = bestk.copy(); cur = best
    improved = True
    while improved:
        improved = False
        for a in range(26):
            for b in range(a + 1, 26):
                k[a], k[b] = k[b], k[a]
                s = score_int(k[c], lp)
                if s > cur + 1e-9: cur = s; improved = True
                else: k[a], k[b] = k[b], k[a]
    return cur, k

def solve(ctext, lp, base, restarts=40, tag=''):
    c = to_int(ctext)
    rows = []
    for r in range(1, restarts + 1):
        s, k = anneal(c, lp, base + r)
        rows.append((base + r, s, ''.join(A[v] for v in k), ''.join(A[v] for v in k[c])))
    rows.sort(key=lambda x: -x[1])
    with open(f"{OUT}/runs/{tag}.tsv", 'w') as f:
        f.write("seed\tscore\tkey_cipher_ABC_to_plain\tdecryption\n")
        for row in sorted(rows):
            f.write(f"{row[0]}\t{row[1]:.3f}\t{row[2]}\t{row[3]}\n")
    return rows

def coverage(p, wl):
    n = len(p); best = [0] * (n + 1)
    for i in range(1, n + 1):
        best[i] = best[i - 1]
        for j in range(max(0, i - 15), i - 2):
            if p[j:i] in wl: best[i] = max(best[i], best[j] + (i - j))
    return best[n] / n
