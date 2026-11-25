"""Fetch native-resolution CUDL images by IIIF region tiles and stitch.
Usage: python fetch_images.py <iiif id> <out.jpg>
id e.g. MS-TS-K-00024-00024-000-00001. Output images are not kept in the repository."""
import sys, io, json, urllib.request
from PIL import Image

BASE = "https://images.lib.cam.ac.uk/iiif/%s.jp2"


def get(u):
    req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
    return urllib.request.urlopen(req, timeout=120).read()


def main(i, out, T=1800):
    info = json.loads(get(BASE % i + "/info.json"))
    W, H = info['width'], info['height']
    im = Image.new('RGB', (W, H))
    for y in range(0, H, T):
        for x in range(0, W, T):
            w = min(T, W - x)
            h = min(T, H - y)
            d = get(BASE % i + f"/{x},{y},{w},{h}/full/0/default.jpg")
            im.paste(Image.open(io.BytesIO(d)), (x, y))
    im.save(out, quality=92)
    print(out, W, H)


main(sys.argv[1], sys.argv[2])
