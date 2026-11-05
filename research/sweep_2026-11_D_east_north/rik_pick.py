"""python rik_pick.py R0000481 name 36,38,41 [tw=620] -> sheet of selected images (2 columns)"""
import requests, io, sys, os
from PIL import Image, ImageDraw
H = {'User-Agent': 'curl/8.0'}
SP = r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\cb9d89e0-a934-4680-b628-8b01f0691a53\scratchpad\rik'
man, name, idxs = sys.argv[1], sys.argv[2], [int(x) for x in sys.argv[3].split(',')]
tw = int(sys.argv[4]) if len(sys.argv) > 4 else 620
cols = 2
tiles = []
for i in idxs:
    r = requests.get(f'https://lbiiif.riksarkivet.se/arkis!{man}_{i:05d}/full/{tw},/0/default.jpg', headers=H, timeout=90)
    im = Image.open(io.BytesIO(r.content)).convert('L')
    d = ImageDraw.Draw(im); d.rectangle([0, 0, 40, 16], fill=255); d.text((2, 2), str(i), fill=0)
    tiles.append(im)
th = max(t.size[1] for t in tiles); rows = (len(tiles) + cols - 1) // cols
out = Image.new('L', (cols * tw, rows * th), 200)
for k, t in enumerate(tiles):
    out.paste(t, ((k % cols) * tw, (k // cols) * th))
p = os.path.join(SP, name)
out.save(p, quality=72)
print(p, out.size)
