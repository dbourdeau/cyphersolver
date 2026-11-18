# python -I -X utf8 rank.py <vol> <thr> <scale>  -- second-line check: scores every canvas with det.score (cached in
# img/<vol>_scores.json) and tiles a crop around the best window of each canvas scoring >= thr (20 per sheet, img/<vol>_crops/).
import sys, os, json
from glob import glob
from PIL import Image, ImageDraw
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
import det
v = sys.argv[1]; d = os.path.join(here, 'img', v); thr = float(sys.argv[2]); SC = float(sys.argv[3])
cf = d + '_scores.json'; sc = json.load(open(cf)) if os.path.exists(cf) else {}
for f in sorted(glob(d + '/c*.jpg')):
    k = os.path.basename(f)[1:5]
    if k not in sc:
        try: s = det.score(f, SC); sc[k] = [s[0], s[3][0], s[3][1]]
        except Exception as e: print('err', f, e)
json.dump(sc, open(cf, 'w'))
hits = sorted([k for k, x in sc.items() if x[0] >= thr], key=int)
out = d + '_crops'; os.makedirs(out, exist_ok=True); CW, CH = 390, 300
for i in range(0, len(hits), 20):
    grp = hits[i:i + 20]; sh = Image.new('L', (CW * 4, (CH + 12) * ((len(grp) + 3) // 4)), 200); dr = ImageDraw.Draw(sh)
    for j, k in enumerate(grp):
        im = Image.open(f'{d}/c{k}.jpg').convert('L'); s, x, y = sc[k]
        if SC != 1.0: im = im.resize((int(im.width * SC * 1.3), int(im.height * SC * 1.3))); x *= 1.3; y *= 1.3
        cx, cy = x + 55, y + 22; x0 = int(min(max(cx - CW / 2, 0), max(im.width - CW, 0))); y0 = int(min(max(cy - CH / 2, 0), max(im.height - CH, 0)))
        X = CW * (j % 4); Y = (CH + 12) * (j // 4); sh.paste(im.crop((x0, y0, x0 + CW, y0 + CH)), (X, Y + 12)); dr.text((X + 2, Y), f'f{int(k)} s={s:.0f}', fill=0)
    fn = f'{out}/r{grp[0]}_{grp[-1]}.jpg'; sh.save(fn, quality=82); print(fn[-18:])
import collections
print(len(sc), 'scored;', len(hits), 'hits >=', thr, '; score of f659:', sc.get('0659'))
vals = sorted(x[0] for x in sc.values()); print('quantiles', [vals[int(len(vals) * q)] for q in (.5, .9, .95, .98, .99)])
