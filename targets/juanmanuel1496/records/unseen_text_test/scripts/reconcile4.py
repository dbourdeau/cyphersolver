"""Part A of PLAN_round4.md: mechanical reconciliation of readers P and Q, run once per letter.
usage: python3 -I reconcile4.py LABEL OUTDIR P1.txt[,P2.txt..] Q1.txt[,Q2.txt..]
Line order = the order of first appearance in P's files. Writes OUTDIR/reconciled_LABEL.txt (agreed tokens; _ = hole)
and OUTDIR/positions_LABEL.tsv; prints agreement per line and in all."""
import sys, re, difflib, os
lab, out, pf, qf = sys.argv[1], sys.argv[2], sys.argv[3].split(','), sys.argv[4].split(',')
def load(paths):
    lines, order = {}, []
    for p in paths:
        for ln in open(p, encoding='utf-8'):
            ln = ln.rstrip('\n')
            m = re.match(r'\s*([A-Z]\d\d)\s*:(.*)', ln)
            if not m or ln.lstrip().startswith('!'): continue
            k, v = m.group(1), m.group(2)
            v = re.sub(r'\?\([^)]*\)', '?', v)
            toks = [t if not t.startswith('{') else t.lower() for t in v.split() if t != '/']
            if k not in lines: order.append(k)
            lines.setdefault(k, []).extend(toks)
    return lines, order
P, order = load(pf); Q, oq = load(qf)
order += [k for k in oq if k not in order]
rows, rec_lines = [], []; ta = tn = 0
for L in order:
    a, b = P.get(L, []), Q.get(L, [])
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False); rec = []; ag = n = 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            for t in a[i1:i2]:
                n += 1
                if t in ('?', '#'): rec.append('_'); rows.append((L, len(rec), 'both-unclear', t, t))
                else: rec.append(t); ag += 1; rows.append((L, len(rec), 'agree', t, t))
        else:
            m = max(i2 - i1, j2 - j1); aa = a[i1:i2] + ['-'] * (m - (i2 - i1)); bb = b[j1:j2] + ['-'] * (m - (j2 - j1))
            for x, y in zip(aa, bb): n += 1; rec.append('_'); rows.append((L, len(rec), op, x, y))
    rec_lines.append(f'{L}: ' + ' '.join(rec)); ta += ag; tn += n
    print(f'{L}: P {len(a)} Q {len(b)} aligned {n} agreed {ag} ({ag / n:.0%})' if n else f'{L}: empty')
open(os.path.join(out, f'reconciled_{lab}.txt'), 'w').write(f'# Round 4 reconciled transcription ({lab}): tokens both readers wrote; _ = hole\n' + '\n'.join(rec_lines) + '\n')
with open(os.path.join(out, f'positions_{lab}.tsv'), 'w') as f:
    f.write('line\tpos\tstatus\tP\tQ\n')
    for r in rows: f.write('\t'.join(map(str, r)) + '\n')
print(f'ALL {lab}: agreed {ta} of {tn} aligned positions ({ta / tn:.1%}); P {sum(map(len, P.values()))} signs, Q {sum(map(len, Q.values()))} signs')
