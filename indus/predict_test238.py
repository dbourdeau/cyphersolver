"""Two-hundred-and-thirty-eighth registered prediction set (PREDICTIONS.md, SR1-SR3): decipherment loop 63, the phrase-level
referent method on seals and their animals. Writes results/predict_test238.md."""
import random

import rtools as R
from predict_test200 import objects
from predict_test237 import qual


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-thirty-eighth registered predictions: decipherment loop 63, the referent method on seals', 'predict_test238')
    objs = objects(F, recs, ('SEAL:S', 'SEAL:R'))
    q = qual(objs)
    nb = {p: m for p, m in q.items() if m != 'Bull1'}
    texts, pics = [t for t, m in objs], [m for t, m in objs]
    rnd = random.Random(238)
    n1, n2 = [], []
    for _ in range(1000):
        rnd.shuffle(pics)
        qq = qual(list(zip(texts, pics)))
        n1.append(len(qq))
        n2.append(sum(1 for m in qq.values() if m != 'Bull1'))
    q1, q2 = sorted(n1)[949], sorted(n2)[949]
    rd.say('- seals %d; qualifying pairs not the one-horned bull: %s.' % (len(objs), '; '.join('%s = %s' % (' '.join(p), m) for p, m in nb.items()) or 'none'))
    rd.say()
    rd.rec('SR1', 'more pairs than shuffles', '%d qualifying; shuffles median %d, 95th percentile %d' % (len(q), sorted(n1)[500], q1), len(q) > q1)
    rd.rec('SR2', 'other animals than the one-horned bull', '%d; shuffles median %d, 95th percentile %d' % (len(nb), sorted(n2)[500], q2), len(nb) > q2)
    rd.rec('SR3', 'progress rule', 'SR2 %s' % (len(nb) > q2), len(nb) > q2)
    rd.finish()


if __name__ == '__main__':
    main()
