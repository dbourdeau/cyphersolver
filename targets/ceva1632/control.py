"""Check the reading of R75 against the decipherment written on the leaf in 1632.

The transcriber of DOC_R75_D2532 copied, above each cipher line, as much of the
contemporary interlinear decipherment as was legible, in <PLAINTEXT ...> lines.
Those lines are an independent witness: they were not used to build the key, the
model or the decoder.  Agreement is measured on letters, ignoring word division,
because neither the clerk nor the decoder marks it reliably.
"""
import sys, os, re, difflib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE))
from lang import lm

def witness(path):
    """The contemporary decipherment, line by line, in cipher-line order."""
    out, pend = [], []
    for line in open(path, encoding='utf-8', errors='replace'):
        s = line.strip()
        m = re.match(r'<PLAINTEXT[:]?(?:\s+IT)?\s*(.*?)>?\s*$', s)
        if s.startswith('<PLAINTEXT') and m:
            t = m.group(1)
            t = re.sub(r'<ABBR[^>]*>?', ' ', t)
            t = re.sub(r'<IL>|<[^>]*>', ' ', t)
            pend.append(t)
        elif s and not s.startswith('#') and not s.startswith('<'):
            out.append(' '.join(pend)); pend = []
    return out

def key(t):
    t = t.replace('?', '').replace('*', '')
    return lm.norm(t, 'early').replace(' ', '')

def main():
    wit = witness(os.path.join(HERE, 'decode', 'DOC_R75_D2532_2532.txt'))
    mine = open(os.path.join(HERE, sys.argv[1] if len(sys.argv) > 1 else 'r75.read.txt'), encoding='utf-8').read().split('\n')
    n = min(len(wit), len(mine))
    tot = agree = 0
    for i in range(n):
        w, g = key(wit[i]), key(mine[i])
        if len(w) < 12:          # too little of the interlinear was legible
            continue
        r = difflib.SequenceMatcher(None, w, g, autojunk=False)
        m = sum(b.size for b in r.get_matching_blocks())
        tot += len(w); agree += m
        print('line %2d  %3d chars  %.2f' % (i + 1, len(w), m / len(w)))
        print('   leaf: %s' % w[:90])
        print('   here: %s' % g[:90])
    print('\ncontrolled lines: letters %d, matched %d, agreement %.3f' % (tot, agree, agree / tot))

main()
