"""Verification sheets: page halves (native 500 px from the 1000 px frames of pet.py), 3x2 a sheet. usage: python3 halves.py <dir> <spec> ...   spec = 345R 376L 544B (B = both)"""
import sys
from PIL import Image, ImageDraw
d = sys.argv[1]; items = []
for s in sys.argv[2:]:
    n, side = int(s[:-1]), s[-1]
    for sd in ('LR' if side == 'B' else side): items.append((n, sd))
for k in range(0, len(items), 6):
    ims = []
    for n, sd in items[k:k + 6]:
        im = Image.open('%s/p%d.jpg' % (d, n)).convert('RGB'); w, h = im.size
        c = im.crop((0, 0, w // 2 + 30, h) if sd == 'L' else (w // 2 - 30, 0, w, h))
        ImageDraw.Draw(c).rectangle([0, 0, 62, 14], fill='white'); ImageDraw.Draw(c).text((2, 1), '%d%s' % (n, sd), fill='red'); ims.append(c)
    W = max(i.width for i in ims); H = max(i.height for i in ims); S = Image.new('RGB', (3 * W, ((len(ims) + 2) // 3) * H), 'white')
    for j, im in enumerate(ims): S.paste(im, ((j % 3) * W, (j // 3) * H))
    fn = '%s/H_%d%s.jpg' % (d, items[k][0], items[k][1]); S.save(fn, quality=80); print(fn, [('%d%s' % x) for x in items[k:k + 6]])
