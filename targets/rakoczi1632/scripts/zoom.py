"""zoom.py SRC.jpg OUT.jpg "y,x0,x1" ... : crops of height 0.034 page around centre y (fractions), x0-x1, at 3x,
autocontrast, stacked top to bottom with a label. For settling single signs."""
import sys
from PIL import Image, ImageOps, ImageDraw
im = Image.open(sys.argv[1]).convert('L'); W, H = im.size; parts = []
for spec in sys.argv[3:]:
    y, x0, x1 = map(float, spec.split(','))
    c = im.crop((int(x0 * W), int((y - 0.019) * H), int(x1 * W), int((y + 0.015) * H)))
    c = ImageOps.autocontrast(c, cutoff=1); c = c.resize((int(c.width * 3), int(c.height * 3)), Image.LANCZOS); parts.append((spec, c))
w = max(c.width for _, c in parts); S = Image.new('L', (w, sum(c.height + 22 for _, c in parts)), 255); d = ImageDraw.Draw(S); y = 0
for spec, c in parts:
    d.text((4, y + 4), spec, fill=0); S.paste(c, (0, y + 22)); y += c.height + 22
S.save(sys.argv[2], quality=92)
