"""Decode 31R with the copied key; compare each value with the supplied reading."""
import csv
import json
from pathlib import Path
from decode import load_dict, parse, val

TARGET = Path(__file__).resolve().parents[1]
ROOT = TARGET.parents[1]
key = load_dict()
with (TARGET / 'readings/s031R.tsv').open() as stream:
    rows = list(csv.DictReader(stream, delimiter='\t'))
groups = [g for _, tokens in parse(TARGET / 'tokens/s031R.txt') for g in tokens]
assert len(groups) == len(rows) == 59
tokens = []
for group, row in zip(groups, rows):
    assert group == row['token']
    value, source = val(group, key)
    cls = 'unk' if source == 'missing' else ('unc' if value != row['value'] else ('code' if source == 'key' else ''))
    tokens.append(dict(g=group, p='?' if cls == 'unk' else value, cls=cls))
data = dict(slug='battier1686', anchor='december', title='19 December 1686: the cipher on 31R',
            caption='The 59 cipher tokens on scan 31R, in manuscript order; intervening clear text is omitted. Values come from the named key, with word spacing left editorial.',
            unit='tokens', key_note='NA 1.10.29 inv. 1209; block:number notation identifies the marked series. Literal values, not contextual replacements.', tokens=tokens)
(ROOT / 'docs/reveal/battier1686.json').write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n')
print(f'reveal: {len(tokens)} tokens; {sum(t["cls"] == "unc" for t in tokens)} differences flagged')
