import re, csv, numpy as np
from collections import Counter
# Paths edited for the repository copy (were local folders): BASE holds transcriptions/ (here ../../, i.e. blind_2026-11-15/); ORT is the OCR text
# of Official Records ser. I vol. 49 pt. 2 (Internet Archive warofrebellion014902rootrich, _djvu.txt).
BASE = "../../"
ORT = "warofrebellion014902rootrich_djvu.txt"
def pref(g): return re.sub(r'\[([^/\]]*)/[^\]]*\]', r'\1', g)
def load(reader):
    rows = list(csv.DictReader(open(BASE+f"transcriptions/{reader}_transcription.tsv"), delimiter='\t'))
    tel = {}
    for r in rows: tel.setdefault((r['frame'], r['telegram']), []).append(r)
    return tel
UNITS = {'T03':('A','v196_0056',1,'COMPLETEVICTORY'),'T05':('A','v196_0065',0,'COMERETRIBUTION'),
         'T06':('A','v196_0071',0,'COMERETRIBUTION'),'T08':('B','v11_0044',1,'COMERETRIBUTION'),
         'T09':('B','v11_0045',0,'COMERETRIBUTION'),'S1':('A','v196_0061',0,'COMERETRIBUTION'),
         'S2':('B','v11_0039',0,'COMERETRIBUTION'),'T07':('B','v11_0044',0,'COMERETRIBUTION'),
         'T10':('B','v11_0046',0,'COMERETRIBUTION'),'T11':('B','v11_0046',1,None)}
_cache = {}
def groups(uid, reader):
    pair, frame, ti, _ = UNITS[uid]
    if reader not in _cache: _cache[reader] = load(reader)
    t = _cache[reader]; ks = [k for k in t if k[0] == frame]
    return [re.sub('[^A-Z]', '', pref(r['group']).upper()) for r in t[ks[ti]]]
def readers(uid): return ['readerA1','readerA2'] if UNITS[uid][0]=='A' else ['readerB1','readerB2']
txt = re.sub(r'[^A-Z]', '', open(ORT, encoding='utf-8', errors='ignore').read().upper())
cnt = Counter(txt[i:i+4] for i in range(len(txt)-3)); N = sum(cnt.values())
Q = np.full(26**4, np.log10(0.01/N), dtype=np.float32)
for k, v in cnt.items():
    Q[((ord(k[0])-65)*26+ord(k[1])-65)*26*26 + (ord(k[2])-65)*26 + ord(k[3])-65] = np.log10(v/N)
def arr(s): return np.array([ord(c)-65 for c in s], dtype=np.int64)
def txtof(a): return ''.join(chr(65+int(x)) for x in a)
def qs(P):  # P: (..., n) -> mean quadgram along last axis
    idx = ((P[...,:-3]*26 + P[...,1:-2])*26 + P[...,2:-1])*26 + P[...,3:]
    return Q[idx].mean(axis=-1)
# T11 runs of cipher between clear words (group indices, 0-based) and clear-word letter counts inserted before group
T11_RUN_STARTS = [0, 8, 13, 21]
T11_CLEAR_BEFORE = {8: 5, 13: 14, 21: 17}  # "as the", "on that"+"If you can", "Can have four or five"
