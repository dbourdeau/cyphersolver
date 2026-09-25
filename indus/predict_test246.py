"""Two-hundred-and-forty-sixth registered prediction set (PREDICTIONS.md, OF1-OF3): decipherment loop 71, sign pairs tied
to the object's class (seal, tablet, pottery, tag, other). Writes results/predict_test246.md."""
import random

import rtools as R
from predict_test237 import qual


def cls(t):
    return 'seal' if t.startswith('SEAL') else 'tablet' if t.startswith('TAB') else 'pot' if t.startswith('POT') else 'tag' if t.startswith('TAG') else 'other'


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-forty-sixth registered predictions: decipherment loop 71, phrases tied to what the object was for', 'predict_test246')
    objs = [(tuple(r['flat']), cls(r['type'])) for r in F if r['flat']]
    q = qual(objs)
    minor = {p: m for p, m in q.items() if m in ('pot', 'tag', 'other')}
    texts, cl = [t for t, m in objs], [m for t, m in objs]
    rnd = random.Random(246)
    nulls = []
    for _ in range(1000):
        rnd.shuffle(cl)
        nulls.append(sum(1 for m in qual(list(zip(texts, cl))).values() if m in ('pot', 'tag', 'other')))
    q95 = sorted(nulls)[949]
    rd.say('- objects %d; pairs qualifying for a minority class: %s.' % (len(objs), '; '.join('%s = %s' % (' '.join(p), m) for p, m in sorted(minor.items(), key=lambda kv: kv[1])) or 'none'))
    rd.say()
    rd.rec('OF1', 'minority-class pairs above shuffles', '%d; shuffles median %d, 95th percentile %d' % (len(minor), sorted(nulls)[500], q95), len(minor) > q95)
    pots = [p for p, m in minor.items() if m == 'pot']
    rd.rec('OF2', 'two or more for pottery', '%d' % len(pots), len(pots) >= 2)
    rd.rec('OF3', 'progress rule', 'OF1 %s' % (len(minor) > q95), len(minor) > q95)
    rd.finish()


if __name__ == '__main__':
    main()
