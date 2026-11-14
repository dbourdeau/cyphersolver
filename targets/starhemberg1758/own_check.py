"""Own check (integration of issue #555, 14 Nov 2026), not the contributor's run_checks.py: (1) the 413 units of the
contributor's parse concatenate to the 1,726-digit stream of manuscript-lines.json; (2) each unit's value agrees with
the contributor's key tables (working-prima-v4.tsv = table A, working-secunda.tsv = table B). Standard library only.
    python3 own_check.py"""
import json, os, re
H = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'aaymeloglu')
def table(name):
    out = {}
    for line in open(os.path.join(H, name), encoding='utf8'):
        if line.strip() and not line.startswith('#'):
            k, v = line.rstrip('\n').split('\t')[:2]
            out[k] = v
    return out
A, B = table('working-prima-v4.tsv'), table('working-secunda.tsv')
doc = json.load(open(os.path.join(H, 'manuscript-tokens.json'), encoding='utf8'))
lines = json.load(open(os.path.join(H, 'manuscript-lines.json'), encoding='utf8'))
stream = ''.join(re.sub(r'\D', '', l['transcription']) for l in lines)
units = ''.join(t['code'] for t in doc['tokens'])
print('digits', len(stream), '| units', len(doc['tokens']), '| units cover the stream exactly:', units == stream)
ok, other = 0, []
for t in doc['tokens']:
    if t['kind'] not in ('ordinary', 'null'):
        continue
    v = (A if t['table'] == 'A' else B).get(t['code'])
    tv = t['value'].lower().replace('[null]', '').strip('?').strip()
    if v is not None:
        vv = v.lower().replace('∅', '').strip()
        if t['kind'] == 'null' or tv in vv or vv in tv or vv.split('/')[0][:3] == tv[:3]:
            ok += 1
            continue
    other.append((t['table'], t['code'], v, t['value'], t['grade']))
print('agree with the tables:', ok, '| differ or missing from the tsv:', len(other))
for o in other:
    print('  ', o)
