"""Ninety-fourth registered prediction set (PREDICTIONS.md, CU1-CU20): copper tablets and their pictures. Writes
results/predict_test94.md."""
import random
from collections import Counter, defaultdict

import rtools as R
from predict_test67 import same_pairs

random.seed(114)
HEAD = ('817', '820', '861')
NONE = ('', 'None', '-', 'Unknown')


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Ninety-fourth registered predictions: copper tablets and their pictures', 'predict_test94')
    mot = lambda r: '' if recs[r['sealid']][18].strip() in NONE else recs[r['sealid']][18].split(':')[0].strip()
    txt = lambda r: tuple(tuple(ln) for ln in r['seq'] if ln)
    C = [r for r in F if r['type'] == 'TAB:C' and txt(r)]
    Cm = [r for r in C if mot(r)]
    rd.say('- copper tablets %d, with a motif %d; motifs %s.' % (len(C), len(Cm), dict(Counter(mot(r) for r in Cm).most_common(8))))
    rd.say()
    texts = [txt(r) for r in Cm]
    ms = [mot(r) for r in Cm]
    obs = same_pairs(texts, ms)
    mm = ms[:]
    ge = 0
    for _ in range(R.N):
        random.shuffle(mm)
        ge += same_pairs(texts, mm) >= obs
    p = (ge + 1) / (R.N + 1)
    rd.rec('CU1', 'same text, same picture', 'same-text pairs sharing a motif %d; p = %.4f' % (obs, p), p < 0.05)
    rd.mi('CU2', 'the picture sets the text', 'tablets with a motif', ms, texts)
    bym = defaultdict(Counter)
    for r in Cm:
        bym[mot(r)][txt(r)] += 1
    m5 = [m for m in bym if sum(bym[m].values()) >= 5]
    share = [bym[m].most_common(1)[0][1] / sum(bym[m].values()) for m in m5]
    rd.rec('CU3', 'each picture has its text', 'motifs %d; mean commonest-text share %.2f; threshold 0.50' % (len(m5), sum(share) / max(1, len(share))),
           bool(share) and sum(share) / len(share) >= 0.5)
    byt = defaultdict(Counter)
    for r in Cm:
        byt[txt(r)][mot(r)] += 1
    t2 = [t for t in byt if sum(byt[t].values()) >= 2]
    rd.thr('CU4', 'each text has its picture', 'repeated texts with one motif', sum(len(byt[t]) == 1 for t in t2), len(t2), 0.8)
    for key, m, lab in (('CU5', 'Anth', 'anthropomorph'), ('CU6', 'Hare', 'hare')):
        c = bym.get(m, Counter())
        n = sum(c.values())
        k = c.most_common(1)[0][1] if n else 0
        rd.thr(key, 'the %s tablets carry one text' % lab, '%s tablets with the commonest text (%s)' % (lab, ' '.join(' '.join(x) for x in c.most_common(1)[0][0]) if n else '-'),
               k, n, 0.8)
    tc = Counter(txt(r) for r in C)
    rd.gtl('CU7', 'repeated labels have pictures', 'motif, repeated-text tablets', [bool(mot(r)) for r in C if tc[txt(r)] >= 2], [bool(mot(r)) for r in C if tc[txt(r)] == 1])
    rd.mi('CU8', 'the picture sets the length', 'tablets with a motif', ms, [R.lstrat(sum(len(x) for x in t)) for t in texts])
    seals = [r for r in F if r['type'].startswith('SEAL') and mot(r)]
    ssig = defaultdict(set)
    for r in seals:
        for ln in r['seq']:
            ssig[mot(r)].update(ln)
    csig = lambda labs: {m: {g for r, l_ in zip(Cm, labs) if l_ == m for ln in txt(r) for g in ln} for m in set(labs)}
    both = [m for m in set(ms) if m in ssig and m != 'Othr']

    def jstat(labs):
        cs = csig(labs)
        same = [len(cs[m] & ssig[m]) / max(1, len(cs[m] | ssig[m])) for m in both if m in cs]
        diff = [len(cs[m] & ssig[n]) / max(1, len(cs[m] | ssig[n])) for m in both if m in cs for n in both if n != m]
        return sum(same) / max(1, len(same)) - sum(diff) / max(1, len(diff))
    obs = jstat(ms)
    ge = 0
    mm = ms[:]
    for _ in range(R.N // 10):
        random.shuffle(mm)
        ge += jstat(mm) >= obs
    p = (ge + 1) / (R.N // 10 + 1)
    rd.rec('CU9', 'the animal has its signs across media', 'animals on both %d (%s); same minus different Jaccard %+.3f; p = %.4f (1,000 shuffles)' % (
        len(both), ', '.join(sorted(both)), obs, p), obs > 0 and p < 0.05)
    rd.thr('CU10', 'few labels', 'distinct copper texts (at most 60)', len(tc), len(C), 60 / len(C), above=False)
    sealtok = {g for r in F if r['type'].startswith('SEAL') for ln in r['seq'] for g in ln}
    ct = [g for r in C for ln in txt(r) for g in ln]
    rd.thr('CU11', 'copper has its own signs', 'copper tokens never on seals', sum(g not in sealtok for g in ct), len(ct), 0.2)
    cl = [ln for r in C for ln in txt(r)]
    sl = [tuple(ln) for r in F if r['type'].startswith('SEAL') for ln in r['seq'] if ln]
    rd.thr('CU12', 'copper counts', 'copper lines with a numeral', sum(any(g in R.NUMS for g in ln) for ln in cl), len(cl), 0.4)
    rd.gtl('CU13', 'copper uses long strokes', 'long kind, copper numerals', [R.kind(g) == 'long' for ln in cl for g in ln if g in R.NUMS],
           [R.kind(g) == 'long' for ln in sl for g in ln if g in R.NUMS])
    rd.ltl('CU14', 'copper is not headed', 'heading first, copper lines', [ln[0] in HEAD for ln in cl], [ln[0] in HEAD for ln in sl])
    rd.thr('CU15', 'copper rarely ends in 740', 'copper lines ending in 740', sum(ln[-1] == '740' for ln in cl), len(cl), 0.4, above=False)
    isn = lambda r: any(R.name_of(list(ln)) for ln in txt(r))
    rd.gtl('CU16', 'animal tablets carry names', 'name, animal-motif tablets', [isn(r) for r in Cm if mot(r) != 'Othr'], [isn(r) for r in Cm if mot(r) == 'Othr'])
    oth = [txt(r) for r in Cm if mot(r) == 'Othr']
    ani = [txt(r) for r in Cm if mot(r) != 'Othr']
    ro, ra = len(set(oth)) / max(1, len(oth)), len(set(ani)) / max(1, len(ani))
    rd.rec('CU17', "'other' tablets are varied", 'distinct texts per tablet: Othr %.2f, animals %.2f' % (ro, ra), ro > ra)
    rd.rec('CU18', 'copper labels are one line', 'two-line copper tablets %d; threshold 5' % sum(len(txt(r)) >= 2 for r in C), sum(len(txt(r)) >= 2 for r in C) <= 5)
    hd = [t[-1][-1] for t in texts]
    obs = same_pairs(hd, ms)
    ge = 0
    mm = ms[:]
    for _ in range(R.N):
        random.shuffle(mm)
        ge += same_pairs(hd, mm) >= obs
    p = (ge + 1) / (R.N + 1)
    rd.rec('CU19', 'the picture sets the last sign', 'same-last-sign pairs sharing a motif %d; p = %.4f' % (obs, p), p < 0.05)
    lines = sorted(set(cl)) + sorted(set(sl))
    labs = [0] * len(set(cl)) + [1] * len(set(sl))

    def shared(lb):
        a, c = set(), set()
        for t, l_ in zip(lines, lb):
            (a if l_ == 0 else c).update(zip(t, t[1:]))
        return len(a & c)
    obs = shared(labs)
    lb = labs[:]
    le = 0
    for _ in range(R.N // 10):
        random.shuffle(lb)
        le += shared(lb) <= obs
    p = (le + 1) / (R.N // 10 + 1)
    rd.rec('CU20', 'copper and seals write differently', 'shared pair types %d; p = %.4f (1,000 shuffles)' % (obs, p), p < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
