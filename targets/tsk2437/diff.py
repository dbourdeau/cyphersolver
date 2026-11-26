"""Diff two positioned passes sign by sign. Usage: python diff.py pass1.txt pass2.txt [tolerance px=45]
Signs are paired per line by nearest x within the tolerance; reports agreements, code disagreements, one-pass-only signs."""
import sys
import tok

a = tok.parse(sys.argv[1])
b = tok.parse(sys.argv[2])
tol = int(sys.argv[3]) if len(sys.argv) > 3 else 45
skip = ('|',)


def per_line(rows):
    d = {}
    for ln, x, c, g, n in rows:
        if c in skip:
            continue
        d.setdefault(ln, []).append((x, c, g))
    return d


A, B = per_line(a), per_line(b)
agree = dis = onlya = onlyb = 0
out = []
for ln in sorted(A, key=lambda s: int(s[1:])):
    la, lb = sorted(A[ln]), sorted(B.get(ln, []))
    usedb = set()
    for x, c, g in la:
        best, bd = None, tol + 1
        for j, (x2, c2, g2) in enumerate(lb):
            if j in usedb:
                continue
            # prefer same-code candidates inside the tolerance
            d = abs(x - x2) + (0 if c == c2 else 15)
            if abs(x - x2) <= tol and d < bd:
                best, bd = j, d
        if best is None:
            onlya += 1
            out.append('%s@%d  pass1 only: %s (%s)' % (ln, x, c, g))
        else:
            usedb.add(best)
            x2, c2, g2 = lb[best]
            if c == c2:
                agree += 1
            else:
                dis += 1
                out.append('%s@%d  %s (%s) vs pass2 %s@%d (%s)' % (ln, x, c, g, c2, x2, g2))
    for j, (x2, c2, g2) in enumerate(lb):
        if j not in usedb:
            onlyb += 1
            out.append('%s@%d  pass2 only: %s (%s)' % (ln, x2, c2, g2))
print('\n'.join(out))
print('agree %d, code disagreements %d, pass1 only %d, pass2 only %d' % (agree, dis, onlya, onlyb))
