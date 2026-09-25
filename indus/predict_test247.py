"""Two-hundred-and-forty-seventh registered prediction set (PREDICTIONS.md, TS1-TS3): decipherment loop 72, sign pairs
tied to a minority find site (toponym or local-title candidates). Writes results/predict_test247.md."""
import random

import rtools as R
from predict_test237 import qual

MAJOR = ('Mohenjo-daro', 'Harappa')


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-forty-seventh registered predictions: decipherment loop 72, phrases tied to a site', 'predict_test247')
    objs = [(tuple(r['flat']), r['site']) for r in F if r['flat'] and r['site']]
    q = qual(objs)
    minor = {p: s for p, s in q.items() if s not in MAJOR}
    texts, sites = [t for t, s in objs], [s for t, s in objs]
    rnd = random.Random(247)
    nulls = []
    for _ in range(1000):
        rnd.shuffle(sites)
        nulls.append(sum(1 for s in qual(list(zip(texts, sites))).values() if s not in MAJOR))
    q95 = sorted(nulls)[949]
    rd.say('- objects %d; pairs bound to a minority site: %s.' % (len(objs), '; '.join('%s = %s' % (' '.join(p), s) for p, s in sorted(minor.items(), key=lambda kv: kv[1])) or 'none'))
    rd.say()
    rd.rec('TS1', 'minority-site pairs above shuffles', '%d; shuffles median %d, 95th percentile %d' % (len(minor), sorted(nulls)[500], q95), len(minor) > q95)
    rd.rec('TS2', 'two or more minority sites', '%s' % sorted(set(minor.values())), len(set(minor.values())) >= 2)
    rd.rec('TS3', 'progress rule', 'TS1 %s' % (len(minor) > q95), len(minor) > q95)
    rd.finish()


if __name__ == '__main__':
    main()
