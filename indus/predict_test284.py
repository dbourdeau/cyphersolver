"""Two-hundred-and-eighty-fourth registered prediction set (PREDICTIONS.md, MN1-MN4): decipherment loop 109, the
copy-free restoration check (set 283) replicated on new cases: ICIT lines of 4+ signs with exactly one illegible sign
(any position, broken edges allowed), not in set 255's worklist, whose aligned M77 lines agree on one legible sign
(m77_gaps alignment). Each case: model retrained without copies of the gap line (predict_test283.copy_of), top 5 of
the 150 commonest signs, compared with M77. Writes results/predict_test284.md and results/restoration_m77_new.tsv."""
import csv
import os
from collections import Counter

import icit_full
import rtools as R
from m77_gaps import DEFAULT, m77_lines
from predict_test283 import copy_of, predict
from progress import data

HERE = os.path.dirname(os.path.abspath(__file__))


def new_cases():
    R.load_all()
    icit_full.LINES_REVERSED = True
    with open(os.path.join(HERE, 'results', 'restoration_worklist.tsv'), encoding='utf-8') as f:
        old = {(w['id'], w['line'], w['pos']) for w in csv.DictReader(f, delimiter='\t')}
    L = m77_lines(DEFAULT)
    out = []
    for rec in icit_full.records(R.FPATH):
        for li, ln in enumerate(icit_full.lines_of(rec[34])):
            s = ln['signs']
            if len(s) < 4 or sum(g is None for g in s) != 1 or '?' in s:
                continue
            k = s.index(None)
            if (rec[0], str(li), str(k)) in old:
                continue
            t = tuple('???' if g is None else g for g in s)
            vals = Counter(m[k] for mid, m in L if len(m) == len(t) and sum(a != b for j, (a, b) in enumerate(zip(t, m)) if j != k) <= (1 if len(t) >= 5 else 0))
            if len(vals) == 1 and next(iter(vals)) not in ('000', '?'):
                out.append((rec[0], rec[1], li, k, t, next(iter(vals))))
    return out


def main():
    rd = R.Round('Two-hundred-and-eighty-fourth registered predictions: decipherment loop 109, the copy-free restoration check on new cases', 'predict_test284')
    DL, tr, te = data()
    cases = new_cases()
    top = Counter(g for x in DL for g in x).most_common(1)[0][0]
    h1 = h5 = hb = 0
    rows = []
    for sid, cisi, li, k, t, g in cases:
        train = [u for u in DL if not copy_of(t, k, u)]
        cands = [c for c, n in Counter(c for x in train for c in x).most_common(150)]
        pred = predict(train, t, k, cands)
        h1 += pred[0] == g
        h5 += g in pred
        hb += top == g
        rows.append((sid, cisi, str(li), str(k), ' '.join(t), g, str(len(DL) - len(train)), ' '.join(pred)))
    with open(os.path.join(HERE, 'results', 'restoration_m77_new.tsv'), 'w', encoding='utf-8', newline='') as f:
        f.write('id\tcisi\tline\tpos\ttext_with_gap\tm77\tcopies_removed\tpredicted_top5\n')
        for r in rows:
            f.write('\t'.join(r) + '\n')
    n = len(cases)
    rd.say('- %d new cases (%d distinct texts); rows in results/restoration_m77_new.tsv.' % (n, len({r[4] for r in rows})))
    rd.say()
    rd.rec('MN1', 'top-1 matches the M77 reading in 25%+ (10+ cases)', '%d of %d' % (h1, n), n >= 10 and h1 >= 0.25 * n)
    rd.rec('MN2', 'top-5 contains it in 50%+', '%d of %d' % (h5, n), n >= 10 and h5 >= 0.5 * n)
    rd.rec('MN3', 'top-1 beats the frequency baseline (%s)' % top, 'top-1 %d against %d' % (h1, hb), n >= 10 and h1 > hb)
    rd.rec('MN4', 'progress rule: MN1 and MN3 on the new cases', 'MN1 %s, MN3 %s' % (n >= 10 and h1 >= 0.25 * n, n >= 10 and h1 > hb), n >= 10 and h1 >= 0.25 * n and h1 > hb)
    rd.finish()


if __name__ == '__main__':
    main()
