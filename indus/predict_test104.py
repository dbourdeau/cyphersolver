"""Hundred-and-fourth registered prediction set (PREDICTIONS.md, TP1-TP20): line templates. Writes
results/predict_test104.md."""
import random
from collections import Counter

import rtools as R
from predict_test50 import ent
from predict_test53 import lab_perm
from predict_test103 import CL
from signs import FISH

random.seed(124)
HEAD = ('817', '820', '861')


def template(t):
    out = []
    for i, g in enumerate(t):
        if i == 0 and g in HEAD:
            r = 'H'
        elif g in R.NUMS:
            r = 'N'
        elif g in R.END:
            r = 'E'
        elif g in ('400', '90', '151') and i > 0 and t[i - 1] in R.END:
            r = 'S'
        elif g in CL:
            r = 'C'
        elif g in FISH:
            r = 'F'
        else:
            r = 'X'
        if out and ((r == 'X' and out[-1] == 'X') or (r == 'N' and out[-1] == 'N')):
            continue
        out.append(r)
    return ''.join(out)


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-fourth registered predictions: line templates', 'predict_test104')
    DL = sorted({tuple(t) for t in AB})
    tp = Counter(template(t) for t in DL)
    rd.say('- distinct lines %d; templates %d; commonest: %s.' % (len(DL), len(tp), ', '.join('%s x%d' % kv for kv in tp.most_common(12))))
    rd.say()

    def tp1(lines, key, lab):
        c = Counter(template(t) for t in lines)
        rd.thr(key, 'a few templates%s' % lab, 'lines in the ten commonest templates', sum(n for _, n in c.most_common(10)), len(lines), 0.5)
    tp1(DL, 'TP1', '')
    Fn = [r for r in F if r['type'] != 'TAB:C']
    FD = sorted({(r['site'].strip(), r['type'][:3], tuple(ln)) for r in Fn for ln in r['seq'] if ln})
    st = [(ty, template(t)) for s, ty, t in FD if ty in ('SEA', 'TAB')]
    rd.mi('TP2', 'the medium sets the template', 'F lines', [a for a, _ in st], [b for _, b in st])
    cs = [(s, template(t)) for s, ty, t in FD if s in ('Mohenjo-daro', 'Harappa')]
    rd.mi('TP3', 'the city sets the template', 'F lines', [a for a, _ in cs], [b for _, b in cs])
    ta = Counter(template(t) for t in sorted({tuple(t) for t in A}))
    tb = Counter(template(t) for t in sorted({tuple(t) for t in B}))
    sa, sb = {k for k, _ in ta.most_common(5)}, {k for k, _ in tb.most_common(5)}
    rd.rec('TP4', 'the templates hold in B', 'A top 5 %s; B top 5 %s; shared %d; threshold 4' % (sorted(sa), sorted(sb), len(sa & sb)), len(sa & sb) >= 4)
    ss = Counter(b for a, b in st if a == 'SEA')
    tt = Counter(b for a, b in st if a == 'TAB')
    rd.rec('TP5', "'XE' leads on seals", 'seal top 3: %s' % ss.most_common(3), ss.most_common(1)[0][0] == 'XE')
    rd.rec('TP6', "'NX' leads on tablets", 'tablet top 3: %s' % tt.most_common(3), tt.most_common(1)[0][0] == 'NX')
    ht = [template(t) for t in DL if template(t).startswith('H')]
    rd.thr('TP7', 'the heading takes a number', "templates starting 'HN'", sum(x.startswith('HN') for x in ht), len(ht), 0.9)
    et = [template(t) for t in DL if 'E' in template(t)]
    fin = lambda x: x.rstrip('S').endswith('E') and x.count('E') == 1
    rd.thr('TP8', 'the ending ends', 'E only followed by S or the end', sum(fin(x) for x in et), len(et), 0.9)
    ct = [template(t) for t in DL if 'C' in template(t)]
    rd.thr('TP9', "'XC' is the closer template", "lines 'XC'", sum(x == 'XC' for x in ct), len(ct), 0.5)
    o, p = lab_perm([b for a, b in cs if a == 'Mohenjo-daro'], [b for a, b in cs if a == 'Harappa'], lambda a, b: ent(a) - ent(b), R.N)
    rd.rec('TP10', 'Mohenjo-daro writes more forms', 'entropy difference %+.2f bits; p = %.4f' % (o, p), o > 0 and p < 0.05)
    o, p = lab_perm([b for a, b in st if a == 'SEA'], [b for a, b in st if a == 'TAB'], lambda a, b: ent(a) - ent(b), R.N)
    rd.rec('TP11', 'seals write more forms', 'entropy difference %+.2f bits; p = %.4f' % (o, p), o > 0 and p < 0.05)
    cu = sorted({tuple(ln) for r in F if r['type'] == 'TAB:C' for ln in r['seq'] if ln})
    se = [t for s, ty, t in FD if ty == 'SEA']
    rc = len({template(t) for t in cu}) / max(1, len(cu))
    rs = len({template(t) for t in se}) / max(1, len(se))
    rd.rec('TP12', 'copper writes few forms', 'templates per line: copper %.2f, seals %.2f' % (rc, rs), rc < rs)
    nx = [t for t in DL if template(t) == 'NX']
    val = lambda t: sum(R.NUMS[g][0] for g in t if g in R.NUMS)
    rd.thr('TP13', "'NX' is a count", "'NX' lines with value 2-4", sum(2 <= val(t) <= 4 for t in nx), len(nx), 0.7)
    rd.thr('TP14', 'endings and closers exclude each other', 'lines with E and C', sum('E' in template(t) and 'C' in template(t) for t in DL), len(DL), 0.02, above=False)
    rd.thr('TP15', 'one number per line', 'lines with 2+ N', sum(template(t).count('N') >= 2 for t in DL), len(DL), 0.1, above=False)
    pl = [(R.level('Harappa', recs[r['sealid']]), template(tuple(ln))) for r in Fn if r['site'].strip() == 'Harappa' for ln in r['seq'] if ln
          if R.level('Harappa', recs[r['sealid']]) in ('E', 'L')]
    o, p = R.mi_perm([a for a, _ in pl], [b for _, b in pl])
    rd.rec('TP16', 'the templates do not change over time', 'Harappa lines %d; MI %.3f; p = %.4f' % (len(pl), o, p), p >= 0.05)
    gr = sorted({tuple(ln) for r in Fn if r['type'] == 'POT:T:g' for ln in r['seq'] if ln})
    rd.thr('TP17', 'graffiti are not names', 'graffiti without E', sum('E' not in template(t) for t in gr), len(gr), 0.8)
    tp1([t for s, ty, t in FD], 'TP18', ' (F)')
    tp1(sorted({tuple(t) for t in B}), 'TP19', ' (B)')
    hn = [s for s, ty, t in FD if template(t).startswith('HN') and 'E' in template(t)]
    rd.thr('TP20', 'headed names are Mohenjo-daran', "'HN..E' lines from Mohenjo-daro", sum(s == 'Mohenjo-daro' for s in hn), len(hn), 0.7)
    rd.finish()


if __name__ == '__main__':
    main()
