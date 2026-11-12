"""Mechanical decryption of the key source DLI.3.524.1.   python scripts/decrypt_524.py > decryption_524.txt

Every row of transcription_524.txt (rows tagged '!' included, so that they can be checked) is decrypted with
key_frozen.tsv. A group not in the key prints as [nn]; a group cut by the scan ('??', '8?') prints as [?].
Output: seg<TAB>words of the contemporary translation<TAB>our decryption. This is a check of the key against
the contemporary translation, not a reading of our own.
"""
import sys
from keylib import ROOT, load_key

sys.stdout.reconfigure(encoding='utf-8', newline='\n')
key = load_key(ROOT / 'key_frozen.tsv')
print('# DLI.3.524.1: decryption with key_frozen.tsv, row by row against the contemporary translation (page 2).')
print('# seg\ttranslation\tdecryption')
for line in (ROOT / 'transcription_524.txt').read_text(encoding='utf-8').splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    f = line.split('\t')
    out = []
    for g in f[2].split():
        if g == '|':
            out.append(' | ')
        elif '?' in g:
            out.append('[?]')
        else:
            out.append(key.get(g, f'[{g}]'))
    print(f[0] + '\t' + f[1] + '\t' + ''.join(out))
