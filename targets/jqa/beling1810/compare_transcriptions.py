"""Compare two transcriptions of the same coded run, number by number.

python compare_transcriptions.py FIRST SECOND

Both files: any text; the numbers are taken in order from lines that hold code (lines starting with '#', '==' or a
header word are skipped; line labels like 'A01:' or '01' are dropped). An alternative [a/b] counts as its first
reading for the sequence and as agreeing when either reading equals the other transcription's number. Marks and '?'
are ignored. The two sequences are aligned with difflib; agreement = numbers equal at aligned places / the longer
sequence. Prints the counts and every disagreement. Python standard library only.
"""
import re, sys, difflib

def nums(path):
    seq = []
    for line in open(path, encoding='utf8'):
        s = line.strip()
        if not s or s.startswith(('#', '==', '@', '=')):
            continue
        if re.match(r'^[A-Za-z]', s) and not re.match(r'^([A-G]\d\d|L\d+):', s):
            continue
        s = re.sub(r'^([A-G]\d\d|L\d+|\d{1,2})[:\s]', ' ', s)  # line label (a code run never starts a line with a 1-2 digit group here)
        s = re.sub(r'\{[^}]*\}|\([^)]*\)', ' ', s)
        s = re.sub(r'(\d+)\[alt(\d+)\]', r'[\1/\2]', s)
        for t in s.split():
            m = re.fullmatch(r'\[?(\d+)(?:/(\d+))?\]?[^\d]*', t.replace('.', ''))
            if m:
                seq.append((m.group(1), m.group(2)))
    return seq

def main():
    a, b = nums(sys.argv[1]), nums(sys.argv[2])
    sm = difflib.SequenceMatcher(None, [x[0] for x in a], [x[0] for x in b], autojunk=False)
    eq = 0; diffs = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            eq += i2 - i1
        elif op == 'replace' and i2 - i1 == j2 - j1:
            for x, y in zip(a[i1:i2], b[j1:j2]):
                if set(filter(None, x)) & set(filter(None, y)):
                    eq += 1
                else:
                    diffs.append(f"{'/'.join(filter(None, x))} | {'/'.join(filter(None, y))}")
        else:
            diffs.append(f"{op}: {' '.join(x[0] for x in a[i1:i2])} | {' '.join(y[0] for y in b[j1:j2])}")
    n = max(len(a), len(b))
    print(f'first {len(a)} numbers, second {len(b)}; agreeing at aligned places {eq} = {eq / n:.3f} of the longer')
    for d in diffs:
        print('  ', d)

if __name__ == '__main__':
    main()
