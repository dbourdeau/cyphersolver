"""Half-width native-resolution crops, 3-4 lines each, for close transcription: half/<fol>_<k><L|R>.png"""
import os, sys
from PIL import Image, ImageOps
os.makedirs("half", exist_ok=True)
fol = sys.argv[1]
im = ImageOps.autocontrast(Image.open(f"pages/f{fol}.jpg").convert("L"), cutoff=1)
w, h = im.size
y = int(sys.argv[2]) if len(sys.argv) > 2 else 150
k = 0
while y < h - 200:
    im.crop((int(w * 0.06), y, int(w * 0.54), y + 560)).save(f"half/{fol}_{k:02d}L.png")
    im.crop((int(w * 0.50), y, int(w * 0.99), y + 560)).save(f"half/{fol}_{k:02d}R.png")
    y += 500; k += 1
print(k)
