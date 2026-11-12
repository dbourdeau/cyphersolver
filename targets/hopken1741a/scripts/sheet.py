"""Contact sheet: python sheet.py out.jpg cols width img1 img2 ... (labels each tile)"""
import sys
from PIL import Image, ImageDraw
out, cols, w = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); files = sys.argv[4:]
ims = []
for f in files:
    im = Image.open(f).convert("RGB"); im = im.resize((w, int(im.height * w / im.width))); ims.append((f, im))
h = max(i.height for _, i in ims); rows = (len(ims) + cols - 1) // cols
S = Image.new("RGB", (cols * w, rows * h), "white"); d = ImageDraw.Draw(S)
for k, (f, im) in enumerate(ims):
    x, y = (k % cols) * w, (k // cols) * h; S.paste(im, (x, y)); d.text((x + 5, y + 5), f.split("/")[-1].split("\\")[-1][:18], fill="red")
S.save(out, quality=85)
