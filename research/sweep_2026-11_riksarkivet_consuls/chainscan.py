"""find long gapless ink chains (Molinari's unbroken digit rows) on 1200-px spreads.
python chainscan.py <dir> [imgs...]  -> image, n_long_chains, details"""
import os
import sys

import cv2
import numpy as np

D = sys.argv[1]
DIL = int(os.environ.get('DIL', '5'))
MINW = float(os.environ.get('MINW', '0.30'))


def scan(p):
    g = cv2.imread(p, cv2.IMREAD_GRAYSCALE)
    H, W = g.shape
    spread = W > 0.95 * H
    pw = W / 2 if spread else W
    b = cv2.GaussianBlur(g, (3, 3), 0)
    bw = cv2.adaptiveThreshold(b, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 31, 15)
    # remove specks
    bw = cv2.morphologyEx(bw, cv2.MORPH_OPEN, np.ones((2, 2), np.uint8))
    k = cv2.getStructuringElement(cv2.MORPH_RECT, (DIL, 1))
    d = cv2.dilate(bw, k)
    n, lab, st, cen = cv2.connectedComponentsWithStats(d, 8)
    hits = []
    for i in range(1, n):
        x, y, w, h, a = st[i]
        if w < MINW * pw or h > 40 or h < 6 or x < 3 or y < 3 or x + w > W - 3 or y + h > H - 3 or w > 1.05 * pw:
            continue
        # ink fill within the component: digits fill densely; dashes/underlines are thin
        sub = bw[y:y + h, x:x + w]
        cols = (sub > 0).any(axis=0).mean()  # fraction of columns with ink
        hgt = (sub > 0).sum(axis=0)
        mh = np.median(hgt[hgt > 0]) if (hgt > 0).any() else 0
        if cols < 0.75 or mh < 3:
            continue
        hits.append((x, y, w, h, round(cols, 2), int(mh)))
    return hits


files = sys.argv[2:] or sorted((f.split('.')[0] for f in os.listdir(D) if f.endswith('.jpg')), key=int)
for f in files:
    h = scan(os.path.join(D, f'{f}.jpg'))
    print(f, len(h), ' '.join(f'{x},{y},{w}' for x, y, w, *_ in h[:6]), flush=True)
