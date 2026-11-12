# compare_blind.py: the blind second transcription (b103) against the first (b101), f.307v and f.309v.
# Standard library only. python3 -I scripts/compare_blind.py  -> controls/compare_blind.txt
# Parsers as in scripts/original/b103_compare.py. Numerals "read in full" = tokens without a gutter mark ('~' or '?').
# Agreement is counted on the full numerals aligned by difflib after the cut tokens are removed from both sides.
import os, re, difflib
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(HERE, *a)

def blind(p):
    out = []
    for l in open(p, encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        n, rest = l.split(' ', 1)
        rest = re.sub(r'\[[^\]]*\]', ' ', rest)
        for t in re.split(r'[.\s]+', rest):
            if t: out.append((int(n), t.replace('?', '~')))
    return out

def first(p):
    out = []
    for l in open(p, encoding='utf-8'):
        m = re.match(r'R(\d+):(.*)', l)
        if not m: continue
        rest = re.sub(r'"[^"]*"', ' ', m.group(2))
        for t in rest.split(): out.append((int(m.group(1)), t))
    return out

res = []; TA = TB = TE = 0
for page in ('f307v_323L', 'f309v_325L'):
    a = [x for x in blind(P('second_transcription', 'blind_' + page + '.txt')) if '~' not in x[1]]
    b = [x for x in first(P('transcriptions', page + '.txt')) if '~' not in x[1]]
    A = [t for _, t in a]; B = [t for _, t in b]
    sm = difflib.SequenceMatcher(None, A, B, autojunk=False)
    eq = 0; diffs = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal': eq += i2 - i1
        else: diffs.append('  %s blind %s first %s' % (op, a[i1:i2], b[j1:j2]))
    res.append('%s: full numerals blind %d, first %d; identical aligned %d' % (page, len(A), len(B), eq))
    res += diffs
    TA += len(A); TB += len(B); TE += eq
res.append('both: blind %d, first %d; identical %d; %d/%d = %.2f%% of the first transcription\'s full numerals' % (TA, TB, TE, TE, TB, 100.0 * TE / TB))
os.makedirs(P('controls'), exist_ok=True)
open(P('controls', 'compare_blind.txt'), 'w', encoding='utf-8').write('\n'.join(res) + '\n')
print('\n'.join(res))
