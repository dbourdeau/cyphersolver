"""Three-hundred-and-thirty-eighth registered prediction set (PREDICTIONS.md, MC1-MC4): decipherment loop 163, the referent
pool with only true duplicates collapsed: objects from the same mould (moulded tablets, TAB:B) and seal impressions
(tags) with the same text count once; seals, copper and incised tablets, each made by hand, count as separate objects.
Set 334's stratified binomial (alpha 0.005), FDR over the collapsed observations with within-stratum shuffles. The
figure replaces set 337's 1.09% whatever it is (registered before measuring); not counted as progress, since the
counting unit is re-decided after set 337. Writes results/predict_test338.md."""
from collections import Counter, defaultdict

import predict_test334 as S
import rtools as R
import referents as X
from damaged import segments
from predict_test200 import SKIP
from predict_test237 import merged
from predict_test304 import coverage
from predict_test335 import fdr
from progress import data

TYPES = ('TAB:C', 'TAB:I', 'TAB:B', 'SEAL:S', 'SEAL:R', 'SEAL', 'SEAL:C', 'SEAL:CY', 'TAG')


def dup(ty):
    return ty.startswith('TAB:B') or ty.startswith('TAG')


def objects_typed(F, recs):
    clean, frag = [], []
    for r in F:
        rec = recs.get(r['sealid'])
        if not rec or not any(rec[20].startswith(t) for t in TYPES):
            continue
        m = rec[18].split(':')[0]
        if m in SKIP or not r['flat']:
            continue
        clean.append((tuple(r['flat']), m, (rec[3], S.cls(rec[20])), dup(rec[20]), r['sealid']))
    by = defaultdict(list)
    for s in segments(drop_copies=False):
        if any(s['type'].startswith(t) for t in TYPES) and s['motif'] not in SKIP:
            by[(s['sealid'], s['motif'], (s['site'], S.cls(s['type'])), dup(s['type']))].append(s['signs'])
    for (sid, m, st, d), runs in by.items():
        frag.append((tuple(x for i, run in enumerate(runs) for x in (('|',) if i else ()) + run), m, st, d, 'f' + sid))
    allo = clean + frag
    mg = merged([(o[0], o[1]) for o in allo])
    both = [(t, o[1], o[2], o[3], o[4]) for (t, _), o in zip(mg, allo)]
    return clean, both


def collapse(objs):
    g = defaultdict(list)
    for t, m, s, d, oid in objs:
        g[(t, s[1]) if d else (t, oid)].append((m, s))
    out = []
    for (t, _), ms in g.items():
        out.append((t, Counter(x for x, s in ms).most_common(1)[0][0], Counter(s for x, s in ms).most_common(1)[0][0]))
    return out


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-thirty-eighth registered predictions: decipherment loop 163, the referent pool with true duplicates collapsed', 'predict_test338')
    DL, tr, te = data()
    clean, both = objects_typed(F, recs)
    S.ALPHA = 0.005
    cc, cb = collapse(clean), collapse(both)
    P = {'made': ([(o[0], o[1]) for o in clean], [(o[0], o[1]) for o in both])}
    u = S.units(cc, cb)
    n, f = fdr(cc, cb, 338)
    nb = {k: {g: m for g, m in v.items() if m != 'Bull1'} for k, v in u.items()}
    c, cnb = coverage(DL, P, u), coverage(DL, P, nb)
    rd.say('- %d objects -> %d observations (mould copies and impressions collapsed); %d units (%d Bull1), FDR %.1f%%; coverage %.2f%% (without Bull1 units %.2f%%); set 337 1.09%%.' % (len(both), len(cb), n, sum(1 for k, v in u.items() for g, m in v.items() if m == 'Bull1'), 100 * f, 100 * c, 100 * cnb))
    rd.say()
    rd.rec('MC1', 'FDR <= 10%', '%.1f%%' % (100 * f), f <= 0.10)
    rd.rec('MC2', 'coverage above 1.09% (set 337)', '%.2f%%' % (100 * c), c > 0.0109)
    rd.rec('MC3', 'without Bull1 units above 0.99%', '%.2f%%' % (100 * cnb), cnb > 0.0099)
    rd.rec('MC4', 'progress rule: none (the counting unit is re-decided after set 337; the figure replaces 1.09% if MC1 holds)', 'MC1 %s' % (f <= 0.10), False)
    rd.finish()


if __name__ == '__main__':
    main()
