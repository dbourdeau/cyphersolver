"""Dot-aware decoder for R91 under key 2 (Meister's rule: "con il punto sopra la precedente").

The stream comes from the image re-read (reread/) where a line has been re-read, else from DECODE's
transcript (no dots). A dot over digit i marks the code that starts at i+1 as dotted: 80-83 ta te ti to, 84-86 qua
que qui, 87-89 che chi non, 08 N.S., 00 S.M.ta. An undotted 8x/08/00 takes its plain value (na ... ro); its dotted
value is still allowed at a cost (dotpen) because a dot can be faint or lost. Lines not yet re-read (DECODE, no
dots recorded) take either value at no cost. Digits lost to corrosion holes are
skipped at a small cost and shown as '_'; so may any digit marked uncertain (shown '#'). Struck digits are dropped.

  python vdot.py [keymodule] [--codes]
"""
import importlib, os, sys
import numpy as np
import numba as nb

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
from lang import lm
import parse_r91, parse_reread

MAXO, MAXL = 8, 6
DOTTED = {'80': ['ta'], '81': ['te'], '82': ['ti'], '83': ['to'], '84': ['qua'], '85': ['que'], '86': ['qui'],
          '87': ['che'], '88': ['chi'], '89': ['non'], '08': ['ns'], '00': ['smta']}


def stream():
    """[(folio.line, [tokens])] in text order; token = (digit or -1 lost, dotted_flag, unsure)."""
    rr = {(f, l): toks for f, l, toks in parse_reread.lines()}
    out = []
    for page, n, toks, _ in parse_r91.lines():
        rl = n - 15 if page == '64r' else n          # the re-read numbers 64r lines 16-21 as 16-21 too
        key = (page, n)
        if key in rr:
            ts = [(t['d'] if t['d'] is not None else -1, t['dot'] > 0, t['unsure'])
                  for t in rr[key] if t['d'] is not None or t['mark'] == 'lost']
            out.append((f'{page}.{n}', ts, True))
        else:
            out.append((f'{page}.{n}', [(int(t[0]), False, '?' in t) for t in toks], False))
    return out


def code_index(c, dotted=False):
    i = int(c) if len(c) == 1 else 10 + int(c)
    return i + 100 if dotted else i


def pack(key, m, dotted):
    oc = np.zeros((210, MAXO, MAXL), np.int64); ol = np.zeros((210, MAXO), np.int64); no = np.zeros(210, np.int64)
    def put(i, outs):
        for k, o in enumerate(outs[:MAXO]):
            ol[i, k] = len(o)
            for j, ch in enumerate(o):
                oc[i, k, j] = m.index[ch]
        no[i] = min(len(outs), MAXO)
    for c, outs in key.items():
        put(code_index(c), outs)
    for c, outs in dotted.items():
        put(code_index(c, True), outs)
    return oc, ol, no


@nb.njit(cache=True)
def _ins(bs, bc, bp, bk, bo, cnt, j, s, c, pi, pk, o, B):
    m = cnt[j]; worst = 1e300; wk = -1
    for k in range(m):
        if bc[j, k] == c:
            if s > bs[j, k]:
                bs[j, k] = s; bp[j, k] = pi; bk[j, k] = pk; bo[j, k] = o
            return
        if bs[j, k] < worst:
            worst = bs[j, k]; wk = k
    if m < B:
        k = m; cnt[j] = m + 1
    elif s > worst:
        k = wk
    else:
        return
    bs[j, k] = s; bc[j, k] = c; bp[j, k] = pi; bk[j, k] = pk; bo[j, k] = o


@nb.njit(cache=True)
def ddecode(dig, dotp, uns, oc, ol, no, lp, A, A4, B, skippen, lostpen, lbonus, nullpen, dotpen):
    n = dig.shape[0]
    bs = np.full((n + 1, B), -1e300); bc = np.zeros((n + 1, B), np.int64)
    bp = np.zeros((n + 1, B), np.int64); bk = np.zeros((n + 1, B), np.int64); bo = np.zeros((n + 1, B), np.int64)
    cnt = np.zeros(n + 1, np.int64)
    bs[0, 0] = 0.0; cnt[0] = 1
    for i in range(n):
        for k in range(cnt[i]):
            s = bs[i, k]; c = bc[i, k]
            if dig[i] < 0:
                _ins(bs, bc, bp, bk, bo, cnt, i + 1, s - lostpen, c, i, k, -2, B)
                continue
            for L in range(1, 3):
                if i + L > n:
                    break
                if L == 2 and dig[i + 1] < 0:
                    break
                base = dig[i] if L == 1 else 10 + dig[i] * 10 + dig[i + 1]
                for variant in range(2):
                    if variant == 1 and L == 1:
                        break
                    code = base + 100 * variant
                    pen = 0.0
                    if L == 2:
                        if dotp[i] == 1 and variant == 0 and no[base + 100] > 0:
                            pen = dotpen          # dotted position read with a plain value
                        if dotp[i] == 0 and variant == 1:
                            pen = dotpen          # plain position read with a dotted value
                    for o in range(no[code]):
                        ns = s - pen; nc = c
                        if ol[code, o] == 0:
                            ns -= nullpen
                        for j in range(ol[code, o]):
                            x = nc * A + oc[code, o, j]
                            ns += lp[x] + lbonus; nc = x % A4
                        _ins(bs, bc, bp, bk, bo, cnt, i + L, ns, nc, i, k, code * 16 + o, B)
            _ins(bs, bc, bp, bk, bo, cnt, i + 1, s - (lostpen if uns[i] == 1 else skippen), c, i, k, -1, B)
    best = -1e300; kk = 0
    for k in range(cnt[n]):
        if bs[n, k] > best:
            best = bs[n, k]; kk = k
    path = np.full(n, -9, np.int64)
    j = n; k = kk
    while j > 0:
        pi = bp[j, k]; pk = bk[j, k]
        path[pi] = bo[j, k]
        j = pi; k = pk
    return best, path


class Dec:
    def __init__(self, B=64, skippen=15.0, lostpen=3.0, lbonus=1.3, nullpen=4.0, dotpen=4.0, only=None):
        self.m = lm.load('it-cinquecento', order=5, spaces=False)
        self.lp = self.m.lp.astype(np.float64)
        self.S = stream()
        if only is not None:
            self.S = [x for x in self.S if x[0] in only]
        self.dig = np.array([t[0] for _, ts, _ in self.S for t in ts], dtype=np.int64)
        flat = [t for _, ts, _ in self.S for t in ts]
        rrflag = [rr for _, ts, rr in self.S for t in ts]
        self.uns = np.array([1 if t[2] else 0 for t in flat], dtype=np.int64)
        self.dotp = np.array([(1 if (i > 0 and flat[i - 1][1]) else 0) if rrflag[i] else 2
                              for i in range(len(flat))], dtype=np.int64)
        self.p = (B, skippen, lostpen, lbonus, nullpen, dotpen)

    def run(self, key, dotted=DOTTED):
        oc, ol, no = pack(key, self.m, dotted)
        B, sk, lo, lb, nu, dp = self.p
        s, path = ddecode(self.dig, self.dotp, self.uns, oc, ol, no, self.lp, self.m.A, self.m.A ** 4, B, sk, lo, lb, nu, dp)
        out = []
        n = len(self.dig)
        i = 0
        names = {}
        while i < n:
            e = path[i]
            if e == -2:
                out.append((i, '?', '_')); i += 1
            elif e == -1:
                out.append((i, str(self.dig[i]), '#')); i += 1
            else:
                code, o = e // 16, e % 16
                dotted_v = code >= 110
                base = code - 100 if dotted_v else code
                cname = str(base) if base < 10 else f'{(base - 10) // 10}{(base - 10) % 10}'
                val = (dotted if dotted_v else key)[cname][o]
                out.append((i, ("'" if dotted_v else '') + cname, val))
                i += 1 if base < 10 else 2
        return s, out

    def lines_out(self, out):
        """Group decoded units by manuscript line."""
        ends, pos = [], 0
        for name, ts, rr in self.S:
            pos += len(ts); ends.append((pos, name, rr))
        res, j, cur = [], 0, []
        for i, c, v in out:
            while j < len(ends) and i >= ends[j][0]:
                res.append((ends[j][1], ends[j][2], cur)); cur = []; j += 1
            cur.append((c, v))
        while j < len(ends):
            res.append((ends[j][1], ends[j][2], cur)); cur = []; j += 1
        return res


if __name__ == '__main__':
    from wordcov91 import segment
    keymod = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('-') else 'k2b'
    key = {k: list(v) for k, v in importlib.import_module(keymod).KEY.items()}
    # plain values only on undotted codes
    for c in DOTTED:
        if c in key:
            key[c] = [v for v in key[c] if v not in DOTTED[c]]
    D = Dec()
    s, out = D.run(key)
    print('score', round(s, 1))
    for name, rr, units in D.lines_out(out):
        txt = ''.join('|' if c == '11' else v for c, v in units)
        print(name, '*' if rr else ' ', ' | '.join(' '.join(segment(p)) for p in txt.split('|')))
        if '--codes' in sys.argv:
            print('      ', ' '.join(f'{c}={v or "-"}' for c, v in units))
