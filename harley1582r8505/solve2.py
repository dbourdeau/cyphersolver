"""Annealer where each sign may stand for a letter, a common French syllable, a double, or a null.

usage: [W=..] python solve2.py restarts iters [fixed.json]
"""
import sys, os, json, random, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm
import numpy as np
from solve import load_runs

M = lm.load('fr-1530-despatches', order=5, spaces=False)

LETTERS = list('abcdefghilmnopqrstuxy')
SYL = ['le','la','de','re','se','te','ne','me','ce','pe','be','ve','en','on','an','in','un','ou',
       'qu','ur','er','es','et','ar','or','ai','ei','au','eu','ie','io','ra','ro','ri','li','lo',
       'ta','to','ti','na','no','ni','ma','mo','mi','sa','so','si','ca','co','ci','pa','po','pi',
       'da','do','di','ss','ll','tt','mm','nn','ee','rr','ff','pp','ion','ent','men','par','pou']
VALUES = LETTERS + SYL


def main():
    R = int(sys.argv[1]); IT = int(sys.argv[2])
    fixed = json.load(open(sys.argv[3])) if len(sys.argv) > 3 else {}
    runs = [r for r in load_runs() if len(r) >= 3]
    signs = sorted({s for r in runs for s in r})
    si = {s: i for i, s in enumerate(signs)}
    seq = [[si[s] for s in r] for r in runs]
    occ = [[j for j, r in enumerate(seq) if i in r] for i in range(len(signs))]
    free = [i for i, s in enumerate(signs) if s not in fixed]
    W = float(os.environ.get('W', '0.3'))
    print(len(signs), 'signs', sum(len(r) for r in seq), 'tokens', file=sys.stderr)

    def txt(key, r):
        return ''.join(key[i] for i in r)

    def sc(key, r):
        return M.score(txt(key, r))

    def lenpen(key):
        # keep the expansion sane: mean value length near 1.6 chars
        m = sum(len(key[i]) for i in free) / max(1, len(free))
        return (m - 1.6) ** 2

    best_all = None
    for rs in range(R):
        key = [fixed.get(s, random.choice(VALUES)) for s in signs]
        rsc = [sc(key, r) for r in seq]
        cur = sum(rsc) - W * 1000 * lenpen(key)
        best = (cur, list(key))
        for it in range(IT):
            T = 4.0 * (1 - it / IT) + 0.05
            i = random.choice(free); old = key[i]
            key[i] = random.choice(VALUES)
            if key[i] == old: continue
            js = occ[i]; ns = [sc(key, seq[j]) for j in js]
            new = sum(rsc) - sum(rsc[j] for j in js) + sum(ns) - W * 1000 * lenpen(key)
            if new >= cur or random.random() < math.exp((new - cur) / T):
                cur = new
                for j, v in zip(js, ns): rsc[j] = v
                if cur > best[0]: best = (cur, list(key))
            else:
                key[i] = old
        print('restart', rs, round(best[0], 1), file=sys.stderr)
        if best_all is None or best[0] > best_all[0]: best_all = best
    key = best_all[1]
    print(json.dumps({s: key[i] for i, s in enumerate(signs)}, sort_keys=True))
    for r in seq:
        print(txt(key, r))


if __name__ == '__main__':
    main()
