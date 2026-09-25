"""Two-hundred-and-seventy-fifth registered prediction set (PREDICTIONS.md, EP1-EP3): decipherment loop 100, are the
end-prone signs alternative name endings? The body before a line-final end-prone sign (set 262) should then be an
attested name body (the body before 740 / 520 in some other A line) more often than the body before a line-final 400
(not a name, set 270). Writes results/predict_test275.md."""
from collections import Counter

from scipy.stats import fisher_exact

import rtools as R
from grammar import lexical
from progress import edge_sets
from signs import load


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-seventy-fifth registered predictions: decipherment loop 100, end-prone signs as endings', 'predict_test275')
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    endp, openp = edge_sets()
    nb = Counter()
    for t in DA:
        nm = R.name_of(list(t))
        if nm and nm[0]:
            nb[tuple(nm[0])] += 1
    res = {}
    for name, L in (('A', DA), ('B', DB)):
        ep = [t[:-1] for t in L if len(t) >= 2 and t[-1] in endp and all(lexical(g) for g in t[:-1])]
        p4 = [t[:-1] for t in L if len(t) >= 2 and t[-1] == '400' and all(lexical(g) for g in t[:-1])]
        a = sum(nb[b] > 0 for b in ep)
        c = sum(nb[b] > 0 for b in p4)
        p = fisher_exact([[a, len(ep) - a], [c, len(p4) - c]], alternative='greater')[1] if ep and p4 else 1.0
        res[name] = (a, len(ep), c, len(p4), p)
        rd.say('- %s: end-prone bodies attested as name bodies %d of %d; 400 bodies %d of %d; p = %.2g.' % (name, *res[name]))
    rd.say()
    f = lambda r: '%d/%d against %d/%d, p = %.2g' % r
    rd.rec('EP1', 'A: end-prone bodies are attested name bodies more often than 400 bodies', f(res['A']), res['A'][4] < 0.05)
    rd.rec('EP2', 'B: the same (name bodies from A)', f(res['B']), res['B'][4] < 0.05)
    rd.rec('EP3', 'progress rule: EP1 and EP2 (a new finding: end-prone signs close name bodies)', 'EP1 %s, EP2 %s' % (res['A'][4] < 0.05, res['B'][4] < 0.05), res['A'][4] < 0.05 and res['B'][4] < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
