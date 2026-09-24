"""Sixty-first registered prediction set (PREDICTIONS.md, SG1-SG10): recurring units inside names. Writes
results/predict_test61.md."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from signs import FISH

random.seed(81)


def units(bodies, k=5):
    c = Counter()
    for b in bodies:
        c.update(set(zip(b, b[1:])))
    return {p for p, n in c.items() if n >= k}


def coverage(bodies):
    u = units(bodies)
    cov = tot = 0
    for b in bodies:
        tot += len(b)
        m = [False] * len(b)
        for i in range(len(b) - 1):
            if (b[i], b[i + 1]) in u:
                m[i] = m[i + 1] = True
        cov += sum(m)
    return cov / max(1, tot)


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Sixty-first registered predictions: recurring units inside names', 'predict_test61')
    bodies = sorted({b for b, _ in T.names(AB) if len(b) >= 2})
    U = units(bodies)
    rd.say('- distinct bodies %d; units %d.' % (len(bodies), len(U)))
    rd.say()
    obs = coverage(bodies)
    ge = 0
    for _ in range(R.N // 10):
        sh = []
        for b in bodies:
            s = list(b)
            random.shuffle(s)
            sh.append(tuple(s))
        ge += coverage(sh) >= obs
    p = (ge + 1) / (R.N // 10 + 1)
    rd.rec('SG1', 'names are built of units', 'coverage %.3f; p = %.4f (1,000 shuffles)' % (obs, p), p < 0.05)
    end = start = 0
    for b in bodies:
        if len(b) >= 3:
            start += (b[0], b[1]) in U
            end += (b[-2], b[-1]) in U
    p = R.binom_ge(end, end + start)
    rd.rec('SG2', 'units close the name', 'units at the end %d, at the start %d; p = %.4f' % (end, start, p), end > start and p < 0.05)
    adj = {p_ for b in bodies for p_ in zip(b, b[1:])}
    rd.thr('SG3', 'units keep their order', 'units never reversed', sum((y, x) not in adj for x, y in U), len(U), 0.9)
    fb = lambda site: {p_ for r in F if r['site'].strip() == site for b, _ in R.names_in(r) for p_ in zip(b, b[1:])}
    md, ha = fb('Mohenjo-daro'), fb('Harappa')
    pres = [u for u in U if u in md or u in ha]
    rd.thr('SG4', 'units are shared by the cities', 'units at both', sum(u in md and u in ha for u in pres), len(pres), 0.7)
    uA = units({b for b, _ in T.names(A)})
    uB = units({b for b, _ in T.names(B)}, 3)
    rd.thr('SG5', 'units hold in the other transcription', "A units recurring in B", sum(u in uB for u in uA), len(uA), 0.6)
    fol = defaultdict(Counter)
    for b in bodies:
        for x, y in zip(b, b[1:]):
            fol[x][y] += 1
    firsts = {x for x, _ in U}
    sh_ = [fol[x].most_common(1)[0][1] / sum(fol[x].values()) for x in firsts]
    rd.rec('SG6', 'the first sign calls the second', 'unit first signs %d; mean share of the commonest follower %.2f; threshold 0.50' % (
        len(firsts), sum(sh_) / len(sh_)), sum(sh_) / len(sh_) >= 0.5)
    rd.thr('SG7', 'units carry numbers', 'units with a numeral', sum(x in R.NUMS or y in R.NUMS for x, y in U), len(U), 0.3)
    rd.thr('SG8', 'units carry fish', 'units with a fish sign', sum(x in FISH or y in FISH for x, y in U), len(U), 0.2)
    long_ = {p_ for b in bodies if len(b) >= 5 for p_ in zip(b, b[1:])} & U
    short = {p_ for b in bodies if 3 <= len(b) <= 4 for p_ in zip(b, b[1:])}
    rd.thr('SG9', 'long names reuse short-name units', 'long-body units also in 3-4 sign bodies', len(long_ & short), len(long_), 0.6)
    rd.thr('SG10', 'units stand alone', 'units attested as whole 2-sign bodies', sum(u in set(bodies) for u in U), len(U), 0.3)
    rd.finish()


if __name__ == '__main__':
    main()
