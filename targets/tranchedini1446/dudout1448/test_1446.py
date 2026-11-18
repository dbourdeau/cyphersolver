"""Tests asked in issue #616, after the f. 30 measurement, with the frozen table_1448.json (no re-fitting).
f. 139: Daniel's texts/f139_signs.txt, labels crosswalked to the 1448 labels (texts/sign_legend.md, column f139).
Score = mean log-probability per letter of the stretches of >= 3 valued signs (as table_test.py) under lang.lm it-cinquecento,
order 4 without spaces (the order-5 no-space cache was not available offline; Daniel's own table is rescored here with the same
model so the two figures compare). 200 within-class shuffles, seed 1446.
Run from a cyphersolver checkout root: python3 <this file> <path to table_1448.json>"""
import os, sys, json, random, statistics as st
sys.path.insert(0, os.getcwd())
from lang import lm
m = lm.load('it-cinquecento', order=4, spaces=False)
T = json.load(open(sys.argv[1], encoding='utf8'))['table']
X = {'e/ee': 'e', 'n/ne': 'n', "r'/ri": 'ri', "r'": 'rb', 'ss/s3': 'ss', 'pe/de': 'de', 'ma/b': 'ma', 'b/co': 'co', 'm/ci': 'ci',
     'du/do': 'do', 'me/fa': 'fa', '@12': 'l', '@102': 'l', '@08': 'i2', '@23': 'oc', '@18': 'Z7', '@05': 'T', 'SFORZA?': 'FIOR',
     'SFORZA': 'SFZ', 'VENEZIANI': 'VEN', "a'": 'asm', "o'": 'Abold', 'o': 'o2', "o''": 'o3', 's3': 'sI'}
# Daniel's values (table_test.py + relabel.py: duca, fiorentini, l)
DW = {'NON': 'non', 'VENEZIANI': 'duca', 'CON': 'con', 'ET': 'et', 'IN': 'in', 'CHE': 'che', 'CONTE': 'conte', 'SFORZA?': 'fiorentini', 'SFORZA': 'sforza', '@12': 'l', '@102': 'l'}
syl = {'ce','ci','co','de','du','fa','li','lo','me','mi','na','ne','no','pi','re','ri','ro','si','ta','te','to','pe'}
let = set('acdeghilmnopqrstuz') | {'ee', 'll', 'ss', 'tt'}
def clean(t): return t if t == 'SFORZA?' else t.rstrip('?')
def dval(t):
    t = clean(t)
    if t in DW: return DW[t]
    t2 = t.replace("'", '').replace('"', '')
    return t2 if (t2 in syl or t2 in let) else None
def lab(t): t = clean(t); return X.get(t, t)
runs = [ln.split()[1:] for ln in open('targets/tranchedini1446/texts/f139_signs.txt', encoding='utf8') if ln.strip()]
toks = [t for r in runs for t in r]
def stretches(valf):
    out = []
    for r in runs:
        cur = []
        for t in r + ['@end']:
            v = valf(t)
            if not v or t == '@end':
                if len(cur) >= 3: out.append(''.join(cur))
                cur = []
            else: cur.append(v.replace('~', '').replace('_', ''))
    return out
def score(valf):
    tot = n = 0
    for s in stretches(valf):
        s = lm.norm(s, 'early')
        if len(s) >= 3: tot += m.per_char(s) * len(s); n += len(s)
    return (tot / n if n else float('nan')), n
v48 = lambda t: T.get(lab(t)) if T.get(lab(t)) not in (None, '_') else None
cov48 = sum(1 for t in toks if v48(t)) / len(toks)
covD = sum(1 for t in toks if dval(t)) / len(toks)
types = sorted(set(clean(t) for t in toks))
both = [t for t in types if dval(t) and v48(t)]
agree = [t for t in both if dval(t).replace('v', 'u') == v48(t).replace('li~', '').replace('v', 'u')]
def shuffled_scores(valmap, seed):
    keys = [k for k in valmap]
    cls = lambda k: 'w' if k.isupper() else 'l'
    rnd = random.Random(seed); out = []
    for _ in range(200):
        mp = dict(valmap)
        for c in 'wl':
            ks = [k for k in keys if cls(k) == c]; vs = [valmap[k] for k in ks]; rnd.shuffle(vs); mp.update(zip(ks, vs))
        out.append(score(lambda t: mp.get(clean(t)))[0])
    return out
map48 = {t: v48(t) for t in types if v48(t)}
mapD = {t: dval(t) for t in types if dval(t)}
s48, n48 = score(lambda t: map48.get(clean(t))); c48 = shuffled_scores(map48, 1446)
sD, nD = score(lambda t: mapD.get(clean(t))); cD = shuffled_scores(mapD, 1446)
res = {'f139_tokens': len(toks), 'coverage_1448': round(cov48, 3), 'coverage_daniel_table': round(covD, 3),
       'types_valued_by_both': len(both), 'types_same_value': len(agree), 'same': agree,
       'differ': {t: [dval(t), v48(t)] for t in both if t not in agree},
       'score_1448': round(s48, 3), 'letters_1448': n48, 'ctl_1448_mean': round(st.mean(c48), 3), 'z_1448': round((s48 - st.mean(c48)) / st.pstdev(c48), 1),
       'score_daniel': round(sD, 3), 'letters_daniel': nD, 'ctl_daniel_mean': round(st.mean(cD), 3), 'z_daniel': round((sD - st.mean(cD)) / st.pstdev(cD), 1),
       'sample_1448': stretches(lambda t: map48.get(clean(t)))[:25]}
print(json.dumps(res, ensure_ascii=False, indent=1))
