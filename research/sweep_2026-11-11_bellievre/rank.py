# python3 rank.py <dir> [thr]  -- scores every canvas with det.score (cached in <dir>_scores.json), then builds crop sheets
# (native-scale 390x300 crops around the best window, 4x5 per sheet) of canvases scoring >= thr, best first.
import sys, os, json
from glob import glob
from PIL import Image, ImageDraw
import det
d = sys.argv[1]; thr = float(sys.argv[2]) if len(sys.argv) > 2 else 20
SC = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0   # 0.5 for colour single-page scans (same glyph size as the microfilm openings)
cf = d + '_scores.json'; sc = json.load(open(cf)) if os.path.exists(cf) else {}
for f in sorted(glob(d + '/c*.jpg')):
    k = os.path.basename(f)[1:5]
    if k not in sc:
        try: s = det.score(f, SC); sc[k] = [s[0], s[3][0], s[3][1]]
        except Exception as e: print('err', f, e)
        if len(sc) % 40 == 0: json.dump(sc, open(cf, 'w'))
json.dump(sc, open(cf, 'w'))
done_f = d + '_viewed.json'; done = set(json.load(open(done_f))) if os.path.exists(done_f) else set()
hits = sorted([k for k, v in sc.items() if v[0] >= thr and k not in done], key=lambda k: int(k))
out = d + '_crops'; os.makedirs(out, exist_ok=True)
CW, CH = 390, 300
for i in range(0, len(hits), 20):
    grp = hits[i:i + 20]; sh = Image.new('L', (CW * 4, (CH + 12) * ((len(grp) + 3) // 4)), 200); dr = ImageDraw.Draw(sh)
    for j, k in enumerate(grp):
        im = Image.open(f'{d}/c{k}.jpg').convert('L'); s, x, y = sc[k]
        if SC != 1.0: im = im.resize((int(im.width * SC * 1.3), int(im.height * SC * 1.3))); x *= 1.3; y *= 1.3
        cx, cy = x + 55, y + 22; x0 = int(min(max(cx - CW / 2, 0), max(im.width - CW, 0))); y0 = int(min(max(cy - CH / 2, 0), max(im.height - CH, 0)))
        X = CW * (j % 4); Y = (CH + 12) * (j // 4); sh.paste(im.crop((x0, y0, x0 + CW, y0 + CH)), (X, Y + 12)); dr.text((X + 2, Y), f'c{k} s={s:.0f}', fill=0)
    fn = f'{out}/r{grp[0]}_{grp[-1]}.jpg'; sh.save(fn, quality=82); print(fn)
json.dump(sorted(done | set(hits)), open(done_f, 'w'))
print(len(sc), 'scored;', len(hits), 'new hits >=', thr)
