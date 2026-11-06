"""Polyphonic key refinement for R91 (numba beam decoder).

A key maps each code (10 single digits, 100 pairs) to a set of outputs (letters, syllables, words, or '' = null).
Score = 5-gram log-prob (it-cinquecento, no spaces) of the best parse + lbonus per letter - nullpen per null used
- skippen per undecodable digit - optpen per output in the key.
Greedy: try every (code, output) addition and every removal; apply the best gain > 0; repeat.

  python vpoly.py --start k2cur --rounds 40 --out k2_learn
"""
import argparse, importlib, json, os, sys, time
import numpy as np
import numba as nb

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
from lang import lm
from parse_r91 import lines

MAXO, MAXL = 8, 5
V = 'aeiou'
CONS = 'bcdfglmnprstz'
VOCAB = list('abcdefghilmnopqrstuxz') + [c + v for c in CONS for v in V] + \
    ['che', 'chi', 'non', 'qua', 'que', 'qui', 'ghe', 'ghi', 'et', 'ns', 'smta', 'per', 'con', '']


def code_index(c):
    return int(c) if len(c) == 1 else 10 + int(c)


def code_name(i):
    return str(i) if i < 10 else f'{(i - 10) // 10}{(i - 10) % 10}'


def pack(key, m):
    oc = np.zeros((110, MAXO, MAXL), np.int64)
    ol = np.zeros((110, MAXO), np.int64)
    no = np.zeros(110, np.int64)
    for c, outs in key.items():
        i = code_index(c)
        for k, o in enumerate(outs[:MAXO]):
            ol[i, k] = len(o)
            for j, ch in enumerate(o):
                oc[i, k, j] = m.index[ch]
        no[i] = min(len(outs), MAXO)
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
def pdecode(dig, oc, ol, no, lp, A, A4, B, skippen, lbonus, nullpen):
    n = dig.shape[0]
    bs = np.full((n + 1, B), -1e300); bc = np.zeros((n + 1, B), np.int64)
    bp = np.zeros((n + 1, B), np.int64); bk = np.zeros((n + 1, B), np.int64); bo = np.zeros((n + 1, B), np.int64)
    cnt = np.zeros(n + 1, np.int64)
    bs[0, 0] = 0.0; cnt[0] = 1
    for i in range(n):
        for k in range(cnt[i]):
            s = bs[i, k]; c = bc[i, k]
            for L in range(1, 3):
                if i + L > n:
                    break
                code = dig[i] if L == 1 else 10 + dig[i] * 10 + dig[i + 1]
                if dig[i] < 0 or (L == 2 and dig[i + 1] < 0):
                    continue
                for o in range(no[code]):
                    ns = s; nc = c
                    if ol[code, o] == 0:
                        ns -= nullpen
                    for j in range(ol[code, o]):
                        x = nc * A + oc[code, o, j]
                        ns += lp[x] + lbonus; nc = x % A4
                    _ins(bs, bc, bp, bk, bo, cnt, i + L, ns, nc, i, k, code * 16 + o, B)
            _ins(bs, bc, bp, bk, bo, cnt, i + 1, s - skippen, c, i, k, -1, B)
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


@nb.njit(cache=True)
def usage(dig, path, nout):
    u = np.zeros((110, 16), np.int64)
    for i in range(dig.shape[0]):
        e = path[i]
        if e >= 0:
            u[e // 16, e % 16] += 1
    return u


class Model:
    def __init__(self, B=16, skippen=15.0, digits=None, lbonus=2.0, nullpen=3.0):
        self.m = lm.load('it-cinquecento', order=5, spaces=False)
        if digits is None:
            digits = ''.join(t[0] for _, _, toks, _ in lines() for t in toks)
        self.d = digits
        self.dig = np.array([int(x) for x in digits], dtype=np.int64)
        self.lp = self.m.lp.astype(np.float64)
        self.B = B; self.skippen = skippen; self.lbonus = lbonus; self.nullpen = nullpen

    def score(self, key):
        oc, ol, no = pack(key, self.m)
        return pdecode(self.dig, oc, ol, no, self.lp, self.m.A, self.m.A ** 4, self.B, self.skippen, self.lbonus, self.nullpen)

    def text(self, key, B=64):
        oc, ol, no = pack(key, self.m)
        s, path = pdecode(self.dig, oc, ol, no, self.lp, self.m.A, self.m.A ** 4, B, self.skippen, self.lbonus, self.nullpen)
        out = []
        for i, e in enumerate(path):
            if e == -1:
                out.append((self.d[i], '#'))
            elif e >= 0:
                c = code_name(e // 16)
                out.append((c, key[c][e % 16]))
        return s, out


def nopts(key):
    return sum(len(v) for v in key.values())


_W = {}


def _winit(B, skippen, lbonus, nullpen):
    _W['M'] = Model(B=B, skippen=skippen, lbonus=lbonus, nullpen=nullpen)


def _wcode(args):
    key, c, optpen, base, vocab = args
    M = _W['M']; best = (0.0, None)
    outs = key.get(c, [])
    for o in list(outs):           # removal
        k2 = dict(key); k2[c] = [x for x in outs if x != o]
        g = M.score(k2)[0] - optpen * nopts(k2) - base
        if g > best[0]: best = (g, ('-', c, o))
    if len(outs) < MAXO:
        for o in vocab:            # addition (a single digit carries one letter or a null)
            if len(c) == 1 and len(o) > 1: continue
            if o in outs: continue
            k2 = dict(key); k2[c] = outs + [o]
            g = M.score(k2)[0] - optpen * nopts(k2) - base
            if g > best[0]: best = (g, ('+', c, o))
    return best


def greedy(M, key, optpen, rounds, codes=None, vocab=VOCAB, log=print, procs=6):
    from multiprocessing import Pool
    base = M.score(key)[0] - optpen * nopts(key)
    codes = codes or [code_name(i) for i in range(110)]
    present = set(M.d[i:i + 2] for i in range(len(M.d) - 1)) | set(M.d)
    codes = [c for c in codes if c in present]
    with Pool(procs, initializer=_winit, initargs=(M.B, M.skippen, M.lbonus, M.nullpen)) as pool:
        for r in range(rounds):
            t = time.time()
            res = pool.map(_wcode, [(key, c, optpen, base, vocab) for c in codes])
            best = max(res, key=lambda x: x[0])
            if best[1] is None:
                log(f'round {r}: no gain'); break
            op, c, o = best[1]
            key = dict(key)
            key[c] = [x for x in key.get(c, []) if x != o] if op == '-' else key.get(c, []) + [o]
            base = M.score(key)[0] - optpen * nopts(key)
            log(f'round {r}: {op}{c}={o!r} gain {best[0]:.1f} -> {base:.1f} ({time.time() - t:.0f}s)')
    return key, base


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--start', default='k2cur')
    ap.add_argument('--rounds', type=int, default=30)
    ap.add_argument('--optpen', type=float, default=12.0)
    ap.add_argument('--B', type=int, default=12)
    ap.add_argument('--out', default='k2_learn')
    ap.add_argument('--lbonus', type=float, default=2.0)
    ap.add_argument('--nullpen', type=float, default=3.0)
    a = ap.parse_args()
    if a.start.endswith('.json'):
        key = json.load(open(a.start))
    else:
        key = {k: list(v) for k, v in importlib.import_module(a.start).KEY.items()}
    M = Model(B=a.B, lbonus=a.lbonus, nullpen=a.nullpen)
    logf = open(a.out + '.log', 'w', encoding='utf-8')
    def log(s):
        print(s, flush=True); logf.write(s + '\n'); logf.flush()
    log(f'start score {M.score(key)[0]:.1f} options {nopts(key)}')
    key, base = greedy(M, key, a.optpen, a.rounds, log=log)
    json.dump(key, open(a.out + '.json', 'w'), indent=0, sort_keys=True)
    s, out = M.text(key)
    log(''.join(o for _, o in out))
