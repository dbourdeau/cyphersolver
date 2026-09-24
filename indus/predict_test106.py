"""Hundred-and-sixth registered prediction set (PREDICTIONS.md, XL1-XL20): bare lines. Writes
results/predict_test106.md."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test99 import roles
from predict_test104 import template

random.seed(126)


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-sixth registered predictions: bare lines', 'predict_test106')
    DL = [t for t in sorted({tuple(t) for t in AB}) if len(t) >= 2]
    bare = lambda t: len(t) >= 2 and template(t) == 'X'
    X = [t for t in DL if bare(t)]
    NL = [t for t in DL if R.name_of(list(t))]
    ns = sorted({(b, e) for b, e in T.names(AB) if b})
    bodies = {b for b, e in ns}
    heads = {b[-1] for b in bodies}
    openers = {b[0] for b in bodies if len(b) >= 2}
    rd.say('- bare lines %d; name lines %d.' % (len(X), len(NL)))
    rd.say()

    def xl1(Xs, Ns, key, lab):
        rd.rank(key, 'bare lines are short%s' % lab, 'name against bare lines', [len(t) for t in Ns], [len(t) for t in Xs])
    xl1(X, NL, 'XL1', '')
    x4 = [t for t in X if t[-1] == '400']
    rd.thr('XL2', 'bare lines end in 400', 'bare lines ending in 400', len(x4), len(X), 0.1)
    rd.thr('XL3', 'name + 400 without the ending', "bare '... 400' lines whose rest is a name body", sum(tuple(t[:-1]) in bodies for t in x4), len(x4), 0.3)
    Fn = [r for r in F if r['type'] != 'TAB:C']
    FD = sorted({(r['site'].strip(), r['type'][:3], r['type'], tuple(ln)) for r in Fn for ln in r['seq'] if len(ln) >= 2})
    rd.gtl('XL4', 'bare lines are on tablets', 'tablet, bare lines', [ty == 'TAB' for s, ty, tt, t in FD if bare(t)], [ty == 'TAB' for s, ty, tt, t in FD if R.name_of(list(t))])
    rd.gtl('XL5', 'bare lines are Harappan', 'bare share, Harappa', [bare(t) for s, ty, tt, t in FD if s == 'Harappa'], [bare(t) for s, ty, tt, t in FD if s == 'Mohenjo-daro'])
    rd.thr('XL6', 'bare lines end in a head', 'bare lines ending in a name head', sum(t[-1] in heads for t in X), len(X), 0.5)
    rd.thr('XL7', 'bare lines start with an opener', 'bare lines starting with a name opener', sum(t[0] in openers for t in X), len(X), 0.5)

    def xl8(Xs, bd, key, lab):
        x2 = [t for t in Xs if len(t) == 2]
        rd.thr(key, 'bare pairs are names without the ending%s' % lab, '2-sign bare lines that are name bodies', sum(tuple(t) in bd for t in x2), len(x2), 0.2)
    xl8(X, bodies, 'XL8', '')
    objs = defaultdict(set)
    for r in Fn:
        for ln in r['seq']:
            if ln:
                objs[tuple(ln)].add(r['sealid'])
    rd.gtl('XL9', 'bare texts recur', 'on 2+ objects, bare texts', [len(objs[t]) >= 2 for s, ty, tt, t in FD if bare(t)],
           [len(objs[t]) >= 2 for s, ty, tt, t in FD if R.name_of(list(t))])
    rd.gtl('XL10', 'bare lines are graffiti', 'potsherd, bare lines', [tt.startswith('POT') for s, ty, tt, t in FD if bare(t)],
           [tt.startswith('POT') for s, ty, tt, t in FD if R.name_of(list(t))])
    bsig = {g for b in bodies for g in b}
    rd.gtl('XL11', 'bare lines use formula words', 'formula-only, bare tokens', [g not in bsig for t in X for g in t], [g not in bsig for t in NL for g in t])
    ro = roles(DL)[0]
    rd.thr('XL12', 'bare lines end in a closer-type sign', 'bare lines ending in a final specialist', sum(ro.get(t[-1]) == 'F' for t in X), len(X), 0.3)
    rd.thr('XL13', '368 and 595 close bare lines', 'bare lines ending in 368 or 595', sum(t[-1] in ('368', '595') for t in X), len(X), 0.1)
    t368 = [(t, i) for t in DL for i in range(len(t)) if t[i] == '368']
    rd.thr('XL14', '368 follows a head', '368 tokens after a name head', sum(i > 0 and t[i - 1] in heads for t, i in t368), len(t368), 0.6)
    t595 = [(t, i) for t in DL for i in range(len(t)) if t[i] == '595']
    rd.thr('XL15', '595 closes lines', '595 tokens line-final', sum(i == len(t) - 1 for t, i in t595), len(t595), 0.6)
    rd.gtl('XL16', 'bare seal texts are personal', 'one object, bare seal texts', [len(objs[t]) == 1 for s, ty, tt, t in FD if ty == 'SEA' and bare(t)],
           [len(objs[t]) == 1 for s, ty, tt, t in FD if ty == 'SEA' and R.name_of(list(t))])
    hp = [(R.level('Harappa', recs[r['sealid']]), bare(tuple(ln))) for r in Fn if r['site'].strip() == 'Harappa' for ln in r['seq'] if len(ln) >= 2
          if R.level('Harappa', recs[r['sealid']]) in ('E', 'L')]
    rd.gtl('XL17', 'bare lines are early', 'bare, earlier Harappa lines', [x for l_, x in hp if l_ == 'E'], [x for l_, x in hp if l_ == 'L'])
    rd.gtl('XL18', 'bare 400 is Harappan', "ending in 400, Harappa bare lines", [t[-1] == '400' for s, ty, tt, t in FD if bare(t) and s == 'Harappa'],
           [t[-1] == '400' for s, ty, tt, t in FD if bare(t) and s == 'Mohenjo-daro'])
    DB = [t for t in sorted({tuple(t) for t in B}) if len(t) >= 2]
    XB = [t for t in DB if bare(t)]
    xl1(XB, [t for t in DB if R.name_of(list(t))], 'XL19', ' (B)')
    xl8(XB, {b for b, e in T.names(B) if b}, 'XL20', ' (B)')
    rd.finish()


if __name__ == '__main__':
    main()
