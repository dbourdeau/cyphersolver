"""Hundred-and-fifth registered prediction set (PREDICTIONS.md, CB1-CB20): closer inscriptions against name
inscriptions. Writes results/predict_test105.md."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test4 import OPEN
from predict_test61 import units
from predict_test81 import classes_of
from predict_test103 import CL
from signs import FISH

random.seed(125)
HEAD = ('817', '820', '861')
NONE = ('', 'None', '-', 'Unknown')


def cbody(t):
    t = list(t)
    if not t or t[-1] not in CL:
        return None
    if len(t) >= 3 and t[0] in OPEN and t[1] in ('2', '60', '1'):
        t = t[2:]
    return tuple(t[:-1])


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-fifth registered predictions: closer inscriptions against name inscriptions', 'predict_test105')
    DL = [t for t in sorted({tuple(t) for t in AB}) if len(t) >= 2]
    ns = sorted({(b, e) for b, e in T.names(AB) if b})
    nb = {b for b, e in ns}
    heads = {b[-1] for b in nb}
    cls = [(t, cbody(t)) for t in DL if cbody(t)]
    cb = sorted({b for t, b in cls})
    rd.say('- closer lines %d; distinct closer bodies %d.' % (len(cls), len(cb)))
    rd.say()

    def cb1(bodies, hd, key, lab):
        b2 = [b for b in bodies if len(b) >= 2]
        rd.thr(key, 'closer bodies end in name heads%s' % lab, 'closer bodies ending in a name head', sum(b[-1] in hd for b in b2), len(b2), 0.6)
    cb1(cb, heads, 'CB1', '')
    rd.thr('CB2', 'closer bodies are names', 'closer bodies also name bodies', sum(b in nb for b in cb), len(cb), 0.2)
    rd.rank('CB3', 'closer bodies are short', 'name against closer bodies', [len(b) for b in nb], [len(b) for b in cb])
    U = units(sorted({b for b in nb if len(b) >= 2}))
    hu_ = lambda b: any(p in U for p in zip(b, b[1:]))
    a = [hu_(b) for b in cb if len(b) >= 2]
    c = [hu_(b) for b in nb if len(b) >= 2]
    p = min(1, 2 * min(R.hyper_ge(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c)), R.fisher_less(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c))))
    rd.rec('CB4', 'closer bodies use the name units', 'unit, closer bodies %s' % R.fl(sum(a), len(a), sum(c), len(c), p), p >= 0.05)

    def cb5(rows, key, lab):
        x = [(t[-1], b[-1]) for t, b in rows if b]
        rd.mi(key, 'each closer has its heads%s' % lab, 'closer lines', [a_ for a_, _ in x], [b_ for _, b_ in x])
    cb5(cls, 'CB5', '')
    cl = classes_of(ns)
    shared = {b[-1] for b in cb if b} & set(cl)
    rd.thr('CB6', 'closer heads are 740-class heads', 'shared heads in the 740 class (%s)' % ', '.join(sorted(shared)[:12]), sum(cl[h] == '740' for h in shared), len(shared), 0.9)
    hu = lambda t: len(t) >= 3 and t[0] in HEAD and t[1] in ('2', '60', '1')
    nl = [t for t in DL if R.name_of(list(t))]
    rd.ltl('CB7', 'closer lines are not titled', 'heading unit, closer lines', [hu(t) for t, b in cls], [hu(t) for t in nl])
    Fn = [r for r in F if r['type'] != 'TAB:C']
    mot = lambda r: '' if recs[r['sealid']][18].strip() in NONE else recs[r['sealid']][18].split(':')[0].strip()
    sm = [(cbody(tuple(ln)) is not None, mot(r) == 'Bull1') for r in Fn if r['type'].startswith('SEAL') and mot(r) for ln in r['seq'] if len(ln) >= 2
          if cbody(tuple(ln)) is not None or R.name_of(ln)]
    a = [u for c_, u in sm if c_]
    c = [u for c_, u in sm if not c_]
    p = min(1, 2 * min(R.hyper_ge(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c)), R.fisher_less(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c))))
    rd.rec('CB8', 'the same animals', 'unicorn, closer seal lines %s' % R.fl(sum(a), len(a), sum(c), len(c), p), p >= 0.05)
    FD = sorted({(r['site'].strip(), r['type'][:3], tuple(ln)) for r in Fn for ln in r['seq'] if len(ln) >= 2})
    si = lambda s: [cbody(t) is not None for s_, ty, t in FD if s_ == s and ty == 'SEA' and (cbody(t) is not None or R.name_of(list(t)))]
    rd.gtl('CB9', 'a Mohenjo-daro inscription type', 'closer share of seal inscriptions, MD', si('Mohenjo-daro'), si('Harappa'))
    fish = lambda b: any(g in FISH for g in b)
    rd.ltl('CB10', 'closer bodies are not fish names', 'fish, closer bodies', [fish(b) for b in cb], [fish(b) for b in nb])
    num = lambda b: any(g in R.NUMS for g in b)
    a = [num(b) for b in cb]
    c = [num(b) for b in nb]
    p = min(1, 2 * min(R.hyper_ge(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c)), R.fisher_less(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c))))
    rd.rec('CB11', 'closer bodies count like names', 'numeral, closer bodies %s' % R.fl(sum(a), len(a), sum(c), len(c), p), p >= 0.05)
    x = [(t[-1], b[0]) for t, b in cls if len(b) >= 2]
    rd.mi('CB12', 'each closer has its openers', 'closer lines', [a_ for a_, _ in x], [b_ for _, b_ in x])
    no = {b[0] for b in nb if len(b) >= 2}
    co = {b[0] for b in cb if len(b) >= 2}
    rd.thr('CB13', 'closer bodies share the name openers', 'closer opener types also name openers', len(co & no), len(co), 0.6)
    objs = defaultdict(set)
    for r in Fn:
        for ln in r['seq']:
            if ln:
                objs[tuple(ln)].add(r['sealid'])
    rd.gtl('CB14', 'closer texts are personal', 'one object, closer texts', [len(objs[t]) == 1 for s, ty, t in FD if cbody(t) is not None],
           [len(objs[t]) == 1 for s, ty, t in FD if R.name_of(list(t))])
    hp = [(R.level('Harappa', recs[r['sealid']]), cbody(tuple(ln)) is not None) for r in Fn if r['site'].strip() == 'Harappa' for ln in r['seq'] if len(ln) >= 2
          if R.level('Harappa', recs[r['sealid']]) in ('E', 'L')]
    rd.gtl('CB15', 'closers are early', 'closer lines, earlier', [x_ for l_, x_ in hp if l_ == 'E'], [x_ for l_, x_ in hp if l_ == 'L'])
    s1 = [s == 'Mohenjo-daro' for s, ty, t in FD if t[-1] == '156' and s in ('Mohenjo-daro', 'Harappa')]
    s2 = [s == 'Mohenjo-daro' for s, ty, t in FD if t[-1] == '527' and s in ('Mohenjo-daro', 'Harappa')]
    p = min(1, 2 * min(R.hyper_ge(sum(s1), len(s1) - sum(s1), sum(s2), len(s2) - sum(s2)), R.fisher_less(sum(s1), len(s1) - sum(s1), sum(s2), len(s2) - sum(s2))))
    rd.rec('CB16', '156 and 527 are different places', 'Mohenjo-daro, 156 lines %s' % R.fl(sum(s1), len(s1), sum(s2), len(s2), p), p < 0.05)
    c520 = {h for h in cl if cl[h] == '520'}
    rd.ltl('CB17', 'closers do not follow the 520 class', '520-class head before, closers', [b[-1] in c520 for b in cb if b],
           [b[-1] in c520 for b, e in ns if e == '520'])
    rd.thr('CB18', 'name + closer', 'closer lines with 740/520 just before the closer', sum(len(t) >= 2 and t[-2] in R.END for t, b in cls), len(cls), 0.12)
    DB = [t for t in sorted({tuple(t) for t in B}) if len(t) >= 2]
    clB = [(t, cbody(t)) for t in DB if cbody(t)]
    cb5(clB, 'CB19', ' (B)')
    cb1(sorted({b for t, b in clB}), {b[-1] for b, e in T.names(B) if b}, 'CB20', ' (B)')
    rd.finish()


if __name__ == '__main__':
    main()
