"""Vote each transcribed group against NARA OCR of its own frame and of the cable copy."""
import json, re, sys, difflib
sys.stdout.reconfigure(encoding='utf-8')
C = '../../research/nara_reels/cache/'
def roll(naid):
    rec = json.load(open(C + naid + '.rec.json', encoding='utf-8'))
    names = {o['objectId']: o['objectFilename'] for o in rec['digitalObjects']}
    out = {}
    for o in json.load(open(C + naid + '.txt.json', encoding='utf-8')):
        fn = names.get(o['objectId'], '')
        if fn.endswith('.jpg'): out[fn[-8:-4]] = o.get('extractedText') or ''
    return out
R = {'141': roll('27158076'), '114': roll('27133946'), '122': roll('27140577'), '108': roll('27128808')}
T = {}; meta = {}; cur = None
for l in open(sys.argv[1] if len(sys.argv) > 1 else 'transcription_pass1.txt', encoding='utf-8'):
    if l.startswith('#'): continue
    if l.startswith('@'):
        p = l.split(); cur = p[0][1:]; T[cur] = []; meta[cur] = p[1]; continue
    T[cur] += [g for g in l.split() if re.fullmatch(r'\d+', g)]
CAB = {'w763': '0691 0692 0693 0694 0695', 'w752': '0700 0701', 'w749': '0723 0724', 'w735': '0725', 'w746': '0726 0727',
       'w765': '0747 0748 0749 0750 0751 0752 0753', 'w2635': '0512 0513', 'w512': '0513 0514', 'w513': '0514 0515',
       'w791': '0705 0706 0707 0708 0709', 'w769': '0697 0698 0699', 'w716': '0699 0700', 'w592': '0722 0723'}
tok = lambda t: re.findall(r'\d{2,7}', t)
for t, g in T.items():
    r, fr = meta[t].split('-')
    frames = fr.split('+')
    own = []
    for f in frames: own += tok(R[r].get(f, ''))
    cab = []
    for f in CAB.get(t, '').split(): cab += tok(R['108'].get(f, ''))
    bad = []
    for i, x in enumerate(g):
        a, b = x in own, x in cab
        if not a or (CAB.get(t) and not b):
            bad.append(f'{i}:{x}[{"O" if a else "-"}{"C" if b else "-"}]')
    print(f'{t} n={len(g)} own-ocr {sum(x in own for x in g)} cable-ocr {sum(x in cab for x in g)}')
    print('   ', ' '.join(bad))
