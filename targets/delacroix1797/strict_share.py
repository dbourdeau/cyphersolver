#!/usr/bin/env python3
"""Strict read share for delacroix1797 (integration of PR #884, 24 Nov 2026; owner's decision of 23 Nov 2026).

The contributor's reading (beling2026/readings/reading_1797-07-13.md) counts a word as read when the partial table
gives the draft's letters for its groups: 27 of 444 words carry a mark, share 0.939. But 148 numbers of the table
(class B and B2) rest on a single use in this one letter. Here each cipher word is put in one of three classes:

  hole      at least one letter marked by beling2026/scripts/make_reading.py (proposal place, class C value, or the
            group's table value differs from the draft's letters)
  probable  no mark, but at least one letter comes from a group of class B or B2 (a single-use value)
  sure      every letter comes from a class A group (two or more uses that agree)

The word division and the marking rule are those of make_reading.py, so the hole count must come out the same (27 of
444). Stdlib only, local files only.

usage: python strict_share.py [beling2026]
"""
import csv, pathlib, re, sys, unicodedata
from collections import Counter


def base(c):
    d = unicodedata.normalize('NFD', c.lower())
    d = ''.join(x for x in d if unicodedata.category(x) != 'Mn')
    return d if len(d) == 1 and 'a' <= d <= 'z' else ''


B = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parent / 'beling2026'
text = ' '.join(l.strip() for l in open(B / 'transcriptions/clear_draft_test_text.txt', encoding='utf-8')
                if l.strip() and not l.startswith('#'))
letters = [(i, base(c)) for i, c in enumerate(text) if base(c)]
key, cls = {}, {}
for r in csv.DictReader(open(B / 'key/code_table_F_partial.tsv', encoding='utf-8'), delimiter='\t'):
    vals = {''.join(base(c) for c in r['value'])}
    for a in (r.get('all_values') or '').split(';'):
        a = re.sub(r'\s*x\d+\s*$', '', a.strip())
        if a:
            vals.add(''.join(base(c) for c in a))
    key[int(r['group'])] = vals
    cls[int(r['group'])] = r['class']
PROP = {int(r['token_index']) for r in csv.DictReader(
    (l for l in open(B / 'proposals/transcription_corrections.tsv', encoding='utf-8') if not l.startswith('#')),
    delimiter='\t')}

state = [None] * len(text)      # per character: 'omit', 'hole', or the class of its group (A, B, B2)
tokens, causes = Counter(), Counter()
pos = n = 0
for line in open(B / 'key/alignment_by_group.txt', encoding='utf-8'):
    if line.startswith('#') or not line.strip():
        continue
    for t in line.split():
        if t.startswith('~'):               # a draft word with no group in the copy: not a cipher word
            for k in range(len(t) - 1):
                state[letters[pos + k][0]] = 'omit'
            pos += len(t) - 1
            continue
        g, v = t.split('=', 1)
        g = int(g)
        n += 1
        tokens[cls.get(g)] += 1
        lets = '' if v in ('0', '.', '?') else v.split('!')[0]
        span = letters[pos:pos + len(lets)]
        assert ''.join(b for _, b in span) == lets, (t, pos)
        if lets:
            if n - 1 in PROP:
                why = 'proposal place'
            elif cls.get(g) == 'C':
                why = 'class C value'
            elif lets not in key.get(g, set()):
                why = 'table value differs from the draft'
            else:
                why = None
            if why:
                causes[why] += 1
            for i, _ in span:
                state[i] = 'hole' if why else cls[g]
        pos += len(lets)
assert pos == len(letters)

shown = ''.join(' ' if state[i] == 'omit' else c for i, c in enumerate(text))
words = Counter()
for m in re.finditer(r"[\w'’]+", shown):
    st = {state[i] for i in range(m.start(), m.end()) if state[i]}
    words['hole' if 'hole' in st else 'sure' if st == {'A'} else 'probable'] += 1
total = sum(words.values())
print(f'groups {n}; tokens by class: ' + ', '.join(f'{k} {v}' for k, v in sorted(tokens.items())))
print(f'marked groups {sum(causes.values())}: ' + ', '.join(f'{v} {k}' for k, v in causes.most_common()))
print(f'cipher words {total}: sure {words["sure"]}, probable (a single-use value) {words["probable"]}, holes {words["hole"]}')
print(f'share with probable words counted as read: {1 - words["hole"] / total:.3f}')
print(f'strict share (sure words only): {words["sure"] / total:.3f}')
