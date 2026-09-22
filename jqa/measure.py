"""Measure No. 88: groups valued by code_table.tsv and groups read as sense (valued and not flagged in sense88.tsv).
python measure.py        Tokens with lost digits (142x ...) count as groups not read. 'cw:' tokens (catchwords) are skipped."""
import os, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))
tab = {}
for l in open('code_table.tsv', encoding='utf8'):
    p = l.rstrip('\n').split('\t')
    if l.startswith('#') or len(p) < 3 or not p[0].isdigit():
        continue
    tab[int(p[0])] = p[2][:1]
flags = set()
for l in open('sense88.tsv', encoding='utf8'):
    p = l.rstrip('\n').split('\t')
    if l.startswith('#') or len(p) < 3:
        continue
    g, _, k = p[2].partition('@')
    flags.add((p[0], int(p[1]), int(g), int(k) if k else 0))
tot = {'all': [0, 0, 0, 0, 0, 0]}
for f in ('gap88.txt', 'rem88.txt'):
    n = valued = sense = sense_noI = lost = 0
    grades = {'H': 0, 'C': 0, 'M': 0, 'I': 0}
    for i, line in enumerate(open(f, encoding='utf8'), 1):
        seen = {}
        for t in line.split():
            if re.fullmatch(r'\d+', t):
                n += 1
                seen[t] = seen.get(t, 0) + 1
                g = tab.get(int(t))
                if g:
                    valued += 1
                    if (f, i, int(t), 0) not in flags and (f, i, int(t), seen[t]) not in flags:
                        sense += 1; grades[g] += 1
                        if g != 'I':
                            sense_noI += 1
            elif re.fullmatch(r'\d+x+', t):
                n += 1; lost += 1
    print(f'{f}: {n} groups ({lost} with lost digits); valued {valued}; read as sense {sense} = {sense/n:.3f} '
          f'(without I-graded: {sense_noI} = {sense_noI/n:.3f}); sense by grade {grades}')
    for k, v in zip(range(6), (n, valued, sense, sense_noI, lost, 0)):
        tot['all'][k] += v
n, valued, sense, sense_noI, lost, _ = tot['all']
print(f'No. 88 total: {n} groups; valued {valued} = {valued/n:.3f}; read as sense {sense} = {sense/n:.3f}; without I {sense_noI} = {sense_noI/n:.3f}')
