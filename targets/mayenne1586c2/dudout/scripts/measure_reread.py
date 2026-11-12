"""PREREG measure (see PREREG.md). Portion = re-read lines r15-r19, r24-r31, v03-v05 of f. 120.
Tokens: Daniel's convention (to_read.py): letter signs one token, word signs '=word', unvalued '?', polyphone -> first
alternative. Statistic M = share of tokens READ by targets/matignon1586c3/f276/scripts/measure.py (run of >= 3 lexicon
words, >= 10 letters, fr-1600-letters, mincount 20).
Controls: 200 permuted letter keys (measure.py's own control, seeds 1..200) + 200 shuffles of the token order inside
the portion (seeds 1..200). Comparison: Harumi-Matsuba's transcription, same lines, same key, same rule.
usage: measure_reread.py <cyphersolver worktree> <decode_reread.txt> <decode harumi r> <decode harumi v>"""
import sys, re, random, os
wt, mine, hr, hv = sys.argv[1:5]
sys.path.insert(0, os.path.join(wt, 'targets/matignon1586c3/f276/scripts'))
import measure as M
PORTION = {f'r{k:02d}' for k in list(range(15, 20)) + list(range(24, 32))} | {'v03', 'v04', 'v05'}
def toks_from_decode(s):
    s = re.sub(r'\(([^|)]*)\|[^)]*\)', r'\1', s)
    out = []
    for t in s.split():
        if t.startswith('[?'): out.append('?')
        elif t.startswith('='): out.append('=' + t[1:].lower())
        else: out.append(t)
    return out
def mine_lines(p):
    L = []
    for l in open(p, encoding='utf-8'):
        m = re.match(r'^(\w\d\d) (.*)$', l.rstrip('\n'))
        if m and m.group(1) in PORTION: L.append(toks_from_decode(m.group(2)))
    return L
def harumi_lines(p, page):
    L = []
    for l in open(p, encoding='utf-8'):
        m = re.match(r'^c(\d+)\s+(.*)$', l.rstrip('\n'))
        if not m or f'{page}{int(m.group(1)):02d}' not in PORTION: continue
        s = re.sub(r'\(([^|)]*)\|[^)]*\)', r'\1', m.group(2)); s = re.sub(r'\[\?[^\]]*\]', ' ? ', s)
        t = []
        for ch in s.split():
            for run in re.findall(r'[A-Z]+|[a-z]|\?', ch): t.append('?' if run == '?' else ('=' + run.lower() if run.isupper() else run))
        L.append(t)
    return L
LEX, scheme = M.lexicon('fr-1600-letters', 20)
def conv(lines):
    out = []
    for toks in lines:
        r = []
        for t in toks:
            if t.startswith('='): r.append(('w', M.norm(t[1:], scheme)))
            elif t == '?': r.append(('?', ''))
            else:
                v = t.replace('y', 'i'); r.append(('l', v) if v and all(c in M.A for c in v) else ('?', ''))
        out.append(r)
    return out
A_ = conv(mine_lines(mine)); H_ = conv(harumi_lines(hr, 'r') + harumi_lines(hv, 'v'))
nlet = sum(len(v) for l in A_ for k, v in l if k == 'l') + sum(len(v) for l in A_ for k, v in l if k == 'w')
r, n = M.measure(A_, LEX); rh, nh = M.measure(H_, LEX)
print(f'portion: {len(A_)} lines, {n} tokens, {nlet} plaintext letters')
print(f'M re-read  = {r}/{n} = {r/n:.3f}'); print(f'M Harumi   = {rh}/{nh} = {rh/nh:.3f}')
ctl = []
for s in range(1, 201):
    random.seed(s); p = list(M.A); random.shuffle(p); ctl.append(('key', M.measure(A_, LEX, str.maketrans(M.A, ''.join(p)))[0] / n))
flat = [t for l in A_ for t in l]
for s in range(1, 201):
    random.seed(1000 + s); f = flat[:]; random.shuffle(f); ctl.append(('shuf', M.measure([f], LEX)[0] / n))
for kind in ('key', 'shuf'):
    v = sorted(x for k, x in ctl if k == kind); print(f'{kind}: n={len(v)} median {v[len(v)//2]:.3f} p99 {v[int(.99*len(v))-1]:.3f} max {v[-1]:.3f}')
ge = sum(1 for _, x in ctl if x >= r / n); print(f'controls >= M re-read: {ge}/400 ; p = {(ge+1)/401:.4f}')
