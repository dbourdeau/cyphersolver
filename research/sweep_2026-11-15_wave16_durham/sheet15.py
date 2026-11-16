"""python sheet15.py <tag> <first> <count> : 2 x 3 sheet of wave 15's 1,024-px two-form frames, forms only."""
import os, sys, glob
from PIL import Image, ImageDraw
here = os.path.dirname(os.path.abspath(__file__)); tag, a, n = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
ims = []
for i in range(a, a + n):
    g = glob.glob(os.path.join(here, '..', 'sweep_2026-11-15_wave15_arabic2', 'img', tag, '%03d_*.jpg' % i))
    if not g: continue
    im = Image.open(g[0]).convert('L'); w, h = im.size
    im = im.crop((int(w * .03), int(h * .10), int(w * .98), int(h * .84))); im = im.resize((780, int(im.size[1] * 780 / im.size[0])))
    ImageDraw.Draw(im).text((4, 2), os.path.basename(g[0])[:-4], fill=0); ims.append(im)
H = max(i.size[1] for i in ims); rows = -(-len(ims) // 2)
sh = Image.new('L', (1560, H * rows), 255)
for k, im in enumerate(ims): sh.paste(im, ((k % 2) * 780, (k // 2) * H))
fn = os.path.join(here, 'img', 'v', 'w15_%s_%03d.jpg' % (tag, a)); sh.save(fn, quality=80); print(fn, sh.size)
