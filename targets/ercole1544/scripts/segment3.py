# usage: segment3.py : rectifies each text line along its fitted curve, finds descender strokes, matches them in order to descender tokens with fitted sign widths.
# Writes scans/enh/strip_<line>.npy and round3/cells3.json (one record per token with its located x and whether it was matched to a stroke).
import json, re, sys
import numpy as np
from scipy import ndimage as ni
from grid import PAGES
C = json.load(open('round3/curves.json'))
TR = {}
for f in sys.argv[1:] or ['transcription_0078_0079.txt', 'transcription_0174_0175.txt']:
    for l in open(f, encoding='utf8'):
        if l.startswith('#') or not l.strip(): continue
        lab, _, b = l.strip().partition(' ')
        TR[lab] = re.findall(r'L\^\w+|\d+|\?|[A-Za-z]', b)
vocab = sorted({t for v in TR.values() for t in v}); vi = {t: i for i, t in enumerate(vocab)}
strips = {}; ext = {}; peaks = {}; HH = {}
for k, (p, n) in PAGES.items():
    a = np.load(f'scans/enh/ds_{p}.npy').astype(float); H = C[k]['H']; W = a.shape[1]
    bg = ni.gaussian_filter(a, 30)
    up, dn = int(.75*H), int(1.1*H)
    for i, c in enumerate(C[k]['lines']):
        L = f'{k}{i+1:02d}'; HH[L] = H
        f2, f1, f0, y = c
        xs = np.arange(W); ysh = (y+np.polyval([f2, f1, f0], xs)).astype(int)
        s = np.full((up+dn, W), 255.)
        for x in xs:
            lo = ysh[x]-up; hi = ysh[x]+dn
            lo2 = max(0, lo); hi2 = min(a.shape[0], hi)
            s[lo2-lo:lo2-lo+hi2-lo2, x] = a[lo2:hi2, x]/np.maximum(bg[lo2:hi2, x], 1)*235
        strips[L] = np.clip(s, 0, 255)
        ink = s < 165
        xh = ink[up-int(.2*H):up+int(.2*H)].sum(axis=0).astype(float)
        col = np.where(ni.uniform_filter1d(xh, 25) > 1.0)[0]
        m = int(W*.03); col = col[(col > m) & (col < W-m)]
        ext[L] = (int(col.min()), int(col.max()))
        band = ink[up+int(.3*H):up+int(.5*H)].sum(axis=0).astype(float)
        band = ni.gaussian_filter1d(band, 3)
        pk = [x for x in range(8, W-8) if band[x] == band[max(0, x-14):x+15].max() and band[x] > 1.2 and ext[L][0]-12 <= x <= ext[L][1]+12]
        mm = []
        for x in pk:
            if mm and x-mm[-1] < 6: continue
            mm.append(x)
        peaks[L] = mm
        np.save(f'scans/enh/strip_{L}.npy', strips[L].astype('uint8'))
labs = sorted(TR)
A = np.zeros((len(labs), len(vocab))); b = np.zeros(len(labs))
for r, L in enumerate(labs):
    for t in TR[L]: A[r, vi[t]] += 1
    b[r] = ext[L][1]-ext[L][0]
w = np.linalg.solve(A.T@A+3*np.eye(len(vocab)), A.T@b+3*np.full(len(vocab), b.sum()/A.sum()))
w = np.clip(w, 20, 200)
print('width', {t: round(float(w[vi[t]])) for t in 'gzqpfnxr'})
HARD = set('fgpqz')
def dflag(t):
    if t in HARD: return 1.0
    if t.isdigit() and re.search('[3479]', t): return .7
    if t == 'S': return .5
    if t == 't': return .3
    return 0
cells = []
for L in labs:
    toks = TR[L]; wt = np.array([w[vi[t]] for t in toks]); x0, x1 = ext[L]
    sc = (x1-x0)/wt.sum(); ex = x0+np.cumsum(wt*sc)-wt*sc/2
    H = HH[L]; dt = [(i, t, dflag(t)) for i, t in enumerate(toks) if dflag(t) > 0]; pk = peaks[L]
    n, m = len(dt), len(pk)
    D = np.zeros((n+1, m+1)); D[:, 0] = np.cumsum([0]+[.9*H*d[2] for d in dt]); D[0, :] = np.arange(m+1)*.2*H
    Bk = {}
    for i in range(1, n+1):
        for j in range(1, m+1):
            o = [(D[i-1, j-1]+abs(ex[dt[i-1][0]]-pk[j-1]), 's'), (D[i-1, j]+.9*H*dt[i-1][2], 'u'), (D[i, j-1]+.2*H, 'd')]
            D[i, j], Bk[i, j] = min(o, key=lambda v: v[0])
    i, j = n, m; pairs = {}
    while i and j:
        op = Bk[i, j]
        if op == 's': pairs[dt[i-1][0]] = pk[j-1]; i -= 1; j -= 1
        elif op == 'u': i -= 1
        else: j -= 1
    for ti, t in enumerate(toks):
        cx = pairs.get(ti); mth = 'p'
        if cx is None:
            left = [q for q in pairs if q < ti]; right = [q for q in pairs if q > ti]; base = ex[ti]
            if left and right:
                l, r = max(left), min(right); base = pairs[l]+(pairs[r]-pairs[l])*(ex[ti]-ex[l])/max(1, ex[r]-ex[l])
            cx = int(base); mth = 'i'
        cells.append(dict(line=L, ti=ti, tok=t, n=len(toks), cx=int(cx), H=H, m=mth))
json.dump(cells, open('round3/cells3.json', 'w'))
hd = [c for c in cells if c['tok'] in HARD]
print('hard', len(hd), sum(c['m'] == 'p' for c in hd), 'gz', sum(c['tok'] in 'gz' for c in cells), sum(c['tok'] in 'gz' and c['m'] == 'p' for c in cells))
