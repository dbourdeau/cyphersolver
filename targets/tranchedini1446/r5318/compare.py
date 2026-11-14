"""R5318 "Nicodemus" key against the 1448 table (BnF ital. 1585 f. 28) - cheap comparison on training material only (14 Nov 2026).
1) table: 1448 labels with a value that have an R5318 sign of the same shape -> same value?
   two crosswalks: A = key_R5318_by_1448_label.tsv (settled); B = labels given by the blind pass B (R5318_passB_blind.tsv, '?' dropped).
2) f. 28 (1448 training slip): share of valued tokens whose R5318 value equals the settled f. 28 value; 200 within-class shuffles
   (letters/syllables, word signs), seed 5318.
3) coverage: f. 28 and f. 139 tokens (f. 139 labels crosswalked as in tranchedini1448/dudout/test_1446.py) that have an R5318 sign.
Usage: python3 -I compare.py <targets/tranchedini1448/dudout> <targets/tranchedini1446/texts/f139_signs.txt> > results_R5318.json"""
import sys, json, random, statistics as st, os
here = os.path.dirname(os.path.abspath(__file__))
dud, f139 = sys.argv[1], sys.argv[2]
T = json.load(open(os.path.join(dud, 'table_1448.json'), encoding='utf8'))['table']
EQ = {'come': 'como', 'cosimo': 'cosmo', 'su': 'us'}
def norm(v):
    v = v.lower().replace('li~', '').replace('la~', '').replace('~', '').replace('v', 'u')
    return EQ.get(v, v)
def normset(s): return {norm(x) for x in s.split('|')}
A = {}
for ln in open(os.path.join(here, 'key_R5318_by_1448_label.tsv'), encoding='utf8'):
    if ln.startswith('#') or not ln.strip(): continue
    lab, val, conf, _ = ln.rstrip('\n').split('\t')
    A[lab] = (val, conf)
legend = set(T) | {'NON', 'IN', 'COSIMO', 'FIOR', 'VEN', 'b6', 'm8', 'p9', 'oo+', 'X3', 'dd', 'T', 'iI', 'Abold', 'Ap', 'SFZ', 'COLL', 'MIL'}
B = {}
for ln in open(os.path.join(here, 'R5318_passB_blind.tsv'), encoding='utf8'):
    p = ln.rstrip('\n').split('\t')
    if len(p) < 3 or p[0] in ('null', 'foot'): continue
    lab = p[2].split()[0].rstrip('?')
    if lab in legend: B.setdefault(lab, set()).add(p[1])
def table_cmp(M, getval):
    same, diff, nov = [], {}, []
    for lab in sorted(M):
        if lab not in T:
            nov.append(lab); continue
        if normset(getval(M[lab])) & {norm(T[lab])}: same.append(lab)
        else: diff[lab] = [T[lab], getval(M[lab])]
    return {'labels_with_1448_value': len(same) + len(diff), 'same': len(same), 'differ': len(diff),
            'same_list': same, 'differ_list': diff, 'R5318_only_or_no_1448_value': nov}
resA = table_cmp(A, lambda x: x[0])
resB = table_cmp(B, lambda x: '|'.join(sorted(x)))
# f28 tokens
toks = []
for ln in open(os.path.join(dud, 'texts', 'f28_signs.txt'), encoding='utf8'):
    if ln.startswith('R'):
        for t in ln.split(':', 1)[1].split():
            if '=' in t:
                l, v = t.split('=', 1); toks.append((l, v))
valued = [(l, v) for l, v in toks if v not in ('?', '_')]
def hits(M):
    return sum(1 for l, v in valued if l in M and norm(v) in normset(M[l]))
MA = {l: A[l][0] for l in A}
real = hits(MA)
covered = sum(1 for l, v in valued if l in MA)
word = lambda l: l.isupper() or l in ('oo+', 'FIOR', 'VEN', 'COSIMO', 'SFZ', 'COLL')
rnd = random.Random(5318); ctl = []
labs = list(MA)
for _ in range(200):
    mp = {}
    for cls in (True, False):
        ks = [k for k in labs if word(k) == cls]; vs = [MA[k] for k in ks]; rnd.shuffle(vs); mp.update(zip(ks, vs))
    ctl.append(hits(mp))
# coverage f139 (crosswalk of test_1446.py)
X = {'e/ee': 'e', 'n/ne': 'n', "r'/ri": 'ri', "r'": 'rb', 'ss/s3': 'ss', 'pe/de': 'de', 'ma/b': 'ma', 'b/co': 'co', 'm/ci': 'ci',
     'du/do': 'do', 'me/fa': 'fa', '@12': 'l', '@102': 'l', '@08': 'i2', '@23': 'oc', '@18': 'Z7', '@05': 'T', 'SFORZA?': 'FIOR',
     'SFORZA': 'SFZ', 'VENEZIANI': 'VEN', "a'": 'asm', "o'": 'Abold', 'o': 'o2', "o''": 'o3', 's3': 'sI'}
def clean(t): return t if t == 'SFORZA?' else t.rstrip('?')
f139toks = [t for ln in open(f139, encoding='utf8') if ln.strip() for t in ln.split()[1:]]
lab139 = lambda t: X.get(clean(t), clean(t))
cov139_R = sum(1 for t in f139toks if lab139(t) in MA) / len(f139toks)
cov139_48 = sum(1 for t in f139toks if T.get(lab139(t)) not in (None, '_')) / len(f139toks)
cov28_R = sum(1 for l, v in toks if l in MA) / len(toks)
cov28_48 = sum(1 for l, v in toks if l in T) / len(toks)
out = {'table_vs_1448_crosswalk_A_settled': resA, 'table_vs_1448_crosswalk_B_blind': resB,
       'f28_tokens': len(toks), 'f28_valued_tokens': len(valued), 'f28_tokens_with_R5318_sign': covered,
       'f28_hits_R5318': real, 'f28_score': round(real / len(valued), 3),
       'f28_controls_200': {'mean': round(st.mean(ctl) / len(valued), 3), 'max': round(max(ctl) / len(valued), 3),
                            'sd': round(st.pstdev(ctl) / len(valued), 3), 'z': round((real - st.mean(ctl)) / st.pstdev(ctl), 1)},
       'coverage': {'f28_R5318': round(cov28_R, 3), 'f28_1448': round(cov28_48, 3),
                    'f139_tokens': len(f139toks), 'f139_R5318': round(cov139_R, 3), 'f139_1448': round(cov139_48, 3)},
       'f28_misses': sorted({f'{l}={v} (R5318 {MA[l]})' for l, v in valued if l in MA and norm(v) not in normset(MA[l])})}
print(json.dumps(out, ensure_ascii=False, indent=1))
