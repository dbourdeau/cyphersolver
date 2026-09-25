"""Two-hundred-and-eighty-second registered prediction set (PREDICTIONS.md, MR1-MR4): decipherment loop 107, the frozen
restoration predictions (set 255, committed in 002427952) against Mahadevan's 1977 readings of the same gaps
(results/restoration_m77.tsv, m77_gaps.py). Cases: gap lines of 4+ signs whose aligned M77 lines all give the same
legible sign. Writes results/predict_test282.md."""
import csv
import os
from collections import Counter

import rtools as R
from progress import data

HERE = os.path.dirname(os.path.abspath(__file__))


def tsv(name):
    with open(os.path.join(HERE, 'results', name), encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def main():
    rd = R.Round('Two-hundred-and-eighty-second registered predictions: decipherment loop 107, frozen restorations against Mahadevan 1977', 'predict_test282')
    preds = {(r['id'], r['line'], r['pos']): [r['top%d' % k] for k in range(1, 6)] for r in tsv('restoration_predictions.tsv')}
    cases = [r for r in tsv('restoration_m77.tsv') if r['reading'] not in ('no match', 'conflict', 'illegible') and len(r['text_with_gap'].split()) >= 4]
    DL, tr, te = data()
    top = Counter(g for t in DL for g in t).most_common(1)[0][0]
    h1 = h5 = hb = 0
    for r in cases:
        cand = preds[(r['id'], r['line'], r['pos'])]
        g = r['reading']
        h1 += cand[0] == g
        h5 += g in cand
        hb += top == g
        rd.say('- %s %s: M77 %s; predicted %s.' % (r['cisi'] or r['id'], r['text_with_gap'], g, ' '.join(cand)))
    n = len(cases)
    rd.say()
    rd.rec('MR1', 'top-1 matches the M77 reading in 25%+ of 10+ cases', '%d of %d' % (h1, n), n >= 10 and h1 >= 0.25 * n)
    rd.rec('MR2', 'top-5 contains it in 50%+', '%d of %d' % (h5, n), n >= 10 and h5 >= 0.5 * n)
    rd.rec('MR3', 'top-1 beats the frequency baseline (%s)' % top, 'top-1 %d against %d' % (h1, hb), n >= 10 and h1 > hb)
    rd.rec('MR4', 'progress rule: MR1 and MR3 (tier 3 gains its first line)', 'MR1 %s, MR3 %s' % (n >= 10 and h1 >= 0.25 * n, n >= 10 and h1 > hb), n >= 10 and h1 >= 0.25 * n and h1 > hb)
    rd.finish()


if __name__ == '__main__':
    main()
