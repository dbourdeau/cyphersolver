"""sheet.py out.jpg img1 img2 ... : paste previews side by side, scaled to a common height, max width 2000."""
import sys
from PIL import Image
ims = [Image.open(p).convert("RGB") for p in sys.argv[2:]]
h = 1400
ims = [i.resize((int(i.width*h/i.height), h)) for i in ims]
o = Image.new("RGB", (sum(i.width for i in ims), h), "white"); x = 0
for i in ims: o.paste(i, (x, 0)); x += i.width
o.thumbnail((2000, 2000)); o.save(sys.argv[1], quality=85)
