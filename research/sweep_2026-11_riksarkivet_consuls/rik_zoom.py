"""python rik_zoom.py <man> <image> <width> <x0,y0,x1,y1 as fractions> [name] -> crop of one image at full width `width`.
Used to check for faint interlinear decipherments that do not show at screen size."""
import os
import sys

from rik_common import SP, img

man, i, w = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
x0, y0, x1, y1 = [float(v) for v in sys.argv[4].split(',')]
name = sys.argv[5] if len(sys.argv) > 5 else f'{man}_{i}_z{w}_{sys.argv[4].replace(",", "_")}.jpg'
im = img(man, i, w)
W, H = im.size
c = im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H)))
p = os.path.join(SP, name)
c.save(p, quality=85)
print(p, c.size)
