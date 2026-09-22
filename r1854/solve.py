"""Homophonic substitution annealer for the R1854 token transcriptions.

Usage: python r1854/solve.py <tokens.txt> <model> [restarts] [iters] [--fix SIGN=letter ...] [--null SIGN ...]
Each sign maps to one letter; signs given with --null are dropped. Score = shared lang/ n-gram model, no spaces.
"""
import os, sys, random, math
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm


def read_tokens(path, keep_sep=False):
    lines = []
    for l in open(path, encoding='utf-8'):
        if not l.startswith('L') or ':' not in l:
            continue
        lab, rest = l.split(':', 1)
        toks = [t for t in rest.split() if t != '?' and (keep_sep or t != '_')]
        lines.append((lab.strip(), toks))
    return lines


def main():
    args = sys.argv[1:]
    fix, nulls, pos = {}, set(), []
    i = 0
    while i < len(args):
        if args[i] == '--fix':
            i += 1
            while i < len(args) and '=' in args[i]:
                k, v = args[i].split('=', 1); fix[k] = ' ' if v == 'SP' else v; i += 1
        elif args[i] == '--null':
            i += 1
            while i < len(args) and not args[i].startswith('--'):
                nulls.add(args[i]); i += 1
        else:
            pos.append(args[i]); i += 1
    path, model = pos[0], pos[1]
    restarts = int(pos[2]) if len(pos) > 2 else 8
    iters = int(pos[3]) if len(pos) > 3 else 60000
    m = lm.load(model, order=int(os.environ['ORDER']) if os.environ.get('ORDER') else None, spaces=bool(os.environ.get('SPACES')))
    alpha = m.alpha
    lines = read_tokens(path)
    toks = [t for _, ts in lines for t in ts if t not in nulls]
    signs = sorted(set(toks))
    sidx = {s: k for k, s in enumerate(signs)}
    x = np.array([sidx[t] for t in toks])
    # unigram prior for initialisation
    freq = np.array([0.117, .009, .045, .037, .118, .011, .016, .015, .113, .0, .0, .065, .025, .069, .098,
                     .03, .005, .064, .05, .056, .03, .0, .0, .003, .0, .005])
    letters = [c for c in alpha]
    lf = np.array([freq['abcdefghijklmnopqrstuvwxyz'.index(c)] if c != ' ' else 0.15 for c in letters]) + 1e-3
    lf /= lf.sum()
    LAM = float(os.environ.get('LAM', '1.0'))
    logq = np.log(lf)
    N = len(x)
    NMAX = int(os.environ.get('NMAX', '0'))
    NULLC = float(os.environ.get('NULLC', '-3.0'))
    NUL = len(alpha)
    def total(key):
        if NMAX and (key == NUL).sum() > NMAX:
            return -1e12
        y = key[x]
        y = y[y != NUL]
        N = len(y)
        c = np.bincount(y, minlength=len(alpha)) / N
        nz = c > 0
        kl = float((c[nz] * (np.log(c[nz]) - logq[nz])).sum())
        return m.score_idx(y) - LAM * N * kl + NULLC * (len(x) - N)
    fixed = {sidx[k]: alpha.index(v) for k, v in fix.items() if k in sidx}
    best_all = (-1e18, None)
    for r in range(restarts):
        key = np.random.choice(len(alpha), size=len(signs), p=lf)
        if ' ' in alpha: key[key == 0] = alpha.index('e')
        for k, v in fixed.items():
            key[k] = v
        cur = total(key); best = (cur, key.copy())
        T0 = 12.0
        free = [k for k in range(len(signs)) if k not in fixed]
        VOW = set(os.environ.get('VOWELS', '').split(',')) - {''}
        allowed = {}
        if VOW:
            vi = [alpha.index(c) for c in 'aeiou' if c in alpha]
            ci = [alpha.index(c) for c in alpha if c not in 'aeiou ']
            for k in free:
                allowed[k] = vi if signs[k] in VOW else ci
                key[k] = random.choice(allowed[k])
        for it in range(iters):
            T = T0 * (1 - it / iters) + 0.2
            k = random.choice(free); k2 = k
            ok, ok2 = key[k], key[k]
            if random.random() < 0.8:
                key[k] = random.choice(allowed[k]) if allowed else random.randrange(1 if ' ' in alpha else 0, len(alpha) + (1 if NMAX else 0))
            else:
                k2 = random.choice(free); ok2 = key[k2]
                if allowed and (key[k2] not in allowed[k] or key[k] not in allowed[k2]): k2 = k; ok2 = key[k]
                key[k], key[k2] = key[k2], key[k]
            new = total(key)
            if new >= cur or random.random() < math.exp((new - cur) / T):
                cur = new
                if cur > best[0]:
                    best = (cur, key.copy())
            else:
                key[k2] = ok2; key[k] = ok
        # note: swap undo handled by restoring from snapshot below
        per = best[0] / len(x)
        print(f'restart {r}: {per:.3f}/char', flush=True)
        if best[0] > best_all[0]:
            best_all = best
    key = best_all[1]
    A2 = alpha + '_'
    print('best per char', best_all[0] / len(x))
    print('key:', ' '.join(f'{s}={A2[key[sidx[s]]]}' for s in signs))
    for lab, ts in lines:
        print(lab, ''.join(A2[key[sidx[t]]] if t in sidx else '.' for t in ts if t not in nulls))


if __name__ == '__main__':
    main()
