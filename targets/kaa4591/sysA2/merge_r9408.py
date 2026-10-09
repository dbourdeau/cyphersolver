"""r9408m.tok = the v4 re-transcribed lines (r9408v4.tok, 98 lines with codes by shape) + every other line from
r9408s.tok (v3 with the image-confirmed y/4 splits applied from the reading, applysplit.py)."""
import re
new = {l.split(' ', 1)[0]: l.rstrip('\n') for l in open('../r9408/retranscribe_v4.txt', encoding='utf8') if re.match(r'P\d\.\d\d ', l)}
v4 = {l.split(' ', 1)[0]: l.rstrip('\n') for l in open('r9408v4.tok', encoding='utf8') if l.strip()}
out = []
for l in open('r9408s.tok', encoding='utf8'):
    k = l.split(' ', 1)[0]
    out.append(v4[k] if k in new else l.rstrip('\n'))
open('r9408m.tok', 'w', encoding='utf8').write('\n'.join(out) + '\n')
print(sum(1 for l in out if l.split(' ', 1)[0] in new), 'lines from v4')
