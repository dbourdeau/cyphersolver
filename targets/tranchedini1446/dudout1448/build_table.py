"""Build the 1448 table from texts/f28_signs.txt: majority of settled values per label ('?' does not vote; ties -> no value).
Run: python3 build_table.py  -> table_1448.json"""
import json, re, collections, os
here = os.path.dirname(os.path.abspath(__file__))
votes = collections.defaultdict(collections.Counter)
for ln in open(os.path.join(here, 'texts/f28_signs.txt'), encoding='utf8'):
    if not re.match(r'R\d+ ', ln): continue
    for tok in ln.split(':', 1)[1].split():
        lab, val = tok.split('=')
        if val != '?': votes[lab][val] += 1
        else: votes[lab]  # seen
table, notes = {}, {}
for lab, c in sorted(votes.items()):
    if not c: notes[lab] = 'seen, no settled value'; continue
    (v1, n1), *rest = c.most_common()
    if rest and rest[0][1] == n1: notes[lab] = 'tie: ' + ', '.join(f'{v}x{n}' for v, n in c.most_common()); continue
    table[lab] = v1
    if rest: notes[lab] = 'votes: ' + ', '.join(f'{v}x{n}' for v, n in c.most_common())
json.dump({'table': table, 'notes': notes}, open(os.path.join(here, 'table_1448.json'), 'w'), ensure_ascii=False, indent=1, sort_keys=True)
print(len(table), 'labels valued;', len(notes), 'notes')
for k, v in notes.items(): print(' ', k, v)
