"""Ninety-sixth registered prediction set (PREDICTIONS.md, LB1-LB20): how the copper labels are built. Writes
results/predict_test96.md."""
from collections import Counter, defaultdict

import rtools as R

NONE = ('', 'None', '-', 'Unknown')


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Ninety-sixth registered predictions: how the copper labels are built', 'predict_test96')
    mot = lambda r: '' if recs[r['sealid']][18].strip() in NONE else recs[r['sealid']][18].split(':')[0].strip()
    C = [r for r in F if r['type'] == 'TAB:C' and any(r['seq'])]
    line = lambda r: tuple(g for ln in r['seq'] if ln for g in ln)
    DT = sorted({line(r) for r in C})
    animal = lambda m: m not in ('', 'Othr')
    seals = [r for r in F if r['type'].startswith('SEAL')]
    sl = [(r, tuple(ln)) for r in seals for ln in r['seq'] if ln]
    sset = Counter(t for r, t in sl)
    rd.say('- copper tablets %d, distinct texts %d.' % (len(C), len(DT)))
    rd.say()
    w407 = [t for t in DT if '407' in t]
    before = lambda t: '845' in t[:t.index('407')]
    rd.thr('LB1', '845 comes before 407', 'texts with 407 and 845 before it', sum(before(t) for t in w407), len(w407), 0.7)
    has = lambda t, a, b: a in t and b in t and t.index(a) < len(t) - 1 - t[::-1].index(b)
    t845 = [r for r in C if has(line(r), '845', '407')]
    rd.thr('LB2', "'845 ... 407' goes with animals", 'tablets with an animal or figure motif', sum(animal(mot(r)) for r in t845), len(t845), 0.7)
    jar = lambda t: any(t[i] in ('705', '706') and t[i + 1] == '33' for i in range(len(t) - 1))
    tj = [r for r in C if jar(line(r))]
    rd.thr('LB3', "'705/706 33' goes with animals", 'tablets with an animal or figure motif', sum(animal(mot(r)) for r in tj), len(tj), 0.9)
    rd.rec('LB4', 'the elephant label is on a seal', "seal lines '706 33 923 740': %d" % sset[('706', '33', '923', '740')], sset[('706', '33', '923', '740')] >= 1)
    rd.rec('LB5', "the 'Othr' label is a seal name", "seal lines '503 615 752 740': %d; threshold 5" % sset[('503', '615', '752', '740')], sset[('503', '615', '752', '740')] >= 5)
    cm = defaultdict(set)
    for r in C:
        if mot(r):
            cm[line(r)].add(mot(r))
    sm = [(mot(r), cm[t]) for r, t in sl if t in cm and mot(r)]
    rd.thr('LB6', 'the seal shows the same picture', 'seals with a copper text carrying its motif', sum(m in ms for m, ms in sm), len(sm), 0.5)
    sg = defaultdict(Counter)
    for r in C:
        for g in set(line(r)):
            sg[g][mot(r) or '(none)'] += 1
    s3 = [g for g in sg if sum(sg[g].values()) >= 3]
    rd.thr('LB7', 'signs belong to pictures', 'signs with 80%+ of copper tokens under one motif', sum(max(sg[g].values()) / sum(sg[g].values()) >= 0.8 for g in s3), len(s3), 0.5)
    allt = [(r['type'] == 'TAB:C', g) for r in F for ln in r['seq'] for g in ln]
    for key, s, th in (('LB8', '845', 0.3), ('LB9', '407', 0.2)):
        k = [c for c, g in allt if g == s]
        rd.thr(key, '%s is a copper sign' % s, '%s tokens on copper' % s, sum(k), len(k), th)
    cl = [t for t in DT]
    sll = sorted(set(t for r, t in sl))
    a1 = lambda t: any(t[i] == '740' and t[i + 1] == '1' for i in range(len(t) - 1))
    rd.gtl('LB10', 'copper adds 1 after 740', "'740 1', copper lines", [a1(t) for t in cl], [a1(t) for t in sll])
    aft = lambda t: '740' in t and t.index('740') < len(t) - 1
    rd.gtl('LB11', 'copper adds a tail after 740', 'sign after 740, copper lines with 740', [aft(t) for t in cl if '740' in t],
           [aft(t) for t in sll if '740' in t and R.name_of(list(t))])
    bym = defaultdict(Counter)
    for r in C:
        if mot(r):
            bym[mot(r)][line(r)] += 1
    m3 = [m for m in bym if sum(bym[m].values()) >= 3]
    sh = [bym[m].most_common(1)[0][1] / sum(bym[m].values()) for m in m3]
    rd.rec('LB12', 'the label is copied whole', 'motifs %d; mean commonest-label share %.2f; threshold 0.60' % (len(m3), sum(sh) / max(1, len(sh))), bool(sh) and sum(sh) / len(sh) >= 0.6)
    multi = [t for t, ms in cm.items() if len(ms) >= 2]
    rd.rec('LB13', 'one label, one picture', 'labels under 2+ motifs %d (%s); threshold 2' % (len(multi), '; '.join(' '.join(t) for t in multi)), len(multi) <= 2)
    rd.rank('LB14', 'copper labels are long', 'copper against seal lines', [len(t) for t in cl], [len(t) for t in sll])
    rd.thr('LB15', 'labels end in 407', 'distinct copper texts ending in 407', sum(t[-1] == '407' for t in DT), len(DT), 0.15)
    q = [(line(r), i) for r in C for i, g in enumerate(line(r)) if g in ('421', '422', '423', '424')]
    rd.thr('LB16', "'3 42x' is a unit", '421-424 tokens after 3', sum(i > 0 and t[i - 1] == '3' for t, i in q), len(q), 0.8)
    mt = {line(r) for r in C if mot(r)}
    nm = [r for r in C if not mot(r)]
    rd.thr('LB17', 'pictureless tablets carry picture labels', 'no-motif tablets with a motif-tablet text', sum(line(r) in mt for r in nm), len(nm), 0.3)
    ss = Counter(r['site'].strip() for r, t in sl if t in set(DT))
    rd.rec('LB18', 'copper texts are Mohenjo-daro seal texts', 'seal matches at Mohenjo-daro %d, Harappa %d' % (ss['Mohenjo-daro'], ss['Harappa']), ss['Mohenjo-daro'] > ss['Harappa'])
    an = ('806', '845', '61', '407', '850', '900', '740')
    rd.rec('LB19', 'the anthropomorph label is copper-only', 'seal lines with it: %d' % sset[an], sset[an] == 0)
    o = sset[('777',)] + sset[('782',)]
    so = sum(g in ('777', '782') for r, t in sl for g in t)
    rd.rec('LB20', 'one-sign labels are copper-only', 'seal tokens of 777 or 782: %d' % so, so == 0)
    rd.finish()


if __name__ == '__main__':
    main()
