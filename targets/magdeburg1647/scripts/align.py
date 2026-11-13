"""align.py R2 R1 : word alignment of two frozen transcriptions of the same slip (difflib, no junk heuristic).
Same arithmetic as scripts/original/align_b162.py. Agreement = exact-equal aligned cipher words / words of R2."""
import sys, re, difflib
def W(f): return [re.sub('[^a-z]', '', w.lower()) for l in open(f) if not l.startswith('#') for w in l.replace('|', ' ').split() if re.sub('[^a-z]', '', w.lower())]
def align(f2, f1):
    a, b = W(f2), W(f1); sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    eq = sum(i2 - i1 for op, i1, i2, j1, j2 in sm.get_opcodes() if op == 'equal')
    return eq, len(a), len(b), sm
if __name__ == '__main__':
    tot = [0, 0]
    for s in sys.argv[1:]:
        f2, f1 = f'transcriptions/{s}_R2.txt', f'transcriptions/{s}_R1.txt'
        eq, na, nb, sm = align(f2, f1); tot[0] += eq; tot[1] += na
        print(f'{s}: R2 {na} words, R1 {nb} words; exact-equal aligned words {eq}; {eq}/{na} = {100*eq/na:.2f}% of R2; {eq}/{nb} = {100*eq/nb:.2f}% of R1')
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op != 'equal': print(f'   {op:8s} R2: {" ".join(W(f2)[i1:i2])}  |  R1: {" ".join(W(f1)[j1:j2])}')
    print(f'ALL: {tot[0]}/{tot[1]} = {100*tot[0]/tot[1]:.2f}% of R2 words (sum of the slips above; an agreement measure, not a reading figure)')
