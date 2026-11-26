# crop.py SRC_DIR OUT_DIR BOXES.tsv : crop cipher blocks (fractions of the source image), optional white masks.
# BOXES.tsv rows: name<TAB>src<TAB>x0 y0 x1 y1<TAB>masks (x0 y0 x1 y1 ; ... fractions of the SOURCE, may be empty)
import sys, os
from PIL import Image, ImageDraw
src, out, boxes = sys.argv[1:4]
for l in open(boxes, encoding="utf-8"):
    if not l.strip() or l.startswith("#"):
        continue
    f = l.rstrip("\n").split("\t") + [""]
    name, s, box, masks = f[0], f[1], f[2], f[3]
    im = Image.open(os.path.join(src, s)).convert("L"); w, h = im.size
    d = ImageDraw.Draw(im)
    for m in [m for m in masks.split(";") if m.strip()]:
        a, b, c, e = (float(x) for x in m.split())
        d.rectangle([a*w, b*h, c*w, e*h], fill=255)
    x0, y0, x1, y1 = (float(x) for x in box.split())
    c = im.crop((int(x0*w), int(y0*h), int(x1*w), int(y1*h)))
    c.save(os.path.join(out, name), quality=92)
    print(name, c.size)
