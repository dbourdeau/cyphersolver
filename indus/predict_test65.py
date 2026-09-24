"""Sixty-fifth registered prediction set (PREDICTIONS.md, MT1-MT10): moulded against incised tablets. Writes
results/predict_test65.md."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test44 import nonname

random.seed(85)


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Sixty-fifth registered predictions: moulded against incised tablets', 'predict_test65')
    tb = [r for r in F if r['type'] in ('TAB:B', 'TAB:I')]
    mb = lambda r: r['type'] == 'TAB:B'
    txt = lambda r: tuple(tuple(ln) for ln in r['seq'] if ln)
    # the field holds the string 'None' where no motif is recorded
    mot = lambda r: '' if recs[r['sealid']][18].strip() in ('', 'None') else recs[r['sealid']][18].strip()
    rd.say('- TAB:B %d, TAB:I %d.' % (sum(map(mb, tb)), len(tb) - sum(map(mb, tb))))
    rd.say()
    tcB = Counter(txt(r) for r in tb if mb(r))
    tcI = Counter(txt(r) for r in tb if not mb(r))
    rd.gtl('MT1', 'moulded texts repeat', 'distinct texts on 2+ objects, TAB:B', [n >= 2 for n in tcB.values()], [n >= 2 for n in tcI.values()])
    ln_ = lambda r: sum(len(x) for x in txt(r))
    rd.rank('MT2', 'moulded texts are short', 'TAB:I against TAB:B lengths', [ln_(r) for r in tb if not mb(r)], [ln_(r) for r in tb if mb(r)])
    items = [(not mb(r), R.lstrat(len(ln)), 1 if R.name_of(ln) else 0) for r in tb for ln in r['seq'] if len(ln) >= 2]
    rd.strat('MT3', 'moulded tablets carry fewer names', 'names, TAB:I minus TAB:B', items)
    rd.thr('MT4', 'moulding is a Harappa craft', 'TAB:B from Harappa', sum(r['site'].strip() == 'Harappa' for r in tb if mb(r)),
           sum(map(mb, tb)), 0.8)
    rd.gtl('MT5', 'moulded tablets have pictures', 'motif recorded, TAB:B', [bool(mot(r)) for r in tb if mb(r)], [bool(mot(r)) for r in tb if not mb(r)])
    bm = [r for r in tb if mb(r) and mot(r)]
    rd.say('- TAB:B motifs: %s.' % ', '.join('%s x%d' % kv for kv in Counter(mot(r) for r in bm).most_common(6)))
    rd.mi('MT6', 'the picture goes with the text', 'TAB:B with a motif', [mot(r) for r in bm], [txt(r) for r in bm])
    texts = [txt(r) for r in bm]
    mots = [mot(r) for r in bm]

    def same(ms):
        g = defaultdict(Counter)
        for t, m in zip(texts, ms):
            g[t][m] += 1
        return sum(n * (n - 1) // 2 for c in g.values() for n in c.values())
    obs = same(mots)
    mm = mots[:]
    ge = 0
    for _ in range(R.N):
        random.shuffle(mm)
        ge += same(mm) >= obs
    p = (ge + 1) / (R.N + 1)
    rd.rec('MT7', 'the same text, the same picture', 'same-text pairs sharing a motif %d; p = %.4f' % (obs, p), p < 0.05)
    num = lambda t: any(g in R.NUMS for g in t)
    items = [(mb(r), R.lstrat(len(ln)), 1 if num(ln) else 0) for r in tb for ln in r['seq'] if len(ln) >= 2]
    rd.strat('MT8', 'moulded tablets count', 'numeral, TAB:B minus TAB:I', items)
    bsig = {g for b, _ in T.names(AB) for g in b}
    fo = lambda r: any(g not in R.NUMS and g not in bsig for ln in r['seq'] if nonname(ln) for g in ln)
    rd.ltl('MT9', 'moulded texts are stereotyped', 'formula-only sign, TAB:B', [fo(r) for r in tb if mb(r)], [fo(r) for r in tb if not mb(r)])
    seal = {tuple(ln) for r in F if r['type'].startswith('SEAL') for ln in r['seq'] if ln}
    rd.gtl('MT10', 'moulded tablets copy seals', 'line also on a seal, TAB:B', [tuple(ln) in seal for r in tb if mb(r) for ln in r['seq'] if ln],
           [tuple(ln) in seal for r in tb if not mb(r) for ln in r['seq'] if ln])
    rd.finish()


if __name__ == '__main__':
    main()
