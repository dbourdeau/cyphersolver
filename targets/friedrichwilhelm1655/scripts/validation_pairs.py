#!/usr/bin/env python3
"""Write validation.tsv (one cipher token per line: number TAB reading) from the six transcriptions and key.tsv.
Written at integration (12 Nov 2026); standard library only.   python scripts/validation_pairs.py
A number with a diaeresis (N:) or a bar (N^) is its own token. 51 (no value) is written as '?'. Slips of the writer are
read as the key gives them (the key value, not the intended letter)."""
import re, pathlib, sys, unicodedata
sys.stdout.reconfigure(encoding='utf-8')
R = pathlib.Path(__file__).resolve().parent.parent
key = {l.split('\t')[0]: l.split('\t')[1] for l in (R / 'key.tsv').read_text(encoding='utf-8').splitlines()[1:]}
out = ['# model: de-1640s', '# source: transcription_{c793,ps797,ps717,l819,w787,w813}.txt with key.tsv (scripts/validation_pairs.py)',
       '# note: every number is a token; N: = diaeresis, N^ = doubled letter; 51 has no value and is left out']
for d in ['c793', 'ps797', 'ps717', 'l819', 'w787', 'w813']:
    for l in (R / f'transcription_{d}.txt').read_text(encoding='utf-8').splitlines():
        if l.startswith('#') or '\t' not in l: continue
        t = re.sub(r'"[^"]*"|\[[^\]]*\]', ' ', l.split('\t', 1)[1])
        for u in re.findall(r'\d+[:^]?\??', t):
            m = re.fullmatch(r'(\d+)([:^]?)\??', u); n, mk = m.groups()
            c = key.get(n)
            if c is None: out.append(f'{n}\t?'); continue
            if mk == ':': c = unicodedata.normalize('NFC', c + '̈')
            if mk == '^': c = c + c
            out.append(f'{n}{mk}\t{c}')
(R / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(len(out) - 3, 'tokens')
