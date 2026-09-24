"""Ciphertext-only SAT attack on nonce-free LC4 with a partly known key.

The plaintext is a SAT variable. Before the signature ('#' starts it) every character is a letter or '_', and every
3-gram and 4-gram (with '_' as space) must occur in the English corpus. The signature is unconstrained.
usage: python lc4sat_co.py ciphertext keytemplate [--minmsg N] [--th3 N] [--th4 N] [--max K]
"""
import os, site, sys, time
os.add_dll_directory(os.path.join(site.getsitepackages()[-1], 'z3', 'lib'))
import numpy as np
from pysat.solvers import Cadical153
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool

AL = "#_23456789abcdefghijklmnopqrstuvwxyz"


def opt(name, default):
    return int(sys.argv[sys.argv.index(name) + 1]) if name in sys.argv else default


def rot_map(r, y):
    f = {}
    for k in range(36):
        i, j = divmod(k, 6)
        if i == r: j = (j + 1) % 6
        if j == y: i = (i + 1) % 6
        f[k] = i * 6 + j
    return f


def sym27(v):  # LC4 char index -> 0..25 letters, 26 '_', None otherwise
    ch = AL[v]
    if 'a' <= ch <= 'z': return ord(ch) - 97
    if ch == '_': return 26
    return None


def main():
    args = [a for a in sys.argv[1:]]
    ct, tmpl = args[0], args[1]
    minmsg, th3, th4, maxsol = opt('--minmsg', 25), opt('--th3', 1), opt('--th4', 1), opt('--max', 5)
    C = [AL.index(ch) for ch in ct]; T = len(C)
    cnt3 = np.load('cnt3.npy'); cnt4 = np.load('cnt4.npy')
    pool = IDPool(); cls = []
    X = lambda t, v, k: pool.id(('X', t, v, k))
    M = lambda t, k: pool.id(('M', t, k))
    R = lambda t, r: pool.id(('R', t, r))
    Y = lambda t, y: pool.id(('Y', t, y))
    MV = lambda t, v: pool.id(('MV', t, v))
    PT = lambda t, v: pool.id(('PT', t, v))
    PP = lambda t, k: pool.id(('PP', t, k))
    H = lambda t: pool.id(('H', t))
    TG = lambda t, g: pool.id(('TG', t, g))
    eo = lambda lits: cls.extend(CardEnc.equals(lits=lits, bound=1, vpool=pool, encoding=EncType.seqcounter).clauses)
    RM = {(r, y): rot_map(r, y) for r in range(6) for y in range(6)}
    for t in range(T + 1):
        for v in range(36): eo([X(t, v, k) for k in range(36)])
        for k in range(36): eo([X(t, v, k) for v in range(36)])
        eo([M(t, k) for k in range(36)])
    cls.append([M(0, 0)])
    for k, ch in enumerate(tmpl):
        if ch != '?': cls.append([X(0, AL.index(ch), k)])
    for t in range(T):
        c = C[t]
        eo([R(t, r) for r in range(6)]); eo([Y(t, y) for y in range(6)]); eo([MV(t, v) for v in range(36)])
        eo([PT(t, v) for v in range(36)]); eo([PP(t, k) for k in range(36)])
        for v in range(36):
            for k in range(36):
                cls.append([-PT(t, v), -X(t, v, k), PP(t, k)])
                cls.append([-PP(t, k), -X(t, v, k), PT(t, v)])
        for k in range(36): cls.append([-PP(t, k), R(t, k // 6)])
        for k in range(36):
            for r in range(6):
                cls.append([-X(t, c, k), -R(t, r), Y(t, (k % 6 + (1 if k // 6 == r else 0)) % 6)])
        for K in range(36):
            for v in range(36): cls.append([-M(t, K), -X(t, v, K), MV(t, v)])
        for v in range(36):
            dr, dc = divmod(v, 6)
            for Pc in range(36):
                i, j = divmod(Pc, 6)
                cls.append([-MV(t, v), -PP(t, Pc), X(t, c, ((i + dr) % 6) * 6 + (j + dc) % 6)])
        for (r, y), f in RM.items():
            a, b = R(t, r), Y(t, y)
            for v in range(36):
                for k in range(36): cls.append([-a, -b, -X(t, v, k), X(t + 1, v, f[k])])
            for k in range(36):
                i, j = divmod(f[k], 6)
                cls.append([-a, -b, -M(t, k), M(t + 1, ((i + c // 6) % 6) * 6 + (j + c % 6) % 6)])
    # plaintext language constraints
    for t in range(T - 1): cls.append([-H(t), H(t + 1)])
    for t in range(min(minmsg, T)): cls.append([-H(t)])
    cls.append([H(T - 1)])
    hashv = AL.index('#')
    for t in range(T):
        cls.append([-PT(t, hashv), H(t)])                       # '#' only inside the signature
        if t > 0: cls.append([-H(t), H(t - 1), PT(t, hashv)])  # the signature starts with '#'
        else: cls.append([-H(0), PT(0, hashv)])
        for v in range(36):
            if sym27(v) is None and v != hashv: cls.append([H(t), -PT(t, v)])
    let = [v for v in range(36) if sym27(v) is not None]
    allowed3 = [(a, b, c) for a in range(27) for b in range(27) for c in range(27) if cnt3[(a * 27 + b) * 27 + c] >= th3]
    inv = {sym27(v): v for v in let}
    for t in range(T - 2):
        lits = [H(t + 2)]
        for g, (a, b, c) in enumerate(allowed3):
            v = TG(t, g); lits.append(v)
            cls.append([-v, PT(t, inv[a])]); cls.append([-v, PT(t + 1, inv[b])]); cls.append([-v, PT(t + 2, inv[c])])
            if t + 3 < T:
                nxt = [PT(t + 3, inv[d]) for d in range(27) if cnt4[((a * 27 + b) * 27 + c) * 27 + d] >= th4]
                cls.append([-v, H(t + 3)] + nxt)
        cls.append(lits)
    print('vars', pool.top, 'clauses', len(cls), flush=True)
    s = Cadical153(bootstrap_with=cls); t0 = time.time()
    for n in range(maxsol):
        if not s.solve(): print('UNSAT/no more', '%.0fs' % (time.time() - t0), flush=True); break
        mod = set(l for l in s.get_model() if l > 0)
        pt = ''.join(AL[v] for t in range(T) for v in range(36) if PT(t, v) in mod)
        key = ''.join(next(AL[v] for v in range(36) if X(0, v, k) in mod) for k in range(36))
        print('%.0fs key=%s pt=%s' % (time.time() - t0, key, pt), flush=True)
        s.add_clause([-X(0, AL.index(key[k]), k) for k in range(36)])


if __name__ == '__main__':
    main()
