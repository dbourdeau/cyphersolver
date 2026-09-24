"""Ninety-eighth registered prediction set (PREDICTIONS.md, XM1-XM20): picture labels across media. Writes
results/predict_test98.md."""
import random
from collections import Counter, defaultdict

import rtools as R
from predict_test67 import same_pairs

random.seed(118)
NONE = ('', 'None', '-', 'Unknown')


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Ninety-eighth registered predictions: picture labels across media', 'predict_test98')
    mot = lambda r: '' if recs[r['sealid']][18].strip() in NONE else recs[r['sealid']][18].split(':')[0].strip()
    txt = lambda r: tuple(tuple(ln) for ln in r['seq'] if ln)
    flat = lambda r: tuple(g for ln in r['seq'] if ln for g in ln)
    Cu = [r for r in F if r['type'] == 'TAB:C' and txt(r)]
    Mo = [r for r in F if r['type'] == 'TAB:B' and txt(r)]
    In = [r for r in F if r['type'] == 'TAB:I' and txt(r)]
    Se = [r for r in F if r['type'].startswith('SEAL') and txt(r)]
    rd.say('- copper %d, moulded %d, incised %d, seals %d.' % (len(Cu), len(Mo), len(In), len(Se)))
    rd.say()
    csig = defaultdict(set)
    for r in Cu:
        if mot(r):
            csig[mot(r)].update(flat(r))

    def xm(key, title, objs):
        om = [r for r in objs if mot(r)]
        both = sorted({mot(r) for r in om} & set(csig))
        labs = [mot(r) for r in om]

        def stat(ls):
            s = defaultdict(set)
            for r, l_ in zip(om, ls):
                s[l_].update(flat(r))
            jac = lambda a, b: len(a & b) / max(1, len(a | b))
            same = [jac(csig[m], s[m]) for m in both]
            diff = [jac(csig[m], s[n]) for m in both for n in both if n != m]
            return sum(same) / max(1, len(same)) - sum(diff) / max(1, len(diff))
        obs = stat(labs)
        ll = labs[:]
        ge = 0
        for _ in range(R.N // 10):
            random.shuffle(ll)
            ge += stat(ll) >= obs
        p = (ge + 1) / (R.N // 10 + 1)
        rd.rec(key, title, 'pictures on both %d (%s); same minus different Jaccard %+.3f; p = %.4f (1,000 shuffles)' % (len(both), ', '.join(both), obs, p),
               obs > 0 and p < 0.05)
    xm('XM1', 'copper and moulded labels agree', Mo)
    xm('XM2', 'copper and incised labels agree', In)
    ct = {txt(r) for r in Cu}
    mt = {txt(r) for r in Mo}
    rd.rec('XM3', 'different texts on copper and moulds', 'identical texts on both: %d; threshold 1' % len(ct & mt), len(ct & mt) <= 1)
    mm = {mot(r) for r in Mo if mot(r)}
    rd.thr('XM4', 'the same pictures', 'moulded motif types also on copper', len(mm & set(csig)), len(mm), 0.3)
    cl = sorted({tuple(ln) for r in Cu for ln in r['seq'] if ln})
    ml = sorted({tuple(ln) for r in Mo for ln in r['seq'] if ln})
    lines, labs = cl + ml, [0] * len(cl) + [1] * len(ml)

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
    rd.rec('XM5', 'copper and moulds write differently', 'shared pair types %d; p = %.4f (1,000 shuffles)' % (obs, p), p < 0.05)
    bym = defaultdict(Counter)
    for r in Mo:
        if mot(r):
            bym[mot(r)][txt(r)] += 1
    m5 = [m for m in bym if sum(bym[m].values()) >= 5]
    sh = [bym[m].most_common(1)[0][1] / sum(bym[m].values()) for m in m5]
    rd.rec('XM6', 'each moulded picture has its text', 'motifs %d; mean share %.2f; threshold 0.50' % (len(m5), sum(sh) / max(1, len(sh))), bool(sh) and sum(sh) / len(sh) >= 0.5)
    byt = defaultdict(Counter)
    for r in Mo:
        if mot(r):
            byt[txt(r)][mot(r)] += 1
    t2 = [t for t in byt if sum(byt[t].values()) >= 2]
    rd.thr('XM7', 'each moulded text has its picture', 'repeated texts with one motif', sum(len(byt[t]) == 1 for t in t2), len(t2), 0.8)
    im = [r for r in In if mot(r)]
    obs = same_pairs([txt(r) for r in im], [mot(r) for r in im])
    ms = [mot(r) for r in im]
    ge = 0
    for _ in range(R.N):
        random.shuffle(ms)
        ge += same_pairs([txt(r) for r in im], ms) >= obs
    p = (ge + 1) / (R.N + 1)
    rd.rec('XM8', 'incised text follows picture', 'same-text pairs sharing a motif %d; p = %.4f' % (obs, p), p < 0.05)
    mom = [r for r in Mo if mot(r)]
    rd.thr('XM9', 'moulded pictures are Harappan', 'moulded with motif from Harappa', sum(r['site'].strip() == 'Harappa' for r in mom), len(mom), 0.9)
    num = lambda r: any(g in R.NUMS for g in flat(r))
    rd.ltl('XM10', 'picture labels do not count', 'numeral, moulded with motif', [num(r) for r in mom], [num(r) for r in Mo if not mot(r)])
    rd.thr('XM11', 'moulded labels are short', 'moulded motif texts of 1-3 signs', sum(len(flat(r)) <= 3 for r in mom), len(mom), 0.6)
    rd.rank('XM12', "'Mult' tablets say more", 'Mult against other motif', [len(flat(r)) for r in mom if mot(r) == 'Mult'], [len(flat(r)) for r in mom if mot(r) != 'Mult'])
    lv = lambda r: R.level('Harappa', recs[r['sealid']])
    per = defaultdict(set)
    cnt = Counter()
    for r in mom:
        if lv(r) in ('E', 'L'):
            per[(txt(r), mot(r))].add(lv(r))
            cnt[(txt(r), mot(r))] += 1
    k2 = [k for k in cnt if cnt[k] >= 2]
    rd.thr('XM13', 'picture labels persist', 'dated pairs spanning both periods', sum(len(per[k]) == 2 for k in k2), len(k2), 0.3)
    uni = lambda rs: [mot(r) == 'Bull1' for r in rs if mot(r)]
    rd.ltl('XM14', 'tablets are not unicorn objects', 'unicorn, tablet motifs', uni(Mo + In), uni(Se))
    off = [(r, tuple(ln)) for r in F if r['type'] != 'TAB:C' for ln in r['seq'] if ln]
    t845 = [r['type'] for r, t in off for g in t if g == '845']
    rd.thr('XM15', '845 off copper is on tablets', '845 off-copper tokens on tablets', sum(ty.startswith('TAB') for ty in t845), len(t845), 0.5)
    t407 = [(r, t, i) for r, t in off for i, g in enumerate(t) if g == '407']
    rd.thr('XM16', '407 off copper is on seals', '407 off-copper tokens on seals', sum(r['type'].startswith('SEAL') for r, t, i in t407), len(t407), 0.5)
    a = [('407' in t) for r, t in off if '845' in t]
    c = [('407' in t) for r, t in off if '845' not in t]
    rd.gtl('XM17', '845 and 407 go together', '407, off-copper lines with 845', a, c)
    rd.thr('XM18', '407 closes lines', '407 off-copper tokens line-final', sum(i == len(t) - 1 for r, t, i in t407), len(t407), 0.3)
    s845 = [r['site'].strip() for r, t in off for g in t if g == '845']
    rd.thr('XM19', '845 off copper is Mohenjo-daran', '845 off-copper tokens at Mohenjo-daro', sum(s == 'Mohenjo-daro' for s in s845), len(s845), 0.7)
    cu407 = [(t, i) for r in Cu for t in [flat(r)] for i, g in enumerate(t) if g == '407']
    rd.ltl('XM20', '407 after 845 is a copper formula', '407 after 845, off copper', [i > 0 and t[i - 1] == '845' for r, t, i in t407],
           [i > 0 and t[i - 1] == '845' for t, i in cu407])
    rd.finish()


if __name__ == '__main__':
    main()
