"""Decode R91 with Meister 1906 key no. 1 ("Cifra data a Monsig. Montepulciano", 1539-42, Chigi M II 49), as printed.

Polyphonic digits, two-digit syllables, 1 = null written at the end of every word (read as a space).
The DECODE transcript records no dots, so the dotted syllables (sa se si so: dot over the preceding digit; ra re ri ro)
are invisible and fall back to the plain digit values. Beam decode with the it-cinquecento 5-gram (with spaces).

  python key1.py [--B 64] [--show]
"""
import argparse, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
from lang import lm
from parse_r91 import lines

KEY1 = {
    '8': ['a', 'c'], '6': ['e', 'u'], '4': ['i', 'd'], '2': ['o', 't'], '7': ['b', 'f', 'g'], '5': ['l', 'n'],
    '3': ['p', 'r', 'z'], '0': ['m', 's'], '1': [' '],
    '49': ['da'], '69': ['de'], '89': ['do'],
    '24': ['na'], '26': ['ne'], '28': ['ni'], '29': ['no'],
    '94': ['che'], '9': ['chi'], '92': ['non'],
    '96': ['ta'], '98': ['te'], '99': ['ti'],
    '82': ['qua'], '84': ['que'], '86': ['qui'],
}


def beam_decode(d, key, m, B=64, unitpen=0.0, skippen=15.0):
    """d: digit string. key: code -> list of outputs. Returns (score, [(code, output)])."""
    A = m.A; k = m.order; Ak = A ** (k - 1)
    sp = m.index.get(' ', 0)
    beams = [dict() for _ in range(len(d) + 1)]
    ctx0 = 0
    for _ in range(k - 1):
        ctx0 = ctx0 * A + sp
    beams[0][ctx0] = (0.0, None)
    lp = m.lp
    for i in range(len(d)):
        cur = beams[i]
        if not cur:
            continue
        if len(cur) > B:
            cur = dict(sorted(cur.items(), key=lambda kv: -kv[1][0])[:B]); beams[i] = cur
        for ctx, (s, bp) in cur.items():
            for L in (1, 2):
                code = d[i:i + L]
                if len(code) < L or code not in key:
                    continue
                for out in key[code]:
                    c, sc = ctx, s - unitpen
                    for ch in out:
                        x = c * A + m.index[ch]
                        sc += lp[x]; c = x % Ak
                    nb = beams[i + L]
                    if c not in nb or nb[c][0] < sc:
                        nb[c] = (sc, (i, ctx, code, out))
            if skippen is not None:
                nb = beams[i + 1]
                if ctx not in nb or nb[ctx][0] < s - skippen:
                    nb[ctx] = (s - skippen, (i, ctx, d[i], '#'))
    end = beams[len(d)]
    ctx, (s, bp) = max(end.items(), key=lambda kv: kv[1][0])
    path = []
    j = len(d)
    while bp is not None:
        i, pctx, code, out = bp
        path.append((code, out))
        j = i; s2, bp = beams[i][pctx]
    return s, path[::-1]


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--B', type=int, default=64)
    a = ap.parse_args()
    m = lm.load('it-cinquecento')
    d = ''.join(t[0] for _, _, toks, _ in lines() for t in toks)
    s, path = beam_decode(d, KEY1, m, a.B)
    text = ''.join(o for _, o in path)
    print(f'score {s:.1f}  per char {s / len(text):.3f}  chars {len(text)}')
    print(text)
