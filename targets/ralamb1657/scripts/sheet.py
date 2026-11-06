"""Contact sheet: python sheet.py <indir> <out.jpg> <n> [<n>...]  (3 columns, 600 px tiles, numbered)"""
import sys, os
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass
from PIL import Image, ImageDraw
ind, out, ns = sys.argv[1], sys.argv[2], [int(x) for x in sys.argv[3:]]
W = 600; cols = 3
tiles = []
for n in ns:
    im = Image.open(os.path.join(ind, f"{n:03d}.jpg")).convert("RGB")
    im = im.resize((W, int(im.height * W / im.width)))
    d = ImageDraw.Draw(im); d.rectangle((0, 0, 60, 30), fill="white"); d.text((5, 5), str(n), fill="red")
    tiles.append(im)
H = max(t.height for t in tiles); rows = (len(tiles) + cols - 1) // cols
sh = Image.new("RGB", (cols * W, rows * H), "white")
for i, t in enumerate(tiles):
    sh.paste(t, ((i % cols) * W, (i // cols) * H))
sh.save(out, quality=85)
