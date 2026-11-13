"""Fetch one Estense IIIF page as stitched region tiles.

usage: python fetch.py <service_id> <W> <H> <out.jpg> [scale]
scale 1 = full resolution, 2 = half (tiles of 2048 px requested at 1024 px).
One request at a time, 1.6 s apart, User-Agent WAINUT-research. Stops on 403/429.
"""
import sys, time, io, urllib.request
from PIL import Image

sid, W, H, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
scale = int(sys.argv[5]) if len(sys.argv) > 5 else 1
T = 1024 * scale
canvas = Image.new("RGB", ((W + scale - 1) // scale, (H + scale - 1) // scale), "white")
for y in range(0, H, T):
    for x in range(0, W, T):
        w, h = min(T, W - x), min(T, H - y)
        url = f"{sid}/{x},{y},{w},{h}/{max(1, w // scale)},/0/default.jpg"
        req = urllib.request.Request(url, headers={"User-Agent": "WAINUT-research"})
        try:
            data = urllib.request.urlopen(req, timeout=60).read()
        except urllib.error.HTTPError as e:
            print("HTTP", e.code, url)
            if e.code in (403, 429):
                sys.exit(2)
            raise
        tile = Image.open(io.BytesIO(data)).convert("RGB")
        canvas.paste(tile, (x // scale, y // scale))
        time.sleep(1.6)
canvas.save(out, quality=92)
print("saved", out, canvas.size)
