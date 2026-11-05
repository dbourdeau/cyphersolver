"""Same test as table_test.py, on the clustered inventory (texts/f139_seg.txt) with a hand mapping cluster -> table value
(from the contact sheets seg/clu_90_*.png against Domnina Fig. 5 / Lasry's table). Run from the repository root."""
import os, random, statistics as st, sys
sys.path.insert(0, os.getcwd())
from lang import lm
m = lm.load('it-cinquecento', order=5, spaces=False)
MAP = {29:'a',1:'e',10:'i',67:'l',22:'o',26:'o',60:'p',83:'non',59:'in',5:'de',14:'pe',64:'si',62:'no',66:'sforza',71:'se',65:'n',
       39:'s',88:'s',79:'u',70:'u',4:'u',47:'t',82:'sa',18:'ma',51:'te',74:'te',9:'do',33:'to',54:'ri',52:'co',0:'r',42:'da',81:'r',85:'ss',
       76:'re',24:'re',50:'re',12:'u',48:'h',80:'ne',77:'ce',32:'ce'}
def runs_of(path):
    runs = []
    for ln in open(path, encoding='utf8'):
        cur = []
        for t in ln.split()[1:] + ['W']:
            if t.startswith('c') and int(t[1:]) in MAP: cur.append(int(t[1:]))
            else:
                if len(cur) >= 3: runs.append(cur)
                cur = []
    return runs
runs = runs_of('targets/tranchedini1446/texts/f139_seg.txt')
def score(mp):
    tot = n = 0
    for r in runs:
        s = lm.norm(''.join(mp[c] for c in r), 'early')
        if len(s) >= 3: tot += m.per_char(s) * len(s); n += len(s)
    return tot / n
used = sorted({c for r in runs for c in r}); vals = [MAP[c] for c in used]
random.seed(1); sc = []
for _ in range(300):
    v = vals[:]; random.shuffle(v); mp = dict(MAP); mp.update(zip(used, v)); sc.append(score(mp))
b = score(MAP)
print(len(runs), 'stretches,', sum(map(len, runs)), 'tokens; mapped', round(b, 3), 'shuffled', round(st.mean(sc), 3), 'sd', round(st.pstdev(sc), 3), 'z', round((b - st.mean(sc)) / st.pstdev(sc), 2))
