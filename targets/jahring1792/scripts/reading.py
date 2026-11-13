"""Build transcription_*.txt, reading_*.md and the word counts from runs.json."""
import json, re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from decrypt import HERE

def resolve(r):
    r = re.sub(r'\{[a-z]/([a-z])\}', r'\1', r)
    r = re.sub(r'\{\+([a-z])\}', r'\1', r)
    r = re.sub(r'\[\.\.\.\|[a-z]+\]', '[...]', r)
    r = re.sub(r'\[\?([^|\]]*)\|[a-z]+\]', r'[?\1]', r)
    return r

def count(r):
    v = rep = hole = 0
    for w in r.split():
        if w.startswith('[...'): hole += 1
        elif '{' in w or w.startswith('[?'): rep += 1
        else: v += 1
    return v, rep, hole

REVIEWED = {
    '119': '# corrected 13 Nov 2026 after the blind review, from the image: 119.5 letter 7 q -> g; 119.13 letter 13 q -> g\n',
    '120': '# corrected 13 Nov 2026 after the blind review, from the image: 120.1 letter 57 q -> g; 120.2 letter 15 q -> y; 120.3 letter 51 q -> g\n',
}
rows = json.load(open(HERE / 'runs.json', encoding='utf8'))
tot = {}
for doc in ('119', '120'):
    rr = [r for r in rows if r[0] == doc]
    with open(HERE / f'transcription_{doc}.txt', 'w', encoding='utf8') as f:
        f.write('# reconciled transcription (pass 1 and pass 2 settled on the image); signs per SIGN_CONVENTIONS.md\n')
        f.write(REVIEWED[doc])
        f.write('# run\tsigns\n')
        for r in rr: f.write(f'{r[1]}\t{r[2]}\n')
    V = R = H = 0
    for r in rr:
        v, rep, h = count(r[3]); V += v; R += rep; H += h
        print(doc, r[1], v, rep, h)
    tot[doc] = (V, R, H)
    print(doc, 'verbatim', V, 'marked repair', R, 'hole', H, 'total', V + R + H)
json.dump(tot, open(HERE / 'work_counts.json', 'w'), indent=1)
for r in rows: print(r[1], '|', resolve(r[3]))
