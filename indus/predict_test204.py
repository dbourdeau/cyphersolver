"""Two-hundred-and-fourth registered prediction set (PREDICTIONS.md, TG1-TG5, SB1-SB3): decipherment loop 29, the Tamil
Nadu graffiti composites against Indus lines by a language-free order fingerprint; a two-direction SIGN model. Writes
results/predict_test204.md."""
from collections import Counter

import graffiti as G
import rtools as R
from famlm import M3, fit3
from prizebench import _lp
from progress import MODEL, data
from signs import load as sload


def sign2(tr, te, keys, ncand=150):
    wf, _ = fit3(tr, keys)
    mf = M3(tr)
    rtr = [tuple(reversed(t)) for t in tr]
    wb, _ = fit3(rtr, keys)
    mb = M3(rtr)
    cands = [g for g, n in Counter(g for t in tr for g in t).most_common(ncand)]
    f1 = b1 = n = 0
    for t in te:
        for i, g in enumerate(t):
            sf = {c: _lp(mf, t[:i] + (c,) + t[i + 1:], wf) for c in cands}
            sb = {c: _lp(mb, tuple(reversed(t[:i] + (c,) + t[i + 1:])), wb) for c in cands}
            f1 += max(cands, key=lambda c: sf[c]) == g
            b1 += max(cands, key=lambda c: sf[c] + sb[c]) == g
            n += 1
    return f1 / n, b1 / n, n


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-fourth registered predictions: decipherment loop 29, the Tamil Nadu graffiti as writing; a two-direction SIGN model', 'predict_test204')
    gr = G.load()
    seqs = [s for c, n, s in gr if len(s) >= 2]
    DL, tr, te = data()
    oc, ot = G.order_consistency(seqs)
    ic, it = G.order_consistency(DL)
    rd.say('- graffiti composites %d (2+ elements %d) on %d sherds; Indus distinct lines %d.' % (len(gr), len(seqs), len({c for c, n, s in gr}), len(DL)))
    rd.say()
    rd.rec('TG1', 'graffiti order consistency 80%+', '%.1f%% of %d co-occurrences' % (100 * oc, ot), oc >= 0.8)
    rd.rec('TG2', 'within 10 points of Indus', 'graffiti %.1f%%, Indus %.1f%% (%d co-occurrences)' % (100 * oc, 100 * ic, it), abs(oc - ic) <= 0.10)
    xs, ys = [], []
    for s in seqs:
        for i, g in enumerate(s):
            xs.append(g)
            ys.append('F' if i == 0 else ('L' if i == len(s) - 1 else 'M'))
    rd.mi('TG3', 'elements prefer slots', 'graffiti element tokens', xs, ys)
    per = {}
    for site in ('KLD', 'TKP'):
        ss = [s for c, n, s in gr if len(s) >= 2 and c.startswith(site + '-')]
        per[site] = G.order_consistency(ss)
    rd.rec('TG4', 'order consistency at the two largest sites', '; '.join('%s %.1f%% of %d' % (k, 100 * v[0], v[1]) for k, v in per.items()), all(v[0] >= 0.8 for v in per.values()))
    gf = Counter(s[-1] for s in seqs).most_common(1)[0]
    inf = Counter(t[-1] for t in DL).most_common(1)[0]
    gs, isr = gf[1] / len(seqs), inf[1] / len(DL)
    rd.rec('TG5', 'final-element concentration like Indus', 'graffiti %s %.1f%%; Indus %s %.1f%%' % (gf[0], 100 * gs, inf[0], 100 * isr), abs(gs - isr) <= 0.10)
    f1, b1, n = sign2(tr, te, MODEL['keys'])
    rd.rec('SB1', 'two-direction SIGN, fixed test', 'top-1 forward %.1f%%, two-direction %.1f%% (%d signs)' % (100 * f1, 100 * b1, n), b1 - f1 >= 0.005)
    DA = sorted({tuple(t) for t in A})
    DBx = sorted({tuple(ln) for r in sload(only_m77=True) for ln in r['seq'] if ln} - set(DA))[:300]
    fa, ba, na = sign2(DA, DBx, MODEL['keys'])
    rd.rec('SB2', 'and A -> B', 'top-1 forward %.1f%%, two-direction %.1f%% (%d signs)' % (100 * fa, 100 * ba, na), ba > fa)
    ok = (oc >= 0.8 and all(v[0] >= 0.8 for v in per.values())) or (b1 - f1 >= 0.005 and ba > fa)
    rd.rec('SB3', 'progress rule', 'graffiti %s; SIGN %s' % (oc >= 0.8 and all(v[0] >= 0.8 for v in per.values()), b1 - f1 >= 0.005 and ba > fa), ok)
    rd.finish()


if __name__ == '__main__':
    main()
