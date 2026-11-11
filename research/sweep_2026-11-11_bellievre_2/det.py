# Cipher-likeness per canvas from connected components: cipher is written in separate, similar-sized glyphs,
# a cursive hand in long joined strokes.  python3 det.py <file>...  prints best-window score.
import sys, numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage as ndi
def comps(fn, scale=1.0):
    im = Image.open(fn).convert('L')
    if scale != 1.0: im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
    A = np.asarray(im, dtype=np.int16)
    bg = np.asarray(im.filter(ImageFilter.MedianFilter(9)).filter(ImageFilter.BoxBlur(5)), dtype=np.int16)
    D = bg - A; paper = bg > 105
    thr = max(10.0, min(40.0, 0.45 * float(np.percentile(D[paper], 99.5)))) if paper.any() else 40.0
    ink = (D > thr) & paper
    lab, n = ndi.label(ink, structure=np.ones((3, 3)))
    sl = ndi.find_objects(lab)
    out = []
    for s in sl:
        h = s[0].stop - s[0].start; w = s[1].stop - s[1].start
        out.append(((s[0].start + s[0].stop) / 2, (s[1].start + s[1].stop) / 2, h, w))
    return np.array(out).reshape(-1, 4), A.shape
def score(fn, scale=1.0, WX=110, WY=44):
    c, (H, W) = comps(fn, scale)
    if len(c) == 0: return 0, 0, 0, (0, 0)
    y, x, h, w = c.T
    glyph = (h >= 4) & (h <= 13) & (w >= 3) & (w <= 11)
    big = (w > 14) | (h > 16)
    gy, gx = (y // (WY // 2)).astype(int), (x // (WX // 2)).astype(int)
    ny, nx = H // (WY // 2) + 2, W // (WX // 2) + 2
    G = np.zeros((ny, nx)); B = np.zeros((ny, nx))
    np.add.at(G, (gy[glyph], gx[glyph]), 1); np.add.at(B, (gy[big], gx[big]), 1)
    G2 = G[:-1, :-1] + G[1:, :-1] + G[:-1, 1:] + G[1:, 1:]; B2 = B[:-1, :-1] + B[1:, :-1] + B[:-1, 1:] + B[1:, 1:]
    S = G2 - 3.0 * B2
    i = np.unravel_index(np.argmax(S), S.shape)
    return float(S[i]), float(G2[i]), float(B2[i]), (int(i[1] * WX / 2), int(i[0] * WY / 2))
if __name__ == '__main__':
    sc = 1.0
    for f in sys.argv[1:]:
        if f.startswith('x'): sc = float(f[1:]); continue
        print(f.split('/')[-1], score(f, sc))
