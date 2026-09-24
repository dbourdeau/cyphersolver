"""Hundred-and-thirty-ninth registered prediction set (PREDICTIONS.md, CS1-CS10): Parpola's CISI (the mayig
digitisation, cisi.py) as a second transcription of Mohenjo-daro M-1 to M-184. Writes results/predict_test139.md."""
from collections import Counter

import cisi
import rtools as R
from predict_test103 import CL
from predict_test138 import fish_counts
from signs import FISH

HEAD = ('817', '820', '861')


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round("Hundred-and-thirty-ninth registered predictions: a second transcription, Parpola's CISI", 'predict_test139')
    C = cisi.load()
    P = cisi.p2icit()
    fs = {r['sealid']: r for r in F}
    byno = {}
    for k, rec in recs.items():
        if k in fs:
            byno.setdefault(rec[1].strip(), k)
    objs = {}
    for side, o in C.items():
        if any('P000' in ln for ln in o['seq']):
            continue
        no = cisi.cisi_no(side)
        if no in byno:
            e = objs.setdefault(no, {'seq': [], 'damage': [], 'unc': [], 'icit': fs[byno[no]]})
            e['seq'] += o['seq']
            e['damage'] += o['damage']
            e['unc'] += o['unc']
    rd.say('- joined intact objects without P000: %d.' % len(objs))
    rd.say()
    flat = lambda xs: [g for ln in xs for g in ln]
    same_len = [len(flat(e['seq'])) == len(e['icit']['flat']) for e in objs.values()]
    rd.thr('CS1', 'the same number of signs', 'objects with equal length', sum(same_len), len(same_len), 0.7)
    single = [e for e in objs.values() if len(e['seq']) == 1 and len(e['icit']['seq']) == 1 and len(e['seq'][0]) == len(e['icit']['seq'][0])]
    tc = Counter(g for t in A for g in t)
    pos = []
    for e in single:
        for p, g, d, u in zip(e['seq'][0], e['icit']['seq'][0], e['damage'][0], e['unc'][0]):
            pos.append((g in P.get(p, set()), d > 0 or u > 0, tc[g] < 20, p, g))
    rd.thr('CS2', 'positions agree', 'agreeing positions on %d single-line equal-length objects' % len(single), sum(x[0] for x in pos), len(pos), 0.8)
    dis = Counter((p, g) for ok, _, _, p, g in pos if not ok)
    rd.say('- commonest disagreements (Parpola, ICIT): %s.' % ', '.join('%s/%s %d' % (p, g, n) for (p, g), n in dis.most_common(12)))
    rd.say()

    def val(p):
        vs = {R.NUMS[g][0] for g in P.get(p, set()) if g in R.NUMS}
        return vs.pop() if len(vs) == 1 and all(g in R.NUMS for g in P.get(p, set())) else None
    isfish = lambda p: bool(P.get(p, set()) & set(FISH))
    ishead = lambda p: bool(P.get(p, set()) & set(HEAD))

    def cfish(ln):
        out = []
        i = 0
        while i < len(ln):
            if val(ln[i]) is not None:
                j = i
                while j < len(ln) and val(ln[j]) is not None:
                    j += 1
                if j < len(ln) and isfish(ln[j]) and not (i > 0 and ishead(ln[i - 1])):
                    out.append(sum(val(x) for x in ln[i:j]))
                i = j
            else:
                i += 1
        return out
    agree = []
    for e in objs.values():
        iv = [v for v, f, t in fish_counts([tuple(ln) for ln in e['icit']['seq']])]
        cv = [v for ln in e['seq'] for v in cfish(ln)]
        for v in iv:
            agree.append(v in cv)
    rd.thr('CS3', 'the counted fish agree', 'ICIT numeral-before-fish values found in CISI', sum(agree), len(agree), 0.8)
    cc = Counter(v for e in objs.values() for ln in e['seq'] for v in cfish(ln))
    ic = Counter(v for e in objs.values() for v, f, t in fish_counts([tuple(ln) for ln in e['icit']['seq']]))
    rd.rec('CS4', 'two is the commonest count in CISI too', 'CISI values %s; ICIT values on the same objects %s' % (dict(cc.most_common(6)), dict(ic.most_common(6))),
           bool(cc) and cc.most_common(1)[0][0] == 2)
    sl = [e for e in objs.values() if len(e['seq']) == 1 and len(e['icit']['seq']) == 1]
    rd.thr('CS5', 'the last sign agrees', 'single-line objects', sum(e['icit']['seq'][0][-1] in P.get(e['seq'][0][-1], set()) for e in sl), len(sl), 0.9)
    last = Counter(ln[-1] for e in objs.values() for ln in e['seq'] if ln)
    rd.rec('CS6', 'the jar is the commonest last sign', 'commonest CISI last signs %s' % dict(last.most_common(5)), last.most_common(1)[0][0] == 'P324')
    a = [not ok for ok, unc, _, _, _ in pos if unc]
    c = [not ok for ok, unc, _, _, _ in pos if not unc]
    rd.gtl('CS7', 'uncertain signs disagree more', 'disagreement, uncertain or damaged positions', a, c)
    a = [not ok for ok, _, rare, _, _ in pos if rare]
    c = [not ok for ok, _, rare, _, _ in pos if not rare]
    rd.gtl('CS8', 'rare signs disagree more', 'disagreement, positions with a rare ICIT glyph', a, c)
    nc = len({g for e in objs.values() for g in flat(e['seq'])})
    ni = len({g for e in objs.values() for g in e['icit']['flat']})
    rd.rec('CS9', 'CISI uses no more distinct signs', 'CISI %d, ICIT %d distinct signs' % (nc, ni), nc <= ni)
    nos = set(objs)
    rest = [tuple(ln) for r in rowsA if r['cisi'].strip() not in nos for ln in r['seq']] + [tuple(t) for t in B]
    before = {}
    for t in rest:
        for i in range(1, len(t)):
            if t[i] in R.END or t[i] in CL:
                before.setdefault(t[i], set()).add(t[i - 1])
    ok = n = 0
    for e in objs.values():
        for ln in e['seq']:
            if len(ln) >= 2:
                ends = [g for g in P.get(ln[-1], set()) if g in before]
                if ends:
                    n += 1
                    ok += any(g in before[x] for x in ends for g in P.get(ln[-2], set()))
    rd.thr('CS10', 'the ending paradigm holds in CISI', 'CISI sign before an ending attested there in ICIT', ok, n, 0.8)
    rd.finish()


if __name__ == '__main__':
    main()
