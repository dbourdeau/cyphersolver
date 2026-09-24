"""Hundred-and-seventeenth registered prediction set (PREDICTIONS.md, OT1-OT15): the lines no genre claims. Writes
results/predict_test117.md."""
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test44 import nonname
from predict_test103 import CL
from predict_test104 import template
from predict_test108 import genre
from signs import FISH

HEAD = ('817', '820', '861')
POST = ('400', '90', '151')


def sub(t):
    tp = template(t)
    if not any(c in tp for c in 'HNEC') and 'F' in tp:
        return 'fishbare'
    if 'E' in tp:
        i = max(k for k, g in enumerate(t) if g in R.END)
        rest = t[i + 1:]
        if rest and not (len(rest) == 1 and rest[0] in POST):
            return 'nametail'
    if any(g in CL for g in t[:-1]):
        return 'closertail'
    if tp.startswith('H') and not tp.startswith('HN'):
        return 'headword'
    return 'rest'


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-seventeenth registered predictions: the lines no genre claims', 'predict_test117')
    DL = sorted({tuple(t) for t in AB})
    O = [t for t in DL if genre(t) == 'other']
    S = defaultdict(list)
    for t in O:
        S[sub(t)].append(t)
    rd.say('- other lines %d: %s.' % (len(O), {k: len(v) for k, v in S.items()}))
    rd.say()
    ns = sorted({(b, e) for b, e in T.names(AB) if b})
    heads = {b[-1] for b, e in ns}
    openers = {b[0] for b, e in ns if len(b) >= 2}
    fb = S['fishbare']
    rd.thr('OT1', 'fish-bare lines end in a head', 'ending in a name head', sum(t[-1] in heads for t in fb), len(fb), 0.5)
    rd.thr('OT2', 'fish-bare lines start with an opener', 'starting with a name opener', sum(t[0] in openers for t in fb), len(fb), 0.5)
    Fn = [r for r in F if r['type'] != 'TAB:C']
    FD = sorted({(r['type'], tuple(ln)) for r in Fn for ln in r['seq'] if ln})
    tp = lambda ty: ty.startswith('TAB') or ty.startswith('POT')
    rd.gtl('OT3', 'fish-bare lines are practical', 'tablet or potsherd, fish-bare', [tp(ty) for ty, t in FD if genre(t) == 'other' and sub(t) == 'fishbare'],
           [tp(ty) for ty, t in FD if genre(t) == 'name'])
    tails = []
    for t in S['nametail']:
        i = max(k for k, g in enumerate(t) if g in R.END)
        tails.append(t[i + 1:])
    rd.thr('OT4', 'name tails are short', 'tails of 1-3 signs', sum(1 <= len(x) <= 3 for x in tails), len(tails), 0.8)
    ct = []
    for t in S['closertail']:
        i = max(k for k, g in enumerate(t[:-1]) if g in CL)
        ct.append((t[i], t[i + 1:]))
    rd.thr('OT5', 'closer tails are short', 'tails of 1-2 signs', sum(1 <= len(x) <= 2 for c, x in ct), len(ct), 0.8)
    rd.thr('OT6', 'closers are followed by counts or suffixes', 'first tail sign a numeral or 400/90/151 (%s)' % dict(Counter(x[0] for c, x in ct).most_common(5)),
           sum(x[0] in R.NUMS or x[0] in POST for c, x in ct), len(ct), 0.4)
    hw = S['headword']
    rd.thr('OT7', '368 fills the heading slot', "second sign 368 (%s)" % dict(Counter(t[1] for t in hw if len(t) > 1).most_common(5)), sum(len(t) > 1 and t[1] == '368' for t in hw), len(hw), 0.4)

    def unassigned(lines):
        o = [t for t in lines if genre(t) == 'other']
        return sum(sub(t) == 'rest' for t in o), len(lines)
    k, n = unassigned(DL)
    rd.thr('OT8', 'the leftovers are extensions of known genres', 'lines left unassigned', k, n, 0.05, above=False)
    rd.thr('OT9', 'name tails are counts, suffixes or closers', 'first tail sign a closer, numeral or 400/90/151 (%s)' % dict(Counter(x[0] for x in tails).most_common(6)),
           sum(x[0] in CL or x[0] in R.NUMS or x[0] in POST for x in tails), len(tails), 0.5)
    fin = [t[-1] for t in DL if t and t[-1] in CL]
    rd.gtl('OT10', '151 and 156 take tails', '151/156, closers with a tail', [c in ('151', '156') for c, x in ct], [c in ('151', '156') for c in fin])
    bsig = {g for b, e in ns for g in b}
    fo = lambda t: any(g not in bsig and g not in R.NUMS for g in t)
    bare = [t for t in DL if genre(t) == 'bare']
    rd.ltl('OT11', 'fish-bare lines use name signs', 'formula-only sign, fish-bare', [fo(t) for t in fb], [fo(t) for t in bare])
    rd.gtl('OT12', "'other' lines are seal lines", "seal, 'other' lines", [ty.startswith('SEAL') for ty, t in FD if genre(t) == 'other'],
           [ty.startswith('SEAL') for ty, t in FD if genre(t) == 'bare'])
    objs = defaultdict(set)
    for r in Fn:
        for ln in r['seq']:
            if ln:
                objs[tuple(ln)].add(r['sealid'])
    ft = sorted({t for ty, t in FD})
    rd.gtl('OT13', "'other' texts are one-off", "one object, 'other' texts", [len(objs[t]) == 1 for t in ft if genre(t) == 'other'],
           [len(objs[t]) == 1 for t in ft if genre(t) == 'name'])
    k, n = unassigned(sorted({tuple(t) for t in B}))
    rd.thr('OT14', 'the leftovers are extensions (B)', 'lines left unassigned', k, n, 0.05, above=False)
    k, n = unassigned(ft)
    rd.thr('OT15', "the leftovers are extensions (F')", 'lines left unassigned', k, n, 0.05, above=False)
    rd.say('- remaining unassigned examples: %s.' % '; '.join(' '.join(t) for t in S['rest'][:12]))
    rd.finish()


if __name__ == '__main__':
    main()
