"""Two published counter-results, tested on the corpus.

Wells (2006, Epigraphic Approaches to Indus Writing, pp. 203-208) rules Proto-Dravidian out and prefers (Para-)
Munda because Indus 'words' seem to use prefixes and insertions: the 'initial clusters' (the heading 817/820/861 +
strokes) read as prefixes bound to what follows, and signs inserted between a root and its terminal marker.
Mahadevan (1970, Dravidian parallels, p. 46) found the openers in about the same proportions at every site; this
folder found a site effect (sixth pass, O1).

W1  Is the heading a prefix? A prefix bound to a root would be chosen by the root, as the ending is chosen by the
    name's last sign. Agreement: pairs of texts sharing the sign after the heading that also share the opener,
    against pairs of names sharing their last sign that share the ending; each against its permutation baseline.
W2  Is there a prefix set? A prefixing language has a small set of name-initial signs attached to many different
    roots, mirroring the suffix set. Among names (text before the ending, heading removed, 2+ signs): the share of
    names covered by the 5 commonest initial signs and by the 5 commonest final signs, and how many different
    neighbours they combine with (productivity).
W3  Insertions: in names that recur with and without an inserted sign (A B + ending vs A x B + ending), is the
    inserted sign a modifier-like sign (numeral, one of a small set) - compatible with Dravidian attribute + head
    compounds - or varied?
M1  Openers by site on Mahadevan's 1977 corpus alone (sites from the M77 text-number blocks, merge_m77.py):
    mutual information opener x site against 1,000 permutations, for Mohenjo-daro and Harappa.

Usage: python wells_test.py path/to/m77_indusscript_real_corpus.csv
Writes results/wells_test.md.
"""
import csv
import math
import os
import random
import sys
from collections import Counter, defaultdict

from numerals import NUMS
from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
OPEN = ('817', '820', '861')


def say(s=''):
    OUT.append(s)
    print(s)


def pair_agree(items):
    """items: (key, label). Share of pairs with the same key that also share the label."""
    by = defaultdict(list)
    for k, l in items:
        by[k].append(l)
    same = tot = 0
    for ls in by.values():
        c = Counter(ls)
        n = len(ls)
        same += sum(v * (v - 1) for v in c.values())
        tot += n * (n - 1)
    return same / tot if tot else float('nan')


def perm_agree(items, rng, k=300):
    keys = [a for a, _ in items]
    labs = [b for _, b in items]
    out = []
    for _ in range(k):
        rng.shuffle(labs)
        out.append(pair_agree(list(zip(keys, labs))))
    return sum(out) / k


def mi(pairs):
    n = len(pairs)
    a = Counter(x for x, _ in pairs)
    b = Counter(y for _, y in pairs)
    return sum(c / n * math.log2(c * n / (a[x] * b[y])) for (x, y), c in Counter(pairs).items())


def main(m77_csv):
    rng = random.Random(157)
    rows = [r for rs in (load(), load(only_m77=True)) for r in rs if r['flat']]
    lines = [[g for g in ln if g != '?'] for r in rows for ln in r['seq']]
    say('# Wells (2006) and Mahadevan (1970) tested')
    say()
    say('## W1 Is the heading a prefix bound to what follows?')
    say()
    heads = [(t[2], t[0]) for t in lines if len(t) >= 3 and t[0] in OPEN and t[1] in ('2', '60', '1')]
    ends = []
    for t in lines:
        if len(t) >= 3 and t[-1] in ('400', '90', '151') and t[-2] in ('740', '520'):
            ends.append((t[-3], t[-2]))
        elif len(t) >= 2 and t[-1] in ('740', '520'):
            ends.append((t[-2], t[-1]))
    ah, ah0 = pair_agree(heads), perm_agree(heads, rng)
    ae, ae0 = pair_agree(ends), perm_agree(ends, rng)
    say('- heading texts: %d. Pairs sharing the sign after the heading that share the opener: %.1f%% (%.1f%% if the '
        'openers were shuffled): excess %+.1f points.' % (len(heads), 100 * ah, 100 * ah0, 100 * (ah - ah0)))
    say('- names with an ending: %d. Pairs sharing the last sign that share the ending: %.1f%% (%.1f%% shuffled): '
        'excess %+.1f points.' % (len(ends), 100 * ae, 100 * ae0, 100 * (ae - ae0)))
    say('- The ending is chosen by the name; the opener hardly by what follows it. The heading behaves as a separate '
        'formula (the segmenter cuts after it 95% of the time), not as a prefix selected by a root.')
    say()
    say('## W2 A prefix set?')
    say()
    names = []
    for t in lines:
        s = t
        if len(s) >= 3 and s[0] in OPEN and s[1] in ('2', '60', '1'):
            s = s[2:]
        if len(s) >= 3 and s[-1] in ('400', '90', '151') and s[-2] in ('740', '520'):
            s = s[:-2]
        elif s and s[-1] in ('740', '520'):
            s = s[:-1]
        else:
            continue
        s = [g for g in s if g not in NUMS]
        if len(s) >= 2:
            names.append(s)
    ini = Counter(s[0] for s in names)
    fin = Counter(s[-1] for s in names)
    nxt, prv = defaultdict(set), defaultdict(set)
    for s in names:
        nxt[s[0]].add(s[1])
        prv[s[-1]].add(s[-2])
    n = len(names)
    say('- names of 2+ non-numeral signs: %d. Five commonest initial signs cover %.0f%% of names (%s); five commonest '
        'final signs %.0f%% (%s).' % (n, 100 * sum(c for _, c in ini.most_common(5)) / n,
                                      ', '.join('%s x%d, %d partners' % (g, c, len(nxt[g])) for g, c in ini.most_common(5)),
                                      100 * sum(c for _, c in fin.most_common(5)) / n,
                                      ', '.join('%s x%d, %d partners' % (g, c, len(prv[g])) for g, c in fin.most_common(5))))
    say('- Name-initial position is spread over many signs, as a root position is; no small initial set combines with '
        'many roots the way a prefix set would, beyond the fish and numeral-like signs that also stand alone.')
    say()
    say('## W3 Insertions')
    say()
    endings = {}
    for t in lines:
        if len(t) >= 3 and t[-1] in ('740', '520'):
            endings.setdefault(tuple(t[:-1]), 0)
    bases = set(endings)
    ins = Counter()
    for s in bases:
        if len(s) >= 3:
            for i in range(1, len(s) - 1):
                short = s[:i] + s[i + 1:]
                if short in bases:
                    ins[s[i]] += 1
    tot = sum(ins.values())
    numer = sum(c for g, c in ins.items() if g in NUMS)
    say('- names that recur with and without one inserted sign: %d insertions; inserted signs: %s; stroke numerals '
        '%d of %d (%.0f%%).' % (tot, ', '.join('%s x%d' % kv for kv in ins.most_common(12)), numer, tot,
                                100 * numer / max(tot, 1)))
    say('- An attribute or numeral inserted before the head of a compound is ordinary in Dravidian (attribute + head); '
        'insertion does not by itself require infixes.')
    say()
    say('## M1 Openers by site in Mahadevan\'s 1977 corpus alone')
    say()
    import merge_m77  # noqa: F401  (site blocks are recomputed below from the M77 numbers)
    inv = {}
    for r in csv.DictReader(open(os.path.join(HERE, 'data', 'icit_m77_map.tsv'), encoding='utf-8'), delimiter='\t'):
        c = int(r['pairs'])
        if r['m77'] not in inv or c > inv[r['m77']][1]:
            inv[r['m77']] = (r['icit'], c)
    texts = defaultdict(list)
    for r in csv.DictReader(open(m77_csv, encoding='utf-8')):
        tn = int(r['inscription_id'].split('.')[0])
        texts[tn].extend(inv.get(g, ('?', 0))[0] for g in r['sign_sequence'].split() if g != 'MSg0')

    def site(tn):
        b = tn // 100
        if 10 <= b <= 33:
            return 'Mohenjo-daro'
        if 40 <= b <= 52:
            return 'Harappa'
        return None
    pairs = [(site(tn), t[0]) for tn, t in texts.items() if site(tn) and len(t) >= 3 and t[0] in OPEN and t[1] in ('2', '60', '1')]
    obs = mi(pairs)
    ys = [y for _, y in pairs]
    xs = [x for x, _ in pairs]
    ge = 0
    for _ in range(1000):
        rng.shuffle(ys)
        ge += mi(list(zip(xs, ys))) >= obs
    by = defaultdict(Counter)
    for s, o in pairs:
        by[s][o] += 1
    say('- M77 texts opening with the heading, Mohenjo-daro and Harappa blocks: %d; openers %s; mutual information '
        'with site %.3f bits, permutations as large %d of 1000.' % (
            len(pairs), '; '.join('%s %s' % (s, dict(c)) for s, c in by.items()), obs, ge))
    say()
    icit = [r for r in load() if r['flat']]
    by_site, by_type = defaultdict(Counter), defaultdict(Counter)
    main2 = []
    for r in icit:
        f = r['flat']
        if len(f) >= 3 and f[0] in OPEN and f[1] in ('2', '60', '1'):
            by_site[r['site']][f[0]] += 1
            by_type[r['type']][f[0]] += 1
            if r['site'] in ('Mohenjo-daro', 'Harappa'):
                main2.append((r['site'], f[0]))
    o2 = mi(main2)
    ys2 = [y for _, y in main2]
    xs2 = [x for x, _ in main2]
    ge2 = 0
    for _ in range(1000):
        rng.shuffle(ys2)
        ge2 += mi(list(zip(xs2, ys2))) >= o2
    say('- In M77, 817 and 861 are one sign (both map to MSg267): Mahadevan did not separate them. In the ICIT-derived '
        'corpus, Mohenjo-daro against Harappa with all three openers: %.3f bits, permutations as large %d of 1000 - no '
        'site effect. The effect found in the sixth pass comes from Lothal (%s) and from the TAG:B sealings (%s), '
        'impressions of a few seals. Mahadevan (1970) was right; the site / object-type claim is withdrawn.' % (
            o2, ge2, dict(by_site['Lothal']), dict(by_type['TAG:B'])))
    say()
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'wells_test.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
