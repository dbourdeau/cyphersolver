#!/usr/bin/env python3
"""Write docs/reveal/delacroix1797.json: the first five lines of the copy (66 groups, the lines shown in the page's
figure) with the value the partial table gives each group (24 Nov 2026).

Values are taken as in replay.py: the table's value for the number; where the table lists two values for a number,
the listed one that the hand alignment has at that place. Marks:
  ''     a value confirmed by two or more agreeing uses (class A)
  unc    a value that rests on one use in this letter (class B, B2), or a group whose table value differs from the
         draft's letters at this place (175 se for ses, 855 pre for pres)
  unk    an unsure value (class C), shown as ?
  null   the null 469
w marks the first group of each word of the draft, so that the tiles are spaced by words.

usage: python mk_reveal.py          (writes ../../docs/reveal/delacroix1797.json)
"""
import csv, json, pathlib, re, unicodedata

HERE = pathlib.Path(__file__).resolve().parent
B = HERE / 'beling2026'
N = 66


def base(c):
    d = unicodedata.normalize('NFD', c.lower())
    d = ''.join(x for x in d if unicodedata.category(x) != 'Mn')
    return d if len(d) == 1 and 'a' <= d <= 'z' else ''


def norm(s):
    return ''.join(base(c) for c in s)


text = ' '.join(l.strip() for l in open(B / 'transcriptions/clear_draft_test_text.txt', encoding='utf-8')
                if l.strip() and not l.startswith('#'))
letters = [i for i, c in enumerate(text) if base(c)]
starts = {m.start() for m in re.finditer(r"[\w'’]+", text)}          # first character of each word of the draft

main, allv, cls = {}, {}, {}
for r in csv.DictReader(open(B / 'key/code_table_F_partial.tsv', encoding='utf-8'), delimiter='\t'):
    g = int(r['group'])
    cls[g] = r['class']
    main[g] = r['value']
    allv[g] = {norm(r['value'])}
    for a in (r.get('all_values') or '').split(';'):
        a = re.sub(r'\s*x\d+\s*$', '', a.strip())
        if a:
            allv[g].add(norm(a))

tokens, pos, n = [], 0, 0
for line in open(B / 'key/alignment_by_group.txt', encoding='utf-8'):
    if line.startswith('#') or not line.strip():
        continue
    for t in line.split():
        if t.startswith('~'):
            pos += len(t) - 1
            continue
        g, v = t.split('=', 1)
        g = int(g)
        lets = '' if v in ('0', '.', '?') else v.split('!')[0]
        first = bool(lets) and letters[pos] in starts
        if main[g] == '(null)':
            tok = {'g': str(g), 'p': '', 'cls': 'null'}
        elif main[g] == '(full stop)':
            tok = {'g': str(g), 'p': '.', 'cls': ''}
        elif cls[g] == 'C' or main[g].startswith('('):
            tok = {'g': str(g), 'p': '?', 'cls': 'unk'}
        elif lets in allv[g]:
            tok = {'g': str(g), 'p': lets, 'cls': '' if cls[g] == 'A' else 'unc'}
        else:
            tok = {'g': str(g), 'p': norm(main[g]), 'cls': 'unc'}
        if first:
            tok['w'] = 1
        tokens.append(tok)
        pos += len(lets)
        n += 1
        if n == N:
            break
    if n == N:
        break

groups = [x for l in open(HERE / 'ciphertext.txt', encoding='utf-8')
          if l.strip() and not l.startswith('#') and not l.startswith('frame') for x in l.split()][:N]
assert [t['g'] for t in tokens] == groups
out = {
    'slug': 'delacroix1797',
    'anchor': 'copy',
    'title': 'The first five lines of the copy (frame 0244, right page)',
    'caption': 'Delacroix to Létombe, Paris, 25 Messidor an V, the first 66 of the 653 groups in Michael Brackx’s '
               'transcription (US National Archives, RG 59, M30 roll 4, frame 0244), with the values of the partial table.',
    'unit': 'code groups',
    'key_note': 'beling2026/key/code_table_F_partial.tsv, the table Andrew Beling built by laying the ministry’s clear '
                'draft on the groups. Where the table lists two values for a number (consul and consuls, on and ont), the '
                'listed one that the draft has at that place is shown. Marked doubtful: the values that rest on one use '
                'in this letter, and 175 and 855, where the table gives se and pre and the draft has ses and pres. 383 '
                'and 496 are unsure and shown as ?. 469 is a null.',
    'tokens': tokens,
}
dst = HERE.parent.parent / 'docs' / 'reveal' / 'delacroix1797.json'
dst.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8', newline='\n')
print(f'{len(tokens)} groups:', ' '.join((t['p'] or '_') + ('*' if t['cls'] == 'unc' else '') for t in tokens))
