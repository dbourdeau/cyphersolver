# usage: python comp.py <name> <yc> <x0> <x1> [manifest-index] [slope] : line crop as numbered panels, no overlap between panels
import sys, json, os
from cropv import crop
from PIL import Image, ImageDraw
m = json.load(open('man/' + os.environ.get('MANIFEST', 'bf3cf88e-72bf-4608-8e75-a0390e17284b') + '.json', encoding='utf8'))
name, yc, x0, x1 = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
idx = int(sys.argv[5]) if len(sys.argv) > 5 else 0
c = m['sequences'][0]['canvases'][idx]
b, W = c['images'][0]['resource']['@id'], c['width']
slope = float(sys.argv[6]) if len(sys.argv) > 6 else 0  # y change per panel: these lines rise to the right
wd, hh = 125, 25
pieces = []
for k, x in enumerate(range(x0, x1, wd)):
    y = round(yc + slope * k)
    tmp = f'tmp{os.getpid()}'
    crop(b, W, tmp, x, y - hh, x + wd, y + hh + 4, out=900)
    im = Image.open(f'crops/{tmp}.jpg').copy()
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, 30, 16), fill='yellow')
    d.text((3, 3), str(k + 1), fill='black')
    pieces.append(im)
h = max(p.size[1] for p in pieces)
out = Image.new('RGB', (1800, ((len(pieces) + 1) // 2) * (h + 3)), 'red')
for i, im in enumerate(pieces):
    out.paste(im, ((i % 2) * 900, (i // 2) * (h + 3)))
out.save(f'crops/{name}.jpg')
print(name, out.size, len(pieces))
