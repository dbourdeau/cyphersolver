"""Rank cart. 1597 key sheets by how well their signs match a family's cluster prototypes.
usage: python keyfind.py render | glyphs | rank <tokens.pkl>"""
import sys, os, glob, re, pickle, json
import numpy as np, cv2
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from signreader import load_binary, glyph_mask, feat

KEYIDS = [i for i in list(range(5301, 5415)) + [5469, 5470, 5471] if i not in (5380, 5391)]

def render():
    import pymupdf
    os.makedirs('keypng', exist_ok=True)
    for i in KEYIDS:
        for f in sorted(glob.glob(f'pdf/IMG_R{i}_*.pdf')):
            d = pymupdf.open(f)
            for k, pg in enumerate(d):
                o = f'keypng/R{i}_{os.path.basename(f)[-6:-4]}_{k}.png'
                if not os.path.exists(o): pg.get_pixmap(dpi=200).save(o)

def seg2d(ink, min_area=40, gap=5):
    n, lab, st, cen = cv2.connectedComponentsWithStats(ink, 8)
    comps = [[st[i, 0], st[i, 1], st[i, 0] + st[i, 2], st[i, 1] + st[i, 3], st[i, 4], [i]] for i in range(1, n) if st[i, 4] >= min_area]
    changed = True
    while changed:
        changed = False
        for a in range(len(comps)):
            for b in range(a + 1, len(comps)):
                A, B = comps[a], comps[b]
                if A[0] - gap <= B[2] and B[0] - gap <= A[2] and A[1] - gap <= B[3] and B[1] - gap <= A[3]:
                    comps[a] = [min(A[0], B[0]), min(A[1], B[1]), max(A[2], B[2]), max(A[3], B[3]), A[4] + B[4], A[5] + B[5]]
                    del comps[b]; changed = True; break
            if changed: break
    return comps, lab

def glyphs():
    out = []
    for p in sorted(glob.glob('keypng/*.png')):
        g, ink = load_binary(p, 30)
        h, w = ink.shape
        ink[int(h * 0.62):, :] = 0 if False else ink[int(h * 0.62):, :]   # keep whole page: nomenclators carry signs too
        comps, lab = seg2d(ink)
        for x0, y0, x1, y1, a, ids in comps:
            ww, hh = x1 - x0, y1 - y0
            if ww > 160 or hh > 160 or ww < 6 or hh < 8: continue   # words of the heading, rules, specks
            m = glyph_mask(lab, ids, x0, y0, ww, hh)
            out.append(dict(key=os.path.basename(p)[:5], mask=m, f=feat(m)[:-2]))
        print(p, len(comps), flush=True)
    pickle.dump(out, open('keyglyphs.pkl', 'wb'))

def rank(tok_pkl):
    recs, lab = pickle.load(open(tok_pkl, 'rb'))
    kg = pickle.load(open('keyglyphs.pkl', 'rb'))
    labs = np.array(lab); F = np.array([r['feat'][:-2] for r in recs])
    cents, wts = [], []
    for c in sorted(set(lab)):
        idx = labs == c
        cents.append(F[idx].mean(0)); wts.append(idx.sum())
    cents = np.array(cents); wts = np.array(wts, float); wts /= wts.sum()
    keys = sorted(set(g['key'] for g in kg))
    KF = {k: np.array([g['f'] for g in kg if g['key'] == k]) for k in keys}
    res = []
    for k in keys:
        if len(KF[k]) < 8: continue
        d = np.sqrt(((cents[:, None, :] - KF[k][None, :, :]) ** 2).sum(2)).min(1)
        res.append((float((d * wts).sum()), k, len(KF[k])))
    res.sort()
    for s, k, n in res[:12]: print(f'{s:.3f} {k} glyphs={n}')
    print('median', np.median([r[0] for r in res]), 'worst', res[-1])

if __name__ == '__main__':
    {'render': render, 'glyphs': glyphs}.get(sys.argv[1], lambda: rank(sys.argv[2]))()
