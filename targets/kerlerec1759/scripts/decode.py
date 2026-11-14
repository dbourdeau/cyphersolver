"""Decode a code transcription with a key. Usage: python3 -I decode.py <key.tsv> <transcription> [--src]
Prints per line: the groups decoded, '[n]' for a code absent from the key, and flags stacked pairs whose upper
and lower numbers do not decode to the same thing."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kcommon import parse

key, src = {}, {}
for l in open(sys.argv[1], encoding='utf-8'):
    if l.startswith('#') or not l.strip():
        continue
    f = l.rstrip('\n').split('\t')
    key[int(f[0])] = f[1]
    src[int(f[0])] = f[2] if len(f) > 2 else 'M'
tot = res = 0
for p in parse(sys.argv[2]):
    print('==', p['page'], p['folio'])
    for L in p['lines']:
        out = []
        for g in L['codes']:
            if g['kind'] != 'code':
                out.append('[' + g['raw'] + ']')
                continue
            tot += 1
            v = key.get(g['code'])
            if v is None:
                out.append('[%d]' % g['code'])
            else:
                res += 1
                s = v
                if g['top'] is not None and key.get(g['top']) != v:
                    s += '{top %d=%s}' % (g['top'], key.get(g['top']))
                out.append(s)
        print('L%d: %s' % (L['n'], '.'.join(out)))
print('groups %d resolved %d (%.1f%%)' % (tot, res, 100 * res / max(tot, 1)))
