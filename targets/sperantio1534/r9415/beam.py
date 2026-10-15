"""Beam decode a KAA 4591 transcription: fixed key + per-sign alternatives, chosen by a lang/ LM over each cipher run."""
import re, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lang import lm
src, keyf, altf, model, dst = sys.argv[1:6]
M = lm.load(model, spaces=False)
KEY = dict((kv[0], kv[2:]) for kv in open(keyf, encoding='utf8').read().strip().split(','))
ALT = {}
for kv in open(altf, encoding='utf8').read().split():
    k, v = kv[0], kv[2:]; ALT[k] = v.split('/')
def opts(c): return ALT.get(c, [KEY.get(c, '?')])
lines = []   # (label, [items]) item = ('clear', text) or ('sig', char)
for l in open(src, encoding='utf8'):
    if l.startswith('=='): lines.append((l.strip(), None)); continue
    m = re.match(r'(\d\d) (.*)', l)
    if not m: continue
    items = []
    for cl, ci in re.findall(r'(\[[^\]]*\])|([^\[\]])', m.group(2)):
        items.append(('clear', cl) if cl else ('sig', ci))
    lines.append((m.group(1), items))
# runs of signs across lines, broken by clear text
runs, cur = [], []
for lab, items in lines:
    if items is None: continue
    for it in items:
        if it[0] == 'clear':
            if cur: runs.append(cur); cur = []
        else: cur.append(it)
if cur: runs.append(cur)
def sc(s): return M.score_idx(M.encode(lm.norm(s, 'latin') if model == 'la' else s)) if s else 0.0
CODE = {'X': '[D.]'} if model == 'la' else {'e': '[F.G.]'}
choice = {}
B = 60
for run in runs:
    beam = [('', [])]
    for it in run:
        c = it[1]
        if c in '?.,': 
            beam = [(t, ch + ['']) for t, ch in beam]; continue
        new = []
        for t, ch in beam:
            for o in opts(c):
                o2 = '' if o in ('_',) else o
                new.append((t + o2, ch + [o]))
        seen = {}
        for t, ch in new:
            s = sc(t[-60:]) + (0 if len(t) <= 60 else 0)
            key = t[-6:]
            if key not in seen or seen[key][0] < s: seen[key] = (s, t, ch)
        best = sorted(seen.values(), key=lambda x: -x[0])[:B]
        beam = [(t, ch) for s, t, ch in best]
    t, ch = beam[0]
    for it, o in zip(run, ch): choice[id(it)] = o
out = []
for lab, items in lines:
    if items is None: out.append(lab); continue
    s = ''.join(it[1] if it[0] == 'clear' else (CODE.get(it[1],'') if choice.get(id(it))=='_' else choice.get(id(it), '')) for it in items)
    out.append(f'{lab} {s}')
open(dst, 'w', encoding='utf8').write('\n'.join(out) + '\n')
print('\n'.join(out))
