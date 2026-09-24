"""Hundred-and-seventieth registered prediction set (PREDICTIONS.md, C1-C10): follow-ups on content. Writes
results/predict_test170.md."""
import csv
import os
from collections import Counter

import rtools as R
from gulf import IRAN_WEST, WEST
from predict_test112 import runs
from predict_test161 import heading
from signs import FISH

HEAD = ('817', '820', '861')


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-seventieth registered predictions: follow-ups on content', 'predict_test170')
    DL = sorted({tuple(t) for t in A + B})
    two_f = []
    for t in DL:
        for i, j, r in runs(t):
            if j < len(t) and t[j] in FISH and not (i > 0 and t[i - 1] in HEAD) and sum(R.NUMS[g][0] for g in r) == 2:
                two_f.append((t, tuple(r)))
    rd.thr('C1', 'the 2 is the short pair', "distinct lines with '2 + fish' written with sign 2 (%s)" % dict(Counter(r for t, r in two_f)),
           sum(r == ('2',) for t, r in two_f), len(two_f), 0.8)
    nm = [R.name_of(list(t)) for t, r in two_f]
    nm = [x for x in nm if x and x[0]]
    rd.thr('C2', "'2 + fish' is a whole name", "names containing '2 + fish' whose body is just '2 fish'",
           sum(len(b) == 2 and b[0] == '2' and b[1] in FISH for b, e in nm), len(nm), 0.5)
    seals = [r for r in F if r['type'].startswith('SEAL')]
    other = []
    for r in seals:
        ls = [tuple(ln) for ln in r['seq'] if ln]
        if len(ls) == 2:
            isn = [bool(R.name_of(list(x))) for x in ls]
            if isn.count(True) == 1:
                other.append(ls[isn.index(False)])
    rd.thr('C3', 'the second line counts', 'non-name lines with a numeral', sum(any(g in R.NUMS for g in o) for o in other), len(other), 0.5)
    ct = [(tuple(r['flat']), recs[r['sealid']][4].strip()) for r in F if recs[r['sealid']][3] == 'Harappa' and len(r['flat']) == 2
          and r['flat'][1] == '700' and r['flat'][0] in R.NUMS and R.NUMS[r['flat'][0]][1] == 'long' and recs[r['sealid']][4].strip() not in ('--', '')]
    rd.mi('C4', 'count values depend on the unit', 'Harappa count tokens (%s)' % dict(Counter(t[0] for t, u in ct)), [t[0] for t, u in ct], [u for t, u in ct])
    ident = {}
    for r in csv.DictReader((ln for ln in open(os.path.join(R.HERE, 'keys', 'fairservis1992_raw.tsv'), encoding='utf-8') if not ln.startswith('#')), delimiter='\t'):
        if r['confidence'] in ('sure', 'likely') and r['icit']:
            ident.setdefault(r['icit'].split('|')[0], r['fcode'])
    tok = Counter(g for r in F for g in r['flat'])
    onc = Counter(g for r in F if r['type'] == 'TAB:C' for g in r['flat'])
    only = {g for g, n in tok.items() if n >= 2 and onc[g] == n}
    pict = lambda g: ident[g][:1] in ('A', 'B', 'C', 'D')
    rd.gtl('C5', 'copper-only signs are pictures', 'animal or human, copper-only signs (%s)' % ', '.join(sorted(only)),
           [pict(g) for g in only if g in ident], [pict(g) for g in ident if g not in only])
    rl = {tuple(ln) for r in F if recs[r['sealid']][24].strip() == 'R/L' for ln in r['seq'] if ln}
    lr = [tuple(ln) for r in F if recs[r['sealid']][24].strip() == 'L/R' for ln in r['seq'] if len(ln) >= 2]
    rev = sum(t[::-1] in rl and t not in rl for t in lr)
    dirm = sum(t in rl and t[::-1] not in rl for t in lr)
    rd.rec('C6', 'left-to-right texts are reversed copies', 'left-to-right lines %d: matched reversed only %d, as written only %d' % (len(lr), rev, dirm), rev > dirm)
    st = {tuple(r['flat']) for r in seals}
    tg = [r for r in F if r['type'].startswith('TAG')]
    rd.rank('C7', 'matched sealings are shorter', 'length, unmatched against matched sealing texts', [len(r['flat']) for r in tg if tuple(r['flat']) not in st],
            [len(r['flat']) for r in tg if tuple(r['flat']) in st])
    west = lambda r: recs[r['sealid']][2] in WEST or r['site'].strip() in IRAN_WEST
    home = Counter(g for r in F if not west(r) for g in r['flat'])
    rd.gtl('C8', 'foreign lines use rare signs', 'rare-at-home tokens, West Asian', [home[g] < 5 for r in F if west(r) for g in r['flat']],
           [home[g] < 5 for r in F if not west(r) for g in r['flat']])
    rd.ltl('C9', 'no heading on copper', 'heading, copper texts', [heading(tuple(r['flat'])) for r in F if r['type'] == 'TAB:C' and r['flat']],
           [heading(tuple(ln)) for r in seals for ln in r['seq'] if ln])
    rd.gtl('C10', 'sealing names are 740 names', '740, sealing names', [e == '740' for r in tg for b, e in R.names_in(r) if b],
           [e == '740' for r in seals for b, e in R.names_in(r) if b])
    rd.finish()


if __name__ == '__main__':
    main()
