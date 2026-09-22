"""ctx.py KEYFILE SIGN [SIGN...] [--set a=b,...] — show every occurrence of SIGN in the decrypt with 8 letters of context.
Also: ctx.py KEYFILE --full [--set ...] prints the whole decrypt with the key."""
import re, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
args = sys.argv[1:]
setv = {}
if '--set' in args:
    i = args.index('--set'); setv = dict(kv.split('=') for kv in args[i+1].split(',') if kv); del args[i:i+2]
keyf, signs = args[0], args[1:]
key = {}
for l in open(keyf, encoding='utf8'):
    p = l.split()
    if len(p) >= 2: key[p[0]] = p[1]
key.update(setv)
lines, page = [], ''
for l in open(os.path.join(HERE, 'transcription.txt'), encoding='utf8'):
    if l.startswith('=='): page = l.split()[1]; continue
    m = re.match(r'(\d\d)\s+(.*)', l.rstrip('\n'))
    if m:
        s = re.sub(r'\[[^\]]*\]', ' ', m.group(2)).replace(':', '').replace('?', '').replace('jo', 'J').replace('mg', 'M')
        lines.append((page + '.' + m.group(1), s))
def dec(c): return key.get(c, '?').replace('_', '')
if signs and signs[0] == '--full':
    for n, s in lines: print(n, ''.join(dec(c) if c != ' ' else ' | ' for c in s))
    sys.exit()
for sg in signs:
    print('==', sg, key.get(sg))
    for n, s in lines:
        for i, c in enumerate(s):
            if c == sg:
                L = ''.join(dec(x) for x in s[max(0, i-8):i] if x != ' ')
                R = ''.join(dec(x) for x in s[i+1:i+9] if x != ' ')
                print(f'  {n:7} {L:>14}[{dec(c)}]{R}')
