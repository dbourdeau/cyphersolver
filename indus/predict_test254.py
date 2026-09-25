"""Two-hundred-and-fifty-fourth registered prediction set (PREDICTIONS.md, RD1-RD3): decipherment loop 79, the phrase-level
referent method with pictured damaged tablets added (their legible runs, never pairing across a gap). Writes
results/predict_test254.md."""
import random
from collections import defaultdict

import rtools as R
from damaged import segments
from predict_test200 import SKIP, objects
from predict_test233 import qualifying
from predict_test237 import merged, qual
from progress import data


def frag_objects(types):
    by = defaultdict(list)
    for s in segments(drop_copies=False):
        if any(s['type'].startswith(t) for t in types) and s['motif'] not in SKIP:
            by[(s['sealid'], s['motif'])].append(s['signs'])
    return [(tuple(x for i, run in enumerate(runs) for x in (('|',) if i else ()) + run), m) for (sid, m), runs in by.items()]


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-fifty-fourth registered predictions: decipherment loop 79, the referent method with the pictured fragments', 'predict_test254')
    pools = {'individually made': ('TAB:C', 'TAB:I'), 'moulded': ('TAB:B',)}
    old, new, ok1 = {}, {}, True
    for lab, types in pools.items():
        clean = objects(F, recs, types)
        frag = frag_objects(types)
        both = clean + frag
        q0 = qual(merged(clean))
        q1 = {p: m for p, m in qual(merged(both)).items() if '|' not in p}
        texts, pics = [t for t, m in both], [m for t, m in both]
        rnd = random.Random(254)
        nulls = []
        for _ in range(1000):
            rnd.shuffle(pics)
            nulls.append(len({p for p in qual(merged(list(zip(texts, pics)))) if '|' not in p}))
        q95 = sorted(nulls)[949]
        rd.say('- %s: %d clean + %d damaged pictured objects; qualifying %d (clean alone %d); shuffles 95th percentile %d; new: %s.' % (
            lab, len(clean), len(frag), len(q1), len(q0), q95, ', '.join('%s=%s' % (' '.join(p), m) for p, m in q1.items() if p not in q0) or 'none'))
        ok1 = ok1 and len(q1) > q95
        old.update(q0)
        new.update({p: m for p, m in q1.items() if p not in q0})
    rd.say()
    rd.rec('RD1', 'more pairs than shuffles in each pool', 'see above', ok1)
    rd.rec('RD2', 'three or more new pairs', '%d new' % len(new), len(new) >= 3)
    DL, tr, te = data()
    ind = objects(F, recs, ('TAB:C', 'TAB:I'))
    mo = objects(F, recs, ('TAB:B',))
    q = qualifying(ind)
    used = {t for t, m in ind} | {t for t, m in mo}
    allp = dict(old)
    allp.update(new)
    tot = sum(len(t) for t in DL)

    def line(pairs):
        cov = 0
        for t in DL:
            if t in q:
                cov += len(t)
                continue
            if t in used:
                mark = set()
                for i in range(len(t) - 1):
                    if t[i:i + 2] in pairs:
                        mark |= {i, i + 1}
                cov += len(mark)
        return cov / tot
    v0, v1 = line(old), line(allp)
    rd.rec('RD3', 'progress rule', 'RD1 %s, RD2 %s; referent line %.2f%% -> %.2f%%' % (ok1, len(new) >= 3, 100 * v0, 100 * v1), ok1 and len(new) >= 3 and v1 > v0)
    rd.finish()


if __name__ == '__main__':
    main()
