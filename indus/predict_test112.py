"""Hundred-and-twelfth registered prediction set (PREDICTIONS.md, NS1-NS20): the number system across genres. Writes
results/predict_test112.md."""
from collections import Counter

import rtools as R
from predict_test103 import CL
from predict_test108 import genre


def runs(t):
    out, i = [], 0
    while i < len(t):
        if t[i] in R.NUMS:
            j = i
            while j < len(t) and t[j] in R.NUMS:
                j += 1
            out.append((i, j, t[i:j]))
            i = j
        else:
            i += 1
    return out


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-twelfth registered predictions: the number system across genres', 'predict_test112')
    DL = sorted({tuple(t) for t in AB})
    G = {g: [t for t in DL if genre(t) == g] for g in ('name', 'count', 'closer', 'bare', 'other')}
    val = lambda r: sum(R.NUMS[g][0] for g in r)
    allr = [(genre(t), r) for t in DL for i, j, r in runs(t)]
    rd.say('- runs %d; by genre %s.' % (len(allr), dict(Counter(g for g, r in allr))))
    rd.say()

    def tier(lines, key, lab):
        nt = [g for t in lines for g in t if g in R.NUMS]
        rd.gtl(key, 'tiered for large numbers%s' % lab, 'tiered, 5-8', [R.kind(g) == 'tiered' for g in nt if 5 <= R.NUMS[g][0] <= 8],
               [R.kind(g) == 'tiered' for g in nt if 1 <= R.NUMS[g][0] <= 4])
    tier(G['name'], 'NS1', ' in names')
    tier(G['count'], 'NS2', ' in counts')
    tier(G['closer'], 'NS3', ' in closer lines')
    gv = [(g, min(val(r), 8)) for g, r in allr if g != 'other']
    rd.mi('NS4', 'the genre sets the value', 'runs', [a for a, _ in gv], [b for _, b in gv])
    gk = [(genre(t), R.kind(g)) for t in DL for g in t if g in R.NUMS and genre(t) != 'other']
    rd.mi('NS5', 'the genre sets the notation', 'numerals', [a for a, _ in gk], [b for _, b in gk])
    cr = [(t, j) for t in G['closer'] for i, j, r in runs(t)]
    rd.thr('NS6', 'closer numbers sit inside', 'closer-line runs not directly before the closer', sum(not (j == len(t) - 1 and t[-1] in CL) for t, j in cr), len(cr), 0.7)
    tops = {g: Counter(val(r) for g_, r in allr if g_ == g).most_common(1)[0][0] for g in ('name', 'count', 'closer')}
    rd.rec('NS7', 'three is the commonest number everywhere', 'commonest value by genre: %s' % tops, all(v == 3 for v in tops.values()))
    rd.ltl('NS8', 'counts are small', 'value 5+, count runs', [val(r) >= 5 for g, r in allr if g == 'count'], [val(r) >= 5 for g, r in allr if g == 'name'])
    cr2 = [r for g, r in allr if g == 'count']
    rd.thr('NS9', 'compound numbers in counts', 'count runs of 2+ signs', sum(len(r) >= 2 for r in cr2), len(cr2), 0.05)

    def ns10(lines, key, lab):
        r2 = [r for t in lines for i, j, r in runs(t) if len(r) == 2 and R.NUMS[r[0]][0] != R.NUMS[r[1]][0]]
        rd.thr(key, 'the larger part comes first%s' % lab, '2-sign runs with the larger value first', sum(R.NUMS[r[0]][0] > R.NUMS[r[1]][0] for r in r2), len(r2), 0.7)
    ns10(DL, 'NS10', '')
    ng = {}
    for t in DL:
        for g in t:
            if g in R.NUMS:
                ng.setdefault(g, Counter())[genre(t)] += 1
    n10 = [g for g in ng if sum(ng[g].values()) >= 10]
    rd.thr('NS11', 'one number set for all genres', 'numeral signs (10+) in 2+ genres', sum(len([k for k in ng[g] if k != 'other']) >= 2 for g in n10), len(n10), 1.0)
    Fn = [r for r in F if r['type'] != 'TAB:C']
    FD = sorted({(r['type'][:3], tuple(ln)) for r in Fn for ln in r['seq'] if ln})
    ct = [(ty, g) for ty, t in FD if genre(t) == 'count' for g in t if g in R.NUMS]
    rd.gtl('NS12', 'seal counts are tiered', 'tiered, seal count numerals', [R.kind(g) == 'tiered' for ty, g in ct if ty == 'SEA'], [R.kind(g) == 'tiered' for ty, g in ct if ty == 'TAB'])
    nb = [(R.name_of(list(t))[0], i) for t in G['name'] for i in [0] if R.name_of(list(t))]
    bh = [(b[-2], True) for b, _ in nb if len(b) >= 2 and b[-2] in R.NUMS]
    ob = [(g, False) for b, _ in nb for k, g in enumerate(b[:-2]) if g in R.NUMS]
    rd.gtl('NS13', 'long numbers count the head', 'long kind, numerals before the head', [R.kind(g) == 'long' for g, _ in bh], [R.kind(g) == 'long' for g, _ in ob])
    nc = Counter(g for t in DL for g in t if g in R.NUMS)
    rd.rec('NS14', "'2' is the commonest numeral", 'commonest: %s' % nc.most_common(4), nc.most_common(1)[0][0] == '2')
    vc = Counter(val(r) for g, r in allr)
    rd.rec('NS15', 'one is rarer than two', 'runs worth 1: %d, worth 2: %d' % (vc[1], vc[2]), vc[1] < vc[2])
    rd.thr('NS16', 'large numbers are rare', 'runs worth 9+', sum(n for v, n in vc.items() if v >= 9), sum(vc.values()), 0.05, above=False)
    rd.rec('NS17', 'twelve stands out', 'runs worth 10: %d, 11: %d, 12: %d' % (vc[10], vc[11], vc[12]), vc[12] > vc[10] + vc[11])
    BL = sorted({tuple(t) for t in B})
    tier([t for t in BL if genre(t) == 'name'], 'NS18', ' in names (B)')
    tier([t for t in BL if genre(t) == 'count'], 'NS19', ' in counts (B)')
    ns10(sorted({t for ty, t in FD}), 'NS20', " (F')")
    rd.finish()


if __name__ == '__main__':
    main()
