"""rekey.py - rebuild the key of one LJS 51 cipher chain from its plaintext.

    python rekey.py A            # run one pilot chain (A, B, C, D, see CHAINS)
    python rekey.py A --shuffles 20 --kmax 30

Steps (see pilot_report.md for the measures):
 1. chain -> ordered right-to-left sign sequence with dividers (signs from segment.py's index.json)
 2. shape clusters of the 64x64 sign crops (HOG + blurred pixels + box size, PCA, Ward); k chosen by the fit
    against shuffled plaintext (z score of purity), silhouette reported alongside
 3. sign-to-letter alignment: global DP, hard-EM (key learned from its own alignment); moves: match,
    surplus sign, dropped letter, lam+alif folded into one sign; dividers are soft word boundaries;
    `sign_per_letter=2` lets one letter take two consecutive signs (numeral-like blocks)
 4. key table class -> letters, fit report, control (100 shuffles, same procedure), leave-one-line-out check

A key learned from its own alignment is self-consistent evidence only. The shuffle control and the held-out
lines are what say whether the consistency is more than the freedom of the procedure.
"""
import os, sys, json, re, math, random, argparse
import numpy as np
from PIL import Image, ImageDraw
from scipy.cluster.hierarchy import linkage, fcluster
from skimage.feature import hog
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SIGNS = os.path.join(ROOT, 'output', 'ljs51', 'signs')
KEYS_OUT = os.path.join(ROOT, 'output', 'ljs51', 'keys')
HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- plaintext
LETTERS = list('ابتثجحخدذرزسشصضطظعغفقكلمنهويء')
_MAP = {'أ': 'ا', 'إ': 'ا', 'ٱ': 'ا', 'ة': 'ه', 'ى': 'ي', 'ؤ': 'و', 'ئ': 'ي', 'ک': 'ك', 'ی': 'ي', 'ی': 'ي'}
RASM = ['ا', 'بتثني', 'جحخ', 'دذ', 'رز', 'سش', 'صض', 'طظ', 'عغ', 'فق', 'ك', 'ل', 'م', 'ه', 'و', 'ء']
RASM_OF = {c: i for i, g in enumerate(RASM) for c in g}


def norm_plain(text):
    """-> (letters list, space_after list). Marks like [?] and diacritics are removed; hamza kept as a letter."""
    text = re.sub(r'\[[^\]]*\]', '', text)
    letters, sp = [], []
    for ch in text:
        if ch in ' \n/|':
            if sp:
                sp[-1] = True
            continue
        ch = {'آ': 'اء'}.get(ch, ch)
        for c in ch:
            c = _MAP.get(c, c)
            if c in LETTERS:
                letters.append(c)
                sp.append(False)
    return letters, sp


# ---------------------------------------------------------------- chain -> sign sequence
def load_chain(spec):
    """spec = list of (image, first_line, last_line). Returns list of items (sign or divider), reading order."""
    items = []
    for img, l0, l1 in spec:
        d = json.load(open(os.path.join(SIGNS, '%04d' % img, 'index.json')))
        for r in d:
            if l0 <= r['line'] <= l1:
                items.append(r)
    items.sort(key=lambda r: (r['image'], r['line'], r['pos'], 0 if r['kind'] == 'sign' else 1))
    signs, div_after = [], []
    for r in items:
        if r['kind'] == 'sign':
            signs.append(r)
            div_after.append(False)
        elif signs:
            div_after[-1] = True
    for r, da in zip(signs, div_after):
        r['div_after'] = da
    for i, r in enumerate(signs):
        r['idx'] = i
    return signs


def get_crop(r):
    if 'crop' in r:
        return r['crop']
    return np.array(Image.open(os.path.join(SIGNS, '%04d' % r['image'], r['file'])).convert('L'), float)


_MASTER = {}


def master(img):
    if img not in _MASTER:
        Image.MAX_IMAGE_PIXELS = None
        _MASTER[img] = np.array(Image.open(os.path.join(ROOT, 'output', 'ljs51', 'master', '0084_%04d.tif' % img)).convert('RGB')).astype(int)
    return _MASTER[img]


def red_sequence(signs):
    """Every red letter over the chain's signs as its own pseudo-sign (64x64 crop of the red ink), reading order:
    sign order, and right to left inside a sign. div_after is carried over from the sign (last red of it)."""
    seq = []
    for r in signs:
        reds = sorted(r.get('red', []), key=lambda b: -b[0])
        arr = master(r['image'])
        for k, b in enumerate(reds):
            x0, y0, x1, y1 = b
            if max(x1 - x0, y1 - y0) < 16:   # a dot or a speck, not a letter
                continue
            x0, y0, x1, y1 = x0 - 3, y0 - 3, x1 + 3, y1 + 3
            sub = arr[y0:y1, x0:x1]
            m = (sub[..., 0] - (sub[..., 1] + sub[..., 2]) / 2) > 45
            ys, xs = np.where(m)
            if len(xs) < 4:
                continue
            m = m[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
            h, w = m.shape
            sc = 56.0 / max(h, w)
            im = Image.fromarray(((~m) * 255).astype(np.uint8)).resize((max(1, int(w * sc)), max(1, int(h * sc))), Image.BILINEAR)
            can = Image.new('L', (64, 64), 255)
            can.paste(im, ((64 - im.width) // 2, (64 - im.height) // 2))
            seq.append(dict(image=r['image'], line=r['line'], pos=r['pos'], kind='red', box=[x0, y0, x1, y1], crop=np.array(can, float),
                            div_after=bool(r['div_after']) and k == len(reds) - 1, sign_idx=r['idx'], file='red'))
    for i, r in enumerate(seq):
        r['idx'] = i
    return seq


def sign_features(signs):
    feats, sizes = [], []
    for r in signs:
        im = get_crop(r)
        ink = 1 - im / 255.0
        h = hog(ink, orientations=8, pixels_per_cell=(8, 8), cells_per_block=(2, 2), feature_vector=True)
        small = np.array(Image.fromarray((ink * 255).astype(np.uint8)).resize((16, 16), Image.BILINEAR), float) / 255
        feats.append(np.concatenate([h * 1.0, small.ravel() * 1.5]))
        b = r['box']
        sizes.append([b[2] - b[0], b[3] - b[1]])
    sizes = np.array(sizes, float)
    medh = np.median(sizes[:, 1])
    sz = np.stack([np.log(sizes[:, 0] / medh), np.log(sizes[:, 1] / medh)], 1) * 3.0
    X = np.hstack([np.array(feats), sz])
    X = X - X.mean(0)
    n = min(30, X.shape[0] - 1, X.shape[1])
    return PCA(n_components=n, random_state=0).fit_transform(X)


def cluster_tree(F):
    return linkage(F, 'ward')


def cut(Z, k):
    return fcluster(Z, k, criterion='maxclust') - 1


# ---------------------------------------------------------------- DP alignment
class Params:
    gs = -2.2          # surplus sign
    gl = -2.6          # dropped letter
    gl_hamza = -0.4
    la = -1.2          # lam+alif folded into one sign (extra cost)
    div = {(1, 1): 1.2, (1, 0): -1.6, (0, 1): -0.4, (0, 0): 0.05}
    inner_div = -1.2   # a divider inside a multi-sign unit
    alpha = 0.4        # key smoothing


def build_units(signs, cls, s):
    n = len(signs)
    units = [None] * n  # unit ending at sign i (needs s signs)
    for i in range(s - 1, n):
        units[i] = tuple(cls[i - s + 1:i + 1])
    return units


def key_from_pairs(pairs, ncls, s, bg):
    """pairs: list of (unit tuple, letter index). counts[p][c, l]."""
    cnt = np.zeros((s, ncls, len(LETTERS)))
    for u, l in pairs:
        for p, c in enumerate(u):
            cnt[p, c, l] += 1
    return cnt


def key_scores(cnt, bg, alpha):
    s, ncls, L = cnt.shape
    tot = cnt.sum(2, keepdims=True)
    P = (cnt + alpha * bg[None, None, :] * L * 0.25) / (tot + alpha * L * 0.25)
    return np.log(P / bg[None, None, :])


def align(cls, div_after, letters, sp, KS, s, P, prior_w=0.0, sigma=None):
    """Global DP. cls: class id per sign; KS: [s, ncls, L] log score. Returns list of moves and total score.
    Moves: ('m', i_end, j) unit of s signs ending at sign i matched to letter j; ('s', i); ('d', j); ('la', i, j)."""
    n, m = len(cls), len(letters)
    lidx = np.array([LETTERS.index(c) for c in letters])
    cls = np.asarray(cls)
    # unit score matrix M[i,j] for unit ending at sign i (0-based), letter j (0-based)
    M = np.full((n, m), -1e9)
    for i in range(s - 1, n):
        sc = np.zeros(m)
        for p in range(s):
            sc += KS[p, cls[i - s + 1 + p]][lidx]
        da = 1 if div_after[i] else 0
        spj = np.array([1 if x else 0 for x in sp])
        dterm = np.where(spj == 1, P.div[(da, 1)], P.div[(da, 0)])
        inner = sum(1 for q in range(i - s + 1, i) if div_after[q]) * P.inner_div
        M[i, :] = sc + dterm + inner
    if prior_w > 0:
        jj = np.arange(m)[None, :] + 0.5
        pos_i = (np.arange(n)[:, None] + 1) / n * m
        sg = sigma or max(3.0, 0.03 * m)
        M = M - prior_w * 0.5 * ((pos_i - jj - 0.5) / sg) ** 2
    gl = np.array([P.gl_hamza if c == 'ء' else P.gl for c in letters])
    cumgl = np.concatenate([[0.0], np.cumsum(gl)])  # cumgl[j] = cost of dropping first j letters
    NEG = -1e12
    D = np.full((n + 1, m + 1), NEG)
    E = np.full((n + 1, m + 1), NEG)
    D[0, :] = cumgl
    E[0, :] = NEG
    E[0, 0] = 0.0
    is_la = np.array([False] + [letters[j - 1] == 'ل' and letters[j] == 'ا' for j in range(1, m)])  # for pair ending j (0-based)
    for i in range(1, n + 1):
        e = np.full(m + 1, NEG)
        # surplus sign
        e = D[i - 1] + P.gs
        # match: unit of s signs ending at sign i-1 uses D[i-s, j-1]
        if i - s >= 0 and i >= s:
            cand = D[i - s, :-1] + M[i - 1, :]
            e[1:] = np.maximum(e[1:], cand)
        # lam-alif: one sign (unit s must be 1) for letters j-1, j
        if s == 1:
            la_sc = D[i - 1, :-2] + KS[0, cls[i - 1]][lidx[:-1]] + P.la
            ok = is_la[1:]
            cand = np.where(ok, la_sc, NEG)
            e[2:] = np.maximum(e[2:], cand)
        E[i] = e
        D[i] = cumgl + np.maximum.accumulate(e - cumgl)
    # backtrace
    moves = []
    i, j = n, m
    tol = 1e-7
    while i > 0 or j > 0:
        if i == 0:
            moves.append(('d', j - 1)); j -= 1; continue
        if abs(D[i, j] - E[i, j]) < tol or j == 0:
            # came via E
            v = E[i, j]
            if abs(v - (D[i - 1, j] + P.gs)) < tol:
                moves.append(('s', i - 1)); i -= 1; continue
            if j >= 1 and i >= s and abs(v - (D[i - s, j - 1] + M[i - 1, j - 1])) < tol:
                moves.append(('m', i - 1, j - 1)); i -= s; j -= 1; continue
            if s == 1 and j >= 2 and is_la[j - 1] and abs(v - (D[i - 1, j - 2] + KS[0, cls[i - 1]][lidx[j - 2]] + P.la)) < tol:
                moves.append(('la', i - 1, j - 1)); i -= 1; j -= 2; continue
            moves.append(('s', i - 1)); i -= 1; continue
        else:
            moves.append(('d', j - 1)); j -= 1
    moves.reverse()
    return moves, D[n, m]


def moves_to_pairs(moves, cls, letters, s):
    pairs = []
    for mv in moves:
        if mv[0] == 'm':
            i, j = mv[1], mv[2]
            pairs.append((tuple(cls[i - s + 1:i + 1]), LETTERS.index(letters[j]), i, j))
        elif mv[0] == 'la':
            i, j = mv[1], mv[2]
            pairs.append(((cls[i],), LETTERS.index('ل'), i, j - 1))
    return pairs


def em(cls, div_after, letters, sp, ncls, s=1, P=None, iters=10, bg=None):
    P = P or Params
    cls = list(cls)
    if bg is None:
        bg = np.array([max(letters.count(c), 0.5) for c in LETTERS], float)
        bg /= bg.sum()
    cnt = np.zeros((s, ncls, len(LETTERS)))
    KS = key_scores(cnt, bg, P.alpha)
    prev = None
    moves = None
    for t in range(iters):
        pw = 1.0 if t < 3 else 0.0
        if t >= 3 and prev is not None:
            pw = 0.0
        moves, score = align(cls, div_after, letters, sp, KS, s, P, prior_w=pw, sigma=max(3.0, 0.04 * len(letters)) * (3 - t if t < 3 else 1))
        pairs = moves_to_pairs(moves, cls, letters, s)
        cnt = key_from_pairs([(u, l) for u, l, _, _ in pairs], ncls, s, bg)
        KS = key_scores(cnt, bg, P.alpha)
        if prev is not None and moves == prev and t >= 3:
            break
        prev = moves
    return dict(moves=moves, pairs=pairs, cnt=cnt, KS=KS, bg=bg, score=score)


# ---------------------------------------------------------------- measures
def measures(res, n_signs, n_letters, ncls, s=1):
    pairs = res['pairs']
    N = len(pairs)
    if N == 0:
        return dict(aligned_share=0, letter_fit=0, class_purity=0, rasm_purity=0, surplus=n_signs, dropped=n_letters, n_pairs=0)
    cnt1 = res['cnt']  # [s, ncls, L]
    # class-side purity uses the full unit tuples
    from collections import Counter
    cl = {}
    cl_r = {}
    ltr = {}
    for u, l, i, j in pairs:
        cl.setdefault(u, Counter())[l] += 1
        cl_r.setdefault(u, Counter())[RASM_OF[LETTERS[l]]] += 1
        ltr.setdefault(l, Counter())[u] += 1
    purity = sum(max(c.values()) for c in cl.values()) / N
    rpurity = sum(max(c.values()) for c in cl_r.values()) / N
    lfit = sum(max(c.values()) for c in ltr.values()) / N
    surplus = sum(1 for mv in res['moves'] if mv[0] == 's')
    dropped = sum(1 for mv in res['moves'] if mv[0] == 'd')
    folds = sum(1 for mv in res['moves'] if mv[0] == 'la')
    matched_signs = sum(s for mv in res['moves'] if mv[0] == 'm') + folds
    return dict(aligned_share=matched_signs / n_signs, letter_fit=lfit, letter_fit_of_letters=sum(max(c.values()) for c in ltr.values()) / n_letters,
                class_purity=purity, rasm_purity=rpurity, surplus=surplus, dropped=dropped, lamalif_folds=folds, n_pairs=N)


def shuffled(letters, sp, rng):
    """Shuffle the letter sequence, keep the word-length layout."""
    idx = list(range(len(letters)))
    rng.shuffle(idx)
    return [letters[i] for i in idx], sp


def control(cls, div_after, letters, sp, ncls, s, nshuf, seed=1, P=None):
    rng = random.Random(seed)
    out = []
    bg = None
    for _ in range(nshuf):
        l2, sp2 = shuffled(letters, sp, rng)
        r = em(cls, div_after, l2, sp2, ncls, s, P)
        out.append(measures(r, len(cls), len(l2), ncls, s))
    return out


def summarise_control(ctrl, keys=('aligned_share', 'letter_fit', 'class_purity', 'rasm_purity', 'surplus', 'dropped')):
    return {k: (float(np.mean([c[k] for c in ctrl])), float(np.std([c[k] for c in ctrl])), float(np.max([c[k] for c in ctrl]))) for k in keys}


# ---------------------------------------------------------------- leave one line out
def leave_one_line_out(signs, cls, letters, sp, ncls, s, res, P=None):
    P = P or Params
    pairs = res['pairs']
    bg = res['bg']
    line_of = [(r['image'], r['line']) for r in signs]
    lines = sorted(set(line_of), key=lambda x: (x[0], x[1]))
    tot_ok = tot_ok_set = tot_n = 0
    tot_lett = 0
    per = []
    # letter span per line from the full alignment
    for ln in lines:
        sidx = [i for i, l in enumerate(line_of) if l == ln]
        pr_in = [(u, l, i, j) for u, l, i, j in pairs if line_of[i] == ln]
        if not pr_in:
            continue
        pr_out = [(u, l) for u, l, i, j in pairs if line_of[i] != ln]
        j0 = min(j for _, _, _, j in pr_in)
        j1 = max(j for _, _, _, j in pr_in)
        cnt = key_from_pairs(pr_out, ncls, s, bg)
        KS = key_scores(cnt, bg, P.alpha)
        # letter -> modal unit from the other lines
        from collections import Counter
        lt = {}
        for u, l in pr_out:
            lt.setdefault(l, Counter())[u] += 1
        i0, i1 = min(sidx), max(sidx)
        sub_cls = [cls[i] for i in range(i0, i1 + 1)]
        sub_div = [signs[i]['div_after'] for i in range(i0, i1 + 1)]
        sub_let = letters[j0:j1 + 1]
        sub_sp = sp[j0:j1 + 1]
        mv, _ = align(sub_cls, sub_div, sub_let, sub_sp, KS, s, P)
        pp = moves_to_pairs(mv, sub_cls, sub_let, s)
        ok = ok_set = 0
        for u, l, i, j in pp:
            c = lt.get(l)
            if c:
                if c.most_common(1)[0][0] == u:
                    ok += 1
                tot_set = {x for x, v in c.items() if v >= 0.2 * sum(c.values())}
                if u in tot_set:
                    ok_set += 1
        # decode the held-out letters from the signs: sign unit -> most likely letter, compared with the aligned letter
        per.append(dict(line=list(ln), signs=len(sidx), letters_in_span=len(sub_let), aligned=len(pp), consistent=ok, consistent_set=ok_set))
        tot_ok += ok
        tot_ok_set += ok_set
        tot_n += len(sidx)
        tot_lett += len(sub_let)
    return dict(per_line=per, heldout_share=tot_ok / max(tot_lett, 1), heldout_share_set=tot_ok_set / max(tot_lett, 1), signs=tot_n, letters=tot_lett)


def heldout_decode(signs, cls, letters, sp, ncls, s, res, P=None):
    """Held-out line decoded top-1: for each held-out unit, the key from the other lines names a letter (argmax P(l|c));
    scored against the letter the full alignment has there (rasm group too)."""
    P = P or Params
    pairs = res['pairs']
    bg = res['bg']
    line_of = [(r['image'], r['line']) for r in signs]
    ok = okr = n = 0
    for ln in sorted(set(line_of)):
        pr_in = [(u, l) for u, l, i, j in pairs if line_of[i] == ln]
        pr_out = [(u, l) for u, l, i, j in pairs if line_of[i] != ln]
        cnt = key_from_pairs(pr_out, ncls, s, bg)
        KS = key_scores(cnt, bg, P.alpha)
        for u, l in pr_in:
            sc = sum(KS[p, c] for p, c in enumerate(u))
            if all(cnt[p, c].sum() == 0 for p, c in enumerate(u)):
                n += 1
                continue
            g = int(np.argmax(sc))
            n += 1
            ok += (g == l)
            okr += (RASM_OF[LETTERS[g]] == RASM_OF[LETTERS[l]])
    return dict(top1_letter=ok / max(n, 1), top1_rasm=okr / max(n, 1), n=n)


# ---------------------------------------------------------------- outputs
TRANS = dict(zip(LETTERS, ['a', 'b', 't', 'th', 'j', 'H', 'kh', 'd', 'dh', 'r', 'z', 's', 'sh', 'S', 'D', 'T', 'Z', 'c', 'gh', 'f', 'q', 'k', 'l', 'm', 'n', 'h', 'w', 'y', "'"]))


def cluster_sheets(signs, cls, ncls, letter_of_sign, outdir):
    os.makedirs(outdir, exist_ok=True)
    for f in os.listdir(outdir):
        if f.startswith('cluster_') or f == 'key_sheet.png':
            os.remove(os.path.join(outdir, f))
    cell = 72
    rows = []
    for c in range(ncls):
        mem = [i for i in range(len(signs)) if cls[i] == c]
        if not mem:
            continue
        cols = min(len(mem), 14)
        nr = (len(mem) + cols - 1) // cols
        sheet = Image.new('L', (cols * cell, nr * (cell + 12)), 255)
        dr = ImageDraw.Draw(sheet)
        for k, i in enumerate(mem):
            im = Image.fromarray(get_crop(signs[i]).astype(np.uint8))
            x, y = (k % cols) * cell, (k // cols) * (cell + 12)
            sheet.paste(im, (x + 4, y))
            lab = letter_of_sign.get(i)
            dr.text((x + 6, y + 64), (TRANS[lab] if lab else '-') + ' #%d' % i, fill=0)
        sheet.save(os.path.join(outdir, 'cluster_%02d.png' % c))
        rows.append((c, mem[:12]))
    # overview: one row per cluster, first 12 members
    ov = Image.new('L', (12 * 66 + 50, len(rows) * 68), 255)
    dr = ImageDraw.Draw(ov)
    for r, (c, mem) in enumerate(rows):
        dr.text((4, r * 68 + 26), 'c%d' % c, fill=0)
        for k, i in enumerate(mem):
            im = Image.fromarray(get_crop(signs[i]).astype(np.uint8))
            ov.paste(im, (50 + k * 66, r * 68))
    ov.save(os.path.join(outdir, 'key_sheet.png'))


def key_table(res, cls, ncls, signs):
    from collections import Counter
    tab = {}
    for u, l, i, j in res['pairs']:
        tab.setdefault('-'.join(map(str, u)), Counter())[LETTERS[l]] += 1
    return {k: dict(v.most_common()) for k, v in sorted(tab.items(), key=lambda kv: -sum(kv[1].values()))}


def run_chain(name, spec, plaintext, s=1, kgrid=None, nshuf=100, nsel=8, outdir=None, kfixed=None, log=print, extra=None, signs=None, window=None):
    signs = signs if signs is not None else load_chain(spec)
    letters, sp = norm_plain(plaintext)
    n, m = len(signs), len(letters)
    log('%s: %d signs, %d letters' % (name, n, m))
    F = sign_features(signs)
    Z = cluster_tree(F)
    all_signs, all_n = signs, n
    if window:   # cluster on the whole chain, align only a stretch of it (plaintext shorter than the block)
        a, b = window
        signs = signs[a:b]
        n = len(signs)
        log('  window signs %d-%d of %d' % (a, b, all_n))
        F = F[a:b]
    else:
        a, b = 0, n
    div_after = [r['div_after'] for r in signs]
    kgrid = kgrid or [10, 14, 18, 22, 26, 30, 36]
    kgrid = [k for k in kgrid if k < all_n // 2]
    sel = []
    for k in kgrid:
        cls = list(cut(Z, k)[a:b])
        kk = int(max(cut(Z, k))) + 1
        try:
            sil = float(silhouette_score(F, cls)) if len(set(cls)) > 1 else float('nan')
        except Exception:
            sil = float('nan')
        res = em(cls, div_after, letters, sp, kk, s)
        ms = measures(res, n, m, kk, s)
        ctrl = control(cls, div_after, letters, sp, kk, s, nsel, seed=7)
        z = {}
        for key in ('class_purity', 'rasm_purity', 'letter_fit'):
            arr = np.array([c[key] for c in ctrl])
            z[key] = (ms[key] - arr.mean()) / (arr.std() + 0.01)
        sel.append(dict(k=k, k_actual=kk, silhouette=sil, **{kx: ms[kx] for kx in ('aligned_share', 'letter_fit', 'class_purity', 'rasm_purity')}, z_letter_fit=z['letter_fit'], z_rasm=z['rasm_purity'], z_purity=z['class_purity']))
        log('  k=%d sil=%.3f aligned=%.2f fit=%.2f purity=%.2f rasm=%.2f | z fit %.1f rasm %.1f purity %.1f' % (kk, sil, ms['aligned_share'], ms['letter_fit'], ms['class_purity'], ms['rasm_purity'], z['letter_fit'], z['rasm_purity'], z['class_purity']))
    if kfixed:
        kbest = kfixed
    else:
        # the fit itself picks k: highest mean z of letter-side fit and rasm purity (ties to the smaller k)
        kbest = max(sel, key=lambda r: (r['z_letter_fit'] + r['z_rasm'], -r['k']))['k']
    cls = list(cut(Z, kbest)[a:b])
    ncls = int(max(cut(Z, kbest))) + 1
    res = em(cls, div_after, letters, sp, ncls, s)
    ms = measures(res, n, m, ncls, s)
    ctrl = control(cls, div_after, letters, sp, ncls, s, nshuf, seed=11)
    cs = summarise_control(ctrl)
    ho = leave_one_line_out(signs, cls, letters, sp, ncls, s, res)
    hd = heldout_decode(signs, cls, letters, sp, ncls, s, res)
    # the same held-out decode on shuffled plaintext (key learned from the shuffled alignment): what the procedure reaches by itself
    rng = random.Random(23)
    hc = []
    for _ in range(min(nshuf, 30)):
        l2, sp2 = shuffled(letters, sp, rng)
        r2 = em(cls, div_after, l2, sp2, ncls, s)
        hc.append(heldout_decode(signs, cls, l2, sp2, ncls, s, r2))
    hd['control_top1_letter'] = [float(np.mean([h['top1_letter'] for h in hc])), float(np.max([h['top1_letter'] for h in hc]))]
    hd['control_top1_rasm'] = [float(np.mean([h['top1_rasm'] for h in hc])), float(np.max([h['top1_rasm'] for h in hc]))]
    letter_of_sign = {}
    for u, l, i, j in res['pairs']:
        letter_of_sign[i] = LETTERS[l]
    outdir = outdir or os.path.join(KEYS_OUT, name)
    cluster_sheets(signs, cls, ncls, letter_of_sign, outdir)
    out = dict(chain=name, spec=spec, signs=n, letters=m, sign_per_letter=s, k_chosen=kbest, k_classes=ncls, selection=sel,
               measures=ms, control=cs, heldout=ho, heldout_decode=hd,
               key=key_table(res, cls, ncls, signs), cluster_sheet=outdir,
               alignment=[dict(sign=i, line=[signs[i]['image'], signs[i]['line']], cls=int(cls[i]), letter=LETTERS[l], j=j) for u, l, i, j in res['pairs']],
               plaintext=''.join(letters))
    if extra:
        out['extra'] = extra(signs, cls, res, letters)
    return out, signs, cls, res, letters, sp



# ---------------------------------------------------------------- tree figure (f. 63v): trees anchored on their red letters
def tree_sequence(img, rows, win_w=100, win_h=215):
    """rows = line indexes of the tree rows. One item per red letter (a tree sits under each): a 64x64 crop of the black ink in a
    window under the red letter (constant scale, so height and number of branch pairs stay visible), and the red letter's own crop.
    Returns (trees, reds) in reading order (rows top to bottom, right to left)."""
    d = json.load(open(os.path.join(SIGNS, '%04d' % img, 'lines.json')))
    arr = master(img)
    g = arr.mean(2)
    import cv2
    paper = cv2.GaussianBlur(g.astype(np.float32), (0, 0), 25)
    redm = (arr[..., 0] - (arr[..., 1] + arr[..., 2]) / 2) > 45
    ink = ((paper - g) > 45) & (~redm)
    trees, reds = [], []
    for l in d['lines']:
        if l['index'] not in rows:
            continue
        rl = [r['box'] for r in l['red_letters'] if max(r['box'][2] - r['box'][0], r['box'][3] - r['box'][1]) >= 16]
        rl.sort(key=lambda b: -(b[0] + b[2]))
        for b in rl:
            cx = (b[0] + b[2]) // 2
            y0 = b[3] + 4
            x0, x1, y1 = cx - win_w // 2, cx + win_w // 2, y0 + win_h
            sub = ink[y0:y1, x0:x1]
            sc = 64.0 / win_h
            im = Image.fromarray(((~sub) * 255).astype(np.uint8))
            im = im.resize((max(1, int(sub.shape[1] * sc)), max(1, int(sub.shape[0] * sc))), Image.BILINEAR)
            can = Image.new('L', (64, 64), 255)
            can.paste(im, ((64 - im.width) // 2, 0))
            trees.append(dict(image=img, line=l['index'], pos=len(trees) + 1, kind='tree', box=[x0, y0, x1, y1], crop=np.array(can, float), div_after=False, file='tree', red=[b]))
            x0r, y0r, x1r, y1r = b[0] - 3, b[1] - 3, b[2] + 3, b[3] + 3
            subr = arr[y0r:y1r, x0r:x1r]
            m = (subr[..., 0] - (subr[..., 1] + subr[..., 2]) / 2) > 45
            ys, xs = np.where(m)
            if len(xs) >= 4:
                m = m[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
                h, w = m.shape
                s2 = 56.0 / max(h, w)
                im2 = Image.fromarray(((~m) * 255).astype(np.uint8)).resize((max(1, int(w * s2)), max(1, int(h * s2))), Image.BILINEAR)
                can2 = Image.new('L', (64, 64), 255)
                can2.paste(im2, ((64 - im2.width) // 2, (64 - im2.height) // 2))
            else:
                can2 = Image.new('L', (64, 64), 255)
            reds.append(dict(image=img, line=l['index'], pos=len(reds) + 1, kind='red', box=[x0r, y0r, x1r, y1r], crop=np.array(can2, float), div_after=False, file='red'))
    for seq in (trees, reds):
        for i, r in enumerate(seq):
            r['idx'] = i
    return trees, reds


# ---------------------------------------------------------------- pilot chains
PT = {}
PT['A'] = 'ابري كبير والصغير يقول لي اطعن حشاي به وكن صنديدا ناديت هذا الاحول فقال لي عندي بحور وثلثه تقليدا'
PT['A2'] = PT['A3'] = PT['A']
PT['B'] = 'على وجهه ماء الجمال المرقرق يزيد اذا رددت طرفك رونقا تبدي فاخفي صبر عشاقه وكم عيون بدر مع حين اشرقا'
PT['C2'] = PT['C'] = 'لا تكن ناكحا السوداء ما عشت فشر المناكح السودا'
PT['D'] = ('سلكنا مهمه القفر الصميم وخضنا لجه الليل البهيم '
           'وجبنا بالمفاوز كل نائ وردنا في السباسب كل ميم '
           'اردنا ان نفوز بعذب ماء وردنا في الفيافي شبه هيم '
           'وردنا شرقها والغرب حتى وردنا شاطي البحر العظيم '
           'اخذنا عنك فصفا لدنيا ورق وراق باللطف العميم '
           'قصدنا ظله فضفا علينا وحولنا عن المرعى الوخيم '
           'بغير تكلف حنو ويغنيني وجبر الكسر من خيم وخيم '
           'على يا بان فضل الله حطت ركائب كل سباق عليم '
           'بحل المشكلات وكل صعب بجلى الكرب والخطب الجسيم '
           'يوشى بالبراع مدبجات تفوق قلايد الدر النظيم '
           'ويغني رايه والجاش جيشا عن الرايات للملك العقيم '
           'زكا اصلا وفرعا فهو يدعى الكريم ابن الكريم ابن الكريم '
           'الوف للفضائل والعطايا نفور عن مواحش كريم '
           'هو السم الذعاف لمن يبادي هو الحلو الفكاهه للنديم '
           'وبلغني قاصديه بطلق وجه واخلاق ارق من النسيم '
           'اذا ما هم المغتاظ ياتي ببشر شيمه البر الحليم '
           'بمنه ما فاه دهرا للمداني وصه ما قال يوما للغريم '
           'ولم يرم العدو بسهم نطق ومتكل على نجح قويم '
           'مضعف عكس ما انا فيه ونم بلا عود فاو زوج جيم '
           'ومالي غيره من بعد ربي طبيب قربه برء السقيم '
           'ادام الله رفعته ليبقى على الايام في عز مقيم')

# ---------------------------------------------------------------- chain-specific extras
GOLD_B_LINE4 = ['ع', 'ل', 'ي', 'و', 'ج', 'ه', 'ه', 'م', 'ا', 'ا', 'ل', 'ج', 'م']   # red letters read by eye on the master, f. 57v l.4


def extra_B(signs, cls, res, letters):
    """Red letters as an independent key: (a) the 13 red letters of l.4 read by eye against the DP letters of the same signs;
    (b) the automatically segmented red letters of the whole block: how many per sign."""
    dp = {i: LETTERS[l] for u, l, i, j in res['pairs']}
    agree = sum(1 for i, g in enumerate(GOLD_B_LINE4) if dp.get(i) == g)
    pl = ''.join(letters)
    first13 = pl[:13]
    reds = red_sequence(signs)
    per = {}
    for r in reds:
        per[r['sign_idx']] = per.get(r['sign_idx'], 0) + 1
    # same-red-letter -> same black class (gold line 4)
    from collections import defaultdict, Counter
    g = defaultdict(Counter)
    for i, gl in enumerate(GOLD_B_LINE4):
        g[gl][int(cls[i])] += 1
    return dict(gold_line4=''.join(GOLD_B_LINE4), plaintext_first13=first13, gold_vs_plaintext_agree=sum(1 for a, b in zip(GOLD_B_LINE4, first13) if a == b),
                dp_letters_line4=''.join(dp.get(i, '-') for i in range(13)), gold_vs_dp_agree=agree,
                gold_letter_to_black_classes={k: dict(v) for k, v in g.items()},
                red_letters_found=len(reds), signs_with_red=len(per), signs_with_two_reds=sum(1 for v in per.values() if v > 1))


EARLIER_D = {'S1': 'ا', 'S2': 'بتثني', 'S3': 'جحخ', 'S4': 'دذ', 'S5': 'رز', 'S6': 'سش', 'S7': 'صض', 'S8': 'طظ', 'S9': 'عغ', 'S10': 'فق',
             'S11': 'ك', 'S12': 'ل', 'S13': 'م', 'S14': 'ه', 'S15': 'و'}


def extra_D(signs, cls, res, letters):
    """Compare with the 15-class key of research/ljs51_pass/vet_tashifi.md class by class."""
    from collections import Counter, defaultdict
    cl_r = defaultdict(Counter)
    grp_cls = defaultdict(Counter)
    for u, l, i, j in res['pairs']:
        c = u[0]
        g = RASM_OF[LETTERS[l]]
        cl_r[c][g] += 1
        grp_cls[g][c] += 1
    table = []
    for gi, g in enumerate(RASM):
        if g == 'ء':
            continue
        cs = grp_cls[gi]
        tot = sum(cs.values())
        # clusters whose modal group is this group
        mine = [c for c in cl_r if cl_r[c].most_common(1)[0][0] == gi]
        inside = sum(cs[c] for c in mine)
        table.append(dict(earlier_class=[k for k, v in EARLIER_D.items() if v == g][0], letters=g, plaintext_letters_aligned=tot,
                          my_clusters=mine, share_in_own_clusters=round(inside / max(tot, 1), 3),
                          cluster_sizes={int(c): sum(cl_r[c].values()) for c in mine}))
    pur = {int(c): dict(cl_r[c].most_common(1) and {RASM[cl_r[c].most_common(1)[0][0]]: cl_r[c].most_common(1)[0][1], 'of': sum(cl_r[c].values())}) for c in cl_r}
    n_unique = sum(1 for t in table if t['my_clusters'])
    return dict(groups_recovered=n_unique, per_group=table, cluster_modal_group=pur,
                earlier_agent_fit=0.94, my_rasm_fit=None)


CHAINS = {
    'A': dict(name='f63v_couplet', spec=[(131, 1, 6)], s=1),
    'B': dict(name='f57v_glossed', spec=[(119, 4, 10)], s=1),
    'C': dict(name='f9r_block2_first37', spec=[(22, 6, 11)], s=1, window=(0, 37)),
    'C2': dict(name='f9r_block2_pairs', spec=[(22, 6, 11)], s=2),
    'A2': dict(name='f63v_trees', spec=[(131, 8, 12)], s=1),
    'A3': dict(name='f63v_treered', spec=[(131, 8, 12)], s=1),
    'D': dict(name='f14v_tashifi', spec=[(33, 7, 13), (34, 1, 13), (35, 1, 14), (36, 1, 13), (37, 1, 5)], s=1),
}


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('chain')   # A B C C2 D (C = first 37 signs, one sign per letter; C2 = two signs per letter)
    ap.add_argument('--shuffles', type=int, default=100)
    ap.add_argument('--sel', type=int, default=8)
    ap.add_argument('--k', type=int, default=None)
    ap.add_argument('--kgrid', type=str, default=None)
    ap.add_argument('--plain', type=str, default=None, help='override plaintext')
    a = ap.parse_args()
    c = CHAINS[a.chain]
    kg = [int(x) for x in a.kgrid.split(',')] if a.kgrid else None
    seq = None
    if a.chain in ('A2', 'A3'):   # tree figure on f. 63v: trees (A2) and the red letters over them (A3), anchored on the red letters
        trees, reds = tree_sequence(131, {8, 9, 10, 11, 12})
        seq = trees if a.chain == 'A2' else reds
        if kg is None:
            kg = [6, 8, 10, 12, 16, 20]
    out, *_ = run_chain(c['name'], c['spec'], a.plain or PT[a.chain], s=c['s'], signs=seq, kgrid=kg, nshuf=a.shuffles, nsel=a.sel, kfixed=a.k,
                        extra={'B': extra_B, 'D': extra_D}.get(a.chain), window=c.get('window'))
    os.makedirs(os.path.join(HERE, 'keys'), exist_ok=True)
    json.dump(out, open(os.path.join(HERE, 'keys', c['name'] + '.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1, default=lambda o: int(o) if isinstance(o, np.integer) else float(o))
    print(json.dumps({k: out[k] for k in ('chain', 'signs', 'letters', 'k_chosen', 'measures', 'control', 'heldout_decode')}, ensure_ascii=False, indent=1))
    print('heldout', out['heldout']['heldout_share'], out['heldout']['heldout_share_set'])
