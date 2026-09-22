"""Word-aware scoring: best segmentation of a letter string under the spaced it-cinquecento model (beam search),
and coordinate ascent over chosen signs. python spaced.py key.json [sign,sign,...]"""
import os, sys, json, math
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm
from solve import load_segments

M = lm.load('it-cinquecento', order=5, spaces=True)
A, K = M.A, M.order
SP = M.index[' ']


def seg_score(text, beam=24):
    """max over space insertions of log P(' ' + text-with-spaces + ' ')."""
    lp = M.lp
    # state: tuple of last K-1 indices, score, string
    states = [((SP,) * (K - 1), 0.0, '')]
    for ch in text:
        c = M.index[ch]
        nxt = {}
        for ctx, s, st in states:
            for ins in (False, True):
                cc, sc, ss = ctx, s, st
                if ins:
                    if cc[-1] == SP:
                        continue
                    sc += lp[sum(v * A ** (K - 1 - j) for j, v in enumerate(cc + (SP,)))]
                    cc = cc[1:] + (SP,); ss += ' '
                sc += lp[sum(v * A ** (K - 1 - j) for j, v in enumerate(cc + (c,)))]
                cc = cc[1:] + (c,); ss += ch
                if cc not in nxt or nxt[cc][0] < sc:
                    nxt[cc] = (sc, ss)
        states = sorted(((k, v[0], v[1]) for k, v in nxt.items()), key=lambda z: -z[1])[:beam]
    best = max(states, key=lambda z: z[1] + lp[sum(v * A ** (K - 1 - j) for j, v in enumerate(z[0] + (SP,)))])
    return best[1], best[2]


def decode(key, segs):
    return [''.join(key[t] for t in s if key[t] != '.') for s in segs]


def total(key, segs):
    tot = 0; outs = []
    for t in decode(key, segs):
        s, st = seg_score(t); tot += s; outs.append(st)
    return tot, outs


if __name__ == '__main__':
    key = json.load(open(sys.argv[1]))
    segs = load_segments()
    signs = sys.argv[2].split(',') if len(sys.argv) > 2 else []
    cur, outs = total(key, segs)
    print('%.1f' % cur); [print('  ', o) for o in outs]
    letters = os.environ.get('LET','abcdefghilmnopqrstuz.')
    for rnd in range(2):
        for t in signs:
            res = []
            for c in letters:
                k2 = dict(key); k2[t] = c
                res.append((total(k2, segs)[0], c))
            res.sort(reverse=True)
            print(t, 'was', key[t], ' '.join('%s%.1f' % (c, s - res[0][0]) for s, c in res[:5]), flush=True)
            key[t] = res[0][1]
    cur, outs = total(key, segs)
    print('%.1f' % cur); [print('  ', o) for o in outs]
    json.dump(key, open(os.environ.get('OUT', 'key_spaced.json'), 'w'))
