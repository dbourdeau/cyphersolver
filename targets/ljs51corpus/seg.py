"""Pilot segmenter for LJS 51 master TIFFs: text-line bands and glyph components, right to left.
usage: python seg.py <image number> [out dir]
"""
import sys, json, numpy as np, cv2
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
def load(n):
    im = Image.open(f'output/ljs51/master/0084_{n:04d}.tif').convert('L')
    return np.array(im)
def binarize(g):
    # ink = dark; local threshold copes with the page's uneven tone
    b = cv2.adaptiveThreshold(g, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 51, 18)
    b = cv2.morphologyEx(b, cv2.MORPH_OPEN, np.ones((2, 2), np.uint8))
    return b
def text_bounds(b):
    cols = b.sum(0); rows = b.sum(1)
    xs = np.where(cols > cols.max() * 0.03)[0]; ys = np.where(rows > rows.max() * 0.03)[0]
    return xs.min(), xs.max(), ys.min(), ys.max()
def bands(b, x0, x1):
    prof = b[:, x0:x1].sum(1).astype(float)
    prof = np.convolve(prof, np.ones(9) / 9, 'same')
    thr = prof.max() * 0.06
    on = prof > thr
    out = []; s = None
    for y, v in enumerate(on):
        if v and s is None: s = y
        if not v and s is not None:
            if y - s > 25: out.append((s, y))
            s = None
    return out
if __name__ == '__main__':
    n = int(sys.argv[1]); g = load(n); b = binarize(g)
    # restrict to the text block: ignore the left spine and the right gutter
    h, w = b.shape
    x0, x1, y0, y1 = 420, 1950, 200, 2800
    sub = np.zeros_like(b); sub[y0:y1, x0:x1] = b[y0:y1, x0:x1]
    bs = bands(sub, x0, x1)
    print(n, g.shape, 'bands', len(bs), bs)
