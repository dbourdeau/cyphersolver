"""Known-key test on the blind transcriptions of 15 Nov 2026 (TEST_PLAN.md). Re-runnable copy.

Same computation as the run of 15 Nov (seed 1865, same order of random draws); only the paths are made relative
and the JSON is written with numpy integers converted (the original run crashed on that after printing every result).

    python run_test.py <path to warofrebellion014902rootrich_djvu.txt> [out.json]

The quadgram model is built from the Internet Archive OCR text of Official Records Ser. I vol. 49 pt. 2:
https://archive.org/download/warofrebellion014902rootrich/warofrebellion014902rootrich_djvu.txt
(sha256 834848aeeda9eb159e451a457434c7eab1029e96d26a2e37de8b016285fea24c; not in the repository).
"""
import csv, re, json, random, sys, pathlib
from collections import Counter
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
KEYS = ["COMPLETEVICTORY", "COMERETRIBUTION", "MANCHESTERBLUFF", "THENAVYOURPRIDE"]


def pref(g):  # preferred reading: [Y/V] -> Y
    return re.sub(r'\[([^/\]]*)/[^\]]*\]', r'\1', g)


def load(reader):
    rows = list(csv.DictReader(open(HERE / 'transcriptions' / f'{reader}_transcription.tsv', encoding='utf-8'),
                               delimiter='\t'))
    tel = {}
    for r in rows:
        tel.setdefault((r['frame'], r['telegram']), []).append(r)
    return tel


txt = re.sub(r'[^A-Z]', '', open(sys.argv[1], encoding='utf-8', errors='ignore').read().upper())
cnt = Counter(txt[i:i+4] for i in range(len(txt)-3)); N = sum(cnt.values())
Q = np.full(26**4, np.log10(0.01/N))
for k, v in cnt.items():
    Q[((ord(k[0])-65)*26+ord(k[1])-65)*26*26 + (ord(k[2])-65)*26 + ord(k[3])-65] = np.log10(v/N)


def qscores(p):
    idx = ((p[:-3]*26 + p[1:-2])*26 + p[2:-1])*26 + p[3:]
    return Q[idx]


def keyarr(k): return np.array([ord(c)-65 for c in k])


def decs(c, key):
    ka = keyarr(key); n = len(c)
    return np.array([(c - ka[(o + np.arange(n)) % 15]) % 26 for o in range(15)])


def m1(c, keys):  # one phase: best over keys and the 15 starting positions
    best = (-99, None, None)
    for key in keys:
        D = decs(c, key)
        for o in range(15):
            s = qscores(D[o]).mean()
            if s > best[0]: best = (s, key, o)
    return best


def m2(c, keys, bounds):  # two phases of the same key, split at one group boundary (one slip)
    n = len(c); best = (-99, None, None)
    for key in keys:
        D = decs(c, key); S = np.array([qscores(D[o]) for o in range(15)])
        cs = np.concatenate([np.zeros((15, 1)), np.cumsum(S, axis=1)], axis=1)
        for s in bounds:
            if s < 15 or n - s < 15: continue
            L = cs[:, s-3]; R = cs[:, n-3] - cs[:, s]
            tot = (L[:, None] + R[None, :]) / ((s-3) + (n-3-s))
            i, j = np.unravel_index(np.argmax(tot), tot.shape)
            if tot[i, j] > best[0]: best = (tot[i, j], key, (int(i), int(j), int(s)))
    return best


UNITS = [('T01','A','v196_0053',0),('T02','A','v196_0056',0),('T03','A','v196_0056',1),('T04','A','v196_0064',0),
         ('T05','A','v196_0065',0),('T06','A','v196_0071',0),('T07','B','v11_0044',0),('T08','B','v11_0044',1),
         ('T09','B','v11_0045',0),('T10','B','v11_0046',0),('T11','B','v11_0046',1),('T12','B','v10_0056',0),
         ('S1','A','v196_0061',0),('S2','B','v11_0039',0)]
rng = random.Random(1865)
results = []
tels = {r: load(r) for r in ['readerA1','readerA2','readerB1','readerB2']}
for uid, pair, frame, ti in UNITS:
    for reader in (['readerA1','readerA2'] if pair == 'A' else ['readerB1','readerB2']):
        ks = [k for k in tels[reader] if k[0] == frame]
        groups = [re.sub('[^A-Z]', '', pref(r['group']).upper()) for r in tels[reader][ks[ti]]]
        c = np.array([ord(x)-65 for x in ''.join(groups)])
        bounds = list(np.cumsum([len(g) for g in groups])[:-1])
        r1 = m1(c, KEYS); r2 = m2(c, KEYS, bounds)
        perkey = {k: m1(c, [k])[0] for k in KEYS}
        sh1, sh2, wk1, wk2 = [], [], [], []
        for t in range(200):
            perm = list(c); rng.shuffle(perm); perm = np.array(perm)
            sh1.append(m1(perm, KEYS)[0]); sh2.append(m2(perm, KEYS, bounds)[0])
            rk = ''.join(chr(65+rng.randrange(26)) for _ in range(15))
            wk1.append(m1(c, [rk])[0]); wk2.append(m2(c, [rk], bounds)[0])
        ctl1 = max(sh1 + wk1); ctl2 = max(sh2 + wk2)
        srt = sorted(perkey.values(), reverse=True)
        res = dict(unit=uid, reader=reader, frame=frame, letters=int(len(c)),
                   M1=dict(score=round(float(r1[0]),3), key=r1[1], offset=r1[2], control_max=round(float(ctl1),3), passed=bool(r1[0] > ctl1)),
                   M2=dict(score=round(float(r2[0]),3), key=r2[1], phases_split=r2[2], control_max=round(float(ctl2),3), passed=bool(r2[0] > ctl2)),
                   perkey_M1={k: round(float(v),3) for k, v in perkey.items()},
                   key_margin=round(float(srt[0]-srt[1]),3),
                   wrongkey_spread_95_5=round(float(np.percentile(wk1,95)-np.percentile(wk1,5)),3))
        results.append(res)
        print(uid, reader, len(c), 'M1', res['M1'], 'M2', res['M2'], 'margin', res['key_margin'], 'spread', res['wrongkey_spread_95_5'], flush=True)
if len(sys.argv) > 2:
    json.dump(results, open(sys.argv[2], 'w'), indent=1)
