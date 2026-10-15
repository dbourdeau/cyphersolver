"""Token coverage per letter under decode.py (unknown groups, ? and / count unread).
The entry's documents are N.45, N.57 and N.60 (read here); N.12, N.39, N.41 are deciphered siblings, shown for
reference. N.73 (1515) is in another key and was split off to targets/vich1515/ on 14 Oct 2026."""
import sys, collections
sys.path.insert(0, '.')
from decode import LET, CODE
F = {'N.12': ['n12_transcription.txt'], 'N.39': ['n39_transcription.txt'], 'N.41': ['n41_transcription.txt'], 'N.45': ['n45_pp03-09_v2.txt', 'n45_pp10-15_v2.txt'],
     'N.57': ['n57_transcription_v2.txt'], 'N.60': ['n60_transcription_v3.txt'], 'N.60old': ['n60_pp03-09.txt', 'n60_pp10-15.txt']}
DOCS = ('N.45', 'N.57', 'N.60')
T = K = DT = DK = 0; unk = collections.Counter()
for n, fs in F.items():
    t = k = 0
    for f in fs:
        for l in open(f, encoding='utf-8'):
            if not l.startswith('L'): continue
            for x in l.split(':', 1)[1].split():
                t += 1
                if x in LET or x in CODE: k += 1
                else: unk[x] += 1
    T += t*(n != 'N.60old'); K += k*(n != 'N.60old'); print(f'{n}: {k}/{t} = {k/t:.3f}')
    if n in DOCS: DT += t; DK += k
print(f'all letters in the 1511-12 key: {K}/{T} = {K/T:.3f}')
print(f'documents N.45+N.57+N.60: {DK}/{DT} = {DK/DT:.4f}')
if '-v' in sys.argv: print(unk.most_common(60))
