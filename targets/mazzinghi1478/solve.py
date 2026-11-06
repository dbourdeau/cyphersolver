"""Homophonic-substitution annealer for the Mazzinghi cipher (MAP 89/142), scored on it-cinquecento (order 5, spaces).

Usage: python solve.py <transcription> [restarts] [--fix g=l,g=l,...] [--control]
Cipher words are the space-separated tokens outside [...] that hold no '?' and are not numbers.
Each glyph maps to one plaintext letter; several glyphs may share a letter (homophones).
--control enciphers a clear Italian passage of the same length with a random key in the same glyph count and solves it.
"""
import os, sys, re, random, math
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm

M = lm.load('it-cinquecento')
A = M.alpha
SP = M.index[' ']
LET = [c for c in A if c != ' ' and c not in 'jvkwxy']
RANK = 'eaiontrlscdupmgfbhqz'
_F = dict(e=11.8, a=11.7, i=11.3, o=9.8, n=6.9, r=6.4, t=5.6, l=6.5, s=5.0, c=4.5, d=3.7, u=3.0, p=3.0, m=2.5, g=1.6,
          f=1.1, b=0.9, h=1.2, q=0.5, z=0.5)
UNI = np.full(M.A, 1e-3)
for _c, _v in _F.items():
    UNI[M.index[_c]] = _v / 100
UNI /= UNI.sum()
KLW = 3.0


def words_of(path):
    out = []
    for l in open(path, encoding='utf-8'):
        if l.startswith('#') or not l.strip():
            continue
        l = re.sub(r'\[[^\]]*\]', ' ', l[3:])
        out += [w for w in l.split() if '?' not in w and not re.fullmatch(r'[\d/]+', w)]
    return out


def solve(words, restarts=20, iters=40000, fix=None, seed=0):
    fix = fix or {}
    glyphs = sorted(set(''.join(words)))
    gi = {g: i for i, g in enumerate(glyphs)}
    stream = []
    for w in words:
        stream += [-1] + [gi[g] for g in w]
    stream += [-1]
    stream = np.array(stream)
    is_sp = stream < 0
    free = [g for g in glyphs if g not in fix]
    cnt = {g: sum(w.count(g) for w in words) for g in glyphs}
    rng = random.Random(seed)
    k, Aa = M.order, M.A

    gcnt = np.array([cnt[g] for g in glyphs], dtype=float)
    ntot = gcnt.sum()

    def score(key):
        # KL penalty against Italian letter frequencies keeps homophones from collapsing onto one letter
        obs = np.bincount(key, weights=gcnt, minlength=Aa) / ntot
        nz = obs > 0
        kl = float((obs[nz] * np.log(obs[nz] / UNI[nz])).sum())
        x = np.where(is_sp, SP, key[np.maximum(stream, 0)])
        ctx = np.zeros(len(x) - k + 1, dtype=np.int64)
        for j in range(k):
            ctx = ctx * Aa + x[j:len(x) - k + 1 + j]
        return float(M.lp[ctx].sum()) - KLW * ntot * kl

    best = (-1e18, None)
    for r in range(restarts):
        # start from a frequency-rank key with some noise
        order = sorted(free, key=lambda g: -cnt[g])
        key = np.zeros(len(glyphs), dtype=np.int64)
        for g in glyphs:
            key[gi[g]] = M.index[fix[g]] if g in fix else 0
        for i, g in enumerate(order):
            key[gi[g]] = M.index[RANK[min(len(RANK) - 1, max(0, i + rng.randint(-2, 2)))]]
        cur = score(key)
        T0 = 30.0
        for it in range(iters):
            T = T0 * (1 - it / iters) + 0.2
            g = gi[rng.choice(free)]
            old = key[g]
            if rng.random() < 0.5 and len(free) > 1:
                h = gi[rng.choice(free)]
                oh = key[h]
                key[g], key[h] = oh, old
            else:
                h, oh = None, None
                key[g] = M.index[rng.choice(LET)]
            s = score(key)
            if s >= cur or rng.random() < math.exp((s - cur) / T):
                cur = s
            else:
                key[g] = old
                if h is not None:
                    key[h] = oh
        if cur > best[0]:
            best = (cur, key.copy())
        print(f'restart {r}: {cur:.1f}  best {best[0]:.1f}', file=sys.stderr)
    key = {g: A[best[1][gi[g]]] for g in glyphs}
    n = int((~is_sp).sum())
    return best[0] / n, key


def decode(words, key):
    return ' '.join(''.join(key[g] for g in w) for w in words)


if __name__ == '__main__':
    path = sys.argv[1]
    restarts = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 20
    fix = {}
    if '--fix' in sys.argv:
        for kv in sys.argv[sys.argv.index('--fix') + 1].split(','):
            g, l = kv.split('=')
            fix[g] = l
    words = words_of(path)
    if '--control' in sys.argv:
        clear = ("io ti scrissi per l ultima mia quanto era seguito qui di questa materia et come el papa haveva "
                 "publicato el breve contro e fiorentini et di poi non e seguito altro se non che si dice che el conte "
                 "girolamo manda gente verso perugia et che el re ferrando vuole che el duca di calavria venga in toscana "
                 "con le sue genti el papa sta di mala voglia et dice che non vuole pace se lorenzo non viene a roma a "
                 "chiedergli perdono io ho parlato con monsignore di novara et con lo ambasciatore di milano e quali mi "
                 "dicono che faranno ogni cosa per bene della citta ma che bisogna avere patientia et aspettare quello "
                 "che fara el re di francia el quale ha mandato qui uno suo huomo").split()
        glyphs = sorted(set(''.join(words)))
        letters = sorted(set(''.join(clear)))
        # homophonic key with the same number of glyphs as the real letter: frequent letters get two or three signs
        rng = random.Random(7)
        pool = letters + [c for c in 'eaoint' for _ in range(2)]
        pool = pool[:len(glyphs)] if len(pool) >= len(glyphs) else pool + list('eaoi') * 5
        signs = {c: [] for c in letters}
        for i, c in enumerate(pool[:len(glyphs)]):
            signs[c].append(chr(0x100 + i))
        ctw, total = [], 0
        target = sum(len(w) for w in words)
        for w in clear:
            if total >= target:
                break
            ctw.append(''.join(rng.choice(signs[c]) if signs[c] else c for c in w))
            total += len(w)
        sc, key = solve(ctw, restarts)
        dec = decode(ctw, key)
        ok = sum(a == b for a, b in zip(dec, ' '.join(clear)[:len(dec)]))
        print(f'control: {total} signs, {len(set("".join(ctw)))} glyphs, per-char {sc:.3f}, letters right {ok}/{len(dec)}')
        print(dec[:600])
        sys.exit()
    sc, key = solve(words, restarts, fix=fix)
    print(f'per-char {sc:.3f}')
    print(' '.join(f'{g}={l}' for g, l in sorted(key.items())))
    print(decode(words, key))
