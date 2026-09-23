"""Test the corpus claims in Asko Parpola, 'Study of the Indus Script' (ICES Tokyo 2005,
Transactions of the International Conference of Eastern Studies 50, pp. 28-66),
https://old.harappa.com/script/indusscript.pdf, against the ICIT-derived corpus
(data/corpus.tsv, built by build_corpus.py). Writes results/parpola_checks.md.

Every number below is computed here; page numbers refer to the lecture.
"""
import math
import os
import random
from collections import Counter, defaultdict

from signs import (CRAB, EYE, FIG, FIG_CRAB, FISH, FISH_PLAIN, JAR, NUMERAL, POT,
                   ROOF_FISH, WATER, WEST_ASIA, CENTRAL_ASIA, load, south_asian)

HERE = os.path.dirname(os.path.abspath(__file__))
random.seed(20260923)
OUT = []


def say(s=''):
    OUT.append(s)
    print(s)


def bigrams(rows):
    for r in rows:
        for ln in r['seq']:
            for a, b in zip(ln, ln[1:]):
                yield r, a, b


def shuffle_null(rows, test, n=1000):
    """Distribution of test(rows') where each line's signs are shuffled in place."""
    lines = [(r, ln) for r in rows for ln in r['seq']]
    vals = []
    for _ in range(n):
        fake = []
        for r, ln in lines:
            s = ln[:]
            random.shuffle(s)
            fake.append({'seq': [s], 'flat': s, 'site': r['site'], 'cisi': r['cisi']})
        vals.append(test(fake))
    return vals


def pair_count(rows, A, B):
    return sum(1 for _, a, b in bigrams(rows) if a in A and b in B)


def main():
    rows = [r for r in load(split=True) if r['flat']]
    raw = [r for r in load(split=False) if r['flat']]
    sa = [r for r in rows if south_asian(r)]
    toks = Counter(g for r in rows for g in r['flat'])
    N = sum(toks.values())

    say('# Parpola 2005 against the ICIT-derived corpus')
    say()
    say('Corpus: %d objects (%d South Asian), %d sign tokens after splitting fused repeats, '
        '%d sign types.' % (len(rows), len(sa), N, len(toks)))
    say()

    # --- C1-C3 the general statistics (pp. 36, 45, 49)
    say('## C1-C3 General statistics (pp. 36, 45, 49)')
    lens = [len(r['flat']) for r in rows]
    say('- mean signs per object: %.2f; median %d; longest %d (p. 45: "the longest text is '
        'merely 26 signs"; p. 36: "on the average only five signs").'
        % (sum(lens) / len(lens), sorted(lens)[len(lens) // 2], max(lens)))
    longest = sorted(rows, key=lambda r: -len(r['flat']))[:3]
    say('- longest objects: ' + '; '.join('%s %s (%s) %d signs in %d lines' % (
        r['cisi'] or 'sealid ' + r['sealid'], r['site'], r['type'], len(r['flat']), len(r['seq']))
        for r in longest))
    rawtoks = Counter(g for r in raw for g in r['flat'])
    single = sum(1 for c in rawtoks.values() if c == 1)
    say('- sign types (unsplit glyph ids): %d; occurring once: %d = %.0f%% (p. 36, Farmer et al.: '
        '"between 25 to 50 per cent of the around 400-600 different signs are attested only once").'
        % (len(rawtoks), single, 100 * single / len(rawtoks)))
    say()

    # --- C4-C5 jar (p. 47)
    say('## C4-C5 The most frequent sign and its doubling (p. 47)')
    top = toks.most_common(3)
    say('- most frequent sign: %s with %d tokens = %.1f%% of all tokens (p. 47: "almost 10%%"); '
        'next %s (%d), %s (%d).' % (top[0][0], top[0][1], 100 * top[0][1] / N,
                                    top[1][0], top[1][1], top[2][0], top[2][1]))
    nb = sum(1 for _ in bigrams(rows))
    p = toks[JAR] / N
    jj = [(r['cisi'] or 'sealid ' + r['sealid'], r['site'], r['type'])
          for r, a, b in bigrams(rows) if a == JAR and b == JAR]
    say('- adjacent pairs in the corpus: %d. Expected jar+jar under independent signs: '
        '%d x p^2 = %.0f. Observed: %d, at %s.' % (nb, nb, nb * p * p, len(jj), jj))
    twice = [r for r in rows if r['flat'].count(JAR) >= 2]
    null = shuffle_null(rows, lambda rs: pair_count(rs, {JAR}, {JAR}), 500)
    say('- objects with the jar twice or more: %d; with the order shuffled inside each line '
        'the jar+jar pair would appear %.1f times on average (max %d in 500 shuffles).'
        % (len(twice), sum(null) / len(null), max(null)))
    for r in twice:
        say('    - %s %s %s: %s' % (r['cisi'] or 'sealid ' + r['sealid'], r['site'], r['type'],
                                   ' | '.join(' '.join(ln) for ln in r['seq'])))
    say()

    # --- C6 West Asian seals (p. 47)
    say('## C6 Indus seals found in West Asia: typical or unique sequences? (p. 47)')
    west_asia_surprisal(rows, sa)
    say()

    # --- C7 fish share (p. 52)
    say('## C7 Share of the fish signs (p. 52)')
    seals = [r for r in rows if r['type'].startswith('SEAL')]
    st = Counter(g for r in seals for g in r['flat'])
    fs = sum(c for g, c in st.items() if g in FISH)
    say('- fish series (%s): %d of %d tokens on seals = %.1f%% ("almost every tenth sign"); '
        'plain fish %s: %d; roof-fish %s: %d.' % (' '.join(sorted(FISH, key=int)), fs,
                                                 sum(st.values()), 100 * fs / sum(st.values()),
                                                 FISH_PLAIN, toks[FISH_PLAIN], '235',
                                                 toks['235']))
    say()

    # --- C8 numeral + fish (p. 54)
    say('## C8 Numeral + fish (p. 54)')
    before_fish = Counter()
    for r, a, b in bigrams(rows):
        if b == FISH_PLAIN and a in NUMERAL:
            before_fish[NUMERAL[a]] += 1
    say('- numerals read immediately before the plain fish, by value: ' +
        ', '.join('%d: %d' % kv for kv in sorted(before_fish.items())))
    only = [r for r in rows if len(r['flat']) == 2 and r['flat'][1] == FISH_PLAIN
            and r['flat'][0] in NUMERAL]
    say('- whole inscriptions that are numeral + plain fish: ' + '; '.join(
        '%s %s %s (%d strokes)' % (r['cisi'] or r['sealid'], r['site'], r['type'],
                                   NUMERAL[r['flat'][0]]) for r in only))
    takes = Counter()
    for r, a, b in bigrams(rows):
        if a in NUMERAL:
            takes[b] += 1
    say('- signs most often read right after a numeral: ' +
        ', '.join('%s (%d)' % kv for kv in takes.most_common(12)))
    say()

    # --- C9-C13 fig, crab, crab+fish (pp. 55-59)
    say('## C9-C13 Fig, crab and their combinations (pp. 55-59)')
    for name, S in (('fig', FIG), ('fig+crab ligature', FIG_CRAB), ('crab', CRAB)):
        say('- %s %s: %d tokens' % (name, ' '.join(sorted(S, key=int)),
                                    sum(toks[g] for g in S)))
    fig_next = Counter(b for r, a, b in bigrams(rows) if a in FIG)
    say('- signs read right after the fig: %s' % dict(fig_next.most_common()))
    for r in rows:
        if any(g in FIG_CRAB for g in r['flat']):
            say('    - fig+crab on %s %s %s: %s' % (r['cisi'] or 'sealid ' + r['sealid'],
                                                 r['site'], r['type'], ' '.join(r['flat'])))
    tabs = defaultdict(list)
    for r in rows:
        if r['type'] == 'TAB:C':
            tabs[' '.join(r['flat'])].append(r['cisi'])
    say('- copper tablets (TAB:C), %d objects; the Fig. 4 inscription (read '
        '806 845 61 407 850 900 740) is on %d, the fig+crab sign alone on %d (Fig. 4: 14 and 7 '
        'examples). Tablets sharing the tail 845 (61) 407:' % (
            sum(len(v) for v in tabs.values()), len(tabs['806 845 61 407 850 900 740']),
            len(tabs['777'])))
    for k, v in sorted(tabs.items(), key=lambda x: -len(x[1])):
        if '845' in k.split() and '407' in k.split():
            say('    - %d x %s' % (len(v), k))
    cf = [(r['cisi'] or r['sealid'], a, b) for r, a, b in bigrams(rows)
          if a in CRAB and b in FISH]
    say('- crab read immediately before a fish sign: %d times %s (p. 58: "three times")'
        % (len(cf), cf))
    near = lambda rs: sum(1 for r in rs for ln in r['seq'] for i, g in enumerate(ln)
                          if g in CRAB and any(x in FISH for x in ln[max(0, i - 1):i] + ln[i + 1:i + 2]))
    obs = near(rows)
    ncrab = sum(toks[g] for g in CRAB)
    null = shuffle_null(rows, near, 500)
    mu = sum(null) / len(null)
    say('- crab tokens with a fish sign immediately beside them: %d of %d (%.0f%%); with the '
        'signs shuffled inside each line: %.1f expected, exceeded in %d of 500 shuffles '
        '(p. 57: "usually occurs in the immediate vicinity of the fish signs").'
        % (obs, ncrab, 100 * obs / ncrab, mu, sum(1 for v in null if v >= obs)))
    say()

    # --- C14-C15 eye (pp. 60-61)
    say('## C14-C15 Eye + eye and water + eye (pp. 60-61)')
    for A, B, lab in ((EYE, EYE, 'eye + eye'), (WATER, EYE, 'water + eye'),
                      (WATER, set(toks), 'water + anything')):
        hits = [(r['cisi'] or r['sealid'], a, b) for r, a, b in bigrams(rows) if a in A and b in B]
        say('- %s: %d; %s' % (lab, len(hits), Counter((a, b) for _, a, b in hits).most_common(6)))
    fin = [r for r in rows if len(r['flat']) >= 2 and r['flat'][-2] in WATER and r['flat'][-1] in EYE]
    say('- inscriptions ending water + eye: ' + ', '.join(
        '%s (%s)' % (r['cisi'] or r['sealid'], ' '.join(r['flat'])) for r in fin))
    say()

    # --- C16 repetition (pp. 36-38)
    say('## C16 Sign repetition within one inscription (pp. 36-38)')
    repetition(rows, toks)
    say()

    # --- C17 compounds as units
    say('## C17 Are the proposed compounds real units? (PMI against a within-line shuffle)')
    pmi_table(rows)

    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'parpola_checks.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


def lm(train):
    uni, bi, ctx = Counter(), Counter(), Counter()
    for r in train:
        for ln in r['seq']:
            s = ['<s>'] + ln + ['</s>']
            uni.update(s[1:])
            for a, b in zip(s, s[1:]):
                bi[a, b] += 1
                ctx[a] += 1
    return uni, bi, ctx


def surprisal(r, uni, bi, ctx, V, lam=0.6):
    """Per-sign bits: interpolated bigram, and plain unigram (add-one)."""
    tot = sum(uni.values())
    hb = hu = n = 0
    for ln in r['seq']:
        s = ['<s>'] + ln + ['</s>']
        for a, b in zip(s, s[1:]):
            pu = (uni[b] + 1) / (tot + V)
            pb = bi[a, b] / ctx[a] if ctx[a] else 0
            hb += -math.log2(lam * pb + (1 - lam) * pu)
            hu += -math.log2(pu)
            n += 1
    return hb / n, hu / n


def west_asia_surprisal(rows, sa):
    uni, bi, ctx = lm(sa)
    V = len(uni) + 1
    home = []
    for r in sa:  # leave-one-out
        u, b, c = lm([r])
        uni2, bi2, ctx2 = uni - u, bi - b, ctx - c
        hb, hu = surprisal(r, uni2, bi2, ctx2, V)
        home.append((hb, hb - hu))
    away = [r for r in rows if r['site'] in WEST_ASIA or (r['site'] in ('Unknown', '') and
                                                         r['type'] in ('SEAL:C', 'SEAL:CY'))]
    say('Model: bigram language model (interpolated with unigram) trained on the %d South '
        'Asian objects, each home object scored leave-one-out. "order" = bigram bits minus '
        'unigram bits: negative when the signs stand in their usual order, positive when common '
        'signs stand in unusual order. Percentile = share of home objects scoring lower.' % len(sa))
    say()
    say('| object | site | type | signs (reading order) | bits/sign | pct | order | pct |')
    say('|---|---|---|---|---|---|---|---|')
    hb_sorted = sorted(h for h, _ in home)
    od_sorted = sorted(o for _, o in home)
    pct = lambda xs, v: 100 * sum(1 for x in xs if x < v) / len(xs)
    groups = defaultdict(list)
    for r in away:
        hb, hu = surprisal(r, uni, bi, ctx, V)
        shape = 'square' if r['type'] == 'SEAL:S' else ('round/cylinder' if r['type'] in (
            'SEAL:C', 'SEAL:CY') else 'other')
        groups[shape].append((pct(hb_sorted, hb), pct(od_sorted, hb - hu)))
        say('| %s | %s | %s | %s | %.2f | %.0f | %+.2f | %.0f |' % (
            r['cisi'] or 'sealid ' + r['sealid'], r['site'], r['type'], ' '.join(r['flat']),
            hb, pct(hb_sorted, hb), hb - hu, pct(od_sorted, hb - hu)))
    say()
    for k, v in groups.items():
        say('- %s (%d): median percentile, bits/sign %.0f, order %.0f' % (
            k, len(v), sorted(x for x, _ in v)[len(v) // 2], sorted(y for _, y in v)[len(v) // 2]))


def repetition(rows, toks):
    N = sum(toks.values())
    signs, w = zip(*toks.items())
    say('Share of inscriptions (one line, excluding numerals) with a sign occurring twice, '
        'observed vs. the same lengths drawn at random from the corpus sign frequencies '
        '(2,000 draws per inscription). A phonetic script roughly follows the random line '
        '(p. 36-37, Farmer et al.); a logo-syllabic seal legend need not (Parpola).')
    say()
    say('| length | inscriptions | observed repeat | random repeat |')
    say('|---|---|---|---|')
    bins = defaultdict(lambda: [0, 0, 0.0])
    for r in rows:
        for ln in r['seq']:
            s = [g for g in ln if g not in NUMERAL]
            L = len(s)
            if L < 2:
                continue
            k = min(L, 10)
            bins[k][0] += 1
            bins[k][1] += len(set(s)) < L
    ws = [x / N for x in w]
    for k in sorted(bins):
        draws = 2000
        hit = 0
        for _ in range(draws):
            s = random.choices(signs, ws, k=k)
            hit += len(set(s)) < k
        n, obs, _ = bins[k]
        say('| %s | %d | %.1f%% | %.1f%% |' % ('%d+' % k if k == 10 else k, n,
                                             100 * obs / n, 100 * hit / draws))


def pmi_table(rows):
    uni_first, uni_second, pairs = Counter(), Counter(), Counter()
    for _, a, b in bigrams(rows):
        uni_first[a] += 1
        uni_second[b] += 1
        pairs[a, b] += 1
    NB = sum(pairs.values())
    claims = [('6 + fish (aru-min, Pleiades)', {'16', '36'}, {FISH_PLAIN}),
              ('7 + fish (elu-min, Ursa Major)', {'17', '7'}, {FISH_PLAIN}),
              ('any numeral + fish', set(NUMERAL), {FISH_PLAIN}),
              ('any numeral + pot', set(NUMERAL), POT),
              ('fig + fish (vata-min, north star)', FIG, {FISH_PLAIN}),
              ('crab + fish series (kon-min)', CRAB, FISH),
              ('eye + eye (kan-kani, overseer)', EYE, EYE),
              ('water + eye (nir-k-kanti)', WATER, EYE),
              ('roof-fish + anything', ROOF_FISH, None)]
    say('| pair (reading order) | observed | expected | PMI (bits) | shuffles >= observed |')
    say('|---|---|---|---|---|')
    for lab, A, B in claims:
        if B is None:
            continue
        obs = sum(c for (a, b), c in pairs.items() if a in A and b in B)
        exp = sum(uni_first[a] for a in A) * sum(uni_second[b] for b in B) / NB
        null = shuffle_null(rows, lambda rs: pair_count(rs, A, B), 300)
        say('| %s | %d | %.1f | %s | %d / 300 |' % (
            lab, obs, exp, '%.2f' % math.log2(obs / exp) if obs and exp else 'n/a',
            sum(1 for v in null if v >= obs)))


if __name__ == '__main__':
    main()
