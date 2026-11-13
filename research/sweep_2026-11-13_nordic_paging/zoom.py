"""python zoom.py <man> i j ... : for each image, the 390x260 window round the digi.score maximum of the local 900 px copy at native scale, 12 a sheet"""
import sys, os
import numpy as np
from PIL import Image, ImageFilter
import rik
man = sys.argv[1]; ids = [int(x) for x in sys.argv[2:]]; d = f'{rik.SP}/pg/{man}'
def win(im, W=390, H=260):
    g = im.convert('L'); bg = g.filter(ImageFilter.GaussianBlur(12))
    m = ((np.asarray(bg).astype(int) - np.asarray(g).astype(int)) > 28).astype(float)
    I = m.cumsum(0).cumsum(1); h, w = m.shape; best = (-1, 0, 0)
    for r in range(0, max(1, h - H), 20):
        for c in range(0, max(1, w - W), 20):
            s = I[min(h - 1, r + H), min(w - 1, c + W)] - I[r, min(w - 1, c + W)] - I[min(h - 1, r + H), c] + I[r, c]
            if s > best[0]: best = (s, r, c)
    _, r, c = best; return g.crop((c, r, c + W, r + H))
import digi
def win(im, W=390, H=260):
    g = im.convert('L'); sc, (r, c) = digi.score(g); cx, cy = c + 100, r + 60
    x0 = max(0, min(g.size[0] - W, cx - W // 2)); y0 = max(0, min(g.size[1] - H, cy - H // 2)); return g.crop((x0, y0, x0 + W, y0 + H))
for k in range(0, len(ids), 12):
    ch = ids[k:k + 12]; tiles = [win(Image.open(f'{d}/{i:05d}.jpg')) for i in ch]
    print(rik.grid(tiles, ch, 4, 390, f'{rik.SP}/ps/{man}_z_{ch[0]}.jpg'))
