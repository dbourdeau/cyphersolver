import sys
from PIL import Image, ImageOps
src, tag = sys.argv[1], sys.argv[2]; cents = list(map(int, sys.argv[3].split(',')))
im = Image.open(src).convert('L'); w, h = im.size
for n, cy in enumerate(cents):
    for side, (a0, a1) in (('a', (40, w//2+30)), ('b', (w//2-30, w-10))):
        c = ImageOps.autocontrast(im.crop((a0, cy-20, a1, cy+18)), cutoff=1)
        c.resize((c.width*4, c.height*4), Image.LANCZOS).save(f'lines/{tag}{n+1:02d}{side}.png')
