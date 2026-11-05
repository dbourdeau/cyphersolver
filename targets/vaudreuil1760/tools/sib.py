"""Decode a sibling transcription with the 1757 table: python tools/sib.py sibs/1390.txt"""
import sys, re
sys.path.insert(0, 'tools')
import decode
k = decode.load()
fol = ''
for l in open(sys.argv[1], encoding='utf8'):
    l = l.rstrip('\n')
    if l.startswith('#'): continue
    if l.startswith('@'): fol = l; print('\n' + fol); continue
    toks = re.findall(r'\[[^\]]*\]|\d+[?~^]*', l.replace('¶', '').replace('|', ''))
    print(' '.join(decode.val(k, t) for t in toks))
