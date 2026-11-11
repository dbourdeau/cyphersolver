# python3 sheets.py <dir> <start> <end> [cols rows tilew]  -- contact sheets of canvases (two-page openings), labelled cNNNN
import os, sys
from PIL import Image, ImageOps, ImageDraw
d = sys.argv[1]; a = int(sys.argv[2]); b = int(sys.argv[3])
cols, rows, W = (int(x) for x in sys.argv[4:7]) if len(sys.argv) > 6 else (3, 4, 520)
out = d + '_sheets'; os.makedirs(out, exist_ok=True)
ids = [i for i in range(a, b + 1) if os.path.exists(f'{d}/c{i:04d}.jpg')]
per = cols * rows
for k in range(0, len(ids), per):
    grp = ids[k:k + per]; ims = []
    for i in grp:
        im = Image.open(f'{d}/c{i:04d}.jpg').convert('L')
        bb = ImageOps.invert(im.point(lambda v: 255 if v > 60 else 0)).getbbox()  # trim black film border
        im = im.resize((W, int(im.height * W / im.width)), Image.LANCZOS); ims.append(im)
    h = max(im.height for im in ims)
    sh = Image.new('L', (W * cols, h * rows), 255); dr = ImageDraw.Draw(sh)
    for j, im in enumerate(ims):
        x = W * (j % cols); y = h * (j // cols); sh.paste(im, (x, y))
        dr.rectangle([x, y, x + 46, y + 13], fill=255); dr.text((x + 3, y + 1), f'c{grp[j]:04d}', fill=0)
    fn = f'{out}/s{grp[0]:04d}_{grp[-1]:04d}.jpg'; sh.save(fn, quality=78); print(fn)
