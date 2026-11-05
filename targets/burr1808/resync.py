"""Find where the key phase slips (a number missed, added or misread) in each section.
Viterbi over words: each word takes a phase; staying in step costs 0, a slip costs PEN."""
import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parents[2]))
from lang import lm
import decrypt as D

M = lm.load('en-modern')
PEN = 12.0

def dec(w, p):
    return ''.join(chr(97 + (n - 1 - D.SHIFTS[(p + j) % 6]) % 26) for j, n in enumerate(w))

def wscore(s):
    return M.score(' ' + s + ' ') - M.score(' ')

secs = D.parse()
for sec, lines in secs.items():
    W = [w for _, ws in lines for w in ws]
    # state: phase at start of word
    best = {p: (0.0 if p == 0 else -PEN, [p]) for p in range(6)}
    for i, w in enumerate(W):
        new = {}
        for p in range(6):
            sc = wscore(dec(w, p))
            cands = []
            for q, (v, path) in best.items():
                exp = (q + len(W[i - 1])) % 6 if i else 0
                cost = 0 if p == (exp if i else q) else PEN
                cands.append((v - cost + sc, path))
            v, path = max(cands, key=lambda t: t[0])
            new[p] = (v, path + [p] if i else [p])
        best = new
    v, path = max(best.values(), key=lambda t: t[0])
    path = path[-len(W):]
    out = []
    for i, w in enumerate(W):
        exp = (path[i - 1] + len(W[i - 1])) % 6 if i else path[0]
        mark = '' if path[i] == exp else f'<<slip {(path[i]-exp)%6} at word {i}>>'
        out.append(mark + dec(w, path[i]))
    print(sec, ' '.join(out), '\n')
