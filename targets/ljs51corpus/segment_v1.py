"""Line finder and sign segmenter for the Penn LJS 51 master TIFFs (0084_NNNN.tif, about 2340 x 2960).

    from segment import segment_page
    lines = segment_page(35)          # list of dicts, top to bottom

Each line: {'index', 'y0', 'y1', 'x0', 'x1', 'kind': 'cipher'|'arabic', 'features', 'items'}.
For cipher lines `items` is the signs right to left: {'kind': 'sign'|'divider', 'box': [x0, y0, x1, y1],
'red': [[x0, y0, x1, y1], ...] (red letters attached to that sign), 'merged': True if a touching pair was cut}.
`line['red_letters']` lists every red letter box with the index of the item it is attached to.

Command line:  python segment.py 35 36 37          (writes output/ljs51/signs/<image>/ and prints counts)
               python segment.py 35 --overlay      (also writes output/ljs51/crops/s_<image>_overlay.png)
See README.md in this folder for the parameters and failure modes.
"""
import os, sys, json, subprocess
import numpy as np, cv2
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MASTER = os.path.join(ROOT, 'output', 'ljs51', 'master')
SIGNS = os.path.join(ROOT, 'output', 'ljs51', 'signs')
CROPS = os.path.join(ROOT, 'output', 'ljs51', 'crops')
URL = 'https://openn.library.upenn.edu/Data/0001/ljs51/data/master/0084_%04d.tif'

# ---- parameters (pixels refer to the 2340 x 2960 master) -------------------------------------------------------
P = dict(
    ink_depth=75,        # a pixel is ink if it is this much darker than the local paper (0-255 grey)
    faint_page=0,        # if > 0: pages whose median ink depth is below this use the looser faint_* thresholds (off: it
                         # rescued some signs on f. 1v but produced garbage on f. 1r; see README)
    faint_depth=60, faint_peak=85, faint_mean=80,   # looser ink thresholds, used when the page's ink is pale (median depth < 115)
    ink_mean=100,        # ... and its mean depth at least this (drops grey smudges)
    ink_rel=0.8,         # a piece whose mean depth is below this share of the page median is a stain, not ink
    ink_peak=105,        # a connected ink piece is kept only if its darkest pixel is this much darker (drops show-through)
    red_excess=45,       # red ink: R - (G+B)/2 at least this
    paper_erode=61,      # ink closer than this to the page edge is ignored
    body_area=250,       # a piece this big is a "body" (sign, stem, or Arabic stroke); smaller ones are dots / specks
    dot_max_area=260,    # a piece up to this area, small in both directions, is a dot / flag candidate
    speck_area=45,       # smaller than this is noise
    line_prom=0.07,      # a text line is a peak of the row profile at least this share of the highest peak
    margin_gap=2.0,      # a piece starting more than this many sign widths right of the block's right margin is dropped
    fuse_h2=1.0, fuse_bot2=0.07,   # a fused divider shorter than 1.1 unit is accepted if its stem is this thin
    stray_left=3.0, stray_right=2.5,   # gaps (in median sign widths) that cut stray pieces off the line ends       # an end piece separated from the line by a gap of this many median sign widths is dropped
    stem_ratio=2.4,      # a divider stem is at least this many times taller than wide (and at most 0.36 unit wide)
    split_ratio=3.4,     # a piece wider than this many median sign widths is a touching group and gets cut
    wide_ratio=1.7,      # ... a piece wider than this is only flagged 'wide' (big signs such as the comb square are 2 x median)
)


# ---- I/O -------------------------------------------------------------------------------------------------------
def master_path(n):
    return os.path.join(MASTER, '0084_%04d.tif' % n)


def load_rgb(n):
    """Master TIFF as an RGB array; downloads it with curl if missing or truncated."""
    p = master_path(n)
    for attempt in (0, 1):
        if not os.path.exists(p) or os.path.getsize(p) < 1000:
            os.makedirs(MASTER, exist_ok=True)
            subprocess.run(['curl', '-s', '-o', p, URL % n], check=True)
        try:
            return np.array(Image.open(p).convert('RGB'))
        except OSError:
            if attempt:
                raise
            os.remove(p)
    raise OSError(p)


# ---- ink and pieces --------------------------------------------------------------------------------------------
def paper_mask(g):
    paper = (cv2.blur(g, (15, 15)) > 110).astype(np.uint8)
    nl, lab, st, _ = cv2.connectedComponentsWithStats(paper)
    k = 1 + int(np.argmax(st[1:, 4]))
    ff = (lab == k).astype(np.uint8) * 255
    inv = 255 - ff
    m = np.zeros((g.shape[0] + 2, g.shape[1] + 2), np.uint8)
    cv2.floodFill(inv, m, (0, 0), 0)          # fill the text holes: whatever the outside cannot reach is page
    paper = ((ff > 0) | (inv > 0)).astype(np.uint8)
    e = P['paper_erode']
    return cv2.erode(paper, np.ones((e, e), np.uint8))


def make_ink(rgb, faint=False):
    """Return (black ink mask, red ink mask, depth map)."""
    g = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    bg = cv2.morphologyEx(g, cv2.MORPH_CLOSE, np.ones((41, 41), np.uint8))
    bg = cv2.GaussianBlur(bg, (0, 0), 20)
    # depth below the local paper, rescaled so a stained (darker) patch of paper counts like clean paper (bg 172)
    d = ((bg.astype(np.float32) - g) * (172.0 / np.maximum(bg.astype(np.float32), 60.0))).astype(np.int16)
    pm = paper_mask(g) > 0
    r = rgb.astype(np.int16)
    redness = r[..., 0] - (r[..., 1] + r[..., 2]) // 2
    red = (redness > P['red_excess']) & (d > 30) & pm
    red = cv2.dilate(red.astype(np.uint8), np.ones((3, 3), np.uint8)) > 0
    dep, pk_t, mn_t = (P['faint_depth'], P['faint_peak'], P['faint_mean']) if faint else (P['ink_depth'], P['ink_peak'], P['ink_mean'])
    blk = (d > dep) & pm & ~red
    blk = blk.astype(np.uint8)
    # drop pieces whose darkest pixel is faint (show-through of the other side) or whose mean depth is low (smudges)
    nl, lab, st, _ = cv2.connectedComponentsWithStats(blk, connectivity=8)
    peak = np.zeros(nl, np.int16)
    np.maximum.at(peak, lab.ravel(), d.ravel())
    tot = np.bincount(lab.ravel(), weights=d.ravel().astype(np.float64), minlength=nl)
    mean = tot / np.maximum(st[:, 4], 1)
    keep = (peak >= pk_t) & (mean >= mn_t)
    keep[0] = False
    big = keep & (st[:, 4] >= P['body_area'])
    if big.sum() > 8:                      # smudges and stains are paler than the page's ink: drop pieces well below its median
        M = float(np.median(mean[big]))
        keep &= ~((st[:, 4] >= 120) & (mean < P['ink_rel'] * M))
    blk = keep[lab].astype(np.uint8)
    # red: small clean closing, then drop specks
    redm = cv2.morphologyEx(red.astype(np.uint8), cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8))
    nl, lab, st, _ = cv2.connectedComponentsWithStats(redm, connectivity=8)
    keep = st[:, 4] >= 25
    keep[0] = False
    redm = keep[lab].astype(np.uint8)
    return blk, redm, d


def pieces(mask, min_area):
    nl, lab, st, cen = cv2.connectedComponentsWithStats(mask, connectivity=8)
    out = []
    for i in range(1, nl):
        x, y, w, h, a = [int(v) for v in st[i]]
        if a < min_area:
            continue
        out.append(dict(id=i, x=x, y=y, w=w, h=h, area=a, cx=x + w / 2, cy=y + h / 2))
    return out, lab


# ---- text lines ------------------------------------------------------------------------------------------------
def find_skew(body):
    xs = np.array([p['cx'] for p in body])
    ys = np.array([p['cy'] for p in body])
    ws = np.array([np.sqrt(p['area']) for p in body])
    best = (-1, 0.0)
    for a in np.arange(-6.0, 6.01, 0.1):
        t = np.tan(np.radians(a))
        yy = ys - xs * t
        h, _ = np.histogram(yy, bins=np.arange(yy.min() - 5, yy.max() + 10, 6), weights=ws)
        s = float((h ** 2).sum())
        if s > best[0]:
            best = (s, t)
    return best[1]


def main_columns(body, bin_w=60, max_gap=2):
    """x-range of the text block: the densest run of occupied x bins (pieces' centres), runs separated by at most
    `max_gap` empty bins.  Cuts the spine shadow and the fore-edge stripes, which sit apart from the text."""
    big = [p for p in body if p['area'] >= 300]
    if not big:
        return 0, 10 ** 6
    xs = np.array([p['cx'] for p in big])
    nb = int(xs.max() // bin_w) + 2
    cnt = np.bincount((xs // bin_w).astype(int), minlength=nb)
    runs, cur, gap = [], None, 0
    for i, c in enumerate(cnt):
        if c > 0:
            if cur is None:
                cur = [i, i, c]
            else:
                cur[1] = i; cur[2] += c
            gap = 0
        elif cur is not None:
            gap += 1
            if gap > max_gap:
                runs.append(cur); cur = None
    if cur is not None:
        runs.append(cur)
    r = max(runs, key=lambda r: r[2])
    return r[0] * bin_w - 40, (r[1] + 1) * bin_w + 40


def find_lines(pcs, slope):
    """Row profile of the pieces' ink in sheared coordinates y' = y - slope*x, cut at the valleys between
    prominent peaks.  Returns the list of (top, bottom) y' ranges, top to bottom."""
    from scipy.signal import find_peaks
    big = [p for p in pcs if p['area'] >= 120]
    wts, ys = [], []
    for p in big:                      # each piece spreads its area over its vertical extent
        yc = p['cy'] - p['cx'] * slope
        a, b = int(yc - p['h'] / 2), int(yc + p['h'] / 2) + 1
        ys.append((a, b)); wts.append(p['area'] / max(b - a, 1))
    lo = min(a for a, b in ys); hi = max(b for a, b in ys)
    prof = np.zeros(hi - lo + 2)
    for (a, b), w in zip(ys, wts):
        prof[a - lo:b - lo] += w
    sm = np.convolve(prof, np.ones(13) / 13, 'same')
    pk, _ = find_peaks(sm, prominence=P['line_prom'] * sm.max(), distance=60)
    if len(pk) == 0:
        return []
    cuts = [0]
    for a_, b_ in zip(pk[:-1], pk[1:]):
        cuts.append(a_ + int(np.argmin(sm[a_:b_])))
    cuts.append(len(sm))
    pitch = float(np.median(np.diff(pk))) if len(pk) > 1 else 160.0
    cuts[0] = max(cuts[0], int(pk[0] - 0.7 * pitch))          # the first and last line are bounded, not open-ended
    cuts[-1] = min(cuts[-1], int(pk[-1] + 0.7 * pitch))
    return [(c0 + lo, c1 + lo) for c0, c1 in zip(cuts[:-1], cuts[1:])]


# ---- cipher / Arabic -------------------------------------------------------------------------------------------
def n_dotted_stems(items, allp, lab, u):
    """Stems with at least two dot-sized pieces on top (the divider signature), or a stem fused with its dots."""
    n = 0
    for p in items:
        if not is_stem(p, lab, u):
            continue
        dots = [q for q in allp if q is not p and q['w'] <= 0.65 * u and q['h'] <= 0.7 * u
                and abs(q['cx'] - p['cx']) <= 0.32 * u and p['y'] - 1.1 * u <= q['y'] <= p['y'] + 0.13 * u]
        if len(dots) >= 2 or p['w'] > 0.3 * u:
            n += 1
    return n


def line_features(items, allp, lab):
    """items: the body pieces of the line; allp: every piece (incl. dots) assigned to it."""
    ws = np.array([p['w'] for p in items], float)
    hs = np.array([p['h'] for p in items], float)
    ar = np.array([p['area'] for p in items], float)
    nsmall = sum(1 for p in allp if p['area'] < P['body_area'])
    signlike = [p for p in items if 22 <= p['w'] <= 115 and 35 <= p['h'] <= 115]
    u = float(np.median(hs))
    nd = n_dotted_stems(items, allp, lab, u)
    f = dict(
        n_body=len(items), n_small=nsmall,
        med_w=float(np.median(ws)), max_w=float(ws.max()),
        wide_frac=float(ar[ws > 130].sum() / ar.sum()),
        aspect_frac=float(ar[ws > 2.3 * hs].sum() / ar.sum()),
        w_cv=float(ws.std() / ws.mean()), h_cv=float(hs.std() / hs.mean()),
        n_w100=int((ws > 100).sum()),
        signlike_frac=len(signlike) / len(items),
        n_div=nd, div_rate=nd / len(items), unit=u,
    )
    return f


def classify(f):
    """Cipher signs are single glyphs at most about 100 px wide (a rare touching pair reaches 110-150), so a
    cipher line has at most 2 pieces wider than 100 px (0-1 on nearly every line); naskh joins letters into words
    and has 3 or more (3-8 on every Arabic line of the test pages).  Lines with almost no pieces, a very wide piece
    or most of their ink in wide pieces are Arabic as well.
    Two overrides for blocks whose signs are letter-like shapes (ff. 1r-1v, red gloss): a line with five or more red
    letters just above it is cipher (naskh has no red), and so is a line with at least 3 dotted dividers making up
    a fifth of its pieces (no Arabic line of the test pages has that)."""
    if f.get('n_red', 0) >= 5:
        return 'cipher'
    if f['n_div'] >= 3 and f['div_rate'] >= 0.2 and f['max_w'] <= 200:
        return 'cipher'
    if f['n_w100'] >= 3 or f['wide_frac'] > 0.3 or f['aspect_frac'] > 0.35 or f['max_w'] > 180:
        return 'arabic'
    if f['n_body'] < 3:
        return 'arabic'
    return 'cipher'


# ---- sign segmentation -----------------------------------------------------------------------------------------
def has_hole(p, lab, min_area=18):
    m = (lab[p['y']:p['y'] + p['h'], p['x']:p['x'] + p['w']] == p['id']).astype(np.uint8)
    m = cv2.copyMakeBorder(m, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=0)
    cs, hier = cv2.findContours(m, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    if hier is None:
        return False
    return any(hier[0][i][3] >= 0 and cv2.contourArea(c) >= min_area for i, c in enumerate(cs))


def is_stem(p, lab, u=76.0):
    """Divider stem shape: narrow and tall, one unbroken stroke in its lower half (so a flat arch with two legs is not
    one).  Returns 'thin' (stem alone; the dots are separate pieces), 'fused' (stem fused with its dots) or None."""
    w, h = p['w'], p['h']
    if h < 0.45 * u or w > 0.58 * u:
        return None
    m = (lab[p['y']:p['y'] + h, p['x']:p['x'] + w] == p['id'])
    low = m[h // 2:]
    rw = low.sum(1)
    bot = float(np.median(rw))
    if bot > 0.28 * u:
        return None
    runs = (np.diff(np.pad(low.astype(np.int8), ((0, 0), (1, 0))), axis=1) == 1).sum(1)
    if (runs >= 2).mean() > 0.15:
        return None
    top = float(m[:max(h // 3, 1)].sum(1).max())
    if w <= 0.36 * u and h >= P['stem_ratio'] * w:
        return 'thin'
    # stem fused with its dots: head up to ~1.7x wider than the stem and the stem hangs below it
    if (top <= 0.56 * u and top >= 1.4 * bot and bot <= 0.19 * u and not has_hole(p, lab)
            and (h >= 1.1 * u or (h >= P['fuse_h2'] * u and bot <= P['fuse_bot2'] * u))):
        return 'fused'
    return None


def box(p):
    return [p['x'], p['y'], p['x'] + p['w'], p['y'] + p['h']]


def union(a, b):
    return [min(a[0], b[0]), min(a[1], b[1]), max(a[2], b[2]), max(a[3], b[3])]


def xover(a, b):
    return max(0, min(a[2], b[2]) - max(a[0], b[0]))


def cut_touching(p, lab, medw):
    """Cut a piece that is a run of touching signs at valleys of its column profile."""
    x, y, w, h = p['x'], p['y'], p['w'], p['h']
    k = int(round(w / medw))
    if k < 2:
        return [box(p)]
    m = (lab[y:y + h, x:x + w] == p['id']).astype(np.uint8)
    prof = m.sum(0).astype(float)
    prof = np.convolve(prof, np.ones(3) / 3, 'same')
    cuts = []
    for j in range(1, k):
        e = w * j / k
        lo, hi = int(max(2, e - 0.28 * medw)), int(min(w - 2, e + 0.28 * medw))
        if hi <= lo:
            return [box(p)]
        cuts.append(lo + int(np.argmin(prof[lo:hi])))
    cuts = [0] + sorted(set(cuts)) + [w]
    out = []
    for a, b in zip(cuts[:-1], cuts[1:]):
        if b - a < 10:
            continue
        sub = m[:, a:b]
        ys = np.where(sub.any(1))[0]
        if len(ys) == 0:
            continue
        out.append([x + a, y + int(ys.min()), x + b, y + int(ys.max()) + 1])
    return out or [box(p)]


def segment_cipher_line(items, smalls, lab, medw, u, right_edge=1e9):
    """items: body pieces, smalls: dot-sized pieces on the line. Returns ordered right-to-left items."""
    # filled blobs far smaller than a sign are dots or ink spots, not signs (a ring sign has a hole)
    small_blobs = [p for p in items if p['w'] < 0.42 * u and p['h'] < 0.42 * u and not has_hole(p, lab, 5)]
    if small_blobs:
        smalls = smalls + small_blobs
        items = [p for p in items if p not in small_blobs]
    # 0. strays at the ends of the line (marginalia, stains, the neighbouring page): a piece cut off from the rest by
    #    a gap of several sign widths is dropped
    items = sorted(items, key=lambda p: p['x'])
    # left end: at most 2 pieces cut off by a gap of 3 sign widths (spine shadow, stains); right end: at most 6 pieces cut
    # off by a gap of 2.5 sign widths (facing page, fore-edge, marginal notes).  Bigger groups are kept (a real block).
    def gaps(its):
        return [its[i + 1]['x'] - max(q['x'] + q['w'] for q in its[:i + 1]) for i in range(len(its) - 1)]
    g = gaps(items)
    gm = float(np.median([max(x, 0) for x in g])) if g else 0.0       # typical gap of this line (letter-like blocks are sparse)
    thr_l = max(P['stray_left'] * medw, 4.0 * gm + 30)
    thr_r = max(P['stray_right'] * medw, 3.5 * gm + 30)
    for i, gp in enumerate(g):
        if gp > thr_l and i + 1 <= 2 and len(items) - (i + 1) >= 5:
            items = items[i + 1:]
            break
    g = gaps(items)
    for i in range(len(g) - 1, -1, -1):
        if g[i] > thr_r and len(items) - (i + 1) <= 6 and i + 1 >= 5:
            items = items[:i + 1]
            break
    items = [p for p in items if p['x'] <= right_edge]   # right of the block's right margin
    # 1. dividers: stems (with or without separate dots above)
    shape = {p['id']: is_stem(p, lab, u) for p in items}
    stems = [p for p in items if shape[p['id']]]
    others = [p for p in items if not shape[p['id']]]
    divs = []
    for s_ in stems:
        divs.append(dict(kind='divider', box=box(s_), cx=s_['cx'], piece=s_, fused=shape[s_['id']] == 'fused'))
    # dots belonging to a divider: small pieces sitting on top of the stem (any area: big round dots are 'body' pieces)
    used = set()
    for dv in divs:
        sb = dv['box']
        scx = (sb[0] + sb[2]) / 2
        for q in smalls + [p for p in others if p['w'] <= 0.65 * u and p['h'] <= 0.7 * u]:
            if q['id'] in used:
                continue
            qb = box(q)
            qcx = (qb[0] + qb[2]) / 2
            if abs(qcx - scx) <= 0.3 * u and sb[1] - 1.1 * u <= qb[1] and qb[3] <= sb[1] + 0.6 * u:
                dv['box'] = union(dv['box'], qb)
                dv['dots'] = dv.get('dots', 0) + 1
                used.add(q['id'])
    # a thin stem with no dots on it is a sign (numeral 1, alif, ...), not a divider
    keep = []
    for dv in divs:
        if dv['fused'] or dv.get('dots'):
            keep.append(dv)
        else:
            others.append(dv['piece'])
    divs = keep
    others = [p for p in others if p['id'] not in used]
    # 2. signs: body pieces; attach dots/flags and cut touching groups
    sg = []
    for p in others:
        sg.append(dict(kind='sign', box=box(p), piece=p))
    # join fragments of one sign: a body piece that sits (almost) completely above/below another within its x-range
    changed = True
    while changed:
        changed = False
        sg.sort(key=lambda s: s['box'][0])
        for i in range(len(sg)):
            for j in range(i + 1, len(sg)):
                a, b = sg[i]['box'], sg[j]['box']
                ov = xover(a, b)
                wa, wb = a[2] - a[0], b[2] - b[0]
                small = sg[i] if sg[i]['piece']['area'] < sg[j]['piece']['area'] else sg[j]
                if ov >= 0.6 * min(wa, wb) and small['piece']['area'] < 900 and \
                        min(wa, wb) < 0.8 * medw and max(a[1], b[1]) - min(a[3], b[3]) < 0.33 * u:
                    sg[i]['box'] = union(a, b)
                    sg[i]['piece'] = dict(sg[i]['piece'], area=sg[i]['piece']['area'] + sg[j]['piece']['area'])
                    del sg[j]
                    changed = True
                    break
            if changed:
                break
    orphans, cnt, lostdiv = [], [], []
    for q in smalls:
        if q['id'] in used:
            continue
        qb = box(q)
        if q['area'] < P['speck_area']:
            continue
        best, bd = None, 1e9
        for s in sg:
            b = s['box']
            dx = max(b[0] - qb[2], qb[0] - b[2], 0)
            dy = max(b[1] - qb[3], qb[1] - b[3], 0)
            dd = np.hypot(dx, dy)
            if dd < bd:
                best, bd = s, dd
        if best is not None and bd <= 0.19 * u:
            best['box'] = union(best['box'], qb)
        else:
            orphans.append(qb)
    # a divider whose stem is lost: two or more dots clustered together, away from any sign
    orphans.sort(key=lambda b: b[0])
    grp = []
    for qb in orphans:
        if grp and qb[0] - grp[-1][2] <= 0.4 * u:
            grp[-1] = union(grp[-1], qb); cnt[-1] += 1
        else:
            grp.append(list(qb)); cnt.append(1)
    for b, c in zip(grp, cnt):
        if c >= 2:
            lostdiv.append(dict(kind='divider', box=b, stemless=True))
    out = []
    for s in sg:
        w = s['box'][2] - s['box'][0]
        if w > P['split_ratio'] * medw and s['piece']['w'] == w:
            bs = cut_touching(s['piece'], lab, medw)
            for b in bs:
                out.append(dict(kind='sign', box=b, merged=len(bs) > 1))
        else:
            e = dict(kind='sign', box=s['box'])
            if w > P['wide_ratio'] * medw:
                e['wide'] = True
            out.append(e)
    for dv in divs:
        out.append(dict(kind='divider', box=dv['box']))
    out.extend(lostdiv)
    out.sort(key=lambda e: -(e['box'][0] + e['box'][2]))
    return out


# ---- red letters -----------------------------------------------------------------------------------------------
def attach_red(lines, redp):
    """Red letters sit just above the sign they gloss.  Each red letter goes to the sign below it: horizontally the
    nearest centre within 0.8 sign widths, vertically the smallest gap between the letter's bottom and the sign's top
    (the sign may begin up to 15 px above the letter's centre).  Letters with no sign below them stay unattached
    (page['red_unattached'])."""
    cands = []
    for L in lines:
        if L['kind'] != 'cipher':
            continue
        L['red_letters'] = []
        for i, it in enumerate(L['items']):
            if it['kind'] == 'sign':
                cands.append((L, i, it))
    unattached = []
    for q in redp:
        qb = box(q)
        qcx = (qb[0] + qb[2]) / 2
        best, bs = None, 1e9
        for L, i, it in cands:
            b = it['box']
            w = b[2] - b[0]
            dx = abs((b[0] + b[2]) / 2 - qcx)
            if dx > 0.8 * max(w, 30):
                continue
            gap = b[1] - qb[3]
            if gap < -45 or gap > 110:
                continue
            sc = max(gap, 0) + 0.6 * dx
            if sc < bs:
                best, bs = (L, i, it), sc
        if best is None:
            unattached.append(qb)
        else:
            L, i, it = best
            it.setdefault('red', []).append(qb)
            L['red_letters'].append(dict(box=qb, item=i))
    return unattached


# ---- page ------------------------------------------------------------------------------------------------------
_cache = {}


def analyse_page(n):
    if n in _cache:
        return _cache[n]
    rgb = load_rgb(n)
    blk, redm, d = make_ink(rgb)
    if np.median(d[blk > 0]) < P['faint_page']:
        blk, redm, d = make_ink(rgb, faint=True)
    allp, lab = pieces(blk, P['speck_area'])
    body0 = [p for p in allp if p['area'] >= P['body_area'] and p['w'] < 700 and p['h'] < 420]
    xl, xr = main_columns(body0) if len(body0) > 8 else (0, 10 ** 6)
    allp = [p for p in allp if xl <= p['cx'] <= xr]
    # red letters: merge a letter with its own dots / accents (pieces within about 10 px), then shrink the box back
    rd = cv2.dilate(redm, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11)))
    redp, redlab = pieces(rd, 60)
    for q in redp:
        q['x'] += 5; q['y'] += 5; q['w'] -= 10; q['h'] -= 10
        q['cx'] = q['x'] + q['w'] / 2; q['cy'] = q['y'] + q['h'] / 2
    redp = [q for q in redp if q['w'] > 4 and q['h'] > 4 and q['h'] < 150]
    body = [p for p in allp if p['area'] >= P['body_area'] and p['w'] < 700 and p['h'] < 420]
    slope = find_skew(body) if len(body) > 8 else 0.0
    pitch = 0
    lines = []
    ranges = find_lines(body, slope) if len(body) > 5 else []
    if not ranges:
        _cache[n] = (rgb.shape, lines, slope, pitch, [])
        return _cache[n]
    for p in allp:
        p['yy'] = p['cy'] - p['cx'] * slope
    groups = ranges
    centers = [(a + b) / 2 for a, b in ranges]
    assigned = [[] for _ in groups]
    for p in allp:
        for k, (a, b) in enumerate(ranges):
            if a <= p['yy'] < b:
                assigned[k].append(p)
                break
    # curved or warped pages: fit each line its own slope and give every piece to the nearest fitted line
    xmid = float(np.median([p['cx'] for p in allp]))
    pitch = float(np.median(np.diff(centers))) if len(centers) > 1 else 160.0
    for _ in range(2):
        fits = []
        for k, mem in enumerate(assigned):
            pts = [(q['cx'], q['cy'], q['area']) for q in mem if q['area'] >= 300]
            b0, a0 = slope, centers[k] + slope * xmid
            if len(pts) >= 6:
                xs_, ys_, ws_ = (np.array(v, float) for v in zip(*pts))
                if np.ptp(xs_) > 400:
                    b1, a1 = np.polyfit(xs_, ys_, 1, w=np.sqrt(ws_))
                    if abs(b1 - slope) < 0.07:
                        b0, a0 = b1, a1
                    else:
                        b0, a0 = slope, float(np.average(ys_ - slope * xs_, weights=ws_))
            fits.append((b0, a0))
        assigned = [[] for _ in groups]
        for q in allp:
            ds = [abs(q['cy'] - (a_ + b_ * q['cx'])) for b_, a_ in fits]
            k = int(np.argmin(ds))
            if ds[k] <= 0.55 * pitch:
                assigned[k].append(q)
    for gi, g in enumerate(groups):
        mem = assigned[gi]
        items = [p for p in mem if p['area'] >= P['body_area']]
        smalls = [p for p in mem if p['area'] < P['body_area']]
        if len(items) < 1:
            continue
        f = line_features(items, mem, lab)
        x0 = min(p['x'] for p in mem); x1 = max(p['x'] + p['w'] for p in mem)
        y0 = min(p['y'] for p in mem); y1 = max(p['y'] + p['h'] for p in mem)
        f['n_red'] = sum(1 for q in redp if y0 - 100 <= q['cy'] <= y0 + 0.5 * (y1 - y0) and x0 - 20 <= q['cx'] <= x1 + 20)
        kind = classify(f)
        lines.append(dict(y0=y0, y1=y1, x0=x0, x1=x1, kind=kind, features=f, _items=items, _smalls=smalls,
                          _gc=centers[gi]))
    lines.sort(key=lambda L: L['_gc'])
    # context: an isolated 'arabic' verdict between cipher lines of a block is a short cipher line, and a
    # one-piece cipher verdict next to Arabic lines is Arabic.  (Only applied to lines with few pieces.)
    for i, L in enumerate(lines):
        L['index'] = i + 1
    # median sign width over cipher lines of the page
    cw = [p['w'] for L in lines if L['kind'] == 'cipher' for p in L['_items']
          if not is_stem(p, lab, L['features']['unit'])]
    medw = float(np.median(cw)) if cw else 50.0
    rights = [max(p['x'] + p['w'] for p in L['_items']) for L in lines if L['kind'] == 'cipher' and len(L['_items']) >= 8]
    right_edge = float(np.median(rights)) + P['margin_gap'] * medw if rights else 1e9
    for L in lines:
        if L['kind'] != 'cipher':
            continue
        L['items'] = segment_cipher_line(L['_items'], L['_smalls'], lab, medw, L['features']['unit'], right_edge)
        if L['items']:
            bs = [it['box'] for it in L['items']]
            L['x0'] = min(b[0] for b in bs); L['x1'] = max(b[2] for b in bs)
            L['y0'] = min(b[1] for b in bs); L['y1'] = max(b[3] for b in bs)
    unatt = attach_red(lines, redp)
    for L in lines:
        L.pop('_items'); L.pop('_smalls'); L.pop('_gc')
    _cache.clear()
    _cache[n] = (rgb.shape, lines, slope, pitch, unatt)
    return _cache[n]


def segment_page(n):
    """Lines of image n, top to bottom. See module docstring."""
    return analyse_page(n)[1]


# ---- overlay and export ----------------------------------------------------------------------------------------
def overlay(n, path=None):
    rgb = load_rgb(n)
    lines = segment_page(n)
    im = rgb.copy()
    for L in lines:
        col = (0, 160, 0) if L['kind'] == 'cipher' else (0, 90, 255)
        cv2.rectangle(im, (L['x0'], L['y0']), (L['x1'], L['y1']), col, 3)
        cv2.putText(im, '%d%s' % (L['index'], 'c' if L['kind'] == 'cipher' else 'a'), (max(L['x0'] - 70, 5), L['y0'] + 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.6, col, 4)
        for k, it in enumerate(L.get('items', [])):
            b = it['box']
            c = (255, 0, 0) if it['kind'] == 'divider' else ((255, 0, 255) if it.get('merged') else (0, 0, 255))
            cv2.rectangle(im, (b[0], b[1]), (b[2], b[3]), c, 2)
            cv2.putText(im, str(k + 1), (b[0], b[1] - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.7, c, 2)
        for r in L.get('red_letters', []):
            b = r['box']
            cv2.rectangle(im, (b[0], b[1]), (b[2], b[3]), (255, 140, 0), 2)
    path = path or os.path.join(CROPS, 's_%04d_overlay.png' % n)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    cv2.imwrite(path, cv2.cvtColor(im, cv2.COLOR_RGB2BGR))
    return path


def norm_crop(g, b, size=64, pad=6):
    """Sign box -> size x size PNG: dark ink on white, aspect kept, centred."""
    x0, y0, x1, y1 = b
    x0 = max(0, x0 - pad); y0 = max(0, y0 - pad); x1 = min(g.shape[1], x1 + pad); y1 = min(g.shape[0], y1 + pad)
    c = g[y0:y1, x0:x1].astype(np.float32)
    lo, hi = np.percentile(c, 1), np.percentile(c, 90)
    c = np.clip((c - lo) / max(hi - lo, 1), 0, 1) * 255
    h, w = c.shape
    s = (size - 4) / max(h, w)
    c = cv2.resize(c, (max(1, int(round(w * s))), max(1, int(round(h * s)))), interpolation=cv2.INTER_AREA)
    out = np.full((size, size), 255, np.uint8)
    yy = (size - c.shape[0]) // 2; xx = (size - c.shape[1]) // 2
    out[yy:yy + c.shape[0], xx:xx + c.shape[1]] = c.astype(np.uint8)
    return out


def export_signs(n, size=64, outdir=None):
    """Write signs/<image>/<line>_<k>.png (cipher lines, right to left, k from 1; dividers as <line>_<k>d.png)
    and index.json. Returns the index."""
    lines = segment_page(n)
    rgb = load_rgb(n)
    g = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    outdir = outdir or os.path.join(SIGNS, '%04d' % n)
    os.makedirs(outdir, exist_ok=True)
    index = []
    for L in lines:
        if L['kind'] != 'cipher':
            continue
        k = 0
        for it in L['items']:
            if it['kind'] == 'divider':
                name = '%02d_%dd.png' % (L['index'], k)
            else:
                k += 1
                name = '%02d_%d.png' % (L['index'], k)
            cv2.imwrite(os.path.join(outdir, name), norm_crop(g, it['box'], size))
            index.append(dict(file=name, image=n, line=L['index'], pos=k, kind=it['kind'], box=it['box'],
                              red=it.get('red', []), merged=bool(it.get('merged'))))
    with open(os.path.join(outdir, 'index.json'), 'w', encoding='utf8') as f:
        json.dump(index, f)
    page = []
    for L in lines:
        d = {k: L[k] for k in ('index', 'kind', 'y0', 'y1', 'x0', 'x1')}
        d['n_signs'] = sum(1 for it in L.get('items', []) if it['kind'] == 'sign')
        d['n_dividers'] = sum(1 for it in L.get('items', []) if it['kind'] == 'divider')
        if L['kind'] == 'cipher':
            d['items'] = L['items']
            d['red_letters'] = L['red_letters']
        page.append(d)
    with open(os.path.join(outdir, 'lines.json'), 'w', encoding='utf8') as f:
        json.dump(dict(image=n, slope=analyse_page(n)[2], lines=page), f, default=int)
    return index


def summary(n):
    lines = segment_page(n)
    rows = []
    for L in lines:
        ns = sum(1 for it in L.get('items', []) if it['kind'] == 'sign')
        nd = sum(1 for it in L.get('items', []) if it['kind'] == 'divider')
        rows.append((L['index'], L['kind'], L['y0'], L['y1'], ns, nd, len(L.get('red_letters', []))))
    return rows


def parse_pages(args):
    out = []
    for a in args:
        if a == '--all':
            out += sorted(int(f[5:9]) for f in os.listdir(MASTER) if f.startswith('0084_') and f.endswith('.tif'))
        elif '-' in a:
            lo, hi = a.split('-')
            out += list(range(int(lo), int(hi) + 1))
        else:
            out.append(int(a))
    return out


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if a == '--all' or not a.startswith('--')]
    ov = '--overlay' in sys.argv
    for n in parse_pages(args):
        try:
            export_signs(n)
        except Exception as e:                      # a truncated or missing download must not stop a batch
            print('image', n, 'FAILED:', e)
            continue
        print('image', n)
        for r in summary(n):
            print('  line %2d %-6s y %4d-%4d  signs %3d  dividers %2d  red %2d' % r)
        if ov:
            print('  overlay', overlay(n))
