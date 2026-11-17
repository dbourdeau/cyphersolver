"""Compare pass-1 crib transcriptions (transcriptions/<frame>.txt) with second passes (pass2/<frame>.p2, digits only,
same line labels). Prints per frame: groups compared, agreements, and each difference. Usage: python3 -I compare_passes.py"""
import re, glob, os, difflib
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
def lines1(f):
    d = {}
    for line in open(f):
        m = re.match(r'([LR]\d+\w*):\s*(.*)', line.strip())
        if not m: continue
        body = re.sub(r'\[(?:cut|struck|1791|Struck)[^\]]*\]', ' ', m.group(2))
        d[m.group(1)] = [t.split('=')[0].replace('?', '') for t in body.split() if re.match(r'^\d', t.split('=')[0])]
    return d
tot = agree = 0
for p2 in sorted(glob.glob(B + '/pass2/*.p2')):
    fr = os.path.basename(p2)[:-3]
    d1 = lines1(B + f'/transcriptions/{fr}.txt')
    d2 = {}
    for line in open(p2):
        m = re.match(r'([LR]\d+\w*):\s*(.*)', line.strip())
        if m: d2[m.group(1)] = m.group(2).split()
    key = lambda k: (k[0], int(re.sub(r'\D', '', k)), k)
    labels = sorted(d2, key=key)
    a = [g for k in labels for g in d1.get(k, [])]; b = [g for k in labels for g in d2[k]]
    if True:
        sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
        n = max(len(a), len(b)); ok = sum(x.size for x in sm.get_matching_blocks())
        tot += n; agree += ok
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op != 'equal': print(fr, op, 'pass1:', a[i1:i2], 'pass2:', b[j1:j2])
print(f'groups compared {tot}, agreeing {agree} ({agree/max(1,tot):.1%})')
