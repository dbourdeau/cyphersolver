# Look-alike sign pairs of the 1520-21 cipher (3 Oct 2026): c / CE / e, QB / 8, AMP / EL, x / xp.
# For every occurrence in R1136 (r1136_pass4.txt), R1139 (r1139_pass4.txt), V1920 and R1138 (caprile1521_transcription.txt)
# and V1921 (as in caprile1521_transcription.txt), each sign of a pair is given the UNION of the pair's candidate values
# (no preference), the beam decoder (beam21.py, it-cinquecento order 5) chooses a letter per occurrence, and the choices
# are tabulated per sign label. A split between two labels is accepted only if their chosen-value distributions differ
# consistently (the majority value of one is rare for the other). V1920 and R1138 also have Somogyi's plaintext, so for
# them the EM counts (key21_counts.json) are shown beside the LM choice.
# Run: python lookalike21.py
import os, sys, math, json, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import beam21
from lang import lm

PAIRS = {'c/CE/e': ['c', 'CE', 'e'], 'QB/8': ['QB', '8'], 'AMP/EL': ['AMP', 'EL'], 'x/xp': ['x', 'XQ']}
UNION = {'c/CE/e': ['o', 'c', 'e'], 'QB/8': ['o', 'e', 't', 'd'], 'AMP/EL': ['p', 'f', 'd'], 'x/xp': ['r', 'q']}   # no null: these are letter signs

def decode_track(toks, m, P):
    A = m.A; k = m.order; idx = m.index; letters = [c for c in m.alpha if c != ' ']
    beams = {(): (0.0, ())}
    for t in toks:
        if t in ('|',): cand = {'': 0.0}
        elif t == '#': cand = {c: -3.0 for c in letters}
        else:
            cand = dict(P.get(t, {}))
            for c in letters:
                if c not in cand: cand[c] = beam21.OFFKEY
        nb = {}
        for ctx, (sc, ch) in beams.items():
            for v, pv in cand.items():
                s2 = sc + pv; c2 = ctx
                for x in v:
                    i = idx[x]
                    if len(c2) == k - 1:
                        f = 0
                        for y in c2: f = f * A + y
                        s2 += float(m.lp[f * A + i])
                    c2 = (c2 + (i,))[-(k - 1):]
                if c2 not in nb or nb[c2][0] < s2: nb[c2] = (s2, ch + ((t, v),))
        beams = dict(sorted(nb.items(), key=lambda kv: -kv[1][0])[:1500])
    return max(beams.values())[1]

def main():
    m = lm.load('it-cinquecento', spaces=False)
    P = beam21.priors()
    for pair, labs in PAIRS.items():
        for l in labs:
            P[l] = {v: math.log(1 / len(UNION[pair])) for v in UNION[pair]}
    srcs = [('R1136', 'r1136_pass4.txt'), ('R1139', 'r1139_pass4.txt'), ('V1920', 'caprile1521_transcription.txt'),
            ('R1138', 'caprile1521_transcription.txt'), ('V1921', 'caprile1521_transcription.txt')]
    tab = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
    for src, fn in srcs:
        for line in open(os.path.join(HERE, fn), encoding='utf8'):
            if not line.startswith(src + ' '): continue
            toks = beam21.tokens(line)
            for t, v in decode_track(toks, m, P):
                for pair, labs in PAIRS.items():
                    if t in labs: tab[pair][t][v or 'null'] += 1; tab[pair][t]['_' + src] += 1
    C = json.load(open(os.path.join(HERE, 'key21_counts.json'), encoding='utf8'))
    out = {}
    for pair, labs in PAIRS.items():
        print('==', pair)
        for l in labs:
            c = tab[pair][l]
            vals = {k: v for k, v in c.items() if not k.startswith('_')}
            srcn = {k[1:]: v for k, v in c.items() if k.startswith('_')}
            print(f'  {l:4s} LM choices {dict(collections.Counter(vals).most_common())}  occurrences {srcn}  EM(Somogyi) {C.get(l, {})}')
            out[f'{pair}:{l}'] = vals
    json.dump(out, open(os.path.join(HERE, 'lookalike21.json'), 'w'), indent=1)

if __name__ == '__main__':
    main()
