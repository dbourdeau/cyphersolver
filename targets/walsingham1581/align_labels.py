"""Experimental projection-based glyph alignment; outputs visual audit sheets."""

from pathlib import Path
import sys

import cv2
import numpy as np
from PIL import Image, ImageDraw


def align(projection, start, end, count, step=5):
    xs = np.arange(start, end + step, step)
    ink = np.interp(xs, np.arange(len(projection)), projection)
    mean = (end - start) / count
    n = len(xs)
    previous = np.full(n, np.inf)
    previous[0] = 0
    back = []
    width_lo = int(max(35, mean * 0.48) / step)
    width_hi = int(min(180, mean * 1.65) / step)
    for k in range(1, count + 1):
        current = np.full(n, np.inf)
        parent = np.full(n, -1, dtype=np.int32)
        lo = max(1, int((k * mean - 130) / step))
        hi = min(n - 1, int((k * mean + 130) / step))
        if k == count:
            lo = hi = n - 1
        for j in range(lo, hi + 1):
            a = max(0, j - width_hi)
            b = max(0, j - width_lo) + 1
            if b <= a:
                continue
            candidates = np.arange(a, b)
            widths = (j - candidates) * step
            cost = previous[a:b] + 2.0 * ((widths - mean) / 22) ** 2
            h = np.argmin(cost)
            if np.isfinite(cost[h]):
                current[j] = cost[h] + 0.16 * ink[j]
                parent[j] = candidates[h]
        previous = current
        back.append(parent)
    j = n - 1
    bounds = [end]
    for parent in reversed(back):
        j = int(parent[j])
        bounds.append(int(xs[j]))
    return bounds[::-1]


base = Path(__file__).parent
scan = cv2.imread(str(base / "cipher_f138.png"), cv2.IMREAD_GRAYSCALE)
residual = cv2.GaussianBlur(scan.astype(np.float32), (0, 0), 35) - scan
rows = [
    (542, 455, 5045),
    (681, 455, 5160),
    (833, 455, 5180),
    (990, 455, 5180),
    (1144, 455, 5180),
    (1293, 455, 5180),
    (1457, 455, 5180),
    (1639, 455, 5180),
    (1821, 455, 5180),
    (2006, 455, 5180),
    (2193, 455, 5180),
    (2368, 455, 5180),
    (2527, 455, 5180),
    (2692, 455, 3400),
]
with (base / "SP53_11_50b.txt").open(encoding="utf-8") as f:
    labels = [line.strip().strip(";").split(";") for line in f if line.strip() and not line.startswith("#")]

row_number = int(sys.argv[1]) if len(sys.argv) > 1 else 0
y, start, end = rows[row_number]
row_labels = labels[row_number]
projection = (residual[y - 52 : y + 52] > 18).sum(axis=0).astype(float)
projection = cv2.GaussianBlur(projection.reshape(1, -1), (1, 1), 0).ravel()
bounds = align(projection, start, end, len(row_labels))
sheet = Image.new("RGB", (1200, ((len(row_labels) + 9) // 10) * 160), "white")
draw = ImageDraw.Draw(sheet)
for i, label in enumerate(row_labels):
    left, right = bounds[i], bounds[i + 1]
    crop = Image.fromarray(scan[y - 60 : y + 65, left:right])
    crop.thumbnail((112, 120))
    x = (i % 10) * 120
    yy = (i // 10) * 160
    sheet.paste(crop, (x + (112 - crop.width) // 2, yy + 30))
    draw.text((x + 5, yy + 3), f"{i+1}:{label}", fill="black")
    draw.text((x + 5, yy + 17), f"{left}-{right}", fill="black")
out = base / f"aligned_row_{row_number+1:02d}.png"
sheet.save(out)
print(out)
print(bounds)
