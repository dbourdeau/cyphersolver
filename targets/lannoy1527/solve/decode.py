"""Decode the transcription line by line with a key file, for reading by hand.

  python solve/decode.py [KEYFILE] [LEAF ...]

KEYFILE (default key.tsv): one 'token<TAB>value' per line; a sign gets a letter (or a pair), a code group a word.
'#' starts a comment. Unknown signs print as {sign}, unknown groups as [group]; clear text prints in braces.
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); TR = os.path.join(HERE, '..', 'transcription')
args = sys.argv[1:]
kf = args.pop(0) if args and not re.match(r'^00\d\d[rv]$', args[0]) else os.path.join(HERE, '..', 'key.tsv')
leaves = args or ['0009r', '0009v', '0010r', '0010v', '0011r']
key = {}
for l in open(kf, encoding='utf-8'):
    l = l.split('#')[0].rstrip('\n')
    if '\t' in l:
        k, v = l.split('\t')[:2]; key[k.strip()] = v.strip()
for leaf in leaves:
    p = os.path.join(TR, leaf + '.txt')
    if not os.path.exists(p): continue
    print(f'== {leaf}')
    for line in open(p, encoding='utf-8'):
        m = re.match(r'^(L\d+):\s*(.*)$', line.strip())
        if not m: continue
        out = []
        for s in re.findall(r'\{[^}]*\}|[^\s{}]+', m.group(2)):
            if s.startswith('{'): out.append(' ' + s + ' '); continue
            t = s.rstrip('?') if s != '??' else s
            v = key.get(t)
            g = len(t) == 3 and t.isalpha() and t.islower()
            if v is None: out.append(f' [{t}] ' if g else '{' + t + '}')
            else: out.append(f' {v.upper()} ' if g else v)
        print(f'{m.group(1)}: ' + re.sub(' +', ' ', ''.join(out)).strip())
