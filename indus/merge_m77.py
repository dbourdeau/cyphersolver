"""Merge Mahadevan's 1977 concordance (M77) into the ICIT-derived corpus.

M77 (the mayig/indusscript export, 3,573 lines, 2,906 texts) has no site or object type, only
Mahadevan's text numbers. Its signs are mapped to ICIT glyph ids with data/icit_m77_map.tsv
(align_m77.py; for each M77 sign the ICIT glyph it was paired with most often). Each M77 text is
then compared with every ICIT object: an M77 text is taken to be an object already in the corpus
when an ICIT object's text is within a normalised edit distance of 0.25 (the two transcriptions
differ in detail) - with each ICIT object matched at most once, best matches first, so that texts
made in many copies keep their copies. The unmatched M77 texts are the additions.

Site: Mahadevan numbers texts in site blocks. For each block of 100 text numbers, the sites of the
matched ICIT objects give the block's site when one site has 80%+ of them (8+ matches); the
additions take the site of their block, or 'unknown'. Object type is 'M77' (not recorded).

Writes data/corpus_m77_added.tsv (same columns as corpus.tsv, signs in reading order in both
signs_visual and signs_reading; sealid 'M77-<text number>'), and results/merge_m77.md.
Use signs.load(with_m77=True) to read the merged corpus.

Usage: python merge_m77.py path/to/m77_indusscript_real_corpus.csv
"""
import csv
import os
import sys
from collections import Counter, defaultdict

from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []


def say(s=''):
    OUT.append(s)
    print(s)


def ed(a, b):
    d = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        p, d[0] = d[0], i
        for j, cb in enumerate(b, 1):
            p, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, p + (ca != cb))
    return d[len(b)]


def main(path):
    inv = {}
    for r in csv.DictReader(open(os.path.join(HERE, 'data', 'icit_m77_map.tsv'), encoding='utf-8'), delimiter='\t'):
        c = int(r['pairs'])
        if r['m77'] not in inv or c > inv[r['m77']][1]:
            inv[r['m77']] = (r['icit'], c)
    texts = defaultdict(list)
    unk = Counter()
    for r in csv.DictReader(open(path, encoding='utf-8')):
        tn = r['inscription_id'].split('.')[0]
        seq = []
        for g in r['sign_sequence'].split():
            if g == 'MSg0':
                continue
            if g in inv:
                seq.append(inv[g][0])
            else:
                seq.append('?')
                unk[g] += 1
        if seq:
            texts[tn].append(seq)
    rows = [r for r in load() if r['flat']]
    say('# Merging M77 into the corpus')
    say()
    say('- M77 texts: %d; sign tokens with no ICIT counterpart in the map: %d (%d sign types), kept as "?".' % (
        len(texts), sum(unk.values()), len(unk)))
    bylen = defaultdict(list)
    for i, r in enumerate(rows):
        bylen[len(r['flat'])].append(i)
    cands = []
    for tn, lines in texts.items():
        flat = [g for ln in lines for g in ln]
        n = len(flat)
        for L in range(max(1, n - n // 4 - 1), n + n // 4 + 2):
            for i in bylen.get(L, ()):
                f = rows[i]['flat']
                if abs(len(f) - n) > max(1, n // 4):
                    continue
                d = ed(flat, f) / max(n, len(f))
                if d <= 0.25:
                    cands.append((d, tn, i))
    cands.sort()
    used_t, used_i, match = set(), set(), {}
    for d, tn, i in cands:
        if tn in used_t or i in used_i:
            continue
        used_t.add(tn)
        used_i.add(i)
        match[tn] = (i, d)
    exact = sum(1 for i, d in match.values() if d == 0)
    say('- M77 texts matched to an ICIT object: %d (%d exactly, %d with small differences); ICIT objects with no '
        'M77 counterpart: %d; M77 texts with no ICIT counterpart: %d.' % (
            len(match), exact, len(match) - exact, len(rows) - len(used_i), len(texts) - len(match)))
    blk = defaultdict(Counter)
    for tn, (i, _) in match.items():
        blk[int(tn) // 100][rows[i]['site']] += 1
    site_of = {}
    for b, c in blk.items():
        s, k = c.most_common(1)[0]
        if k >= 8 and k / sum(c.values()) >= 0.8:
            site_of[b] = s
    ranges = defaultdict(list)
    for b in sorted(site_of):
        ranges[site_of[b]].append(b)
    say('- site blocks (text numbers, x100) with a clear site: %s.' % '; '.join(
        '%s %s' % (s, ','.join(str(b) for b in bs)) for s, bs in sorted(ranges.items(), key=lambda x: x[1][0])))
    add = []
    for tn in sorted(texts, key=int):
        if tn in match:
            continue
        lines = texts[tn]
        site = site_of.get(int(tn) // 100, 'unknown')
        rd = ' 0 '.join(' '.join(ln) for ln in lines)
        add.append({'sealid': 'M77-' + tn, 'cisi': '', 'site': site, 'type': 'M77', 'complete': 'Y',
                    'direction': 'M77', 'signs_visual': rd, 'signs_reading': rd, 'motif': ''})
    with open(os.path.join(HERE, 'data', 'corpus_m77_added.tsv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['sealid', 'cisi', 'site', 'type', 'complete', 'direction', 'signs_visual',
                                          'signs_reading', 'motif'], delimiter='\t')
        w.writeheader()
        w.writerows(add)
    toks = sum(len(a['signs_reading'].split()) for a in add)
    unks = sum(a['signs_reading'].split().count('?') for a in add)
    say('- added: %d texts, %d sign tokens (%d unmapped "?"); by site: %s.' % (
        len(add), toks, unks, ', '.join('%s %d' % kv for kv in Counter(a['site'] for a in add).most_common(10))))
    say('- merged corpus: %d objects (ICIT-derived %d + M77 additions %d).' % (len(rows) + len(add), len(rows), len(add)))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'merge_m77.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
