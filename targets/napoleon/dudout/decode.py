"""Decodes transcription.txt with the Great Cipher of 1812 entries in key_entries.tsv: one output line per cipher line,
each group followed by the first value of its table entry (python decode.py > decryption.txt)."""
import os
H = os.path.dirname(os.path.abspath(__file__))
SPECIAL = {'un point': '.', 'point et virgule': ';', 'alinéa': '¶'}
tab = {}
for l in open(os.path.join(H, 'key_entries.tsv'), encoding='utf-8'):
    if l.startswith('#') or l.startswith('group\t'): continue
    g, e = l.rstrip('\n').split('\t'); tab[g] = e
n = 0
for l in open(os.path.join(H, 'transcription.txt'), encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    n += 1
    vals = [(g, tab.get(g, '??')) for g in l.split()]
    print('%02d  %s' % (n, ' '.join('%s=%s' % (g, SPECIAL.get(v, v.split(',')[0])) for g, v in vals)))
