"""Contact sheets of HStAD D 4 185/3 images: 6 per sheet (3x2), 520 px wide each, labelled. Usage: sheets.py start end"""
import sys, os
from PIL import Image, ImageDraw
a, b = int(sys.argv[1]), int(sys.argv[2])
W = 520
for s in range(a, b + 1, 6):
    ims = []
    for n in range(s, min(s + 6, b + 1)):
        p = f'img/d4/{n:03d}.jpg'
        if os.path.exists(p) and os.path.getsize(p) > 1000:
            im = Image.open(p).convert('L'); im = im.resize((W, int(im.height * W / im.width)))
            ImageDraw.Draw(im).text((5, 5), str(n), fill=0); ims.append(im)
    if not ims: continue
    h = max(i.height for i in ims)
    sh = Image.new('L', (W * 3, h * 2), 255)
    for k, im in enumerate(ims): sh.paste(im, ((k % 3) * W, (k // 3) * h))
    sh.save(f'img/d4s/s{s:03d}.jpg', quality=80)
