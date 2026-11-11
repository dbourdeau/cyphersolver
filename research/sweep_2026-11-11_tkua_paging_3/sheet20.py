"""20-frame sheets (400 px) from frames saved by pet.py, skipping images already on the 1-in-4 grid. usage: python3 sheet20.py <dir> <lo> <hi> [all]"""
import sys, os
from PIL import Image, ImageDraw
d, lo, hi = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); allf = len(sys.argv) > 4; w = 400
ns = [n for n in range(lo, hi + 1) if os.path.exists('%s/p%d.jpg' % (d, n)) and (allf or n % 4 != 1)]
for s in range(0, len(ns), 20):
    ims = []
    for n in ns[s:s + 20]:
        im = Image.open('%s/p%d.jpg' % (d, n)).convert('RGB'); im = im.resize((w, int(im.height * w / im.width)))
        ImageDraw.Draw(im).rectangle([0, 0, 60, 16], fill='white'); ImageDraw.Draw(im).text((3, 2), 'img %d' % n, fill='red'); ims.append(im)
    h = max(i.height for i in ims); S = Image.new('RGB', (4 * w, ((len(ims) + 3) // 4) * h), 'white')
    for k, im in enumerate(ims): S.paste(im, ((k % 4) * w, (k // 4) * h))
    S.save('%s/T_%04d.jpg' % (d, ns[s]), quality=72)
print(len(ns))
