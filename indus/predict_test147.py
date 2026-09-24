"""Hundred-and-forty-seventh registered prediction set (PREDICTIONS.md, CR1-CR7): how many names existed
(capture-recapture across Mohenjo-daro and Harappa seals). Writes results/predict_test147.md."""
from collections import Counter

import rtools as R


def chapman(n1, n2, m):
    return (n1 + 1) * (n2 + 1) / (m + 1) - 1


def chao1(counts):
    s = len(counts)
    f1 = sum(1 for v in counts.values() if v == 1)
    f2 = sum(1 for v in counts.values() if v == 2)
    return s + (f1 * f1 / (2 * f2) if f2 else f1 * (f1 - 1) / 2), f1, f2


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-forty-seventh registered predictions: how many names existed', 'predict_test147')
    seals = [r for r in F if r['type'].startswith('SEAL') and recs[r['sealid']][3] in ('Mohenjo-daro', 'Harappa')]
    nm = {'Mohenjo-daro': Counter(), 'Harappa': Counter()}
    hd = {'Mohenjo-daro': Counter(), 'Harappa': Counter()}
    for r in seals:
        s = recs[r['sealid']][3]
        for b, e in {x for x in R.names_in(r) if x[0]}:
            nm[s][(b, e)] += 1
            hd[s][b[-1]] += 1
    M, H = set(nm['Mohenjo-daro']), set(nm['Harappa'])
    obs = len(M | H)
    lp = chapman(len(M), len(H), len(M & H))
    rd.say('- seals %d; distinct names Mohenjo-daro %d, Harappa %d, both %d, together %d.' % (len(seals), len(M), len(H), len(M & H), obs))
    rd.say()
    rd.rec('CR1', 'a large name population', 'Lincoln-Petersen (Chapman) %.0f against %d observed (%.1fx); threshold 3x' % (lp, obs, lp / obs), lp >= 3 * obs)
    pooled = nm['Mohenjo-daro'] + nm['Harappa']
    c1, f1, f2 = chao1(pooled)
    rd.rec('CR2', 'Chao1 names', 'Chao1 %.0f (f1 %d, f2 %d) against %d observed (%.1fx); threshold 2x' % (c1, f1, f2, obs, c1 / obs), c1 >= 2 * obs)
    Mh, Hh = set(hd['Mohenjo-daro']), set(hd['Harappa'])
    ho = len(Mh | Hh)
    lph = chapman(len(Mh), len(Hh), len(Mh & Hh))
    rd.rec('CR3', 'heads are a closed set', 'heads: Mohenjo-daro %d, Harappa %d, both %d, together %d; Lincoln-Petersen %.0f (%.2fx); threshold at most 1.5x' % (
        len(Mh), len(Hh), len(Mh & Hh), ho, lph, lph / ho), lph <= 1.5 * ho)
    rd.thr('CR4', 'most names are on one seal', 'distinct names on exactly one seal', f1, obs, 0.6)
    both = M & H
    a = [e == '520' for b, e in both]
    c = [e == '520' for b, e in (M | H) - both]
    rd.gtl('CR5', 'shared names are 520 names', '520, names in both cities', a, c)
    rd.rank('CR6', 'shared names are shorter', 'body length, one-city against both-city names (positive = one-city longer)',
            [len(b) for b, e in (M | H) - both], [len(b) for b, e in both])
    ph = hd['Mohenjo-daro'] + hd['Harappa']
    ch, g1, g2 = chao1(ph)
    rd.rec('CR7', 'Chao1 heads', 'Chao1 %.0f (f1 %d, f2 %d) against %d observed (%.2fx); threshold at most 1.5x' % (ch, g1, g2, ho, ch / ho), ch <= 1.5 * ho)
    rd.say('- names in both cities: %s.' % '; '.join(' '.join(b) + ' ' + e for b, e in sorted(both)[:40]))
    rd.finish()


if __name__ == '__main__':
    main()
