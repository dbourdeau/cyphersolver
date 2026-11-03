"""Find text-line centres on a full-size page by a smoothed row ink profile (dark pixels in the text block).
usage: lines.py IMG X0 X1 Y0 Y1   -> prints peak row, ink mass"""
import sys
import numpy as np
from PIL import Image
im = np.asarray(Image.open(sys.argv[1]).convert('L')).astype(float)
x0, x1, y0, y1 = map(int, sys.argv[2:6])
a = im[y0:y1, x0:x1]
bg = np.median(a)
ink = (a < bg - 45).sum(1).astype(float)
k = np.ones(25) / 25
s = np.convolve(ink, k, 'same')
pk = [i for i in range(20, len(s) - 20) if s[i] == s[i - 20:i + 21].max() and s[i] > 8]
for p in pk:
    print(p + y0, int(s[p]))
