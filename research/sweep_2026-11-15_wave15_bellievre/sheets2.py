# python -I -X utf8 sheets2.py <vol> <start> <end> [cols rows tilew]  -- contact sheets that leave out blank pages
# (ink fraction < 0.0045, see ink.py; the skipped views are listed in img/<vol>_blank.json). Tiles carry the view (f) number.
import os, sys, json
from PIL import Image, ImageDraw
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)   # -I drops the script folder
from ink import ink
v = sys.argv[1]; d = os.path.join(here, 'img', v); a = int(sys.argv[2]); b = int(sys.argv[3])
cols, rows, W = (int(x) for x in sys.argv[4:7]) if len(sys.argv) > 6 else (6, 3, 320)
out = d + '_s2'; os.makedirs(out, exist_ok=True)
cf = d + '_ink.json'; I = json.load(open(cf)) if os.path.exists(cf) else {}
ids = []
for i in range(a, b + 1):
    f = f'{d}/c{i:04d}.jpg'
    if not os.path.exists(f): continue
    if str(i) not in I: I[str(i)] = ink(f)[0]
    if I[str(i)] >= 0.0045: ids.append(i)
json.dump(I, open(cf, 'w'))
json.dump(sorted(int(k) for k, x in I.items() if x < 0.0045), open(d + '_blank.json', 'w'))
per = cols * rows
for k in range(0, len(ids), per):
    grp = ids[k:k + per]; ims = []
    for i in grp:
        im = Image.open(f'{d}/c{i:04d}.jpg').convert('L')
        ims.append(im.resize((W, int(im.height * W / im.width)), Image.LANCZOS))
    h = sorted(im.height for im in ims)[len(ims) // 2] + 6
    ims = [im.crop((0, 0, W, min(im.height, h))) for im in ims]
    sh = Image.new('L', (W * cols, h * ((len(grp) + cols - 1) // cols)), 255); dr = ImageDraw.Draw(sh)
    for j, im in enumerate(ims):
        x = W * (j % cols); y = h * (j // cols); sh.paste(im, (x, y))
        dr.rectangle([x, y, x + 40, y + 13], fill=255); dr.text((x + 3, y + 1), f'f{grp[j]}', fill=0)
    fn = f'{out}/s{grp[0]:04d}_{grp[-1]:04d}.jpg'; sh.save(fn, quality=80); print(fn[-19:], len(grp))
