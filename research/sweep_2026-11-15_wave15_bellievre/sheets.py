# python -I -X utf8 sheets.py <vol> [start end cols rows tilew]  -- contact sheets img/<vol>_sheets/sAAAA_BBBB.jpg, tiles labelled with the view (f) number
import os, sys
from PIL import Image, ImageDraw
here = os.path.dirname(os.path.abspath(__file__))
v = sys.argv[1]; d = os.path.join(here, 'img', v)
a = int(sys.argv[2]) if len(sys.argv) > 2 else 1; b = int(sys.argv[3]) if len(sys.argv) > 3 else 9999
cols, rows, W = (int(x) for x in sys.argv[4:7]) if len(sys.argv) > 6 else (4, 5, 480)
out = d + ('_sheets' if cols == 4 else f'_sheets{cols}x{rows}'); os.makedirs(out, exist_ok=True)
ids = [i for i in range(a, b + 1) if os.path.exists(f'{d}/c{i:04d}.jpg')]
per = cols * rows
for k in range(0, len(ids), per):
    grp = ids[k:k + per]
    fn = f'{out}/s{grp[0]:04d}_{grp[-1]:04d}.jpg'
    if os.path.exists(fn) and len(grp) == per: continue
    ims = []
    for i in grp:
        im = Image.open(f'{d}/c{i:04d}.jpg').convert('L')
        ims.append(im.resize((W, int(im.height * W / im.width)), Image.LANCZOS))
    h = sorted(im.height for im in ims)[len(ims)//2] + 6
    ims = [im.crop((0, 0, W, min(im.height, h))) for im in ims]
    sh = Image.new('L', (W * cols, h * ((len(grp) + cols - 1) // cols)), 255); dr = ImageDraw.Draw(sh)
    for j, im in enumerate(ims):
        x = W * (j % cols); y = h * (j // cols); sh.paste(im, (x, y))
        dr.rectangle([x, y, x + 40, y + 13], fill=255); dr.text((x + 3, y + 1), f'f{grp[j]}', fill=0)
    sh.save(fn, quality=80); print(fn, sh.size)
