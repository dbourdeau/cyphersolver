"""Fetch one Estense IIIF image as tiles (source regions <= 1500x640) and stitch.

Usage: python -I fetch_tiles.py <service_url> <width> <height> <out.jpg> [scale_pct]
One request at a time, 1 s apart, User-Agent WAINUT-research. Stops on any HTTP error.
Images are CC BY-NC-SA; keep them in scans/ (git-ignored).
"""
import io
import sys
import time
import urllib.request

from PIL import Image

TW, TH = 1500, 640


def main():
    svc, W, H, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    pct = int(sys.argv[5]) if len(sys.argv) > 5 else 100
    s = pct / 100.0
    canvas = Image.new("RGB", (int(W * s) + 2, int(H * s) + 2), "white")
    for y in range(0, H, TH):
        for x in range(0, W, TW):
            w, h = min(TW, W - x), min(TH, H - y)
            size = "full" if pct == 100 else f"pct:{pct}"
            url = f"{svc}/{x},{y},{w},{h}/{size}/0/default.jpg"
            req = urllib.request.Request(url, headers={"User-Agent": "WAINUT-research"})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            tile = Image.open(io.BytesIO(data)).convert("RGB")
            canvas.paste(tile, (int(x * s), int(y * s)))
            time.sleep(1)
    canvas = canvas.crop((0, 0, int(W * s), int(H * s)))
    canvas.save(out, quality=92)
    print(out, canvas.size)


if __name__ == "__main__":
    main()
