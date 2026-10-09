"""Crib fit: best code sequence for a line's first-pass tokens whose values spell a given Italian text.

Text: letters are matched exactly (lm 'early' normalisation, spaces ignored); '…' or '...' or '[...]' is a gap that any
tokens may fill (scored by channel + prior only); '*' is a one-token wildcard. Each token's cost is its channel
log-prob + BETA * prior; tokens may also be skipped (SKIP). Reports per token: chosen code, value, channel log-prob.

Library: fit(tokens, text, model) -> (total, [(code or None, lchan, in_gap)])
CLI:     python -I fit.py <page> <line> "<text>"        (tokens from ct_<page>.txt line)
         python -I fit.py - "<tokens>" "<text>"
"""
import sys, os, re, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dec

def pattern(text):
    t = text.replace('[...]', '\x01').replace('...', '\x01').replace('…', '\x01').replace('*', '\x02')
    t = re.sub(r'[\[\]]', '', t)
    out = []
    for ch in t:
        if ch in '\x01\x02': out.append(ch); continue
        n = dec.lm.norm(ch, 'early', spaces=False)
        out.extend(n)
    return out

def fit(toks, text, model, maxlc=None):
    pat = pattern(text); n = len(pat)
    cands = []
    for t in toks:
        cs = [(model.lchan(t, k), k) for k in dec.KEY]
        cands.append(cs)
    INF = -1e18
    # state: (i tokens consumed, j pattern pos, g = 1 if inside a gap at j)
    best = {(0, 0, 0): (0.0, None)}
    # allow starting inside a leading gap
    def closure(i, j, g, s, bp, frontier):
        pass
    import collections
    layer = {(0, 0): (0.0, None)}
    for i, t in enumerate(toks):
        nl = {}
        for (j, gstate), (s, bp) in layer.items():
            # positions reachable without consuming tokens: skip over gap markers (exit a gap)
            js = [j]
            while js[-1] < n and pat[js[-1]] == '\x01': js.append(js[-1] + 1)
            for jj in js:
                ingap = jj > j or (j < n and pat[j] == '\x01')
                # option A: token inside a gap at position j (pattern char at j is a gap marker)
                if j < n and pat[j] == '\x01' and jj == j:
                    for lc, k in cands[i]:
                        sc = s + lc + dec.P['BETA'] * model.lprior[k] - 0.5
                        key = (j, 1)
                        if key not in nl or nl[key][0] < sc: nl[key] = (sc, (bp, (i, k, lc, True)))
                    sc = s - dec.P['SKIP']
                    if (j, 1) not in nl or nl[(j, 1)][0] < sc: nl[(j, 1)] = (sc, (bp, (i, None, 0, True)))
                # option B: token matches pattern starting at jj
                if jj < n and pat[jj] == '\x02':
                    for lc, k in cands[i]:
                        sc = s + lc + dec.P['BETA'] * model.lprior[k]
                        key = (jj + 1, 0)
                        if key not in nl or nl[key][0] < sc: nl[key] = (sc, (bp, (i, k, lc, True)))
                    continue
                for lc, k in cands[i]:
                    v = dec.VAL[k].replace(' ', '')
                    if not v: continue
                    if ''.join(pat[jj:jj + len(v)]) == v:
                        sc = s + lc + dec.P['BETA'] * model.lprior[k]
                        key = (jj + len(v), 0)
                        if key not in nl or nl[key][0] < sc: nl[key] = (sc, (bp, (i, k, lc, False)))
                # skip / null
                for lc, k in cands[i]:
                    if dec.VAL[k] == '':
                        sc = s + lc + dec.P['BETA'] * model.lprior[k]
                        if (jj, 0) not in nl or nl[(jj, 0)][0] < sc: nl[(jj, 0)] = (sc, (bp, (i, k, lc, False)))
                sc = s - dec.P['SKIP']
                if (jj, 0) not in nl or nl[(jj, 0)][0] < sc: nl[(jj, 0)] = (sc, (bp, (i, None, 0, False)))
        layer = nl
    # end: pattern consumed (trailing gaps allowed)
    fin = None
    for (j, g), (s, bp) in layer.items():
        jj = j
        while jj < n and pat[jj] == '\x01': jj += 1
        if jj == n and (fin is None or s > fin[0]): fin = (s, bp)
    if fin is None: return None, []
    s, bp = fin; out = []
    while bp: bp, (i, k, lc, gp) = bp; out.append((k, lc, gp))
    out.reverse()
    return s, out

def show(toks, text, model):
    s, out = fit(toks, text, model)
    if s is None: print('no fit'); return
    print('total %.1f  per token %.2f' % (s, s / len(toks)))
    print('  '.join('%s>%s=%s(%.1f)%s' % (t, k or '-', (dec.VAL[k] or '_') if k else '', lc, '~' if gp else '')
                    for t, (k, lc, gp) in zip(toks, out)))

if __name__ == '__main__':
    model = dec.Model(dec.PAGES)
    if sys.argv[1] == '-':
        toks = sys.argv[2].split(); text = sys.argv[3]
    else:
        lines = dict(dec.load_ct(sys.argv[1])); toks = lines[int(sys.argv[2])]; text = sys.argv[3]
    show(toks, text, model)
