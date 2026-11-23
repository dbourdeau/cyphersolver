"""Parse the two blind passes of one letter, drop struck groups and catchwords, align the two token streams
and write the merged stream with every disagreement marked.
Usage: python3 -I merge_passes.py <passA> <passB> <out.tsv>
Output rows: idx, kind (G group / W clear words), status (agree / dispute), A reading, B reading, A place, B place, A alternatives, B alternatives."""
import sys, re, difflib

def parse(path):
    pages = []; cur = None
    for line in open(path, encoding='utf-8'):
        line = line.rstrip('\n')
        if line.startswith('## page'):
            cur = []; pages.append((line.split()[2], cur)); continue
        m = re.match(r'(L\d+):\s*(.*)', line)
        if not m or cur is None: continue
        toks = []
        for t in m.group(2).split():
            t = t.rstrip('=')
            if t.startswith('{x:'): continue                       # struck through by the writer
            mm = re.fullmatch(r'\{\^(.+)\}', t)
            if mm: t = mm.group(1)
            if re.fullmatch(r'[\d?]+(\|[\d?]+)*', t):
                alts = t.split('|'); toks.append(('G', alts[0], alts[1:]))
            elif t != '(?)' and not re.search(r'[A-Za-z0-9]', t): continue   # dashes, rows of dots, '~': marks, not words
            else: toks.append(('W', t, []))
        cur.append((m.group(1), toks))
    # catchwords: a last line of one or two groups repeated at the head of the next page
    for i in range(len(pages) - 1):
        lines = pages[i][1]
        if not lines: continue
        last = lines[-1][1]
        nxt = [t for _, tk in pages[i + 1][1] for t in tk][:len(last)]
        if 0 < len(last) <= 2 and all(t[0] == 'G' for t in last) and [t[1] for t in last] == [t[1] for t in nxt]:
            lines.pop()
    out = []
    for pg, lines in pages:
        for ln, toks in lines:
            for kind, val, alts in toks:
                if kind == 'W' and out and out[-1][0] == 'W' :
                    out[-1] = ('W', out[-1][1] + ' ' + val, [], out[-1][3]); continue
                out.append((kind, val, alts, f'p{pg} {ln}'))
    return out

A, B = parse(sys.argv[1]), parse(sys.argv[2])
key = lambda t: 'W' if t[0] == 'W' else t[1]
sm = difflib.SequenceMatcher(None, [key(t) for t in A], [key(t) for t in B], autojunk=False)
rows = []; nG = agree = 0
for op, a0, a1, b0, b1 in sm.get_opcodes():
    if op == 'equal':
        for a, b in zip(A[a0:a1], B[b0:b1]):
            rows.append((a[0], 'agree', a[1], b[1], a[3], b[3], '|'.join(a[2]), '|'.join(b[2])))
            if a[0] == 'G': nG += 1; agree += 1
    else:
        la, lb = A[a0:a1], B[b0:b1]
        for i in range(max(len(la), len(lb))):
            a = la[i] if i < len(la) else None; b = lb[i] if i < len(lb) else None
            kind = (a or b)[0] if not (a and b) or a[0] == b[0] else 'X'
            rows.append((kind, 'dispute', a[1] if a else '-', b[1] if b else '-', a[3] if a else '', b[3] if b else '',
                         '|'.join(a[2]) if a else '', '|'.join(b[2]) if b else ''))
            nG += 1
with open(sys.argv[3], 'w', encoding='utf-8') as f:
    f.write('idx\tkind\tstatus\tA\tB\tA_place\tB_place\tA_alt\tB_alt\n')
    for i, r in enumerate(rows): f.write(f'{i}\t' + '\t'.join(r) + '\n')
print(f'{sys.argv[3]}: group places {nG}, agreed {agree} ({agree/nG:.1%}), disputes {nG-agree}; A groups {sum(t[0]=="G" for t in A)}, B groups {sum(t[0]=="G" for t in B)}')
for i, r in enumerate(rows):
    if r[1] == 'dispute': print(i, *r, sep='  ')
