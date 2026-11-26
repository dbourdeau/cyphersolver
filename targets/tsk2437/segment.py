"""Ink components of a leaf image: background-normalised threshold, connected components, sheet of numbered crops.
Usage: python segment.py <image> <outprefix> [thr] [minarea] [maxx] [region x0,y0,x1,y1]
Writes <outprefix>_comps.json (bbox, area per component) and contact sheets <outprefix>_sheet_N.png."""
import sys, json
import numpy as np
import cv2
from PIL import Image, ImageDraw

img, pre = sys.argv[1], sys.argv[2]
thr = float(sys.argv[3]) if len(sys.argv) > 3 else 38
minarea = int(sys.argv[4]) if len(sys.argv) > 4 else 150
region = [int(v) for v in sys.argv[5].split(',')] if len(sys.argv) > 5 else None
g = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
if region:
    x0, y0, x1, y1 = region
else:
    x0, y0, x1, y1 = 0, 0, g.shape[1], g.shape[0]
sub = g[y0:y1, x0:x1].astype(np.float32)
bg = cv2.medianBlur(sub.astype(np.uint8), 101).astype(np.float32)
diff = bg - sub
ink = (diff > thr).astype(np.uint8)
ink = cv2.morphologyEx(ink, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
n, lab, st, cen = cv2.connectedComponentsWithStats(ink, 8)
comps = []
for i in range(1, n):
    x, y, w, h, a = st[i]
    if a >= minarea:
        comps.append(dict(id=len(comps), x=int(x + x0), y=int(y + y0), w=int(w), h=int(h), area=int(a)))
json.dump(comps, open(pre + '_comps.json', 'w'))
print(len(comps), 'components')
cv2.imwrite(pre + '_ink.png', (255 - ink * 255).astype(np.uint8))
