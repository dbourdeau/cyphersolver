"""Two-hundred-and-fifty-eighth registered prediction set (PREDICTIONS.md, RC1-RC3): decipherment loop 83, the frozen
restoration predictions (set 255) against Parpola's own transcription (CISI digitisation, cisi.py) where it reads a
gap that ICIT marks illegible. Writes results/predict_test258.md."""
import csv
import os

import cisi
import rtools as R

HERE = os.path.dirname(os.path.abspath(__file__))
# (CISI object, position of the gap in the ICIT line, Parpola's sign at that position, his uncertainty %)
CASES = [('M-62', 1, 'P310', 0), ('M-61', 5, 'P251', 90)]


def tsv(name):
    with open(os.path.join(HERE, 'results', name), encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def main():
    rd = R.Round('Two-hundred-and-fifty-eighth registered predictions: decipherment loop 83, frozen restorations against Parpola\'s transcription', 'predict_test258')
    pm = cisi.p2icit()
    ids = {w['cisi'].strip(): (w['id'], w['line'], w['pos']) for w in tsv('restoration_worklist.tsv')}
    preds = {(r['id'], r['line'], r['pos']): [r['top%d' % k] for k in range(1, 6)] for r in tsv('restoration_predictions.tsv')}
    res = {}
    for obj, pos, p, unc in CASES:
        k = ids[obj]
        assert int(k[2]) == pos, (obj, k)
        cand = preds[k]
        ok = pm[p]
        res[obj] = (cand[0] in ok, bool(ok & set(cand)))
        rd.say('- %s: Parpola %s = ICIT %s (uncertainty %d%%); predicted %s.' % (obj, p, '/'.join(sorted(ok)), unc, ' '.join(cand)))
    rd.say()
    rd.rec('RC1', 'M-62 (certain reading): ICIT 700 in the top 5', 'top-5 %s' % res['M-62'][1], res['M-62'][1])
    rd.rec('RC2', 'M-61 (uncertain reading): one of Parpola\'s ICIT equivalents in the top 5', 'top-5 %s' % res['M-61'][1], res['M-61'][1])
    rd.rec('RC3', 'progress rule: not applicable (fewer than 10 cases; consistency only)', 'n = 2', False)
    rd.finish()


if __name__ == '__main__':
    main()
