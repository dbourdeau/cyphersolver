"""Ink components of the deskewed recto, with ids, for sign-by-sign transcription (second attempt).
Writes img/w/comps.json and img/w/lab.npy. Component id = running number, line = nearest line centre (CY)."""
import cv2, numpy as np, json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
CY = [680, 945, 1170, 1404, 1664, 1881, 2124, 2348, 2616, 2828]
g = cv2.imread('img/w/deskew_gray.png', 0)
bg = cv2.medianBlur(g, 101).astype(np.float32)
ink = ((bg - g.astype(np.float32)) > 40).astype(np.uint8)
X0, X1, Y0, Y1 = 250, 3500, 420, 3050
mask = np.zeros_like(ink)
mask[Y0:Y1, X0:X1] = ink[Y0:Y1, X0:X1]
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
n, lab, st, cen = cv2.connectedComponentsWithStats(mask, 8)
out = []
for i in range(1, n):
    x, y, w, h, a = [int(v) for v in st[i]]
    if a < 150:
        continue
    cx, cy = cen[i]
    ln = int(np.argmin([abs(cy - c) for c in CY])) + 1
    out.append(dict(i=i, x=x, y=y, w=w, h=h, a=a, cx=float(cx), cy=float(cy), line=ln))
for L in range(1,11):
    for k,c in enumerate(sorted([c for c in out if c['line']==L],key=lambda c:c['cx']),1): c['k']=k
json.dump(out, open('img/w/comps.json', 'w'))
np.save('img/w/lab.npy', lab.astype(np.int32))
import collections
print(len(out), sorted(collections.Counter(c['line'] for c in out).items()))
