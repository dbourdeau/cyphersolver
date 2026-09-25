"""Three-hundred-and-thirty-seventh registered prediction set (PREDICTIONS.md, DT1-DT4): decipherment loop 162, the
referent pool counted by distinct text. Set 336 found mould copies counted as independent objects. Here each distinct
text (after merging part-texts) is one observation, with the majority picture and stratum (site, class) of the objects
carrying it; base rates, units (set 334's kinds, stratified binomial, alpha 0.005) and the within-stratum shuffles of the
FDR are all over distinct texts. Validation: these figures replace the current ones (13.64%; 6.84% without Bull1 units)
if lower. Writes results/predict_test337.md."""
import random
from collections import Counter, defaultdict

import predict_test334 as S
import rtools as R
import referents as X
from predict_test304 import coverage
from predict_test335 import fdr
from progress import data


def distinct(objs):
    g = defaultdict(list)
    for t, m, s in objs:
        g[t].append((m, s))
    out = []
    for t, ms in g.items():
        m = Counter(x for x, s in ms).most_common(1)[0][0]
        s = Counter(s for x, s in ms).most_common(1)[0][0]
        out.append((t, m, s))
    return out


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-thirty-seventh registered predictions: decipherment loop 162, the referent pool counted by distinct text', 'predict_test337')
    DL, tr, te = data()
    clean, both = S.site_objects(F, recs)
    S.ALPHA = 0.005
    dclean, dboth = distinct(clean), distinct(both)
    P = {'made': ([(t, m) for t, m, s in clean], [(t, m) for t, m, s in both])}
    u = S.units(dclean, dboth)
    n, f = fdr(dclean, dboth, 337)
    nb = {k: {g: m for g, m in v.items() if m != 'Bull1'} for k, v in u.items()}
    c, cnb = coverage(DL, P, u), coverage(DL, P, nb)
    rd.say('- %d objects -> %d distinct texts; %d units (%d Bull1), FDR %.1f%%; coverage %.2f%% (without Bull1 units %.2f%%); current 13.64%% / 6.84%%.' % (len(both), len(dboth), n, sum(1 for k, v in u.items() for g, m in v.items() if m == 'Bull1'), 100 * f, 100 * c, 100 * cnb))
    rd.say()
    rd.rec('DT1', 'FDR over distinct texts <= 10%', '%.1f%%' % (100 * f), f <= 0.10)
    rd.rec('DT2', 'coverage at least 13.64%', '%.2f%%' % (100 * c), c >= 0.1364)
    rd.rec('DT3', 'without Bull1 units at least 6.84%', '%.2f%%' % (100 * cnb), cnb >= 0.0684)
    rd.rec('DT4', 'progress rule: none (a correction; lower figures replace the current ones)', 'DT2 %s, DT3 %s' % (c >= 0.1364, cnb >= 0.0684), False)
    rd.finish()


if __name__ == '__main__':
    main()
