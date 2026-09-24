"""Hundred-and-forty-fifth registered prediction set (PREDICTIONS.md, MH1-MH8): Mahadevan 2014, the 'merchant of the
city' phrase 255 435 690 740. Writes results/predict_test145.md."""
import math
from collections import Counter

import predict_test13 as T
import rtools as R
from predict_test103 import CL
from predict_test108 import genre

PH = ('255', '435', '690', '740')
M = set(R.END) | set(CL) | {'400', '90'}
BEAR = ('151', '154', '155', '156', '157', '158')


def find(t, sub):
    return [i for i in range(len(t) - len(sub) + 1) if t[i:i + len(sub)] == sub]


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round("Hundred-and-forty-fifth registered predictions: Mahadevan 2014, the 'merchant of the city' phrase", 'predict_test145')
    DL = sorted({tuple(t) for t in A + B})
    ph = [t for t in DL if find(t, PH)]
    rd.say('- distinct lines with the phrase: %d (%s).' % (len(ph), '; '.join(' '.join(t) for t in ph[:30])))
    rd.say()
    comp = sum(t == PH for t in ph)
    rd.rec('MH1', 'a complete text, more often part of longer ones', 'complete %d, longer %d' % (comp, len(ph) - comp), comp >= 1 and len(ph) - comp > comp)
    ab = [t for t in DL if find(t, PH[:2]) and not find(t, PH)]
    cd = [t for t in DL if find(t, PH[2:]) and not find(t, PH)]
    rd.rec('MH2', 'the phrase splits AB | CD', 'AB without CD %d (%s); CD without AB %d' % (len(ab), '; '.join(' '.join(t) for t in ab[:6]), len(cd)), len(ab) >= 3 and len(cd) >= 3)
    ab_other = [t for t in DL for i in find(t, PH[:2]) if i + 3 < len(t) and t[i + 2] != '690' and t[i + 3] == '740']
    rd.rec('MH3', 'AB qualifies other heads', 'AB + X + 740, X not 690: %d (%s)' % (len(ab_other), '; '.join(' '.join(t) for t in ab_other[:6])), len(ab_other) >= 3)
    uni = Counter(g for t in DL for g in t)
    bi = Counter((a, b) for t in DL for a, b in zip(t, t[1:]))
    n1, n2 = sum(uni.values()), sum(bi.values())
    pmi = lambda a, b: math.log((bi[(a, b)] / n2) / ((uni[a] / n1) * (uni[b] / n1))) if bi[(a, b)] else float('-inf')
    v = [pmi(PH[i], PH[i + 1]) for i in range(3)]
    rd.rec('MH4', 'B-C is the weakest junction', 'PMI 255-435 %.2f, 435-690 %.2f, 690-740 %.2f' % tuple(v), v[1] < v[0] and v[1] < v[2])
    lg = [t for t in ph if t != PH]
    fin = [all(g in M for g in t[find(t, PH)[0] + 4:]) for t in lg]
    rd.thr('MH5', 'the phrase ends the text', 'longer texts with the phrase final', sum(fin), len(lg), 0.8)
    toks = [(t, i) for t in DL for i, g in enumerate(t) if g in BEAR]
    # a head is the last body sign: the next sign is the ending 740 or 520
    hd = sum(i + 1 < len(t) and t[i + 1] in R.END for t, i in toks)
    rd.thr('MH6', 'the bearer signs are names', 'bearer tokens as the name head (%s)' % dict(Counter(t[i] for t, i in toks)), hd, len(toks), 0.5)
    sl = sorted({tuple(ln) for r in F if r['type'].startswith('SEAL') for ln in r['seq'] if ln})
    rd.thr('MH7', 'mostly names and titles', 'seal lines, name or closer (%s)' % dict(Counter(genre(t) for t in sl)), sum(genre(t) in ('name', 'closer') for t in sl), len(sl), 0.5)
    sites = Counter(r['site'].strip() for r in F for ln in r['seq'] if find(tuple(ln), PH))
    prev = {t[find(t, PH)[0] - 1] for t in ph if find(t, PH)[0] > 0}
    rd.rec('MH8', 'a title across sites and names', 'sites %s; preceding signs %d (%s)' % (dict(sites), len(prev), ', '.join(sorted(prev))), len(sites) >= 2 and len(prev) >= 5)
    rd.finish()


if __name__ == '__main__':
    main()
