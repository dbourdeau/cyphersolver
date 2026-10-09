"""Download every image of the listed DECODE records and save 1600-px previews in img/v/."""
import sys, os
from PIL import Image
import decode_fetch as F
Image.MAX_IMAGE_PIXELS = None
for i in sys.argv[1:]:
    im, dc = F.files(F.page(i))
    for n in dc: F.fetch(n, "decode")
    for n in im:
        p = F.fetch(n)
        v = os.path.join(F.HERE, "img", "v", n.replace("IMG_", "").replace(".png", ".jpg"))
        if not os.path.exists(v):
            try:
                x = Image.open(p).convert("RGB"); x.thumbnail((1600, 1600)); x.save(v, quality=80)
            except Exception as e: print("bad", n, e)
    print(i, len(im), flush=True)
