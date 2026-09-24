"""Eighty-third registered prediction set (PREDICTIONS.md, SF1-SF20): what the suffixes do. Writes
results/predict_test83.md."""
import random
from collections import Counter, defaultdict

import rtools as R
from predict_test82 import suffix_lines

random.seed(103)
HEAD = ('817', '820', '861')


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Eighty-third registered predictions: what the suffixes do', 'predict_test83')
    full = lambda r: '' if recs[r['sealid']][18].strip() in ('', 'None') else recs[r['sealid']][18].strip()
    # object-level suffix rows in F: (r, line, body, ending, follower)
    rows = [(r, tuple(ln), b, e, f) for r in F for ln in r['seq'] if ln for b, e, f in suffix_lines([tuple(ln)])]
    D = {(r['site'].strip(), r['type'][:3], t, b, e, f) for r, t, b, e, f in rows}
    tab = lambda ty: ty == 'TAB'
    t400 = [x for x in D if tab(x[1]) and x[5] == '400']
    toth = [x for x in D if tab(x[1]) and x[5] != '400']
    sealb = {b for r, t, b, e, f in rows if r['type'].startswith('SEAL')}
    sealbs = defaultdict(set)
    for r, t, b, e, f in rows:
        if r['type'].startswith('SEAL'):
            sealbs[r['site'].strip()].add(b)
    rd.say('- F name lines %d; distinct 400 tablet lines %d, other tablet name lines %d.' % (len(rows), len(t400), len(toth)))
    rd.say()
    rd.gtl('SF1', 'receipts name seal owners', 'body on a seal, 400 tablet lines', [x[3] in sealb for x in t400], [x[3] in sealb for x in toth])
    ss = [x[0] for x in t400]
    bb = [x[3] for x in t400]
    st = lambda s_: sum(b in sealbs[s] for s, b in zip(s_, bb))
    obs = st(ss)
    sh = ss[:]
    ge = 0
    for _ in range(R.N):
        random.shuffle(sh)
        ge += st(sh) >= obs
    p = (ge + 1) / (R.N + 1)
    rd.rec('SF2', 'receipts name local seal owners', '400 tablet lines %d; body on a seal at its site %d; p = %.4f' % (len(t400), obs, p), p < 0.05)
    tt = [(r['type'], f == '400') for r, t, b, e, f in rows if r['type'].startswith('TAB')]
    rd.gtl('SF3', 'receipts are incised', 'TAB:I, 400 tablet lines', [ty == 'TAB:I' for ty, x in tt if x], [ty == 'TAB:I' for ty, x in tt if not x])
    lv = lambda r: R.level('Harappa', recs[r['sealid']])
    hl = [(lv(r) == 'E', f == '400') for r, t, b, e, f in rows if r['site'].strip() == 'Harappa' and r['type'].startswith('TAB') and lv(r) in ('E', 'L')]
    rd.gtl('SF4', 'receipts are early', 'earlier period, 400 tablet lines', [a for a, x in hl if x], [a for a, x in hl if not x])
    oc = Counter(t for r, t, b, e, f in rows if r['type'].startswith('TAB'))
    k4 = {t: f == '400' for r, t, b, e, f in rows if r['type'].startswith('TAB')}
    rd.gtl('SF5', 'receipts are stamped', 'on 2+ objects, 400 tablet texts', [oc[t] >= 2 for t in k4 if k4[t]], [oc[t] >= 2 for t in k4 if not k4[t]])
    hc = Counter(x[3][-1] for x in t400)
    rd.thr('SF6', 'few receipt heads', 'three commonest heads (%s)' % ', '.join('%s x%d' % kv for kv in hc.most_common(3)),
           sum(n for _, n in hc.most_common(3)), len(t400), 0.5)
    to = {}
    for r, t, b, e, f in rows:
        if r['type'].startswith('TAB'):
            to[r['sealid']] = to.get(r['sealid'], False) or f == '400'
    tobj = {r['sealid']: r for r in F}
    rd.ltl('SF7', 'receipts have no picture', 'picture, tablets with a 400 line', [bool(full(tobj[s])) for s, x in to.items() if x],
           [bool(full(tobj[s])) for s, x in to.items() if not x])
    allrows = rows + [(None, tuple(t), b, e, f) for t in A + B for b, e, f in suffix_lines([tuple(t)])]
    bare = {(b, e) for _, t, b, e, f in allrows if f == '#'}
    bare_seal = {(b, e) for r, t, b, e, f in rows if f == '#' and r['type'].startswith('SEAL')}

    def bodies_with(sfx):
        return {(b, e) for _, t, b, e, f in allrows if f == sfx}
    b400 = bodies_with('400')
    rd.thr('SF8', 'the receipt suffix is added to a name', '400 bodies also unsuffixed', len(b400 & bare), len(b400), 0.3)
    bb400 = b400 & bare
    rd.thr('SF9', 'the bare form is a seal name', 'unsuffixed forms on a seal', len(bb400 & bare_seal), len(bb400), 0.5)
    site_rows = lambda site: [(r['type'][:3]) for r, t, b, e, f in rows if f == '400' and r['site'].strip() == site]
    h = site_rows('Harappa')
    rd.thr('SF10', 'at Harappa 400 is on tablets', 'Harappa 400 lines on tablets', sum(x == 'TAB' for x in h), len(h), 0.9)
    m = site_rows('Mohenjo-daro')
    rd.thr('SF11', 'at Mohenjo-daro 400 is on seals', 'Mohenjo-daro 400 lines on seals', sum(x == 'SEA' for x in m), len(m), 0.5)
    sr = [(t, f, full(r)) for r, t, b, e, f in rows if r['type'].startswith('SEAL')]
    hu = lambda t: len(t) >= 3 and t[0] in HEAD and t[1] in ('2', '60', '1')
    rd.ltl('SF12', 'owner names are not titled', 'heading unit, 90 seal lines', [hu(t) for t, f, m_ in sr if f == '90'], [hu(t) for t, f, m_ in sr if f != '90'])
    rd.gtl('SF13', 'owner names are on unicorns', 'unicorn, 90 seal lines', [m_.split(':')[0].strip() == 'Bull1' for t, f, m_ in sr if f == '90' and m_],
           [m_.split(':')[0].strip() == 'Bull1' for t, f, m_ in sr if f != '90' and m_])
    sb = [(b, f) for r, t, b, e, f in rows if r['type'].startswith('SEAL')]
    num = lambda b: any(g in R.NUMS for g in b)
    rd.ltl('SF14', 'owner names are not counted', 'numeral, 90 seal names', [num(b) for b, f in sb if f == '90'], [num(b) for b, f in sb if f != '90'])
    b90 = bodies_with('90')
    rd.thr('SF15', 'the owner suffix is added to a name', '90 bodies also unsuffixed', len(b90 & bare), len(b90), 0.3)
    o90 = [r['type'][:3] for r, t, b, e, f in rows if f == '90' and r['site'].strip() not in ('Harappa', 'Mohenjo-daro')]
    rd.thr('SF16', 'small sites use 90 on seals', 'small-site 90 lines on seals', sum(x == 'SEA' for x in o90), len(o90), 0.7)
    s151 = [r['type'][:3] for r, t, b, e, f in rows if f == '151']
    rd.thr('SF17', '151 is on seals', '151 suffix lines on seals', sum(x == 'SEA' for x in s151), len(s151), 0.7)
    one = [len([ln for ln in r['seq'] if ln]) == 1 for r, t, b, e, f in rows if f in ('90', '400', '151')]
    rd.thr('SF18', 'a suffix line stands alone', 'suffix lines alone on their object', sum(one), len(one), 0.95)
    h90 = {b[-1] for r, t, b, e, f in rows if f == '90'}
    h400 = {b[-1] for r, t, b, e, f in rows if f == '400'}
    rd.thr('SF19', '90 and 400 serve different words', 'shared head types (90: %d, 400: %d)' % (len(h90), len(h400)), len(h90 & h400), len(h90 | h400), 0.2, above=False)
    ar = [(r['type'], f) for r in rowsA for ln in r['seq'] if ln for b, e, f in suffix_lines([tuple(ln)]) if f in ('90', '400')]
    rd.gtl('SF20', 'the tablet suffix in A', 'tablet, 400 lines', [ty.startswith('TAB') for ty, f in ar if f == '400'], [ty.startswith('TAB') for ty, f in ar if f == '90'])
    rd.finish()


if __name__ == '__main__':
    main()
