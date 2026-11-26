"""Frozen September-only key applied to the November letter, against shuffled tables.

Key: sept_key_from_pair.tsv as produced from the September pair (no November value, no override).
Numbers with two values in that file (conflicts) are left out. Transcription: nov_transcription_v2.tsv,
first digit alternative everywhere (the key is NOT allowed to choose among alternatives).
Score: mean log-probability per character (lang model fr-1750-nospace) of the decoded text of each
cipher run of 3 or more consecutive valued groups, main text only. Control: the same values dealt at
random to the same numbers, 200 draws.
"""
import csv, hashlib, io, os, random, re, sys, unicodedata
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm
import decode_nov as d

HERE = os.path.dirname(os.path.abspath(__file__))
kp = os.path.join(HERE, 'sept_key_from_pair.tsv')
sha = hashlib.sha256(open(kp, 'rb').read()).hexdigest()
key = {}
for r in csv.DictReader(open(kp, encoding='utf-8'), delimiter='\t'):
    n, v = r['number'].strip(), r['value'].strip()
    if n.isdigit() and v and ' / ' not in v and '?' not in v:
        key[int(n)] = re.sub(r'\s*\(.*', '', v)

rows = [r for r in csv.DictReader(open(os.path.join(HERE, 'nov_transcription_v2.tsv'), encoding='utf-8'), delimiter='\t')
        if 'margin' not in r['folio'] and 'PS' not in r['folio']]
runs, cur = [], []
for r in rows:
    if r['kind'] != 'num':
        if cur: runs.append(cur); cur = []
        continue
    c = d.expand(r['text'])
    cur.append(c[0] if c else -1)
if cur: runs.append(cur)
groups = sum(len(x) for x in runs)

def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(ch for ch in s if 'a' <= ch <= 'z')

M = lm.load('fr-1750-nospace')
def score(k):
    tot = n = 0; cov = 0
    for run in runs:
        seg = []
        for g in run + [-1]:
            if g in k:
                seg.append(k[g]); cov += 1
            else:
                if len(seg) >= 3:
                    t = norm(''.join(seg))
                    if len(t) >= 6:
                        tot += M.per_char(t) * len(t); n += len(t)
                seg = []
    return tot / max(n, 1), cov, n

real, cov, nch = score(key)
random.seed(1759)
nums, vals = list(key), list(key.values())
ctrl = []
for _ in range(200):
    random.shuffle(vals)
    ctrl.append(score(dict(zip(nums, vals)))[0])
ctrl.sort()
print('key file sha256', sha)
print('key numbers used', len(key), '| November main-text groups', groups, '| groups with a value', cov, '(%.3f)' % (cov / groups))
print('scored characters', nch)
print('real key   mean log-prob per char: %.3f' % real)
print('shuffled   best %.3f  p99 %.3f  median %.3f  worst %.3f' % (ctrl[-1], ctrl[-3], ctrl[100], ctrl[0]))
print('draws at or above the real key:', sum(1 for x in ctrl if x >= real), 'of 200')
