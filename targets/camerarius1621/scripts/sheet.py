"""Contact sheet: sheet.py OUT.jpg SIZE PAGE..."""
import sys, os
from PIL import Image, ImageDraw
out, size, pages = sys.argv[1], sys.argv[2], [int(x) for x in sys.argv[3:]]
d = os.path.join(os.path.dirname(__file__), '..', 'scans')
ims = [Image.open(os.path.join(d, os.environ.get('PFX','') + f'p{p:03d}_{size}.jpg')).convert('L') for p in pages]
w = max(i.width for i in ims); h = max(i.height for i in ims); cols = min(4, len(ims)); rows = (len(ims)+cols-1)//cols
S = Image.new('L', (w*cols, h*rows), 255); dr = ImageDraw.Draw(S)
for k, (p, i) in enumerate(zip(pages, ims)):
    x, y = (k % cols)*w, (k//cols)*h; S.paste(i, (x, y)); dr.text((x+5, y+5), str(p), fill=0)
S.save(out, quality=85)
