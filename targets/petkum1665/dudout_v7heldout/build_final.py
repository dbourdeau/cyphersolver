"""build_final.py BLIND.tsv OUT.tsv [adjudicate]: pages 505L 505R 501R; '-' rows joined to the preceding glossed row of the page."""
import sys
PAGES = ['505L', '505R', '501R']
FIX_T = {('505R', '8', '365~'): '365', ('505R', '12', '270~'): '270', ('505R', '25', 'X'): 'LAM'}
FIX_G = {('505R', '2'): ("lEuesque~", "l'Euesque"), ('505R', '8'): ('de pousser', 'despouser'), ('505R', '11'): ('petites ?', 'petites emulitez')}
adj = len(sys.argv) > 3
rows = []
for l in open(sys.argv[1], encoding='utf8'):
    if l.startswith('#') or l.startswith('image\t') or not l.strip():
        continue
    img, line, toks, gl = l.rstrip('\n').split('\t')[:4]
    if img not in PAGES:
        continue
    tt = toks.split()
    if adj:
        tt = [FIX_T.get((img, line, t), t) for t in tt]
        if img == '505R' and line == '21':
            tt = ' '.join(tt).replace('MT 269', 'MT 169').split()
        if (img, line) in FIX_G and FIX_G[(img, line)][0] in gl:
            gl = gl.replace(*FIX_G[(img, line)])
    rows.append([img, line, tt, gl])
out = []
pending = []
for r in rows:
    if r[3].strip() == '-':
        if out and out[-1][0] == r[0]:
            out[-1][2] += r[2]
        else:
            pending.append(r)
    else:
        if pending and pending[0][0] == r[0]:
            r[2] = sum((p[2] for p in pending), []) + r[2]
        pending = []
        out.append(r)
with open(sys.argv[2], 'w', encoding='utf8') as f:
    f.write('image\tline\ttokens\tgloss\n')
    for img, line, tt, gl in out:
        f.write('%s\t%s\t%s\t%s\n' % (img, line, ' '.join(tt), gl))
print(len(out), 'rows', sum(len(r[2]) for r in out), 'tokens')
