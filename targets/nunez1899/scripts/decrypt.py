"""Mechanical decryption of 9926: transcription + key.tsv -> decryption_9926.txt.
Code words become their key value (in UPPER CASE for display); clear words pass through in lower case."""
import sys
from common import HERE, read_lines, read_key, decrypt_tokens
key = read_key(HERE / 'key.tsv')
lines = read_lines(HERE / 'transcription_9926.txt')
out = ['# Mechanical decryption of CEHM CDLIV.1a.1883.38.9926 (scripts/decrypt.py from transcription_9926.txt + key.tsv).',
       '# UPPER CASE = value of a code word from key.tsv; lower case = clear word as telegraphed; [...] = code word with no value.']
for lab, toks in lines:
    words = []
    for code, val in decrypt_tokens(toks, key):
        words.append(code if val is None else ('[...]' if val == '[...]' else val.upper()))
    out.append(lab + ' ' + ' '.join(words))
open(HERE / 'decryption_9926.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('\n'.join(out))
