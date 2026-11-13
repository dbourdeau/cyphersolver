"""Unjoined-glyph strip score: in 220x34 strips (900 px spread) the ink area held by components with w<=11 and h<=15 must be >=65% of the strip's ink
and at least MINK px. score = max of that ink area over qualifying strips (stride 10 px). Returns (score, (row, col))"""
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage as ndi
def score(im, W=220, H=34, MINK=140):
    if im.size[1] > im.size[0] * 1.6: im = im.crop((0, 0, im.size[0], int(im.size[0] * 1.3)))
    g = im.convert('L'); bg = g.filter(ImageFilter.GaussianBlur(10))
    m = (np.asarray(bg).astype(int) - np.asarray(g).astype(int)) > 30
    lab, n = ndi.label(m)
    if n == 0: return 0, (0, 0)
    sl = ndi.find_objects(lab); area = ndi.sum(m, lab, range(1, n + 1))
    small = np.zeros(n + 1, bool)
    for k, s in enumerate(sl):
        h = s[0].stop - s[0].start; w = s[1].stop - s[1].start
        if h <= 15 and w <= 11 and area[k] >= 4: small[k + 1] = True
    sm = small[lab] & m; I1 = np.pad(sm.cumsum(0).cumsum(1), ((1, 0), (1, 0))); I2 = np.pad(m.cumsum(0).cumsum(1), ((1, 0), (1, 0)))
    hh, ww = m.shape
    if hh <= H or ww <= W: return 0, (0, 0)
    f = lambda I: I[H:, W:] - I[:-H, W:] - I[H:, :-W] + I[:-H, :-W]
    A = f(I1)[::5, ::10].astype(float); T = f(I2)[::5, ::10].astype(float)
    ok = (A >= MINK) & (A >= 0.65 * T)
    if not ok.any(): return 0, (0, 0)
    A = np.where(ok, A, 0); r, c = np.unravel_index(A.argmax(), A.shape); return int(A.max()), (int(r * 5 - 40), int(c * 10 - 0))
