"""Ciphertext-only simple-substitution solver for the Smolensk letter of 1 June 1633 (AGAD AR dz. II nr 1116).

Reads a transcription (lines 'Lnn word word ...'), splits each word into signs (tokenise), and anneals a
sign -> letter key against a Polish character n-gram model with word spaces (lang/). Several signs may take the
same letter (homophones). Usage: python solve.py <transcription> [restarts] [iters] [model]
"""
import os, sys, random, math, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm


ATTACH = set('34578')  # digits that carry an attached cross; a '+' after any other digit is the free sign


def tokenise(w):
    """Signs: '+0' and '10' -> T (one sign); a digit followed by '+' -> crossed digit; a free '+' -> '1+'."""
    w = w.replace(',', '').replace('?', '').replace('[', '').replace(']', '')
    out, i = [], 0
    while i < len(w):
        c = w[i]
        if c == '+':
            if i + 1 < len(w) and w[i + 1] == '0':
                out.append('T'); i += 2; continue
            out.append('1+'); i += 1; continue
        if c == '1' and i + 1 < len(w) and w[i + 1] == '0':
            out.append('T'); i += 2; continue
        if c in ATTACH and i + 1 < len(w) and w[i + 1] == '+':
            out.append(c + '+'); i += 2; continue
        out.append(c); i += 1
    return out


TOK = 'sign'


def read(path):
    words = []
    for l in open(path, encoding='utf-8'):
        if not l.strip() or l.startswith('#'):
            continue
        parts = l.split()
        for w in parts[1:]:
            t = tokenise(w) if TOK == 'sign' else __import__('teen').tok(w)
            if t:
                words.append(t)
    return words


def main():
    path = sys.argv[1]
    restarts = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    iters = int(sys.argv[3]) if len(sys.argv) > 3 else 20000
    model = sys.argv[4] if len(sys.argv) > 4 else 'pl-1790'
    global TOK
    TOK = sys.argv[5] if len(sys.argv) > 5 else 'sign'
    maxdup = int(sys.argv[6]) if len(sys.argv) > 6 else 99
    words = read(path)
    m = lm.load(model, order=4)
    syms = sorted({t for w in words for t in w})
    sid = {s: i for i, s in enumerate(syms)}
    flat = []
    for w in words:
        flat += [sid[t] for t in w] + [-1]
    letters = 'abcdefghijklmnoprstuwyz'
    li = [m.encode(c)[0] for c in letters]
    sp = m.encode(' ')[0]
    import numpy as np
    flat = np.array(flat)

    def text_idx(key):
        k = np.array(key + [sp])
        return np.concatenate([[sp], k[flat]])

    best_all = None
    for r in range(restarts):
        key = random.sample(li, len(syms)) if len(syms) <= len(li) else [random.choice(li) for _ in syms]
        cur = m.score_idx(text_idx(key))
        best = (cur, key[:])
        T0 = 2.0
        for it in range(iters):
            T = T0 * (1 - it / iters) + 0.01
            k2 = key[:]
            if random.random() < 0.5:
                k2[random.randrange(len(syms))] = random.choice(li)
            else:
                a, b = random.randrange(len(syms)), random.randrange(len(syms))
                k2[a], k2[b] = k2[b], k2[a]
            if max(collections.Counter(k2).values()) > maxdup:
                continue
            s = m.score_idx(text_idx(k2))
            if s > cur or random.random() < math.exp((s - cur) / T):
                key, cur = k2, s
                if cur > best[0]:
                    best = (cur, key[:])
        if best_all is None or best[0] > best_all[0]:
            best_all = best
        inv = {v: k for k, v in zip(letters, li)}
        print(r, round(best[0] / len(flat), 3), ' '.join(f'{s}={inv[best[1][i]]}' for i, s in enumerate(syms)), flush=True)
    inv = {v: k for k, v in zip(letters, li)}
    key = best_all[1]
    print('BEST', round(best_all[0] / len(flat), 3))
    print(' '.join(f'{s}={inv[key[i]]}' for i, s in enumerate(syms)))
    print(' '.join(''.join(inv[key[sid[t]]] for t in w) for w in words))


if __name__ == '__main__':
    main()
