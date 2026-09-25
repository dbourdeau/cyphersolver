"""Two-hundred-and-forty-third registered prediction set (PREDICTIONS.md, MR1-MR3): decipherment loop 68, the phrase-level
referent method on moulded tablets (distinct texts = independent designs). Writes results/predict_test243.md."""
import random

import rtools as R
from predict_test200 import objects
from predict_test237 import qual


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-forty-third registered predictions: decipherment loop 68, referent phrases on moulded tablets', 'predict_test243')
    objs = objects(F, recs, ('TAB:B',))
    q = qual(objs)
    old = qual(objects(F, recs, ('TAB:C', 'TAB:I')))
    new = {p: m for p, m in q.items() if p not in old}
    texts, pics = [t for t, m in objs], [m for t, m in objs]
    rnd = random.Random(243)
    nulls = []
    for _ in range(1000):
        rnd.shuffle(pics)
        nulls.append(len(qual(list(zip(texts, pics)))))
    q95 = sorted(nulls)[949]
    rd.say('- moulded tablets %d; qualifying pairs: %s.' % (len(objs), '; '.join('%s = %s' % (' '.join(p), m) for p, m in sorted(q.items(), key=lambda kv: kv[1]))))
    rd.say()
    rd.rec('MR1', 'more pairs than shuffles', '%d; shuffles median %d, 95th percentile %d' % (len(q), sorted(nulls)[500], q95), len(q) > q95)
    rd.rec('MR2', 'three or more new pairs', '%d new: %s' % (len(new), ', '.join(' '.join(p) for p in new)), len(new) >= 3)
    rd.rec('MR3', 'progress rule', 'MR1 %s, MR2 %s' % (len(q) > q95, len(new) >= 3), len(q) > q95 and len(new) >= 3)
    rd.finish()


if __name__ == '__main__':
    main()
