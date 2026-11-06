"""Find text-line centres on a leaf by horizontal ink projection and cut one strip per line pair."""
import sys
from PIL import Image
import numpy as np
leaf, y0, y1 = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
im = Image.open(f'img/{leaf}.jpg').convert('L')
a = np.asarray(im, dtype=float)
W = a.shape[1]
band = a[:, int(W*0.1):int(W*0.9)]
ink = (band < 110).sum(axis=1).astype(float)
k = 25
sm = np.convolve(ink, np.ones(k)/k, mode='same')
peaks = [y for y in range(y0+40, y1-40) if sm[y] == sm[y-40:y+41].max() and sm[y] > sm[y0:y1].max()*0.25]
out = []
for y in peaks:
    if not out or y - out[-1] > 60: out.append(y)
print(' '.join(map(str, out)))
