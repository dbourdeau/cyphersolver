"""Turn segments_a.json (by-eye ledger) into the transcription files.
Writes signs.tsv (line, index, x0, x1, label, grade), transcription.txt ('L1: tok tok . tok', page order left to right),
cipher_tokens.txt (signs only) and prints class counts per grade. HC = closed form of HB (second bar joined by a right stem)."""
import json, os, collections
os.chdir(os.path.dirname(os.path.abspath(__file__)))
d = json.load(open('segments_a.json'))
HC = {(1, 19), (2, 19), (2, 22), (3, 14), (4, 15), (6, 5), (6, 13), (6, 18), (7, 12), (8, 6), (10, 8)}
rows = []
for ln in sorted(d, key=int):
    L = int(ln)
    for i, (x0, x1, lab, g) in enumerate(d[ln], 1):
        if lab == 'HB' and (L, i) in HC:
            lab = 'HC'
        rows.append((L, i, x0, x1, lab, g))
with open('signs.tsv', 'w') as f:
    f.write('line\tindex\tx0\tx1\tlabel\tgrade\n')
    for r in rows:
        f.write('%d\t%d\t%d\t%d\t%s\t%s\n' % r)
hdr = ['# T-S K24.24 recto, second attempt (24 Nov 2026): sign-level transcription by eye from the deskewed native image.',
       '# One Latin label per sign shape (legend in NOTES.md); page order, left to right, lines 1-10 top to bottom; "." = dot cluster standing alone.',
       '# Grades per sign are in signs.tsv (firm / likely / doubtful). Reading direction: probably right to left (NOTES.md); not proved.']
with open('transcription.txt', 'w') as f:
    f.write('\n'.join(hdr) + '\n')
    for L in range(1, 11):
        f.write('L%d: %s\n' % (L, ' '.join(r[4] for r in rows if r[0] == L)))
with open('cipher_tokens.txt', 'w') as f:
    f.write('# The cipher signs only, page order (left to right), one line per cipher line (from transcription.txt: dot clusters removed). Replaces the stroke-cluster stream of the first attempt (kept as transcription_auto.txt).\n')
    for L in range(1, 11):
        f.write(' '.join(r[4] for r in rows if r[0] == L and r[4] != '.') + '\n')
c = collections.Counter((r[4], r[5]) for r in rows if r[4] != '.')
tot = collections.Counter(r[4] for r in rows if r[4] != '.')
for k, v in tot.most_common():
    print(k, v, 'firm %d likely %d doubtful %d' % (c[(k, 'firm')], c[(k, 'likely')], c[(k, 'doubtful')]))
print('signs', sum(tot.values()), 'classes', len(tot), 'dots', sum(1 for r in rows if r[4] == '.'))
g = collections.Counter(r[5] for r in rows if r[4] != '.')
print(g)
