# compare_blind.py: b127 blind transcription of image 489R against the first (b119). Standard library only.
# python3 -I scripts/compare_blind.py -> controls/compare_blind.txt. Parsers as in scripts/original/b127_cmp.py:
# blind tokens are the '.'-separated numbers of each RUN line ('?' stripped); first tokens are the numbers outside quotes.
import os, re, difflib
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(HERE, *a)
a = []
for l in open(P('second_transcription', 'blind_489R.txt'), encoding='utf-8'):
    if l.startswith('R'): a += [t.rstrip('?') for t in l.split('|')[-1].strip().split('.')]
b = []
for l in open(P('transcriptions', 'despatch_1677-11-24_489R.txt'), encoding='utf-8'):
    if l.startswith('R'): b += re.findall(r'(?<![\w"])\d+(?![\w"])', re.sub(r'"[^"]*"', '', l.split(':', 1)[1]))
res = ['blind numbers %d, first numbers %d' % (len(a), len(b))]
sm = difflib.SequenceMatcher(None, a, b, autojunk=False); eq = 0
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == 'equal': eq += i2 - i1
    else: res.append('%s blind[%d:%d] %s first[%d:%d] %s' % (op, i1, i2, a[i1:i2], j1, j2, b[j1:j2]))
res.append('identical aligned numbers %d of %d = %.2f%%' % (eq, len(b), 100.0 * eq / len(b)))
os.makedirs(P('controls'), exist_ok=True)
open(P('controls', 'compare_blind.txt'), 'w', encoding='utf-8').write('\n'.join(res) + '\n')
print('\n'.join(res))
