#!/usr/bin/env python3
"""Build the reading: the clear draft's words (transcriptions/clear_draft_test_text.txt) laid on the 653 groups by the
hand alignment (key/alignment_by_group.txt), with every letter that the key (key/code_table_F_partial.tsv) does NOT
give for Brackx's digits (any value the table records for the group, column all_values) put in square brackets. Draft words with no group at all are shown as <<not in the groups: ...>>.
usage: python make_reading.py ../transcriptions/clear_draft_test_text.txt ../key/alignment_by_group.txt ../key/code_table_F_partial.tsv"""
import csv, re, sys, unicodedata

def base(c):
    d = unicodedata.normalize('NFD', c.lower())
    d = ''.join(x for x in d if unicodedata.category(x) != 'Mn')
    return d if len(d) == 1 and 'a' <= d <= 'z' else ''

text = ' '.join(l.strip() for l in open(sys.argv[1], encoding='utf-8') if l.strip() and not l.startswith('#'))
letters = [(i, base(c)) for i, c in enumerate(text) if base(c)]
key, cls = {}, {}
for r in csv.DictReader(open(sys.argv[3], encoding='utf-8'), delimiter='\t'):
    vals = {''.join(base(c) for c in r['value'])}
    for a in (r.get('all_values') or '').split(';'):   # e.g. "les x2; le x1": every value the table records
        a = re.sub(r'\s*x\d+\s*$', '', a.strip())
        if a: vals.add(''.join(base(c) for c in a))
    key[int(r['group'])] = vals
    cls[int(r['group'])] = r['class']
mark = [False] * len(text)       # letters not given by the key
omit = [False] * len(text)       # letters of draft words with no group
pos = 0; n_groups = 0; n_marked_groups = 0
for line in open(sys.argv[2], encoding='utf-8'):
    if line.startswith('#') or not line.strip():
        continue
    for t in line.split():
        if t.startswith('~'):
            w = t[1:]
            for k in range(len(w)):
                omit[letters[pos + k][0]] = True
            assert ''.join(b for _, b in letters[pos:pos + len(w)]) == w, (t, pos)
            pos += len(w); continue
        g, v = t.split('=', 1)
        g = int(g); n_groups += 1
        lets = '' if v in ('0', '.', '?') else v.split('!')[0]
        span = letters[pos:pos + len(lets)]
        assert ''.join(b for _, b in span) == lets, (t, pos, ''.join(b for _, b in span))
        if lets and (lets not in key.get(g, set()) or cls.get(g) == 'C'):
            n_marked_groups += 1
            for i, _ in span: mark[i] = True
        pos += len(lets)
assert pos == len(letters), (pos, len(letters))
out = []; i = 0
while i < len(text):
    if omit[i]:
        j = i
        while j < len(text) and (omit[j] or (not base(text[j]) and j + 1 < len(text) and omit[j + 1])):
            j += 1
        out.append('<<not in the groups: ' + text[i:j] + '>>'); i = j; continue
    if mark[i]:
        j = i
        while j < len(text) and mark[j]: j += 1
        out.append('[' + text[i:j] + ']'); i = j; continue
    out.append(text[i]); i += 1
body = ''.join(out)
words = re.findall(r"[\w\[\]'’]+", re.sub(r'<<[^>]*>>', ' ', body))
holes = sum(1 for w in words if '[' in w)
print(body)
print(f'\n<!-- groups {n_groups}; groups whose letters the key does not give: {n_marked_groups}; words {len(words)}; words with a mark: {holes}; read share {1 - holes / len(words):.3f} -->')
