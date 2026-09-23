"""Replicate the main structural findings on the M77-only texts (an independent sample) and on the
merged corpus (merge_m77.py).

For each sample (ICIT-derived; M77 additions alone; merged):
RP1 endings fixed per name: whole names seen with both 740 and 520, against shuffled endings.
RP2 fish-final names take 520: share of 520 among ending lines after a fish sign, and after others.
RP3 740 and 520 never adjacent; share of 520 that is text-final.
RP4 6 + fish: share of stroke numerals before a fish that are six, against six before other signs
    (distinct texts; pairs and the opener-slot single stroke left out).
RP5 the opening formula [817/820/861] + [2/60/1]: texts that open with it.
RP6 two numeral systems: Jensen-Shannon divergence between the signs after short and after long
    strokes (values 1-6), against 500 permutations of the short/long label.
RP7 the published keys (Yajnadevam, Parpola) against 100 shuffles in their claimed language.

Usage: python replicate_m77.py <mw.txt> <dedr forms.csv> <sux_gloss.tsv> <yajnadevam xlits.csv>
Writes results/replicate_m77.md.
"""
import math
import os
import random
import sys
from collections import Counter, defaultdict

import bench
from numerals import NUMS
from signs import FISH, load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
random.seed(83)


def say(s=''):
    OUT.append(s)
    print(s)


def split_end(t):
    if len(t) >= 3 and t[-1] in ('400', '90', '151') and t[-2] in ('740', '520'):
        return tuple(t[:-2]), t[-2]
    if len(t) >= 2 and t[-1] in ('740', '520'):
        return tuple(t[:-1]), t[-1]
    return None, None


def rp1(texts):
    ends = [split_end(t) for t in texts]
    ends = [(s, e) for s, e in ends if s]

    def both(pairs):
        w = defaultdict(set)
        for s, e in pairs:
            w[s].add(e)
        return sum(1 for v in w.values() if len(v) == 2), len(w)
    real, n = both(ends)
    es = [e for _, e in ends]
    sims = []
    for _ in range(200):
        random.shuffle(es)
        sims.append(both([(s, e) for (s, _), e in zip(ends, es)])[0])
    sims.sort()
    return '%d of %d names; shuffled median %d (%d-%d)' % (real, n, sims[100], sims[0], sims[-1])


def rp2(texts):
    f = o = f5 = o5 = 0
    for t in texts:
        s, e = split_end(t)
        if s:
            if s[-1] in FISH:
                f += 1
                f5 += e == '520'
            else:
                o += 1
                o5 += e == '520'
    return 'after a fish sign %d/%d (%.0f%%); after other signs %d/%d (%.0f%%)' % (
        f5, f, 100 * f5 / max(f, 1), o5, o, 100 * o5 / max(o, 1))


def rp3(texts):
    adj = sum(1 for t in texts for a, b in zip(t, t[1:]) if {a, b} == {'740', '520'})
    n520 = sum(t.count('520') for t in texts)
    fin = sum(1 for t in texts if t and t[-1] == '520')
    return '740/520 adjacent %d times; 520 text-final %d of %d (%.0f%%)' % (adj, fin, n520, 100 * fin / max(n520, 1))


def rp4(rows):
    seen, dist = set(), []
    for r in rows:
        k = tuple(map(tuple, r['seq']))
        if k not in seen:
            seen.add(k)
            dist.append(r)
    F, O = Counter(), Counter()
    for r in dist:
        for ln in r['seq']:
            for i in range(len(ln) - 1):
                a, b = ln[i], ln[i + 1]
                if a in NUMS and a not in ('2', '32') and b not in NUMS:
                    if a in ('1', '31') and i and ln[i - 1] in ('817', '820', '861', '2', '32', '60'):
                        continue
                    (F if b in FISH else O)[NUMS[a][0]] += 1
    nf, no = sum(F.values()), sum(O.values())
    p0 = O[6] / no
    k = F[6]
    p = sum(math.comb(nf, i) * p0 ** i * (1 - p0) ** (nf - i) for i in range(k, nf + 1))
    return 'six before a fish %d/%d (%.1f%%), elsewhere %.1f%%, ratio %.1f, binomial p = %.2g; seven before a fish %d' % (
        k, nf, 100 * k / max(nf, 1), 100 * p0, (k / nf) / p0 if nf and p0 else 0, p, F[7])


def rp5(rows):
    k = sum(1 for r in rows if len(r['flat']) >= 3 and r['flat'][0] in ('817', '820', '861') and r['flat'][1] in ('2', '60', '1'))
    return '%d of %d texts (%.1f%%)' % (k, len(rows), 100 * k / len(rows))


def jsd(a, b):
    na, nb = sum(a.values()), sum(b.values())
    out = 0
    for g in set(a) | set(b):
        pa, pb = a[g] / na, b[g] / nb
        m = (pa + pb) / 2
        out += 0.5 * (pa * math.log2(pa / m) if pa else 0) + 0.5 * (pb * math.log2(pb / m) if pb else 0)
    return out


def rp6(rows):
    tok = []
    for r in rows:
        for ln in r['seq']:
            for a, b in zip(ln, ln[1:]):
                if a in NUMS and NUMS[a][1] in ('short', 'long') and 1 <= NUMS[a][0] <= 6 and a not in ('2', '32') and b not in NUMS:
                    tok.append((NUMS[a][1], b))
    def div(pairs):
        s = Counter(b for k, b in pairs if k == 'short')
        l = Counter(b for k, b in pairs if k == 'long')
        return jsd(s, l) if s and l else 0
    obs = div(tok)
    lab = [k for k, _ in tok]
    ge = 0
    for _ in range(500):
        random.shuffle(lab)
        ge += div(list(zip(lab, [b for _, b in tok]))) >= obs
    return 'JSD %.3f bits (%d short, %d long tokens), permutations as large %d of 500' % (
        obs, sum(1 for k, _ in tok if k == 'short'), sum(1 for k, _ in tok if k == 'long'), ge)


def rp7(texts, keys, lex):
    out = []
    freq = Counter(g for t in texts for g in t)
    for title, lang, key in keys:
        real = bench.score(texts, key, lex[lang], bench.ENDINGS[lang])
        sims = sorted(bench.score(texts, k2, lex[lang], bench.ENDINGS[lang])
                      for k2 in bench.shuffles(key, freq, n=100, band=10 if len(key) > 60 else 3))
        out.append('%s: %.1f%% against shuffles %.1f%% (%d of 100 as good)' % (
            title, 100 * real, 100 * sims[50], sum(1 for s in sims if s >= real)))
    return '; '.join(out)


def main(mw, dedr, sux, yaj):
    lex, _ = bench.lexicons(mw, dedr, sux)
    keys = [('Yajnadevam', 'sa', bench.load_yajnadevam(yaj)[1]),
            ('Parpola 1994', 'dra', bench.load_key(os.path.join(HERE, 'keys', 'parpola1994.tsv'))[1])]
    say('# The main findings on the M77 texts')
    say()
    say('The M77-only texts (merge_m77.py) are Mahadevan\'s transcriptions of texts that the ICIT-derived dump lacks '
        'or transcribes too differently to match: an independent sample, with signs mapped to ICIT ids through '
        'the alignment (about 7%% of its tokens have no counterpart and count as unknown).')
    say()
    for lab, rows in (('ICIT-derived', load()), ('M77 additions only', load(only_m77=True)),
                      ('merged', load(with_m77=True))):
        rows = [r for r in rows if r['flat']]
        texts = [ln for r in rows for ln in r['seq'] if len(ln) >= 2]
        texts3 = [t for t in texts if len(t) >= 3]
        say('## %s (%d objects, %d lines of 2+ signs)' % (lab, len(rows), len(texts)))
        say()
        say('- RP1 endings fixed per name: %s.' % rp1(texts))
        say('- RP2 520 after a fish-final name: %s.' % rp2(texts))
        say('- RP3 %s.' % rp3(texts))
        say('- RP4 %s.' % rp4(rows))
        say('- RP5 opening formula: %s.' % rp5(rows))
        say('- RP6 short against long strokes: %s.' % rp6(rows))
        say('- RP7 %s.' % rp7(texts3, keys, lex))
        say()
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'replicate_m77.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(*sys.argv[1:5])
