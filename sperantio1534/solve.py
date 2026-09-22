"""Refine the System L key on the two Sperantio letters.

f.248 is Latin, f.250-251 German; one key serves both, so the score is the sum of the
Latin model over the Latin pages and the de-1500s model over the German ones.
Hill-climbing over sign->value assignments, seeded with key.txt; the values read from
the f.248r gloss and the clear passages are pinned (PINNED).
"""
import os
import random
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm

import dec

HERE = os.path.dirname(os.path.abspath(__file__))
LATIN = {'248r', '248v'}
VALUES = list('abcdefghilmnopqrstuz')  # single letters only: output length stays fixed
PINNED = {'X', 'N', 'R', 'x', 'w', '3', 'v', 'y', 'q', 'm', '5', '7', '9', 'P'}


def texts():
    """[(page, [tokens per line])]; clear passages are kept as fixed strings."""
    out = []
    for pg, n, s in dec.lines(os.path.join(HERE, 'transcription.txt')):
        out.append((pg, dec.tokens(s)))
    return out


def render(rows, key, latin):
    buf = []
    for pg, toks in rows:
        if (pg in LATIN) != latin:
            continue
        for t in toks:
            if t.startswith('['):
                buf.append(' ' + t[1:-1].lower() + ' ')
            elif t == ':':
                buf.append(' ')
            else:
                v = key.get(t, '')
                buf.append('' if v == '_' else v)
        buf.append(' ')
    return ''.join(buf)


def main():
    rows = texts()
    key = dec.load_key(os.path.join(HERE, 'key.txt'))
    signs = sorted({t for _, toks in rows for t in toks if not t.startswith('[') and t != ':'})
    for s in signs:
        key.setdefault(s, '?')
    free = [s for s in signs if s not in PINNED]
    mla, mde = lm.load('la'), lm.load('de-1500s')

    def score(k):
        la = mla.per_char(lm.norm(render(rows, k, True), 'latin'))
        de = mde.per_char(lm.norm(render(rows, k, False), 'early'))
        return la + de

    best = score(key)
    print('seed %.4f  (%d signs, %d free)' % (best, len(signs), len(free)))
    rng = random.Random(7)
    for it in range(60):
        improved = False
        for s in free:
            cur = key[s]
            for v in VALUES:
                if v == cur:
                    continue
                key[s] = v
                sc = score(key)
                if sc > best + 1e-9:
                    best, cur, improved = sc, v, True
                else:
                    key[s] = cur
        print('pass %2d  %.4f' % (it, best))
        if not improved:
            break
        rng.shuffle(free)
    with open(os.path.join(HERE, 'key_refined.txt'), 'w', encoding='utf-8') as f:
        f.write('# refined by solve.py; score %.4f\n' % best)
        f.write(','.join('%s=%s' % (k, v) for k, v in sorted(key.items())) + '\n')


if __name__ == '__main__':
    main()
