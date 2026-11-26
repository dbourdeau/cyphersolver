"""Crop a region of an image with background flattening, for reading. Usage: python crop.py <img> <out> x0 y0 x1 y1 [scale]"""
import sys
import numpy as np
import cv2

img, out = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = [int(v) for v in sys.argv[3:7]]
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
g = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
pad = 150
sub = g[max(0, y0 - pad):y1 + pad, max(0, x0 - pad):x1 + pad].astype(np.float32)
bg = cv2.GaussianBlur(sub, (0, 0), 40)
flat = np.clip(128 + (sub - bg) * 2.2, 0, 255).astype(np.uint8)
oy, ox = y0 - max(0, y0 - pad), x0 - max(0, x0 - pad)
c = flat[oy:oy + (y1 - y0), ox:ox + (x1 - x0)]
if scale != 1.0:
    c = cv2.resize(c, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA if scale < 1 else cv2.INTER_CUBIC)
cv2.imwrite(out, c)
print(out, c.shape)
