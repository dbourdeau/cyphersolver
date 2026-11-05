"""Contact sheets for Riksarkivet IIIF volumes: python rik_sheet.py R0003582 568 [samples=20] [start=1] [end=n]
Writes <scratchpad>/rik/<R>_<start>_<end>.jpg (4 columns, tile width 320, label = image number). Polite: 0.8 s between requests."""
import io
import os
import sys
import time

import requests
from PIL import Image, ImageDraw

H = {'User-Agent': 'curl/8.0'}
SP = r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\cb9d89e0-a934-4680-b628-8b01f0691a53\scratchpad\rik'
os.makedirs(SP, exist_ok=True)


def sheet(man, n, samples=20, start=1, end=None, cols=4, tw=320):
    end = end or n
    step = max(1, (end - start) / samples)
    idx = sorted({int(round(start + i * step)) for i in range(samples) if start + i * step <= end})
    tiles = []
    for i in idx:
        u = f'https://lbiiif.riksarkivet.se/arkis!{man}_{i:05d}/full/{tw},/0/default.jpg'
        for a in range(3):
            try:
                r = requests.get(u, headers=H, timeout=60)
                if r.status_code == 200:
                    im = Image.open(io.BytesIO(r.content)).convert('L')
                    break
            except Exception:
                time.sleep(2)
        else:
            im = Image.new('L', (tw, 250), 255)
        d = ImageDraw.Draw(im)
        d.rectangle([0, 0, 38, 16], fill=255)
        d.text((2, 2), str(i), fill=0)
        tiles.append(im)
        time.sleep(0.8)
    th = max(t.size[1] for t in tiles)
    rows = (len(tiles) + cols - 1) // cols
    out = Image.new('L', (cols * tw, rows * th), 200)
    for k, t in enumerate(tiles):
        out.paste(t, ((k % cols) * tw, (k // cols) * th))
    p = os.path.join(SP, f'{man}_{start}_{end}.jpg')
    out.save(p, quality=70)
    print(p, out.size, idx[:3], '...', idx[-1])


if __name__ == '__main__':
    man, n = sys.argv[1], int(sys.argv[2])
    samples = int(sys.argv[3]) if len(sys.argv) > 3 else 20
    start = int(sys.argv[4]) if len(sys.argv) > 4 else 1
    end = int(sys.argv[5]) if len(sys.argv) > 5 else n
    sheet(man, n, samples, start, end)
