"""Sixty-seventh registered prediction set (PREDICTIONS.md, TP1-TP10): seal text and seal picture. Writes
results/predict_test67.md."""
import random
from collections import Counter, defaultdict

import rtools as R

random.seed(87)


def same_pairs(texts, ms):
    g = defaultdict(Counter)
    for t, m in zip(texts, ms):
        g[t][m] += 1
    return sum(n * (n - 1) // 2 for c in g.values() for n in c.values())


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Sixty-seventh registered predictions: seal text and seal picture', 'predict_test67')
    full = lambda r: '' if recs[r['sealid']][18].strip() in ('', 'None') else recs[r['sealid']][18].strip()
    pre = lambda r: full(r).split(':')[0].strip()
    txt = lambda r: tuple(tuple(ln) for ln in r['seq'] if ln)
    seals = [r for r in F if r['type'].startswith('SEAL') and full(r)]
    mc = Counter(pre(r) for r in seals)
    top = mc.most_common(1)[0][0]
    rd.say('- seals with a motif %d; motifs: %s.' % (len(seals), ', '.join('%s x%d' % kv for kv in mc.most_common(8))))
    rd.say()
    texts = [txt(r) for r in seals]
    ms = [full(r) for r in seals]
    obs = same_pairs(texts, ms)
    mm = ms[:]
    ge = 0
    for _ in range(R.N):
        random.shuffle(mm)
        ge += same_pairs(texts, mm) >= obs
    p = (ge + 1) / (R.N + 1)
    rd.rec('TP1', 'same text, same picture on seals', 'same-text pairs sharing a motif %d; p = %.4f' % (obs, p), p < 0.05)
    hs = [(pre(r), b[-1], e) for r in seals for b, e in R.names_in(r) if b]
    rd.mi('TP2', 'the picture goes with the head', 'seal names', [m for m, _, _ in hs], [h for _, h, _ in hs])
    rd.mi('TP3', 'the picture goes with the ending', 'seal names', [m for m, _, _ in hs], [e for _, _, e in hs])
    ll = [(pre(r), R.lstrat(len(ln))) for r in seals for ln in r['seq'] if ln]
    rd.mi('TP4', 'the picture goes with the length', 'seal lines', [m for m, _ in ll], [s for _, s in ll])
    tabs = [r for r in F if r['type'].startswith('TAB') and full(r)]
    stext = defaultdict(list)
    for r in seals:
        stext[txt(r)].append(full(r))
    tt = [(txt(r), full(r)) for r in tabs if txt(r) in stext]
    tm = [m for _, m in tt]

    def cross(tms):
        return sum(sum(sm == m for sm in stext[t]) for (t, _), m in zip(tt, tms))
    obs = cross(tm)
    ge = 0
    sh = tm[:]
    for _ in range(R.N):
        random.shuffle(sh)
        ge += cross(sh) >= obs
    p = (ge + 1) / (R.N + 1)
    rd.rec('TP5', 'the picture follows the text across media', 'tablets sharing a seal text %d; seal-tablet pairs with one motif %d; p = %.4f' % (
        len(tt), obs, p), p < 0.05 and len(tt) > 0)
    num = lambda r: any(g in R.NUMS for ln in r['seq'] for g in ln)
    rd.gtl('TP6', 'other animals count', 'numeral, seals with another motif', [num(r) for r in seals if pre(r) != top],
           [num(r) for r in seals if pre(r) == top])
    st = defaultdict(Counter)
    for r in seals:
        for ln in r['seq']:
            for g in ln:
                st[g][pre(r)] += 1
    s10 = [g for g in st if sum(st[g].values()) >= 10]
    spec = [g for g in s10 if any(m != top and n / sum(st[g].values()) >= 0.5 for m, n in st[g].items())]
    rd.thr('TP7', 'some signs belong to a picture', 'signs mostly on one non-commonest motif (%s)' % ', '.join(
        '%s:%s' % (g, st[g].most_common(1)[0][0]) for g in spec[:12]), len(spec), len(s10), 0.2)
    for key, site in (('TP8', 'Mohenjo-daro'), ('TP9', 'Harappa')):
        h = [(m, h_) for r in seals if r['site'].strip() == site for b, _ in R.names_in(r) if b for m, h_ in [(pre(r), b[-1])]]
        rd.mi(key, 'the picture goes with the head at %s' % site, 'seal names', [m for m, _ in h], [x for _, x in h])
    fs = [(pre(r), ln[0]) for r in seals for ln in r['seq'] if ln]
    rd.mi('TP10', 'the picture goes with the first sign', 'seal lines', [m for m, _ in fs], [g for _, g in fs])
    rd.finish()


if __name__ == '__main__':
    main()
