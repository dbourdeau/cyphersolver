#!/usr/bin/env python3
"""Monotone alignment of code groups to the words of the interlined decipherment, despatch by despatch,
with a shared group->word table learned by repeated passes (hard EM, leave-one-despatch-out counts).
Uses the crib despatches only (FILES in corpus.py); No. 35 is not read here."""
import re, sys, json, math
from collections import Counter, defaultdict
from corpus import FILES, load

def norm(w):
    w = w.lower().replace('’', "'")
    w = re.sub(r"'s$", '', w)
    w = w.strip("'")
    return w
def stem(w):
    w = norm(w)
    for suf in ('ing', 'ed', 'es', 's', 'ly', 'd'):
        if len(w) > len(suf) + 3 and w.endswith(suf):
            return w[:-len(suf)]
    return w
def same(a, b):
    if a == b: return True
    sa, sb = stem(a), stem(b)
    if sa == sb: return True
    if len(sa) >= 5 and len(sb) >= 5 and (sa.startswith(sb[:5]) and abs(len(sa)-len(sb)) <= 3): return True
    return False

def build():
    D = []
    for f in FILES:
        d = load(f)
        G = []; W = []
        for li, l in enumerate(d['lines']):
            for n, u in zip(l['f'], l['ul']): G.append((n, li, u))
            for w in l['g']: W.append((norm(w), li))
        D.append({'file': f, 'head': d['head'], 'G': G, 'W': W, 'nl': len(d['lines'])})
    return D

def align(d, T, lam_line=0.0, lam_diag=0.0):
    """T: dict group -> Counter(words) (excluding this despatch). Returns list of (gi, wi or None) and list of unmatched words."""
    G, W = d['G'], d['W']; I, J = len(G), len(W)
    NEG = -1e9
    S = [[NEG]*(J+1) for _ in range(I+1)]; B = [[None]*(J+1) for _ in range(I+1)]
    S[0][0] = 0
    def msc(i, j):
        g, gl, ul = G[i]; w, wl = W[j]
        t = T.get(g)
        s = 0.0
        if t:
            tot = sum(t.values()); c = sum(v for k, v in t.items() if same(k, w))
            if c: s += 2.0 + 1.5*math.log(1+c) + (1.0 if c == tot else 0)
            else:
                top = max(t.values())
                s -= 1.0 + 1.2*math.log(1+top)
        s -= lam_line * max(0, abs(gl - wl) - 0)
        s -= lam_diag * abs((i+0.5)/I - (j+0.5)/J) * 20
        if ul: s -= 2.0
        return s + 0.3
    for i in range(I+1):
        for j in range(J+1):
            cur = S[i][j]
            if cur <= NEG/2: continue
            if i < I and j < J:
                v = cur + msc(i, j)
                if v > S[i+1][j+1]: S[i+1][j+1] = v; B[i+1][j+1] = 'M'
            if i < I:  # group with no word of its own (null, or second part of a word)
                g, gl, ul = G[i]
                v = cur - (0.2 if ul else 0.9)
                if v > S[i+1][j]: S[i+1][j] = v; B[i+1][j] = 'G'
            if j < J:  # word with no group of its own (part of a phrase group)
                v = cur - 1.1
                if v > S[i][j+1]: S[i][j+1] = v; B[i][j+1] = 'W'
    i, j = I, J; out = []
    while i or j:
        b = B[i][j]
        if b == 'M': out.append(('M', i-1, j-1)); i -= 1; j -= 1
        elif b == 'G': out.append(('G', i-1, None)); i -= 1
        else: out.append(('W', None, j-1)); j -= 1
    out.reverse()
    return out, S[I][J]

def table(D, A, skip=None):
    T = defaultdict(Counter)
    for k, d in enumerate(D):
        if k == skip: continue
        for op, i, j in A[k]:
            if op == 'M': T[d['G'][i][0]][d['W'][j][0]] += 1
    return T

def run(D, iters=12, verbose=True):
    A = [None]*len(D)
    # pass 0: positions only. line-local prior where a despatch tracks its lines, diagonal prior otherwise
    for k, d in enumerate(D):
        A[k], _ = align(d, {}, lam_line=d['lam_line'], lam_diag=d['lam_diag'])
    for it in range(iters):
        changed = 0
        decay = max(0.0, 1 - it/6.0)
        for k, d in enumerate(D):
            T = table(D, A, skip=k)
            new, sc = align(d, T, lam_line=d['lam_line']*max(decay, 0.25), lam_diag=d['lam_diag']*max(decay, 0.25))
            if new != A[k]: changed += 1
            A[k] = new
        if verbose: print('iter', it, 'changed', changed, file=sys.stderr)
        if not changed: break
    return A

def classify(D):
    # despatches in the clerk's hand track line by line; Grantham's own hand runs ahead
    for d in D:
        d['lam_line'] = 0.8; d['lam_diag'] = 0.0
    return D

if __name__ == '__main__':
    D = classify(build())
    local = set(sys.argv[1].split(',')) if len(sys.argv) > 1 else set()
    for d in D:
        key = d['file']
        if any(x in key for x in ('ff132', 'ff185', 'ff219', 'No33', 'No34', 'n36')):
            d['lam_line'] = 0.0; d['lam_diag'] = 1.0
    A = run(D)
    T = table(D, A)
    json.dump({'A': A, 'files': [d['file'] for d in D]}, open('align_out.json', 'w'))
    # report consistency
    multi = {g: t for g, t in T.items() if sum(t.values()) >= 2}
    agree = sum(1 for g, t in multi.items() if max(sum(v for k2, v in t.items() if same(k2, k)) for k in t) >= 2)
    print('groups aligned to a word:', len(T), ' with >=2 aligned occurrences:', len(multi), ' of which some word repeats:', agree)
    tot = sum(sum(t.values()) for t in multi.values()); top = sum(max(sum(v for k2, v in t.items() if same(k2, k)) for k in t) for t in multi.values())
    print('token consistency among repeated groups: %d/%d = %.2f' % (top, tot, top/tot))
    for g, t in sorted(T.items(), key=lambda x: -sum(x[1].values()))[:60]:
        print(g, dict(t.most_common(6)))
