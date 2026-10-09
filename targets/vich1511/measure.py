"""Token coverage per letter under decode.py (unknown groups, ? and / count unread)."""
import sys, collections
sys.path.insert(0, '.')
from decode import LET, CODE
F = {'N.12': ['n12_transcription.txt'], 'N.39': ['n39_transcription.txt'], 'N.41': ['n41_transcription.txt'], 'N.45': ['n45_pp03-09_v2.txt', 'n45_pp10-15_v2.txt'],
     'N.57': ['n57_transcription_v2.txt'], 'N.60': ['n60_transcription_v2.txt'], 'N.60old': ['n60_pp03-09.txt', 'n60_pp10-15.txt'], 'N.73': ['n73_transcription.txt']}
T = K = 0; unk = collections.Counter()
for n, fs in F.items():
    t = k = 0
    for f in fs:
        for l in open(f, encoding='utf-8'):
            if not l.startswith('L'): continue
            for x in l.split(':', 1)[1].split():
                t += 1
                if n != 'N.73' and (x in LET or x in CODE): k += 1
                elif n != 'N.73': unk[x] += 1
    T += t*(n != 'N.60old'); K += k*(n != 'N.60old'); print(f'{n}: {k}/{t} = {k/t:.3f}')
print(f'all: {K}/{T} = {K/T:.3f}')
if '-v' in sys.argv: print(unk.most_common(60))
