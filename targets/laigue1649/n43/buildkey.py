"""Rebuild the no. 43 code from the interlinear glosses (pairs_c*.txt) and apply it to the unglossed opening."""
import glob, re, collections, json
K = collections.defaultdict(collections.Counter)
for f in sorted(glob.glob('pairs_c*.txt')):
    for line in open(f, encoding='utf-8'):
        line = re.sub(r'^L\d+:\s*', '', line.strip())
        for tok in line.split():
            if tok.startswith('#') or '=' not in tok: continue
            n, g = tok.split('=', 1)
            if n.endswith('_') and len(g) == 2: g = g[::-1]   # underline = reversed syllable
            n = n.rstrip('_')
            if n.isdigit() and g and g != '+' and '?' not in g: K[int(n)][g] += 1
key = {n: c.most_common() for n, c in sorted(K.items())}
with open('key43.txt', 'w', encoding='utf-8') as out:
    for n, c in key.items(): out.write(f"{n}\t{' '.join(f'{g}:{k}' for g, k in c)}\n")
print(len(key), 'numbers with glosses;', sum(sum(c.values()) for c in K.values()), 'glossed tokens')
amb = {n: c for n, c in key.items() if len(c) > 1}
print(len(amb), 'with >1 reading')
res = []
for line in open('opening_c245.txt', encoding='utf-8'):
    if line.startswith('#'): continue
    lab, body = line.split(':', 1)
    body = re.sub(r'\^\[([^\]]*)\]', r'\1', body)
    out = []
    for tok in body.split():
        if tok.startswith('#'): out.append(' ' + tok[1:].upper() + ' '); continue
        n = int(re.sub(r'\D', '', tok) or 0)
        out.append(key[n][0][0] if n in key else f'[{n}]')
    res.append(f"{lab}: " + '·'.join(out))
open('opening_decoded.txt', 'w', encoding='utf-8').write('\n'.join(res) + '\n'); print('\n'.join(res))
