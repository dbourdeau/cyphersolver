"""Digit-run detector used to triage pages for a closer look (not a verdict).
Idea: numerals in these hands are written as separate small glyphs at an even pitch with no word gaps, while the clear
Swedish/French/Italian text is cursive (long joined components separated by word gaps). On a 1200-px spread the
script binarises the page, takes connected components of glyph size, chains components that sit on one baseline with a
gap under ~0.9 glyph height, and scores each chain of narrow, similar-height components. A long chain (>= MINRUN glyphs)
is a candidate digit run. Output: per image, the number of candidate runs, the longest, and their boxes.

python digitscan.py <dir-of-jpgs> [--boxes] | [--tsv out.tsv]  (tsv: image, strict glyphs, longest strict run, relaxed glyphs)"""
import os
import sys

import cv2
import numpy as np

MINRUN = 9


def components(gray):
    g = cv2.GaussianBlur(gray, (3, 3), 0)
    bw = cv2.adaptiveThreshold(g, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 31, 15)
    n, lab, st, cen = cv2.connectedComponentsWithStats(bw, 8)
    out = []
    for k in range(1, n):
        x, y, w, h, a = st[k]
        if 5 <= h <= 30 and 2 <= w <= 40 and a >= 10:
            out.append((x, y, w, h))
    return out


def runs(comps):
    """Chain glyph-size components left to right along a baseline."""
    comps = sorted(comps, key=lambda c: c[0])
    used = [False] * len(comps)
    xs = np.array([c[0] for c in comps])
    res = []
    for i, c in enumerate(comps):
        if used[i]:
            continue
        chain = [i]
        cur = c
        while True:
            x, y, w, h = cur
            bottom = y + h
            # candidates starting just to the right
            lo = np.searchsorted(xs, x + w - 2)
            hi = np.searchsorted(xs, x + w + max(4, int(0.9 * h)) + 1)
            best = None
            for j in range(lo, hi):
                if used[j] or j in chain:
                    continue
                x2, y2, w2, h2 = comps[j]
                b2 = y2 + h2
                if abs(b2 - bottom) <= max(3, 0.35 * h) and 0.55 <= h2 / h <= 1.8:
                    if best is None or x2 < comps[best][0]:
                        best = j
            if best is None:
                break
            chain.append(best)
            cur = comps[best]
        if len(chain) >= 4:
            for j in chain:
                used[j] = True
            res.append([comps[j] for j in chain])
    return res


def score_chain(ch):
    ws = np.array([c[2] for c in ch], float)
    hs = np.array([c[3] for c in ch], float)
    mh = np.median(hs)
    narrow = np.mean(ws <= 1.15 * mh)  # glyphs about as wide as tall, not long cursive strokes
    hvar = np.std(hs) / mh
    gaps = np.array([ch[k + 1][0] - (ch[k][0] + ch[k][2]) for k in range(len(ch) - 1)], float)
    gvar = (np.std(gaps) / (np.mean(gaps) + 2)) if len(gaps) else 9
    return narrow, hvar, gvar, mh


def scan(path):
    g = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if g is None:
        return None
    cands = []
    for ch in runs(components(g)):
        if len(ch) < MINRUN:
            continue
        narrow, hvar, gvar, mh = score_chain(ch)
        if narrow >= 0.85 and hvar <= 0.35 and gvar <= 0.9:
            x0 = min(c[0] for c in ch); y0 = min(c[1] for c in ch)
            x1 = max(c[0] + c[2] for c in ch); y1 = max(c[1] + c[3] for c in ch)
            cands.append((len(ch), (x0, y0, x1, y1)))
    return cands


def features(path):
    """Strict score (narrow glyph chains, as scan()) and a relaxed score (any width, even height and pitch)."""
    g = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if g is None:
        return None
    rs = [r for r in runs(components(g)) if len(r) >= MINRUN]
    strict = relaxed = 0
    longest = 0
    for r in rs:
        narrow, hvar, gvar, mh = score_chain(r)
        if narrow >= 0.85 and hvar <= 0.35 and gvar <= 0.9:
            strict += len(r)
            longest = max(longest, len(r))
        if hvar <= 0.3 and gvar <= 0.5:
            relaxed += len(r)
    return strict, longest, relaxed


def scan_volume(d, out):
    files = sorted((f for f in os.listdir(d) if f.endswith('.jpg')), key=lambda f: int(f.split('.')[0]))
    with open(out, 'w') as fh:
        for f in files:
            s = features(os.path.join(d, f))
            if s:
                fh.write(f"{f.split('.')[0]}\t{s[0]}\t{s[1]}\t{s[2]}\n")
    return out


if __name__ == '__main__':
    d = sys.argv[1]
    if '--tsv' in sys.argv:
        print(scan_volume(d, sys.argv[sys.argv.index('--tsv') + 1]))
        sys.exit()
    files = sorted((f for f in os.listdir(d) if f.endswith('.jpg')), key=lambda f: int(f.split('.')[0]))
    for f in files:
        c = scan(os.path.join(d, f))
        if c is None:
            continue
        L = sorted((k for k, _ in c), reverse=True)
        print(f.split('.')[0], len(c), sum(L), L[:8], [b for _, b in c][:3] if '--boxes' in sys.argv else '')
