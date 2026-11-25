"""Segment ledger for the by-eye pass: segments_<pass>.json = {line: [[x0, x1, label, grade], ...]} in page order
(left to right, deskewed native pixels of img/w/flat.png). A divider (dot cluster) has label '.'.
Usage: python seg.py <pass> <line> "x0-x1:LABEL[?|!] x0-x1:LABEL ..."   (? doubtful, ! firm; none = likely)
       python seg.py <pass> show
Also appends the line to transcription.txt (pass a only) so nothing is held in memory."""
import sys, json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
p = sys.argv[1]
fn = 'segments_%s.json' % p
d = json.load(open(fn)) if os.path.exists(fn) else {}
if sys.argv[2] == 'show':
    for k in sorted(d, key=int):
        print(k, ' '.join(s[2] for s in d[k]))
    sys.exit()
line = sys.argv[2]
segs = []
for tok in sys.argv[3].split():
    r, lab = tok.split(':')
    x0, x1 = r.split('-')
    g = 'likely'
    if lab.endswith('?'):
        g, lab = 'doubtful', lab[:-1]
    elif lab.endswith('!'):
        g, lab = 'firm', lab[:-1]
    segs.append([int(x0), int(x1), lab, g])
d[line] = segs
json.dump(d, open(fn, 'w'))
print(line, len(segs), ' '.join(s[2] for s in segs))
