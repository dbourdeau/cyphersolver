"""Fourth pass (slips) helper for 65r: where does a crib encode the digits with at most one wrong digit?

  python slip65_crib.py 65r.1 incarico [questo ...]     search 65r.1 (and the next line)
  python slip65_crib.py 65r.1:18-25 incarico             only starts inside 18..25

For each encoding of the word under k2d (+ dotted codes, + francia 000) that has the same digit count as the stream
at a start position, prints the encoding, the written digits and the mismatch (0 or 1 digit). Dotted codes are
shown with ' and flagged when no dot is seen on the code's first digit or the digit before it.
"""
import sys
import probe

VAL = {}
for c, vs in probe.PLAIN.items():
    for v in vs:
        if v:
            VAL.setdefault(v, []).append((c, False))
for c, vs in probe.DOTTED.items():
    for v in vs:
        VAL.setdefault(v, []).append((c, True))
VAL.setdefault('francia', []).append(('000', False))


def encodings(w, maxn=4000):
    out = []

    def rec(i, acc):
        if len(out) > maxn:
            return
        if i == len(w):
            out.append(list(acc))
            return
        for L in range(1, 8):
            seg = w[i:i + L]
            if len(seg) < L:
                break
            for c, dot in VAL.get(seg, []):
                acc.append((seg, c, dot))
                rec(i + L, acc)
                acc.pop()
    rec(0, [])
    return out


def main():
    where = sys.argv[1]
    lab, _, rng = where.partition(':')
    i0, i1 = probe.span(lab, extra=40)
    s0, s1 = i0, probe.span(lab)[1]
    if rng:
        a, b = map(int, rng.split('-'))
        s0, s1 = probe.span(lab, a, b)
    for w in sys.argv[2:]:
        hits = []
        for enc in encodings(w):
            digs = ''.join(c for _, c, _ in enc)
            n = len(digs)
            for s in range(s0, s1):
                if s + n > len(probe.FLAT):
                    break
                ts = probe.FLAT[s:s + n]
                if any(t[2] < 0 for t in ts):
                    continue
                wr = ''.join(str(t[2]) for t in ts)
                mis = [k for k in range(n) if wr[k] != digs[k]]
                if len(mis) > 1:
                    continue
                # dots
                k = 0
                nodot = []
                for seg, c, dot in enc:
                    if dot:
                        seen = probe.FLAT[s + k][3] or probe.FLAT[s + k - 1][3]
                        if not seen:
                            nodot.append(seg)
                    k += len(c)
                t0 = probe.FLAT[s]
                hits.append((len(mis) + 0.5 * len(nodot), f'{t0[0]}:{t0[1]}', w,
                             ' '.join(("'" if d else '') + c + '=' + seg for seg, c, d in enc),
                             ' '.join(probe.tok(t) for t in ts),
                             (f'slip at +{mis[0] + 1} ({probe.FLAT[s + mis[0]][0]}:{probe.FLAT[s + mis[0]][1]}) '
                              f'{wr[mis[0]]}>{digs[mis[0]]}' if mis else 'exact'),
                             ('no dot: ' + ','.join(nodot)) if nodot else ''))
        hits.sort()
        seen = set()
        for h in hits[:25]:
            key = (h[1], h[3])
            if key in seen:
                continue
            seen.add(key)
            print(f'{h[2]:12} {h[1]:9} {h[3]:40} written {h[4]:32} {h[5]} {h[6]}')
        if not hits:
            print(w, 'no fit')


if __name__ == '__main__':
    main()
