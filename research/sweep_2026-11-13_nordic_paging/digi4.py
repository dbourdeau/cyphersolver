"""Tight-line score for number cipher. Ink mask (900 px spread), connected components; a component is 'digit-like' if h 5-14, w 2-11.
For each 220-px-wide window and each 14-px band: the ink inside the band that belongs to digit-like components must be >= 85% of all ink whose
rows lie within +-10 px of the band (so no ascenders/descenders/long strokes nearby), and the band must hold >= MIN digit-like components.
score = max count over bands. Returns (score, (row, col))."""
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage as ndi
def score(im, W=220, B=14, MIN=8, R=0.6):
    if im.size[1] > im.size[0] * 1.6: im = im.crop((0, 0, im.size[0], int(im.size[0] * 1.3)))
    g = im.convert('L'); bg = g.filter(ImageFilter.GaussianBlur(10))
    m = (np.asarray(bg).astype(int) - np.asarray(g).astype(int)) > 30
    lab, n = ndi.label(m)
    if n == 0: return 0, (0, 0)
    sl = ndi.find_objects(lab); area = ndi.sum(m, lab, range(1, n + 1))
    dig = np.zeros(n + 1, bool)
    for k, s in enumerate(sl):
        h = s[0].stop - s[0].start; w = s[1].stop - s[1].start
        if 5 <= h <= 14 and 2 <= w <= 11 and area[k] >= 6: dig[k + 1] = True
    D = dig[lab] & m
    # centre of mass rows of digit comps
    cy = np.zeros(m.shape, np.int32); pts = np.zeros(m.shape)
    for k, s in enumerate(sl):
        if dig[k + 1]: pts[(s[0].start + s[0].stop) // 2, (s[1].start + s[1].stop) // 2] = 1
    hh, ww = m.shape; best = (0, (0, 0))
    Ip = np.pad(pts.cumsum(0).cumsum(1), ((1, 0), (1, 0))); Ik = np.pad(m.cumsum(0).cumsum(1), ((1, 0), (1, 0))); Id = np.pad(D.cumsum(0).cumsum(1), ((1, 0), (1, 0)))
    f = lambda I, y0, y1, x0, x1: I[y1, x1] - I[y0, x1] - I[y1, x0] + I[y0, x0]
    for y in range(10, hh - B - 10, 4):
        for x in range(0, ww - W, 40):
            c = f(Ip, y, y + B, x, x + W)
            if c < MIN: continue
            tot = f(Ik, y - 10, y + B + 10, x, x + W); d = f(Id, y - 10, y + B + 10, x, x + W)
            if tot > 0 and d >= R * tot and c > best[0]: best = (int(c), (y, x))
    return best
