"""Cut each page into overlapping 4-line bands (contrast-enhanced, full text width) for transcription: bands/<fol>_<k>.png"""
import os, glob
from PIL import Image, ImageOps
os.makedirs("bands", exist_ok=True)
for fn in sorted(glob.glob("pages/f*.jpg")):
    fol = os.path.basename(fn)[1:-4]
    im = ImageOps.autocontrast(Image.open(fn).convert("L"), cutoff=1)
    w, h = im.size
    x0, x1 = int(w * 0.06), int(w * 0.99)
    H, step = 720, 620
    k = 0
    for y in range(int(h * 0.02), int(h * 0.97), step):
        im.crop((x0, y, x1, min(h, y + H))).save(f"bands/{fol}_{k:02d}.png"); k += 1
