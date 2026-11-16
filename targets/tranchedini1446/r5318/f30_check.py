"""Integration check of PRs #625 and #630 (14 Nov 2026, maintainer session): a second decoder for the f. 30 measurement,
written without importing the contributor's code, and the same measurement with the R5318 key sheet instead of the 1448 table.

f. 30 was already measured once with the 1448 table (it is spent as a held-out text); the figures below are comparisons made
afterwards, not a held-out test. The 17 extra matches (EXTRA) pair f. 30 shapes that the 1448 table has no value for with
R5318 entries BY THE WRITTEN SHAPE DESCRIPTIONS ALONE (dudout1448/texts/f30_signs.txt "New shapes" against R5318_passA.tsv and
R5318_passB_blind.tsv); the R5318 image needs a DECODE login and was not seen here.
Run from this folder's parent: python3 -I r5318/f30_check.py > r5318/results_f30_check.json"""
import json, re, random, os
here = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(here, '..', 'dudout1448')
runs, cur = {}, None
for ln in open(os.path.join(D, 'texts', 'f30_signs.txt'), encoding='utf8'):
    if ln.startswith('## New shapes'): break
    m = re.match(r'(R\d+) ', ln)
    if m: cur = m.group(1); runs[cur] = []; continue
    m = re.match(r'\s+(?:v\.)?L\d+:(.*)', ln)
    if m and cur: runs[cur] += [t.rstrip('?') for t in re.sub(r'\[.*?\]', ' ', m.group(1)).split()]
def nz(s):
    out = ''
    for c in s.lower().replace('[—]', ''):
        c = {'v': 'u', 'y': 'i', 'j': 'i'}.get(c, c)
        if c.isascii() and c.isalpha() and c != 'h' and (not out or out[-1] != c): out += c
    return out
def ed(a, b):
    d = [[i + j if i * j == 0 else 0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + (a[i - 1] != b[j - 1]))
    return d[-1][-1]
ref = {m.group(1): nz(m.group(2)) for ln in open(os.path.join(D, 'texts', 'f29_reference.txt'), encoding='utf8')
       for m in [re.match(r'(R\d+): (.*)', ln)] if m}
def score(T):
    d = n = 0
    for r, toks in runs.items():
        d += ed(nz(''.join('' if T.get(x, '') == '_' else T.get(x, '').replace('~', '') for x in toks)), ref[r]); n += len(ref[r])
    return 1 - d / n
def report(T):
    n = sum(len(v) for v in runs.values()); k = sum(1 for v in runs.values() for x in v if x in T)
    rnd = random.Random(11); ks = list(T); ctl = []
    for _ in range(200):
        vs = [T[x] for x in ks]; rnd.shuffle(vs); ctl.append(score(dict(zip(ks, vs))))
    return {'signs': n, 'with_value': k, 'coverage': round(k / n, 3), 'score': round(score(T), 3),
            'shuffles_200_all_labels_best': round(max(ctl), 3)}
T = json.load(open(os.path.join(D, 'table_1448.json'), encoding='utf8'))['table']
R = {}
for ln in open(os.path.join(here, 'key_R5318_by_1448_label.tsv'), encoding='utf8'):
    if ln.startswith('#') or not ln.strip(): continue
    lab, val, conf, _ = ln.rstrip('\n').split('\t'); R[lab] = val.split('|')[0].replace('~', '')
EXTRA = {'@N20': 'rederagona', '@N04': 'fiorini', '@N03': 'pe', '@N15': 'm', '@N21': 'lu', '@N13': 'su', '@N33': 'x', '@N34': 'p',
         '@N08': 'ga', '@N23': 'ge', '@N12': 'z', '@N02': 'le', '@N16': 'i', '@N25': 'a', '@N07': 'me', '@N19': 'pu', 'NON': 'non'}
out = {'1448_table': report(T), 'R5318_contributor_crosswalk': report(R)}
R2 = dict(R); R2['VEN'] = 'venetiani'; out['R5318_with_bar-o-bar-o_as_venetiani'] = report(R2)
RS = dict(R); RS.update(EXTRA); out['R5318_plus_17_shape_matches'] = report(RS)
RS2 = dict(RS); RS2['VEN'] = 'venetiani'; out['R5318_plus_17_with_venetiani'] = report(RS2)
TS = dict(T); TS.update(EXTRA); out['1448_table_plus_17_R5318_values'] = report(TS)
out['uses_on_f30_of_the_17'] = {k: sum(v.count(k) for v in runs.values()) for k in EXTRA}
print(json.dumps(out, ensure_ascii=False, indent=1))
