"""python sheet.py <tag> <start> <count> <cols> : contact sheet of frames, each cropped to the telegram area."""
import os, sys, glob
from PIL import Image, ImageDraw
here = os.path.dirname(os.path.abspath(__file__))
tag, start, count, cols = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
step = int(sys.argv[5]) if len(sys.argv) > 5 else 1
files = {int(os.path.basename(f)[:3]): f for f in glob.glob(os.path.join(here, 'img', tag, '*.jpg'))}
ims = []
for i in range(start, start + count * step, step):
    if i not in files: continue
    im = Image.open(files[i]).convert('L'); w, h = im.size
    if w > h * 1.15:  # two-form frame: crop to the forms' body
        im = im.crop((int(w * .08), int(h * .40), int(w * .88), int(h * .68)))
    else:
        im = im.crop((int(w * .03), int(h * .14), int(w * .95), int(h * .90)))
    d = ImageDraw.Draw(im); d.rectangle((0, 0, 150, 16), fill=255); d.text((2, 2), os.path.basename(files[i])[:-4], fill=0)
    ims.append(im)
W = max(i.size[0] for i in ims); H = max(i.size[1] for i in ims); rows = -(-len(ims) // cols)
sh = Image.new('L', (W * cols, H * rows), 255)
for k, im in enumerate(ims): sh.paste(im, ((k % cols) * W, (k // cols) * H))
fn = os.path.join(here, 'img', 'sheet_%s_%03d.jpg' % (tag, start)); sh.save(fn, quality=85); print(fn, sh.size)
