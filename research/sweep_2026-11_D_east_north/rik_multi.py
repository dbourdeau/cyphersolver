"""python rik_multi.py out.jpg R0003590:333 R0003628:463 ... [samples=10]: one labelled row-block per volume (5 columns)."""
import io, os, sys, time
import requests
from PIL import Image, ImageDraw
H = {'User-Agent': 'curl/8.0'}
SP = r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\cb9d89e0-a934-4680-b628-8b01f0691a53\scratchpad\rik'
out_name = sys.argv[1]
vols = [a.split(':') for a in sys.argv[2:] if ':' in a]
samples = 10
tw = 300
blocks = []
for man, n in vols:
    n = int(n)
    step = (n - 4) / samples
    idx = [int(8 + i * step) for i in range(samples)]
    tiles = []
    for i in idx:
        r = requests.get(f'https://lbiiif.riksarkivet.se/arkis!{man}_{i:05d}/full/{tw},/0/default.jpg', headers=H, timeout=60)
        im = Image.open(io.BytesIO(r.content)).convert('L')
        if im.size[1] > 420:
            im = im.resize((int(im.size[0] * 420 / im.size[1]), 420))
        d = ImageDraw.Draw(im); d.rectangle([0, 0, 52, 16], fill=255); d.text((2, 2), f'{man[-4:]}:{i}', fill=0)
        tiles.append(im)
        time.sleep(0.7)
    rows = 2
    cols = 5
    th = 420
    blk = Image.new('L', (cols * tw, rows * th), 200)
    for k, t in enumerate(tiles):
        blk.paste(t, ((k % cols) * tw, (k // cols) * th))
    blocks.append(blk)
W = max(b.size[0] for b in blocks)
H2 = sum(b.size[1] for b in blocks)
sheet = Image.new('L', (W, H2), 150)
y = 0
for b in blocks:
    sheet.paste(b, (0, y)); y += b.size[1]
p = os.path.join(SP, out_name)
sheet.save(p, quality=70)
print(p, sheet.size)
