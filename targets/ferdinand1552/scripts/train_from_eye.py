"""Add the eye-checked signs of finished letters to the training set (work/train4.pkl = train3 + these).
A sign is taken when its line reads exactly as the reading after the eye edits, and the sign was not merged,
split or inserted; its label is the eye label ('-' = not a sign: stroke, fragment of clear text or gloss).
    python scripts/train_from_eye.py 13oct [18oct ...]"""
import sys, re, pickle, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from transcribe import load_lines, decrypt, toks
P = pickle.load(open(ROOT / 'work/pages.pkl', 'rb'))
base = pickle.load(open(ROOT / 'work/train3.pkl', 'rb'))
add = 0
for L in sys.argv[1:]:
    lines, reading = load_lines(L)
    beam = {}
    for l in open(ROOT / f'work/beam_{L}.tsv', encoding='utf8'):
        f = l.rstrip('\n').split('\t'); beam[f'{f[0]}.{f[1]}'] = ([int(x) for x in f[6].split()], f[3].split())
    eye = {}
    for l in open(ROOT / f'eye_{L}.tsv', encoding='utf8'):
        if l.startswith('#') or not l.strip(): continue
        k, e = l.rstrip('\n').split('\t', 1); eye[k] = e
    for k, (p, j, idx, labs) in lines.items():
        if toks(decrypt(labs).replace('(', '').replace(')', '')) != toks(reading.get(k, '')): continue
        bidx, blabs = beam[k]
        lab = dict(enumerate(blabs)); skip = set()
        for e in eye.get(k, '').split():
            m = re.match(r'^(\d+)\+(\d+)=', e)
            if m: skip.update(range(int(m.group(1)), int(m.group(2)) + 1)); continue
            m = re.match(r'^(\d+)<', e)
            if m: continue
            m = re.match(r'^(\d+)=(.+)$', e)
            if m:
                i, v = int(m.group(1)), m.group(2)
                if ',' in v or v.endswith('?'): skip.add(i)
                else: lab[i] = v
        ss = sorted(P[p][j]['signs'], key=lambda s: s['x0'])
        for n, i in enumerate(bidx):
            if n in skip: continue
            base.append((ss[i]['m'], lab[n])); add += 1
print('added', add, 'total', len(base))
pickle.dump(base, open(ROOT / 'work/train4.pkl', 'wb'))
