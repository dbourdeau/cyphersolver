"""Write validation.tsv for docs/_validate.py: each cipher group of the 1758 letter with its attested code B value.

Groups whose value is inferred (key/code_B_table.tsv, status "inferred") and the one group the two readings of the
figures do not agree on (34|35) are written as '?' (unread), so the test sees only values the printed letters show.
Values are written as the groups give them (vos, lin, der, ra), not as emended in the reading.
Standard library only:  python make_validation.py
"""
import csv, pathlib, re, unicodedata

HERE = pathlib.Path(__file__).resolve().parent


def letters(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if c.isalpha() and not unicodedata.combining(c))


with open(HERE / 'key' / 'code_B_table.tsv', encoding='utf-8') as f:
    tab = {r['group']: r for r in csv.DictReader([l for l in f if not l.startswith('#')], delimiter='\t')}
out = ['# model: fr-1750-nospace', '# source: transcriptions/figures_reconciled.txt with key/code_B_table.tsv (make_validation.py)',
       '# note: inferred values and the unsettled group 34|35 are left unread (?)']
for line in open(HERE / 'transcriptions' / 'figures_reconciled.txt', encoding='utf-8'):
    m = re.match(r'(P\dL\d):\s*(.*)', line.strip())
    if not m:
        continue
    for g in m.group(2).split():
        r = tab.get(g.replace('+', '*'))
        val = '?' if ('|' in g or r is None or r['status'] == 'inferred') else letters(r['value'])
        out.append(f'{g}\t{val}')
(HERE / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(f'validation.tsv: {len(out) - 3} tokens, {sum(1 for l in out[3:] if l.endswith(chr(9) + "?"))} unread')
