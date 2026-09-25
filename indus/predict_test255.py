"""Two-hundred-and-fifty-fifth registered prediction set (PREDICTIONS.md, RS1-RS4): decipherment loop 80, blind
restoration of illegible signs checked on the CISI vol. 1 photographs. Compares results/restoration_readings.tsv
(photo readings, recorded without the predictions in view) with the frozen results/restoration_predictions.tsv.
Writes results/predict_test255.md."""
import csv
import os
from collections import Counter

import rtools as R

HERE = os.path.dirname(os.path.abspath(__file__))


def tsv(name):
    with open(os.path.join(HERE, 'results', name), encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def main():
    rd = R.Round('Two-hundred-and-fifty-fifth registered predictions: decipherment loop 80, blind restoration vs CISI photographs', 'predict_test255')
    reads = tsv('restoration_readings.tsv')
    ids = {w['cisi'].strip(): (w['id'], w['line'], w['pos']) for w in tsv('restoration_worklist.tsv')}
    preds = {(r['id'], r['line'], r['pos']): [r['top%d' % k] for k in range(1, 6)] for r in tsv('restoration_predictions.tsv')}
    st = Counter(r['reading'] for r in reads)
    ok = [r for r in reads if r['reading'] not in ('illegible', 'not examined')]
    rd.say('- worklist objects in CISI vol. 1: %d; examined %d; readable %d (%s).' % (len(reads), len(reads) - st['not examined'], len(ok), ', '.join('%s %d' % kv for kv in st.most_common())))
    rd.say()
    A, B, rowsA, recs, F = R.load_all()
    top = Counter(g for t in F for ln in t['seq'] for g in ln).most_common(1)[0][0]
    h1 = h5 = hb = 0
    for r in ok:
        cand = preds[ids[r['cisi']]]
        h1 += cand[0] == r['reading']
        h5 += r['reading'] in cand
        hb += top == r['reading']
    n = len(ok)
    rd.rec('RS1', 'top-1 >= 25%, at least 10 readable', '%d readable; top-1 %d' % (n, h1), n >= 10 and h1 >= 0.25 * n)
    rd.rec('RS2', 'top-5 >= 50%', '%d readable; top-5 %d' % (n, h5), n >= 10 and h5 >= 0.5 * n)
    rd.rec('RS3', 'top-1 beats frequency baseline', 'top-1 %d vs baseline (%s) %d on %d' % (h1, top, hb, n), n >= 10 and h1 > hb)
    rd.rec('RS4', 'progress rule (RS1 and RS3)', 'not met: no readable gap sign', False)
    rd.finish()


if __name__ == '__main__':
    main()
