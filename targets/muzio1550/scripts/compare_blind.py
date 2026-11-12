"""Compare the blind second transcription of c. 3r with a first-reader transcription. Standard library only.

    python scripts/compare_blind.py <first-reader file> <blind file>

The blind reader used his own shape names and wrote the digit pairs as two digits; M maps his names to ours and EXP
splits our digit groups, so both run on the same units. Struck signs, dots and the stroke on L21 are left out.
"""
import sys, difflib
M = {'9': 'g', 'phi': 'F', 'np': 'P', 'uy': 'O', 'tH': '#', '+o': 'R', 'iy': 'I', 'I': '=', 'ud': 'u', 'xp': 'X', 'mp': 'S', 'r': 't',
     '-o-': 'E', 'o-': 'G', 'mt': 'T', '4_2': 'N42', '4_3': 'N43', '2_6': 'C26', 'e-': 'CE', 'venus': 'NN', '+..': 'PP', 'bd': 'FF',
     'psi': 'PSI', 'op': 'OP', 'V': 'v', 'sig': '6', '4o': 'C4o', 'DEL': '[x]'}
EXP = {'N39': ['3', 'g'], 'N38': ['3', '8'], 'N42': ['N42'], 'N43': ['N43'], 'C13': ['1', '3'], 'C26': ['2', '6'], 'C24': ['2', '4'], 'C25': ['2', '5']}
A = [l.split()[1:] for l in open(sys.argv[1], encoding='utf-8') if l.startswith('L')]
B = [l.split() for l in open(sys.argv[2], encoding='utf-8') if l.strip() and not l.startswith('#')]
tot = agree = nb = 0; dis = []
for i, (a, b) in enumerate(zip(A, B), 1):
    a = [x for t in a if t != '[x]' for x in EXP.get(t, [t])]
    b = [x for t in b if t not in ('.', '|', 'DEL') for x in EXP.get(M.get(t.rstrip('?'), t.rstrip('?')), [M.get(t.rstrip('?'), t.rstrip('?'))])]
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == 'equal': agree += i2 - i1
        else: dis.append(f'L{i:02d} {op:8s} first reader: {" ".join(a[i1:i2]) or "-":12s} blind: {" ".join(b[j1:j2]) or "-"}')
    tot += len(a); nb += len(b)
print(f'{sys.argv[1].split("/")[-1]}: first-reader units (digit pairs split, struck signs out) {tot}; blind units {nb}; agree {agree} = {100 * agree / tot:.2f}%; differ {tot - agree}')
for d in dis: print('  ' + d)
