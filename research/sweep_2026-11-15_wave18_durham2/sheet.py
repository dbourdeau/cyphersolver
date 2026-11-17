"""python sheet.py <tag> <first> <last> [cols] [cellw] : contact sheet of whole frames (img/sheets/<tag>_<first>.jpg)."""
import os, sys, glob
from PIL import Image, ImageDraw
here = os.path.dirname(os.path.abspath(__file__))
tag, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
cols = int(sys.argv[4]) if len(sys.argv) > 4 else 2; cw = int(sys.argv[5]) if len(sys.argv) > 5 else 900
files = {int(os.path.basename(f)[:3]): f for f in glob.glob(os.path.join(here, 'img', tag, '*.jpg'))}
ims = []
for i in range(a, b + 1):
    if i not in files: continue
    im = Image.open(files[i]).convert("L"); w, h = im.size; im = im.crop((int(w*.07), int(h*.1), int(w*.93), int(h*.95))); w, h = im.size; im = im.resize((cw, int(h * cw / w)), Image.LANCZOS)
    d = ImageDraw.Draw(im); d.rectangle((0, 0, 170, 18), fill=255); d.text((3, 3), os.path.basename(files[i])[:-4], fill=0)
    ims.append(im)
H = max(i.size[1] for i in ims); rows = -(-len(ims) // cols)
sh = Image.new('L', (cw * cols + 6 * cols, (H + 6) * rows), 0)
for k, im in enumerate(ims): sh.paste(im, ((k % cols) * (cw + 6), (k // cols) * (H + 6)))
os.makedirs(os.path.join(here, 'img', 'sheets'), exist_ok=True)
fn = os.path.join(here, 'img', 'sheets', '%s_%03d.jpg' % (tag, a)); sh.save(fn, quality=82); print(fn, sh.size)
