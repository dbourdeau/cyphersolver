"""Find each telegram in the OCR of the Christiania cable copies (M367 roll 108) and list the disagreements."""
import json, re, sys, difflib
sys.stdout.reconfigure(encoding='utf-8')
C = '../../research/nara_reels/cache/'
rec = json.load(open(C + '27128808.rec.json', encoding='utf-8'))
names = {o['objectId']: o['objectFilename'] for o in rec['digitalObjects']}
frames = {}
for o in json.load(open(C + '27128808.txt.json', encoding='utf-8')):
    fn = names.get(o['objectId'], '')
    if fn.endswith('.jpg'):
        frames[fn[-8:-4]] = o.get('extractedText') or ''
T = {}; cur = None
src = sys.argv[1] if len(sys.argv) > 1 else 'transcription_pass1.txt'
for l in open(src, encoding='utf-8'):
    if l.startswith('#'): continue
    if l.startswith('@'):
        cur = l.split()[0][1:]; T[cur] = []; continue
    T[cur] += [g for g in l.split() if re.fullmatch(r'\d+', g)]
for t, g in T.items():
    gs = set(x for x in g if len(x) >= 4)
    hits = []
    for f, txt in frames.items():
        tk = re.findall(r'\d{3,6}', txt)
        n = sum(x in gs for x in set(tk))
        if n >= max(4, len(gs) // 12):
            hits.append((f, n))
    print(f'{t:6s} n={len(g):3d} frames {hits}')
    if hits:
        stream = []
        for f, _ in sorted(hits):
            stream += re.findall(r'\d{3,6}', frames[f])
        sm = difflib.SequenceMatcher(None, g, stream, autojunk=False)
        same = sum(b.size for b in sm.get_matching_blocks())
        print(f'       matched {same}/{len(g)}')
        for op, a, b, c, d in sm.get_opcodes():
            if op != 'equal' and (b - a) <= 6 and (d - c) <= 6:
                print('       ', op, g[a:b], '<>', stream[c:d])
