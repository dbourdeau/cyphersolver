"""Recount attestation from sibling ALIGN/SEG data and supplied list-A corrections.
Writes evidence/attestation_25may.tsv and the site reveal. No image inspection.
"""
from pathlib import Path
from collections import defaultdict
import json
from measure import load_key, blocks, group_ok, clean, tgrade
from frscore import norm
ROOT = Path(__file__).resolve().parents[1]
KEY = load_key(ROOT / 'key.tsv')
support = defaultdict(list)
passage = ''
for line in (ROOT / 'transcription/11may1601.md').read_text().splitlines():
    if line.startswith('## '): passage = line[3:].split('|')[0].strip()
    if line.startswith('ALIGN:'):
        for pair in line[6:].split():
            if '=' not in pair: continue
            token, value = pair.split('=', 1)
            if '?' not in value: support[clean(token), norm(value)].append('11May:' + passage)
for block in blocks(ROOT / 'transcription/28may1601.md'):
    for group in block.get('seg', '').split('|'):
        if '=>' not in group: continue
        tokens, word = group.split('=>'); tokens = tokens.split()
        combo = group_ok(tokens, word, KEY)
        if combo:
            for token, value in zip(tokens, combo):
                support[clean(token), norm(value)].append('28May:' + block['id'])
# Supplied visual corrections accepted by codex_review/recount_listA.md.
for token, value, witness in [('qF', 'po', 'A10'), ('qF', 'po', 'A16'),
                              ('42', "la Royne d'Angleterre", 'A12')]:
    support[token, norm(value)].append('30Apr:list-' + witness)
rows = ['position\tpassage\ttoken\tvalue\tgrade\tattestations\twitnesses']
reveal, counts = [], []
for block in blocks(ROOT / 'transcription/25may1601.md'):
    flattened = []
    for group in block['seg'].split('|'):
        tokens, word = group.split('=>'); tokens = tokens.split(); flattened += tokens
        combo = group_ok(tokens, word, KEY)
        for token, value in zip(tokens, combo or ['?'] * len(tokens)):
            witnesses = support[clean(token), norm(value)]
            grade = tgrade(KEY, token, value) if combo else '-'
            counts.append(len(witnesses))
            rows.append('\t'.join(map(str, [len(counts), block['id'], token, value,
                         grade, len(witnesses), '; '.join(witnesses)])))
            cls = 'unk' if not witnesses else 'unc' if grade == 'M' else 'code' if token == '42' else ''
            reveal.append({'g': token, 'p': value if witnesses else '?', 'cls': cls})
    assert flattened == block['tok'], 'SEG/TOK ordering mismatch'
once, twice = sum(n >= 1 for n in counts), sum(n >= 2 for n in counts)
assert (len(counts), once, twice) == (61, 59, 58)
(ROOT / 'evidence/attestation_25may.tsv').write_text('\n'.join(rows) + '\n')
payload = dict(slug='aerssen1601', anchor='reading', title='The 25 May cipher passages',
    caption='Two consecutive cipher runs; intervening clear words omitted. Both name gaps remain visible.',
    unit='cipher tokens', key_note='Sibling glosses and list A; C known plaintext, M uncertain theta. Supplied qF/42 corrections accepted. Attestation is not proof of accuracy.', tokens=reveal)
(ROOT.parents[1] / 'docs/reveal/aerssen1601.json').write_text(json.dumps(payload, ensure_ascii=False, indent=1) + '\n')
print(f'25 May: {once}/61 = {once/61:.1%} attested; {twice}/61 = {twice/61:.1%} attested at least twice')
