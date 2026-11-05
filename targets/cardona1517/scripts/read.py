"""Read the Cardona cipher with the hand-edited working key (key/key.tsv).

  python3 scripts/read.py text [BLOCKS]   decode lines (default ABCD)
  python3 scripts/read.py ctx GROUP ...   every context of the given code groups (5 tokens each side)

Output: sign letters in lower case, code groups in UPPER CASE; a probable or doubtful value carries a trailing '?';
signs and code groups with no value print as [sign] and {group}; a null (value 0) prints nothing. Frame marks
(ratio, ¶) are dropped.
"""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from load import lines, is_code
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALIAS = {'gto': 'gto', 'oo': 'oo', 'ff': 'ff', 'll': 'll', 'ef': 'ef'}
KEY, STATUS = {}, {}
for l in open(os.path.join(ROOT, 'key', 'key.tsv'), encoding='utf-8'):
    if l.startswith('#') or l.startswith('kind\t') or not l.strip(): continue
    kind, tok, val, st = l.rstrip('\n').split('\t')[:4]
    KEY[tok], STATUS[tok] = (None if val == '-' else val), st
CODE_LIKE = lambda t: is_code(t) or (len(t) == 2 and t.isalpha() and t.islower() and t not in ALIAS)

def show(t):
    v = KEY.get(t)
    if v == '0': return ' '          # null
    if CODE_LIKE(t):
        if not v: return f' {{{t}}} '
        return f' {v.upper()}{"?" if STATUS.get(t) in ("doubtful", "probable") else ""} '
    if v is None: return f'[{t}]'
    return v + ('?' if STATUS.get(t) in ('doubtful', 'probable') else '')

FRAME = {'D', 'P#', '=', 'S°', 'ratio', '¶'}   # marks that open and close a cipher piece
PIECES = [('A01', 'A22'), ('B01', 'B03'), ('B04', 'B11'), ('C01', 'C28'), ('D01', 'D12'), ('D13', 'D19')]

def strip_frame(tag, ts):
    ts = list(ts)
    if any(tag == a for a, _ in PIECES):
        while ts and ts[0] in FRAME: ts.pop(0)
    if any(tag == b for _, b in PIECES):
        while ts and ts[-1] in FRAME: ts.pop()
    return [t for t in ts if t not in ('ratio', '¶')]

def text(blocks):
    for b in blocks:
        for tag, ts in lines(b):
            s = ''.join(show(t) for t in strip_frame(tag, ts))
            print(tag, re.sub(' +', ' ', s).strip())

def ctx(groups):
    seq = [(tag, t) for b in 'ABCD' for tag, ts in lines(b) for t in ts if t not in ('ratio', '¶')]
    for g in groups:
        print(f'== {g} = {KEY.get(g, "?")} ({STATUS.get(g, "-")})')
        for i, (tag, t) in enumerate(seq):
            if t != g: continue
            left = ''.join(show(x) for _, x in seq[max(0, i - 6):i]); right = ''.join(show(x) for _, x in seq[i + 1:i + 7])
            print(f'  {tag}: ' + re.sub(' +', ' ', f'{left} <{g}> {right}').strip())

if __name__ == '__main__':
    if sys.argv[1] == 'text': text(sys.argv[2] if len(sys.argv) > 2 else 'ABCD')
    else: ctx(sys.argv[2:])
