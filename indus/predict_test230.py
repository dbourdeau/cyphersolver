"""Two-hundred-and-thirtieth registered prediction set (PREDICTIONS.md, FT1-FT3): decipherment loop 55, fish-headed names
and 520 on seals and on tablets separately. Writes results/predict_test230.md."""
import predict_test13 as T
import rtools as R
from predict_test178 import depiction
from predict_test7 import fisher_less


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-thirtieth registered predictions: decipherment loop 55, the class signal on seals and tablets', 'predict_test230')
    dep = depiction()
    by = {'seal': set(), 'tab': set()}
    for r in F:
        k = 'seal' if r['type'].startswith('SEAL') else ('tab' if r['type'].startswith('TAB') else None)
        if k:
            for ln in r['seq']:
                if ln:
                    by[k].add(tuple(ln))
    oks = []
    for key, k, lab in (('FT1', 'seal', 'seals'), ('FT2', 'tab', 'tablets')):
        ns = [nm for nm in T.names(sorted(by[k])) if nm[0] and dep.get(nm[0][-1])]
        f = [e == '520' for b, e in ns if dep[b[-1]] == 'fish']
        o = [e == '520' for b, e in ns if dep[b[-1]] != 'fish']
        p = fisher_less(sum(o), len(o) - sum(o), sum(f), len(f) - sum(f))
        ok = p < 0.05 and sum(f) / max(1, len(f)) > sum(o) / max(1, len(o))
        rd.rec(key, 'fish names take 520 more, %s' % lab, 'fish-headed %d of %d, other heads %d of %d; p = %.4f' % (sum(f), len(f), sum(o), len(o), p), ok)
        oks.append(ok)
    rd.rec('FT3', 'progress rule', 'FT1 %s, FT2 %s' % tuple(oks), all(oks))
    rd.finish()


if __name__ == '__main__':
    main()
