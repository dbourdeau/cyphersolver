"""Correct one token inside a word identified by its current decode, wherever the word
straddles line breaks. Entries: (current decode, 0-based index in the word, new token)."""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..'))
from solve import parse, is_code
from decode import dec

FIX = [
 ('einmaquartiern', 3, '58'), ('einmaquartiern', 4, '54'),   # einzuquartiern (checked on image 3)
]
path = os.path.join(HERE, 'transcription.txt')
txt = open(path, encoding='utf8').read().split('\n')

def words_with_pos():
    """Re-derive words with the (line index, token index) of each token."""
    out = []; carry = []
    for i, ln in enumerate(txt):
        if ln[:1] != 'P': continue
        toks = ln.split(' ')
        rest = ' '.join(toks[1:])
        inbr = False
        for j, t in enumerate(toks[1:], start=1):
            if t.startswith('['): inbr = True
            if inbr:
                if t.endswith(']'): inbr = False
                continue
            if t in ('z', 'c'):
                if carry: out.append(carry); carry = []
            elif t == '-': pass
            else: carry.append((i, j, t))
        if not rest.rstrip().endswith('-') and carry:
            out.append(carry); carry = []
    if carry: out.append(carry)
    return out

W = words_with_pos()
n = 0
for target, idx, new in FIX:
    for w in W:
        if dec([t for _, _, t in w]) == target and idx < len(w):
            i, j, old = w[idx]
            toks = txt[i].split(' '); toks[j] = new; txt[i] = ' '.join(toks)
            w[idx] = (i, j, new); n += 1
            break
    else:
        print('not found:', target)
open(path, 'w', encoding='utf8').write('\n'.join(txt))
print(n, 'of', len(FIX), 'applied')
