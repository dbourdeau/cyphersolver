"""Digit-texture score: cipher numbers are isolated small glyphs, running hands are long connected strokes.
score(image) = max over 200x120 windows of the number of small isolated components (w 3-11, h 5-14 px at 900 px a spread).
python digi.py <man> : scores every local image -> scratch/ps/<man>_digi.json, prints the top 40"""
import sys, os, glob, json
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage as ndi
import rik
def score(im, W=200, H=120):
    if im.size[1] > im.size[0] * 1.6: im = im.crop((0, 0, im.size[0], int(im.size[0] * 1.3)))
    g = im.convert('L'); bg = g.filter(ImageFilter.GaussianBlur(10))
    m = (np.asarray(bg).astype(int) - np.asarray(g).astype(int)) > 30
    lab, n = ndi.label(m)
    if n == 0: return 0, (0, 0)
    sl = ndi.find_objects(lab); pts = np.zeros(m.shape)
    for s in sl:
        h = s[0].stop - s[0].start; w = s[1].stop - s[1].start
        if 5 <= h <= 14 and 3 <= w <= 11: pts[(s[0].start + s[0].stop) // 2, (s[1].start + s[1].stop) // 2] = 1
    I = np.pad(pts.cumsum(0).cumsum(1), ((1, 0), (1, 0))); hh, ww = pts.shape
    if hh <= H or ww <= W: return int(pts.sum()), (0, 0)
    S = I[H:, W:] - I[:-H, W:] - I[H:, :-W] + I[:-H, :-W]
    r, c = np.unravel_index(S.argmax(), S.shape); return int(S.max()), (int(r), int(c))
if __name__ == '__main__':
    man = sys.argv[1]; out = {}
    for f in sorted(glob.glob(f'{rik.SP}/pg/{man}/*.jpg')):
        i = int(os.path.basename(f)[:5]); s, rc = score(Image.open(f)); out[i] = [s, rc[0], rc[1]]
    json.dump(out, open(f'{rik.SP}/ps/{man}_digi.json', 'w'))
    print(sorted(((v[0], k) for k, v in out.items()), reverse=True)[:40])
    vals = sorted(v[0] for v in out.values()); print('median', vals[len(vals) // 2], 'p90', vals[int(len(vals) * .9)])
