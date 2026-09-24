"""Fifty-seventh registered prediction set (PREDICTIONS.md, CL1-CL10): the other closers. Writes
results/predict_test57.md."""
import random
from collections import Counter

import predict_test13 as T
import rtools as R
from predict_test4 import OPEN
from predict_test44 import nonname

random.seed(77)
CL = ('400', '151', '527', '156', '154')
NEW = ('527', '156', '154')
HEAD = ('817', '820', '861')


def core(t):
    t = list(t)
    if len(t) >= 3 and t[0] in OPEN and t[1] in ('2', '60', '1'):
        t = t[2:]
    return tuple(t)


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    head, attr = R.classes(A)
    rd = R.Round('Fifty-seventh registered predictions: the other closers', 'predict_test57')
    nm = T.names(AB)
    bodies = {b for b, _ in nm if b}

    def closer(t):
        return len(t) >= 2 and nonname(t) and t[-1] in CL and core(t[:-1]) in bodies
    cls = [t for t in AB if closer(t)]
    rd.say('- closer lines %d (%s).' % (len(cls), ', '.join('%s x%d' % kv for kv in Counter(t[-1] for t in cls).most_common())))
    rd.say()
    b400 = {core(t[:-1]) for t in cls if t[-1] == '400'}
    w400 = {core(t[:-2]) for t in AB if len(t) >= 3 and t[-1] == '400' and t[-2] in R.END}
    rd.gtl('CL1', 'the ending was left out', 'attested with ending + 400, bodies of 400-closer lines', [b in w400 for b in b400],
           [b in w400 for b in bodies if b not in b400])
    fl = [(r, ln) for r in F for ln in r['seq']]
    rd.gtl('CL2', 'seals leave the ending out', 'seal, 400-closer lines', [r['type'].startswith('SEAL') for r, ln in fl if closer(ln) and ln[-1] == '400'],
           [r['type'].startswith('SEAL') for r, ln in fl if len(ln) >= 3 and ln[-1] == '400' and ln[-2] in R.END])
    ends = {}
    for b, e in nm:
        ends.setdefault(b, Counter())[e] += 1
    maj = lambda b: ends[b].most_common(1)[0][0]
    rd.gtl('CL3', 'the missing ending is 740', '740, bodies of 400-closer lines', [maj(b) == '740' for b in b400],
           [maj(b) == '740' for b in bodies if b not in b400])
    rd.rank('CL4', 'short names take the new closers', 'regular against new-closer bodies', [len(b) for b, _ in nm if b],
            [len(core(t[:-1])) for t in cls if t[-1] in NEW])
    sl = lambda site: [closer(ln) and ln[-1] in NEW for r, ln in fl if r['site'].strip() == site and len(ln) >= 2]
    rd.gtl('CL5', 'a Harappa habit', 'new-closer lines, Harappa', sl('Harappa'), sl('Mohenjo-daro'))
    rd.thr('CL6', 'closer lines are short', 'closer lines of 2-3 signs', sum(len(t) <= 3 for t in cls), len(cls), 0.7)
    fol = [t[i + 1] in R.END for t in AB for i in range(len(t) - 1) if t[i] in CL]
    rd.thr('CL7', 'closers end the name', 'closer tokens followed by 740/520', sum(fol), len(fol), 0.1, above=False)
    pre = [i > 0 and t[i - 1] in R.END for t in AB for i in range(len(t)) if t[i] in NEW]
    rd.thr('CL8', 'the new closers are post-name signs', 'new-closer tokens after 740/520', sum(pre), len(pre), 0.2)
    rd.ltl('CL9', 'closer lines are not headed', 'heading first, closer lines', [t[0] in HEAD for t in cls],
           [t[0] in HEAD for t in AB if R.name_of(t)])
    pc = Counter(t[-2] for t in cls)
    ty = [g for g in pc if pc[g] >= 2]
    rd.thr('CL10', 'a head comes before', 'pre-closer signs (2+ tokens) in the head class', sum(g in head for g in ty), len(ty), 0.5)
    rd.finish()


if __name__ == '__main__':
    main()
