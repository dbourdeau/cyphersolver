"""Sixty-eighth registered prediction set (PREDICTIONS.md, CP1-CP10): tablets that copy seal texts. Writes
results/predict_test68.md."""
import random
from collections import Counter, defaultdict

import rtools as R

random.seed(88)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Sixty-eighth registered predictions: tablets that copy seal texts', 'predict_test68')
    full = lambda r: '' if recs[r['sealid']][18].strip() in ('', 'None') else recs[r['sealid']][18].strip()
    seal = [(r, tuple(ln)) for r in F if r['type'].startswith('SEAL') for ln in r['seq'] if len(ln) >= 2]
    tab = [(r, tuple(ln)) for r in F if r['type'].startswith('TAB') for ln in r['seq'] if len(ln) >= 2]
    sl = Counter(t for _, t in seal)
    ssites = defaultdict(set)
    for r, t in seal:
        ssites[t].add(r['site'].strip())
    tset = {t for _, t in tab}
    cp = lambda t: t in sl
    rd.say('- seal lines %d, tablet lines %d, copied tablet lines %d.' % (len(seal), len(tab), sum(cp(t) for _, t in tab)))
    rd.say()
    items = [(cp(t), R.lstrat(len(t)), 1 if R.name_of(list(t)) else 0) for _, t in tab]
    rd.strat('CP1', 'tablets copy names', 'names, copied minus other tablet lines', items)
    dist = list(sl)
    rd.rank('CP2', 'popular seal texts are copied', 'copied against uncopied seal texts', [sl[t] for t in dist if t in tset],
            [sl[t] for t in dist if t not in tset])
    ct = [(r, t) for r, t in tab if cp(t)]
    rd.thr('CP3', 'copying is a Harappa practice', 'copied tablet lines from Harappa', sum(r['site'].strip() == 'Harappa' for r, _ in ct), len(ct), 0.8)
    sites = [r['site'].strip() for r, _ in ct]
    same = lambda ss: sum(s in ssites[t] for s, (_, t) in zip(ss, ct))
    obs = same(sites)
    sh = sites[:]
    ge = 0
    for _ in range(R.N):
        random.shuffle(sh)
        ge += same(sh) >= obs
    p = (ge + 1) / (R.N + 1)
    rd.rec('CP4', 'copies are local', 'copied lines matching a seal site %d of %d; p = %.4f' % (obs, len(ct), p), p < 0.05)
    tobj = [r for r in F if r['type'].startswith('TAB')]
    hc = lambda r: any(tuple(ln) in sl for ln in r['seq'] if len(ln) >= 2)
    rd.gtl('CP5', 'copies carry the picture', 'motif, tablets with a copied line', [bool(full(r)) for r in tobj if hc(r)],
           [bool(full(r)) for r in tobj if not hc(r)])
    rd.rank('CP6', 'copied seal texts are short', 'uncopied against copied seal lines', [len(t) for _, t in seal if t not in tset],
            [len(t) for _, t in seal if t in tset])
    sm = [(any(tuple(ln) in tset for ln in r['seq'] if len(ln) >= 2), full(r).split(':')[0].strip() == 'Bull1')
          for r in F if r['type'].startswith('SEAL') and full(r)]
    rd.ltl('CP7', 'the unicorn is not copied', 'unicorn, copied seals', [u for c, u in sm if c], [u for c, u in sm if not c])
    pat = set()
    for t in sl:
        for i in range(len(t)):
            pat.add(t[:i] + ('*',) + t[i + 1:])
    near = sum(1 for _, t in tab if t not in sl and any(t[:i] + ('*',) + t[i + 1:] in pat for i in range(len(t))))
    exact = len(ct)
    rd.rec('CP8', 'copies are exact', 'exact %d, near %d; threshold exact >= 2 x near' % (exact, near), exact >= 2 * near)
    num = lambda t: any(g in R.NUMS for g in t)
    rd.ltl('CP9', 'copies do not count', 'numeral, copied tablet lines', [num(t) for _, t in tab if cp(t)], [num(t) for _, t in tab if not cp(t)])
    sn = [(t in tset, R.name_of(list(t))[1] == '740') for _, t in seal if R.name_of(list(t))]
    rd.gtl('CP10', 'copied names take 740', '740, copied seal name lines', [e for c, e in sn if c], [e for c, e in sn if not c])
    rd.finish()


if __name__ == '__main__':
    main()
