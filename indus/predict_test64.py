"""Sixty-fourth registered prediction set (PREDICTIONS.md, DR1-DR10): lines running the other way. Writes
results/predict_test64.md."""
import random
from collections import Counter

import predict_test13 as T
import rtools as R

random.seed(84)


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Sixty-fourth registered predictions: lines running the other way', 'predict_test64')
    fl = [(r, ln) for r in F for ln in r['seq'] if ln]
    nct = lambda ln: len(ln) >= 2 and ln[-1] == '700' and all(g in R.NUMS for g in ln[:-1])
    rct = lambda ln: len(ln) >= 2 and ln[0] == '700' and all(g in R.NUMS for g in ln[1:])
    cts = [(r, ln, rct(ln)) for r, ln in fl if nct(ln) or rct(ln)]
    rd.say('- count tokens %d, reversed %d.' % (len(cts), sum(x for _, _, x in cts)))
    rd.say()
    rd.gtl('DR1', 'moulds reverse', 'reversed, TAB:B count tokens', [x for r, _, x in cts if r['type'] == 'TAB:B'],
           [x for r, _, x in cts if r['type'] == 'TAB:I'])
    dirs = {r['cisi']: r['direction'] for r in rowsA if r.get('cisi')}
    dj = [(dirs[r['cisi']] == 'L/R', x) for r, _, x in cts if r.get('cisi') in dirs]
    rd.gtl('DR2', 'the catalogue saw the direction', "'L/R', objects with a reversed token", [d for d, x in dj if x], [d for d, x in dj if not x])
    wend = [(r, ln) for r, ln in fl if any(g in R.END for g in ln)]
    rev = lambda ln: len(ln) >= 3 and ln[0] in R.END and ln[-1] not in R.END
    rv = [(r, ln) for r, ln in wend if rev(ln)]
    rd.thr('DR3', 'names also run backwards', 'reversed name lines among lines with 740/520', len(rv), len(wend), 0.02)
    nl = [(r, ln) for r, ln in fl if R.name_of(ln)]
    rd.gtl('DR4', 'reversed names are off the seals', 'off seals, reversed name lines', [not r['type'].startswith('SEAL') for r, _ in rv],
           [not r['type'].startswith('SEAL') for r, _ in nl])
    bodies = {b for b, _ in T.names(AB)}
    rd.thr('DR5', 'read backwards they are names', 'reversed name lines giving an attested body',
           sum(bool(R.name_of(ln[::-1])) and R.name_of(ln[::-1])[0] in bodies for _, ln in rv), len(rv), 0.3)
    rd.thr('DR6', 'reversal is a Harappa habit', 'reversed count tokens from Harappa',
           sum(r['site'].strip() == 'Harappa' for r, _, x in cts if x), sum(x for _, _, x in cts), 0.9)
    anyrev = lambda ln: rct(ln) or rev(ln)
    rd.gtl('DR7', 'graffiti run backwards', 'reversed forms, potsherd lines', [anyrev(ln) for r, ln in fl if r['type'].startswith('POT')],
           [anyrev(ln) for r, ln in fl if r['type'].startswith('SEAL')])
    val = lambda ln: sum(R.NUMS[g][0] for g in ln if g in R.NUMS)
    o, p = R.mi_perm([x for _, _, x in cts], [val(ln) for _, ln, _ in cts])
    rd.rec('DR8', 'the value does not depend on direction', 'MI %.4f bits; p = %.4f' % (o, p), p >= 0.05)
    al = [(r['direction'] == 'L/R', ln) for r in rowsA for ln in r['seq'] if len(ln) >= 2]
    rd.ltl('DR9', 'the direction field matters', "ending last, 'L/R' lines", [ln[-1] in R.END for d, ln in al if d],
           [ln[-1] in R.END for d, ln in al if not d])
    sd = [r['direction'] == 'L/R' for r in rowsA if r['type'].startswith('SEAL') and r['direction'].strip()]
    rd.thr('DR10', 'seals rarely run left to right', "'L/R' seals (%s)" % dict(Counter(r['direction'] for r in rowsA if r['type'].startswith('SEAL'))),
           sum(sd), len(sd), 0.1, above=False)
    rd.finish()


if __name__ == '__main__':
    main()
