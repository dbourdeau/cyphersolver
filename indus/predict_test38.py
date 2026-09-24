"""Thirty-eighth registered prediction set (PREDICTIONS.md, LT1-LT10): the longest texts. Writes
results/predict_test38.md."""
import random
from collections import Counter

import rtools as R

random.seed(58)


def ends_name(t):
    t = list(t)
    while t and t[-1] in R.POST:
        t.pop()
    return bool(t) and t[-1] in R.END


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Thirty-eighth registered predictions: the longest texts', 'predict_test38')
    long_ = [t for t in AB if len(t) >= 8]
    mid = [t for t in AB if 5 <= len(t) <= 7]
    rd.say('- long lines %d, middle lines %d.' % (len(long_), len(mid)))
    rd.say()
    two = lambda t: sum(g in R.END for g in t) >= 2
    rd.gtl('LT1', 'long lines hold two names', 'two or more endings, long lines', [two(t) for t in long_], [two(t) for t in mid])
    v = []
    for t in long_:
        idx = [i for i, g in enumerate(t) if g in R.END]
        if idx and idx[0] < len(t) - 1:
            rest = t[idx[0] + 1:]
            while rest and rest[0] in R.POST:
                rest = rest[1:]
            if rest:
                v.append(ends_name(rest))
    rd.thr('LT2', 'the second part is a name too', 'long lines whose remainder closes with an ending', sum(v), len(v), 0.5)
    num = lambda t: any(g in R.NUMS for g in t)
    rd.gtl('LT3', 'long lines carry numbers', 'numeral, long lines', [num(t) for t in long_], [num(t) for t in mid])
    fl_ = [(r, ln) for r in F for ln in r['seq']]
    rd.gtl('LT4', 'long lines are off the seals', 'not a seal, long lines',
           [not r['type'].startswith('SEAL') for r, ln in fl_ if len(ln) >= 8],
           [not r['type'].startswith('SEAL') for r, ln in fl_ if 5 <= len(ln) <= 7])
    rd.gtl('LT5', 'long lines are titled', 'heading, long lines', [R.headed(t) for t in long_], [R.headed(t) for t in mid])
    whole = {tuple(t) for t in AB}

    def splits(t):
        return any(tuple(t[:k]) in whole and tuple(t[k:]) in whole for k in range(2, len(t) - 1))
    obs = sum(splits(t) for t in long_)
    ge = 0
    for _ in range(R.N // 10):
        k = 0
        for t in long_:
            s = list(t)
            random.shuffle(s)
            k += splits(s)
        ge += k >= obs
    p = (ge + 1) / (R.N // 10 + 1)
    rd.rec('LT6', 'long lines are two texts joined', 'long lines splitting into two attested lines %d of %d; p = %.4f (1,000 shuffles)' % (
        obs, len(long_), p), p < 0.05)
    tc = Counter(tuple(r['flat']) for r in F)
    rd.ltl('LT7', 'long texts are unique', 'distinct long texts on 2+ objects',
           [n >= 2 for t, n in tc.items() if len(t) >= 8], [n >= 2 for t, n in tc.items() if 5 <= len(t) <= 7])
    rd.ltl('LT8', 'long lines do not end in a name', 'ending last, long lines', [ends_name(t) for t in long_], [ends_name(t) for t in mid])
    tok = Counter(g for t in AB for g in t)
    rd.gtl('LT9', 'long lines use rare signs', 'rare-sign tokens, long lines',
           [tok[g] <= 5 for t in long_ for g in t], [tok[g] <= 5 for t in mid for g in t])
    rd.gtl('LT10', 'long lines are from Mohenjo-daro', 'Mohenjo-daro, long lines',
           [r['site'].strip() == 'Mohenjo-daro' for r, ln in fl_ if len(ln) >= 8],
           [r['site'].strip() == 'Mohenjo-daro' for r, ln in fl_ if 5 <= len(ln) <= 7])
    rd.finish()


if __name__ == '__main__':
    main()
