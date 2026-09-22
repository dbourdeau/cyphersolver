"""Print a token file deciphered with a key file (lines 'SIGN=letter'); unknown signs as '?'."""
import sys
key = {}
for l in open(sys.argv[2], encoding='utf-8'):
    l = l.strip()
    if '=' in l and not l.startswith('//'):
        k, v = l.rsplit('=', 1); key[k.strip()] = v.strip()
align = '-a' in sys.argv
for l in open(sys.argv[1], encoding='utf-8'):
    if not l.startswith('L') or ':' not in l:
        continue
    lab, rest = l.split(':', 1)
    toks = rest.split()
    out = ''.join('' if key.get(t, '?') == '_' else ('|' if t == '_' else key.get(t, '?') if t != '?' else '*') for t in toks)
    print(lab, out)
    if align:
        print('    ', ' '.join(f'{t}:{key.get(t,"?")}' for t in toks))
