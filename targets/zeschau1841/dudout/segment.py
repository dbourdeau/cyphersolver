# segment.py - variable-length segmentation of R5005 (zeschau1841), rule proposed by Fable 5.2 (Anthropic), 11 Nov 2026.
# Usage: python3 segment.py ../ct_R5005.txt > R5005_groups.txt
# Reads Daniel Bourdeau's transcription unchanged. Blocks are read as one stream each (lines joined in label order);
# a4 and a5 are joined (a group runs from a4 into a5). Groups that start on a line are listed on it; '>' marks a group
# that runs on into the next line; '*' marks a group outside the forms below.
import re, sys, collections
RX = r'(?:55|77)..|[2579]..|00..|..|.'   # 00xx/55xx/77xx = 4 digits, 2/5/7/9 = 3 digits, everything else = 2
def canon(g):
    if len(g) == 3: return g[0] in '2579' and g[2] in '13468'
    if len(g) == 4: return g[:2] == '00' or (g[:2] in ('55', '77') and g[3] in '13468')
    if len(g) == 2: return g[0] in '01' or (g[0] in '3468' and g[1] in '13468')
    return False
JOIN = [['a1'], ['a2'], ['a3'], ['a4', 'a5'], ['a6'], ['a7'], ['a8']]
L = collections.OrderedDict()
for line in open(sys.argv[1], encoding='utf-8'):
    if line.strip() and not line.startswith('#'):
        k, v = line.split()[:2]; L[k] = v
tot = bad = 0
for grp in JOIN:
    kl = [(k, v) for k, v in L.items() if k[:2] in grp]
    s = ''.join(v for _, v in kl); ends = []; c = 0
    for k, v in kl: c += len(v); ends.append((c, k))
    pos = 0; li = 0; row = []
    for m in re.finditer(RX, s):
        g = m.group(0); st = pos; pos += len(g)
        while st >= ends[li][0]: li += 1
        tag = ('*' if not canon(g) else '') + g + ('>' if pos > ends[li][0] else '')
        row.append((ends[li][1], tag)); tot += 1; bad += not canon(g)
    for k, _ in kl:
        print(k, ' '.join(t for kk, t in row if kk == k))
print(f'# {tot} groups, {bad} outside the forms ({bad / tot:.1%})')
