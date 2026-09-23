"""Seventh pass, lead 1: the numeral + fish signs against the Tamil star names actually attested.

Parpola reads numeral + fish as Old Tamil numeral + min 'star' asterism names (3 + fish mum-min,
6 + fish aru-min 'Pleiades', 7 + fish elu-min 'Ursa Major'). The Tamil Lexicon (Madras 1924-36,
DSAL: headwords ending in -min, and full-text searches for Pleiades, constellation, asterism, Ursa;
parsed into rebus/tlex_star_min.tsv) attests numeral + min star names for 3, 5, 6 and 7 only.

Test: among stroke numerals written immediately before a fish sign, what share has one of those
values, against the share among stroke numerals written before any other sign? If numeral + fish
were numeral + min star names, the attested values should be over-represented before the fish.
Permutation of the following-sign class among numeral tokens. Short and long pairs (2, 32) are left
out in the main count (Parpola reads the long pair as vel 'intermediate space'), then included.

(* marks a value with an attested star name.)

Writes results/tamil_stars.md.
"""
import os
import random
from collections import Counter

from numerals import NUMS
from signs import FISH, load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
random.seed(53)


def say(s=''):
    OUT.append(s)
    print(s)


def attested():
    vals = set()
    with open(os.path.join(HERE, 'rebus', 'tlex_star_min.tsv'), encoding='utf-8') as f:
        for ln in f:
            if ln.startswith('#') or not ln.strip():
                continue
            c = ln.rstrip('\n').split('\t')
            if c[3] != '-':
                vals.add(int(c[3]))
    return vals


def main():
    good = attested()
    rows = [r for r in load(split=False) if r['flat']]
    say('# Numeral + fish against the numeral + min star names of the Tamil Lexicon')
    say()
    say('Numeral + min star names attested (rebus/tlex_star_min.tsv): values %s.' % sorted(good))
    say()
    seen, distinct = set(), []
    for r in rows:
        k = tuple(tuple(ln) for ln in r['seq'])
        if k not in seen:
            seen.add(k)
            distinct.append(r)
    for lab, skip, rs in (('pairs left out', {'2', '32'}, rows), ('pairs included', set(), rows),
                          ('pairs left out, distinct texts only (duplicate sealings and tablet copies counted once)',
                           {'2', '32'}, distinct),
                          ('distinct texts, and the single stroke left out where it stands in the opener formula '
                           '(after 817/820/861, the pair or 60)', {'2', '32', 'opener'}, distinct)):
        tok = []
        for r in rs:
            for ln in r['seq']:
                for i, (a, b) in enumerate(zip(ln, ln[1:])):
                    if 'opener' in skip and a in ('1', '31') and i and ln[i - 1] in ('817', '820', '861', '2', '32', '60'):
                        continue
                    if a in NUMS and a not in skip and b not in NUMS:
                        tok.append((NUMS[a][0], b in FISH))
        fish = Counter(v for v, f in tok if f)
        other = Counter(v for v, f in tok if not f)
        nf, no = sum(fish.values()), sum(other.values())
        kf = sum(c for v, c in fish.items() if v in good)
        ko = sum(c for v, c in other.items() if v in good)
        obs = kf / nf - ko / no
        flags = [f for _, f in tok]
        vals = [v for v, _ in tok]
        ge = 0
        for _ in range(10000):
            random.shuffle(flags)
            a = sum(1 for v, f in zip(vals, flags) if f and v in good)
            ge += a / nf - (sum(1 for v in vals if v in good) - a) / no >= obs - 1e-12
        say('## %s' % lab)
        say()
        say('- numerals before a fish sign: %d; value %s.' % (nf, ', '.join('%d x%d' % kv for kv in sorted(fish.items()))))
        say('- numerals before any other sign: %d; value %s.' % (no, ', '.join('%d x%d' % kv for kv in sorted(other.items()))))
        say('- share with an attested star-name value (%s): before fish %d/%d (%.0f%%), elsewhere %d/%d (%.0f%%); '
            'one-sided permutation p = %.4f.' % ('/'.join(map(str, sorted(good))), kf, nf, 100 * kf / nf, ko, no,
                                                 100 * ko / no, ge / 10000))
        say('- by value, share before fish / share elsewhere: %s.' % ', '.join(
            '%d%s %.1f%%/%.1f%% (x%.1f)' % (v, '*' if v in good else '', 100 * fish[v] / nf, 100 * other[v] / no,
                                          (fish[v] / nf) / (other[v] / no) if other[v] else float('inf'))
            for v in sorted(set(fish) | set(other))))
        miss = {v: c for v, c in fish.items() if v not in good}
        say('- numeral + fish with no attested star name: %s (%d of %d tokens).' % (
            ', '.join('%d x%d' % kv for kv in sorted(miss.items())), sum(miss.values()), nf))
        say()
    # the single stroke before a fish: numeral, or the opener formula's stroke?
    ctx = Counter()
    for r in distinct:
        for ln in r['seq']:
            for i in range(len(ln) - 1):
                if ln[i] in ('1', '31') and ln[i + 1] in FISH:
                    prev = ln[i - 1] if i else '^'
                    ctx['after the opener formula (817/820/861 or the pair)' if prev in ('817', '820', '861', '2', '32', '60')
                        else 'text-initial' if prev == '^' else 'after another sign'] += 1
    say('## The single stroke before a fish (distinct texts)')
    say()
    say('- %s.' % '; '.join('%s: %d' % kv for kv in ctx.most_common()))
    say()
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'tamil_stars.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
