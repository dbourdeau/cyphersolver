"""Mechanical decryption for target 1447.   python scripts/decrypt.py <transcription.txt> [key.tsv]

Transcription lines `R<n> g g g ...` (two-digit groups). Each group becomes its key letter; a group not in the key
prints as [nn]. Output: label<TAB>letters.
"""
import sys
from keylib import ROOT, load_key

sys.stdout.reconfigure(encoding='utf-8', newline='\n')
src = sys.argv[1]
key = load_key(sys.argv[2] if len(sys.argv) > 2 else ROOT / 'key_frozen.tsv')
for line in open(src, encoding='utf-8'):
    if not line.startswith('R'):
        continue
    lab, *gs = line.split()
    print(lab + '\t' + ''.join(key.get(g, f'[{g}]') for g in gs))
