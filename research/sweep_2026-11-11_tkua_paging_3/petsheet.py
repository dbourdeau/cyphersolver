"""Sheets (3x3, 533 px a frame) from the frames saved by pet.py. usage: python3 petsheet.py <dir> <lo> <hi> [prefix]"""
import sys, os
from PIL import Image, ImageDraw
d, lo, hi = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); pre = sys.argv[4] if len(sys.argv) > 4 else 'p'; w = 533
ns = [n for n in range(lo, hi + 1) if os.path.exists('%s/%s%d.jpg' % (d, pre, n))]
for s in range(0, len(ns), 9):
    ims = []
    for n in ns[s:s + 9]:
        im = Image.open('%s/%s%d.jpg' % (d, pre, n)).convert('RGB'); im = im.resize((w, int(im.height * w / im.width)))
        ImageDraw.Draw(im).rectangle([0, 0, 60, 16], fill='white'); ImageDraw.Draw(im).text((3, 2), 'img %d' % n, fill='red'); ims.append(im)
    h = max(i.height for i in ims); S = Image.new('RGB', (3 * w, ((len(ims) + 2) // 3) * h), 'white')
    for k, im in enumerate(ims): S.paste(im, ((k % 3) * w, (k // 3) * h))
    S.save('%s/S_%04d.jpg' % (d, ns[s]), quality=72)
print(len(ns))
