"""Fetch the full-resolution sides of T-S NS J479 from the Cambridge IIIF server in 1024-px regions and stitch them.
Usage: stitch.py   (writes img/full1.jpg, img/full2.jpg)"""
import urllib.request, io
from PIL import Image
W, H = 3097, 4366
for n in (1, 2):
    base = f'https://images.lib.cam.ac.uk/iiif/MS-TS-NS-J-00479-000-0000{n}.jp2'
    import json
    info = json.load(urllib.request.urlopen(base + '/info.json', timeout=60)); w, h = info['width'], info['height']
    out = Image.new('RGB', (w, h)); T = 1024
    for y in range(0, h, T):
        for x in range(0, w, T):
            cw, ch = min(T, w-x), min(T, h-y)
            u = f'{base}/{x},{y},{cw},{ch}/full/0/default.jpg'
            out.paste(Image.open(io.BytesIO(urllib.request.urlopen(u, timeout=120).read())), (x, y))
    out.save(f'img/full{n}.jpg', quality=92); print(n, w, h)
