"""Forty-fourth registered prediction set (PREDICTIONS.md, NN1-NN10): lines without a name. Writes
results/predict_test44.md."""
import random
from collections import Counter

import predict_test13 as T
import rtools as R

random.seed(64)


def nonname(t):
    return len(t) >= 2 and not any(g in R.END for g in t)


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    head, attr = R.classes(A)
    rd = R.Round('Forty-fourth registered predictions: lines without a name', 'predict_test44')
    nn = [t for t in AB if nonname(t)]
    nl = [t for t in AB if R.name_of(t)]
    rd.say('- non-name lines %d, name lines %d.' % (len(nn), len(nl)))
    rd.say()
    rd.ltl('NN1', 'they are not names without the ending', 'last sign in the head class, non-name lines',
           [t[-1] in head for t in nn], [R.name_of(t)[0][-1] in head for t in nl if R.name_of(t)[0]])
    items = []
    for r in F:
        for ln in r['seq']:
            if nonname(ln) or R.name_of(ln):
                items.append((nonname(ln), R.lstrat(len(ln)), 0 if r['type'].startswith('SEAL') else 1))
    rd.strat('NN2', 'they are off the seals', 'off seals, non-name minus name lines', items)
    sl = [(r['motif'].strip(), nonname(ln)) for r in rowsA if r['type'].startswith('SEAL') and r['motif'].strip()
          for ln in r['seq'] if nonname(ln) or R.name_of(ln)]
    rd.mi('NN3', 'the motif goes with the line kind', 'seal lines with a motif', [m for m, _ in sl], [k for _, k in sl])
    num = lambda t: any(g in R.NUMS for g in t)
    rd.gtl('NN4', 'they carry numbers', 'numeral, non-name lines', [num(t) for t in nn], [num(t) for t in nl])
    bodies = {b for b, _ in T.names(AB) if len(b) >= 2}
    mx = max(len(b) for b in bodies)
    has = lambda t: any(tuple(t[i:i + k]) in bodies for k in range(2, min(mx, len(t)) + 1) for i in range(len(t) - k + 1))
    n3 = [t for t in nn if len(t) >= 3]
    obs = sum(map(has, n3))
    ge = 0
    for _ in range(R.N // 10):
        k_ = 0
        for t in n3:
            s = list(t)
            random.shuffle(s)
            k_ += has(s)
        ge += k_ >= obs
    p = (ge + 1) / (R.N // 10 + 1)
    rd.rec('NN5', 'they contain a name body', 'lines %d; with an attested body %d; p = %.4f (1,000 shuffles)' % (len(n3), obs, p),
           p < 0.05)
    rd.rank('NN6', 'they are shorter', 'name against non-name lines', [len(t) for t in nl], [len(t) for t in nn])
    tc = Counter(tuple(ln) for r in F for ln in r['seq'])
    rd.gtl('NN7', 'they recur', 'distinct texts on 2+ objects, non-name', [n >= 2 for t, n in tc.items() if nonname(list(t))],
           [n >= 2 for t, n in tc.items() if R.name_of(list(t))])
    hd = lambda t: t[0] in ('817', '820', '861')
    rd.ltl('NN8', 'they are not headed', 'heading, non-name lines', [hd(t) for t in nn], [hd(t) for t in nl])
    items = [(r['site'].strip() == 'Harappa', R.lstrat(len(ln)), 1 if nonname(ln) else 0) for r in F
             if r['site'].strip() in ('Harappa', 'Mohenjo-daro') for ln in r['seq'] if nonname(ln) or R.name_of(ln)]
    rd.strat('NN9', 'Harappa writes more non-names', 'Harappa minus Mohenjo-daro', items)
    lc = Counter(t[-1] for t in nn)
    rd.thr('NN10', 'they end in a few signs', 'five commonest last signs (%s)' % ', '.join('%s x%d' % kv for kv in lc.most_common(5)),
           sum(n for _, n in lc.most_common(5)), len(nn), 0.5)
    rd.finish()


if __name__ == '__main__':
    main()
