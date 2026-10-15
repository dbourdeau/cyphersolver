# Pen-shape step for the 1520-21 look-alike signs (3 Oct 2026): QB / 8, c / e / CE, AMP / EL.
# Each cipher line of R1136 and R1139 (native-resolution images) is cut into ink blobs (connected components merged when
# they overlap horizontally), sorted left to right. The blob sequence is aligned to the line's token sequence
# (r1136_pass4.txt / r1139_pass4.txt) by a monotone DP on blob width vs expected sign width; a token is cropped only
# where the alignment is one blob to one token. Crops of the target labels go to contact sheets in shapes21/ with
# their label and line, for clustering by eye; a measured feature table (height above/below the x-height band, hole
# count, width) is written to shapes21/features.tsv.
# Run: python shapes21.py
import os, sys, re, json
import numpy as np
from PIL import Image, ImageOps, ImageDraw
from scipy import ndimage
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'shapes21'); os.makedirs(OUT, exist_ok=True)
TARGET = {'QB', '8', 'c', 'e', 'CE', 'AMP', 'EL'}
SRC = {
 'R1136': ('img/IMG_R1136_I5740_P1.png', (880, 900, 2920, 1860), [66, 142, 212, 286, 365, 445, 520, 597, 679, 761, 842, 928], 'r1136_pass4.txt'),
 'R1139': ('img/IMG_R1139_I5752_P2.png', (900, 2080, 2940, 2800), [60, 130, 198, 264, 331, 411, 473, 565, 629, 694], 'r1139_pass4.txt'),
}

def tokens(line):
    s = re.sub(r'\[[^\]]*\]', ' ', line.split(':', 1)[1])
    toks = [x.rstrip('?') for x in s.split()]
    out = []; i = 0
    while i < len(toks):                       # merge ligatures that are one pen unit
        if toks[i] == 'o' and i + 2 < len(toks) and toks[i + 1] == 'SL' and toks[i + 2] == 'o': out.append('oSLo'); i += 3; continue
        if toks[i] in ('m', 'n', 'z', 'x') and i + 1 < len(toks) and toks[i + 1] == 't': out.append(toks[i] + '+'); i += 2; continue
        out.append(toks[i]); i += 1
    return out

def blobs(strip):
    a = np.array(strip).astype(float)
    ink = a < np.percentile(a, 50) - 45
    lab, n = ndimage.label(ink)
    objs = ndimage.find_objects(lab)
    bx = []
    for k, sl in enumerate(objs, 1):
        h = sl[0].stop - sl[0].start; w = sl[1].stop - sl[1].start
        if (lab[sl] == k).sum() < 25: continue
        bx.append([sl[1].start, sl[1].stop, sl[0].start, sl[0].stop])
    bx.sort()
    merged = []
    for b in bx:                               # merge horizontally overlapping blobs (dots, crosses)
        if merged and b[0] < merged[-1][1] - 4:
            m = merged[-1]; m[1] = max(m[1], b[1]); m[2] = min(m[2], b[2]); m[3] = max(m[3], b[3])
        else: merged.append(b)
    return merged

def align(B, T):
    # cost: blob width vs typical token width (oSLo, ligatures wider); DP allowing 1:1, 2 blobs:1 token, 1 blob:2 tokens
    wt = {t: (55 if t == 'oSLo' else 36 if t.endswith('+') or t in ('ss', 'ff', 'HH', 'w') else 24) for t in T}
    n, m = len(B), len(T); INF = 1e18
    D = np.full((n + 1, m + 1), INF); D[0, 0] = 0; P = {}
    for i in range(n + 1):
        for j in range(m + 1):
            if D[i, j] >= INF: continue
            for di, dj in ((1, 1), (2, 1), (1, 2), (1, 0), (0, 1)):
                if i + di > n or j + dj > m: continue
                bw = sum(B[i + k][1] - B[i + k][0] for k in range(di))
                tw = sum(wt[T[j + k]] for k in range(dj))
                c = abs(bw - tw) / 10 + (0 if (di, dj) == (1, 1) else 3 if dj and di else 6)
                if D[i, j] + c < D[i + di, j + dj]: D[i + di, j + dj] = D[i, j] + c; P[(i + di, j + dj)] = (i, j, di, dj)
    i, j = n, m; pairs = []
    while (i, j) in P:
        pi, pj, di, dj = P[(i, j)]
        if di == 1 and dj == 1: pairs.append((pi, pj))
        i, j = pi, pj
    return pairs[::-1]

def holes(crop):
    a = np.array(crop) < 128
    filled = ndimage.binary_fill_holes(a)
    lab, n = ndimage.label(filled & ~a)
    return int(sum(1 for k in range(1, n + 1) if (lab == k).sum() > 6))

def main():
    rows = []; crops = {t: [] for t in TARGET}
    for src, (img, box, centres, tf) in SRC.items():
        im = ImageOps.autocontrast(Image.open(os.path.join(HERE, img)).convert('L').crop(box), cutoff=1)
        lines = [l for l in open(os.path.join(HERE, tf), encoding='utf8') if l.startswith(src + ' ')]
        for li, (c, line) in enumerate(zip(centres, lines), 1):
            strip = im.crop((0, max(0, c - 45), im.width, c + 40))
            B = blobs(strip); T = tokens(line)
            pairs = align(B, T)
            for bi, tj in pairs:
                t = T[tj]
                if t not in TARGET: continue
                x0, x1, y0, y1 = B[bi]
                cr = strip.crop((max(0, x0 - 3), 0, x1 + 3, strip.height))
                bw = cr.point(lambda v: 0 if v < 128 else 255)
                rows.append((src, li, tj, t, x1 - x0, y0, y1, holes(bw)))
                crops[t].append((f'{src[-2:]}L{li}#{tj}', cr))
    with open(os.path.join(OUT, 'features.tsv'), 'w') as f:
        f.write('src\tline\ttok\tlabel\twidth\ttop\tbottom\tholes\n')
        for r in rows: f.write('\t'.join(map(str, r)) + '\n')
    for t, lst in crops.items():
        if not lst: continue
        W = 90; H = 110; cols = 10; n = len(lst)
        sheet = Image.new('L', (cols * W, ((n + cols - 1) // cols) * H), 255); d = ImageDraw.Draw(sheet)
        for k, (name, cr) in enumerate(lst):
            cr = cr.copy(); cr.thumbnail((W - 4, H - 18))
            x, y = (k % cols) * W, (k // cols) * H
            sheet.paste(cr, (x + 2, y + 2)); d.text((x + 2, y + H - 15), name, fill=0)
        sheet.save(os.path.join(OUT, f'sheet_{t}.png'))
        print(t, len(lst), 'crops')
    print('aligned crops total', len(rows))

if __name__ == '__main__':
    main()
