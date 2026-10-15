"""Compare two transcriptions of the same letter group by group (underlines and editorial notes ignored,
fractions normalised, uncertain digits '?' kept). Prints the aligned differences.

usage: python scripts/compare_tx.py <ours.txt> <other.txt>
e.g.   python scripts/compare_tx.py R1957_tx.txt ../ct.txt
       python scripts/compare_tx.py ../../r1955/R1955_tx.txt ../../r1955/transcription_r1955.txt"""
import re, sys, difflib


def groups(path):
    out = []
    for line in open(path, encoding='utf8'):
        if line.startswith('#') or line.startswith('||'):
            continue
        line = re.sub(r'"[^"]*"', ' ', line)
        line = re.sub(r'\{[^}]*\}', '', line)
        line = line.replace('½', '+1/2')
        for t in line.split():
            t = t.strip(',.')
            if t.startswith('[del:'):
                continue
            t = re.sub(r'[_=#!~]', '', t)
            if re.match(r'^[0-9?]+(\+1/2)?\??$', t):
                out.append(t)
    return out


a, b = groups(sys.argv[1]), groups(sys.argv[2])
print(f'{sys.argv[1]}: {len(a)} groups; {sys.argv[2]}: {len(b)} groups')
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
same = sum(bl.size for bl in sm.get_matching_blocks())
print('identical groups in sequence:', same)
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op != 'equal':
        print(f'{op:8s} ours[{i1}:{i2}] {" ".join(a[i1:i2]) or "-":30s} other[{j1}:{j2}] {" ".join(b[j1:j2]) or "-"}')
diff, eight0, other = 0, 0, 0
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == 'replace' and i2 - i1 == j2 - j1:
        for x, y in zip(a[i1:i2], b[j1:j2]):
            diff += 1
            if len(x) == len(y) and all(p == q or {p, q} == {'8', '0'} for p, q in zip(x, y)):
                eight0 += 1
print(f'same-length substitutions: {diff} groups, of which {eight0} differ only by 8 against 0; '
      f'other edits: {sum(1 for o in sm.get_opcodes() if o[0] != "equal" and not (o[0] == "replace" and o[2] - o[1] == o[4] - o[3]))}')
