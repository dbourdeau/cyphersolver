"""Print each segment as number/letter pairs under a key (json value->letter), with the key's homophone lists."""
import json, sys, collections
key = json.load(open(sys.argv[1], encoding='utf-8'))
for l in open('ct_neal.txt'):
    if l.startswith('S'):
        p = l.split()
        print(p[0], ' '.join(f'{t}={key.get(t, "?")}' if len(t) < 3 else f'[{t}]' for t in p[1:]))
        print('   ', ''.join(key.get(t, '?') if len(t) < 3 else f' [{t}] ' for t in p[1:]))
inv = collections.defaultdict(list)
for v, c in key.items(): inv[c].append(int(v))
print({c: sorted(v) for c, v in sorted(inv.items())})
