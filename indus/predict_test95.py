"""Ninety-fifth registered prediction set (PREDICTIONS.md, ON1-ON20): the single stroke '1'. Writes
results/predict_test95.md."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test44 import nonname
from predict_test63 import body_span
from predict_test91 import medial

random.seed(115)
HEAD = ('817', '820', '861')
OTH = ('2', '3')


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round("Ninety-fifth registered predictions: the single stroke '1'", 'predict_test95')
    DL = sorted({tuple(t) for t in AB})

    def toks(lines, s):
        return [(t, i) for t in lines for i in range(len(t)) if t[i] in s]
    o1, o2 = toks(DL, ('1',)), toks(DL, OTH)
    rd.say("- distinct-line tokens: '1' %d, '2'/'3' %d." % (len(o1), len(o2)))
    rd.say()
    nxt = lambda t, i: i + 1 < len(t) and t[i + 1] not in R.NUMS
    rd.ltl('ON1', "'1' is not a count", "followed by a non-numeral, '1'", [nxt(t, i) for t, i in o1], [nxt(t, i) for t, i in o2])

    def on2(a, b, key, lab):
        rd.gtl(key, "'1' closes lines%s" % lab, "line-final, '1'", [i == len(t) - 1 for t, i in a], [i == len(t) - 1 for t, i in b])

    def on3(a, b, key, lab):
        rd.gtl(key, "'1' follows the ending%s" % lab, "after 740/520, '1'", [i > 0 and t[i - 1] in R.END for t, i in a], [i > 0 and t[i - 1] in R.END for t, i in b])
    on2(o1, o2, 'ON2', '')
    on3(o1, o2, 'ON3', '')
    h1 = [t[0] for t, i in o1 if i == 1 and t[0] in HEAD]
    rd.thr('ON4', "'1' belongs to 820", "'heading + 1' that are '820 1'", sum(h == '820' for h in h1), len(h1), 0.9)
    rd.thr('ON5', "'1' follows a word", "'1' after a non-numeral", sum(i > 0 and t[i - 1] not in R.NUMS for t, i in o1), len(o1), 0.7)
    heads = {b[-1] for b, e in T.names(AB) if b}
    rd.gtl('ON6', "'1' follows a head", "name head before, '1'", [i > 0 and t[i - 1] in heads for t, i in o1], [i > 0 and t[i - 1] in heads for t, i in o2])
    ns = sorted({(b, e) for b, e in T.names(AB) if b})
    rd.gtl('ON7', "'1' is a 520 head", "520, bodies ending in '1'", [e == '520' for b, e in ns if b[-1] == '1'], [e == '520' for b, e in ns if b[-1] in R.NUMS and b[-1] != '1'])
    fol = Counter(t[i + 1] for t, i in o1 if nxt(t, i))
    rd.thr('ON8', "'1' has few partners", "five commonest signs after '1' (%s)" % ', '.join('%s x%d' % kv for kv in fol.most_common(5)),
           sum(n for _, n in fol.most_common(5)), sum(fol.values()), 0.5)
    FD = sorted({(r['site'].strip(), r['type'][:3], tuple(ln)) for r in F for ln in r['seq'] if ln})
    ft = [(s, ty, t[i]) for s, ty, t in FD for i in range(len(t)) if t[i] in ('1',) + OTH]
    rd.gtl('ON9', "'1' is a seal sign", "seal, '1' tokens", [ty == 'SEA' for s, ty, g in ft if g == '1'], [ty == 'SEA' for s, ty, g in ft if g != '1'])
    fn = [(s, g == '1') for s, ty, t in FD for g in t if g in R.NUMS and s in ('Mohenjo-daro', 'Harappa')]
    rd.gtl('ON10', "'1' is Mohenjo-daran", "'1' among numerals, Mohenjo-daro", [x for s, x in fn if s == 'Mohenjo-daro'], [x for s, x in fn if s == 'Harappa'])
    ins = lambda t, i: bool(body_span(list(t))) and body_span(list(t))[0] <= i < body_span(list(t))[1]
    rd.gtl('ON11', "'1' is a name sign", "inside a body, '1'", [ins(t, i) for t, i in o1], [ins(t, i) for t, i in o2])
    rd.thr('ON12', "'1' never starts a line", "line-initial '1'", sum(i == 0 for t, i in o1), len(o1), 0.05, above=False)
    adj = lambda t, i: (i > 0 and t[i - 1] in R.NUMS) or (i + 1 < len(t) and t[i + 1] in R.NUMS)
    rd.ltl('ON13', "'1' stands alone", "next to a numeral, '1'", [adj(t, i) for t, i in o1], [adj(t, i) for t, i in o2])
    mt = [(t, j) for t in DL for m in medial(t) for j in [m + 1] if j < len(t) and t[j] == '1']
    rd.thr('ON14', "'1' after a mid-line name is a short tail", "'1' after medial 740 with the line end within two signs", sum(len(t) - j - 1 <= 2 for t, j in mt), len(mt), 0.7)
    ba = [(t[i - 1], t[i + 1]) for t, i in o1 if 0 < i < len(t) - 1]
    rd.mi('ON15', "'1' sits in fixed phrases", "'1' with both neighbours", [a for a, _ in ba], [b for _, b in ba])
    objs = defaultdict(set)
    for r in F:
        for ln in r['seq']:
            if ln:
                objs[tuple(ln)].add(r['sealid'])
    has = lambda t, s: any(g in s for g in t)
    rd.gtl('ON16', "'1' lines are unique", "one object, lines with '1'", [len(objs[t]) == 1 for s, ty, t in FD if has(t, ('1',))],
           [len(objs[t]) == 1 for s, ty, t in FD if has(t, OTH) and not has(t, ('1',))])
    c1 = {t[i + 1] for t, i in o1 if nxt(t, i)}
    c2 = {t[i + 1] for t, i in toks(DL, ('2',)) if nxt(t, i)}
    rd.thr('ON17', "'1' counts other things than '2'", 'shared sign types', len(c1 & c2), len(c1 | c2), 0.3, above=False)
    DB = sorted({tuple(t) for t in B})
    on2(toks(DB, ('1',)), toks(DB, OTH), 'ON18', ' (B)')
    on3(toks(DB, ('1',)), toks(DB, OTH), 'ON19', ' (B)')
    f1 = [(t, i) for t, i in o1 if nonname(list(t))]
    rd.thr('ON20', "in formulas '1' counts", "formula '1' before a non-numeral", sum(nxt(t, i) for t, i in f1), len(f1), 0.5)
    rd.finish()


if __name__ == '__main__':
    main()
