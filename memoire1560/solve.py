"""Many-to-one (homophonic) substitution annealer that keeps the manuscript word division.

Each cipher sign maps to one plaintext letter (several signs may share a letter). Score = fr-1530-despatches
5-gram log-probability of the decrypt with word spaces.

usage: python solve.py [restarts] [iters] [--fix a=b,c=d] [--merge rx,nN] [--pages 152r,152v]
"""
import os, sys, re, glob, math, random
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm

HERE = os.path.dirname(os.path.abspath(__file__))
# multi-sign units collapsed to one symbol before solving (set with --units zo=U,pp=P)
UNITS = {}


def load_ct(pages=None, merge=()):
    words = []
    for fn in sorted(glob.glob(os.path.join(HERE, 'transcription', 'f*.txt')) + glob.glob(os.path.join(HERE, 'transcription', '1*.txt'))):
        fol = os.path.basename(fn).lstrip('f')[:-4]
        if pages and fol not in pages:
            continue
        for line in open(fn, encoding='utf8'):
            line = line.split('#')[0].strip()
            if not line or line.startswith('MARGIN'):
                continue
            line = re.sub(r'\[[^\]]*\]', ' ', line).replace('=', '')
            for w in line.split():
                for a, b in merge:
                    w = w.replace(a, b)
                for u, c in UNITS.items():
                    w = w.replace(u, c)
                w = w.replace('?', '')
                if w:
                    words.append(w)
    return words


def main():
    args = sys.argv[1:]
    fix, merge, pages = {}, [], None
    if '--fix' in args:
        i = args.index('--fix'); fix = dict(p.split('=') for p in args[i + 1].split(',')); del args[i:i + 2]
    if '--merge' in args:
        i = args.index('--merge'); merge = [(p[0], p[1]) for p in args[i + 1].split(',')]; del args[i:i + 2]
    if '--units' in args:
        i = args.index('--units'); UNITS.update(dict(p.split('=') for p in args[i + 1].split(','))); del args[i:i + 2]
    if '--pages' in args:
        i = args.index('--pages'); pages = set(args[i + 1].split(',')); del args[i:i + 2]
    restarts = int(args[0]) if args else 8
    iters = int(args[1]) if len(args) > 1 else 40000
    words = load_ct(pages, merge)
    text = ' '.join(words)
    signs = sorted(set(text) - {' '})
    print(len(words), 'words', len(text.replace(' ', '')), 'signs', len(signs), 'distinct:', ''.join(signs))
    freq = {s: text.count(s) for s in signs}
    print(' '.join(f'{s}:{freq[s]}' for s in sorted(signs, key=lambda s: -freq[s])))
    m = lm.load('fr-1530-despatches')
    A = m.alpha                      # ' ' + letters
    letters = [c for c in A if c != ' ']
    sidx = {s: i for i, s in enumerate(signs)}
    ct = np.array([sidx[c] if c != ' ' else -1 for c in ' ' + text + ' '])
    space = m.index[' ']
    # letter prior for initialisation: French frequencies
    fr = 'eeeeeeeeeeeeesssssssssaaaaaaaaiiiiiiiitttttttnnnnnnnrrrrrrruuuuuuulllllloooooddddcccpppmmmqqgfbhxyz'
    fixed = {s: m.index[v] for s, v in fix.items() if s in sidx}

    def decrypt(key):
        return np.where(ct < 0, space, key[np.maximum(ct, 0)])

    best_all = None
    for r in range(restarts):
        key = np.array([m.index[random.choice(fr)] for _ in signs])
        for s, v in fixed.items():
            key[sidx[s]] = v
        cur = m.score_idx(decrypt(key)); best = (cur, key.copy())
        T0 = 12.0
        free = [i for s, i in sidx.items() if s not in fixed]
        for it in range(iters):
            T = T0 * (1 - it / iters) + 0.2
            k2 = key.copy()
            if random.random() < 0.7:
                k2[random.choice(free)] = m.index[random.choice(letters)]
            else:
                a, b = random.sample(free, 2); k2[a], k2[b] = k2[b], k2[a]
            sc = m.score_idx(decrypt(k2))
            if sc > cur or random.random() < math.exp((sc - cur) / T):
                key, cur = k2, sc
                if cur > best[0]:
                    best = (cur, key.copy())
        pt = ''.join(A[i] for i in decrypt(best[1]))
        print(f'restart {r}: {best[0]:.0f}  per-char {best[0] / len(pt):.3f}')
        print('  ', pt[:300])
        if best_all is None or best[0] > best_all[0]:
            best_all = best
    key = best_all[1]
    print('KEY', ' '.join(f'{s}={A[key[sidx[s]]]}' for s in sorted(signs, key=lambda s: -freq[s])))
    open(os.path.join(HERE, 'solve_best.txt'), 'w', encoding='utf8').write(
        'KEY ' + ' '.join(f'{s}={A[key[sidx[s]]]}' for s in signs) + '\n' + ''.join(A[i] for i in decrypt(key)) + '\n')


if __name__ == '__main__':
    main()
