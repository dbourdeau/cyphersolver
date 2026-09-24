"""Kober's test on Linear A: do word endings (or the initial A-/JA-) track position in the document?

Alice Kober found Linear B's inflection by setting the same stems side by side with different endings in
different grammatical slots. Here the slot is the word's function in its document, from build_reading.py:
heading, entry label (a word followed by a quantity in the same entry), in-list without quantity,
formula/votive word, sealing mark.

Families: word tokens grouped by stem = all signs but the last (final alternation), or all signs but the
first where the first is A or JA (initial alternation). Only stems attested with 2+ different endings count.
Statistic: conditional mutual information I(ending; function | stem), summed over tokens. Null: within each
stem, function labels are permuted across that stem's tokens (so each stem keeps its own mix of functions)
5,000 times. If endings carried case or number tied to syntactic slot, the real statistic would exceed the null.
A second statistic uses the whole vocabulary: for each final sign, its distribution over functions against
all other finals (chi-square), to see which endings lean to headings or entries.
"""
from collections import Counter, defaultdict
import json
from math import log
from pathlib import Path
import random

ROOT = Path(__file__).resolve().parent.parent
READ = json.loads((ROOT / 'reading/reading.json').read_text(encoding='utf-8'))
FUNCS = ('heading', 'entry label', 'in-list, no quantity', 'formula/votive', 'sealing mark')


def tokens():
    out = []
    for r in READ['records']:
        for t in r['tokens']:
            if t['cls'] == 'word' and t.get('function') in FUNCS:
                out.append((tuple(t['label'].split('-')), t['function'], r['name']))
    return out


def cmi(groups):
    """Sum over stems of n * I(ending; function) within the stem."""
    total = 0.0
    for toks in groups.values():
        n = len(toks)
        ce, cf, cef = Counter(), Counter(), Counter()
        for e, f in toks:
            ce[e] += 1
            cf[f] += 1
            cef[(e, f)] += 1
        for (e, f), c in cef.items():
            total += c * log(c * n / (ce[e] * cf[f]))
    return total


def families(T, mode):
    g = defaultdict(list)
    for w, f, _ in T:
        if len(w) < 2:
            continue
        if mode == 'final' and len(w) >= 3:
            g[w[:-1]].append((w[-1], f))
        elif mode == 'initial':
            if w[0] in ('A', 'JA') and len(w) >= 3:
                g[w[1:]].append((w[0], f))
            else:
                g[w].append(('', f))
    return {s: v for s, v in g.items() if len({e for e, _ in v}) >= 2}


def test(groups, rng, reps):
    real = cmi(groups)
    null = []
    for _ in range(reps):
        sh = {}
        for s, v in groups.items():
            fs = [f for _, f in v]
            rng.shuffle(fs)
            sh[s] = [(e, f) for (e, _), f in zip(v, fs)]
        null.append(cmi(sh))
    return real, sum(null) / reps, (sum(x >= real for x in null) + 1) / (reps + 1)


def main(reps=5000, seed=20260923):
    T = tokens()
    rng = random.Random(seed)
    res = {'method': __doc__.strip(), 'word_tokens': len(T), 'tests': {}, 'families': {}}
    for mode in ('final', 'initial'):
        g = families(T, mode)
        real, mean, p = test(g, rng, reps)
        res['tests'][mode] = {'families': len(g), 'tokens': sum(len(v) for v in g.values()), 'cmi_real': round(real, 3),
                              'cmi_null_mean': round(mean, 3), 'p': round(p, 4)}
        res['families'][mode] = {'-'.join(s) if s else '(none)': dict(Counter(f'{e or "0"}:{f}' for e, f in v))
                                 for s, v in sorted(g.items(), key=lambda x: -len(x[1]))}
    # final sign against function over the whole vocabulary (types weighted by tokens)
    fin = defaultdict(Counter)
    for w, f, _ in T:
        if len(w) >= 2:
            fin[w[-1]][f] += 1
    tot = Counter()
    for c in fin.values():
        tot.update(c)
    N = sum(tot.values())
    lean = {}
    for e, c in fin.items():
        n = sum(c.values())
        if n < 15:
            continue
        chi = sum((c[f] - n * tot[f] / N) ** 2 / (n * tot[f] / N) for f in tot if tot[f])
        lean[e] = {'n': n, 'chi2': round(chi, 1), 'share': {f: round(c[f] / n, 2) for f in FUNCS if c[f]},
                   'overall': {f: round(tot[f] / N, 2) for f in FUNCS}}
    res['final_sign_lean'] = dict(sorted(lean.items(), key=lambda x: -x[1]['chi2']))
    (ROOT / 'reading/kober_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('word tokens', len(T))
    for m, v in res['tests'].items():
        print(f"  {m:8} families {v['families']:3} tokens {v['tokens']:4}  CMI {v['cmi_real']} vs null {v['cmi_null_mean']}  p {v['p']}")
    for m in ('final', 'initial'):
        print(f'  largest {m} families:')
        for s, c in list(res['families'][m].items())[:10]:
            print(f'    {s:14} {c}')
    print('  final signs by chi-square against the overall mix (df 4; 9.5 = p .05, 13.3 = p .01):')
    for e, v in list(res['final_sign_lean'].items())[:10]:
        print(f"    -{e:4} n={v['n']:3} chi2={v['chi2']:6}  {v['share']}")


if __name__ == '__main__':
    main()
