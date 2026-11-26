"""Zoom tiles for resolving pass disagreements. Usage: python resolve.py <out.png> <scale> <size> L@x [L@x ...]  (e.g. L1@2380)"""
import sys
import numpy as np
import cv2
import win
import contact

out, scale, size = sys.argv[1], float(sys.argv[2]), int(sys.argv[3])
g = win.load()
tiles = []
for a in sys.argv[4:]:
    ln, x = a.split('@')
    tiles.append(contact.tile(g, ln, int(x), a, S=size, scale=scale))
cols = 3
h, w = tiles[0].shape[:2]
rows = (len(tiles) + cols - 1) // cols
img = np.full((rows * h, cols * w, 3), 255, np.uint8)
for i, t in enumerate(tiles):
    r, c = divmod(i, cols)
    img[r * h:(r + 1) * h, c * w:(c + 1) * w] = t
cv2.imwrite(out, img)
print(out, img.shape)
