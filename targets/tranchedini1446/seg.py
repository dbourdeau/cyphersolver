"""Segment f. 139 (R7908): deskew, 41 text lines (projection peaks), glyph groups per line.
Writes seg/deskew.png, seg/groups.json  ({line: [[x0,y0,x1,y1,ink],...]}), overlays seg/ov_<n>.png
usage: python seg.py [overlay line numbers...]"""
import json, os, sys
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage as ndi
from scipy.signal import find_peaks
os.makedirs('seg', exist_ok=True)
if not os.path.exists('seg/deskew.png'):
    Image.open('img/IMG_R7908_I35658_P.png').convert('L').rotate(-0.8, resample=Image.BICUBIC, fillcolor=255).save('seg/deskew.png')
im = Image.open('seg/deskew.png'); a = np.array(im); b = a < 120
p = ndi.gaussian_filter1d(b[:, 150:1650].sum(1).astype(float), 3)
pk = find_peaks(p[180:1800], distance=28, prominence=15)[0] + 180
print(len(pk), 'lines')
groups = {}
pk = [int(x) for x in pk]
for n, c in enumerate(pk, 1):
    y0, y1 = c - 26, c + 22
    band = b[y0:y1, 100:1700]
    d = ndi.binary_dilation(band, structure=np.ones((3, 5)))
    lab, k = ndi.label(d)
    out = []
    for i, sl in enumerate(ndi.find_objects(lab), 1):
        ys, xs = sl
        ink = int((band[sl] & (lab[sl] == i)).sum())
        if ink < 12: continue
        out.append([int(xs.start + 100), int(ys.start + y0), int(xs.stop + 100), int(ys.stop + y0), ink])
    out.sort()
    groups[n] = out
json.dump({'lines': [int(x) for x in pk], 'groups': groups}, open('seg/groups.json', 'w'))
for n in map(int, sys.argv[1:]):
    c = int(pk[n - 1]); cr = im.convert('RGB').crop((100, c - 30, 1700, c + 26)); dr = ImageDraw.Draw(cr)
    for x0, y0, x1, y1, ink in groups[n]:
        dr.rectangle([x0 - 100, y0 - c + 30, x1 - 100, y1 - c + 30], outline=(255, 0, 0))
    cr.save(f'seg/ov_{n}.png')
