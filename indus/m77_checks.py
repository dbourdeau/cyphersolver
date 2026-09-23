"""Cross-check the frequency claims of Parpola 2005 on Mahadevan's M77 corpus, an
independent transcription with its own sign list (Mahadevan 1977; 2,906 texts).

The machine-readable M77 used here is data/m77_indusscript_real_corpus.csv in
https://github.com/joyboseroy/indus_decipher (one row per line, sign ids 'MSgNNN',
stored in reading order: the jar MSg342 ends 974 lines and begins 4). It came from a
logged-in export of indusscript.in (RMRL), so it is not copied into this folder.
In Mahadevan's numbering the 9xxx texts are the finds from West Asia.

Usage: python m77_checks.py path/to/m77_indusscript_real_corpus.csv
Writes results/m77_checks.md.
"""
import csv
import os
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))


def main(path):
    rows = list(csv.DictReader(open(path, encoding='utf-8')))
    texts = defaultdict(list)
    for r in rows:
        texts[r['inscription_id'].split('.')[0]].append(r['sign_sequence'].split())
    tok = Counter(s for r in rows for s in r['sign_sequence'].split())
    N = sum(tok.values())
    jar, jc = tok.most_common(1)[0]
    out = ['# Parpola 2005 against Mahadevan\'s M77 corpus', '']
    out.append('Corpus: %d lines, %d texts, %d sign tokens, %d sign types (MSg0 = unread '
               'sign, counted as a token).' % (len(rows), len(texts), N, len(tok)))
    out.append('')
    lens = sorted(((sum(len(x) for x in v), k) for k, v in texts.items()), reverse=True)
    out.append('- mean signs per text: %.2f; longest: %s (p. 45: "the longest text is merely 26 '
               'signs").' % (sum(n for n, _ in lens) / len(lens),
                             ', '.join('text %s %d' % (k, n) for n, k in lens[:3])))
    single = sum(1 for c in tok.values() if c == 1)
    out.append('- sign types occurring once: %d of %d = %.0f%%.' % (single, len(tok),
                                                                 100 * single / len(tok)))
    first = sum(1 for r in rows if r['sign_sequence'].split()[0] == jar)
    last = sum(1 for r in rows if r['sign_sequence'].split()[-1] == jar)
    out.append('- most frequent sign: %s, %d tokens = %.1f%% (p. 47: "almost 10%%"); it ends '
               '%d lines and begins %d.' % (jar, jc, 100 * jc / N, last, first))
    dd = [(r['inscription_id'], r['sign_sequence']) for r in rows
          if any(a == b == jar for a, b in zip(r['sign_sequence'].split(),
                                               r['sign_sequence'].split()[1:]))]
    out.append('- %s beside itself: %d time(s): %s (p. 47: never in the Indus Valley; once on a '
               'round seal probably from Mesopotamia).' % (jar, len(dd), dd))
    for lab, pick in (('West Asian finds (9xxx)', lambda i: i.startswith('9')),
                      ('all other texts', lambda i: not i.startswith('9'))):
        bi = same = 0
        ex = Counter()
        for r in rows:
            if not pick(r['inscription_id']):
                continue
            s = [x for x in r['sign_sequence'].split() if x != 'MSg0']
            for a, b in zip(s, s[1:]):
                bi += 1
                if a == b:
                    same += 1
                    ex[a] += 1
        out.append('- doubled signs, %s: %d of %d adjacent pairs = %.1f%%; %s' % (
            lab, same, bi, 100 * same / bi, dict(ex.most_common(8))))
    out += ['', '## The sign claims on M77', '',
            'Sign groups from the ICIT alignment (align_m77.py, data/icit_m77_map.tsv): '
            'fish series MSg59-75, crab MSg53/58, fig MSg348/367/370/371, eye MSg375, '
            'water MSg294, pot MSg328; numerals 97=1 99=2 102=3 103=3 104=4 106=5 109=6 '
            '112=7 114=8 86=1 87=2 89=3 96=5 121=12 (short, two-tier and long strokes).', '']
    out += claims(rows)
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'm77_checks.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    print('\n'.join(out))


M = lambda *n: {'MSg%d' % i for i in n}
FISH = M(*range(59, 76))
FISH_PLAIN = 'MSg59'
CRAB = M(53, 58)
FIG = M(348, 367, 370, 371)
EYE = M(375)
WATER = M(294)
POT = M(328)
NUM = {'MSg97': 1, 'MSg99': 2, 'MSg102': 3, 'MSg103': 3, 'MSg104': 4, 'MSg106': 5,
       'MSg109': 6, 'MSg112': 7, 'MSg114': 8, 'MSg86': 1, 'MSg87': 2, 'MSg89': 3,
       'MSg96': 5, 'MSg121': 12}


def claims(rows):
    import random
    random.seed(20260923)
    lines = [[x for x in r['sign_sequence'].split()] for r in rows]
    ids = [r['inscription_id'] for r in rows]
    home = [ln for ln, i in zip(lines, ids) if not i.startswith('9')]
    out = []

    def pairs(ls, A, B):
        return [(a, b) for ln in ls for a, b in zip(ln, ln[1:]) if a in A and b in B]

    def shuffled(ls, f, n=300):
        vals = []
        for _ in range(n):
            fake = []
            for ln in ls:
                s = ln[:]
                random.shuffle(s)
                fake.append(s)
            vals.append(f(fake))
        return vals

    byval = Counter(NUM[a] for a, b in pairs(lines, set(NUM), {FISH_PLAIN}))
    out.append('- numerals read immediately before the plain fish, by value: ' +
               ', '.join('%d: %d' % kv for kv in sorted(byval.items())))
    whole = [(i, ln) for i, ln in zip(ids, lines) if len(ln) == 2 and ln[0] in NUM
             and ln[1] == FISH_PLAIN]
    out.append('- whole lines that are numeral + plain fish: ' + '; '.join(
        '%s (%d)' % (i, NUM[ln[0]]) for i, ln in whole))
    for lab, A, B in (('6 + fish', M(109), {FISH_PLAIN}), ('7 + fish', M(112), {FISH_PLAIN}),
                      ('any numeral + fish', set(NUM), {FISH_PLAIN}),
                      ('any numeral + pot', set(NUM), POT),
                      ('fig + fish', FIG, {FISH_PLAIN}), ('fig + anything', FIG, None),
                      ('crab + plain fish', CRAB, {FISH_PLAIN}),
                      ('crab + fish series', CRAB, FISH),
                      ('eye + eye', EYE, EYE), ('water + eye', WATER, EYE)):
        if B is None:
            nxt = Counter(b for a, b in pairs(lines, A, set(tok_all(lines))))
            out.append('- %s: %s' % (lab, dict(nxt.most_common(8))))
            continue
        obs = len(pairs(lines, A, B))
        null = shuffled(lines, lambda ls: len(pairs(ls, A, B)))
        out.append('- %s: %d (shuffled mean %.1f; %d of 300 shuffles as high)' % (
            lab, obs, sum(null) / len(null), sum(1 for v in null if v >= obs)))
    ends = [i for i, ln in zip(ids, lines) if len(ln) >= 2 and ln[-2] in WATER and ln[-1] in EYE]
    whole = [i for i, ln in zip(ids, lines) if ln and all(x in WATER | EYE for x in ln)]
    out.append('- lines ending water + eye: %s; lines that are only water/eye signs: %s'
               % (ends, whole))
    ncrab = sum(1 for ln in lines for x in ln if x in CRAB)
    near = lambda ls: sum(1 for ln in ls for k, x in enumerate(ln) if x in CRAB and any(
        y in FISH for y in ln[max(0, k - 1):k] + ln[k + 1:k + 2]))
    obs = near(lines)
    null = shuffled(lines, near)
    out.append('- crab tokens with a fish sign beside them: %d of %d (shuffled mean %.1f; %d of '
               '300 as high)' % (obs, ncrab, sum(null) / len(null),
                                 sum(1 for v in null if v >= obs)))
    return out


def tok_all(lines):
    return {x for ln in lines for x in ln}


if __name__ == '__main__':
    main(sys.argv[1])
