"""Hundred-and-forty-third registered prediction set (PREDICTIONS.md, NP1-NP6): numerals used for their sound.
Writes results/predict_test143.md."""
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test103 import CL
from predict_test108 import genre
from predict_test112 import runs
from signs import FISH

M = set(R.END) | set(CL) | {'400', '90'}


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-forty-third registered predictions: numerals used for their sound', 'predict_test143')
    DL = sorted({tuple(t) for t in AB})
    lex = lambda g: g not in R.NUMS and g not in M
    ns = sorted({(b, e) for b, e in T.names(AB) if b})
    frames = defaultdict(set)
    for t in DL:
        s = ('#',) + t + ('#',)
        for i in range(1, len(s) - 1):
            frames[(s[i - 1], s[i + 1])].add(s[i])
    shared = lambda f: any(lex(g) for g in frames[f])
    fr = lambda t: [(s[i - 1], s[i + 1]) for s in [('#',) + t + ('#',)] for i in range(1, len(s) - 1) if s[i] in R.NUMS]
    a = [shared(f) for t in DL if T.name_of(list(t)) for f in fr(t)]
    c = [shared(f) for t in DL if genre(t) == 'count' for f in fr(t)]
    rd.gtl('NP1', 'name numerals share frames with lexical signs', 'numeral tokens in a lexical-sharing frame, names', a, c)
    byl = defaultdict(list)
    for b, e in ns:
        byl[len(b)].append(b)
    kinds = Counter()
    for L, bs in byl.items():
        seen = set()
        for i in range(L):
            grp = defaultdict(set)
            for b in bs:
                grp[b[:i] + b[i + 1:]].add(b[i])
            for key, vs in grp.items():
                vs = sorted(vs)
                for x in range(len(vs)):
                    for y in range(x + 1, len(vs)):
                        u, v = vs[x], vs[y]
                        if (u in R.NUMS or v in R.NUMS) and (key, i, u, v) not in seen:
                            seen.add((key, i, u, v))
                            kinds['numeral-numeral' if u in R.NUMS and v in R.NUMS else ('numeral-lexical' if lex(u) or lex(v) else 'numeral-marker')] += 1
    tot = sum(kinds.values())
    rd.thr('NP2', 'numerals alternate with lexical signs', 'minimal pairs %s' % dict(kinds), kinds['numeral-lexical'], tot, 0.3)
    val = lambda r: sum(R.NUMS[g][0] for g in r)
    ty, vs, fv, ff, ov, os_ = [], [], [], [], [], []
    for b, e in ns:
        for i, j, r in runs(b):
            if j == len(b):
                ty.append('head')
                vs.append(val(r))
            elif lex(b[j]):
                ty.append('count')
                vs.append(val(r))
                if b[j] in FISH:
                    fv.append(val(r))
                    ff.append(b[j])
                else:
                    ov.append(val(r))
                    os_.append(b[j])
    rd.mi('NP3', 'value depends on counting or heading', 'runs in names (%s)' % dict(Counter(ty)), vs, ty)
    rd.mi('NP4', 'value depends on the fish', 'runs before a fish', fv, ff)
    oc = Counter(os_)
    keep = [i for i, s in enumerate(os_) if oc[s] >= 5]
    rd.mi('NP5', 'value depends on the counted sign', 'runs before other lexical signs with 5+ runs (%d signs)' % len({os_[i] for i in keep}),
          [ov[i] for i in keep], [os_[i] for i in keep])
    wn = [(b, e) for b, e in ns if any(g in R.NUMS for g in b)]
    rd.thr('NP6', 'numerals as heads', 'names with a numeral whose head is a numeral (%s)' % ', '.join(
        [' '.join(b) + ' ' + e for b, e in wn if b[-1] in R.NUMS][:8]), sum(b[-1] in R.NUMS for b, e in wn), len(wn), 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
