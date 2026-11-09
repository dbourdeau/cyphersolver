# python sheets.py <dir> <outdir> [cols rows tileW]
import os, sys
from glob import glob
from PIL import Image, ImageOps, ImageDraw
d, out = sys.argv[1], sys.argv[2]
cols = int(sys.argv[3]) if len(sys.argv) > 3 else 4
rows = int(sys.argv[4]) if len(sys.argv) > 4 else 2
W = int(sys.argv[5]) if len(sys.argv) > 5 else 300
os.makedirs(out, exist_ok=True)
files = sorted(glob(f'{d}/c*.jpg')); per = cols * rows
for i in range(0, len(files) - per + 1 if len(files) % per == 0 else len(files), per):
    grp = files[i:i + per]; ids = [os.path.basename(f)[1:4] for f in grp]
    fn = f'{out}/s{ids[0]}_{ids[-1]}.png'
    if os.path.exists(fn): continue
    ims = []
    for f in grp:
        try: im = Image.open(f).convert('L')
        except Exception: im = Image.new('L', (W, W), 128)
        im = im.resize((W, int(im.height * W / im.width))); ims.append(ImageOps.autocontrast(im, cutoff=1))
    H = max(im.height for im in ims)
    sh = Image.new('L', (W * cols, (H + 14) * rows), 255); dr = ImageDraw.Draw(sh)
    for k, im in enumerate(ims):
        x = W * (k % cols); y = (H + 14) * (k // cols)
        sh.paste(im, (x, y + 14)); dr.text((x + 4, y + 1), 'c' + ids[k], fill=0)
    sh.save(fn)
