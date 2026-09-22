"""Exact order-5 Viterbi over per-sign alternatives (alt2.txt), de-1500s no-spaces. Writes raw decrypt + per-sign choices.
usage: python beam2.py transcription_v2.txt alt2.txt out.txt"""
import re, sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm
src, altf, dst = sys.argv[1:4]
M = lm.load('de-1500s', spaces=False); A = M.A; K = M.order; idx = M.index; lp = M.lp
ALT = {}
for kv in open(altf, encoding='utf8').read().split():
    k, v = kv[0], kv[2:]; ALT[k] = v.split('/')
ALT['0'] = ['n']
def cond(ctx, ch):   # ctx: tuple of K-1 idx
    j = 0
    for c in ctx: j = j * A + c
    return lp[j * A + ch]
lines = []
for l in open(src, encoding='utf8'):
    if l.startswith('=='): lines.append((l.strip(), None)); continue
    m = re.match(r'(\d\d) (.*)', l)
    if not m: continue
    s = re.sub(r'\{-\}', '', m.group(2)); s = re.sub(r'\{[^}]*\}', '?', s).replace('o/', '0')
    items = []; i = 0
    while i < len(s):
        if s[i] == '[':
            j = s.index(']', i); items.append(('clear', s[i:j+1])); i = j + 1
        else:
            items.append(('sig', s[i])); i += 1
    lines.append((m.group(1), items))
# runs, broken by clear text or code e
runs, cur, lastclear = [], [], 'undden'
def flush():
    global cur
    if cur: runs.append((lastclear, cur)); cur = []
for lab, items in lines:
    if items is None: continue
    for it in items:
        if it[0] == 'clear' or it[1] == 'e':
            flush(); lastclear = lm.norm(it[1], 'early', spaces=False) if it[0]=='clear' else 'furstengnaden'
            if len(lastclear) < 4: lastclear = ('undden' + lastclear)
        else: cur.append(it)
flush()
choice = {}
BW = 400
for pre, run in runs:
    ctx0 = tuple(idx[c] for c in pre[-(K-1):])
    states = {ctx0: (0.0, None)}   # ctx -> (score, (prevctx, choice, prevnode))
    hist = []
    for it in run:
        c = it[1]
        opts = ALT.get(c)
        if not opts or opts==['_']: hist.append(None); continue
        new = {}
        for ctx, (sc, bp) in states.items():
            for o in opts:
                ch = idx[o]; s2 = sc + cond(ctx, ch); n2 = ctx[1:] + (ch,)
                if n2 not in new or new[n2][0] < s2: new[n2] = (s2, (ctx, o))
        best = sorted(new.items(), key=lambda kv: -kv[1][0])[:BW]
        states = dict((k, v) for k, v in best)
        hist.append(states)
    # backtrack
    if not states: continue
    ctx = max(states, key=lambda k: states[k][0])
    picks = []
    for h in reversed(hist):
        if h is None: picks.append(None); continue
        sc, (pctx, o) = h[ctx]; picks.append(o); ctx = pctx
    picks.reverse()
    for it, o in zip(run, picks): choice[id(it)] = o
out = []
for lab, items in lines:
    if items is None: out.append(lab); continue
    s = ''
    for it in items:
        if it[0] == 'clear': s += it[1]
        elif it[1] == 'e': s += '[F.G.]'
        else: s += choice.get(id(it)) or '?'
    out.append(f'{lab} {s}')
open(dst, 'w', encoding='utf8').write('\n'.join(out) + '\n')
