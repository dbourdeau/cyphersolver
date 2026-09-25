"""Two-hundred-and-thirty-third registered prediction set (PREDICTIONS.md, RF1-RF4): decipherment loop 58, texts on 3+
individually made pictured objects (copper, incised tablets) with one picture on 80%+ of them. Writes
results/predict_test233.md."""
import random
from collections import Counter, defaultdict

import rtools as R
from predict_test200 import objects
from progress import data


def qualifying(objs):
    g = defaultdict(list)
    for t, m in objs:
        g[t].append(m)
    out = {}
    for t, ms in g.items():
        if len(ms) >= 3:
            k, v = Counter(ms).most_common(1)[0]
            if v / len(ms) >= 0.8:
                out[t] = k
    return out


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-thirty-third registered predictions: decipherment loop 58, texts whose referent the picture fixes', 'predict_test233')
    objs = objects(F, recs, ('TAB:C', 'TAB:I'))
    q = qualifying(objs)
    texts = [t for t, m in objs]
    pics = [m for t, m in objs]
    rnd = random.Random(233)
    ge = 0
    for _ in range(1000):
        rnd.shuffle(pics)
        ge += len(qualifying(list(zip(texts, pics)))) >= len(q)
    p = (ge + 1) / 1001
    rd.say('- individually made pictured objects %d; texts on 3+ of them %d.' % (len(objs), sum(1 for t, c in Counter(texts).items() if c >= 3)))
    rd.say('- qualifying: %s.' % '; '.join('%s = %s' % (' '.join(t), m) for t, m in sorted(q.items(), key=lambda kv: kv[1])))
    rd.say()
    rd.rec('RF1', 'more qualifying texts than shuffles', '%d qualifying; shuffles as many %d of 1000 (p = %.4f)' % (len(q), ge, p), p < 0.05)
    rd.rec('RF2', 'three or more', '%d' % len(q), len(q) >= 3)
    shared = [m for m, n in Counter(q.values()).items() if n > 1]
    rd.rec('RF3', 'each label specific to its scene', 'pictures shared by several qualifying texts: %s' % (', '.join(shared) or 'none'), not shared)
    DL, tr, te = data()
    tot = sum(len(t) for t in DL)
    vref = sum(len(t) for t in DL if t in q) / tot
    rd.rec('RF4', 'progress rule', 'RF1 %s, RF2 %s; referent-fixed share of tokens %.2f%%' % (p < 0.05, len(q) >= 3, 100 * vref), p < 0.05 and len(q) >= 3)
    rd.finish()


if __name__ == '__main__':
    main()
