#!/usr/bin/env python3
"""Count R4936's cipher words by the #728 categories, from the committed files only.

    python3 tools/R4936_count728.py            # counts (run from targets/transylvania1645/)
    python3 tools/R4936_count728.py --align OTHER.tsv   # same counts on another alignment (e.g. main's)
    python3 tools/R4936_count728.py --decode   # mechanical decode of R4936-transcription-b15.txt, frozen family key

Words: the 338 rows of R4936_align.tsv plus the [...] runs of R4936_reading.md (unread figures, one word each)
= 341 cipher words.
  sure        row 'carried', class_resolved empty: every letter on its figure's own value.
  {probable}  row carried with a tag in class_resolved (a letter on the other member of a look-alike pair, or
              'g=u:hook': a figure labelled g, value u, written with the hook of the hand's t), or a [?word]
              (status '... (marked)').
  [restored]  status FLAG without (marked): e[s].
  <unresolved> the [...] runs.
Two views of the 24 Nov 2026 shape check (sign_check/R4936-places.tsv):
  human only  : a word with a g->q relabel made by the AI pass counts {probable} (Daniel's decision, 24 Nov 2026).
  AI included : the AI relabels count like the human ones.
"""
import csv, os, re, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEY = 'a-v b-f c-p d-o e-y g-u h-r i-n k-l m-z q-t s-x'


def rows_tsv(path):
    with open(path, newline='') as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


def decode(text):
    tab = {}
    for pair in KEY.split():
        a, b = pair.split('-')
        tab[a], tab[b] = b, a
    tab['7'] = 'm'
    out, depth = [], 0
    for ch in text:
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
        out.append(ch if depth or ch in '{} _' else tab.get(ch, '?'))
    return ''.join(out)


def main():
    if '--decode' in sys.argv:
        print('# Mechanical decode of R4936-transcription-b15.txt with the frozen family key (%s; 7 = m),' % KEY)
        print('# made by tools/R4936_count728.py --decode. Clear text in braces as there; _ = blot. Not a reading.')
        for line in open(os.path.join(HERE, 'R4936-transcription-b15.txt')):
            line = line.rstrip('\n')
            if line.startswith('# PAGE'):
                print(line)
            elif line and not line.startswith('#'):
                print(decode(line))
        return

    apath = sys.argv[sys.argv.index('--align') + 1] if '--align' in sys.argv else os.path.join(HERE, 'R4936_align.tsv')
    align = rows_tsv(apath)
    places = rows_tsv(os.path.join(HERE, 'sign_check', 'R4936-places.tsv'))
    reading = open(os.path.join(HERE, 'R4936_reading.md')).read().split('## Reading', 1)[1]
    runs = reading.count('[...]')

    # map (line, rank of the figure in the line, '-' skipped) -> align row
    where, per = {}, defaultdict(int)
    for i, r in enumerate(align):
        L = int(r['line'])
        for ch in r['figures']:
            if ch == '-':
                continue
            where[(L, per[L])] = i
            per[L] += 1
    ai_rows = Counter()
    for p in places:
        if p['by'] == 'AI' and p['label_before'] != p['label_after']:  # the 94 AI g->q relabels
            i = where[(int(p['line']), int(p['s']))]
            figs = [ch for ch in align[i]['figures'] if ch != '-']
            assert align[i]['word'] == p['word'] and figs[int(p['pos_in_word'])] in (p['label_before'], p['label_after']), p
            ai_rows[i] += 1

    def category(i, r, human_only):
        st = r['status']
        if st != 'carried':
            return '{probable}' if '(marked)' in st else '[restored]'
        if r['class_resolved'].strip():
            return '{probable}'
        if human_only and ai_rows[i]:
            return '{probable}'
        return 'sure'

    total = len(align) + runs
    print('R4936: %d rows in R4936_align.tsv + %d [...] runs in R4936_reading.md = %d cipher words' % (len(align), runs, total))
    print('AI-relabelled places: %d, in %d words' % (sum(ai_rows.values()), len(ai_rows)))
    tags = Counter(t for r in align for t in r['class_resolved'].split())
    print('tags in class_resolved: %s' % ', '.join('%s %d' % kv for kv in sorted(tags.items())))
    for name, human_only in (('human only (AI places probable)', True), ('AI included', False)):
        c = Counter(category(i, r, human_only) for i, r in enumerate(align))
        c['<unresolved>'] = runs
        print('%-32s sure %d  {probable} %d  [restored] %d  <unresolved> %d  -> sure share %d/%d = %.3f' % (
            name, c['sure'], c['{probable}'], c['[restored]'], c['<unresolved>'], c['sure'], total, c['sure'] / total))


if __name__ == '__main__':
    main()
