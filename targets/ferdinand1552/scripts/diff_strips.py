"""Review strips for the eye pass: every cipher line whose decryption differs from the reading.

    python scripts/diff_strips.py 13oct [per_sheet]   -> work/strips/<letter>_<n>.png

Each row: the line at 1.5x, under each sign its index (blue) and current label; labels in red are the signs whose
letters the reading does not match (from the letter alignment of check_reading.py). The reading is printed at
the right. Labels come from work/transcription_<letter>.tsv if present, else the beam."""
import sys, re, pickle, pathlib, cv2, numpy as np
from PIL import Image, ImageDraw, ImageFont
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from transcribe import load_lines, key, emit_letters, toks
L = sys.argv[1]; per = int(sys.argv[2]) if len(sys.argv) > 2 else 10
only = sys.argv[3].split(',') if len(sys.argv) > 3 else None
P = pickle.load(open(ROOT / 'work/pages.pkl', 'rb'))
lines, reading = load_lines(L)
font = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', 14)
fs = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 11)


def align_signs(labs, rd):
    # letters emitted per sign
    em = [emit_letters(l) for l in labs]
    b = [(c, si) for si, e in enumerate(em) for c in e]
    a = toks(rd)
    n, m = len(a), len(b); D = np.zeros((n + 1, m + 1), int); D[:, 0] = range(n + 1); D[0, :] = range(m + 1)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i, j] = min(D[i-1, j] + 1, D[i, j-1] + 1, D[i-1, j-1] + (a[i-1] != b[j-1][0]))
    bad = set(); i, j = n, m
    while i > 0 or j > 0:
        if i > 0 and j > 0 and D[i, j] == D[i-1, j-1] + (a[i-1] != b[j-1][0]):
            if a[i-1] != b[j-1][0]: bad.add(b[j-1][1])
            i -= 1; j -= 1
        elif i > 0 and D[i, j] == D[i-1, j] + 1:
            # reading letter with no sign: flag neighbours
            if j > 0: bad.add(b[j-1][1])
            if j < m: bad.add(b[j][1])
            i -= 1
        else:
            bad.add(b[j-1][1]); j -= 1
    return bad, D[n, m]


rows = []
for k, (p, j, idx, labs) in lines.items():
    if only and k not in only: continue
    rd = reading.get(k, '')
    bad, d = align_signs(labs, rd)
    if d == 0 and not only: continue
    ss = sorted(P[p][j]['signs'], key=lambda s: s['x0'])
    sel = [ss[i] for i in idx]
    if not sel: continue
    img = cv2.imread(str(ROOT / f'scans/c{p}.jpg'), 0)
    y0 = max(0, min(s['y0'] for s in sel) - 6); y1 = max(s['y1'] for s in sel) + 6
    x0 = max(0, min(s['x0'] for s in sel) - 6); x1 = max(s['x1'] for s in sel) + 6
    sc = 1.5
    c = img[y0:y1, x0:x1]
    t = Image.fromarray(c).resize((int(c.shape[1] * sc), int(c.shape[0] * sc)), Image.LANCZOS).convert('RGB')
    W = max(1700, t.width + 60)
    R = Image.new('RGB', (W, t.height + 52), 'white'); R.paste(t, (50, 0))
    dr = ImageDraw.Draw(R)
    dr.text((0, 4), k, fill='blue', font=fs)
    for n_, (s, lab) in enumerate(zip(sel, labs)):
        xc = 50 + ((s['x0'] + s['x1']) / 2 - x0) * sc
        yy = t.height + (2 if n_ % 2 == 0 else 26)
        dr.text((xc - 6, yy), str(n_), fill='blue', font=fs)
        dr.text((xc - 8, yy + 11), lab, fill='red' if n_ in bad else 'black', font=font)
    dr.text((50 + t.width + 10, 6), rd, fill='darkgreen', font=font)
    rows.append(R)
out = ROOT / 'work/strips'; out.mkdir(exist_ok=True)
for f in out.glob(f'{L}_*.png'): f.unlink()
for b in range(0, len(rows), per):
    rr = rows[b:b + per]; H = sum(r.height for r in rr); W = max(r.width for r in rr)
    S = Image.new('RGB', (W, H), 'white'); y = 0
    for r in rr: S.paste(r, (0, y)); y += r.height
    S.save(out / f'{L}_{b // per:02d}.png')
print(len(rows), 'lines to review,', (len(rows) + per - 1) // per, 'sheets')
