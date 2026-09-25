"""Two-hundred-and-sixty-seventh registered prediction set (PREDICTIONS.md, RL1-RL4): decipherment loop 92, roles from the
new grammar rules. The end-prone and opening-prone signs (learned from A) and line-final 400 behave the same on B; if so
`progress.roles(edges=True)` gives those tokens a role. Writes results/predict_test267.md."""
from collections import Counter

import rtools as R
from progress import data, edge_sets, roles
from signs import load


def main():
    rd = R.Round('Two-hundred-and-sixty-seventh registered predictions: decipherment loop 92, roles from the new grammar rules', 'predict_test267')
    DL, tr, te = data()
    DA = sorted({tuple(t) for t in R.load_all()[0]})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    endp, openp = edge_sets()
    occ = Counter(g for t in DB for g in t)
    last, first = Counter(t[-1] for t in DB), Counter(t[0] for t in DB)
    e = sum(last[g] for g in endp) / max(1, sum(occ[g] for g in endp))
    o = sum(first[g] for g in openp) / max(1, sum(occ[g] for g in openp))
    f4 = last['400'] / max(1, occ['400'])
    rd.say('- end-prone %d signs, opening-prone %d; B tokens %d / %d; 400 on B %d.' % (len(endp), len(openp), sum(occ[g] for g in endp), sum(occ[g] for g in openp), occ['400']))
    rd.rec('RL1', 'B: end-prone signs end 50%+ of their occurrences', '%.0f%%' % (100 * e), e >= 0.5)
    rd.rec('RL2', 'B: opening-prone signs open 50%+ of their occurrences', '%.0f%%' % (100 * o), o >= 0.5)
    rd.rec('RL3', 'B: 400 is line-final in 80%+ of its occurrences', '%.0f%%' % (100 * f4), f4 >= 0.8)
    r0 = roles(DL)[0]
    r1, by, tot = roles(DL, edges=True)
    ok = e >= 0.5 and o >= 0.5 and f4 >= 0.8 and r1 > r0
    rd.rec('RL4', 'progress rule: RL1-RL3 hold and R rises', 'R %.1f%% -> %.1f%% (%s)' % (100 * r0, 100 * r1, ', '.join('%s %d' % (k, by[k]) for k in ('end-prone closer', 'opener', 'line-final 400'))), ok)
    rd.finish()


if __name__ == '__main__':
    main()
