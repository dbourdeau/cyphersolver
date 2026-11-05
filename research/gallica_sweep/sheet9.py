# 3x3 contact sheets of fetched canvases (400 px each), for screening by eye.  python sheet9.py <dir> [start] [end]
import os, sys
from glob import glob
from PIL import Image, ImageOps, ImageDraw
d = sys.argv[1]; a = int(sys.argv[2]) if len(sys.argv) > 2 else 1; b = int(sys.argv[3]) if len(sys.argv) > 3 else 9999
W = 420; per = 9; cols = 3
files = [f for f in sorted(glob(f'{d}/c*.jpg')) if a <= int(os.path.basename(f)[1:4]) <= b]
out = f'{d}_sheets'; os.makedirs(out, exist_ok=True)
for i in range(0, len(files), per):
    grp = files[i:i + per]; ids = [os.path.basename(f)[1:4] for f in grp]
    ims = []
    for f in grp:
        im = Image.open(f).convert('L'); im = im.resize((W, int(im.height * W / im.width)), Image.LANCZOS)
        ims.append(ImageOps.autocontrast(im, cutoff=1))
    h = max(im.height for im in ims); rows = (len(ims) + cols - 1) // cols
    sh = Image.new('L', (W * cols, (h + 22) * rows), 255); dr = ImageDraw.Draw(sh)
    for k, im in enumerate(ims):
        x = W * (k % cols); y = (h + 22) * (k // cols); sh.paste(im, (x, y + 22)); dr.text((x + 6, y + 4), 'c' + ids[k], fill=0)
    sh.save(f'{out}/s{ids[0]}_{ids[-1]}.jpg', quality=80)
print(len(files))
