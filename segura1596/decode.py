"""Decode the saved transcription; emit auditable grades, counts and site reveal."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
key = json.loads((ROOT / 'key.json').read_text(encoding='utf-8'))
lines = [line.split() for line in (ROOT / 'cipher_tokens.txt').read_text().splitlines() if line.strip()]
uncertain = {'Hd', 'rd', 'openC', 'Q', 'X', 'ud'}
expected = ['apon', 'tecreocierto', 'conformanelyes', 'cudero',
            'dizenqueelmundoseacabara', 'omoriraelreyporsetiem',
            'breelbiencercadellopa', 'rescequeandacreoendios']
decoded = [''.join(key[t] for t in line) for line in lines]
assert decoded == expected, (decoded, expected)
rows = [(i, j, t, key[t] or '[null]', 'M' if t in uncertain else 'I')
        for i, line in enumerate(lines, 1) for j, t in enumerate(line, 1)]
with (ROOT / 'token_reading.tsv').open('w', encoding='utf-8', newline='') as f:
    w = csv.writer(f, delimiter='\t')
    w.writerow(['line', 'position', 'token', 'plaintext', 'grade'])
    w.writerows(rows)
total = len(rows)
m = sum(row[-1] == 'M' for row in rows)
stats = dict(tokens=total, distinct=len({r[2] for r in rows}), proposed=total,
             conservative=total-m, fraction_conservative=(total-m)/total,
             grades={'I': total-m, 'M': m}, null_tokens=sum(not key[r[2]] for r in rows))
(ROOT / 'coverage.json').write_text(json.dumps(stats, indent=2)+'\n', encoding='utf-8')
reveal = dict(slug='segura1596', anchor='comet', title='The comet passage, sign by sign',
              caption='Modern sign identifiers; original spacing is not preserved. Proposed readings, with uncertain assignments marked.',
              unit='sign', key_note='Key reconstructed from this text; X=m and ud=ll remain context-dependent.',
              tokens=[dict(g=t, p=key[t], cls='unc' if t in uncertain else '') for line in lines[4:] for t in line])
out = ROOT.parent / 'docs' / 'reveal' / 'segura1596.json'
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(reveal, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print('\n'.join(decoded))
print(json.dumps(stats))
