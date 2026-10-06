"""Sense measure: share of decoded words (code values expanded) that are attested Spanish word forms.
Vocabulary = Villa, Memorias (1500-30 Spanish documents), Don Quijote, and the clerk decipherments of
N.12/N.39/N.41. Bracketed (unknown) groups count as unread. Run: python measure_sense.py"""
import re, sys, glob, unicodedata, collections
sys.path.insert(0, '.')
from decode import decode
def nz(t):
    t = unicodedata.normalize('NFD', t.lower()); t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    return t.replace('v', 'u').replace('j', 'i').replace('y', 'i').replace('ç', 'z')
V = collections.Counter()
for f in ['../vasto1527/memoriasparalah00goog.txt', '../vasto1527/memoriasparalah00villgoog.txt'] + glob.glob('../esp318/lit/quijote*.txt') + glob.glob('n*_clear.txt'):
    try: V.update(re.findall(r'[a-zñ]+', nz(open(f, encoding='utf-8', errors='ignore').read())))
    except FileNotFoundError: pass
VOC = {w for w, c in V.items() if c >= 2 or len(w) <= 3}
F = {'N.12': ['n12_transcription.txt'], 'N.39': ['n39_transcription.txt'], 'N.41': ['n41_transcription.txt'],
     'N.45': ['n45_pp03-09_v2.txt', 'n45_pp10-15_v2.txt'], 'N.57': ['n57_transcription_v2.txt'],
     'N.60': ['n60_transcription_v2.txt'], 'N.60old': ['n60_pp03-09.txt', 'n60_pp10-15.txt']}
TA = TS = 0
for n, fs in F.items():
    toks = []
    for f in fs:
        for l in open(f, encoding='utf-8'):
            if l.startswith('L'): toks += l.split(':', 1)[1].split()
    words = decode(toks).split()
    ok = sum(1 for w in words if not w.startswith('[') and (re.sub('[^a-zñ]', '', nz(w)) in VOC or not re.sub('[^a-zñ]', '', nz(w))))
    TA += len(words)*(n != 'N.60old'); TS += ok*(n != 'N.60old'); print(f'{n}: {ok}/{len(words)} words = {ok/len(words):.3f}')
print(f'1511-12 key letters: {TS}/{TA} = {TS/TA:.3f}')
