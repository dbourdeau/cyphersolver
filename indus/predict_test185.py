"""Hundred-and-eighty-fifth registered prediction set (PREDICTIONS.md, MF1-MF7): decipherment loop 10, do the marks added
to the fish (stroke 231, bar 233, roof hat 235, whiskers 240, against plain 220) work as affixes? Writes
results/predict_test185.md."""
import predict_test13 as T
import rtools as R
from predict_test112 import runs
from signs import FISH, load

VAR = ('220', '231', '233', '235', '240')


def slots(lines):
    out = []
    for t in lines:
        nm = R.name_of(list(t))
        if nm and nm[0]:
            b = nm[0]
            for i, g in enumerate(b):
                if g in VAR:
                    out.append((g, 'head' if i == len(b) - 1 else 'mod'))
    return out


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-eighty-fifth registered predictions: decipherment loop 10, do the other fish marks work as affixes?', 'predict_test185')
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln})
    sa, sb = slots(DA), slots(DB)
    rd.mi('MF1', 'the variant predicts its slot (A)', 'fish tokens in A names', [g for g, s in sa], [s for g, s in sa])
    rd.mi('MF2', 'the variant predicts its slot (B)', 'fish tokens in B names', [g for g, s in sb], [s for g, s in sb])
    DAB = DA + DB
    before = lambda t, i: i + 1 < len(t) and t[i + 1] in FISH
    rd.gtl('MF3', 'the roof fish is an attribute', 'directly before another fish, 235', [before(t, i) for t in DAB for i, g in enumerate(t) if g == '235'],
           [before(t, i) for t in DAB for i, g in enumerate(t) if g == '220'])
    ns = [(b, e) for b, e in {nm for nm in T.names(DAB) if nm[0]}]
    rd.gtl('MF4', 'whisker fish names take 520', '520, names headed by 240', [e == '520' for b, e in ns if b[-1] == '240'], [e == '520' for b, e in ns if b[-1] == '220'])
    share = lambda s, g: sum(1 for x, y in s if x == g and y == 'head') / max(1, sum(1 for x, y in s if x == g))
    dirs = []
    for g in VAR[1:]:
        da = share(sa, g) - share(sa, '220')
        db = share(sb, g) - share(sb, '220')
        dirs.append('%s A %+.2f B %+.2f' % (g, da, db))
        dirs_ok = (da > 0) == (db > 0)
        if not dirs_ok:
            break
    same = all(((share(sa, g) - share(sa, '220')) > 0) == ((share(sb, g) - share(sb, '220')) > 0) for g in VAR[1:])
    rd.rec('MF5', 'the variants behave alike in both samples', '; '.join('%s A %+.2f B %+.2f' % (g, share(sa, g) - share(sa, '220'), share(sb, g) - share(sb, '220')) for g in VAR[1:]), same)
    vv = [(sum(R.NUMS[x][0] for x in r), t[j]) for t in DB for i, j, r in runs(t) if j < len(t) and t[j] in VAR]
    rd.mi('MF6', 'the counted value depends on the variant (B)', 'numeral runs before a fish in B (%d)' % len(vv), [v for v, g in vv], [g for v, g in vv])
    pa = [(t[i - 1], g) for t in DA for i, g in enumerate(t) if g in VAR and i > 0]
    pb = [(t[i - 1], g) for t in DB for i, g in enumerate(t) if g in VAR and i > 0]
    oa, qa = R.mi_perm([p for p, g in pa], [g for p, g in pa])
    ob, qb = R.mi_perm([p for p, g in pb], [g for p, g in pb])
    rd.rec('MF7', 'the mark agrees with its context', 'A: MI %.3f, p = %.4f; B: MI %.3f, p = %.4f' % (oa, qa, ob, qb), qa < 0.05 and qb < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
