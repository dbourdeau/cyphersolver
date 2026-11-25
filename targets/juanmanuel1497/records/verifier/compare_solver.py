"""Compare my reconciled transcription (and each helper) with the solver's final transcription, whole-text alignment.
usage: compare_solver.py mine.txt solver.txt A.txt B.txt"""
import sys, re, difflib
def load(p, order):
    d = {}
    for l in open(p, encoding='utf8'):
        m = re.match(r'(L\d[ab]?):\s*(.*)', l)
        if m and m.group(1) not in d:
            d[m.group(1)] = [re.sub(r'\?\(.*', '?', t) for t in re.sub(r'\?\([^)]*\)', '?', m.group(2)).split() if t not in ('/', '.', 'CLEAR')]
    out = []
    for L in order:
        out += [(L, t) for t in d.get(L, [])]
    return out
# solver puts L8b at the end of L7 and the line-8 start after it; compare in the solver's order
mine = load(sys.argv[1], ['L1','L2','L3','L4','L5','L6','L7','L8b','L8a'])
sol = load(sys.argv[2], ['L1','L2','L3','L4','L5','L6','L7','L8'])
a = [t for _, t in mine]; b = [t for _, t in sol]
sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
eq = diff = onlym = onlys = 0; rows = []
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == 'equal': eq += i2-i1; continue
    n = max(i2-i1, j2-j1)
    for k in range(n):
        x = a[i1+k] if i1+k < i2 else '-'; y = b[j1+k] if j1+k < j2 else '-'
        if x == '-': onlys += 1
        elif y == '-': onlym += 1
        else: diff += 1
        ctx = ' '.join(b[max(0, j1-3):j1]) + ' [' + ' '.join(b[j1:j2]) + '] ' + ' '.join(b[j2:j2+3])
        line = mine[i1+k][0] if i1+k < i2 else (sol[j1+k][0] if j1+k < j2 else '?')
        rows.append(f"{line}\tmine={x}\tsolver={y}\tsolver-index={j1+k}\tcontext(solver): {ctx}")
print(f"equal {eq}; different {diff}; only mine {onlym}; only solver {onlys}; mine {len(a)} solver {len(b)}")
print('\n'.join(rows))
