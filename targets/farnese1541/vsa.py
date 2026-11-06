"""Joint key + segmentation annealer for mixed one-/two-digit substitution (Klee's design for IA-2).

Key: each code (10 single digits, 100 digit pairs) is OFF, NULL, or a letter. An inner beam decoder (B states per
digit position, 5-gram context) finds the best split of the digit stream under a key; the outer simulated annealing
changes the key. Score = 5-gram log-prob of the letters + lbonus per letter - nullpen per null - skippen per
undecodable digit.

  python vsa.py <cipher> [--H 1] [--NN 2] [--iters 300000] [--restarts 12] [--procs 12] [--out run]

<cipher>: r91 (DECODE R91 transcript), ia2 (IA-2 reread, dots dropped, first --len digits), or a file of digits.
"""
import argparse, json, math, os, re, sys, time
from multiprocessing import Pool
import numpy as np
import numba as nb

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from lang import lm

LETTERS = 'abcdefghilmnopqrstuxz'
OFF, NUL = -1, -2


def code_name(c):
    return str(c) if c < 10 else f'{(c - 10) // 10}{(c - 10) % 10}'


def load_cipher(name, length=None, offset=0):
    if name == 'r91':
        from parse_r91 import digits
        d = digits()
    elif name == 'ia2':
        d = ''
        for line in open(os.path.join(HERE, '..', 'vatican5', 'IA-2_reread.txt'), encoding='utf-8'):
            if line.startswith('#') or line.startswith('<'):
                continue
            d += ''.join(re.findall(r'\d', line))
    else:
        d = ''.join(re.findall(r'\d', open(name, encoding='utf-8').read()))
    if length:
        d = d[offset:offset + length]
    return np.array([int(x) for x in d], dtype=np.int64)


@nb.njit(cache=True)
def _insert(bs, bc, bp, bk, be, bcnt, j, s, c, pi, pk, e, B):
    m = bcnt[j]
    worst, wk = 1e300, -1
    for k in range(m):
        if bc[j, k] == c:
            if s > bs[j, k]:
                bs[j, k] = s; bp[j, k] = pi; bk[j, k] = pk; be[j, k] = e
            return
        if bs[j, k] < worst:
            worst = bs[j, k]; wk = k
    if m < B:
        k = m; bcnt[j] = m + 1
    elif s > worst:
        k = wk
    else:
        return
    bs[j, k] = s; bc[j, k] = c; bp[j, k] = pi; bk[j, k] = pk; be[j, k] = e


@nb.njit(cache=True)
def decode(dig, assign, lp, A, A4, B, nullpen, skippen, lbonus):
    """Returns (score, emitted) where emitted[i] codes the transition into the best path (see trace)."""
    n = dig.shape[0]
    bs = np.full((n + 1, B), -1e300)
    bc = np.zeros((n + 1, B), np.int64)
    bp = np.zeros((n + 1, B), np.int64)
    bk = np.zeros((n + 1, B), np.int64)
    be = np.zeros((n + 1, B), np.int64)
    bcnt = np.zeros(n + 1, np.int64)
    bs[0, 0] = 0.0; bcnt[0] = 1
    for i in range(n):
        for k in range(bcnt[i]):
            s = bs[i, k]; c = bc[i, k]
            for L in range(1, 3):
                if i + L > n:
                    break
                code = dig[i] if L == 1 else 10 + dig[i] * 10 + dig[i + 1]
                a = assign[code]
                if a == -1:
                    continue
                if a == -2:
                    _insert(bs, bc, bp, bk, be, bcnt, i + L, s - nullpen, c, i, k, 1000 + code, B)
                else:
                    _insert(bs, bc, bp, bk, be, bcnt, i + L, s + lp[c * A + a] + lbonus, (c * A + a) % A4, i, k, code, B)
            _insert(bs, bc, bp, bk, be, bcnt, i + 1, s - skippen, c, i, k, -1, B)
    best, bkk = -1e300, 0
    for k in range(bcnt[n]):
        if bs[n, k] > best:
            best = bs[n, k]; bkk = k
    # trace: list of (start, emitted)
    path = np.full(n, -9, np.int64)
    j, k = n, bkk
    while j > 0:
        pi = bp[j, k]; pk = bk[j, k]
        path[pi] = be[j, k]
        j, k = pi, pk
    return best, path


@nb.njit(cache=True)
def anneal(dig, cand, letters, H, NN, lp, A, A4, B, nullpen, skippen, lbonus, iters, T0, T1, seed, init):
    np.random.seed(seed)
    nc = cand.shape[0]
    assign = np.full(110, -1, np.int64)
    if init[0] != -9:
        for c in range(110):
            assign[c] = init[c]
    else:
        perm = np.random.permutation(nc)
        for li in range(letters.shape[0]):
            assign[cand[perm[li]]] = letters[li]
    cnt = np.zeros(A, np.int64)
    nnull = 0
    for c in range(110):
        if assign[c] >= 0:
            cnt[assign[c]] += 1
        elif assign[c] == -2:
            nnull += 1
    cur, _ = decode(dig, assign, lp, A, A4, B, nullpen, skippen, lbonus)
    best = cur
    bassign = assign.copy()
    for it in range(iters):
        T = T0 * (T1 / T0) ** (it / iters)
        r = np.random.random()
        a = cand[np.random.randint(nc)]
        old_a = assign[a]
        b = -1; old_b = 0; dn = 0; la = -9; lb = -9
        if r < 0.6:
            b = cand[np.random.randint(nc)]
            old_b = assign[b]
            if old_a == old_b:
                continue
            assign[a] = old_b; assign[b] = old_a
        elif r < 0.85:
            if old_a < 0:
                continue
            l = letters[np.random.randint(letters.shape[0])]
            if l == old_a or cnt[l] >= H:
                continue
            assign[a] = l; cnt[old_a] -= 1; cnt[l] += 1; la = old_a; lb = l
        elif r < 0.95:
            # add or remove a homophone
            if old_a == -1 and H > 1:
                l = letters[np.random.randint(letters.shape[0])]
                if cnt[l] >= H:
                    continue
                assign[a] = l; cnt[l] += 1; la = -1; lb = l
            elif old_a >= 0 and cnt[old_a] > 1:
                assign[a] = -1; cnt[old_a] -= 1; la = old_a; lb = -1
            else:
                continue
        else:
            if old_a == -1 and nnull < NN:
                assign[a] = -2; dn = 1
            elif old_a == -2:
                assign[a] = -1; dn = -1
            else:
                continue
            nnull += dn
        sc, _ = decode(dig, assign, lp, A, A4, B, nullpen, skippen, lbonus)
        if sc >= cur or np.random.random() < math.exp((sc - cur) / T):
            cur = sc
            if cur > best:
                best = cur; bassign[:] = assign
        else:
            assign[a] = old_a
            if b >= 0:
                assign[b] = old_b
            if la != -9 or lb != -9:
                if la >= 0:
                    cnt[la] += 1
                if lb >= 0:
                    cnt[lb] -= 1
            nnull -= dn
    return best, bassign


def render(dig, assign, path, Aalpha):
    out, segs = [], []
    i, n = 0, len(dig)
    while i < n:
        e = path[i]
        if e == -1:
            out.append('#'); segs.append((code_name(dig[i]), '#')); i += 1
        elif e >= 1000:
            c = e - 1000; out.append('.'); segs.append((code_name(c), '.')); i += 1 if c < 10 else 2
        else:
            ch = Aalpha[assign[e]]; out.append(ch); segs.append((code_name(e), ch)); i += 1 if e < 10 else 2
    return ''.join(out), segs


def keystr(assign, Aalpha):
    by = {}
    for c in range(110):
        a = assign[c]
        if a >= 0:
            by.setdefault(Aalpha[a], []).append(code_name(c))
        elif a == -2:
            by.setdefault('NULL', []).append(code_name(c))
    return ' '.join(f'{k}={",".join(v)}' for k, v in sorted(by.items()))


_G = {}


def _work(args):
    seed, opt = args
    m = lm.load(opt['model'], order=5, spaces=False)
    dig = load_cipher(opt['cipher'], opt['len'], opt['offset'])
    A = m.A; A4 = A ** 4
    letters = np.array([m.index[c] for c in opt['letters']], dtype=np.int64)
    from collections import Counter
    s = ''.join(map(str, dig))
    pc = Counter(s[i:i + 2] for i in range(len(s) - 1))
    cand = list(range(10)) + [10 + int(p) for p, v in pc.items() if v >= opt['mincount']]
    cand = np.array(sorted(cand), dtype=np.int64)
    init = np.full(110, -9, np.int64)
    if opt.get('init'):
        init = np.array(opt['init'], dtype=np.int64)
    t = time.time()
    best, assign = anneal(dig, cand, letters, opt['H'], opt['NN'], m.lp.astype(np.float64), A, A4, opt['B'],
                          opt['nullpen'], opt['skippen'], opt['lbonus'], opt['iters'], opt['T0'], opt['T1'], seed, init)
    sc, path = decode(dig, assign, m.lp.astype(np.float64), A, A4, opt['B'], opt['nullpen'], opt['skippen'], opt['lbonus'])
    txt, segs = render(dig, assign, path, m.alpha)
    nl = sum(1 for _, ch in segs if ch not in '.#')
    pure = m.per_char(''.join(ch for _, ch in segs if ch not in '.#'))
    return dict(seed=seed, score=sc, key=keystr(assign, m.alpha), assign=assign.tolist(), text=txt,
                letters=nl, per_char=pure, skips=txt.count('#'), nulls=txt.count('.'), secs=time.time() - t)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('cipher')
    ap.add_argument('--len', type=int, default=None)
    ap.add_argument('--offset', type=int, default=0)
    ap.add_argument('--model', default='it-cinquecento')
    ap.add_argument('--letters', default=LETTERS)
    ap.add_argument('--H', type=int, default=1)
    ap.add_argument('--NN', type=int, default=2)
    ap.add_argument('--B', type=int, default=8)
    ap.add_argument('--nullpen', type=float, default=4.0)
    ap.add_argument('--skippen', type=float, default=12.0)
    ap.add_argument('--lbonus', type=float, default=2.5)
    ap.add_argument('--mincount', type=int, default=3)
    ap.add_argument('--iters', type=int, default=200000)
    ap.add_argument('--T0', type=float, default=15.0)
    ap.add_argument('--T1', type=float, default=0.3)
    ap.add_argument('--restarts', type=int, default=12)
    ap.add_argument('--procs', type=int, default=12)
    ap.add_argument('--seed0', type=int, default=1)
    ap.add_argument('--init', default=None, help='json file with an assign list to start from')
    ap.add_argument('--out', default=None)
    a = ap.parse_args()
    opt = vars(a).copy()
    if a.init:
        opt['init'] = json.load(open(a.init))['assign']
    jobs = [(a.seed0 + i, opt) for i in range(a.restarts)]
    with Pool(a.procs) as p:
        res = p.map(_work, jobs)
    res.sort(key=lambda r: -r['score'])
    for r in res:
        print(f"seed {r['seed']:3d} score {r['score']:9.1f} pc {r['per_char']:.3f} L {r['letters']} null {r['nulls']} skip {r['skips']} {r['secs']:.0f}s")
        print('   ', r['key'])
        print('   ', r['text'][:240])
    if a.out:
        json.dump(dict(opt=opt, results=res), open(a.out + '.json', 'w'), indent=1)


if __name__ == '__main__':
    main()
