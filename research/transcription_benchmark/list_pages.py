"""List the page images of the six documents added in the second round and write small orientation thumbnails.
Run: python research/transcription_benchmark/list_pages.py <thumb_dir>
"""
import glob
import os
import sys

from PIL import Image

Image.MAX_IMAGE_PIXELS = None
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
os.chdir(ROOT)
out = sys.argv[1]
os.makedirs(out, exist_ok=True)
pats = ["targets/hellen1752/decode/IMG_R1953_*.png", "targets/kauderbach1754/img/IMG_R2078_*.png",
        "targets/carpio1677/img/IMG_R1009_*.png", "targets/carpio1677/img/IMG_R1010_*.png",
        "targets/ferdinand3/img/IMG_R1889_*.png", "targets/ferdinand3/img/IMG_R1890_*.png"]
for pat in pats:
    for p in sorted(glob.glob(pat)):
        im = Image.open(p)
        print(p, im.size)
        im = im.convert("RGB")
        im.thumbnail((1100, 1100))
        im.save(os.path.join(out, os.path.basename(p).replace(".png", "_thumb.jpg")), quality=80)
