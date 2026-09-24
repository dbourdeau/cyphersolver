"""Hundred-and-nineteenth registered prediction set (PREDICTIONS.md, EP1-EP15): the ending slot as a paradigm. Writes
results/predict_test119.md."""
from collections import Counter, defaultdict

import rtools as R
from predict_test103 import CL
from predict_test118 import strip

HEAD = ('817', '820', '861')
CITY = ('Mohenjo-daro', 'Harappa')
FILL = ('740', '520') + CL


def fillers(t):
    """(body, filler, stacked) for each filler position after a non-filler body."""
    s = strip(t)
    out = []
    for i in range(1, len(s)):
        if s[i] in FILL and s[i - 1] not in FILL:
            out.append((s[:i], s[i], i + 1 < len(s) and s[i] in R.END and s[i + 1] in CL))
    return out


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-nineteenth registered predictions: the ending slot as a paradigm', 'predict_test119')
    DL = sorted({tuple(t) for t in AB})
    adj = lambda lines, a, b: sum(1 for t in lines for x, y in zip(t, t[1:]) if x in a and y in b)

    def ep1(lines, key, lab):
        c7 = adj(lines, CL, ('740',))
        s7 = adj(lines, ('740',), CL)
        rd.thr(key, 'the order is 740 then closer%s' % lab, "'closer 740' among closer-740 adjacencies", c7, c7 + s7, 0.1, above=False)
    ep1(DL, 'EP1', '')
    s7 = sum(1 for t in DL if any(x == '740' and y in CL for x, y in zip(t, t[1:])))
    s5 = sum(1 for t in DL if any(x == '520' and y in CL for x, y in zip(t, t[1:])))
    rd.rec('EP2', 'closers stack after 740, not 520', "lines '740 + closer' %d, '520 + closer' %d" % (s7, s5), s7 >= 3 * max(1, s5))
    ctx = [(t[i], t[i - 1] == '740') for t in DL for i in range(1, len(t)) if t[i] in CL]
    rd.mi('EP3', 'stacking closers are a subset', 'closer tokens', [a for a, _ in ctx], [b for _, b in ctx])
    bs = []
    ba = []
    for t in DL:
        s = strip(t)
        for i in range(1, len(s)):
            if s[i] in CL and s[i - 1] == '740':
                bs.append(i - 1)
            elif s[i] in CL and s[i - 1] not in FILL:
                ba.append(i)
    rd.rank('EP4', 'stacked names are longer', "'740 + closer' against closer-alone bodies", bs, ba)
    hu = lambda t: len(t) >= 3 and t[0] in HEAD and t[1] in ('2', '60', '1')
    cl_lines = [t for t in DL if any(g in CL for g in t)]
    st = lambda t: any(x == '740' and y in CL for x, y in zip(t, t[1:]))
    rd.gtl('EP5', 'headed names stack', "'740 + closer', headed closer lines", [st(t) for t in cl_lines if hu(t)], [st(t) for t in cl_lines if not hu(t)])
    Fn = [r for r in F if r['type'] != 'TAB:C']
    FD = sorted({(r['site'].strip(), r['type'][:3], tuple(ln)) for r in Fn for ln in r['seq'] if ln})
    x = [ty for s, ty, t in FD if st(t)]
    rd.thr('EP6', 'stacked names are seal texts', "'740 + closer' lines on seals", sum(ty == 'SEA' for ty in x), len(x), 0.8)
    rd.gtl('EP7', 'stacking is Mohenjo-daran', "Mohenjo-daro, '740 + closer' lines", [s == 'Mohenjo-daro' for s, ty, t in FD if st(t) and s in CITY],
           [s == 'Mohenjo-daro' for s, ty, t in FD if any(g in CL for g in t) and not st(t) and s in CITY])
    bf = defaultdict(set)
    for t in DL:
        for b, f, _ in fillers(t):
            bf[b].add(f)
    n3 = sum(len(v) >= 3 for v in bf.values())
    rd.rec('EP8', 'bodies decline through the slot', 'bodies with 3+ fillers: %d; threshold 5' % n3, n3 >= 5)
    hf = [(s, b[-1], f) for s, ty, t in FD if s in CITY for b, f, _ in fillers(t) if b]
    o1, p1 = R.mi_perm([h for s, h, f in hf], [f for s, h, f in hf])
    o2, p2 = R.mi_perm([s for s, h, f in hf], [f for s, h, f in hf])
    rd.rec('EP9', 'the head, not the city, chooses', 'MI head %.3f (p = %.4f), city %.3f (p = %.4f)' % (o1, p1, o2, p2), o1 > o2 and p1 < 0.05)
    after = {y for t in DL for x, y in zip(t, t[1:]) if x == '740' and y in CL}
    rd.thr('EP10', 'every closer can follow 740', 'closers seen after 740 (%s)' % ', '.join(sorted(after)), len(after), len(CL), 0.7)
    n = sum(1 for t in DL if any(t[i] == '740' and t[i + 1] in CL and t[i + 2] == '400' for i in range(len(t) - 2)))
    rd.rec('EP11', 'no double suffix', "lines '740 + closer + 400': %d; threshold 2" % n, n <= 2)
    cs = [(s, g) for s, ty, t in FD if s in CITY for g in t if g in CL]
    rd.mi('EP12', 'the city chooses the closer', 'closer tokens', [a for a, _ in cs], [b for _, b in cs])
    ct = [(ty, g) for s, ty, t in FD if ty in ('SEA', 'TAB') for g in t if g in CL]
    rd.mi('EP13', 'the medium chooses the closer', 'closer tokens', [a for a, _ in ct], [b for _, b in ct])
    BL = sorted({tuple(t) for t in B})
    ep1(BL, 'EP14', ' (B)')
    b7, bc = set(), set()
    for t in BL:
        for b, f, _ in fillers(t):
            (b7 if f == '740' else bc if f in CL else set()).add(b)
    rd.rec('EP15', 'the same body takes either (B)', 'bodies before 740 and a closer: %d; threshold 5' % len(b7 & bc), len(b7 & bc) >= 5)
    rd.finish()


if __name__ == '__main__':
    main()
