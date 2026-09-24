"""Hundred-and-seventy-eighth registered prediction set (PREDICTIONS.md, DC1-DC7): decipherment loop 3, meanings from
depiction (Fairservis 1992) checked by use on B. Writes results/predict_test178.md."""
import csv
import os
from collections import Counter

import predict_test13 as T
import rtools as R
from signs import FISH, load

CATS = {'A': 'human', 'C': 'animal', 'D': 'animal', 'E': 'plant', 'H': 'tool', 'I': 'tool', 'Q': 'fish'}


def depiction():
    out = {}
    for r in csv.DictReader((l for l in open(os.path.join(R.HERE, 'keys', 'fairservis1992_raw.tsv'), encoding='utf-8') if not l.startswith('#')), delimiter='\t'):
        if r['confidence'] in ('sure', 'likely') and r['icit']:
            c = CATS.get(r['fcode'][:1])
            if c:
                out.setdefault(r['icit'].split('|')[0], c)
    for g in FISH:
        out.setdefault(g, 'fish')
    return out


def main():
    rd = R.Round('Hundred-and-seventy-eighth registered predictions: decipherment loop 3, meanings from depiction checked by use', 'predict_test178')
    dep = depiction()
    Bl = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln})
    ns = sorted({(b, e) for b, e in T.names(Bl) if b})
    rd.say('- depiction classes: %s; B names %d.' % (dict(Counter(dep.values())), len(ns)))
    rd.say()
    passed = []

    def share740(cls):
        xs = [e == '740' for b, e in ns if dep.get(b[-1]) == cls]
        return sum(xs), len(xs)
    for key, cls, lab in (('DC1', 'human', 'human figure'), ('DC2', 'tool', 'weapon or implement'), ('DC4', 'animal', 'animal'), ('DC5', 'plant', 'plant')):
        k, n = share740(cls)
        ok = n >= 10 and k / n >= 0.9
        rd.rec(key, '%s heads take 740' % lab, '%d of %d B names (%.0f%%); needs 10+ names and 90%%' % (k, n, 100 * k / max(1, n)), ok)
        if ok:
            passed.append(cls)
    a = [e == '520' for b, e in ns if dep.get(b[-1]) == 'fish']
    c = [e == '520' for b, e in ns if dep.get(b[-1]) != 'fish']
    p = R.hyper_ge(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c))
    ok = len(a) >= 10 and p < 0.05 and sum(a) / len(a) > sum(c) / len(c)
    rd.rec('DC3', 'fish heads take 520', R.fl(sum(a), len(a), sum(c), len(c), p), ok)
    if ok:
        passed.append('fish')
    it = [(dep[b[-1]], e) for b, e in ns if b[-1] in dep]
    rd.mi('DC6', 'the depiction of the head predicts the ending', 'B names with an identified head', [x for x, e in it], [e for x, e in it])
    rd.rec('DC7', 'at least two classes pass', 'passed: %s' % (', '.join(passed) or 'none'), len(passed) >= 2)
    rd.say('- adopted into M+: %s.' % (', '.join(passed) or 'none'))
    rd.finish()
    return passed


if __name__ == '__main__':
    main()
