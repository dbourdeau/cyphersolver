import sys
from PIL import Image, ImageOps, ImageEnhance
# strip.py img out_prefix x0 x1 y0 y1 nstrips  -> strips with gamma to bring up faint glosses
im = Image.open(sys.argv[1]).convert("L"); W, H = im.size
x0, x1, y0, y1 = [float(v) for v in sys.argv[3:7]]; n = int(sys.argv[7])
xm = (x0 + x1) / 2
for i in range(n):
    a = y0 + (y1 - y0) * i / n; b = y0 + (y1 - y0) * (i + 1) / n + 0.006
    for half, (u, v) in enumerate([(x0, xm + 0.01), (xm - 0.01, x1)]):
        c = im.crop((int(u * W), int(a * H), int(v * W), int(b * H)))
        c = ImageOps.autocontrast(c, cutoff=2)
        c = c.point(lambda p: int(255 * (p / 255) ** 1.8))
        c = c.resize((1900, int(c.height * 1900 / c.width)), Image.LANCZOS)
        c.save("%s_%d%s.jpg" % (sys.argv[2], i, "ab"[half]), quality=90)
