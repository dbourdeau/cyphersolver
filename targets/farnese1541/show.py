"""Decode R91 with a key module's KEY and print code=out per manuscript line."""
import sys, importlib
from key1 import beam_decode, lm, lines
mod = importlib.import_module(sys.argv[1] if len(sys.argv) > 1 else 'k2cur')
m = lm.load('it-cinquecento', order=5, spaces=False)
L = list(lines())
d = ''.join(t[0] for _, _, toks, _ in L for t in toks)
s, path = beam_decode(d, mod.KEY, m, int(sys.argv[2]) if len(sys.argv) > 2 else 64)
print('score', round(s, 1))
pos = 0; ends = []
for p, n, toks, _ in L:
    pos += len(toks); ends.append((pos, f'{p}.{n}'))
i = 0; j = 0; row = []; plain = []
for code, out in path:
    row.append(f'{code}={out or "-"}'); plain.append(out)
    i += len(code)
    while j < len(ends) and i >= ends[j][0]:
        print(ends[j][1], ''.join(plain)); print('    ', ' '.join(row)); row = []; plain = []; j += 1
