#!/usr/bin/env python3
"""Re-cut the seven reference crops of the chancery key sheet from the archive's own image.

Usage:
    python make_crops.py SOURCE_JPG OUT_DIR            # image already downloaded
    python make_crops.py --fetch OUT_DIR               # download the image from the archive first

SOURCE_JPG is Rigsarkivet, Arkivalieronline unit 260610, image 150 (api image id 48691625):
https://api.rigsarkivet.dk/ao/v1/images/48691625 (plain GET, no sign-in).

Boxes, sizes and expected hashes are in crops.tsv beside this script. The crops are not filed in the
repository: the archive's image is the source, and this script and crops.tsv record exactly how each crop
was cut. Requires Pillow.

Recipe per row of crops.tsv:
  - box: one or more source boxes "x0,y0,x1,y1" in pixels of the source image (x1, y1 exclusive), joined by ';'.
    Several boxes are stacked top to bottom into one strip (the three table-3 crops put the column's letter
    heading above its table-3 cell).
  - the strip is resized to out_w x out_h with the named resampler (factor 3 for the table and index crops,
    factor 1 for the rule line), converted to RGB, saved as PNG.
  - pixel_sha256 is the sha256 of the decoded RGB pixels (mode, size and raw bytes), so it does not depend on the
    PNG encoder. It does depend on the JPEG decoder: it was measured with Pillow 12.3.0; another libjpeg can
    differ by a level here and there, so a mismatch is reported, not treated as an error.
"""
import hashlib
import os
import sys
import urllib.request

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
URL = "https://api.rigsarkivet.dk/ao/v1/images/48691625"
SOURCE_SHA256 = "1453a074be078cdeb30e4502f2522b88e8a9d45d257dba6ad9a1b118eb442097"  # local integrity check only
RESAMPLE = {"LANCZOS": Image.LANCZOS, "BICUBIC": Image.BICUBIC, "BILINEAR": Image.BILINEAR, "NEAREST": Image.NEAREST}


def pixel_sha256(im):
    im = im.convert("RGB")
    h = hashlib.sha256()
    h.update(f"{im.mode} {im.size[0]}x{im.size[1]}\n".encode())
    h.update(im.tobytes())
    return h.hexdigest()


def rows(path):
    with open(path, encoding="utf-8") as f:
        head = None
        for line in f:
            if not line.strip() or line.startswith("#"):
                continue
            cells = line.rstrip("\n").split("\t")
            if head is None:
                head = cells
                continue
            yield dict(zip(head, cells))


def main(argv):
    if len(argv) != 3:
        sys.exit(__doc__)
    src, out = argv[1], argv[2]
    os.makedirs(out, exist_ok=True)
    if src == "--fetch":
        src = os.path.join(out, "260610_150_48691625.jpg")
        req = urllib.request.Request(URL, headers={"User-Agent": "cyphersolver-make-crops"})
        with urllib.request.urlopen(req, timeout=120) as r, open(src, "wb") as f:
            f.write(r.read())
    with open(src, "rb") as f:
        got = hashlib.sha256(f.read()).hexdigest()
    print(f"source sha256 {got} ({'matches' if got == SOURCE_SHA256 else 'DIFFERS from'} the 24 Nov 2026 fetch)")
    img = Image.open(src).convert("RGB")
    ok = 0
    n = 0
    for r in rows(os.path.join(HERE, "crops.tsv")):
        n += 1
        boxes = [tuple(int(v) for v in b.split(",")) for b in r["box"].split(";")]
        parts = [img.crop(b) for b in boxes]
        w = parts[0].size[0]
        strip = Image.new("RGB", (w, sum(p.size[1] for p in parts)))
        y = 0
        for p in parts:
            strip.paste(p, (0, y))
            y += p.size[1]
        size = (int(r["out_w"]), int(r["out_h"]))
        crop = strip if strip.size == size else strip.resize(size, RESAMPLE[r["resample"]])
        crop.save(os.path.join(out, r["file"]))
        ph = pixel_sha256(crop)
        match = ph == r["pixel_sha256"]
        ok += match
        print(f"{r['file']}\t{crop.size[0]}x{crop.size[1]}\tpixels {'match' if match else 'differ'}")
    print(f"{ok}/{n} crops pixel-identical to the crops first filed in PR #974")


if __name__ == "__main__":
    main(sys.argv)
