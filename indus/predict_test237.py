"""Two-hundred-and-thirty-seventh registered prediction set (PREDICTIONS.md, PL1-PL4): decipherment loop 62, the
picture-referent method on adjacent sign pairs across individually made pictured tablets. Writes
results/predict_test237.md."""
import random
from collections import Counter, defaultdict

import rtools as R
from predict_test200 import objects


def qual(objs):
    occ = defaultdict(list)
    texts = defaultdict(set)
    for t, m in objs:
        for p in {t[i:i + 2] for i in range(len(t) - 1)}:
            occ[p].append(m)
            texts[p].add(t)
    out = {}
    for p, ms in occ.items():
        if len(ms) >= 3 and len(texts[p]) >= 2:
            k, v = Counter(ms).most_common(1)[0]
            if v / len(ms) >= 0.8:
                out[p] = k
    return out


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-thirty-seventh registered predictions: decipherment loop 62, the referent method at phrase level', 'predict_test237')
    objs = objects(F, recs, ('TAB:C', 'TAB:I'))
    q = qual(objs)
    texts, pics = [t for t, m in objs], [m for t, m in objs]
    rnd = random.Random(237)
    nulls = []
    for _ in range(1000):
        rnd.shuffle(pics)
        nulls.append(len(qual(list(zip(texts, pics)))))
    q95 = sorted(nulls)[949]
    rd.say('- qualifying pairs: %s.' % '; '.join('%s = %s' % (' '.join(p), m) for p, m in sorted(q.items(), key=lambda kv: kv[1])))
    rd.say()
    rd.rec('PL1', 'more pairs than shuffles', '%d qualifying; shuffles median %d, 95th percentile %d' % (len(q), sorted(nulls)[500], q95), len(q) > q95)
    rd.rec('PL2', 'three or more (2+ distinct texts each, by construction)', '%d' % len(q), len(q) >= 3)
    used = {t for t, m in objs}
    ext = sum(1 for r in F for ln in r['seq'] if ln and tuple(ln) not in used for i in range(len(ln) - 1) if tuple(ln[i:i + 2]) in q)
    rd.rec('PL3', 'occurrences elsewhere (reported)', '%d pair occurrences on lines not among those used' % ext, True)
    rd.rec('PL4', 'progress rule', 'PL1 %s, PL2 %s' % (len(q) > q95, len(q) >= 3), len(q) > q95 and len(q) >= 3)
    rd.finish()


if __name__ == '__main__':
    main()


def merged(objs):
    """Audit after set 247: a text that is a contiguous part of a longer text among the objects is the same text read in
    part; map it to the longer one before counting distinct texts."""
    def sub(a, b):
        n = len(a)
        return any(b[i:i + n] == a for i in range(len(b) - n + 1))
    texts = sorted({t for t, m in objs}, key=lambda t: (-len(t), t))  # deterministic tie order
    rep = {}
    for t in texts:
        r = next((u for u in texts if len(u) > len(t) and sub(t, u) and rep.get(u) == u), None)
        rep[t] = r if r else t
    return [(rep[t], m) for t, m in objs]
