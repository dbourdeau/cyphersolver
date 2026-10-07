"""Extract cipher units and build the opening reveal from the recorded tables."""
import csv
import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
TOKEN = re.compile(r'~[^~]*~|\{[^}]*\}(?:\^\w+)?|\d+:-?(?:\^\w+)?|[a-zA-Z]\d+(?:\^\w+)?')


def load(name):
    return {p[0]: p[1:] for line in (BASE / 'key' / name).read_text().splitlines()
            if line.strip() and not line.startswith('#') for p in [line.split('\t')]}


def main():
    letters, words, codes = [load('key_' + name + '.tsv') for name in ('letters', 'words', 'codes')]
    for row in csv.DictReader((BASE / 'key/corrections.tsv').open(), delimiter='\t'):
        (words if row['code'].endswith(':') else codes)[row['code'].rstrip(':')] = [row['reading'], row['legacy_band']]
    tokens, reveal = [], []
    for line in (BASE / 'transcription/june1676_tx.txt').read_text().splitlines():
        if not line or line.startswith('#'):
            continue
        lid, rest = line.split(' ', 1)
        for token in TOKEN.findall(rest):
            if token.startswith('~'):
                if '131R.03' <= lid <= '131R.24':
                    reveal.append(dict(g='', p=token[1:-1], cls='plain'))
                continue
            tokens.append(token)
            core, _, suffix = token.partition('^')
            if core.startswith('{'):
                vals = [letters.get(n, ['?', '?']) for n in core[1:-1].split(',')]
                value = ''.join(v[0] for v in vals) + suffix
                uncertain = any(v[1] != 'H' for v in vals)
                cls = 'unc' if uncertain else ''
            else:
                table = words if ':' in core else codes
                key = core.rstrip(':-') if ':' in core else core
                value, band, *_ = table.get(key, ['?', '?'])
                value += ('-' if core.endswith('-') else '') + (('+' + suffix) if suffix else '')
                cls = 'unk' if band == '?' else ('unc' if band in ('I', 'M', 'C') or key == 'm161' else 'code')
            if '131R.03' <= lid <= '131R.24':
                reveal.append(dict(g=token, p=value, cls=cls))
    assert len(tokens) == 278, len(tokens)
    (BASE / 'transcription/june1676_tokens.txt').write_text('\n'.join(tokens) + '\n')
    data = dict(slug='beuningen1676', anchor='reading', title='The plan and the informer',
                caption='Scan 131R, lines 3–24. Values from the rebuilt tables and corrections; doubtful readings remain marked.',
                unit='cipher token', key_note='Braced letter sequences count once. Clear words are shown between the cipher runs. The sum, s439 and the mede clause remain unresolved.',
                tokens=reveal)
    (BASE.parents[1] / 'docs/reveal/beuningen1676.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print('cipher tokens:', len(tokens), '; reveal cipher tokens:', sum(bool(t['g']) for t in reveal))


if __name__ == '__main__':
    main()
