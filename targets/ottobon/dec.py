"""Constrained decoder for the Ottobon 1589 letter (key known: Zifra Prima R1789 + overrides).

Noisy-channel model, decoded with a vectorised Viterbi beam over character-LM states:
    score = sum_i [ log P(read_i | code_i)            digit/base confusion model, estimated from the hand reading
                    + BETA * log P(code_i) ]          code prior, from the hand reading (smoothed)
            + ALPHA * log P_LM(plaintext with spaces) Venetian/Renaissance Italian 5-gram (lang model it-venezia)
            + CLEN * len(plaintext letters) + WBON * word bonus
A read token may also be 'skipped' (spurious/garbled, emits nothing) at cost SKIP.

Library + CLI:
    python -I dec.py calib            leave-one-page-out calibration against the hand reading (high/medium lines)
    python -I dec.py decode [pages]   decode pages, write dec_out/<page>.txt with per-token margins
"""
import os, sys, re, json, math, itertools, collections, glob
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
from lang import lm
PAGES = ['f35r', 'f35v', 'f36r', 'f36v', 'f37r', 'f37v', 'f38r']
PIECE = {'f35r': 1, 'f35v': 1, 'f36r': 1, 'f36v': 1, 'f37r': 2, 'f37v': 2, 'f38r': 2}
P = dict(ALPHA=1.0, BETA=0.6, CLEN=1.3, SKIP=9.0, BEAM=400, MAXC=30, WBON=0.0, WFREQ=0.0, WOOV=0.0, SMOOTH=0.3, PRIORG=2.0)
for k in list(P):
    if k in os.environ: P[k] = type(P[k])(os.environ[k])

# ------------------------------------------------------------------ key
EXP = [('M.ta', 'Maesta'), ('Sig.ria', 'Signoria'), ('Ill.ma', 'Illustrissima'), ('Ser.mo', 'Serenissimo'),
       ('Cons. di X', 'Consiglio di Dieci'), ('Capi di X', 'Capi di Dieci'), ('Gio.', 'Giovanni'), ('Mons.', 'Monsignor'),
       ('Sig.', 'Signor'), ('Princ.', 'Principe'), ('V.ra', 'Vostra')]
def load_key():
    key = {}
    for f in ('keys/zifra_prima_R1789.tsv', 'keys/ottobon_overrides.tsv'):
        for l in open(os.path.join(HERE, f), encoding='utf8'):
            if l.startswith('#') or not l.strip(): continue
            k, v = l.rstrip('\n').split('\t')[:2]; key[k] = v
    return key
KEY = load_key()
def val(k):
    v = KEY[k]
    if v == '_' or v.startswith('#'): return ''
    for a, b in EXP: v = v.replace(a, b)
    return lm.norm(v, 'early')
VAL = {k: val(k) for k in KEY}
def vclass(k):
    v = VAL[k]
    if not v: return 'null'
    if len(v) == 1: return 'letter'
    if len(v) <= 3 and ' ' not in v: return 'syl'
    return 'word'

# ------------------------------------------------------------------ data
TOK = re.compile(r'^([acdfgh])(\d{0,2})(\??)$')
def parse_tok(t):
    m = TOK.match(t)
    if not m: return None
    return m.group(1), m.group(2), bool(m.group(3)) or not m.group(2)
def load_ct(page):
    lines, cur = [], None
    for l in open(os.path.join(HERE, 'ct_%s.txt' % page), encoding='utf8'):
        m = re.match(r'#\s*f\.\s*\d+[rv]\s+l\.(\d+)', l)
        if m: cur = int(m.group(1)); continue
        if l.startswith('#') or not l.strip(): continue
        lines.append((cur, l.split()))
    return lines
def load_rd(page):
    out = []
    txt = open(os.path.join(HERE, 'rd_%s.txt' % page), encoding='utf8').read()
    for b in re.split(r'^# f\.', txt, flags=re.M)[1:]:
        m = re.match(r'\s*\d+[rv]\s+l\.\s*(\d+)', b)
        ct = re.search(r'^ct:\s*(.*)$', b, re.M); cf = re.search(r'^conf:\s*(\w+)', b, re.M)
        it = re.search(r'^it:\s*(.*)$', b, re.M)
        if not ct: continue
        out.append(dict(line=int(m.group(1)) if m else None, toks=ct.group(1).split(), raw='# f.' + b.rstrip(chr(10)) + chr(10),
                        conf=(cf.group(1).lower() if cf else 'low'), it=it.group(1) if it else ''))
    return out
def tcost(a, b):
    pa, pb = parse_tok(a.rstrip('?') or a), parse_tok(b.rstrip('?') or b)
    if not pa or not pb: return 1.0
    if a.rstrip('?') == b.rstrip('?'): return 0.0
    c = 0.0 if pa[0] == pb[0] else 0.5
    da, db = pa[1], pb[1]
    if len(da) == len(db): c += 0.25 * sum(x != y for x, y in zip(da, db))
    else: c += 0.4
    return min(c, 1.2)
def align(A, B, gap=0.9):
    n, m = len(A), len(B)
    D = np.zeros((n + 1, m + 1)); D[:, 0] = np.arange(n + 1) * gap; D[0, :] = np.arange(m + 1) * gap
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i, j] = min(D[i - 1, j - 1] + tcost(A[i - 1], B[j - 1]), D[i - 1, j] + gap, D[i, j - 1] + gap)
    i, j, out = n, m, []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and abs(D[i, j] - D[i - 1, j - 1] - tcost(A[i - 1], B[j - 1])) < 1e-9:
            out.append((i - 1, j - 1)); i -= 1; j -= 1
        elif i > 0 and abs(D[i, j] - D[i - 1, j] - gap) < 1e-9: out.append((i - 1, None)); i -= 1
        else: out.append((None, j - 1)); j -= 1
    return out[::-1]
def page_pairs(page):
    """Aligned (read token, hand token, conf, rd line idx, ct flat idx) for a page."""
    ct = [t for _, L in load_ct(page) for t in L]
    rd = load_rd(page)
    rflat, rinfo = [], []
    for bi, b in enumerate(rd):
        for t in b['toks']: rflat.append(t); rinfo.append((b['conf'], bi))
    pairs = []
    for i, j in align(ct, rflat):
        if i is not None and j is not None:
            pairs.append((ct[i], rflat[j], rinfo[j][0], rinfo[j][1], i))
    return ct, rd, pairs

# ------------------------------------------------------------------ channel + prior
DIG = '0123456789'
class Model:
    def __init__(self, train_pages, extra=()):
        self.bc = collections.Counter(); self.dc = {p: collections.Counter() for p in 'TUS'}
        self.lc = collections.Counter(); self.prior = collections.Counter()
        allp = []
        for pg in train_pages:
            _, _, pairs = page_pairs(pg)
            for r, h, conf, _, _ in pairs:
                if conf not in ('high', 'medium') or '?' in h or '?' in r: continue
                allp.append((r, h, 1.0))
        allp += list(extra)
        for r, h, w in allp:
                pr, ph = parse_tok(r.rstrip('?')), parse_tok(h)
                if not pr or not ph or h not in KEY or not pr[1]: continue
                self.prior[h] += w
                self.bc[(pr[0], ph[0])] += w
                a, b = pr[1], ph[1]
                self.lc[(len(a), len(b))] += w
                if len(a) == len(b):
                    pos = ['S'] if len(a) == 1 else ['T', 'U']
                    for p, x, y in zip(pos, a, b): self.dc[p][(x, y)] += w
        sm = P['SMOOTH']
        self.lb = {}
        for y in 'acdfgh':
            tot = sum(self.bc[(x, y)] for x in 'acdfgh') + 6 * sm
            for x in 'acdfgh': self.lb[(x, y)] = math.log((self.bc[(x, y)] + sm) / tot)
        self.ld = {}
        for p in 'TUS':
            for y in DIG:
                tot = sum(self.dc[p][(x, y)] for x in DIG) + 10 * sm
                for x in DIG: self.ld[(p, x, y)] = math.log((self.dc[p][(x, y)] + sm) / tot)
        totl = sum(self.lc.values()) + 4
        self.ll = {k: math.log((self.lc[k] + 1) / totl) for k in [(1, 1), (2, 2), (1, 2), (2, 1)]}
        # code prior: counts + PRIORG * class-uniform mass
        cls = collections.Counter()
        for k, v in self.prior.items(): cls[vclass(k)] += v
        ncls = collections.Counter(vclass(k) for k in KEY)
        N = sum(self.prior.values())
        self.lprior = {}
        for k in KEY:
            c = vclass(k)
            pc = (cls[c] + 1) / (N + 4)
            self.lprior[k] = math.log((self.prior[k] + P['PRIORG'] * pc) / (N + P['PRIORG']))
        self.ncodes = len(KEY)
    def lchan(self, r, k):
        pr = parse_tok(r)
        bk, dk = k[0], k[1:]
        if not pr: return -12.0
        br, dr, unk = pr
        s = self.lb[(br, bk)]
        if not dr: return s - math.log(100)
        if len(dr) == len(dk):
            pos = ['S'] if len(dr) == 1 else ['T', 'U']
            s += self.ll[(len(dr), len(dk))] + sum(self.ld[(p, x, y)] for p, x, y in zip(pos, dr, dk))
        else:
            s += self.ll.get((len(dr), len(dk)), -6)
            if len(dr) == 2:   # read 2 digits, true 1: one read digit spurious
                s += max(self.ld[('S', dr[0], dk)], self.ld[('S', dr[1], dk)]) - math.log(10)
            else:              # read 1 digit, true 2: one dropped
                s += max(self.ld[('S', dr, dk[0])], self.ld[('S', dr, dk[1])]) - math.log(10)
        if unk: s -= 0.5
        return s
    def cands(self, r):
        out = []
        for k in KEY:
            out.append((self.lchan(r, k) + P['BETA'] * self.lprior[k], k))
        out.sort(reverse=True)
        return out[:P['MAXC']]

# ------------------------------------------------------------------ LM
_LM = None
def get_lm():
    """The registered lang/ model 'it-venezia' (it-cinquecento sources + Alberi's Relazioni at double weight; formerly
    built here by build_venlm.py into corpus/venlm.o5.sp). LMID=<model> overrides; LOCAL_VENLM=1 loads the old local
    table if it is on disk (the 9 Oct 2026 calibration figures were made with it)."""
    global _LM
    if _LM is None:
        p = os.path.join(HERE, 'corpus', 'venlm.o5.sp')
        if os.environ.get('LOCAL_VENLM') and os.path.exists(p + '.json'):
            meta = json.load(open(p + '.json'))
            _LM = lm.DenseLM(np.load(p + '.npy'), meta['order'], meta['alpha'], meta)
        else:
            _LM = lm.load(os.environ.get('LMID', 'it-venezia'), order=5, spaces=True)
    return _LM
_WORDS = None
def words():
    global _WORDS
    if _WORDS is None:
        p = os.path.join(HERE, 'corpus', 'venwords.json')
        _WORDS = json.load(open(p)) if os.path.exists(p) else {}
    return _WORDS

_LEX = None; _PRE = None; _EXT = {}
def lex():
    """Lexicon (word -> log10 freq) and prefix set, words with freq >= LEXMIN in the training corpus."""
    global _LEX, _PRE
    if _LEX is None:
        w = words(); mn = int(os.environ.get('LEXMIN', 3))
        _LEX = {k: math.log10(v) for k, v in w.items() if v >= mn}
        _PRE = set()
        for k in _LEX:
            for n in range(1, len(k) + 1): _PRE.add(k[:n])
    return _LEX, _PRE
def wscore(w):
    if not w: return 0.0
    L, _ = lex()
    if w in L: return P['WBON'] + P['WFREQ'] * L[w]
    return -P['WOOV']
def extend(partial, sp, v):
    """Word-level score of appending (space?) + v to a partial word; returns (score, new partial)."""
    key = (partial, sp, v)
    r = _EXT.get(key)
    if r is not None: return r
    L, PRE = lex()
    g = 0.0; cur = partial
    if sp:
        g += wscore(cur) if (not cur or cur in PRE) else 0.0
        cur = ''
    for ch in v:
        if ch == ' ':
            g += wscore(cur) if (not cur or cur in PRE) else 0.0
            cur = ''
        else:
            was = (cur in PRE) or not cur
            cur = cur + ch
            if was and cur not in PRE: g -= P['WOOV']
    if len(cur) > 24: cur = cur[-24:]
    r = (g, cur); _EXT[key] = r
    return r
_WID = {}
def wid(s):
    r = _WID.get(s)
    if r is None: r = _WID[s] = len(_WID)
    return r

def opt_list(t, model, i, forced, forbid):
    if forced is not None and i in forced:
        k = forced[i]
        return [((model.lchan(t, k) + P['BETA'] * model.lprior[k]) if k else -P['SKIP'], k)]
    opts = [(lc, k) for lc, k in model.cands(t)] + [(-P['SKIP'], None)]
    if forbid and i in forbid:
        opts = [(c, k) for c, k in opts if (VAL[k] if k else '') not in forbid[i]]
    return opts

def decode(toks, model, init_ctx=None, forced=None, forbid=None, init_part=''):
    """toks: read tokens. forced: {i: code or None(skip)}; forbid: {i: set(values)}.
    Returns (score, path [(code or None, space_before)], plaintext, final ctx)."""
    L = get_lm(); A, K = L.A, L.order; M = A ** (K - 1); lp = L.lp
    idx = L.index; useW = bool(P['WBON'] or P['WOOV'] or P['WFREQ'])
    ctx0 = 0 if init_ctx is None else init_ctx
    st = np.array([ctx0], dtype=np.int64); sc = np.array([0.0]); parts = [init_part]
    bps = []
    for i, t in enumerate(toks):
        opts = opt_list(t, model, i, forced, forbid)
        nst, nsc, nbp, npart = [], [], [], []
        ns = len(st); ar = np.arange(ns)
        for oi, (lc, k) in enumerate(opts):
            v = VAL[k] if k else ''
            for sp in ((0, 1) if v else (0,)):
                s = ' ' + v if sp else v
                c = st.copy(); g = sc + lc
                if sp: ok = (c % A) != 0
                for ch in s:
                    code = c * A + idx[ch]
                    g = g + P['ALPHA'] * lp[code] + (P['CLEN'] if ch != ' ' else 0.0)
                    c = code % M
                if sp: g = np.where(ok, g, -1e18)
                if useW:
                    ex = [extend(p, sp, v) for p in parts]
                    g = g + np.fromiter((e[0] for e in ex), float, ns)
                    npart.extend(e[1] for e in ex)
                else:
                    npart.extend(parts)
                nst.append(c); nsc.append(g)
                nbp.append(np.stack([ar, np.full(ns, oi), np.full(ns, sp)], 1))
        nst = np.concatenate(nst); nsc = np.concatenate(nsc); nbp = np.concatenate(nbp)
        keyv = nst * 4000000 + np.fromiter((wid(p) for p in npart), np.int64, len(npart)) if useW else nst
        order = np.argsort(-nsc, kind='stable')
        _, first = np.unique(keyv[order], return_index=True)
        keep = order[first]
        keep = keep[np.argsort(-nsc[keep], kind='stable')][:P['BEAM']]
        st, sc = nst[keep], nsc[keep]; parts = [npart[x] for x in keep]
        bps.append((nbp[keep], opts))
    # close the last word
    if useW: sc = sc + np.array([wscore(p) if p in lex()[1] else 0.0 for p in parts])
    j = int(np.argmax(sc)); best = float(sc[j]); jf = j
    path = []
    for bp, opts in reversed(bps):
        prev, oi, sp = bp[j]
        path.append((opts[oi][1], int(sp))); j = int(prev)
    path.reverse()
    plain = ''.join((' ' if sp else '') + (VAL[k] if k else '') for k, sp in path)
    return best, path, plain, int(st[jf])

def path_states(path):
    L = get_lm(); A, K = L.A, L.order; M = A ** (K - 1)
    states = []; c = 0; part = ''
    for k, sp in path:
        states.append((c, part))
        v = VAL[k] if k else ''
        for ch in (' ' if sp else '') + v: c = (c * A + L.index[ch]) % M
        part = extend(part, sp, v)[1] if v else part
    return states

def margins(toks, path, model, W=6, R=6):
    """Per token: score drop when its value is forced to change, re-decoding a window of +-W tokens
    (left state = the best path's; the next R tokens forced to the best path)."""
    states = path_states(path)
    out = []
    saved = P['BEAM']; P['BEAM'] = int(os.environ.get('MBEAM', 150))
    for i in range(len(toks)):
        a, b = max(0, i - W), min(len(toks), i + W + R + 1)
        sub = toks[a:b]
        forced = {j - a: path[j][0] for j in range(i + W + 1, b)}
        s0, p0, _, _ = decode(sub, model, init_ctx=states[a][0], init_part=states[a][1], forced=forced)
        v = VAL[path[i][0]] if path[i][0] else ''
        s1, p1, _, _ = decode(sub, model, init_ctx=states[a][0], init_part=states[a][1], forced=forced, forbid={i - a: {v}})
        alt = p1[i - a][0]
        out.append((s0 - s1, alt))
    P['BEAM'] = saved
    return out

def piece_toks(pages):
    """Flat token list for a sequence of pages, with (page, ct line, index-in-page) per token."""
    toks, where = [], []
    for pg in pages:
        n = 0
        for ln, L in load_ct(pg):
            for t in L: toks.append(t); where.append((pg, ln, n)); n += 1
    return toks, where

def sim(flat=1.0, seed=1):
    """Synthetic test: hand-read high/medium lines without '?' as truth, re-corrupted by sampling the channel
    (log-probs multiplied by `flat` < 1 to raise the error rate); decode; value agreement."""
    import random
    rnd = random.Random(seed)
    res = []
    for pg in PAGES:
        model = Model([p for p in PAGES if p != pg])
        truth = []
        for b in load_rd(pg):
            if b['conf'] in ('high', 'medium'):
                run = []
                for t in b['toks'] + ['?']:
                    if '?' not in t and t in KEY: run.append(t)
                    else:
                        if len(run) >= 4: truth += run
                        run = []
        def samp(k):
            bk, dk = k[0], k[1:]
            ws = [(math.exp(flat * model.lb[(x, bk)]), x) for x in 'acdfgh']
            b = rnd.choices([x for _, x in ws], [w for w, _ in ws])[0]
            pos = ['S'] if len(dk) == 1 else ['T', 'U']
            d = ''
            for p, y in zip(pos, dk):
                ws = [math.exp(flat * model.ld[(p, x, y)]) for x in DIG]
                d += rnd.choices(DIG, ws)[0]
            d = d.lstrip('0') or '0'
            return b + d
        read = [samp(k) for k in truth]
        ident = sum(1 for r, k in zip(read, truth) if r in KEY and VAL[r] == VAL[k])
        _, path, plain, _ = decode(read, model)
        ag = sum(1 for (k2, _), k in zip(path, truth) if k2 and VAL[k2] == VAL[k])
        res.append((pg, len(truth), ident, ag))
    n = sum(r[1] for r in res)
    print('n', n, end=' ')
    print('flat %.2f ident %.1f%% decoded %.1f%%' % (flat, 100 * sum(r[2] for r in res) / n, 100 * sum(r[3] for r in res) / n), json.dumps(P))

# ------------------------------------------------------------------ CLI
def self_pairs(model, w):
    ex = []
    for g in (['f35r', 'f35v', 'f36r', 'f36v'], ['f37r', 'f37v', 'f38r']):
        toks, _ = piece_toks(g)
        _, path, _, _ = decode(toks, model)
        ex += [(t, k, w) for t, (k, sp) in zip(toks, path) if k]
    return ex
def calib(verbose=False):
    tot = agree = 0; per = {}
    EM = int(os.environ.get('EM', 0)); EMW = float(os.environ.get('EMW', 0.5))
    for pg in PAGES:
        model = Model([p for p in PAGES if p != pg])
        for it in range(EM):
            model = Model([p for p in PAGES if p != pg], extra=self_pairs(model, EMW))
        ct, rd, pairs = page_pairs(pg)
        _, path, plain, _ = decode(ct, model)
        a = n = 0
        for r, h, conf, bi, i in pairs:
            if conf not in ('high', 'medium') or '?' in h or h not in KEY: continue
            n += 1
            k = path[i][0]
            if k and VAL[k] == VAL[h]: a += 1
        per[pg] = (a, n); tot += n; agree += a
    print(' '.join('%s %d/%d=%.0f%%' % (p, a, n, 100 * a / max(1, n)) for p, (a, n) in per.items()),
          '| ALL %d/%d = %.1f%%' % (agree, tot, 100 * agree / max(1, tot)), json.dumps(P))
    return agree / max(1, tot)

if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'calib'
    if cmd == 'calib':
        calib()
    elif cmd == 'sim':
        sim(float(sys.argv[2]) if len(sys.argv) > 2 else 1.0)
    elif cmd == 'decode':
        pages = sys.argv[2:] or PAGES
        model = Model(PAGES)
        groups = [[p for p in pages if PIECE[p] == 1], [p for p in pages if PIECE[p] == 2]]
        os.makedirs(os.path.join(HERE, 'dec_out'), exist_ok=True)
        tag = os.environ.get('TAG', '')
        for g in groups:
            if not g: continue
            toks, where = piece_toks(g)
            forced = None
            if os.environ.get('FORCEHAND'):
                forced = {}; off = 0
                for pg in g:
                    ct, rd, pairs = page_pairs(pg)
                    for r, h, conf, bi, i in pairs:
                        if conf in ('high', 'medium') and '?' not in h and h in KEY: forced[off + i] = h
                    off += len(ct)
            _, path, plain, _ = decode(toks, model, forced=forced)
            mg = margins(toks, path, model) if os.environ.get('MARG', '1') == '1' else [(0, None)] * len(toks)
            for pg in g:
                f = open(os.path.join(HERE, 'dec_out', '%s%s.txt' % (pg, tag)), 'w', encoding='utf8')
                NL = chr(10)
                f.write('# dec.py %s %s' % (pg, json.dumps(P)) + NL)
                lines = collections.OrderedDict()
                for i, (p, ln, n) in enumerate(where):
                    if p == pg: lines.setdefault(ln, []).append(i)
                for ln, ii in lines.items():
                    f.write('# %s l.%s' % (pg, ln) + NL)
                    f.write('rdct: ' + ' '.join(toks[i] for i in ii) + NL)
                    f.write('dec:  ' + ' '.join((path[i][0] or '-') for i in ii) + NL)
                    f.write('val:  ' + ' '.join(((('_' if path[i][1] else '') + VAL[path[i][0]].replace(' ', '~')) if path[i][0] else '-') for i in ii) + NL)
                    f.write('it:   ' + ''.join(((' ' if path[i][1] else '') + (VAL[path[i][0]] if path[i][0] else '')) for i in ii) + NL)
                    f.write('marg: ' + ' '.join('%.1f' % mg[i][0] for i in ii) + NL)
                    f.write('alt:  ' + ' '.join((mg[i][1] or '-') for i in ii) + NL)
                f.close()
            print(g, 'done')
