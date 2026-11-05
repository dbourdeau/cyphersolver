# Contact sheets for screening: python sheetN.py <dir> <cols> <rows> <width> [ink_min] [first] [last]
# Canvases whose ink fraction (from <dir>_ink.json, ink.py) is below ink_min are left out and listed in skipped.txt.
import os, sys, json
from glob import glob
from PIL import Image, ImageOps, ImageDraw
d, cols, rows, W = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
ink_min = float(sys.argv[5]) if len(sys.argv) > 5 else 0
lo = int(sys.argv[6]) if len(sys.argv) > 6 else 1; hi = int(sys.argv[7]) if len(sys.argv) > 7 else 9999
ink = json.load(open(f'{d}_ink.json')) if ink_min else {}
files = [f for f in sorted(glob(f'{d}/c*.jpg')) if lo <= int(os.path.basename(f)[1:4]) <= hi]
keep = [f for f in files if not ink_min or ink.get(os.path.basename(f)[1:4], 1) >= ink_min]
out = f'{d}_sheets'; os.makedirs(out, exist_ok=True)
open(f'{out}/skipped_{lo}_{hi}.txt', 'w').write('\n'.join(os.path.basename(f) for f in files if f not in keep))
per = cols * rows
for i in range(0, len(keep), per):
    grp = keep[i:i + per]; ids = [os.path.basename(f)[1:4] for f in grp]
    ims = []
    for f in grp:
        im = Image.open(f).convert('L'); im = im.resize((W, int(im.height * W / im.width)), Image.LANCZOS)
        ims.append(ImageOps.autocontrast(im, cutoff=1))
    h = max(im.height for im in ims); r = (len(ims) + cols - 1) // cols
    sh = Image.new('L', (W * cols, (h + 22) * r), 255); dr = ImageDraw.Draw(sh)
    for k, im in enumerate(ims):
        x = W * (k % cols); y = (h + 22) * (k // cols); sh.paste(im, (x, y + 22)); dr.text((x + 6, y + 4), 'c' + ids[k], fill=0)
    sh.save(f'{out}/s{ids[0]}_{ids[-1]}.jpg', quality=82)
print('kept', len(keep), 'of', len(files), 'sheets', (len(keep) + per - 1) // per)
