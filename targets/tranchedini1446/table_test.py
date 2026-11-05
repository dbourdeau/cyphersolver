"""Does the Domnina/Lasry table give better Italian on f. 139 than a shuffled table?
Reads texts/f139_signs.txt (one line per text line, cipher labels only), keeps stretches of >= 3 signs that have a table value,
scores their concatenated values with it-cinquecento, and compares with 200 random re-assignments of the same values.
Run from the repository root: python targets/tranchedini1446/table_test.py"""
import os, random, statistics as st, sys
sys.path.insert(0, os.getcwd())
from lang import lm
m = lm.load('it-cinquecento', order=5, spaces=False)
words = {'NON': 'non', 'VENEZIANI': 'veneziani', 'CON': 'con', 'ET': 'et', 'IN': 'in', 'CHE': 'che', 'CONTE': 'conte', 'SFORZA': 'sforza'}
syl = {'ce','ci','co','de','du','fa','li','lo','me','mi','na','ne','no','pi','re','ri','ro','si','ta','te','to','pe'}
let = set('acdeghilmnopqrstuz') | {'ee', 'll', 'ss', 'tt'}
def clean(t): return t.rstrip('?').replace("'", '').replace('"', '')
def val(t):
    t = clean(t)
    return words.get(t) or (t if t in syl or t in let else None)
runs = []
for ln in open('targets/tranchedini1446/texts/f139_signs.txt', encoding='utf8'):
    cur = []
    for t in ln.split()[1:] + ['@end']:
        if val(t) is None:
            if len(cur) >= 3: runs.append(cur)
            cur = []
        else: cur.append(clean(t))
def score(mp):
    tot = n = 0
    for r in runs:
        s = lm.norm(''.join(mp.get(t, val(t)) for t in r), 'early')
        if len(s) >= 3: tot += m.per_char(s) * len(s); n += len(s)
    return tot / n
base = {t: val(t) for r in runs for t in r}
types = sorted(t for t in set(base) if t not in words)
vals = [base[t] for t in types]
random.seed(1); sc = []
for _ in range(200):
    v = vals[:]; random.shuffle(v); mp = dict(base); mp.update(zip(types, v)); sc.append(score(mp))
b = score(base)
print(len(runs), 'stretches,', sum(len(r) for r in runs), 'tokens; table', round(b, 3), 'shuffled', round(st.mean(sc), 3), 'sd', round(st.pstdev(sc), 3), 'z', round((b - st.mean(sc)) / st.pstdev(sc), 2))
