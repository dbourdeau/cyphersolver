"""Column-wise key matching: do the solver's cluster->letter assignments fit a key sheet's letter columns?
usage: python keycols.py glyphs | match <tokens.pkl(v2)> <solver_out.txt>"""
import sys, os, glob, pickle, re, collections, numpy as np, cv2
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from signreader import load_binary, glyph_mask
from keyfind import seg2d

def shape_feat(m, S=32):
    h, w = m.shape; side = max(h, w) + 2
    pad = np.zeros((side, side), np.uint8)
    pad[(side - h) // 2:(side - h) // 2 + h, (side - w) // 2:(side - w) // 2 + w] = m
    r = cv2.resize(pad, (S, S), interpolation=cv2.INTER_AREA).astype(np.float32) / 255
    r = cv2.GaussianBlur(r, (0, 0), 1.1).flatten()
    return r / (np.linalg.norm(r) + 1e-6) * 3

def rows_of(boxes, tol):
    rows = []
    for b in sorted(boxes, key=lambda b: b['cy']):
        if rows and abs(rows[-1][-1]['cy'] - b['cy']) <= tol: rows[-1].append(b)
        else: rows.append([b])
    # row centre = mean cy; merge rows whose means are close
    return rows

def build():
    out = {}
    for p in sorted(glob.glob('keypng/*.png')):
        g, ink = load_binary(p, 30)
        comps, lab = seg2d(ink)
        boxes = []
        for x0, y0, x1, y1, a, ids in comps:
            w, h = x1 - x0, y1 - y0
            if w > 150 or h > 150 or w < 5 or h < 7: continue
            boxes.append(dict(x=x0, y=y0, w=w, h=h, cx=x0 + w / 2, cy=y0 + h / 2, f=shape_feat(glyph_mask(lab, ids, x0, y0, w, h))))
        out[os.path.basename(p)[:5]] = boxes
        print(p, len(boxes), flush=True)
    pickle.dump(out, open('keycols_glyphs.pkl', 'wb'))

ORDER23 = list('abcdefghiklmnopqrstvxyz')
ORDER22 = list('abcdefghilmnopqrstvxyz')
ORDER21 = list('abcdefghilmnopqrstvxz')

def columns(boxes):
    """find the header row (>=19 glyphs with regular spacing near the top) and attach signs below to its columns"""
    if len(boxes) < 30: return None
    med = np.median([b['h'] for b in boxes])
    rows = rows_of(boxes, 0.7 * med)
    for ri, row in enumerate(rows[:6]):
        if 19 <= len(row) <= 26:
            xs = sorted(b['cx'] for b in row)
            gaps = np.diff(xs)
            if np.std(gaps) / np.mean(gaps) > 0.6: continue
            order = {23: ORDER23, 22: ORDER22, 21: ORDER21, 24: ORDER23 + ['z2'], 20: ORDER21[:20], 26: None, 25: None, 19: ORDER21[:19]}.get(len(row))
            if not order: continue
            hx = np.array(xs); sp = np.mean(gaps)
            cols = collections.defaultdict(list)
            # signs: glyphs below the header row, within one column spacing of a header x, up to 7 rows deep
            y_head = np.mean([b['cy'] for b in row])
            for b in boxes:
                if b['cy'] <= y_head + 0.6 * med or b['cy'] > y_head + 8 * 1.2 * med: continue
                j = int(np.argmin(np.abs(hx - b['cx'])))
                if abs(hx[j] - b['cx']) < 0.45 * sp: cols[order[j]].append(b['f'])
            if sum(len(v) for v in cols.values()) >= 20: return cols
    return None

def match(tok_pkl, keyf):
    recs, lab = pickle.load(open(tok_pkl, 'rb')); lab = np.array(lab)
    F = np.array([r['feat'][:1024] for r in recs])
    cnt = collections.Counter(lab); rank = {c: i for i, (c, _) in enumerate(cnt.most_common())}
    protos = {}
    for c in cnt: protos[rank[c]] = F[lab == c].mean(0)
    wts = {rank[c]: cnt[c] for c in cnt}
    key = {}
    for line in open(keyf, encoding='utf-8'):
        m = re.match(r'^([s\d|]+) - ([A-Za-z])$', line.strip())
        if m:
            for c in m.group(1).split('|'): key[int(c[1:])] = m.group(2).lower()
    kg = pickle.load(open('keycols_glyphs.pkl', 'rb'))
    rng = np.random.default_rng(0)
    cl = sorted(key); letters = [key[c] for c in cl]
    res = []
    for k, boxes in kg.items():
        cols = columns(boxes)
        if not cols: continue
        def score(lets):
            s = 0; wsum = 0
            for c, L in zip(cl, lets):
                col = cols.get(L)
                if not col: d = 3.0
                else: d = min(np.linalg.norm(protos[c] - f) for f in col)
                s += wts[c] * d; wsum += wts[c]
            return s / wsum
        real = score(letters)
        null = [score(list(rng.permutation(letters))) for _ in range(150)]
        z = (np.mean(null) - real) / (np.std(null) + 1e-9)
        res.append((z, k, round(real, 3), round(float(np.mean(null)), 3), sum(len(v) for v in cols.values()), len(cols)))
    res.sort(reverse=True)
    print('keys with columns:', len(res))
    for r in res[:12]: print(r)

if __name__ == '__main__':
    if sys.argv[1] == 'glyphs': build()
    else: match(sys.argv[2], sys.argv[3])
