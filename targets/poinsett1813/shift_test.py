"""Test whether Poinsett's groups are a known US code (JQA/Department, Armstrong THE=972, Pinckney legation,
1788 legation, Jefferson 1787) under a constant shift g -> g+k (also mod 1600/1700). Scores the decoded value
stream with the shared en-modern 4-gram model (no spaces); reports the best k per table against the spread."""
import re, json, sys, statistics
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lang import lm
R = Path(__file__).resolve().parents[1]
M = lm.load('en-modern', order=4, spaces=False)

def tokens():
    out = []
    for l in open(Path(__file__).with_name('transcription.tsv'), encoding='utf8'):
        if l.startswith(('#', 'passage')): continue
        for t in l.split('\t')[3].split():
            m = re.match(r'(\d+)', t)
            if m: out.append(int(m.group(1)))
    return out

def tsv(p, ki, vi):
    d = {}
    for l in open(R / p, encoding='utf8'):
        if l.startswith('#'): continue
        c = l.rstrip('\n').split('\t')
        if len(c) > max(ki, vi) and c[ki].strip().isdigit():
            v = re.sub(r'[^a-z]', '', c[vi].lower().split('/')[0])
            if v: d.setdefault(int(c[ki]), v)
    return d

T = {'jqa': tsv('jqa/code_table.tsv', 0, 1), 'pinckney': tsv('erving1807aug/key_pinckney.tsv', 0, 1),
     'legation1788': tsv('legation1788/key.tsv', 1, 2), 'pinckney1793': tsv('pinckney1793/key.tsv', 1, 2),  # Codes No. 10 and No. 16, one file until 11 Nov 2026
     'jefferson1787': tsv('jefferson1787/key.tsv', 0, 1)}
a = json.load(open(R / 'armstrong/code972_partial.json'))
T['armstrong'] = {int(k): re.sub(r'[^a-z]', '', v[0].lower()) for k, v in a.items() if re.sub(r'[^a-z]', '', v[0].lower())}

ct = tokens()
for name, d in T.items():
    res = []
    for mod in (None, 1600, 1700):
        for k in range(-1700, 1701):
            dec = []
            for g in ct:
                h = g + k if mod is None else (g + k - 1) % mod + 1
                if h in d: dec.append(d[h])
            if len(dec) < 0.3 * len(ct): continue
            s = ''.join(dec)
            res.append((M.per_char(s), len(dec) / len(ct), k, mod, ' '.join(dec[:25])))
    sc = [r[0] for r in res]
    mu, sd = statistics.mean(sc), statistics.pstdev(sc)
    res.sort(key=lambda r: -r[0])
    print(f'== {name}: {len(res)} settings, mean {mu:.3f} sd {sd:.3f}')
    for r in res[:3]:
        print(f'  z={(r[0]-mu)/sd:5.2f} score={r[0]:.3f} cov={r[1]:.2f} k={r[2]} mod={r[3]} | {r[4]}')
