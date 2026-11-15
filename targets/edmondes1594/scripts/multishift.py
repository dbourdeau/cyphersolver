"""Test: the cipher is a Caesar substitution on the 24-letter alphabet (no j, no v) with several shifts in use
("alphabets"), the choice of alphabet not shown in the print. Each printed letter is read with one of the shifts in
SET; the best reading under the 1590s quadgram model is found exactly by dynamic programming.

Printed v is taken as the cipher letter u, and printed u as the cipher letter n (n/u and u/v confusion in reading a
secretary hand), unless --raw-uv is given.

Usage: python3 -I multishift.py SHIFTS [--shuffle SEED] [--show] [--ct FILE] [--segs LO-HI]
   e.g. multishift.py 7,8,10 --show
"""
import sys, os, argparse, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lm, poly
A = lm.PA  # abcdefghiklmnopqrstuwxyz

def prep(s, raw_uv=False):
    if raw_uv: return s.replace('v', 'u')
    return ''.join({'v': 'u', 'u': 'n'}.get(c, c) for c in s)

def options(c, shifts):
    i = A.index(c)
    return tuple(dict.fromkeys(A[(i + k) % 24] for k in shifts))

def run(segs, shifts, raw_uv=False):
    key = {c: options(c, shifts) for c in A}
    tot = 0.0; n = 0; outs = []
    for s in segs:
        s2 = prep(s, raw_uv)
        sc, txt = poly.best_reading(s2, key)
        tot += sc; n += max(1, len(s2) - 3); outs.append(txt)
    return tot / n, outs

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('shifts')
    ap.add_argument('--shuffle', type=int, default=0)
    ap.add_argument('--show', action='store_true')
    ap.add_argument('--raw-uv', action='store_true')
    ap.add_argument('--ct', default=os.path.join(HERE, '..', 'transcription', 'pass1.txt'))
    a = ap.parse_args()
    segs, labels = poly.read_ct(a.ct)
    if a.shuffle:
        allc = list(''.join(segs)); random.Random(a.shuffle).shuffle(allc)
        it = iter(allc); segs = [''.join(next(it) for _ in s) for s in segs]
    shifts = [int(x) for x in a.shifts.split(',')]
    sc, outs = run(segs, shifts, a.raw_uv)
    print(f'shifts={shifts} score={sc:.4f} shuffle={a.shuffle}')
    if a.show:
        for lab, s, t in zip(labels, segs, outs):
            # mark which shift was used per letter
            s2 = prep(s, a.raw_uv)
            marks = ''.join(str((A.index(p) - A.index(c)) % 24 % 10) for c, p in zip(s2, t))
            print(f'{lab:6s} {t}\n       {marks}')
