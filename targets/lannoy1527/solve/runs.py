"""Print each cipher run of tokens.txt decoded with key.tsv as one stream (markers 11, g#, -o- shown as |), for writing the reading."""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
key = {}
for l in open(os.path.join(HERE, '..', 'key.tsv'), encoding='utf-8'):
    if l.startswith('# ') or l.startswith('#S'): continue
    if '\t' in l: k, v = l.rstrip('\n').split('\t')[:2]; key[k] = v
isg = lambda t: len(t) == 3 and t.isalpha() and t.islower()
cur = None
for l in open(os.path.join(HERE, 'tokens.txt'), encoding='utf-8'):
    if l.startswith('#00'): cur = l[1:].strip(); continue
    out = []
    for t in l.split():
        v = key.get(t)
        if t in ('11', '-o-'): out.append('|')
        elif isg(t): out.append(f' {v.upper()} ' if v else f' [{t}] ')
        else: out.append(v if v else '{' + t + '}')
    print(f'#{cur}\n' + re.sub(' +', ' ', ''.join(out)).strip() + '\n')
