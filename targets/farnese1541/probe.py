"""Reading aid for the third pass: show a line's digits with dots, list the best local decodes, or test a crib.

  python probe.py show 64v.12            digits with global index, ^ = dot, ? = unsure, _ = lost
  python probe.py top 64v.12 [a b] [K]   best K decodes of positions a..b (line-relative) under k2d + dots
  python probe.py fit 64v.12 "parola"    every place in the line (and the next) where the crib encodes the digits

Dotted codes are allowed where the reread marks a dot on the code's first digit or the digit before it; elsewhere
they are offered with a '*' (no dot seen). 11 is the null. Lost digits ('_') match any one-digit code.
"""
import sys, re
import vdot, k2d
from align91 import build_options
from wordcov91 import segment
sys.path.insert(0, '../..')
from lang import lm

S = vdot.stream()
FLAT = []                      # (label, linepos, digit or -1, dot, unsure)
for lab, ts, rr in S:
    for k, (d, dot, uns) in enumerate(ts):
        FLAT.append((lab, k + 1, d, dot, uns))
PLAIN, DOTTED = build_options(k2d.KEY)


def span(lab, a=None, b=None, extra=0):
    idx = [i for i, t in enumerate(FLAT) if t[0] == lab]
    i0, i1 = idx[0], idx[-1] + 1
    if a is not None:
        i0, i1 = idx[0] + a - 1, idx[0] + b
    return i0, min(len(FLAT), i1 + extra)


def tok(t):
    return ('_' if t[2] < 0 else str(t[2])) + ('^' if t[3] else '') + ('?' if t[4] else '')


def options(i):
    """[(ndigits, code, out, dotflag)] for a code starting at FLAT[i]."""
    res = []
    d0 = FLAT[i][2]
    if d0 < 0:
        return [(1, '_', '', '')]
    c1 = str(d0)
    for o in PLAIN.get(c1, []):
        res.append((1, c1, o, ''))
    if i + 1 < len(FLAT) and FLAT[i + 1][2] >= 0:
        c2 = c1 + str(FLAT[i + 1][2])
        for o in PLAIN.get(c2, []):
            res.append((2, c2, o, ''))
        if c2 in DOTTED:
            seen = FLAT[i][3] or (i > 0 and FLAT[i - 1][3])
            for o in DOTTED[c2]:
                res.append((2, c2, o, '' if seen else '*'))
        if i + 2 < len(FLAT) and c2 == '00' and FLAT[i + 2][2] == 0:
            res.append((3, '000', 'francia', ''))          # Meister p. 177: Francia = 000
    return res


def slip_options(i):
    """Codes the clerk may have meant when one digit of a one- or two-digit code at FLAT[i] is wrong: [(n, code, out, '!')]."""
    res = []
    d0 = FLAT[i][2]
    if d0 < 0:
        return res
    for e in '0123456789':
        if e != str(d0):
            for o in PLAIN.get(e, []):
                if o:
                    res.append((1, f'{d0}>{e}', o, '!'))
    if i + 1 < len(FLAT) and FLAT[i + 1][2] >= 0:
        c0 = f'{d0}{FLAT[i + 1][2]}'
        for c2 in set(PLAIN) | set(DOTTED):
            if len(c2) == 2 and c2 != c0 and sum(a != b for a, b in zip(c2, c0)) == 1:
                for o in PLAIN.get(c2, []) + DOTTED.get(c2, []):
                    if o:
                        res.append((2, f'{c0}>{c2}', o, '!'))
    return res


def top(lab, a=None, b=None, K=15, B=400):
    m = lm.load('it-cinquecento', order=5, spaces=False)
    i0, i1 = span(lab, a, b)
    beams = {i0: [(0.0, '', [])]}
    for i in range(i0, i1):
        for sc, txt, path in beams.pop(i, []):
            for n, c, o, f in options(i):
                if i + n > i1:
                    continue
                if c == '_':
                    for ch in 'aeiou':
                        beams.setdefault(i + 1, []).append((sc - 3, txt + ch, path + [f'_={ch}']))
                    continue
                pen = 4.0 if f else 0.0
                add = m.score(txt[-4:] + o) - m.score(txt[-4:]) if o else -2.0
                beams.setdefault(i + n, []).append((sc + add - pen, txt + (o if o else '|'), path + [f'{c}={o or "-"}{f}']))
        for j in list(beams):
            beams[j] = sorted(beams[j], key=lambda x: -x[0])[:B]
    out = sorted(beams.get(i1, []), key=lambda x: -x[0])[:K]
    for sc, txt, path in out:
        segs = ' | '.join(' '.join(segment(p)) for p in txt.split('|') if p)
        print(f'{sc:8.1f}  {segs}')
        print('          ', ' '.join(path))


def fit(lab, phrase, maxskip=1):
    ph = re.sub(r'[^a-z]', '', phrase.lower())
    i0, i1 = span(lab, extra=40)
    hits = []
    for s in range(i0, i1):
        # DP over (i, j): best skips
        st = {(s, 0): (0, [])}
        frontier = [(s, 0)]
        best = None
        while frontier:
            nf = []
            for (i, j) in frontier:
                sk, path = st[(i, j)]
                if j == len(ph):
                    if best is None or sk < best[0]:
                        best = (sk, path, i)
                    continue
                if i >= len(FLAT):
                    continue
                for n, c, o, f in options(i):
                    if c == '_':
                        cand = [(1, ph[j])] if ph[j] in 'aeiou' else []
                    elif o == '':
                        cand = [(n, '')] if j > 0 else []
                    elif ph.startswith(o, j):
                        cand = [(n, o)]
                    else:
                        cand = []
                    for nn, oo in cand:
                        key = (i + nn, j + len(oo))
                        val = (sk + (1 if f else 0), path + [f'{c}={oo or "-"}{f}'])
                        if key not in st or st[key][0] > val[0]:
                            st[key] = val
                            nf.append(key)
                if FLAT[i][4] and sk < maxskip:      # skip an unsure digit
                    key = (i + 1, j)
                    val = (sk + 1, path + [f'skip{FLAT[i][2]}'])
                    if key not in st or st[key][0] > val[0]:
                        st[key] = val
                        nf.append(key)
            frontier = nf
        if best:
            hits.append((best[0], s, best[2], best[1]))
    for sk, s, e, path in sorted(hits)[:12]:
        print(f'{FLAT[s][0]}:{FLAT[s][1]}-{FLAT[e-1][0]}:{FLAT[e-1][1]} cost {sk}  ', ' '.join(path))
    if not hits:
        print('no fit')


if __name__ == '__main__':
    cmd, lab = sys.argv[1], sys.argv[2]
    if cmd == 'show':
        i0, i1 = span(lab)
        print(lab, ' '.join(f'{FLAT[i][1]}:{tok(FLAT[i])}' for i in range(i0, i1)))
    elif cmd == 'top':
        a = int(sys.argv[3]) if len(sys.argv) > 4 else None
        b = int(sys.argv[4]) if len(sys.argv) > 4 else None
        K = int(sys.argv[5]) if len(sys.argv) > 5 else 15
        top(lab, a, b, K)
    elif cmd == 'fit':
        fit(lab, sys.argv[3])
