"""Hundred-and-third registered prediction set (PREDICTIONS.md, FX1-FX20): the formula closers. Writes
results/predict_test103.md."""
import random
from collections import Counter, defaultdict
from itertools import combinations

import predict_test13 as T
import rtools as R
from predict_test44 import nonname

random.seed(123)
CL = ('151', '154', '156', '161', '226', '241', '426', '527', '565', '621', '679')
HEAD = ('817', '820', '861')
NONE = ('', 'None', '-', 'Unknown')


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-third registered predictions: the formula closers', 'predict_test103')
    DL = [t for t in sorted({tuple(t) for t in AB}) if len(t) >= 2]
    cll = [t for t in DL if t[-1] in CL]
    fm = [t for t in DL if nonname(list(t)) and t[-1] not in CL]
    rd.say('- closer lines %d; other formulas %d.' % (len(cll), len(fm)))
    rd.say()

    def fx1(lines, key, lab):
        rd.thr(key, 'closer lines are formulas%s' % lab, 'closer lines without 740/520', sum(not any(g in R.END for g in t) for t in lines), len(lines), 0.8)
    fx1(cll, 'FX1', '')
    tk = [(t, i) for t in DL for i in range(len(t)) if t[i] in CL]
    rd.thr('FX2', 'closers are counted', 'closer tokens after a numeral', sum(i > 0 and t[i - 1] in R.NUMS for t, i in tk), len(tk), 0.2)
    rd.thr('FX3', 'closers follow names', 'closer tokens after 740/520', sum(i > 0 and t[i - 1] in R.END for t, i in tk), len(tk), 0.1)
    rd.rank('FX4', 'closer lines are short', 'other formulas against closer lines', [len(t) for t in fm], [len(t) for t in cll])
    Fn = [r for r in F if r['type'] != 'TAB:C']
    FD = sorted({(r['site'].strip(), r['type'][:3], tuple(ln)) for r in Fn for ln in r['seq'] if len(ln) >= 2})
    ft = [ty for s, ty, t in FD for g in t if g in CL]
    rd.thr('FX5', 'closers are seal signs', 'closer tokens on seals', sum(ty == 'SEA' for ty in ft), len(ft), 0.6)
    rd.gtl('FX6', 'closers are Mohenjo-daran', 'closer lines, Mohenjo-daro', [t[-1] in CL for s, ty, t in FD if s == 'Mohenjo-daro'], [t[-1] in CL for s, ty, t in FD if s == 'Harappa'])
    pv = [(t[i], t[i - 1]) for t, i in tk if i > 0]
    rd.mi('FX7', 'each closer has its partners', 'closer tokens', [a for a, _ in pv], [b for _, b in pv])
    rd.thr('FX8', 'one closer per line', 'lines with two different closers', sum(len({g for g in t if g in CL}) >= 2 for t in DL), len(DL), 0.03, above=False)
    bodies = {b for b, e in T.names(AB) if len(b) >= 2}
    emb = lambda t: any(tuple(t[i:j]) in bodies for i in range(len(t)) for j in range(i + 2, len(t) + 1))
    cf = [t for t in cll if nonname(list(t))]
    rd.gtl('FX9', 'closer lines cite names', 'embedded body, closer formulas', [emb(t) for t in cf], [emb(t) for t in fm])
    rd.gtl('FX10', 'closer lines are headed', 'heading first, closer formulas', [t[0] in HEAD for t in cf], [t[0] in HEAD for t in fm])
    num = lambda t: any(g in R.NUMS for g in t)
    rd.ltl('FX11', 'closer lines do not count', 'numeral, closer formulas', [num(t) for t in cf], [num(t) for t in fm])
    t156 = [(t, i) for t, i in tk if t[i] == '156']
    rd.thr('FX12', '156 is counted', '156 tokens after a numeral', sum(i > 0 and t[i - 1] in R.NUMS for t, i in t156), len(t156), 0.5)
    heads = {b[-1] for b, e in T.names(AB) if b}
    rd.thr('FX13', 'closers follow heads', 'closer tokens after a name head', sum(i > 0 and t[i - 1] in heads for t, i in tk), len(tk), 0.5)
    ln_ = defaultdict(set)
    cc = Counter()
    for t, i in tk:
        cc[t[i]] += 1
        if i > 0:
            ln_[t[i]].add(t[i - 1])
    c5 = [g for g in CL if cc[g] >= 5]
    js = [len(ln_[a] & ln_[b]) / max(1, len(ln_[a] | ln_[b])) for a, b in combinations(c5, 2)]
    rd.rec('FX14', 'each closer its own company', 'closers %d; mean Jaccard %.3f; threshold 0.2' % (len(c5), sum(js) / max(1, len(js))), bool(js) and sum(js) / len(js) <= 0.2)
    objs = defaultdict(set)
    for r in Fn:
        for ln in r['seq']:
            if ln:
                objs[tuple(ln)].add(r['sealid'])
    ftx = {t for s, ty, t in FD if nonname(list(t))}
    rd.gtl('FX15', 'closer texts recur', 'on 2+ objects, closer formulas', [len(objs[t]) >= 2 for t in ftx if t[-1] in CL], [len(objs[t]) >= 2 for t in ftx if t[-1] not in CL])
    mot = lambda r: '' if recs[r['sealid']][18].strip() in NONE else recs[r['sealid']][18].split(':')[0].strip()
    sm = [(tuple(ln)[-1] in CL, mot(r) == 'Bull1') for r in Fn if r['type'].startswith('SEAL') and mot(r) for ln in r['seq'] if len(ln) >= 2]
    rd.ltl('FX16', 'closers are not on unicorns', 'unicorn, closer seal lines', [u for c_, u in sm if c_], [u for c_, u in sm if not c_])
    tb = Counter(g for t in B for g in t)
    rd.rec('FX17', 'closers in B', 'closers with 5+ B tokens: %d (%s); threshold 5' % (sum(tb[g] >= 5 for g in CL), ', '.join(g for g in CL if tb[g] >= 5)), sum(tb[g] >= 5 for g in CL) >= 5)
    fx1([t for t in sorted({tuple(t) for t in B}) if len(t) >= 2 and t[-1] in CL], 'FX18', ' (B)')
    fx1([t for s, ty, t in FD if t[-1] in CL], 'FX19', ' (F)')
    rd.thr('FX20', 'closer lines are short', 'closer lines of 2-4 signs', sum(2 <= len(t) <= 4 for t in cll), len(cll), 0.8)
    rd.finish()


if __name__ == '__main__':
    main()
