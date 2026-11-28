#!/usr/bin/env python3
"""Decode a transcription of Nassau-Saarbruecken II Nr. 4683 with key.tsv.
Usage: python3 decode.py A transcription_293.txt   (system A, numeric homophonic, table mod 24)
       python3 decode.py H transcription_290.txt   (system H, The Hague letter)
Clear words {..} are copied in lower case, numbers decoded in upper case, unknown values as [n], illegible ?? as [?]."""
import re, sys, os
sysname, path = sys.argv[1], sys.argv[2]
here = os.path.dirname(os.path.abspath(__file__))
table, codes, H = {}, {}, {}
for line in open(os.path.join(here, 'key.tsv'), encoding='utf-8'):
    c = line.rstrip('\n').split('\t')
    if c[0] == 'A' and c[1].startswith('n mod 24'):
        table[int(c[1].split('=')[1])] = c[2]
    elif c[0] == 'A':
        codes[int(c[1])] = c[2]
    elif c[0] == 'H':
        H[int(c[1])] = c[2]
def val(n):
    if sysname == 'A':
        if n >= 200: return '<' + codes.get(n, '[%d]' % n) + '>'
        return table[n % 24].upper() if n >= 40 else '[%d]' % n
    v = H.get(n)
    return v.upper() if v and len(v) <= 3 else ('<%s>' % v if v else '[%d]' % n)
for line in open(path, encoding='utf-8'):
    m = re.match(r'(\S+ L\d+|\S+ ENTETE) \| (.*)', line.strip())
    if not m: continue
    out = []
    for t in re.findall(r'\{[^}]*\}|\?\?|\d+\??|<[^>]*>', m.group(2)):
        if t.startswith('{'): out.append(t[1:-1])
        elif t.startswith('<'): continue
        elif t == '??': out.append('[?]')
        else: out.append(val(int(t.rstrip('?'))))
    print(m.group(1), '|', ' '.join(out))
