"""Step 1 of PLAN.md: compare transcriptions A and B with the fixed notation bridge; write reconciled.txt."""
import re, difflib
def load(fn):
    out = {}
    for ln in open(fn, encoding='utf-8'):
        m = re.match(r'(P[12]L\d\d):\s*(.*)$', ln.rstrip('\n'))
        if not m: continue
        s = re.sub(r'\[\[.*?\]\]', ' ', m.group(2))
        toks = [t for t in s.split() if t not in ('|', '<', '>', ',', '.', '/', '·')]
        toks = [t.strip('<>') for t in toks if t.strip('<>')]
        out[m.group(1)] = toks
    return out
def bridge(toks, who):
    s = ' '.join(toks)
    if who == 'A':
        s = re.sub(r'\bu T t\b', 'W1', s); s = re.sub(r'\bu T P\b', 'W2', s); s = re.sub(r'\bu T 6\b', 'u y 6', s)
        s = re.sub(r'\bh\b', 'H', s)
    else:
        s = re.sub(r'\bu S T\b', 'W1', s); s = re.sub(r'\bu S P\b', 'W2', s)
    toks = s.split()
    if who == 'B':  # B's lone t (the H-like sign) = A's h; B's t after a letter stays t
        toks = ['H' if t == 't' and (i == 0 or toks[i-1] in ('|',)) else t for i, t in enumerate(toks)]
    return toks
A, B = load('transcription_A.txt'), load('transcription_B.txt')
match = total = same_lines = 0; rec = []
for lab in sorted(set(A) | set(B), key=lambda x: (x[:2], int(x[3:]))):
    a, b = bridge(A.get(lab, []), 'A'), bridge(B.get(lab, []), 'B')
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False); r = []; m = t = 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal': r += a[i1:i2]; m += i2 - i1; t += i2 - i1
        else: n = max(i2 - i1, j2 - j1); r += ['?'] * n; t += n
    match += m; total += t; same_lines += (a == b)
    rec.append(f'{lab}: ' + ' '.join(r)); print(f'{lab} {m}/{t}')
open('reconciled.txt', 'w', encoding='utf-8').write('\n'.join(rec) + '\n')
print(f'OVERALL {match}/{total} = {match/total:.3f}; identical lines {same_lines}/{len(rec)}')
