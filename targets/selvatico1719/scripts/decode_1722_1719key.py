"""The frozen 1719 key applied as it stands to the 1722 and undated letters (work/pass_a_1722.txt), line by line.
Not a reading: the 1719 key is another table (scripts/test_1722.py). Written for the full-texts list, 14 Nov 2026.
A group the key gives a letter or syllable prints that value; any other group prints '.'; clear words stay in braces.
usage: python scripts/decode_1722_1719key.py > decryption_1722_1719key.txt"""
import re, sys, os
sys.stdout.reconfigure(encoding='utf-8', newline='\n')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from decrypt import load_key, lines, norm
D = os.path.dirname(HERE)
key = load_key(os.path.join(D, 'key_frozen.tsv'))
letters = {k: v for k, v in key.items() if len(v) <= 2 and not k.endswith('_')}
print('# The frozen 1719 key (key_frozen.tsv, letter and syllable signs) applied unchanged to work/pass_a_1722.txt: the letters of')
print('# 10 Jun, 29 Jul, 8 Aug and 12 Aug 1722 (cc. 21-22, 25-26, 35-36, 23-24), "2 gennaio" (c. 2r) and "10 dicembre" (c. 14r).')
print('# NOT a reading: these letters are in another table, and this decode shows that the 1719 key gives no words on them.')
print('# . = group with no letter value in the 1719 key; {..} = clear words of the letter. They are read in part, with the')
print('# Riva table, in targets/riva1722. scripts/decode_1722_1719key.py, 14 Nov 2026.')
n = c = 0
for lid, body in lines(os.path.join(D, 'work', 'pass_a_1722.txt')):
    out = []
    for part in re.split(r'(\{[^}]*\})', body):
        if part.startswith('{'):
            out.append(' ' + part + ' '); continue
        s = ''
        for t in part.split():
            g, u = norm(t)
            if g.isdigit():
                n += 1; v = letters.get(g); c += v is not None
                s += v if v is not None else '.'
        out.append(s)
    print(lid, ''.join(out).strip())
print(f'# groups {n}; with a letter value in the 1719 key {c} ({c/n:.0%})')
