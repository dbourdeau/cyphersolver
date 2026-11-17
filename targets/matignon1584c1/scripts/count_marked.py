# count_marked.py reading_marked.txt -> sure / {probable} / [restored] / ‹unresolved› word counts
import re, sys
c = [0, 0, 0, 0]
for l in open(sys.argv[1], encoding='utf-8'):
    m = re.match(r'^(\w+):\s*(.*)$', l.rstrip('\n'))
    if not m:
        continue
    for x in re.findall(r'\{[^}]*\}|\[[^\]]*\]|‹[^›]*›|\S+', m.group(2)):
        c['{[‹'.find(x[0]) + 1 if x[0] in '{[‹' else 0] += 1
t = sum(c)
print('sure %d probable %d restored %d unresolved %d total %d strict %.3f sense %.3f'
      % (c[0], c[1], c[2], c[3], t, c[0] / t, (c[0] + c[1] + c[2]) / t))
