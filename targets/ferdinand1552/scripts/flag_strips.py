"""Eye-pass sheets: lines of work/forced_<letter>.tsv with a sign flagged '!' (mismatch) or '-' (dropped).
Under each sign: index, chosen label; flagged signs in red with the flag. Reading at the right.
    python scripts/flag_strips.py 13oct [per_sheet]"""
import sys, pickle, pathlib, cv2
from PIL import Image, ImageDraw, ImageFont
ROOT = pathlib.Path(__file__).resolve().parent.parent
L = sys.argv[1]; per = int(sys.argv[2]) if len(sys.argv) > 2 else 12
P = pickle.load(open(ROOT / 'work/pages.pkl', 'rb'))
reading = {}
for l in open(ROOT / f'reading_{L}.txt', encoding='utf8'):
    if l.startswith('#') or not l.strip(): continue
    k, t = l.rstrip('\n').split('\t'); reading[k] = t
font = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', 14); fs = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 11)
rows = []
for l in open(ROOT / f'work/forced_{L}.tsv', encoding='utf8'):
    k, labs, ch, fl, idx = l.rstrip('\n').split('\t')
    if '!' not in fl and '-' not in fl: continue
    p, j = k.split('.'); j = int(j); idx = [int(x) for x in idx.split()]; ch = ch.split(); labs = labs.split()
    ss = sorted(P[p][j]['signs'], key=lambda s: s['x0']); sel = [ss[i] for i in idx]
    img = cv2.imread(str(ROOT / f'scans/c{p}.jpg'), 0)
    ys = sorted(s['y0'] for s in sel); ye = sorted(s['y1'] for s in sel)
    y0 = max(0, ys[len(ys)//2] - 22); y1 = ye[len(ye)//2] + 22
    x0 = max(0, min(s['x0'] for s in sel) - 6); x1 = max(s['x1'] for s in sel) + 6
    sc = 1.6; c = img[y0:y1, x0:x1]
    t = Image.fromarray(c).resize((int(c.shape[1]*sc), int(c.shape[0]*sc)), Image.LANCZOS).convert('RGB')
    W = max(1800, t.width + 60); R = Image.new('RGB', (W, t.height + 50), 'white'); R.paste(t, (50, 0))
    d = ImageDraw.Draw(R); d.text((0, 4), k, fill='blue', font=fs)
    for n, (s, lab, f) in enumerate(zip(sel, ch, fl)):
        xc = 50 + ((s['x0'] + s['x1'])/2 - x0)*sc; yy = t.height + (1 if n % 2 == 0 else 25)
        d.text((xc-6, yy), str(n), fill='blue', font=fs)
        bad = f in '!-'
        d.text((xc-8, yy+10), (f + lab) if bad else lab, fill='red' if bad else 'gray', font=font)
    d.text((50 + t.width + 10, 6), reading.get(k, ''), fill='darkgreen', font=font)
    rows.append(R)
out = ROOT / 'work/strips'; out.mkdir(exist_ok=True)
for f in out.glob(f'{L}_*.png'): f.unlink()
for b in range(0, len(rows), per):
    rr = rows[b:b+per]; S = Image.new('RGB', (max(r.width for r in rr), sum(r.height for r in rr)), 'white'); y = 0
    for r in rr: S.paste(r, (0, y)); y += r.height
    S.save(out / f'{L}_{b//per:02d}.png')
print(len(rows), 'lines,', (len(rows)+per-1)//per, 'sheets')
