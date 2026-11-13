"""Build key.tsv (all lines) and key_frozen.tsv (lines L01-L10 only) from align_44r.txt.
Each sign takes its most frequent value; other values are listed with counts. '_' = point (null)."""
import sys, os, collections
sys.path.insert(0, os.path.dirname(__file__))
from common import read_align, HERE

def build(lines, al):
    c = collections.defaultdict(collections.Counter)
    for lab in lines:
        for w in al[lab]:
            for tok, val in w:
                if val != '?':
                    c[tok][val] += 1
    return c

def write(c, path, note):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(f'# {note}\nsign\tvalue\tplaces\tall values\n')
        for tok in sorted(c, key=lambda t: (-sum(c[t].values()), t)):
            v, n = c[tok].most_common(1)[0]
            f.write(f"{tok}\t{v}\t{sum(c[tok].values())}\t{', '.join(f'{a} x{b}' for a, b in c[tok].most_common())}\n")

al = read_align()
labs = sorted(al)
write(build(labs, al), os.path.join(HERE, 'key.tsv'), 'Key of c. 44r from all 17 lines aligned with c. 42r (most frequent value first).')
write(build([l for l in labs if l <= 'L10'], al), os.path.join(HERE, 'key_frozen.tsv'),
      'FROZEN 12 Nov 2026: key from lines L01-L10 only; L11-L17 are held out (scripts/heldout.py).')
print('ok')
