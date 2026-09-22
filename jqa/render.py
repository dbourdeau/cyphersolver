"""Apply the JQA code table (code_table.tsv, built by consolidate.py) to a group file.
python render.py FILE
Values graded H or C print plain, M and I with '?', unread groups as {n}. Tokens with lost digits (142x) are
not counted. Last line: groups valued / complete groups, and the count per grade."""
import sys, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
tab = {}
for l in open('code_table.tsv', encoding='utf8'):
    p = l.rstrip('\n').split('\t')
    if l.startswith('#') or len(p) < 3 or not p[0].isdigit():
        continue
    tab[int(p[0])] = (p[1], p[2][:1])
tot = hit = 0
cnt = {'H': 0, 'C': 0, 'M': 0, 'I': 0}
for line in open(sys.argv[1], encoding='utf8'):
    out = []
    for t in line.split():
        if t.isdigit():
            tot += 1
            n = int(t)
            if n in tab:
                v, g = tab[n]; hit += 1; cnt[g] += 1
                out.append(v + ('' if g in 'HC' else '?'))
            else:
                out.append('{' + t + '}')
        else:
            out.append(t.upper() if t != '|' else '|')
    print(' '.join(out))
print(hit, 'of', tot, '  by grade:', ' '.join(f'{k}={v}' for k, v in cnt.items()))
