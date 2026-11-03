"""Test whether the 1719 key (or simple shifts of it) reads the 1722 letters.
Prints the share of 1722 groups the 1719 key covers and a sample decryption per variant."""
import re, sys, collections
sys.stdout.reconfigure(encoding='utf-8')
import os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from decrypt import load_key, lines, norm

D = os.path.dirname(HERE)
key = load_key(os.path.join(D, 'key_frozen.tsv'))
toks = []
for lid, body in lines(os.path.join(D, 'work', 'pass_a_1722.txt')):
    body = re.sub(r'\{[^}]*\}', ' ', body)
    for t in body.split():
        n, u = norm(t)
        if n.isdigit():
            toks.append((lid, n, u))
print('groups', len(toks))
cov = sum(1 for _, n, u in toks if n in key or (n + '_') in key)
print('covered by 1719 key (any value):', cov, f'{cov/len(toks):.0%}')
letters = {k: v for k, v in key.items() if len(v) <= 2 and not k.endswith('_')}
cov2 = sum(1 for _, n, u in toks if n in letters)
print('covered by 1719 letter/syllable signs:', cov2, f'{cov2/len(toks):.0%}')
for name, f in [('as is', lambda n: n), ('mod 30', lambda n: str(int(n) % 30) if int(n) < 100 else n),
                ('-50', lambda n: str(int(n) - 50) if 50 < int(n) < 100 else n),
                ('-60', lambda n: str(int(n) - 60) if 60 < int(n) < 100 else n)]:
    s = []
    for lid, n, u in toks[:120]:
        m = f(n)
        s.append(letters.get(m, '.'))
    print(f'{name:7s}', ''.join(x if len(x) == 1 else f'({x})' for x in s))
