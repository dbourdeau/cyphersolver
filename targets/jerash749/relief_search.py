"""Rank the candidate lines against other lines using independently defined crops.

Run beside jerash-depth.png. Coordinates on the 520 by 1170 preview.
Rows are search bands, not rectifications; bent lines can enter adjacent bands.
"""
from pathlib import Path
import cv2
import numpy as np

src = cv2.imread(str(Path(__file__).with_name("jerash-depth.png")), 0)
gray = cv2.resize(src, (520, 1170), interpolation=cv2.INTER_AREA)
bands = [(14,120),(106,188),(170,253),(236,327),(297,409),(390,471),
         (452,550),(515,613),(579,668),(640,725),(698,789),(775,859),
         (840,944),(917,1018),(987,1088),(1043,1129),(1095,1169)]
known = {7, 8, 9, 10, 11, 17}


def relief(mode):
    a = gray.astype(np.float32)
    if mode == "highpass":
        return a - cv2.GaussianBlur(a, (0, 0), 5)
    if mode == "edge":
        return cv2.magnitude(cv2.Sobel(a,-1,1,0), cv2.Sobel(a,-1,0,1))
    return a


def rank(name, box, home, mode="highpass", scales=(1,), flip=None):
    a = relief(mode)
    x, y, w, h = box
    patch = a[y:y+h, x:x+w]
    if flip is not None:
        patch = cv2.flip(patch, flip)
    scores = []
    for line, (top, bottom) in enumerate(bands, 1):
        if line == home:
            continue
        strip = a[top:bottom]
        best = -2
        for scale in scales:
            probe = cv2.resize(patch, None, fx=scale, fy=scale)
            if probe.shape[0] > strip.shape[0]:
                continue
            matches = cv2.matchTemplate(strip, probe, cv2.TM_CCOEFF_NORMED)
            ph, pw = probe.shape
            # The reconstruction has a black exterior. Exclude all windows
            # crossing it before taking a maximum, including flat background.
            count = cv2.integral((gray[top:bottom] > 4).astype("uint8"))
            coverage = count[ph:,pw:] - count[:-ph,pw:] - count[ph:,:-pw] + count[:-ph,:-pw]
            valid = coverage >= .98 * ph * pw
            if not valid.any():
                continue
            score = matches[valid].max()
            best = max(best, score)
        scores.append((round(float(best),3), line))
    scores.sort(reverse=True)
    top6 = [line for _, line in scores[:6]]
    print(name, scores[:6], "published targets in top six",
          len(known.intersection(top6)) if home == 6 else "-")


group = (367, 411, 67, 39)
for method in ("gray", "highpass", "edge"):
    rank(method, group, 6, method)
rank("scale", group, 6, scales=(.75,1,1.25))
rank("mirror control", group, 6, flip=1)
rank("turn control", group, 6, flip=-1)
rank("left component", (367,416,35,35), 6)
rank("right component", (400,411,32,38), 6)
rank("longer context", (326,407,109,45), 6)
rank("adjacent N control", (445,405,44,46), 6)
rank("line 10 opening", (393,650,83,52), 10)
rank("line 11 opening", (366,716,83,58), 11)
rank("line 17 terminal area", (270,1113,58,45), 17)
rank("line 1 emblem area", (38,44,103,61), 1)
rank("line 16 central area", (209,1062,70,44), 16)
