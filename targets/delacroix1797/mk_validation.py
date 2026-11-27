#!/usr/bin/env python3
"""Write validation.tsv for docs/_validate.py: one line per group of ciphertext.txt, <group> TAB <reading> (24 Nov 2026).

The reading of a group is the draft's letters at that place in the contributor's hand alignment
(beling2026/key/alignment_by_group.txt). Left out as unread ('?'): the 29 groups the reading marks (a class C value, a
place where a digit change is proposed, a table value that differs from the draft's letters) and the two unknown signs.
Read as nothing ('-'): the full stops (412, 413, 416, 417) and the null 469.

Note what the test can and cannot say here: the key was made by laying this French text on these groups, so the
reading is real French by construction. The test only asks whether a key of the same shape, fitted to the shuffled
groups, reads as well.

usage: python mk_validation.py        (writes validation.tsv beside this file)
"""
import csv, pathlib, re, unicodedata

HERE = pathlib.Path(__file__).resolve().parent
B = HERE / 'beling2026'


def norm(s):
    d = unicodedata.normalize('NFD', s.lower())
    return re.sub(r'[^a-z]', '', ''.join(c for c in d if unicodedata.category(c) != 'Mn'))


allv, cls, special = {}, {}, {}
for r in csv.DictReader(open(B / 'key/code_table_F_partial.tsv', encoding='utf-8'), delimiter='\t'):
    g = int(r['group'])
    cls[g] = r['class']
    if r['value'].startswith('('):
        special[g] = '-' if ('full stop' in r['value'] or 'null' in r['value']) else '?'
        continue
    allv[g] = {norm(r['value'])}
    for a in (r.get('all_values') or '').split(';'):
        a = re.sub(r'\s*x\d+\s*$', '', a.strip())
        if a:
            allv[g].add(norm(a))
prop = {int(r['token_index']) for r in csv.DictReader(
    (l for l in open(B / 'proposals/transcription_corrections.tsv', encoding='utf-8') if not l.startswith('#')),
    delimiter='\t')}

rows, n = [], 0
for line in open(B / 'key/alignment_by_group.txt', encoding='utf-8'):
    if line.startswith('#') or not line.strip():
        continue
    for t in line.split():
        if t.startswith('~'):
            continue
        g, v = t.split('=', 1)
        g = int(g)
        lets = '' if v in ('0', '.', '?') else v.split('!')[0]
        if g in special:
            val = special[g]
        elif cls.get(g) == 'C' or n in prop or lets not in allv.get(g, set()):
            val = '?'
        else:
            val = lets
        rows.append((g, val))
        n += 1
groups = [int(x) for l in open(HERE / 'ciphertext.txt', encoding='utf-8')
          if l.strip() and not l.startswith('#') and not l.startswith('frame') for x in l.split()]
for l in open(HERE / 'ciphertext_corrections.tsv', encoding='utf-8'):   # a person's look, plate 2511 (25 Nov 2026)
    f = l.rstrip('\n').split('\t')
    if l.startswith('#') or f[0] == 'token_index':
        continue
    assert groups[int(f[0])] == int(f[4]), f
    groups[int(f[0])] = int(f[5])
assert [g for g, _ in rows] == groups, 'the alignment does not follow ciphertext.txt'
out = ['# model: fr-modern',
       '# source: ciphertext.txt + beling2026/key/alignment_by_group.txt (mk_validation.py)',
       '# note: the 29 marked groups and the two unknown signs are left out; full stops and the null read as nothing']
out += [f'{g}\t{v}' for g, v in rows]
(HERE / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8', newline='\n')
print(f'{len(rows)} groups: {sum(v == "?" for _, v in rows)} left out, {sum(v == "-" for _, v in rows)} read as nothing')
