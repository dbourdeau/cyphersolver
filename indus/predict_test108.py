"""Hundred-and-eighth registered prediction set (PREDICTIONS.md, GS1-GS20): the four genres as systems. Writes
results/predict_test108.md."""
import random
from collections import Counter, defaultdict

import rtools as R
from predict_test44 import nonname
from predict_test102 import blk
from predict_test103 import CL
from predict_test104 import template

random.seed(128)


def genre(t):
    t = list(t)
    if R.name_of(t) and R.name_of(t)[0]:
        return 'name'
    if t and t[-1] in CL and not any(g in R.END for g in t):
        return 'closer'
    if nonname(t) and any(g in R.NUMS for g in t):
        return 'count'
    if len(t) >= 2 and template(tuple(t)) == 'X':
        return 'bare'
    return 'other'


def specific(lines, k=10):
    gc = defaultdict(Counter)
    for t in lines:
        g_ = genre(t)
        for g in t:
            if g not in R.NUMS:
                gc[g][g_] += 1
    out = {}
    for g, c in gc.items():
        n = sum(c.values())
        if n >= k:
            top, m = c.most_common(1)[0]
            out[g] = top if m / n >= 0.7 else None
    return out, gc


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-eighth registered predictions: the four genres as systems', 'predict_test108')
    DL = [t for t in sorted({tuple(t) for t in AB}) if t]
    G = Counter(genre(t) for t in DL)
    rd.say('- distinct lines %d; genres %s.' % (len(DL), dict(G)))
    rd.say()

    def gs1(lines, key, lab):
        sp, gc = specific(lines)
        k = [g for g in sp if sp[g]]
        rd.thr(key, 'signs belong to genres%s' % lab, 'genre-specific signs (%s)' % dict(Counter(sp[g] for g in k)), len(k), len(sp), 0.3)
        return sp, gc
    sp, gc = gs1(DL, 'GS1', '')
    four = {'name', 'closer', 'count', 'bare'}
    have = {sp[g] for g in sp if sp[g]}
    rd.rec('GS2', 'every genre has its own signs', 'genres with specific signs: %s' % sorted(have & four), four <= have)
    Fn = [r for r in F if r['type'] != 'TAB:C']
    med = lambda ty: 'seal' if ty.startswith('SEAL') else ty if ty in ('TAB:I', 'TAB:B') else 'pot' if ty.startswith('POT') else 'other'
    FD = sorted({(r['site'].strip(), med(r['type']), tuple(ln)) for r in Fn for ln in r['seq'] if ln})
    rd.mi('GS3', 'the object sets the genre', 'F lines', [m for s, m, t in FD], [genre(t) for s, m, t in FD])
    cs = [(s, genre(t)) for s, m, t in FD if s in ('Mohenjo-daro', 'Harappa')]
    rd.mi('GS4', 'the city sets the genre', 'F lines', [a for a, _ in cs], [b for _, b in cs])
    pl = sorted({(R.level('Harappa', recs[r['sealid']]), tuple(ln)) for r in Fn if r['site'].strip() == 'Harappa' for ln in r['seq'] if ln
                 if R.level('Harappa', recs[r['sealid']]) in ('E', 'L')})
    rd.mi('GS5', 'the period sets the genre', 'Harappa lines', [a for a, _ in pl], [genre(t) for _, t in pl])
    types = lambda g_: {g for t in DL if genre(t) == g_ for g in t if g not in R.NUMS}
    jac = lambda a, b: len(a & b) / max(1, len(a | b))
    Tn, Tc, Tk, Tb = types('name'), types('closer'), types('count'), types('bare')
    rd.rec('GS6', 'closers write like names', 'Jaccard name-closer %.3f, name-count %.3f' % (jac(Tn, Tc), jac(Tn, Tk)), jac(Tn, Tc) > jac(Tn, Tk))
    rd.rec('GS7', 'bare lines write like counts', 'Jaccard bare-count %.3f, bare-name %.3f' % (jac(Tb, Tk), jac(Tb, Tn)), jac(Tb, Tk) > jac(Tb, Tn))

    def gs8(lines, key, lab):
        x = [(genre(t), R.lstrat(len(t))) for t in lines if genre(t) != 'other']
        rd.mi(key, 'the genre sets the length%s' % lab, 'lines', [a for a, _ in x], [b for _, b in x])
    gs8(DL, 'GS8', '')
    fc = Counter(t[0] for t in DL)
    fx = [(t[0], genre(t)) for t in DL if fc[t[0]] >= 5]
    rd.mi('GS9', 'the first sign tells the genre', 'lines', [a for a, _ in fx], [b for _, b in fx])
    lc = Counter(t[-1] for t in DL)
    lx = [(t[-1], genre(t)) for t in DL if lc[t[-1]] >= 5]
    o1, p1 = R.mi_perm([a for a, _ in lx], [b for _, b in lx])
    o2, p2 = R.mi_perm([a for a, _ in fx], [b for _, b in fx])
    rd.rec('GS10', 'the last sign tells more', 'MI last %.3f (p = %.4f), first %.3f (p = %.4f)' % (o1, p1, o2, p2), o1 > o2 and p1 < 0.05 and p2 < 0.05)
    mo = [[genre(tuple(ln)) for ln in r['seq'] if ln] for r in Fn if len([ln for ln in r['seq'] if ln]) >= 2]
    flat = [g for m in mo for g in m]
    agree = lambda f: sum(len(set(f[i:i + len(m)])) == 1 for i, m in zip(_offs(mo), mo))
    obs = agree(flat)
    ge = 0
    sh = flat[:]
    for _ in range(R.N):
        random.shuffle(sh)
        ge += agree(sh) >= obs
    p = (ge + 1) / (R.N + 1)
    rd.rec('GS11', 'one object, one genre', 'multi-line objects %d; all one genre %d; p = %.4f' % (len(mo), obs, p), p < 0.05)
    se = [genre(t) for s, m, t in FD if m == 'seal']
    rd.thr('GS12', 'seals carry names', 'seal lines that are names or closers', sum(g in ('name', 'closer') for g in se), len(se), 0.7)
    rd.gtl('GS13', 'incised tablets count', 'count or bare, TAB:I', [genre(t) in ('count', 'bare') for s, m, t in FD if m == 'TAB:I'],
           [genre(t) in ('count', 'bare') for s, m, t in FD if m == 'TAB:B'])
    po = [genre(t) for s, m, t in FD if m == 'pot']
    rd.thr('GS14', 'potsherds count or label', 'potsherd lines that are bare or counts', sum(g in ('bare', 'count') for g in po), len(po), 0.7)
    sg = [('city' if s in ('Mohenjo-daro', 'Harappa') else 'small', genre(t)) for s, m, t in FD]
    o, p = R.mi_perm([a for a, _ in sg], [b for _, b in sg])
    rd.rec('GS15', 'the small sites write the same genres', 'MI %.4f; p = %.4f' % (o, p), p >= 0.05)
    tok = Counter(g for t in DL for g in t)
    rd.rank('GS16', 'genre signs are rare', 'shared against specific signs', [tok[g] for g in sp if not sp[g]], [tok[g] for g in sp if sp[g]])
    rd.gtl('GS17', 'count signs come from blocks 1 and 3', 'block 1 or 3, count-specific', [blk(g) in (1, 3) for g in sp if sp[g] == 'count' and blk(g) is not None],
           [blk(g) in (1, 3) for g in sp if sp[g] and sp[g] != 'count' and blk(g) is not None])
    BL = [t for t in sorted({tuple(t) for t in B}) if t]
    gs1(BL, 'GS18', ' (B)')
    gs8(BL, 'GS19', ' (B)')
    gs1(sorted({t for s, m, t in FD}), 'GS20', " (F')")
    rd.finish()


def _offs(mo):
    o, out = 0, []
    for m in mo:
        out.append(o)
        o += len(m)
    return out


if __name__ == '__main__':
    main()
