"""Three-hundred-and-thirty-sixth registered prediction set (PREDICTIONS.md, BW1-BW3): decipherment loop 161, are the
seal bull units words for the bull? Units learned on the pictured seals alone (site-stratified base rates, set 334's
method, alpha 0.005) whose picture is Bull1: on pictured tablets (clean and fragments), the tablets carrying such a unit
should show a bull (Bull1, Bult, Bull, Bull2) more often than tablets in general, if the unit is a word for the bull;
not, if it marks a seal type. Against 1,000 shuffles of the tablet pictures. Writes results/predict_test336.md."""
import random

import predict_test334 as S
import rtools as R
import referents as X
from predict_test304 import fam

BULLS = {'Bull1', 'Bult', 'Bull', 'Bull2'}


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-thirty-sixth registered predictions: decipherment loop 161, are the seal bull units words for the bull?', 'predict_test336')
    clean, both = S.site_objects(F, recs)
    sclean = [o for o in clean if o[2][1] != 'tab']
    sboth = [o for o in both if o[2][1] != 'tab']
    S.ALPHA = 0.005
    u = S.units(sclean, sboth)
    bull = {k: {g for g, m in v.items() if m == 'Bull1'} for k, v in u.items() if k != 'texts'}
    tabs = [(t, m) for t, m, s in both if s[1] == 'tab']

    def carries(t):
        for (lab, n), gs in bull.items():
            tt = fam(t) if lab.startswith('F') else t
            if any(g in gs for g in X.grams_of(tt, n) if '|' not in g):
                return True
        return False

    hit = [carries(t) for t, m in tabs]
    pics = [m in BULLS for t, m in tabs]
    real = sum(h and p for h, p in zip(hit, pics))
    n = sum(hit)
    base = sum(pics) / len(pics)
    rnd = random.Random(336)
    null = []
    for _ in range(1000):
        rnd.shuffle(pics)
        null.append(sum(h and p for h, p in zip(hit, pics)))
    p = (1 + sum(x >= real for x in null)) / 1001
    pics = [m in BULLS for t, m in tabs]
    rd.say('- %d bull units learned on seals; %d of %d pictured tablets carry one; %d of those show a bull (%.0f%%), tablets overall %.0f%%; shuffles median %d; p = %.3f.' % (sum(len(v) for v in bull.values()), n, len(tabs), real, 100 * real / max(1, n), 100 * base, sorted(null)[500], p))
    rd.say()
    rd.rec('BW1', 'tablets carrying a seal bull unit show a bull more often than chance (p < 0.05)', '%d vs median %d, p = %.3f' % (real, sorted(null)[500], p), p < 0.05)
    rd.rec('BW2', 'at least 10 tablets carry a seal bull unit (enough to test)', '%d' % n, n >= 10)
    rd.rec('BW3', 'progress rule: BW1 and BW2 (a new finding: the seal bull units behave as words for the bull)', 'BW1 %s, BW2 %s' % (p < 0.05, n >= 10), p < 0.05 and n >= 10)
    rd.finish()


if __name__ == '__main__':
    main()
