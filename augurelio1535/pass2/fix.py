"""fix.py PAGE LINE NEWTEXT — replace one transcription line (e.g. P6 26 'abc...'), exact page and line number."""
import sys, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'transcription.txt')
page, num, new = sys.argv[1], sys.argv[2].zfill(2), sys.argv[3]
L = open(p, encoding='utf8').read().split('\n')
cur, hits = '', []
for i, l in enumerate(L):
    if l.startswith('=='): cur = l.split()[1]; continue
    if cur == page and l.startswith(num + ' '): hits.append(i)
assert len(hits) == 1, hits
print('old', L[hits[0]]); L[hits[0]] = num + ' ' + new; print('new', L[hits[0]])
open(p, 'w', encoding='utf8').write('\n'.join(L))
