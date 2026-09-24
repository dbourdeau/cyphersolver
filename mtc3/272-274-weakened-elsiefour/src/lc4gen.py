"""General SAT model of LC4 (Kaminsky) for key recovery.

Each message is a list of steps; at every step the plaintext char and/or the ciphertext char may be known ('?' = unknown).
All messages start from the same key with the marker at (0,0). Language constraints (letters/'_' plus corpus 3/4-grams,
signature after '#') can be switched on for a message's unknown plaintext.
usage (python): see solve() below; CLI: python lc4gen.py spec.json
spec: {"key": "36-char template", "msgs": [{"p": "...", "c": "...", "lang": false, "minmsg": 25}], "max": 3}
"""
import os, site, sys, time, json
os.add_dll_directory(os.path.join(site.getsitepackages()[-1], 'z3', 'lib'))
import numpy as np
from pysat.solvers import Cadical153, Glucose4, Solver
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool

AL = "#_23456789abcdefghijklmnopqrstuvwxyz"


def rot_map(r, y):
    f = {}
    for k in range(36):
        i, j = divmod(k, 6)
        if i == r: j = (j + 1) % 6
        if j == y: i = (i + 1) % 6
        f[k] = i * 6 + j
    return f


RM = {(r, y): rot_map(r, y) for r in range(6) for y in range(6)}


def sym27(v):
    ch = AL[v]
    if 'a' <= ch <= 'z': return ord(ch) - 97
    if ch == '_': return 26
    return None


def solve(spec, log=print):
    pool = IDPool(); cls = []
    eo = lambda lits: cls.extend(CardEnc.equals(lits=lits, bound=1, vpool=pool, encoding=EncType.seqcounter).clauses)
    K0 = lambda v, k: pool.id(('K', v, k))
    for v in range(36): eo([K0(v, k) for k in range(36)])
    for k in range(36): eo([K0(v, k) for v in range(36)])
    for k, ch in enumerate(spec.get('key', '?' * 36)):
        if ch != '?': cls.append([K0(AL.index(ch), k)])
    msgvars = []
    for m, msg in enumerate(spec['msgs']):
        P, Cs = msg['p'], msg['c']; T = len(Cs)
        X = lambda t, v, k, m=m: K0(v, k) if t == 0 else pool.id(('X', m, t, v, k))
        M = lambda t, k, m=m: pool.id(('M', m, t, k))
        R = lambda t, r, m=m: pool.id(('R', m, t, r))
        Y = lambda t, y, m=m: pool.id(('Y', m, t, y))
        MV = lambda t, v, m=m: pool.id(('MV', m, t, v))
        PT = lambda t, v, m=m: pool.id(('PT', m, t, v))
        CT = lambda t, v, m=m: pool.id(('CT', m, t, v))
        PP = lambda t, k, m=m: pool.id(('PP', m, t, k))
        CP = lambda t, k, m=m: pool.id(('CP', m, t, k))
        for t in range(1, T + 1):
            for v in range(36): eo([X(t, v, k) for k in range(36)])
            for k in range(36): eo([X(t, v, k) for v in range(36)])
        for t in range(T + 1): eo([M(t, k) for k in range(36)])
        cls.append([M(0, 0)])
        for t in range(T):
            eo([R(t, r) for r in range(6)]); eo([Y(t, y) for y in range(6)]); eo([MV(t, v) for v in range(36)])
            eo([PT(t, v) for v in range(36)]); eo([CT(t, v) for v in range(36)])
            eo([PP(t, k) for k in range(36)]); eo([CP(t, k) for k in range(36)])
            if P[t] != '?': cls.append([PT(t, AL.index(P[t]))])
            if Cs[t] != '?': cls.append([CT(t, AL.index(Cs[t]))])
            pk, ck = P[t] != '?', Cs[t] != '?'
            for v in range(36):
                if pk and v != AL.index(P[t]): pass
                else:
                    for k in range(36):
                        cls.append([-PT(t, v), -X(t, v, k), PP(t, k)])
                        cls.append([-PP(t, k), -X(t, v, k), PT(t, v)])
                if ck and v != AL.index(Cs[t]): pass
                else:
                    for k in range(36):
                        cls.append([-CT(t, v), -X(t, v, k), CP(t, k)])
                        cls.append([-CP(t, k), -X(t, v, k), CT(t, v)])
            for k in range(36): cls.append([-PP(t, k), R(t, k // 6)])
            for k in range(36):
                for r in range(6):
                    cls.append([-CP(t, k), -R(t, r), Y(t, (k % 6 + (1 if k // 6 == r else 0)) % 6)])
            for Kc in range(36):
                for v in range(36): cls.append([-M(t, Kc), -X(t, v, Kc), MV(t, v)])
            for v in range(36):
                dr, dc = divmod(v, 6)
                for Pc in range(36):
                    i, j = divmod(Pc, 6)
                    cls.append([-MV(t, v), -PP(t, Pc), CP(t, ((i + dr) % 6) * 6 + (j + dc) % 6)])
            cvals = [AL.index(Cs[t])] if ck else list(range(36))
            for (r, y), f in RM.items():
                a, b = R(t, r), Y(t, y)
                for v in range(36):
                    for k in range(36):
                        cls.append([-a, -b, -X(t, v, k), X(t + 1, v, f[k])])
                        if spec.get('bwd'): cls.append([-a, -b, X(t, v, k), -X(t + 1, v, f[k])])
                for k in range(36):
                    i, j = divmod(f[k], 6)
                    for c in cvals:
                        nk = ((i + c // 6) % 6) * 6 + (j + c % 6) % 6
                        cls.append([-a, -b, -M(t, k), M(t + 1, nk)] + ([] if ck else [-CT(t, c)]))
        if msg.get('lang'):
            add_lang(pool, cls, PT, T, msg.get('minmsg', 25), msg.get('start', 0))
        msgvars.append((PT, CT, T))
    log('vars %d clauses %d' % (pool.top, len(cls)))
    s = Solver(name=spec.get('solver', 'cadical153'), bootstrap_with=cls); t0 = time.time(); out = []
    for n in range(spec.get('max', 2)):
        if not s.solve():
            log('no (more) solutions %.0fs' % (time.time() - t0)); break
        mod = set(l for l in s.get_model() if l > 0)
        key = ''.join(next(AL[v] for v in range(36) if K0(v, k) in mod) for k in range(36))
        texts = []
        for PT, CT, T in msgvars:
            texts.append((''.join(AL[v] for t in range(T) for v in range(36) if PT(t, v) in mod),
                          ''.join(AL[v] for t in range(T) for v in range(36) if CT(t, v) in mod)))
        log('%.0fs key=%s' % (time.time() - t0, key))
        for p, c in texts: log('   p=%s\n   c=%s' % (p, c))
        out.append((key, texts))
        s.add_clause([-K0(AL.index(key[k]), k) for k in range(36)])
    return out


def add_lang(pool, cls, PT, T, minmsg, start):
    """language constraints on steps start..T-1 (steps before 'start' are a nonce)."""
    cnt3 = np.load('cnt3.npy'); cnt4 = np.load('cnt4.npy')
    H = lambda t: pool.id(('H', id(PT), t)); TG = lambda t, g: pool.id(('TG', id(PT), t, g))
    hashv = AL.index('#')
    for t in range(start, T - 1): cls.append([-H(t), H(t + 1)])
    for t in range(start, min(start + minmsg, T)): cls.append([-H(t)])
    cls.append([H(T - 1)])
    for t in range(start, T):
        cls.append([-PT(t, hashv), H(t)])
        cls.append([-H(t), H(t - 1), PT(t, hashv)] if t > start else [-H(t), PT(t, hashv)])
        for v in range(36):
            if sym27(v) is None and v != hashv: cls.append([H(t), -PT(t, v)])
    inv = {sym27(v): v for v in range(36) if sym27(v) is not None}
    allowed3 = [(a, b, c) for a in range(27) for b in range(27) for c in range(27) if cnt3[(a * 27 + b) * 27 + c] >= 1]
    for t in range(start, T - 2):
        lits = [H(t + 2)]
        for g, (a, b, c) in enumerate(allowed3):
            v = TG(t, g); lits.append(v)
            cls.append([-v, PT(t, inv[a])]); cls.append([-v, PT(t + 1, inv[b])]); cls.append([-v, PT(t + 2, inv[c])])
            if t + 3 < T:
                nxt = [PT(t + 3, inv[d]) for d in range(27) if cnt4[((a * 27 + b) * 27 + c) * 27 + d] >= 1]
                cls.append([-v, H(t + 3)] + nxt)
        cls.append(lits)


if __name__ == '__main__':
    spec = json.load(open(sys.argv[1]))
    solve(spec, log=lambda s: print(s, flush=True))
