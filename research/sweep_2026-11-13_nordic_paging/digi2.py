"""Dot-separated digit-group score: a dot (area 3-40, w,h<=6) at the baseline between two digit-sized glyphs (w 2-12, h 6-16) on the same baseline.
score = max count of such dot triples in a 220x130 window (900 px spread). Returns (score, (row, col))"""
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage as ndi
def score(im, W=220, H=130):
    if im.size[1] > im.size[0] * 1.6: im = im.crop((0, 0, im.size[0], int(im.size[0] * 1.3)))
    g = im.convert('L'); bg = g.filter(ImageFilter.GaussianBlur(10))
    m = (np.asarray(bg).astype(int) - np.asarray(g).astype(int)) > 30
    lab, n = ndi.label(m)
    if n == 0: return 0, (0, 0)
    sl = ndi.find_objects(lab); dg = []; dots = []
    for s in sl:
        h = s[0].stop - s[0].start; w = s[1].stop - s[1].start; a = (m[s]).sum()
        if 6 <= h <= 16 and 2 <= w <= 12: dg.append((s[0].stop, (s[1].start + s[1].stop) / 2))
        elif h <= 6 and w <= 6 and 3 <= a <= 40: dots.append((s[0].stop, (s[1].start + s[1].stop) / 2))
    if not dg or not dots: return 0, (0, 0)
    dg = np.array(dg); pts = np.zeros(m.shape)
    for (by, cx) in dots:
        # digits on the left and right within 14 px, bottoms within 3 px of the dot bottom
        near = dg[(abs(dg[:, 0] - by) <= 3) & (abs(dg[:, 1] - cx) <= 14) & (abs(dg[:, 1] - cx) >= 2)]
        if (near[:, 1] < cx).any() and (near[:, 1] > cx).any(): pts[int(by), int(cx)] = 1
    I = np.pad(pts.cumsum(0).cumsum(1), ((1, 0), (1, 0))); hh, ww = pts.shape
    if hh <= H or ww <= W: return int(pts.sum()), (0, 0)
    S = I[H:, W:] - I[:-H, W:] - I[H:, :-W] + I[:-H, :-W]
    r, c = np.unravel_index(S.argmax(), S.shape); return int(S.max()), (int(r), int(c))
