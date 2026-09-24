"""Hundred-and-tenth registered prediction set (PREDICTIONS.md, RG1-RG20): sets 108-109 on held-out data. Writes
results/predict_test110.md."""
from collections import Counter

import rtools as R
from predict_test108 import genre, specific
from predict_test109 import toks

HEAD = ('817', '820', '861')
CITY = ('Mohenjo-daro', 'Harappa')


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-tenth registered predictions: sets 108-109 on held-out data', 'predict_test110')
    Fn = [r for r in F if r['type'] != 'TAB:C']
    FL = sorted({tuple(ln) for r in Fn for ln in r['seq'] if ln})
    OL = sorted({tuple(ln) for r in Fn if r['site'].strip() not in CITY for ln in r['seq'] if ln})
    OT = sorted({(r['type'][:3], tuple(ln)) for r in Fn if r['site'].strip() not in CITY for ln in r['seq'] if ln})
    BL = sorted({tuple(t) for t in B})
    rd.say("- F' lines %d, small-site lines %d, B lines %d." % (len(FL), len(OL), len(BL)))
    rd.say()
    jac = lambda a, b: len(a & b) / max(1, len(a | b))

    def gs7(lines, key, lab):
        ty = lambda g_: {g for t in lines if genre(t) == g_ for g in t if g not in R.NUMS}
        b, k, n = ty('bare'), ty('count'), ty('name')
        rd.rec(key, 'bare lines write like counts%s' % lab, 'Jaccard bare-count %.3f, bare-name %.3f' % (jac(b, k), jac(b, n)), jac(b, k) > jac(b, n))

    def gs10(lines, key, lab):
        lc = Counter(t[-1] for t in lines)
        fc = Counter(t[0] for t in lines)
        lx = [(t[-1], genre(t)) for t in lines if lc[t[-1]] >= 5]
        fx = [(t[0], genre(t)) for t in lines if fc[t[0]] >= 5]
        o1, p1 = R.mi_perm([a for a, _ in lx], [b for _, b in lx])
        o2, p2 = R.mi_perm([a for a, _ in fx], [b for _, b in fx])
        rd.rec(key, 'the last sign tells more%s' % lab, 'MI last %.3f (p = %.4f), first %.3f (p = %.4f)' % (o1, p1, o2, p2), o1 > o2 and p1 < 0.05 and p2 < 0.05)
        return fx

    def gs8(lines, key, lab):
        x = [(genre(t), R.lstrat(len(t))) for t in lines if genre(t) != 'other']
        rd.mi(key, 'the genre sets the length%s' % lab, 'lines', [a for a, _ in x], [b for _, b in x])
    gs7(FL, 'RG1', " (F')")
    fx = gs10(FL, 'RG2', " (F')")
    rd.mi('RG3', "the first sign tells the genre (F')", 'lines', [a for a, _ in fx], [b for _, b in fx])
    gs10(BL, 'RG4', ' (B)')
    gs7(BL, 'RG5', ' (B)')
    gs10(OL, 'RG6', ' (small sites)')
    sp, gc = specific(OL, 5)
    rd.thr('RG7', 'one vocabulary at the small sites', 'genre-specific signs', sum(bool(v) for v in sp.values()), len(sp), 0.3, above=False)
    gs8(FL, 'RG8', " (F')")
    gs8(OL, 'RG9', ' (small sites)')

    def b615(lines, key, lab):
        x = toks(lines, '615')
        rd.thr(key, '615 is doubled%s' % lab, '615 next to 615', sum((i > 0 and t[i - 1] == '615') or (i + 1 < len(t) and t[i + 1] == '615') for t, i in x), len(x), 0.3)

    def b368(lines, key, lab):
        p1 = {t[i - 1] for t, i in toks(lines, '368') if i > 0}
        p2 = {t[i - 1] for t, i in toks(lines, '740') if i > 0}
        rd.rec(key, '368 and 740 take different words%s' % lab, 'Jaccard %.3f; threshold 0.3' % jac(p1, p2), jac(p1, p2) <= 0.3)

    def b368h(lines, key, lab):
        x = toks(lines, '368')
        rd.thr(key, '368 follows a heading%s' % lab, '368 after a heading sign', sum(i > 0 and t[i - 1] in HEAD for t, i in x), len(x), 0.1)

    def b390(lines, key, lab):
        v = []
        for t, i in toks(lines, '390'):
            if i > 0 and t[i - 1] in R.NUMS:
                j = i - 1
                while j > 0 and t[j - 1] in R.NUMS:
                    j -= 1
                v.append(sum(R.NUMS[g][0] for g in t[j:i]))
        rd.thr(key, '390 is counted high%s' % lab, 'values 3+ before 390', sum(x >= 3 for x in v), len(v), 0.9)

    def b400(lines, key, lab):
        pb = {t[i - 1] for t, i in toks(lines, '400') if i > 0 and t[i - 1] not in R.END}
        p7 = {t[i - 2] for t, i in toks(lines, '400') if i > 1 and t[i - 1] in R.END}
        rd.rec(key, 'two different 400s%s' % lab, 'Jaccard %.3f; threshold 0.3' % jac(pb, p7), jac(pb, p7) <= 0.3)
    b615(FL, 'RG10', " (F')")
    b368(FL, 'RG11', " (F')")
    b368h(FL, 'RG12', " (F')")
    b390(FL, 'RG13', " (F')")
    b400(FL, 'RG14', " (F')")
    b368(BL, 'RG15', ' (B)')
    b400(BL, 'RG16', ' (B)')
    b390(BL, 'RG17', ' (B)')
    b368h(BL, 'RG18', ' (B)')
    x = [ty for ty, t in OT if '390' in t]
    rd.thr('RG19', '390 is a seal sign at the small sites', '390 lines on seals', sum(ty == 'SEA' for ty in x), len(x), 0.7)
    b615(OL, 'RG20', ' (small sites)')
    rd.finish()


if __name__ == '__main__':
    main()
