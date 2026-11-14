#!/usr/bin/env python3
"""Fetch whole pages of a Lodovico Media Library item by IIIF tiles, one request a second. Needs Pillow.

    python fullpage.py <uuid> <outdir> <canvas> [canvas ...]

Source regions over about 1 megapixel return 422, so a page is fetched in tiles. Images are not part of this folder.
"""
import io, json, os, sys, time, urllib.request
from PIL import Image

UA = {'User-Agent': 'WAINUT-research'}
BASE = 'https://edl-jarvis.cultura.gov.it/meta/iiif/{}/manifest'


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()


uuid, outdir = sys.argv[1:3]
os.makedirs(outdir, exist_ok=True)
manifest = json.loads(get(BASE.format(uuid)))
for ci in map(int, sys.argv[3:]):
    c = manifest['sequences'][0]['canvases'][ci - 1]
    service = c['images'][0]['resource']['service']['@id']
    W, H = c['width'], c['height']
    im = Image.new('RGB', (W, H), 'white')
    for y in range(0, H, 700):
        for x in range(0, W, 1400):
            w, h = min(1400, W - x), min(700, H - y)
            b = get(f'{service}/{x},{y},{w},{h}/full/0/default.jpg')
            im.paste(Image.open(io.BytesIO(b)).convert('RGB'), (x, y))
            time.sleep(1)
    out = os.path.join(outdir, f'{uuid}_{ci}.png')
    im.save(out)
    print(out, W, H, flush=True)
