"""Test of the predictions registered in PREDICTIONS.md (committed before this script was written).

Stems = the whole line before its final sign (lines of 2+ signs). A sign X 'replaces 740' when the same stem
occurs with 740 and with X as the final sign. Expected counts: final signs permuted among lines (200
permutations). Discovery: ICIT-derived corpus; held-out check: M77 additions.

Writes results/predict_test.md.
"""
import os
import random
from collections import Counter, defaultdict

from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
EXCL = {'740', '520', '400', '90', '151'}


def say(s=''):
    OUT.append(s)
    print(s)


def pairs(rows):
    out = []
    for r in rows:
        for ln in r['seq']:
            t = [g for g in ln if g != '?']
            if len(t) >= 2:
                out.append((tuple(t[:-1]), t[-1]))
    return out


def replace_counts(pr):
    finals = defaultdict(set)
    for s, f in pr:
        finals[s].add(f)
    c = Counter()
    for s, fs in finals.items():
        if '740' in fs:
            for f in fs:
                if f not in EXCL:
                    c[f] += 1
    return c, finals


def test(pr, rng, n=200):
    obs, finals = replace_counts(pr)
    stems = [s for s, _ in pr]
    fins = [f for _, f in pr]
    ge = Counter()
    mean = Counter()
    for _ in range(n):
        rng.shuffle(fins)
        c, _ = replace_counts(list(zip(stems, fins)))
        for f in set(obs) | set(c):
            mean[f] += c[f] / n
            if c[f] >= obs[f]:
                ge[f] += 1
    return obs, mean, {f: ge[f] / n for f in obs}, finals


def main():
    rng = random.Random(131)
    disc, held = pairs(load()), pairs(load(only_m77=True))
    say('# Registered predictions P1-P3: results')
    say()
    say('## P1 A sign that replaces 740 on the same names')
    say()
    obs, mean, p, finals = test(disc, rng)
    cands = sorted((f for f in obs if obs[f] >= 3), key=lambda f: (p[f], -obs[f]))
    say('Discovery (ICIT-derived, %d lines): signs replacing 740 on 3+ stems, with permutation expectation and p:' % len(disc))
    say()
    say('| sign | stems with both 740 and it | expected | p |')
    say('|---|---|---|---|')
    for f in cands[:15]:
        say('| %s | %d | %.1f | %.3f |' % (f, obs[f], mean[f], p[f]))
    say()
    sig = [f for f in cands if p[f] < 0.01]
    obs_h, mean_h, p_h, finals_h = test(held, rng)
    say('- signs at p < 0.01 in discovery: %s. On the held-out M77 texts (%d lines): %s.' % (
        ', '.join(sig) or 'none', len(held),
        '; '.join('%s %d stems (expected %.1f, p %.3f)' % (f, obs_h.get(f, 0), mean_h.get(f, 0), p_h.get(f, 1.0))
                  for f in sig) or '-'))
    held_ok = [f for f in sig if p_h.get(f, 1.0) < 0.05]
    say('- **P1 %s**%s.' % ('holds' if held_ok else 'fails',
                            (': ' + ', '.join(held_ok) + ' replaces 740 in both samples') if held_ok else ''))
    say()
    say('## P2 The candidate replaces 740 but not 520')
    say()
    fin_all = defaultdict(set)
    for s, f in disc + held:
        fin_all[s].add(f)
    s740 = [s for s, fs in fin_all.items() if '740' in fs]
    s520 = [s for s, fs in fin_all.items() if '520' in fs]
    res2 = []
    for f in held_ok or sig:
        a = sum(1 for s in s740 if f in fin_all[s])
        b = sum(1 for s in s520 if f in fin_all[s])
        res2.append((f, a, b))
        say('- %s: with %d of %d stems that take 740 (%.1f%%), with %d of %d stems that take 520 (%.1f%%).' % (
            f, a, len(s740), 100 * a / len(s740), b, len(s520), 100 * b / len(s520)))
    ok2 = bool(res2) and all(b / len(s520) < a / len(s740) for f, a, b in res2)
    say('- **P2 %s.**' % ('holds' if ok2 else ('not testable (no P1 sign)' if not res2 else 'fails')))
    say()
    say('## P3 The 520 stems do not alternate more than the 740 stems')
    say()
    m740 = sum(1 for s in s740 if len(fin_all[s]) > 1)
    m520 = sum(1 for s in s520 if len(fin_all[s]) > 1)
    say('- stems seen with more than one final sign: 740 stems %d of %d (%.1f%%), 520 stems %d of %d (%.1f%%).' % (
        m740, len(s740), 100 * m740 / len(s740), m520, len(s520), 100 * m520 / len(s520)))
    say('- **P3 %s.**' % ('holds' if m520 / len(s520) <= m740 / len(s740) else 'fails'))
    say()
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
