"""The Mohenjo-daro copper tablets as pictorial bilinguals (rebus/copper_tablets.tsv, from
Parpola 1994 Fig. 7.14 matched to ICIT).

T1  Sign = image equations: two groups with the same inscription, one with an image on the
    reverse, the other with a sign (or short text) in its place.
T2  One image, several texts; one text, several images.
T3  Titles: sign sequences (2-3 signs) found in texts of two or more different image classes.
T4  Names: sign sequences found in two or more different texts, all with one image class.
T5  Prediction for T4 on the seals: does a seal carrying the 'name' also carry the animal?

Writes results/copper.md.
"""
import csv
import os
from collections import Counter, defaultdict
from math import comb

from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []

CLASS = [('markhor goat', 'goat'), ('horned archer', 'archer'), ('rhinoceros', 'rhinoceros'),
         ('elephant', 'elephant'), ('hare', 'hare'), ('endless knot', 'knot'),
         ('horned tiger', 'tiger'), ('tiger-striped', 'bull-tiger'), ('composite', 'composite'),
         ('long horns', 'bull (long-horned)'), ('heart-shaped spots', 'bull, spotted'),
         ('short-horned bull', 'bull (short-horned)')]
SEAL_MOTIF = {'goat': ('Goat',), 'rhinoceros': ('Rhin',), 'elephant': ('Elep',), 'hare': ('Hare',),
              'tiger': ('Tigr',), 'bull (short-horned)': ('Gaur', 'Bull3', 'Bull', 'Bult', 'Zebu', 'Buff'),
              'bull (long-horned)': ('Bull1',), 'archer': ('Anth',)}


def motif_is(m, codes):
    # prefix match only for codes with sub-types (Bull1:W, Goat:4); 'Bull' must not catch 'Bull1'
    return any(m == c or (c in ('Bull1', 'Goat') and m.startswith(c)) for c in codes)


def say(s=''):
    OUT.append(s)
    print(s)


def image_class(desc):
    if desc.startswith('markhor'):
        return 'goat'
    for k, v in CLASS:
        if k in desc:
            return v
    return None


def load_table():
    rows = []
    with open(os.path.join(HERE, 'rebus', 'copper_tablets.tsv'), encoding='utf-8') as f:
        for ln in f:
            if ln.startswith('#') or ln.startswith('group'):
                continue
            g, ex, text, src, rev, kind, link, objs = (ln.rstrip('\n').split('\t') + [''] * 8)[:8]
            rows.append(dict(group=g, ex=int(ex), text=text, src=src, rev=rev, kind=kind, link=link,
                             objs=objs, cls=image_class(rev) if kind == 'image' else None))
    return rows


def ngrams(text, ks=(2, 3)):
    out = set()
    for line in text.split(' / '):
        s = line.split()
        for k in ks:
            for i in range(len(s) - k + 1):
                out.add(' '.join(s[i:i + k]))
    return out


def main():
    rows = load_table()
    by = {r['group']: r for r in rows}
    say('# Copper tablets as pictorial bilinguals')
    say()
    say('%d prototype groups (Parpola 1994 Fig. 7.14), %d tablets; %d texts from ICIT, %d read from the '
        'drawing, %d not transcribed.' % (len(rows), sum(r['ex'] for r in rows),
                                          sum(r['src'] == 'icit' for r in rows),
                                          sum(r['src'] == 'drawing' for r in rows),
                                          sum(r['src'] == 'none' for r in rows)))
    say()
    say('## T1 Sign = image (linked groups with the same inscription)')
    say()
    say('| inscription (reading order) | image side | sign side | groups |')
    say('|---|---|---|---|')
    seen = set()
    for r in rows:
        if not r['link'] or r['link'] not in by:
            continue
        a, b = r, by[r['link']]
        key = tuple(sorted((a['group'], b['group'])))
        if key in seen:
            continue
        seen.add(key)
        img = a if a['kind'] == 'image' else b
        oth = b if img is a else a
        say('| %s | %s (%d) | %s: %s (%d) | %s / %s |' % (
            img['text'] or oth['text'], img['rev'], img['ex'], oth['kind'], oth['rev'], oth['ex'],
            img['group'], oth['group']))
    say()
    say('## T2 One image, several texts; one text, several images')
    say()
    img_texts = defaultdict(list)
    for r in rows:
        if r['cls'] and r['text']:
            img_texts[r['cls']].append((r['group'], r['text']))
    for c, ts in sorted(img_texts.items(), key=lambda x: -len(x[1])):
        if len({t for _, t in ts}) > 1:
            say('- **%s**: %s' % (c, '; '.join('%s %s' % gt for gt in ts)))
    text_imgs = defaultdict(set)
    for r in rows:
        for line in r['text'].split(' / '):
            if r['kind'] == 'image' and r['cls']:
                text_imgs[line].add((r['cls'], r['group']))
            elif r['kind'] in ('sign', 'text'):
                text_imgs[line].add(('%s %s' % (r['kind'], r['rev']), r['group']))
    for t, s in text_imgs.items():
        if len({c for c, _ in s}) > 1 and t:
            say('- text **%s** goes with: %s' % (t, ', '.join('%s (%s)' % cg for cg in sorted(s))))
    say()
    say('## T3 Titles: sequences shared by different images')
    say()
    ng_cls = defaultdict(set)
    ng_txt = defaultdict(set)
    for r in rows:
        if not r['text']:
            continue
        cls = r['cls'] or ('sign %s' % r['rev'])
        for g in ngrams(r['text']):
            ng_cls[g].add(cls)
            ng_txt[g].add(r['text'])
    titles = [(g, c) for g, c in ng_cls.items() if len({x for x in c if not x.startswith('sign')}) >= 2]
    for g, c in sorted(titles, key=lambda x: (-len(x[1]), x[0])):
        if any(g != h and g in h and ng_cls[h] == c for h, _ in titles):
            continue
        say('- **%s**: %s' % (g, ', '.join(sorted(c))))
    say()
    say('## T4 Names: sequences in two or more texts that all go with one image')
    say()
    names = []
    for g, c in ng_cls.items():
        imgs = {x for x in c if not x.startswith('sign')}
        if len(imgs) == 1 and len(ng_txt[g]) >= 2:
            names.append((g, next(iter(imgs)), sorted(ng_txt[g])))
    for g, c, ts in sorted(names, key=lambda x: x[1]):
        if any(g != h and g in h and c == c2 for h, c2, _ in names):
            continue
        say('- **%s** = %s: %s' % (g, c, '; '.join(ts)))
    say()
    say('## T5 The names on the seals')
    say()
    seals = [r for r in load() if r['flat'] and r['type'].startswith('SEAL') and r['motif']]
    N = len(seals)
    say('Seals with a motif: %d. For each name candidate, the seals whose text contains it and their '
        'motifs; p = hypergeometric chance of that many or more with the predicted motif.' % N)
    say()
    for g, c, _ in names:
        codes = SEAL_MOTIF.get(c)
        hits = [r for r in seals if (' ' + g + ' ') in (' ' + ' '.join(r['flat']) + ' ')]
        if not hits:
            say('- %s (%s): on no seal with a motif.' % (g, c))
            continue
        mc = Counter(r['motif'] for r in hits)
        if codes:
            K = sum(1 for r in seals if motif_is(r['motif'], codes))
            k = sum(1 for r in hits if motif_is(r['motif'], codes))
            n = len(hits)
            p = sum(comb(K, i) * comb(N - K, n - i) for i in range(k, min(K, n) + 1)) / comb(N, n)
            say('- %s (%s): %d seals, %d with the %s motif (%.1f expected), p = %.3f; motifs %s' % (
                g, c, n, k, '/'.join(codes), n * K / N, p, dict(mc)))
        else:
            say('- %s (%s): %d seals; motifs %s' % (g, c, len(hits), dict(mc)))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'copper.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
