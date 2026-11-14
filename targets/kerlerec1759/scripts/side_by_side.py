"""Merged decode beside the manuscript-only decode, line by line.
Usage: python3 -I side_by_side.py <key_used_1759.tsv> <reconciled transcription>
Each group prints as value (clerk's pairs) or {value} (value from Pusch 2008 only) or [n] (no value)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kcommon import parse
key = {}
for l in open(sys.argv[1], encoding='utf-8'):
    if l.startswith('#') or l.startswith('code') or not l.strip(): continue
    c, v, s, _ = l.rstrip('\n').split('\t'); key[int(c)] = (v, s)
nm = np_ = nn = 0
for p in parse(sys.argv[2]):
    print('==', p['page'], p['folio'])
    for L in p['lines']:
        a, b = [], []
        for g in L['codes']:
            if g['kind'] != 'code':
                a.append('[' + g['raw'] + ']'); b.append('[' + g['raw'] + ']'); continue
            v, s = key.get(g['code'], ('', 'none'))
            if s == 'M': a.append(v); b.append(v); nm += 1
            elif s == 'P': a.append('{%s}' % v); b.append('_' * max(1, len(v))); np_ += 1
            else: a.append('[%d]' % g['code']); b.append('[%d]' % g['code']); nn += 1
        print('L%-3d merged    : %s' % (L['n'], ' '.join(a)))
        print('     glosses   : %s' % ' '.join(b))
t = nm + np_ + nn
print('groups %d: clerk-attested %d (%.1f%%), Pusch-only %d (%.1f%%), no value %d' % (t, nm, 100*nm/t, np_, 100*np_/t, nn))
