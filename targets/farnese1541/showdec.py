"""Print the R91 decode under a key module, per manuscript line, 11 shown as '|', words split by the unigram segmenter."""
import sys, importlib
import vpoly
from wordcov91 import segment
from parse_r91 import lines
M = vpoly.Model(B=64, lbonus=1.3, nullpen=4)
key = {k: list(v) for k, v in importlib.import_module(sys.argv[1]).KEY.items()}
s, out = M.text(key, B=64)
print('score', round(s, 1))
L = list(lines()); ends = []; pos = 0
for p, n, toks, _ in L:
    pos += len(toks); ends.append((pos, f'{p}.{n}'))
i = 0; j = 0; buf = []; codes = []
for code, o in out:
    buf.append('|' if code == '11' else o); codes.append(f'{code}={o or "-"}')
    i += len(code)
    while j < len(ends) and i >= ends[j][0]:
        parts = ''.join(buf).split('|')
        print(ends[j][1], ' | '.join(' '.join(segment(p)) for p in parts))
        if '-c' in sys.argv: print('     ', ' '.join(codes))
        buf = []; codes = []; j += 1
