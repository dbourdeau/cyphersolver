"""Relabel f. 139 with the f. 134 values (duca, Fiorentini) and scan single unmatched signs for a value.
For each frequent unmatched shape (@NN) every candidate value (letters, syllables, doubles) is tried alone, with the rest of
the labelled transcription fixed; the score is the mean log-probability per letter of the stretches of >= 3 valued signs under
it-cinquecento without spaces (as table_test.py). Control: the same scan on a table sign that is hidden (does the scan restore
its table value?). Run from the repository root: PYTHONUTF8=1 python targets/tranchedini1446/relabel.py"""
import os, sys, collections, random
sys.path.insert(0, os.getcwd()); sys.path.insert(0, 'targets/tranchedini1446')
import solver2 as S
from lang import lm
m = S.m
ALIAS = {'@102': '@12'}
runs = [[ALIAS.get(S.base(t), S.base(t)) if t.startswith('@') else t for t in r] for r in S.load_runs()]
def fixedval(t, words):
    if t in ('VENEZIANI', 'SFORZA'): return ('duca' if t == 'VENEZIANI' else 'fiorentini') if words else None
    v, c = S.cands(t)
    return v if c is None else None
def stretches(mp, words=False):
    out = []
    for r in runs:
        cur = []
        for t in r:
            v = mp.get(t) if t in mp else fixedval(t, words)
            if v is None:
                if len(cur) >= 3: out.append(''.join(cur))
                cur = []
            else: cur.append(v)
        if len(cur) >= 3: out.append(''.join(cur))
    return out
def score(mp, words=False):
    tot = n = 0
    for s in stretches(mp, words):
        s = lm.norm(s, 'early')
        if len(s) >= 3: tot += m.per_char(s) * len(s); n += len(s)
    return tot / n, n
def scan(t, mp, words=False):
    res = []
    for v in S.POOL:
        d = dict(mp); d[t] = v; res.append((score(d, words)[0], v))
    return sorted(res, reverse=True)
if __name__ == '__main__':
    cnt = collections.Counter(t for r in runs for t in r)
    base_s, base_n = score({})
    print('baseline (table only): %.3f over %d letters in %d runs' % (base_s, base_n, len(runs)))
    print('with duca/fiorentini as words: %.3f over %d letters' % score({}, True))
    unm = [(c, t) for t, c in cnt.items() if t.startswith('@') and c >= 5]
    print('\nsingle-sign scans (unmatched shapes with >= 5 uses):')
    for c, t in sorted(unm, reverse=True):
        r = scan(t, {})
        print('  %-5s x%-2d best %-3s %.3f | 2nd %-3s %.3f | 3rd %-3s %.3f | gain %+.3f' % (t, c, r[0][1], r[0][0], r[1][1], r[1][0], r[2][1], r[2][0], r[0][0] - base_s))
    print('\ncontrol: hide one table sign (its tokens become unmatched), scan all values, see whether the table value comes back:')
    for sg in ['u', 'a', 'e', 're', 'o', 'te', 'i', 'n', 'm', 'p', 'c', "a'", "o''", 'du']:
        true = S.val(sg)
        if true is None or sg not in cnt: continue
        hb = score({sg: None})[0]
        res = sorted(((score({sg: v})[0], v) for v in S.POOL), reverse=True)
        rk = [v for _, v in res].index(true) + 1
        print('  %-4s x%-2d table %-3s rank %2d of %d; best %-3s %.3f; table %.3f; hidden baseline %.3f' % (sg, cnt[sg], true, rk, len(res), res[0][1], res[0][0], dict((v, s_) for s_, v in res)[true], hb))
